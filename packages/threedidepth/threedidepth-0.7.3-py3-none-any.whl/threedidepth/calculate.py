# -*- coding: utf-8 -*-

from datetime import datetime as Datetime, timedelta as Timedelta
from functools import cached_property
from itertools import product
from os import path

from osgeo import gdal
from osgeo import osr
from scipy.interpolate import LinearNDInterpolator
from scipy.spatial import Delaunay
import h5netcdf.legacyapi as netCDF4
import h5py
import numpy as np

from threedigrid.admin.gridresultadmin import GridH5ResultAdmin
from threedigrid.admin.gridresultadmin import GridH5AggregateResultAdmin
from threedigrid.admin.gridresultadmin import GridH5WaterQualityResultAdmin
from threedigrid.admin.constants import SUBSET_2D_OPEN_WATER
from threedigrid.admin.constants import NO_DATA_VALUE
from threedidepth.fixes import fix_gridadmin
from threedidepth.tiffs import AuxGeoTIFF
from threedidepth import morton

MODE_COPY = "copy"
MODE_NODGRID = "nodgrid"
MODE_CONSTANT_VAR = "constant-var"
MODE_LINEAR_VAR = "linear-var"
MODE_LIZARD_VAR = "lizard-var"
MODE_CONSTANT = "constant"
MODE_LINEAR = "linear"
MODE_LIZARD = "lizard"
MODE_LIZARD_WQ = "lizard-wq"

# keep old constants for backwards compatibility
MODE_CONSTANT_S1 = "constant-var"
MODE_LINEAR_S1 = "linear-var"
MODE_LIZARD_S1 = "lizard-var"


def num2date(time, units):
    """ Very limited version of the well known cftime implementation. """
    prefix = "seconds since "
    assert units.startswith(prefix)
    assert isinstance(time, (float, int))
    origin = Datetime.fromisoformat(units[len(prefix):])
    return origin + Timedelta(seconds=time)


