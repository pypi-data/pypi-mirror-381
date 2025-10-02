################################################################################
# oops/fov/flatfov.py: FlatFOV subclass of class FOV
################################################################################

import numpy as np

from polymath import Pair
from oops.fov import FOV

class FlatFOV(FOV):
    """FOV subclass that describes a field of view that is free of distortion,
    implementing an exact pinhole ("gnomonic") camera model.
    """

    #===========================================================================
    def __init__(self, uv_scale, uv_shape, uv_los=None, uv_area=None):
        """Constructor for a FlatFOV.

        The U-axis is assumed to align with X and the V-axis aligns with Y.

        Input:
            uv_scale    a single value, tuple or Pair defining the ratios dx/du
                        and dy/dv. For example, if (u,v) are in units of
                        arcseconds, then
                            uv_scale = Pair((pi/180/3600.,pi/180/3600.))
                        Use the sign of the second element to define the
                        direction of increasing V: negative for up, positive for
                        down.

            uv_shape    a single value, tuple or Pair defining size of the field
                        of view in pixels. This number can be non-integral if
                        the detector is not composed of a rectangular array of
                        pixels.

            uv_los      a single value, tuple or Pair defining the (u,v)
                        coordinates of the nominal line of sight. By default,
                        this is the midpoint of the rectangle, i.e, uv_shape/2.

            uv_area     an optional parameter defining the nominal field of view
                        of a pixel. If not provided, the area is calculated
                        based on the area of the central pixel.
        """

        self.uv_scale = Pair.as_pair(uv_scale).as_float().as_readonly()
        self.uv_shape = Pair.as_pair(uv_shape).as_readonly()

        if uv_los is None:
            self.uv_los = self.uv_shape / 2.
        else:
            self.uv_los = Pair.as_pair(uv_los).as_float().as_readonly()

        if uv_area is None:
            self.uv_area = np.abs(self.uv_scale.vals[0] * self.uv_scale.vals[1])
        else:
            self.uv_area = uv_area

        scale = Pair.as_pair(uv_scale).as_readonly()

        self.dxy_duv = Pair([[  scale.vals[0], 0.],
                             [0.,   scale.vals[1]]], drank=1).as_readonly()
        self.duv_dxy = Pair([[1/scale.vals[0], 0.],
                             [0., 1/scale.vals[1]]], drank=1).as_readonly()

    def __getstate__(self):
        return (self.uv_scale, self.uv_shape, self.uv_los, self.uv_area)

    def __setstate__(self, state):
        self.__init__(*state)

    #===========================================================================
    def xy_from_uvt(self, uv_pair, time=None, derivs=False, remask=False):
        """The (x,y) camera frame coordinates given FOV coordinates (u,v).

        Input:
            uv_pair     (u,v) coordinate Pair in the FOV.
            time        Scalar of optional absolute times. Ignored by FlatFOV.
            derivs      If True, any derivatives in (u,v) get propagated into
                        the returned (x,y) Pair.
            remask      True to mask (u,v) coordinates outside the field of
                        view; False to leave them unmasked.

        Return:         Pair of same shape as uv_pair, giving the transformed
                        (x,y) coordinates in the camera's frame.
        """

        uv_pair = Pair.as_pair(uv_pair, recursive=derivs)
        if remask:
            uv_pair = uv_pair.mask_or(self.is_outside(uv_pair).vals)

        return (uv_pair - self.uv_los).element_mul(self.uv_scale)

    #===========================================================================
    def uv_from_xyt(self, xy_pair, time=None, derivs=False, remask=False):
        """The (u,v) FOV coordinates given (x,y) camera frame coordinates.

        Input:
            xy_pair     (x,y) Pair in FOV coordinates.
            time        Scalar of optional absolute times. Ignored by FlatFOV.
            derivs      If True, any derivatives in (x,y) get propagated into
                        the returned (u,v) Pair.
            remask      True to mask (u,v) coordinates outside the field of
                        view; False to leave them unmasked.

        Return:         Pair of same shape as xy_pair, giving the computed (u,v)
                        FOV coordinates.
        """

        xy_pair = Pair.as_pair(xy_pair, recursive=derivs)
        uv_pair = xy_pair.element_div(self.uv_scale) + self.uv_los
        if remask:
            uv_pair = uv_pair.mask_or(self.is_outside(uv_pair).vals)

        return uv_pair

################################################################################
