################################################################################
# oops/backplanes/orbit.py: Orbit backplanes
################################################################################

from polymath       import Scalar, Vector3, Matrix3
from oops.backplane import Backplane
from oops.body      import Body
from oops.frame     import Frame

def orbit_longitude(self, event_key, reference='obs', planet=None):
    """Gridless longitude on an orbit path relative to the central planet.

    Input:
        event_key       key defining the event on the orbit path.
        reference       defines the location of zero longitude.
                        'aries' for the First point of Aries;
                        'node'  for the J2000 ascending node;
                        'obs'   for the sub-observer longitude;
                        'sun'   for the sub-solar longitude;
                        'oha'   for the anti-observer longitude;
                        'sha'   for the anti-solar longitude, returning the
                                solar hour angle.
        planet          ID of the body at the center of the orbit; None for the
                        default, which is the parent of the targeted body.
    """

    if reference not in ('aries', 'node', 'obs', 'oha', 'sun', 'sha'):
        raise ValueError('invalid longitude reference: ' + repr(reference))

    # Determine/validate the planet
    event_key = Backplane.standardize_event_key(event_key)
    if planet is None:
        (body,_) = self.get_body_and_modifier(event_key[1])
        planet = body.parent.name

    # Get the event
    if reference in ('sun', 'sha'):
        orbit_event = self.get_gridless_event(event_key, arrivals=True)
    else:
        orbit_event = self.get_gridless_event(event_key)

    # Look up under the reference
    key0 = ('orbit_longitude', event_key)
    key = key0 + (reference, planet)
    if key in self.backplanes:
        return self.get_backplane(key)

    planet_body = Body.lookup(planet)
    planet_event = planet_body.path.event_at_time(orbit_event.time)
    planet_event = planet_event.wrt_frame(Frame.J2000)
    orbit_event = orbit_event.wrt(planet_body.path, Frame.J2000)

    # Locate reference vector in the J2000 frame
    if reference == 'obs':
        reference_dir = orbit_event.dep_ap
    elif reference == 'oha':
        reference_dir = -orbit_event.dep_ap
    elif reference == 'sun':
        reference_dir = orbit_event.neg_arr_ap
    elif reference == 'sha':
        reference_dir = orbit_event.arr_ap
    elif reference == 'aries':
        reference_dir = Vector3.XAXIS
    else:           # 'node'
        pole = orbit_event.pos.cross(orbit_event.vel)
        reference_dir = Vector3.ZAXIS.cross(pole)

    # This matrix rotates J2000 coordinates to a frame in which the Z-axis
    # is the orbit pole and the moon is instantaneously at the X-axis.
    matrix = Matrix3.twovec(orbit_event.pos, 0, orbit_event.vel, 1)

    # Locate the reference direction in this frame
    reference_wrt_orbit = matrix.rotate(reference_dir)
    ref_lon_wrt_orbit = reference_wrt_orbit.longitude(recursive=self.ALL_DERIVS)

    # Convert to an orbit with respect to the reference direction
    orbit_lon_wrt_ref = (-ref_lon_wrt_orbit) % Scalar.TWOPI
    return self.register_backplane(key, orbit_lon_wrt_ref)

################################################################################

# Add these functions to the Backplane module
Backplane._define_backplane_names(globals().copy())

################################################################################
