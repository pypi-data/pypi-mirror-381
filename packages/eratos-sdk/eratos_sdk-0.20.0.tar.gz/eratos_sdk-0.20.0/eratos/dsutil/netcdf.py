import copy
import logging
import os
import bisect

import numpy as np
from contextlib import contextmanager
from functools import reduce
from typing import Optional

from netCDF4 import Dataset, num2date
from sortedcontainers import SortedList

_logger = logging.getLogger(__name__)

_DEFAULT_FILL = {
    "f4": float(np.finfo(np.float32).min),
    "f8": float(np.finfo(np.float64).min),
    "i1": np.iinfo(np.int8).min,
    "i2": np.iinfo(np.int16).min,
    "i4": np.iinfo(np.int32).min,
    "i8": np.iinfo(np.int32).min,
    "u1": np.iinfo(np.uint8).max,
    "u2": np.iinfo(np.uint16).max,
    "u4": np.iinfo(np.uint32).max,
    "u8": np.iinfo(np.uint32).max,
    "c4": float(np.finfo(np.complex64).min),
    "c8": float(np.finfo(np.complex128).min),
}
_MAX_FLOAT64_PRECISION = 2**53 - 1

@contextmanager
def managed_netcdf(*args, **kwds):
    # Code to acquire resource, e.g.:
    dataset = Dataset(*args, **kwds)
    try:
        yield dataset
    finally:
        dataset.close()


def get_netcdf_variable_data(path, varname):
    with managed_netcdf(path, 'r') as nc:
        return nc[varname][:]


def pipe_netcdf_attrs(dstPath, srcPath, excludeDims=[]):
    with managed_netcdf(srcPath, 'r') as src:
        if not os.path.exists(dstPath):
            with managed_netcdf(dstPath, 'w', format='NETCDF4') as dst:
                _pipe_netcdf_attrs(dst, src, excludeDims=excludeDims)
        else:
            with managed_netcdf(dstPath, 'a', format='NETCDF4') as dst:
                _pipe_netcdf_attrs(dst, src, excludeDims=excludeDims)


def pipe_netcdf_var_attr(dstPath, srcPath, vars, **kwargs):
    with managed_netcdf(srcPath, 'r') as src:
        if not os.path.exists(dstPath):
            with managed_netcdf(dstPath, 'w', format='NETCDF4') as dst:
                _pipe_netcdf_var_attr(dst, src, vars, **kwargs)
        else:
            with managed_netcdf(dstPath, 'a', format='NETCDF4') as dst:
                _pipe_netcdf_var_attr(dst, src, vars, **kwargs)


def pipe_netcdf_vars(dstPath, srcPath, vars, **kwargs):
    with managed_netcdf(srcPath, 'r') as src:
        if not os.path.exists(dstPath):
            with managed_netcdf(dstPath, 'w', format='NETCDF4') as dst:
                _pipe_netcdf_vars(dst, src, vars, **kwargs)
        else:
            with managed_netcdf(dstPath, 'a', format='NETCDF4') as dst:
                _pipe_netcdf_vars(dst, src, vars, **kwargs)


def _pipe_netcdf_attrs(dst, src, excludeDims=[]):
    for name in src.ncattrs():
        dst.setncattr(name, getattr(src, name))
    for k in src.dimensions:
        if k in dst.dimensions or k in excludeDims:
            continue
        dst.createDimension(k, size=src.dimensions[k].size)


def get_netcdf_var_fill_val(srcPath, varName):
    with managed_netcdf(srcPath, 'r') as nc:
        return nc[varName]._FillValue


def _add_variable_attr(args, var, key, srcKey=None):
    try:
        if srcKey is None:
            args[key] = var.getncattr(key)
        else:
            args[key] = var.getncattr(srcKey)
        return args
    except AttributeError as e:
        return args


def _calc_num_chunks(size, chunkSize):
    cnt = size // chunkSize
    if size % chunkSize != 0:
        cnt += 1
    return cnt


def _calc_strides(arr):
    return list([reduce(lambda a, b: a * b, arr[i + 1:], 1) for i in range(len(arr))])


