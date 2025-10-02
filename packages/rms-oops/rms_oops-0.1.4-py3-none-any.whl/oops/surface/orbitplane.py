################################################################################
# oops/surface/orbitplane.py: OrbitPlane subclass of class Surface
################################################################################

import numpy as np

from polymath                 import Scalar, Vector3
from oops.constants           import PI, TWOPI
from oops.frame.frame_        import Frame
from oops.frame.inclinedframe import InclinedFrame
from oops.frame.spinframe     import SpinFrame
from oops.path.path_          import Path
from oops.path.circlepath     import CirclePath
from oops.surface.surface_    import Surface
from oops.surface.ringplane   import RingPlane

class OrbitPlane(Surface):
    """A subclass of the Surface class describing a flat surface sharing its
    geometric center and tilt with a body on an eccentric and/or inclined orbit.
    The orbit is described as circle offset from the center of the planet by a
    distance ae; this approximation is only accurate to first order in
    eccentricty.

    The coordinate system consists of cylindrical coordinates (a, theta, z)
    where a is the mean radius of the orbit. The zero of longitude is aligned
    with the pericenter.

    The system is masked outside the semimajor axis, but unmasked inside.
    However, coordinates and intercepts are calculated at all locations.
    """

    COORDINATE_TYPE = 'polar'
    IS_VIRTUAL = False

    #===========================================================================
    def __init__(self, elements, epoch, origin, frame, path_id=None,
                       radii=None):
        """Constructor for an OrbitPlane surface.

            elements    a tuple containing three, six or nine orbital elements:
                a           mean radius of orbit, km.
                lon         mean longitude at epoch of a reference object, in
                            radians. This is provided if the user wishes to
                            track a moving body in the plane. However, it does
                            not affect the surface or its coordinate system.
                n           mean motion of a body orbiting within the ring, in
                            radians/sec. This affects velocities returned by
                            the surface but not the surface or its coordinate
                            system.

                e           orbital eccentricity.
                peri        longitude of pericenter at epoch, radians.
                prec        pericenter precession rate, radians/sec.

                i           inclination, radians.
                node        longitude of ascending node at epoch, radians.
                regr        nodal regression rate, radians/sec, NEGATIVE!

            epoch       the time TDB relative to which all orbital elements are
                        defined.
            origin      the path or ID of the planet center.
            frame       the frame or ID of the frame in which the orbit is
                        defined. Should be inertial.
            path_id     the ID under which to register the orbit path; None to
                        leave it unregistered
            radii       the nominal inner and outer radii of the ring, in km.
                        None for a ring with no radial limits.

        Note that the origin and frame used by the returned OrbitPlane object
        will differ from those used to define it here.
        """

        # Save the initial center path and frame. The frame should be inertial.
        self.defined_origin = Path.as_waypoint(origin)
        self.defined_frame  = Frame.as_wayframe(frame)
        if self.defined_frame.origin is not None:
            raise ValueError('frame of an OrbitPlane must be inertial')

        # We will update the surface's actual path and frame as needed
        self.internal_origin = self.defined_origin
        self.internal_frame  = self.defined_frame

        # Save the orbital elements
        self.elements = np.asarray(elements, dtype=np.float64)
        self.a     = elements[0]
        self.lon   = elements[1]
        self.n     = elements[2]
        self.epoch = float(epoch)

        if radii is None:
            self.radii = None
        else:
            self.radii    = np.asarray(radii, dtype=np.float64)
            self.radii_sq = self.radii**2

        # Interpret the inclination
        self.has_inclination = (len(elements) >= 9)
        if self.has_inclination:
            self.i = elements[6]
            self.has_inclination = (self.i != 0)

        # If the orbit is inclined, define a special-purpose inclined frame
        if self.has_inclination:
            if path_id is None:
                frame_id = None
            else:
                frame_id = path_id + '_INCLINATION'

            self.inclined_frame = InclinedFrame(inc = elements[6],
                                                node = elements[7],
                                                rate = elements[8],
                                                epoch = self.epoch,
                                                reference = self.internal_frame,
                                                despin = True,
                                                frame_id = frame_id)
            self.internal_frame = self.inclined_frame
        else:
            self.inclined_frame = None

        # The inclined frame changes its tilt relative to the equatorial plane,
        # accounting for nodal regression, but does not change the reference
        # longitude from that used by the initial frame.

        # Interpret the eccentricity
        self.has_eccentricity = (len(elements) >= 6)
        if self.has_eccentricity:
            self.e = elements[3]
            self.has_eccentricity = (self.e != 0)

        # If the orbit is eccentric, construct a special-purpose path defining
        # the center of the displaced ring
        if self.has_eccentricity:
            self.ae = self.a * self.e
            self.lon_sub_peri = self.lon - elements[4]
            self.n_sub_prec = self.n - elements[5]

            if path_id is None:
                new_path_id = None
            else:
                new_path_id = path_id + '_ECCENTRICITY'

            self.peri_path = CirclePath(radius = elements[0] * elements[3],# a*e
                                        lon = elements[4] + PI,     # apocenter
                                        rate = elements[5],         # precession
                                        epoch = self.epoch,
                                        origin = self.internal_origin,
                                        frame = self.internal_frame,
                                        path_id = new_path_id)
            self.internal_origin = self.peri_path

            # The peri_path circulates around the initial origin but does not
            # rotate.

            if path_id is None:
                frame_id = None
            else:
                frame_id = path_id + '_PERICENTER'

            self.spin_frame = SpinFrame(offset = elements[4],       # pericenter
                                        rate = elements[5],         # precession
                                        epoch = self.epoch,
                                        axis = 2,
                                        reference = self.internal_frame,
                                        frame_id = frame_id)
            self.internal_frame = self.spin_frame

        else:
            self.peri_path = None
            self.spin_frame = None

        self.ringplane = RingPlane(origin = self.internal_origin,
                                   frame = self.internal_frame,
                                   radii = self.radii,
                                   gravity = None,
                                   elevation = 0.)

        # The primary origin and frame for the orbit
        self.origin = self.internal_origin.waypoint
        self.frame = self.internal_frame.wayframe

        # Unique key for intercept calculations
        # ('ring', origin, frame, elevation, i, node, dnode_dt, epoch)
        if self.has_inclination:
            extras = tuple(elements[6:9]) + (self.epoch,)
        else:
            extras = (0., 0., 0., 0.)

        self.intercept_key = ('ring', self.defined_origin.waypoint,
                                      self.defined_frame.wayframe,
                                      0.) + extras

        # Save the unmasked version of this surface
        if self.radii is None:
            self.unmasked = self
        else:
            self.unmasked = OrbitPlane.__new__(type(OrbitPlane))
            self.unmasked.__dict__ = self.__dict__.copy()
            self.unmasked.radii = None

    def __getstate__(self):
        return (tuple(self.elements), self.epoch,
                Path.as_primary_path(self.defined_origin),
                Frame.as_primary_frame(self.defined_frame),
                None, self.radii)

    def __setstate__(self, state):
        self.__init__(*state)

    #===========================================================================
    def coords_from_vector3(self, pos, obs=None, time=None, axes=2,
                                       derivs=False, hints=None):
        """Surface coordinates associated with a position vector.

        Input:
            pos         a Vector3 of positions at or near the surface, relative
                        to this surface's origin and frame.
            obs         a Vector3 of observer position relative to this
                        surface's origin and frame; ignored for this Surface
                        subclass.
            time        a Scalar time at which to evaluate the surface.
            axes        2 or 3, indicating whether to return the first two
                        coordinates (rad, theta) or all three (rad, theta, z) as
                        Scalars.
            derivs      True to propagate any derivatives inside pos and obs
                        into the returned coordinates.
            hints       ignored. Provided for compatibility with other Surface
                        subclasses.

        Return:         coordinate values packaged as a tuple containing two or
                        three Scalars, one for each coordinate.
            rad         mean orbital radius in the ring plane, in km.
            theta       mean longitude in radians of the intercept point.
            z           vertical distance in km above the orbit plane; included
                        if axes == 3.
        """

        return self.ringplane.coords_from_vector3(pos, axes=axes, time=time,
                                                  derivs=derivs)

    #===========================================================================
    def vector3_from_coords(self, coords, obs=None, time=None, derivs=False):
        """The position where a point with the given coordinates falls relative
        to this surface's origin and frame.

        Input:
            coords      a tuple of two or three Scalars defining coordinates at
                        or near this surface. These can have different shapes,
                        but must be broadcastable to a common shape.
                rad     mean orbital radius in the ring plane, in km.
                theta   mean longitude in radians of the intercept point.
                z       vertical distance in km above the orbit plane.
            obs         a Vector3 of observer position relative to this
                        surface's origin and frame; ignored for this Surface
                        subclass.
            time        a Scalar time at which to evaluate the surface.
            derivs      True to propagate any derivatives inside the coordinates
                        and obs into the returned position vectors.

        Return:         a Vector3 of points defined by the coordinates, relative
                        to this surface's origin and frame.
        """

        return self.ringplane.vector3_from_coords(coords, time=time,
                                                  derivs=derivs)

    #===========================================================================
    def intercept(self, obs, los, time=None, direction='dep', derivs=False,
                                  guess=None, hints=None):
        """The position where a specified line of sight intercepts the surface.

        Input:
            obs         observer position as a Vector3 relative to this
                        surface's origin and frame.
            los         line of sight as a Vector3 in this surface's frame.
            time        a Scalar time at the surface.
            direction   'arr' for a photon arriving at the surface; 'dep' for a
                        photon departing from the surface; ignored.
            derivs      True to propagate any derivatives inside obs and los
                        into the returned intercept point.
            guess       unused.
            hints       if not None (the default), this value is appended to the
                        returned tuple. Needed for compatibility with other
                        Surface subclasses.

        Return:         a tuple (pos, t) or (pos, t, hints), where
            pos         a Vector3 of intercept points on the surface relative
                        to this surface's origin and frame, in km.
            t           a Scalar such that:
                            position = obs + t * los
            hints       the input value of hints, included if it is not None.
        """

        return self.ringplane.intercept(obs, los, time=time, derivs=derivs,
                                        guess=guess, hints=hints)

    #===========================================================================
    def normal(self, pos, time=None, derivs=False):
        """The normal vector at a position at or near a surface.

        Input:
            pos         a Vector3 of positions at or near the surface relative
                        to this surface's origin and frame.
            time        a Scalar time at which to evaluate the surface; ignored.
            derivs      True to propagate any derivatives of pos into the
                        returned normal vectors.

        Return:         a Vector3 containing directions normal to the surface
                        that pass through the position. Lengths are arbitrary.
        """

        return self.ringplane.normal(pos, time=time, derivs=derivs)

    #===========================================================================
    def velocity(self, pos, time=None):
        """The local velocity vector at a point within the surface.

        This can be used to describe the orbital motion of ring particles or
        local wind speeds on a planet.

        Input:
            pos         a Vector3 of positions at or near the surface relative
                        to this surface's origin and frame.
            time        a Scalar time at which to evaluate the surface; ignored.

        Return:         a Vector3 of velocities, in units of km/s.
        """

        if self.has_eccentricity:
            # For purposes of a first-order velocity calculation, we can assume
            # that the difference between mean longitude and true longitude, in
            # a planet-centered frame, is small.
            #
            # In an inertial, planet-centered frame:
            #
            # r = a - ae cos(lon - peri)
            # lon = lon0 + n * (time - epoch) + 2ae sin(lon - peri)
            #
            # dr/dt = ae sin(lon - peri) (n - prec)
            # dlon/dt = n + 2ae cos(n - peri) (n - prec)
            #
            # In a frame rotating at rate = prec:
            #
            # dr/dt = ae sin(lon - peri) (n - prec)
            # dlon/dt = (n - prec) + 2ae cos(lon - peri) (n - prec)
            #
            # x = r cos(lon)
            # y = r sin(lon)
            #
            # dx/dt = dr/dt * cos(lon) - r sin(lon) dlon/dt
            # dy/dy = dr/dt * sin(lon) + r cos(lon) dlon/dt

            (x,y,z) = pos.to_scalars()
            x = x + self.ae         # shift origin to center of planet

            r = (x**2 + y**2).sqrt()
            cos_lon_sub_peri = x/r
            sin_lon_sub_peri = y/r

            dr_dt = sin_lon_sub_peri * (self.ae * self.n_sub_prec)
            r_dlon_dt = r * self.n_sub_prec * (cos_lon_sub_peri * 2*self.ae + 1)

            dx_dt = dr_dt * cos_lon_sub_peri - r_dlon_dt * sin_lon_sub_peri
            dy_dt = dr_dt * sin_lon_sub_peri + r_dlon_dt * cos_lon_sub_peri

            return Vector3.from_scalars(dx_dt, dy_dt, 0.)

        else:
            return self.n * Vector3.ZAXIS.cross(pos)

    ############################################################################
    # Longitude-anomaly conversions
    ############################################################################

    def from_mean_anomaly(self, anom):
        """The longitude in this frame based on the mean anomaly.

        Accurate to first order in eccentricity.
        """

        anom = Scalar.as_scalar(anom)

        if not self.has_eccentricity:
            return anom
        else:
            return anom + (2*self.ae) * anom.sin()

    #===========================================================================
    def to_mean_anomaly(self, lon):
        """The mean anomaly given an orbital longitude.

        Accurate to first order in eccentricity. Iteration is performed using
        Newton's method to ensure that this function is an exact inverse of
        from_mean_anomaly().
        """

        lon = Scalar.as_scalar(lon)
        if not self.has_eccentricity:
            return lon

        # Solve lon = x + 2ae sin(x)
        #
        # Let
        #   y(x) = x + 2ae sin(x) - lon
        #
        #   dy/dx = 1 + 2ae cos(x)
        #
        # For x[n] as a guess at n,
        #   x[n+1] = x[n] - y(x[n]) / dy/dx

        ae_x2 = 2 * self.ae
        x = lon - ae_x2 * lon.sin()

        # Iterate until all improvement ceases. Should not take long
        prev_max_abs_dx = TWOPI
        max_abs_dx = PI
        while (max_abs_dx < prev_max_abs_dx):
            dx = (lon - x - ae_x2 * x.sin()) / (x.cos() * ae_x2 + 1)
            x += dx

            prev_max_abs_dx = max_abs_dx
            max_abs_dx = abs(dx).max()

        return x

################################################################################
