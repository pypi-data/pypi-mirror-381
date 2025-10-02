################################################################################
# oops/frame/rotation.py: Subclass Rotation of class Frame
################################################################################

import numpy as np

from polymath       import Matrix3, Qube, Scalar, Vector3
from oops.fittable  import Fittable
from oops.frame     import Frame
from oops.transform import Transform

class Rotation(Frame, Fittable):
    """A Frame describing a fixed rotation about one axis of another frame."""

    FRAME_IDS = {}  # frame_id to use if a frame already exists upon un-pickling

    #===========================================================================
    def __init__(self, angle, axis, reference, frame_id=None, unpickled=False):
        """Constructor for a Rotation Frame.

        Input:
            angle       the angle of rotation in radians. Can be a Scalar
                        containing multiple values.
            axis        the rotation axis: 0 for x, 1 for y, 2 for z.
            reference   the frame relative to which this rotation is defined.
            frame_id    the ID to use; None to leave the frame unregistered.
            unpickled   True if this frame has been read from a pickle file.
        """

        self.angle = Scalar.as_scalar(angle)

        self.axis2 = axis           # Most often, the Z-axis
        self.axis0 = (self.axis2 + 1) % 3
        self.axis1 = (self.axis2 + 2) % 3

        self.frame_id  = frame_id
        self.reference = Frame.as_wayframe(reference)
        self.origin    = self.reference.origin
        self.keys      = set()

        self.shape = Qube.broadcasted_shape(self.angle, self.reference)

        mat = np.zeros(self.shape + (3,3))
        mat[..., self.axis2, self.axis2] = 1.
        mat[..., self.axis0, self.axis0] = np.cos(self.angle.vals)
        mat[..., self.axis0, self.axis1] = np.sin(self.angle.vals)
        mat[..., self.axis1, self.axis1] =  mat[..., self.axis0, self.axis0]
        mat[..., self.axis1, self.axis0] = -mat[..., self.axis0, self.axis1]

        # Update wayframe and frame_id; register if not temporary
        self.register(unpickled=unpickled)

        # We need a wayframe before we can create the transform
        self.transform = Transform(Matrix3(mat, self.angle.mask), Vector3.ZERO,
                                   self.wayframe, self.reference, self.origin)

        # Save in internal dict for name lookup upon serialization
        if (not unpickled and self.shape == ()
            and self.frame_id in Frame.WAYFRAME_REGISTRY):
                key = (self.angle.vals, self.axis2, self.reference.frame_id)
                Rotation.FRAME_IDS[key] = self.frame_id

    def __getstate__(self):
        return (self.angle, self.axis2,
                Frame.as_primary_frame(self.reference), self.shape)

    def __setstate__(self, state):
        # If this frame matches a pre-existing frame, re-use its ID
        (angle, axis, reference, shape) = state
        if shape == ():
            key = (angle.vals, axis, reference.frame_id)
            frame_id = Rotation.FRAME_IDS.get(key, None)
        else:
            frame_id = None

        self.__init__(angle, axis, reference, frame_id=frame_id, unpickled=True)

    #===========================================================================
    def transform_at_time(self, time, quick=False):
        """Transform into this Frame at a Scalar of times."""

        return self.transform

    ############################################################################
    # Fittable interface
    ############################################################################

    def set_params(self, params):
        """Redefine the Fittable object, using this set of parameters.

        In this case, params is the set of angles of rotation.

        Input:
            params      a list, tuple or 1-D Numpy array of floating-point
                        numbers, defining the parameters to be used in the
                        object returned.
        """

        params = Scalar.as_scalar(params)
        if params.shape != self.shape:
            raise ValueError('new parameter shape does not match original')

        self.angle = params

        mat = np.zeros(self.shape + (3,3))
        mat[..., self.axis2, self.axis2] = 1.
        mat[..., self.axis0, self.axis0] = np.cos(self.angle.vals)
        mat[..., self.axis0, self.axis1] = np.sin(self.angle.vals)
        mat[..., self.axis1, self.axis1] =  mat[..., self.axis0, self.axis0]
        mat[..., self.axis1, self.axis0] = -mat[..., self.axis0, self.axis1]

        self.transform = Transform(Matrix3(mat, self.angle.mask), Vector3.ZERO,
                                   self.reference, self.origin)

    #===========================================================================
    def get_params(self):
        """The current set of parameters defining this fittable object.

        Return:         a Numpy 1-D array of floating-point numbers containing
                        the parameter values defining this object.
        """

        return self.angle.vals

    #===========================================================================
    def copy(self):
        """A deep copy of the given object.

        The copy can be safely modified without affecting the original.
        """

        return Rotation(self.angle.copy(), self.axis, self.reference_id)

################################################################################