def _pipe_netcdf_var_data(dst, src, var, chunkSize):
    if dst[var].ndim != src[var].ndim:
        raise ValueError('dst dimensions does not match src dimensions')
    if dst[var].ndim != len(chunkSize):
        raise ValueError('dst dimensions does not match chunkSize dimensions')
    for i in range(dst[var].ndim):
        if dst[var].shape[i] != src[var].shape[i]:
            raise ValueError('dst dimensions does not match src dimensions')
    numChunks = list([_calc_num_chunks(dst[var].shape[i], chunkSize[i]) for i in range(dst[var].ndim)])
    chunkStrides = _calc_strides(numChunks)
    totalChunks = reduce(lambda a, b: a * b, numChunks, 1)
    for i in range(totalChunks):
        chunkIndex = list([(i // chunkStrides[n]) % numChunks[n] for n in range(dst[var].ndim)])
        dimStarts = list([chunkSize[n] * chunkIndex[n] for n in range(dst[var].ndim)])
        dimEnds = list([min(chunkSize[n] * (chunkIndex[n] + 1), dst[var].shape[n]) for n in range(dst[var].ndim)])
        dataSlice = tuple([slice(dimStarts[n], dimEnds[n], None) for n in range(dst[var].ndim)])
        data = src[var][dataSlice]
        dst[var][dataSlice] = data


def _pipe_netcdf_var_attr(dst, src, vars, **kwargs):
    for vname in vars:
        vdef = src.variables[vname]
        for aname in vdef.ncattrs():
            if aname in ['_FillValue', 'compression', 'zlib']:
                continue
            dst.variables[vname].setncattr(aname, getattr(vdef, aname))


def _pipe_netcdf_vars(dst, src, vars, **kwargs):
    for vname in vars:
        vdef = src.variables[vname]
        chunkszs = []
        if 'chunksizes' in kwargs:
            for i in range(len(kwargs['chunksizes'])):
                if kwargs['chunksizes'][i] is None:
                    chunkszs += [vdef.shape[i]]
                else:
                    chunkszs += [kwargs['chunksizes'][i]]
        if vname not in dst.variables:
            vargs = {}
            vargs = _add_variable_attr(vargs, vdef, 'compression')
            vargs = _add_variable_attr(vargs, vdef, 'zlib')
            vargs = _add_variable_attr(vargs, vdef, 'shuffle')
            vargs = _add_variable_attr(vargs, vdef, 'szip_coding')
            vargs = _add_variable_attr(vargs, vdef, 'szip_pixels_per_block')
            vargs = _add_variable_attr(vargs, vdef, 'blosc_shuffle')
            vargs = _add_variable_attr(vargs, vdef, 'fletcher32')
            vargs = _add_variable_attr(vargs, vdef, 'contiguous')
            vargs = _add_variable_attr(vargs, vdef, 'chunksizes')
            vargs = _add_variable_attr(vargs, vdef, 'endian')
            vargs = _add_variable_attr(vargs, vdef, 'least_significant_digit')
            vargs = _add_variable_attr(vargs, vdef, 'fill_value', srcKey='_FillValue')
            vargs = _add_variable_attr(vargs, vdef, 'chunk_cache')
            for k in kwargs.keys():
                vargs[k] = kwargs[k]
            if 'chunksizes' in kwargs:
                vargs['chunksizes'] = tuple(chunkszs)
            dst.createVariable(vname, vdef.datatype, dimensions=vdef.dimensions, **vargs)
        for aname in vdef.ncattrs():
            if aname in ['_FillValue', 'compression', 'zlib']:
                continue
            dst.variables[vname].setncattr(aname, getattr(vdef, aname))
        if 'chunksizes' not in kwargs:
            dst[vname][:] = src[vname][:]
        else:
            _pipe_netcdf_var_data(dst, src, vname, chunkSize=chunkszs)
    try:
        for vname in dst.varaibles.keys():
            if vname not in vars:
                raise Exception(f'unknown variable in dst {vname}')
    except AttributeError as e:
        pass


def calculate_netcdf_cf_units_scaling(units):

    # NOTE: the CF convention units

    # udunitDate     = period SINCE reference_date
    # period         = "millisec" | "msec" | "second" | "sec" | "s" | "minute" | "min" | "hour" | "hr" | "day" |
    #                  "week" | "month" | "mon" | "year" | "yr"
    # period         = period + "s" (plural form)
    # reference_date = iso8601 formatted date as described below
    # SINCE          = literal (case insensitive)
    # where
    #
    # msec = millisec = seconds / 1000
    # UDUNITS defines the periods as fixed multiples of seconds. The non-obvious ones are:
    #
    # day = 86400.0 seconds
    # week = 7 days = 604800.0 seconds
    # year = 3.15569259747E7 seconds (365 days of length 86400.0 seconds)
    # month = year/12 = 2629743.831225 seconds

    # http://cfconventions.org/Data/cf-conventions/cf-conventions-1.10/cf-conventions.html

    # https://docs.unidata.ucar.edu/netcdf-java/current/userguide/cdm_calendar_date_time_ref.html
    iso_8601_calendar = "proleptic_gregorian"
    unix_epoch_units = 'seconds since 1970-01-01 00:00:00Z'

    # the cftime datetime of the unix epoch.
    unix_epoch = num2date(0, units=unix_epoch_units, calendar=iso_8601_calendar, only_use_cftime_datetimes=True, has_year_zero=True)

    # the datetime representing the iso8601 datetime contained in the units using the proleptic_gregorian calendar
    units_epoch = num2date(0, units=units, calendar=iso_8601_calendar, only_use_cftime_datetimes=True, has_year_zero=True)

    # 1 unit in the future (proleptic_gregorian calendar)
    units_epoch_time_step = num2date(1, units=units, calendar=iso_8601_calendar, only_use_cftime_datetimes=True, has_year_zero=True)

    unix_timestamp_scale = (units_epoch_time_step - units_epoch).total_seconds()

    unix_timestamp_offset = (units_epoch - unix_epoch).total_seconds()

    return unix_timestamp_scale, unix_timestamp_offset


def varfn_time_netcdf_from_units(vname, file, timeKey='time'):
    if vname != timeKey:
        return {}

    with managed_netcdf(file, 'r') as ds:
        scale, offset = calculate_netcdf_cf_units_scaling(ds[vname].units)
    return {
        'valueScale': scale,
        'valueOffset': offset,
    }


class GriddedConnectorPropertiesBuilder:
    """A builder class for creating gridded connector properties from NetCDF files.

    This class processes NetCDF files to extract dimensions, spaces, and variables
    information, building connector properties that can be used for data access.
    It supports handling time-based unlimited dimensions and can merge with existing
    properties for incremental building. It doesn't support slicing by any dimension other
    than the specified unlimited dimension, typically time.

    When the unlimited dimension coordinate is not provided files are processed in the
    order they are provided, the class assumes the time dimension is monotonicaly increasing.
    Additional files may be added (appended) as slices and the last slice can be replaced with
    a different size. This is useful for acumulating time series data in chunks where each slice
    has more than one time step.

    When the unlimited dimension coordinate IS provided, the builder can insert new files within
    the unlimited coordinate. The allows for patching missing time slices and back filling time series.

    Args:
        unlimited_dimension (str): Name of the unlimited dimension, defaults to 'time'.
        existing_properties (dict, optional): Existing connector properties to merge with.
        existing_unlimited_dim_coords (array-like, optional): Existing coordinates for
            the unlimited dimension, must be monotonically increasing. If coordinates are not
            provided, inserting files in the unlimited dimension is not supported.

    Raises:
        ValueError: If existing_unlimited_dim_coords are not monotonically increasing.

    Examples:
        Basic usage with a single NetCDF file::

            >>> builder = GriddedConnectorPropertiesBuilder()
            >>> builder.parse_netcdf_props('file1.nc', '/path/to/file1.nc')
            >>> props = builder.build()

        Building properties from multiple files with time dimension:
        NOTE: In this case the files must be provided in time coordinate order.::

            >>> builder = GriddedConnectorPropertiesBuilder(unlimited_dimension='time')
            >>> builder.parse_netcdf_props('file1.nc', '/path/to/file1.nc')
            >>> builder.parse_netcdf_props('file2.nc', '/path/to/file2.nc')
            >>> props = builder.build()

        Inserting a new file into the unlimited dimension::

            >>> existing_props = {...}  # Previously built properties
            >>> existing_coords = [0, 86400, 172800]  # Coordinates in dataset
            >>> builder = GriddedConnectorPropertiesBuilder(
            ...     existing_properties=existing_props,
            ...     existing_unlimited_dim_coords=existing_coords
            ... )
            >>> builder.parse_netcdf_props('new_file.nc', '/path/to/new_file.nc')
            >>> updated_props = builder.build()
    """

    ALLOWED_DATA_TYPES = ["i1", "u1", "i2", "u2", "i4", "u4", "i8", "u8", "f4", "f8"]

    def __init__(self, unlimited_dimension='time', existing_properties=None, existing_unlimited_dim_coords=None):
        self._dimensions = {}
        self._spaces = {}
        self._variables = {}
        self._unlimited_dimension = unlimited_dimension

        if existing_unlimited_dim_coords is not None:
            if not np.all(np.diff(existing_unlimited_dim_coords) > 0):
                raise ValueError(f"Unlimited dimension coordinates must be monotonically increasing")
            self._unlimited_dimension_coords= SortedList(existing_unlimited_dim_coords)
        else:
            self._unlimited_dimension_coords = None

        if existing_properties:
            self._validate_props(existing_properties, unlimited_dimension)
            self._dimensions = copy.deepcopy(existing_properties['dimensions'])
            self._spaces = copy.deepcopy(existing_properties['spaces'])
            self._variables = copy.deepcopy(existing_properties['variables'])


    @staticmethod
    def _validate_props(props, time_dimension):
        errors = []

        if "dimensions" not in props:
            errors.append("'dimensions' property is missing")

        if "spaces" not in props:
            errors.append("'spaces' property is missing")

        if "variables" not in props:
            errors.append("'variables' property is missing")

        if errors:
            raise ValueError("\n".join(errors))

        dimensions = props['dimensions']
        dnames = dimensions.keys()

        spaces = props['spaces']
        snames = spaces.keys()

        for k, v in spaces.items():
            if 'dimensions' not in v:
                errors.append(f"'dimensions' property is missing in space {k}")
            elif not set(v['dimensions']).issubset(dnames):
                errors.append(f"'dimensions' values in space {k} are not a subset of dimensions keys. Expected subset of {dnames}, got {v['dimensions']}")

        variables = props['variables']
        vnames = variables.keys()

        for k, v in variables.items():
            space = spaces[v['space']]
            space_dimensions = space['dimensions']

            if k == time_dimension:
                if 'returnType' not in v or v['returnType'] != 'f8':
                    errors.append(f"return type for {time_dimension} must be type f8 but got {v.get('returnType')}")

            if 'dataType' not in v:
                errors.append(f"'dataType' property is missing in variable {k}")

            if 'space' not in v or v['space'] not in snames:
                errors.append(f"space property in variable {k} is not a valid space. Expected one of {snames}, got {v.get('space')}")

            if 'slices' not in v:
                errors.append(f"'slices' property is missing in variable {k}")
            else:
                for key, slice in v['slices'].items():

                    if 'starts' not in slice:
                        errors.append(f"'starts' property is missing in slice {key} in variable {k}")
                    elif len(slice['starts']) != len(space_dimensions):
                        errors.append(f"'starts' property length in slice {key} in variable {k} does not match space dimensions. Expected {len(space_dimensions)}, got {len(slice['starts'])}")

                    if 'counts' not in slice:
                        errors.append(f"'counts' property is missing in slice {key} in variable {k}")
                    elif len(slice['counts']) != len(space_dimensions):
                        errors.append(f"'counts' property length in slice {key} in variable {k} does not match space dimensions. Expected {len(space_dimensions)}, got {len(slice['counts'])}")

                    if 'varPath' not in slice:
                        errors.append(f"'varPath' property is missing in slice {slice} in variable {k}")
                    elif slice['varPath'] not in vnames:
                        errors.append(f"'varPath' property value in slice {key} in variable {k} is not a valid variable. Expected one of {vnames}, got {slice['varPath']}")

                    if k == time_dimension:
                        if 'valueScale' not in slice:
                            errors.append(f"expecting 'valueScale' property to be present for {time_dimension} dimension in slice {key} in variable {k}")
                        if 'valueOffset' not in slice:
                            errors.append(f"expecting 'valueOffset' property to be present for {time_dimension} dimension in slice {key} in variable {k}")

            if errors:
                raise ValueError("\n".join(errors))

            if time_dimension not in space_dimensions:
               pass
            else:

                next_start = 0

                # sort by time dimension start indices
                slices_by_time_starts = sorted(v['slices'].items(),
                                               key=lambda x: x[1]['starts'][space_dimensions.index(time_dimension)])

                for _, s in slices_by_time_starts:
                    if next_start != s['starts'][space_dimensions.index(time_dimension)]:
                        errors.append(f"starts value for time dimension in slice {list(v['slices'].keys()).index(s['filename'])} in variable {k} does not match next expected start value. Expected {next_start}, got {s['starts'][space_dimensions.index(time_dimension)]}")
                    count = s['counts'][space_dimensions.index(time_dimension)]
                    next_start += count

                if dimensions[time_dimension]['size'] != next_start:
                    errors.append(f"size property for time dimension in variable {k} does not match next expected start value. Expected {next_start}, got {dimensions[time_dimension]['size']}")

            if errors:
                raise ValueError("\n".join(errors))



    def build(self):
        props = {
            "dimensions": self._dimensions,
            "spaces": self._spaces,
            "variables": self._variables
        }
        self._validate_props(props, self._unlimited_dimension)
        return props

    def add_dimension(self, name):
        if name in self._dimensions.keys():
            raise KeyError(f"dimension {name} already exists")

        self._dimensions[name] = {"size": 0, "data": name}

    def add_space(self, name, dimensions):
        if name in self._spaces.keys():
            raise KeyError(f"space {name} already exists")

        if not dimensions:
            raise ValueError("dimensions list must be provided for space")

        for d in dimensions:
            if d not in self._dimensions.keys():
                raise KeyError(f"unknown dimension {d} not found in dimension list {self._dimensions.keys()}")

        self._spaces[name] = {"dimensions": dimensions}

    def add_variable(self, name, dataType, returnType=None, returnFillValue: Optional[float | int] = None):
        if name in self._variables.keys():
            raise KeyError(f"variable {name} already exists")

        if dataType not in self.ALLOWED_DATA_TYPES:
            _logger.warning(f"Warning: {dataType} not found in known datatypes {self.ALLOWED_DATA_TYPES}")

        if returnType and returnType not in self.ALLOWED_DATA_TYPES:
            _logger.warning(f"Warning: {returnType} not found in known datatypes {self.ALLOWED_DATA_TYPES}")

        if name not in self._spaces.keys():
            raise KeyError(f"unknown space {name} for variable {name}")

        self._variables[name] = {
            "dataType": dataType,
            "space": name,
            "slices": {}
        }

        if returnType:
            self._variables[name]["returnType"] = returnType
        if returnFillValue:
            self._variables[name]["returnFillValue"] = returnFillValue

    def add_slice(
        self,
        variable: str,
        file: str,
        counts: list[int],
        unlimed_dim_insert_index: int = None,
        value_scale: Optional[float] = None,
        value_offset: Optional[float] = None,
        amend_last_unlimed_slice: bool = False,
        fill_value : Optional[float | int] = None,
    ):
        """
        Adds a slice to the specified variable in the dataset, managing spatial and temporal dimensions.

        The method handles adding information about a slice of data (linked to a specific file) and its dimensions to the
        tracked attributes of a variable. It ensures consistency of dimension sizes and constraints, particularly for unlimited
        dimensions. If the variable's space dimensions or slice properties (e.g., counts and starts) deviate from the expected
        requirements, appropriate errors are raised. Furthermore, modifications to existing slices (e.g., amendments) are
        controlled under specific conditions, such as append operations or replacements at the last slice.

        Parameters:
        variable : str
            The name of the variable in which the slice is being added.
        file : str
            The file name or path associated with the data slice.
        counts : list[int]
            The count values representing the size of each dimension for this slice.
        insert_index : int, optional
            An integer representing the position for inserting this slice in the unlimited dimension. If none, the slice is appended to the end of the list. Must be None for an ammend operation.
        valueScale : float, optional
            A scaling factor for variable values in this slice. None if no scaling is applied.
        valueOffset : float, optional
            An offset amount for variable values in this slice. None if no offset is applied.
        amend_slice : bool, optional
            If True, allows modifications to specific properties of an existing slice. Defaults to False.
        fillValue : float | int, optional
            A default fill value added during the slice creation, if provided.

        Raises:
        KeyError
            Raised when the specified variable does not exist in the dataset.
        ValueError
            Raised for inconsistencies in space dimensions, for attempting to modify slices against allowed constraints,
            or if dimension sizes between slices deviate where not allowed.
        """
        if variable not in self._variables.keys():
            raise KeyError(f"variable {variable} not found")

        space = self._variables[variable]['space']
        space_dims = self._spaces[space]['dimensions']

        if len(space_dims) != len(counts):
            raise ValueError(f"space dimensions {space_dims} and counts {counts} must be of equal length")

        if self._unlimited_dimension not in space_dims and len(self._variables[variable]['slices'].keys()) == 1:
            # the connector properties only requires a single slice to defined if the variable does not include the
            # unlimited dimension. The first file/slice will be used to represent the shape for all other files/slices
            # associated with this variable.
            _logger.info(f"ignoring adding space, already satisfied for non unlimited dimension {variable}, {file}, {counts}, {value_scale}, {value_offset}")
            return


        starts = [0 for _ in space_dims]

        for dimension in space_dims:
            dim_idx = self._get_space_dimension_index(space, dimension)

            if dimension == self._unlimited_dimension:
                # Unlimited dimensions are allowed to have slices inserted at any position

                if file in self._variables[variable]["slices"]:
                    starts = self._prepare_dimension_for_replace_slice(variable, file, counts, amend_last_unlimed_slice, dim_idx, starts)
                else:
                    starts = self._prepare_dimension_for_insert_slice(variable, counts, dimension, dim_idx,
                                                                      unlimed_dim_insert_index, starts)
            else:
                # Dimensions other than the unlimited dimension are not allowed to change shape.
                # Or in other words the size of the slice in these dimensions must be equal across all slices.
                current_size = self._dimensions[dimension]['size']
                new_size = counts[dim_idx]
                if current_size == 0: # TODO: is this the right test? could you have a variable with slices with dimension length of 0?
                    self._dimensions[dimension]['size'] = new_size
                elif current_size != new_size:
                    raise ValueError(f"'{dimension}' dimension cannot change shape between files slices. Only the unlimited dimension '{self._unlimited_dimension}' is allowed to change.")

        sl = {'starts': starts, 'counts': counts, 'varPath': variable}

        if value_scale is not None:
            sl['valueScale'] = value_scale

        if value_offset is not None:
            sl['valueOffset'] = value_offset

        if fill_value is not None:
            sl['fillValue'] = fill_value

        self._variables[variable]['slices'][file] = sl

    def _prepare_dimension_for_insert_slice(self, variable, counts, dimension, dim_idx, unlim_dim_insert_index, starts ):
        """
        Determines the start indices for a new slice and also adjusts existing slices and spaces appropriately.

        Args:
            variable (str): The variable name.
            counts (list): The counts for the new slice.
            dim_idx (int): The dimension index.
            unlim_dim_insert_index (int): The insert index for the unlimited dimension.
            starts (list): The start indices for the new slice so far.

        Returns:
            list: Updated start indices for the new slice.
        """

        if unlim_dim_insert_index is not None:
            ordered_slices = self.get_var_slices_sorted_by_dim_start(variable, dim_idx)

            # initialise starts as if the insert position is the first slice
            if ordered_slices:
                starts[dim_idx] = ordered_slices[0][1]['starts'][dim_idx]
            else:
                # no existing slices, so the start index must be 0
                starts[dim_idx] = 0

            last_starts = starts

            # shift all slices by new count on current dimension where starts is greater than insert index
            for i, (_, existing_slice) in enumerate(ordered_slices):
                existing_start = existing_slice["starts"][dim_idx]
                if  i >= unlim_dim_insert_index:
                    # this slice is after the inserted slice, needs shifting by the size of the new slice
                    existing_slice["starts"][dim_idx] = existing_start + counts[dim_idx]
                    last_starts = existing_slice['starts']
                else:
                    # this slice is before the inserted slice, adjust start and count of new slice (may not be the final value)
                    starts[dim_idx] = existing_start + existing_slice["counts"][dim_idx]
                    last_starts = starts

            # Adjust the dimension size to the size
            self._dimensions[dimension]["size"] = last_starts[dim_idx] + counts[dim_idx]

        else:
            # must be an append-only operation
            starts[dim_idx] = self._get_next_start(variable, dim_idx)
            self._dimensions[dimension]["size"] = starts[dim_idx] + counts[dim_idx]

        return starts

    def _prepare_dimension_for_replace_slice(self, variable, file, counts, amend_slice, dim_idx, starts):
        """
        Replacing a slice can happen anywhere so long as the size of the slice does not change, the file name can change.
        amending a slice (changing the size) can only happen on the last slice in the unlimited dimension.
        """

        existing_slice = self._variables[variable]["slices"][file]

        # Get slices in order of unlimited dimension start indices
        last_file, last_slice = self.get_var_slices_sorted_by_dim_start(variable, dim_idx)[-1]

        is_last_slice = last_file == file

        if amend_slice and existing_slice["counts"] != counts:
            if not is_last_slice:
                raise ValueError(f'The file {file} is not the last slice in the unlimited dimension and therefore cannot be amended.')

            # adjust size of unlimited dimension based on new slice size
            self._dimensions[self._unlimited_dimension]["size"] = (
                    last_slice["starts"][dim_idx] + counts[dim_idx]
            )
        else:
            # replace only
            if existing_slice["counts"] != counts:
              raise ValueError('The new file slice size does not match the existing file slice size.')

        # maintain the original start and update time dimension size in props
        existing_start = existing_slice["starts"][dim_idx]
        starts[dim_idx] = existing_start
        return starts


    def get_var_slices_sorted_by_dim_start(self, variable, dim_idx):
        return sorted(self._variables[variable]['slices'].items(), key=lambda x: x[1]['starts'][dim_idx])

    def get_variable_missing_or_fillvalue(self, variable):
        fillValue = variable.getncattr('_FillValue').item() if '_FillValue' in variable.ncattrs() else None
        missing_value = variable.getncattr('missing_value').item() if 'missing_value' in variable.ncattrs() else None

        fill = fillValue if fillValue else missing_value
        if isinstance(fill, float) and np.isnan(fill):
            fill = None
        
        if isinstance(fillValue, int):
            if abs(fillValue) > _MAX_FLOAT64_PRECISION:
                raise ValueError("Integer fill values cannot be larger in magnitude than 2^53 - 1")

        return fill


    def parse_netcdf_props(
        self,
        fileKey,
        filePath,
        skip_dimensions=None,
        skip_variables=None,
        unlimited_dimension_name="time",
        cf_time_units_conversion_fn=calculate_netcdf_cf_units_scaling,
        amend_slice=False,
        returnFills: Optional[dict[str, float | int]] = None
    ):
        """
        Parse NetCDF file and extract slices.

        IMPORTANT: If you don't provide unlimited_dimension_coords then the slices will be appended to the end of the time coordinate in the given file.

        Args:
            fileKey (str): A unique identifier for the file, used to index the file in the slices dictionary.
            filePath (str): The local path to the NetCDF file.
            skip_dimensions (Optional[list[str]]): A list of dimensions to skip. Defaults to None.
            skip_variables (Optional[list[str]]): A list of variables to skip. Defaults to None.
            time_dim_name (str): The name of the time dimension. Defaults to "time".
            cf_time_units_conversion_fn (Callable[[str], float]): A function that converts the time coordinate to unix time units. Defaults to calculate_netcdf_cf_units_scaling.
            amend_slice (bool): Whether to use the given netcdf to amend the latest slice in the time dimensions. Defaults to False.
            returnFills (Optional[dict[str, float | int]]): A dictionary mapping variables to the fill values to return. Defaults to None.
        """

        if skip_dimensions and isinstance(skip_dimensions, str):
            skip_dimensions = [skip_dimensions]

        if skip_variables and isinstance(skip_variables, str):
            skip_variables = [skip_variables]

        if returnFills:
            if not isinstance(returnFills, dict):
                raise ValueError(f"returnFills must be a dictionary mapping variables to fill values")

        scale_offset_override_fn = {
            unlimited_dimension_name: cf_time_units_conversion_fn
        }

        if unlimited_dimension_name != self._unlimited_dimension:
            raise ValueError(f'argument time_dim_name must match unlimited_dimension of the builder object')


        # sorted list of unlimited dimension coordinates
        unlimited_dim_slice_starts = SortedList()
        unlimited_dim_slice_starts_coords = SortedList()
        unlimited_dim_slice_counts = SortedList()

        unlimited_dim_append_only = False

        if self._unlimited_dimension_coords is None:
            unlimited_dim_append_only = True

        # created sorted lookup of existing unlimited dimension coordinate.
        if not unlimited_dim_append_only and len(self._unlimited_dimension_coords) > 0 and unlimited_dimension_name in self._variables:
            for key, slice in self._variables[unlimited_dimension_name]['slices'].items():
                # unlimited coordinate variable should be 1d by definition
                assert(len(slice['starts'])) == 1

                # get coord for index of slice
                try:
                    coord = self._unlimited_dimension_coords[slice['starts'][0]]
                    unlimited_dim_slice_starts_coords.add(coord)
                except IndexError:
                    # Unlimited coords not available
                    logging.warning(f"Adding slice without unlimited dimension coordinates which cover existing slices, file will be treated as append operation")
                    unlimited_dim_append_only = True

                unlimited_dim_slice_counts.add(slice['counts'][0])
                unlimited_dim_slice_starts.add(slice['starts'][0])

        with managed_netcdf(filePath, 'r') as ds:
            dimensions = set(ds.dimensions.keys()) - set(skip_dimensions) if skip_dimensions else set(ds.dimensions.keys())
            for d in dimensions:
                if d not in self._dimensions.keys():
                    self.add_dimension(d)

            unlimited_dim_coord_var = ds.variables[unlimited_dimension_name]
            offset, scale = self._get_value_offset_scale(unlimited_dim_coord_var, scale_offset_override_fn)
            scale = scale if scale is not None else 1
            offset = offset if offset is not None else 0
            file_unlimited_coord_values = unlimited_dim_coord_var[:] * scale + offset

            if np.any(np.isin(file_unlimited_coord_values, self._unlimited_dimension_coords)):
                raise ValueError("Unlimited dimension coordinates overlap with existing slices. New slices must not overlap on the time dimension")

            # calculate the unlimited dimension coordinate insert position
            # This is used to determine the insertion position of the unlimited coordinate slice but also other variable slices
            # which have the unlimited dimension in their space
            if not unlimited_dim_append_only:
                insert_index = bisect.bisect_left(unlimited_dim_slice_starts_coords, file_unlimited_coord_values[0])

                if insert_index > 0:
                    prior_slice_start_index = unlimited_dim_slice_starts[insert_index-1]
                    prior_slice_count = unlimited_dim_slice_counts[insert_index-1]
                    prior_slice_end_coord = self._unlimited_dimension_coords[prior_slice_start_index + prior_slice_count -1]

                    if file_unlimited_coord_values[0] < prior_slice_end_coord:
                        raise ValueError(
                            "Unlimited dimension coordinates overlap with existing slices. New slices must not overlap on the time dimension")

                if insert_index <= len(unlimited_dim_slice_starts)-1:
                    # There _is_ a next slice
                    next_slice_start_index = unlimited_dim_slice_starts[insert_index]
                    next_slice_start_coord = self._unlimited_dimension_coords[next_slice_start_index]

                    if file_unlimited_coord_values[-1] >= next_slice_start_coord:
                        raise ValueError(
                            "Unlimited dimension coordinates overlap with existing slices. New slices must not overlap on the time dimension")

            else:
                # Insert not possible without unlimited dimension coordinate. Fallback to append-only mode.
                logging.warning('Adding files without unlimited dimension coordinate. Fallback to append-only mode. Please provide unlimited dimension coordinates for better robustness.')
                insert_index = self._dimensions[self._unlimited_dimension]['size']

            for vname, variable in ds.variables.items():
                if skip_dimensions and any(d in skip_dimensions for d in ds[vname].dimensions):
                    _logger.info("skipping variable %s as it contains a dimension that has been marked as ignored." % (vname, ))
                    continue

                if skip_variables and vname in skip_variables:
                    _logger.info("skipping variable %s as has been marked as ignored." % (vname, ))
                    continue

                if vname not in self._spaces.keys():
                    self.add_space(vname, ds[vname].dimensions)

                offset, scale = self._get_value_offset_scale(variable, scale_offset_override_fn)

                # TODO: Add Fill value attrs here
                fillValue = self.get_variable_missing_or_fillvalue(variable)

                dataType = ds[vname].dtype.str.strip('|<>=')

                returnType = None
                # If returnType isn't time or has scale/offset values then return None, platform then infers dataType as the returnType
                if len(ds[vname].dimensions) == 1 and unlimited_dimension_name in ds[vname].dimensions:
                    returnType = 'f8'
                elif scale is not None or offset is not None:
                    returnType = 'f8'

                rfill = None
                if returnFills is not None:
                    rfill = returnFills.get(vname)
                else:
                    rfill = _DEFAULT_FILL[returnType if returnType else dataType]
                if vname not in self._variables.keys():
                    self.add_variable(vname, dataType, returnType, returnFillValue=rfill)
                else:
                    # provide return fill value to object if does not exist
                    if fillValue:
                        self._variables[vname]["returnFillValue"] = rfill

                self.add_slice(
                    vname,
                    fileKey,
                    list(ds[vname].shape),
                    unlimed_dim_insert_index=insert_index,
                    value_scale=scale,
                    value_offset=offset,
                    amend_last_unlimed_slice=amend_slice,
                    fill_value=fillValue
                )

            if self._unlimited_dimension_coords is not None:
                self._unlimited_dimension_coords.update(file_unlimited_coord_values)



    def  _get_value_offset_scale(self, variable, scale_offset_override_fn_map):
        scale = variable.getncattr('scale_factor').item() if 'scale_factor' in variable.ncattrs() else None
        offset = variable.getncattr('add_offset').item() if 'add_offset' in variable.ncattrs() else None

        if fn := scale_offset_override_fn_map.get(variable.name, None):
            scale, offset = fn(variable.units)

        return offset, scale

    def _get_space_dimension_index(self, space, dim):
        if dim in self._spaces[space]['dimensions']:
            return self._spaces[space]['dimensions'].index(dim)
        else:
            return None

    def _get_next_start(self, variable, dim_idx):
        slices = self._variables[variable]['slices']

        if not slices:
            return 0

        # Find slice with highest start value for the dimension
        max_start_slice = max(slices.values(), key=lambda s: s['starts'][dim_idx])

        return max_start_slice['starts'][dim_idx] + max_start_slice['counts'][dim_idx]


def gridded_geotime_netcdf_props(
    fileMap,
    skipDimensions=None,
    skipVars=None,
    existingProps=None,
    existing_unlimited_dimension_coords=None,
    cf_time_units_conversion_fn=calculate_netcdf_cf_units_scaling,
    amend_slice=False
):
    """
    Limitations:
     - New variables can only be added with new dimensions. This effectively means that all files must have all variables, you can't partition a dataset into a per variable files. This is not a limitation of the platform, just a limitation of this netcdf connector properties builder.

    Args:
        fileMap (dict): file mappings e.g {'file.nc': './files/file.nc', ...}. Files must be provided in unlimited dimension order. All other dimension sizes must be consistent across files.
        skipDimensions (list[str], optional): dimensions to exclude from the results. All spaces and variables dependent on these dimensions will also be dropped. Defaults to None.
        existingProps (dict, optional): Optional existing connector properties to merge. Should be used when appending new objects to an existing connector definition. Defaults to None.
        cf_time_units_conversion_fn (function, optional): Callback fn for manipulating variables during processing. Defaults to calculate_netcdf_cf_units_scaling.
        amend_slice (bool, optional): If True, will allow for the amendment of the last slice from a GriddedConnectorPropertiesBuilder object. Defaults to False.
        existing_unlimited_dimension_coords (dict, optional): Optional existing unlimited dimension coordinates. Should be used when inserting slices within an existign unlimited dimension coordinate. Defaults to None.

    Returns:
        dict: connector properties in the form {"dimensions": {}, "spaces": {}, "variables": {}}
    """

    builder = GriddedConnectorPropertiesBuilder(existing_properties=existingProps,
                                                existing_unlimited_dim_coords=existing_unlimited_dimension_coords)

    for fileKey, filePath in fileMap.items():
        builder.parse_netcdf_props(
            fileKey,
            filePath,
            skip_dimensions=skipDimensions,
            skip_variables=skipVars,
            cf_time_units_conversion_fn=cf_time_units_conversion_fn,
            amend_slice=amend_slice
        )
    return builder.build()