class BaseCalculator:
    """Depth calculator using constant waterlevel in a grid cell.

    Args:
        result_admin (ResultAdmin): ResultAdmin instance.
        calculation_step (int): Calculation step.
        dem_shape (int, int): Shape of the dem array.
        dem_geo_transform: (tuple) Geo_transform of the dem.
    """
    def __init__(
        self, result_admin, dem_shape, dem_geo_transform,
        calculation_step=None, get_max_level=False
    ):
        assert get_max_level == (calculation_step is None)  # only one allowed
        self.ra = result_admin
        self.calculation_step = calculation_step
        self.get_max_level = get_max_level
        self.dem_shape = dem_shape
        self.dem_geo_transform = dem_geo_transform

    def __call__(self, indices, values, no_data_value):
        """Return result values array.

        Args:
            indices (tuple): ((i1, j1), (i2, j2)) subarray indices
            values (array): source values for the calculation
            no_data_value (scalar): source and result no_data_value

        Override this method to implement a calculation. The default
        implementation is to just return the values, effectively copying the
        source.

        Note that the no_data_value for the result has to correspond to the
        no_data_value argument.
        """
        raise NotImplementedError

    @staticmethod
    def _depth_from_water_level(dem, fillvalue, waterlevel):
        # determine depth
        depth = np.full_like(dem, fillvalue)
        dem_active = dem != fillvalue
        waterlevel_active = waterlevel != NO_DATA_VALUE
        active = dem_active & waterlevel_active
        depth_1d = waterlevel[active] - dem[active]

        # paste positive depths only
        negative_1d = depth_1d <= 0
        depth_1d[negative_1d] = fillvalue
        depth[active] = depth_1d

        return depth

    @cached_property
    def variable_lut(self):
        """
        Return the lookup table to find waterlevel by cell id.

        Both cells outside any defined grid cell and cells in a grid cell that
        are currently not active ('no data') will return the NO_DATA_VALUE as
        defined in threedigrid.
        """
        nodes = self.ra.get_nodes().subset(SUBSET_2D_OPEN_WATER)
        n_time = self.ra.get_timestamps().size
        if self.get_max_level:
            # array off n_time * n_nodes
            timeseries = nodes.timeseries(indexes=slice(0, n_time))
            data = timeseries.only(self.ra.variable, "id").data
            values = np.max(data[self.ra.variable], axis=0)
        else:
            timeseries = nodes.timeseries(indexes=slice(
                self.calculation_step, self.calculation_step + 1
            ))
            data = timeseries.only(self.ra.variable, "id").data
            values = data[self.ra.variable][0]
        variable_lut = np.full((data["id"]).max() + 1, NO_DATA_VALUE)
        variable_lut[data["id"]] = values
        return variable_lut

    @property
    def coordinates(self):
        nodes = self.ra.get_nodes().subset(SUBSET_2D_OPEN_WATER)
        data = nodes.only("id", "coordinates").data
        # transpose does:
        # [[x1, x2, x3], [y1, y2, y3]] --> [[x1, y1], [x2, y2], [x3, y3]]
        points = data["coordinates"].transpose()
        ids = data["id"]
        return points, ids

    @cached_property
    def interpolator(self):
        points, ids = self.coordinates
        values = self.variable_lut[ids]
        interpolator = LinearNDInterpolator(
            points, values, fill_value=NO_DATA_VALUE
        )
        return interpolator

    @cached_property
    def delaunay(self):
        """
        Return a (delaunay, ids) tuple.

        `delaunay` is a scipy.spatial.Delaunay object, and `ids` is an array of
        ids for the corresponding simplices.
        """
        points, ids = self.coordinates

        # reorder a la lizard
        points, ids = morton.reorder(points, ids)

        delaunay = Delaunay(points)
        return delaunay, ids

    def _get_nodgrid(self, indices):
        """Return node grid.

        Args:
            indices (tuple): ((i1, j1), (i2, j2)) subarray indices
        """
        # (xm, ym) is the lower-left nodgrid origin
        dx, _, xm, _, dy, ym = self.ra.grid.transform

        # (xi, yi) is the upper-left target origin
        xt, yt = self.dem_geo_transform[::3]

        # compute the distance in cells between these origins
        dj = round((xt - xm) / dx)
        di = round((yt - ym) / dy)

        (i1, j1), (i2, j2) = indices

        # note that get_nodgrid() starts counting rows from the bottom
        i1, i2 = di - i2, di - i1
        j1, j2 = dj + j1, dj + j2

        # note that get_nodgrid() expects a columns-first bbox
        return self.ra.cells.get_nodgrid(
            [j1, i1, j2, i2], subset_name=SUBSET_2D_OPEN_WATER
        )

    def _get_points(self, indices):
        """Return points array.

        Args:
            indices (tuple): ((i1, j1), (i2, j2)) subarray indices
        """
        (i1, j1), (i2, j2) = indices
        local_ji = np.mgrid[i1:i2, j1:j2].reshape(2, -1)[::-1].transpose()
        p, a, b, q, c, d = self.dem_geo_transform
        return local_ji * [a, d] + [p + 0.5 * a, q + 0.5 * d]


class CopyCalculator(BaseCalculator):
    def __call__(self, indices, values, no_data_value):
        """Return input values unmodified."""
        return values


class NodGridCalculator(BaseCalculator):
    def __call__(self, indices, values, no_data_value):
        """Return node grid."""
        return self._get_nodgrid(indices)


class ConstantLevelCalculator(BaseCalculator):
    def __call__(self, indices, values, no_data_value):
        """Return waterlevel array."""
        return self.variable_lut[self._get_nodgrid(indices)]


class LinearLevelCalculator(BaseCalculator):
    def __call__(self, indices, values, no_data_value):
        """Return waterlevel array."""
        points = self._get_points(indices)
        return self.interpolator(points).reshape(values.shape)


