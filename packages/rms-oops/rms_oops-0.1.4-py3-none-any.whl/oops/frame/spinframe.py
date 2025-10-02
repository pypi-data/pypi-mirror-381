################################################################################
# oops/frame/spinframe.py: Subclass SpinFrame of class Frame
################################################################################

import numpy as np

from polymath       import Matrix3, Qube, Scalar, Vector3
from oops.frame     import Frame
from oops.transform import Transform

class SpinFrame(Frame):
    """A Frame subclass describing a frame in uniform rotation about one axis of
    another frame.

    It can be created without a frame_id, reference_id or origin_id; in this
    case it is not registered and can therefore be used as a component of
    another frame.
    """

    FRAME_IDS = {}  # frame_id to use if a frame already exists upon un-pickling

    #===========================================================================
    def __init__(self, offset, rate, epoch, axis, reference, frame_id=None,
                       unpickled=False):
        """Constructor for a Spin Frame.

        Input:
            offset      the angular offset of the frame at the epoch.
            rate        the rotation rate of the frame in radians/second.
            epoch       the time TDB at which the frame is defined.
            axis        the rotation axis: 0 for x, 1 for y, 2 for z.
            reference   the frame relative to which this frame is defined.
            frame_id    the ID under which this frame is to be registered;
                        None to use a temporary ID.
            unpickled   True if this frame has been read from a pickle file.

        Note that rate, offset and epoch can be Scalar values, in which case the
        shape of the SpinFrame is defined by broadcasting the shapes of these
        Scalars.
        """

        self.offset = Scalar.as_scalar(offset)
        self.rate = Scalar.as_scalar(rate)
        self.epoch = Scalar.as_scalar(epoch)

        self.shape = Qube.broadcasted_shape(self.rate, self.offset, self.epoch)

        self.axis2 = axis           # Most often, the Z-axis
        self.axis0 = (self.axis2 + 1) % 3
        self.axis1 = (self.axis2 + 2) % 3

        omega_vals = np.zeros(list(self.shape) + [3])
        omega_vals[..., self.axis2] = self.rate.vals
        self.omega = Vector3(omega_vals, self.rate.mask)

        # Required attributes
        self.frame_id  = frame_id
        self.reference = Frame.as_wayframe(reference)
        self.origin    = self.reference.origin or Frame.PATH_CLASS.SSB
        self.keys      = set()

        # Update wayframe and frame_id; register if not temporary
        self.register(unpickled=unpickled)

        # Save in internal dict for name lookup upon serialization
        if (not unpickled and self.shape == ()
            and self.frame_id in Frame.WAYFRAME_REGISTRY):
                key = (self.offset.vals, self.rate.vals, self.epoch.vals,
                       self.axis2, self.reference.frame_id)
                SpinFrame.FRAME_IDS[key] = self.frame_id

    # Unpickled frames will always have temporary IDs to avoid conflicts
    def __getstate__(self):
        return (self.offset, self.rate, self.epoch, self.axis2,
                Frame.as_primary_frame(self.reference), self.shape)

    def __setstate__(self, state):
        # If this frame matches a pre-existing frame, re-use its ID
        (offset, rate, epoch, axis2, reference, shape) = state
        if shape == ():
            key = (offset.vals, rate.vals, epoch.vals, axis2,
                   reference.frame_id)
            frame_id = SpinFrame.FRAME_IDS.get(key, None)
        else:
            frame_id = None

        self.__init__(offset, rate, epoch, axis2, reference, frame_id=frame_id,
                      unpickled=True)

    #===========================================================================
    def transform_at_time(self, time, quick={}):
        """The Transform to this Frame at a specified Scalar of times.

        QuickFrame options are ignored.
        """

        time = Scalar.as_scalar(time)
        angle = (time - self.epoch) * self.rate + self.offset

        mat = np.zeros(list(angle.shape) + [3,3])
        mat[..., self.axis2, self.axis2] = 1.
        mat[..., self.axis0, self.axis0] = np.cos(angle.values)
        mat[..., self.axis1, self.axis1] = mat[..., self.axis0, self.axis0]
        mat[..., self.axis0, self.axis1] = np.sin(angle.values)
        mat[..., self.axis1, self.axis0] = -mat[...,self.axis0,self.axis1]

        matrix = Matrix3(mat, angle.mask)
        return Transform(matrix, self.omega, self.wayframe, self.reference,
                                 self.origin)

################################################################################
