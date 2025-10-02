################################################################################
# oops/frame/poleframe.py: Subclass PoleFrame of class Frame
################################################################################

import numpy as np

from polymath       import Matrix3, Qube, Scalar, Vector3
from oops.frame     import Frame
from oops.transform import Transform

class PoleFrame(Frame):
    """A Frame subclass describing a non-rotating frame centered on the Z-axis
    of a body's pole vector.

    This differs from RingFrame in that the pole may precess around a separate,
    invariable pole for the system. Because of this behavior, the reference
    longitude is defined as the ascending node of the invariable plane rather
    than as the ascending node of the ring plane. This frame is recommended for
    Neptune in particular.
    """

    FRAME_IDS = {}  # frame_id to use if a frame already exists upon un-pickling

    #===========================================================================
    def __init__(self, frame, pole, retrograde=False, aries=False, frame_id='+',
                       cache_size=1000, unpickled=False):
        """Constructor for a PoleFrame.

        Input:
            frame       a (possibly) rotating frame, or its ID, describing the
                        central planet relative to J2000. This is typically a
                        body's rotating SpiceFrame.

            pole        The pole of the invariable plane, about which planet's
                        pole precesses. This enables the reference longitude to
                        be defined properly. Defined in J2000 coordinates.

            retrograde  True to flip the sign of the Z-axis. Necessary for
                        retrograde systems like Uranus.

            aries       True to use the First Point of Aries as the longitude
                        reference; False to use the ascending node of the
                        invariable plane. Note that the former might be
                        preferred in a situation where the invariable pole is
                        uncertain, because small changes in the invariable pole
                        will have only a limited effect on the absolute
                        reference longitude.

            frame_id    the ID under which the frame will be registered. None to
                        leave the frame unregistered. If the value is "+", then
                        the registered name is the planet frame's name with the
                        suffix "_POLE". Note that this default ID will not be
                        unique if frames are defined for multiple Laplace Planes
                        around the same planet.

            cache_size  number of transforms to cache. This can be useful
                        because it avoids unnecessary SPICE calls when the frame
                        is being used repeatedly at a finite set of times.

            unpickled   True if this frame has been read from a pickle file.
        """

        # Rotates from J2000 to the invariable frame
        pole = Vector3.as_vector3(pole)
        (ra, dec, _) = pole.to_ra_dec_length(recursive=False)
        self.invariable_matrix = Matrix3.pole_rotation(ra,dec)
            # Rotates J2000 coordinates into a frame where the Z-axis is the
            # invariable pole and the X-axis is the ascending node of the
            # invariable plane on J2000
        self.invariable_pole = pole
        self.invariable_node = Vector3.ZAXIS.ucross(pole)

        self.aries = bool(aries)
        if self.aries:
            # The ascending node of the invariable plane falls 90 degrees ahead
            # pole's RA
            self.invariable_node_lon = ra + np.pi/2.
        else:
            self.invariable_node_lon = 0.

        self.planet_frame = Frame.as_frame(frame).wrt(Frame.J2000)
        self.origin = self.planet_frame.origin
        self.retrograde = bool(retrograde)
        self.keys = set()
        self.reference = Frame.J2000
        self.shape = Qube.broadcasted_shape(self.invariable_pole,
                                            self.planet_frame)

        # Define cache
        self.cache = {}
        self.trim_size = max(cache_size//10, 1)
        self.given_cache_size = cache_size
        self.cache_size = cache_size + self.trim_size
        self.cache_counter = 0
        self.cached_value_returned = False          # Just used for debugging

        # Fill in the frame ID
        if frame_id is None:
            self.frame_id = Frame.temporary_frame_id()
        elif frame_id == '+':
            self.frame_id = self.planet_frame.frame_id + '_POLE'
        elif frame_id.startswith('+'):
            self.frame_id = self.planet_frame.frame_id + '_' + frame_id[1:]
        else:
            self.frame_id = frame_id

        # Register if necessary
        self.register(unpickled=unpickled)

        # Save in internal dict for name lookup upon serialization
        if (not unpickled and self.shape == ()
            and self.frame_id in Frame.WAYFRAME_REGISTRY):
                key = (self.planet_frame.frame_id,
                       tuple(self.invariable_pole.vals),
                       retrograde, aries)
                PoleFrame.FRAME_IDS[key] = self.frame_id

    # Unpickled frames will always have temporary IDs to avoid conflicts
    def __getstate__(self):
        return (Frame.as_primary_frame(self.planet_frame),
                self.invariable_pole, self.retrograde,
                self.aries, self.given_cache_size, self.shape)

    def __setstate__(self, state):
        # If this frame matches a pre-existing frame, re-use its ID
        (frame, pole, retrograde, aries, cache_size, shape) = state
        if shape == ():
            key = (frame.frame_id, tuple(pole.vals), retrograde, aries)
            frame_id = PoleFrame.FRAME_IDS.get(key, None)
        else:
            frame_id = None

        self.__init__(frame, pole, retrograde, aries, frame_id=frame_id,
                      cache_size=cache_size, unpickled=True)

    #===========================================================================
    def transform_at_time(self, time, quick={}):
        """The Transform into the this Frame at a Scalar of times."""

        time = Scalar.as_scalar(time)

        # Check cache first if time is a Scalar
        if time.shape == ():
            key = time.values

            if key in self.cache:
                self.cached_value_returned = True
                (count, key, xform) = self.cache[key]
                self.cache_counter += 1
                count[0] = self.cache_counter
                return xform

        self.cached_value_returned = False

        # Calculate the planet frame for the current time in J2000
        xform = self.planet_frame.transform_at_time(time, quick=quick)

        # The bottom row of the matrix is the Z-axis of the ring frame in J2000
        z_axis = xform.matrix.row_vector(2)

        # For a retrograde ring, reverse Z
        if self.retrograde:
            z_axis = -z_axis

        planet_matrix = Matrix3.twovec(z_axis, 2,
                                       Vector3.ZAXIS.cross(z_axis), 0)

        # This is the RingFrame matrix. It rotates from J2000 to the frame where
        # the pole at epoch is along the Z-axis and the ascending node relative
        # to the J2000 equator is along the X-axis.

        # Locate the J2000 ascending node of the RingFrame on the invariable
        # plane.
        planet_pole_j2000 = planet_matrix.inverse() * Vector3.ZAXIS
        joint_node_j2000 = self.invariable_pole.cross(planet_pole_j2000)

        joint_node_wrt_planet = planet_matrix * joint_node_j2000
        joint_node_wrt_frame = self.invariable_matrix * joint_node_j2000

        node_lon_wrt_planet = joint_node_wrt_planet.to_ra_dec_length()[0]
        node_lon_wrt_frame = joint_node_wrt_frame.to_ra_dec_length()[0]

        # Align the X-axis with the node of the invariable plane
        matrix = Matrix3.z_rotation(node_lon_wrt_planet - node_lon_wrt_frame +
                                    self.invariable_node_lon) * planet_matrix

        # Create the transform
        xform = Transform(Matrix3(matrix, xform.matrix.mask), Vector3.ZERO,
                          self.wayframe, self.reference, self.origin)

        # Cache the transform if necessary
        if time.shape == () and self.given_cache_size > 0:

            # Trim the cache, removing the values used least recently
            if len(self.cache) >= self.cache_size:
                all_keys = list(self.cache.values())
                all_keys.sort()
                for (_, old_key, _) in all_keys[:self.trim_size]:
                    del self.cache[old_key]

            # Insert into the cache
            key = time.values
            self.cache_counter += 1
            count = np.array([self.cache_counter])
            self.cache[key] = (count, key, xform)

        return xform

    #===========================================================================
    def node_at_time(self, time, quick={}):
        """Angle from the frame's X-axis to the ring plane ascending node on the
        invariable plane.
        """

        # Calculate the pole for the current time
        xform = self.planet_frame.transform_at_time(time, quick=quick)

        # The bottom row of the matrix is the pole in J2000 coordinates
        z_axis = xform.matrix.row_vector(2)
        if self.retrograde:
            z_axis = -z_axis

        # Locate this pole relative to the invariable plane
        z_axis_wrt_invar = self.invariable_matrix * z_axis

        # The ascending node is 90 degrees ahead of the pole
        (x, y, _) = z_axis_wrt_invar.to_scalars()

        node = (y.arctan2(x) + Scalar.HALFPI + self.invariable_node_lon)
        return node % Scalar.TWOPI

################################################################################