class LizardLevelCalculator(BaseCalculator):
    def __call__(self, indices, values, no_data_value):
        """ Return waterlevel array.

        This uses both the grid layout from the constant level method and the
        triangulation from the linear method.

        Interpolation is used to determine the waterlevel for a result cell if
        all of the following requirements are met:
        - The point is inside a grid cell
        - The point is inside the triangulation
        - The sum of weights of active (not 'no data' nodes) is more than half
          of the total weight of all nodes. Only active nodes are included in
          the interpolation.

        In all other cases, the waterlevel from the constant level method is
        used."""
        # start with the constant level result
        nodgrid = self._get_nodgrid(indices).ravel()
        level = self.variable_lut[nodgrid]

        # determine result raster cell centers and in which triangle they are
        points = self._get_points(indices)
        delaunay, ids = self.delaunay
        s1 = self.variable_lut[ids]
        simplices = delaunay.find_simplex(points)

        # determine which points will use interpolation
        in_gridcell = nodgrid != 0
        in_triangle = simplices != -1
        in_interpol = in_gridcell & in_triangle
        points = points[in_interpol]

        # get the nodes and the transform for the corresponding triangles
        transform = delaunay.transform[simplices[in_interpol]]
        simplices = delaunay.simplices[simplices[in_interpol]]

        # calculate weight, see print(spatial.Delaunay.transform.__doc__) and
        # Wikipedia about barycentric coordinates
        weight = np.empty(simplices.shape)
        weight[:, :2] = np.sum(
            transform[:, :2] * (points - transform[:, 2])[:, np.newaxis], 2
        )
        weight[:, 2] = 1 - weight[:, 0] - weight[:, 1]

        # set weight to zero when for inactive nodes
        nodelevel = s1[simplices]
        weight[nodelevel == NO_DATA_VALUE] = 0

        # determine the sum of weights per result cell
        weight_sum = weight.sum(axis=1)

        # further subselect points suitable for interpolation
        suitable = weight_sum > 0.5
        weight = weight[suitable] / weight_sum[suitable][:, np.newaxis]
        nodelevel = nodelevel[suitable]

        # combine weight and nodelevel into result
        in_interpol_and_suitable = in_interpol.copy()
        in_interpol_and_suitable[in_interpol] &= suitable
        level[in_interpol_and_suitable] = np.sum(weight * nodelevel, axis=1)
        return level.reshape(values.shape)


class ConstantLevelDepthCalculator(ConstantLevelCalculator):
    def __call__(self, indices, values, no_data_value):
        """Return waterdepth array."""
        waterlevel = super().__call__(indices, values, no_data_value)
        return self._depth_from_water_level(
            dem=values, fillvalue=no_data_value, waterlevel=waterlevel
        )


class LinearLevelDepthCalculator(LinearLevelCalculator):
    def __call__(self, indices, values, no_data_value):
        """Return waterdepth array."""
        waterlevel = super().__call__(indices, values, no_data_value)
        return self._depth_from_water_level(
            dem=values, fillvalue=no_data_value, waterlevel=waterlevel
        )


class LizardLevelDepthCalculator(LizardLevelCalculator):
    def __call__(self, indices, values, no_data_value):
        """Return waterdepth array."""
        waterlevel = super().__call__(indices, values, no_data_value)
        return self._depth_from_water_level(
            dem=values, fillvalue=no_data_value, waterlevel=waterlevel
        )


