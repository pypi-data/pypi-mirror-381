################################################################################
# oops/frame/synchronousframe.py: Subclass SynchronousFrame of class Frame
################################################################################

from polymath       import Matrix3, Qube
from oops.frame     import Frame
from oops.transform import Transform

class SynchronousFrame(Frame):
    """A Frame subclass describing a a body that always keeps the x-axis pointed
    toward a central planet and the y-axis in the negative direction of motion.
    """

    FRAME_IDS = {}  # frame_id to use if a frame already exists upon un-pickling

    #===========================================================================
    def __init__(self, body_path, planet_path, frame_id=None, unpickled=False):
        """Constructor for a SynchronousFrame.

        Input:
            body_path       the path or path ID followed by the body.
            planet_path     the path or path ID followed by the central planet.
            frame_id        the ID to use; None to leave the frame unregistered.
            unpickled       True if this frame has been read from a pickle file.
        """

        self.body_path = Frame.PATH_CLASS.as_path(body_path)
        self.planet_path = Frame.PATH_CLASS.as_path(planet_path)
        self.path = Frame.PATH_CLASS.wrt(self.planet_path, self.body_path)

        if self.planet_path.shape:
            raise ValueError('SynchronousFrame requires a shapeless body path')

        self.frame_id  = frame_id
        self.reference = Frame.as_wayframe(self.planet_path.frame)
        self.origin    = self.planet_path.origin
        self.shape     = Qube.broadcasted_shape(self.body_path,
                                                self.planet_path)
        self.keys      = set()

        # Update wayframe and frame_id; register if not temporary
        self.register(unpickled=unpickled)

        # Save in internal dict for name lookup upon serialization
        if (not unpickled and self.shape == ()
            and self.frame_id in Frame.WAYFRAME_REGISTRY):
                key = (self.body_path.path_id, self.planet_path.path_id)
                SynchronousFrame.FRAME_IDS[key] = self.frame_id

    # Unpickled frames will always have temporary IDs to avoid conflicts
    def __getstate__(self):
        return (Frame.PATH_CLASS.as_primary_path(self.body_path),
                Frame.PATH_CLASS.as_primary_path(self.planet_path), self.shape)

    def __setstate__(self, state):
        # If this frame matches a pre-existing frame, re-use its ID
        (body_path, planet_path, shape) = state
        if shape == ():
            key = (body_path.path_id, planet_path.path_id)
            frame_id = SynchronousFrame.FRAME_IDS.get(key, None)
        else:
            frame_id = None

        self.__init__(body_path, planet_path, frame_id=frame_id,
                      unpickled=True)

    #===========================================================================
    def transform_at_time(self, time, quick=False):
        """The Transform into the this Frame at a Scalar of times."""

        event = self.path.event_at_time(time, quick=quick)
        matrix = Matrix3.twovec(event.pos, 0, event.vel, 1)
        omega = event.pos.cross(event.vel) / event.pos.dot(event.pos)

        return Transform(matrix, omega, self.frame_id, self.reference,
                                        self.body_path)

################################################################################