class GeoTIFFConverter:
    """Convert tiff, applying a calculating function to the data.

    Args:
        source_path (str): Path to source GeoTIFF file.
        target_path (str): Path to target GeoTIFF file.
        result_admin (ResultAdmin): calculators.ResultAdmin object
        calculation_steps (list[int]): List of (zero-based) calculation steps
        progress_func: a callable.

        The progress_func will be called multiple times with values between 0.0
        amd 1.0.
    """

    def __init__(
            self,
            source_path,
            target_path,
            result_admin,
            calculation_steps,
            progress_func=None,
    ):
        self.source_path = source_path
        self.target_path = target_path
        self.ra = result_admin
        self.calculation_steps = calculation_steps
        self.band_count = len(calculation_steps)
        self.progress_func = progress_func

        if path.exists(self.target_path):
            raise OSError("%s already exists." % self.target_path)

    def __enter__(self):
        """Open datasets."""
        self.source = gdal.Open(self.source_path, gdal.GA_ReadOnly)
        block_x_size, block_y_size = self.block_size
        options = ["compress=deflate", "blockysize=%s" % block_y_size]
        if block_x_size != self.raster_x_size:
            options += ["tiled=yes", "blockxsize=%s" % block_x_size]

        self.target = gdal.GetDriverByName("gtiff").Create(
            self.target_path,
            self.raster_x_size,
            self.raster_y_size,
            self.band_count,
            self.source.GetRasterBand(1).DataType,
            options=options,
        )
        self.target.SetProjection(self.projection)
        self.target.SetGeoTransform(self.geo_transform)
        time_units = self.ra.get_time_units()
        timestamps = self.ra.get_timestamps()
        for i, s in enumerate(self.calculation_steps):
            band = self.target.GetRasterBand(i + 1)
            band.SetNoDataValue(self.no_data_value)
            try:
                datetime = num2date(timestamps[s].item(), units=time_units)
                band.SetDescription(str(datetime))
            except AssertionError:
                pass
                # there are wq files lying around with nothing after "seconds since"
        return self

    def __exit__(self, *args):
        """Close datasets.
        """
        self.source = None
        self.target = None

    @property
    def projection(self):
        return self.source.GetProjection()

    @property
    def geo_transform(self):
        return self.source.GetGeoTransform()

    @property
    def no_data_value(self):
        value = self.source.GetRasterBand(1).GetNoDataValue()
        return value if value is not None else -9999.0

    @property
    def raster_x_size(self):
        return self.source.RasterXSize

    @property
    def raster_y_size(self):
        return self.source.RasterYSize

    @property
    def block_size(self):
        return self.source.GetRasterBand(1).GetBlockSize()

    def __len__(self):
        block_size = self.block_size
        blocks_x = -(-self.raster_x_size // block_size[0])
        blocks_y = -(-self.raster_y_size // block_size[1])
        return blocks_x * blocks_y

    def partition(self):
        """Return generator of band_no, (xoff, xsize), (yoff, ysize) values.
        """
        def offset_size_range(stop, step):
            for start in range(0, stop, step):
                yield start, min(step, stop - start)

        # make y the outer loop, tiled tiff writing is much faster row-wise...
        raster_size = self.raster_y_size, self.raster_x_size
        block_size = self.block_size[::-1]
        generator = product(*map(offset_size_range, raster_size, block_size))

        total = len(self)
        for count, (y_part, x_part) in enumerate(generator, start=1):
            # ...and in the result put x before y
            yield x_part, y_part
            if self.progress_func is not None:
                self.progress_func(count / total)

    def convert_using(self, calculator, band):
        """Convert data writing it to tiff.

        Args:
            calculator (BaseCalculator): Calculator implementation instance
            band (int): Which band to write to.
        """
        no_data_value = self.no_data_value

        for (xoff, xsize), (yoff, ysize) in self.partition():
            # read
            values = self.source.ReadAsArray(
                xoff=xoff, yoff=yoff, xsize=xsize, ysize=ysize
            )
            indices = (yoff, xoff), (yoff + ysize, xoff + xsize)

            # calculate
            result = calculator(
                indices=indices,
                values=values,
                no_data_value=no_data_value,
            )

            # write - note GDAL counts bands starting at 1
            self.target.GetRasterBand(band + 1).WriteArray(
                array=result, xoff=xoff, yoff=yoff,
            )


class NetcdfConverter(GeoTIFFConverter):
    """Convert NetCDF4 according to the CF-1.6 standards."""

    def __init__(self, *args, write_time_dimension=True, **kwargs):
        super().__init__(*args, **kwargs)
        self.write_time_dimension = write_time_dimension

    def __enter__(self):
        """Open datasets"""
        self.source = gdal.Open(self.source_path, gdal.GA_ReadOnly)
        self.target = netCDF4.Dataset(self.target_path, "w")
        self._set_coords()
        if self.write_time_dimension:
            self._set_time()
        self._set_meta_info()
        self._create_variable()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close datasets"""
        self.source = None
        self.target.close()

    def _set_meta_info(self):
        """Set meta info in the root group"""
        self.target.Conventions = "CF-1.6"
        self.target.institution = "3Di Waterbeheer"
        self.target.model_slug = self.ra.model_slug
        postfix = {"s1": "", "s1_max": " (using s1_max)"}[self.ra.variable]
        self.target.result_type = "Derived water depth" + postfix
        self.target.references = "http://3di.nu"

    def _set_time(self):
        """Set time"""

        self.target.createDimension("time", self.band_count)
        time = self.target.createVariable("time", "f4", ("time",))
        time.standard_name = "time"
        time.calendar = "standard"
        time.axis = "T"
        time.units = self.ra.get_time_units()
        time[:] = self.ra.get_timestamps()[self.calculation_steps]

    def _set_coords(self):
        geotransform = self.source.GetGeoTransform()

        self.target.createDimension("y", self.raster_y_size)
        ycoords = self.target.createVariable("y", "f4", ("y",))

        # In CF-1.6 the coordinates are cell centers, while GDAL interprets
        # them as the upper-left corner.
        y_upper_left = geotransform[3] + geotransform[5] / 2
        ycoords[:] = np.arange(
            y_upper_left,
            y_upper_left + geotransform[5] * self.raster_y_size,
            geotransform[5]
        )
        ycoords.standard_name = "projection_y_coordinate"
        ycoords.long_name = "y coordinate of projection"
        ycoords.units = "m"
        ycoords.axis = "Y"

        self.target.createDimension("x", self.raster_x_size)
        xcoords = self.target.createVariable("x", "f4", ("x",))

        # CF 1.6 coordinates are cell center, while GDAL interprets
        # them as the upper-left corner.
        x_upper_left = geotransform[0] + geotransform[1] / 2
        xcoords[:] = np.arange(
            x_upper_left,
            x_upper_left + geotransform[1] * self.raster_x_size,
            geotransform[1]
        )
        xcoords.standard_name = "projection_x_coordinate"
        xcoords.long_name = "x coordinate of projection"
        xcoords.units = "m"
        xcoords.axis = "X"

        projection = self.target.createVariable(
            "projected_coordinate_system", "i4"
        )
        projection.EPSG_code = f"EPSG:{self.ra.epsg_code}"
        projection.epsg = self.ra.epsg_code
        projection.long_name = "Spatial Reference"
        projection.spatial_ref = osr.GetUserInputAsWKT(
            f"EPSG:{self.ra.epsg_code}"
        )  # for GDAL

    def _create_variable(self):
        water_depth = self.target.createVariable(
            "water_depth",
            "f4",
            ("time", "y", "x",) if self.write_time_dimension else ("y", "x",),
            fill_value=-9999,
            zlib=True
        )
        water_depth.long_name = "water depth"
        water_depth.units = "m"
        water_depth.grid_mapping = "projected_coordinate_system"

    def convert_using(self, calculator, band):
        """Convert data writing it to netcdf4."""

        no_data_value = self.no_data_value
        for (xoff, xsize), (yoff, ysize) in self.partition():
            # read
            values = self.source.ReadAsArray(
                xoff=xoff, yoff=yoff, xsize=xsize, ysize=ysize
            )

            # calculate
            indices = (yoff, xoff), (yoff + ysize, xoff + xsize)
            result = calculator(
                indices=indices,
                values=values,
                no_data_value=no_data_value,
            )

            # write
            water_depth = self.target["water_depth"]
            if self.write_time_dimension:
                water_depth[
                    band, yoff:yoff + ysize, xoff:xoff + xsize
                ] = result
            else:
                water_depth[yoff:yoff + ysize, xoff:xoff + xsize] = result


class ProgressClass:
    """ Progress function and calculation step iterator in one.

    Args:
        calculation_steps (list(int)): Calculation steps
        progress_func: a callable.

    The main purpose is iterating over the calculation steps, but inside the
    iteration progress_class() can be passed values between 0 and 1 to record
    the partial progress for a calculation step. The supplied `progress_func`
    will be called with increasing values up to and including 1.0 for the
    complete iteration.
    """
    def __init__(self, calculation_steps, progress_func):
        self.progress_func = progress_func
        self.calculation_steps = calculation_steps

    def __iter__(self):
        """ Generator of (band_no, calculation_step) """
        for band_no, calculation_step in enumerate(self.calculation_steps):
            self.current = band_no
            yield band_no, calculation_step
        del self.current

    def __call__(self, progress):
        """ Progress method for the current calculation step. """
        self.progress_func(
            (self.current + progress) / len(self.calculation_steps)
        )


class ResultAdmin:
    """
    args:
        gridadmin_path (str): Path to gridadmin.h5 file.
        results_3di_path (str): Path to (aggregate_)results_3di.nc file.

    There differences in the way the different ResultAdmin classes from
    threedigrid work. The GridH5ResultAdmin and the GridH5AggregateResultAdmin
    give access to all variables through the same nodes instance, but for the
    latter the timestamps is a mapping because they can be different from
    variable to variable. The GridH5WaterQualityResultAdmin has each variable
    as presented as its own "nodes" attribute on the object.

    This class selects the correct ResultAdmin class, and adds a number of
    custom properties that are otherwise derived or used in different ways from
    the different ResultAdmins: `result_type`, `variable` and
    `calculation_steps` and `unodes` (unified nodes)
    """

    def __init__(self, gridadmin_path, results_3di_path, variable=None):
        with h5py.File(results_3di_path) as h5:
            self.result_type = h5.attrs["result_type"].decode("ascii")

        result_admin_args = gridadmin_path, results_3di_path
        if self.result_type == "raw":
            self._result_admin = GridH5ResultAdmin(*result_admin_args)
            self.nodes_attr = "nodes"
            self.variable = "s1"
        elif self.result_type == "aggregate":
            self._result_admin = GridH5AggregateResultAdmin(*result_admin_args)
            self.nodes_attr = "nodes"
            self.variable = "s1_max"
        else:
            assert self.result_type == "Water Quality Results"
            assert variable is not None
            self._result_admin = GridH5WaterQualityResultAdmin(
                *result_admin_args
            )
            self.nodes_attr = variable
            self.variable = "concentration"

    def get_nodes(self):
        return getattr(self._result_admin, self.nodes_attr)

    def get_timestamps(self):
        nodes = self.get_nodes()
        if self.result_type == "aggregate":
            return nodes.timestamps[self.variable]
        else:
            return nodes.timestamps

    def get_time_units(self):
        if self.result_type == "raw":
            return self.time_units.decode("utf-8")
        if self.result_type == "aggregate":
            time_variable = "time_s1_max"
        else:
            time_variable = "time"
        nc = self._result_admin.netcdf_file
        return nc[time_variable].attrs["units"].decode("utf-8")

    def __getattr__(self, name):
        return getattr(self._result_admin, name)


calculator_classes = {
    MODE_COPY: CopyCalculator,
    MODE_NODGRID: NodGridCalculator,
    MODE_CONSTANT_VAR: ConstantLevelCalculator,
    MODE_LINEAR_VAR: LinearLevelCalculator,
    MODE_LIZARD_VAR: LizardLevelCalculator,
    MODE_CONSTANT: ConstantLevelDepthCalculator,
    MODE_LINEAR: LinearLevelDepthCalculator,
    MODE_LIZARD: LizardLevelDepthCalculator,
    MODE_LIZARD_WQ: LizardLevelCalculator,
}


def calculate_waterdepth(
    gridadmin_path,
    results_3di_path,
    dem_path,
    waterdepth_path,
    calculation_steps=None,
    calculate_maximum_waterlevel=False,
    mode=MODE_LIZARD,
    progress_func=None,
    netcdf=False,
):
    """Calculate waterdepth and save it as GeoTIFF.

    Args:
        gridadmin_path (str): Path to gridadmin.h5 file.
        results_3di_path (str): Path to (aggregate_)results_3di.nc file.
        dem_path (str): Path to dem.tif file.
        waterdepth_path (str): Path to waterdepth.tif file.
        calculation_steps (list(int)): Calculation step (default: [-1] (last))
        calculate_maximum_waterlevel (bool):
          Use temporal maximum instead of specific timestep
        mode (str): Interpolation mode.
        progress_func(callable):
          Function that receives progress updates as float between 0 and 1
        netcdf(bool): Write a netCDF file instead of a GeoTIFF.
    """
    try:
        CalculatorClass = calculator_classes[mode]
    except KeyError:
        raise ValueError("Unknown mode: '%s'" % mode)

    result_admin = ResultAdmin(
        gridadmin_path=gridadmin_path, results_3di_path=results_3di_path,
    )
    assert result_admin.result_type in {"raw", "aggregate"}

    # handle calculation step
    if calculate_maximum_waterlevel:
        calculation_steps = [0]

    max_calculation_step = result_admin.get_timestamps().size - 1
    if calculation_steps is None:
        calculation_steps = [max_calculation_step]
    else:
        assert min(calculation_steps) >= 0
        assert max(calculation_steps) <= max_calculation_step, (
            "Maximum calculation step is '%s'." % max_calculation_step
        )

    # TODO remove at some point, newly produced gridadmins don't need it
    fix_gridadmin(gridadmin_path)

    progress_class = ProgressClass(
        calculation_steps=calculation_steps, progress_func=progress_func,
    )
    converter_kwargs = {
        "source_path": dem_path,
        "target_path": waterdepth_path,
        "result_admin": result_admin,
        "calculation_steps": calculation_steps,
        "progress_func": None if progress_func is None else progress_class,
    }
    if netcdf:
        converter_class = NetcdfConverter
        converter_kwargs["write_time_dimension"] = not calculate_maximum_waterlevel
    else:
        converter_class = GeoTIFFConverter

    with converter_class(**converter_kwargs) as converter:
        calculator_kwargs_except_step = {
            "result_admin": result_admin,
            "dem_geo_transform": converter.geo_transform,
            "dem_shape": (converter.raster_y_size, converter.raster_x_size),
            "get_max_level": calculate_maximum_waterlevel
        }

        for band, calculation_step in progress_class:
            calculator_kwargs = {
                "calculation_step": calculation_step,
                **calculator_kwargs_except_step,
            }

            calculator = CalculatorClass(**calculator_kwargs)
            converter.convert_using(calculator=calculator, band=band)


def calculate_water_quality(
    gridadmin_path,
    water_quality_results_3di_path,
    variable,
    output_extent,
    output_path,
    calculation_steps=None,
    calculate_maximum_concentration=False,
    mode=MODE_LIZARD_VAR,
    progress_func=None,
    netcdf=False,
):
    """Calculate concentation and save it as GeoTIFF.

    Args:
        gridadmin_path (str): Path to gridadmin.h5 file.
        water_quality_results_3di_path (str): Path to water_quality_results_3di.nc file.
        variable(str): Name of the substance variable, e.g. "substance7".
        output_extent(tuple): Extent for the output concentration GeoTIFF file.
        output_path (str): Path to output concentration GeoTIFF file.
        calculation_steps (list(int)): Calculation step (default: [-1] (last))
        calculate_maximum_concentration (bool):
          Use temporal maximum instead of specific timestep
        mode (str): Interpolation mode.
        progress_func(callable):
          Function that receives progress updates as float between 0 and 1
        netcdf(bool): Write a netCDF file instead of a GeoTIFF.

    The actual extent of the output will be the extent argument rounded
    to align with dem cells.
    """
    result_admin = ResultAdmin(
        gridadmin_path=gridadmin_path,
        results_3di_path=water_quality_results_3di_path,
        variable=variable,
    )
    assert result_admin.result_type == "Water Quality Results"

    try:
        CalculatorClass = calculator_classes[mode]
    except KeyError:
        raise ValueError("Unknown mode: '%s'" % mode)

    # handle calculation step
    if calculate_maximum_concentration:
        calculation_steps = [0]

    max_calculation_step = result_admin.get_timestamps().size - 1
    if calculation_steps is None:
        calculation_steps = [max_calculation_step]
    else:
        assert min(calculation_steps) >= 0
        assert max(calculation_steps) <= max_calculation_step, (
            "Maximum calculation step is '%s'." % max_calculation_step
        )

    # construct a prototype in-memory geotiff
    dx, _, xmin, _, dy, ymin = result_admin.grid.transform
    with AuxGeoTIFF(
        bbox=output_extent,
        origin=(xmin, ymin),
        cellsize=(dx, dy),
        projection=osr.GetUserInputAsWKT(f"EPSG:{result_admin.epsg_code}"),
    ) as prototype_path:

        # set up things
        progress_class = ProgressClass(
            calculation_steps=calculation_steps, progress_func=progress_func,
        )
        converter_kwargs = {
            "source_path": prototype_path,
            "target_path": output_path,
            "result_admin": result_admin,
            "calculation_steps": calculation_steps,
            "progress_func": None if progress_func is None else progress_class,
        }
        if netcdf:
            converter_class = NetcdfConverter
            converter_kwargs[
                "write_time_dimension"
            ] = not calculate_maximum_concentration
        else:
            converter_class = GeoTIFFConverter

        # calculate
        with converter_class(**converter_kwargs) as converter:
            calculator_kwargs_except_step = {
                "result_admin": result_admin,
                "dem_geo_transform": converter.geo_transform,
                "dem_shape": (converter.raster_y_size, converter.raster_x_size),
                "get_max_level": calculate_maximum_concentration
            }

            for band, calculation_step in progress_class:
                calculator_kwargs = {
                    "calculation_step": calculation_step,
                    **calculator_kwargs_except_step,
                }

                calculator = CalculatorClass(**calculator_kwargs)
                converter.convert_using(calculator=calculator, band=band)
