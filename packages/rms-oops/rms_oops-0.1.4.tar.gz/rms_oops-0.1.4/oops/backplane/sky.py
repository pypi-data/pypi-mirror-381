################################################################################
# oops/backplanes/sky.py: Sky plane (celestial coordinates) backplanes
################################################################################

import numpy as np

from polymath       import Scalar, Vector3
from oops.backplane import Backplane
from oops.frame     import Frame

def right_ascension(self, event_key=(), apparent=True, direction='arr'):
    """Right ascension of the arriving or departing photon

    Optionally, it allows for stellar aberration.

    Input:
        event_key       key defining the surface event, typically () to refer to
                        the observation.
        apparent        True to return the apparent direction of photons in the
                        frame of the event; False to return the purely geometric
                        directions of the photons.
        direction       'arr' to return the direction of an arriving photon;
                        'dep' to return the direction of a departing photon.
    """

    event_key = Backplane.standardize_event_key(event_key)
    key = ('right_ascension', event_key, apparent, direction)
    if key not in self.backplanes:
        self._fill_ra_dec(event_key, apparent, direction)

    return self.get_backplane(key)

#===============================================================================
def declination(self, event_key=(), apparent=True, direction='arr'):
    """Declination of the arriving or departing photon.

    Optionally, it allows for stellar aberration.

    Input:
        event_key       key defining the surface event, typically () to refer to
                        the observation.
        apparent        True to return the apparent direction of photons in the
                        frame of the event; False to return the purely geometric
                        directions of the photons.
        direction       'arr' to base the direction on an arriving photon;
                        'dep' to base the direction on a departing photon.
    """

    event_key = Backplane.standardize_event_key(event_key)
    key = ('declination', event_key, apparent, direction)
    if key not in self.backplanes:
        self._fill_ra_dec(event_key, apparent, direction)

    return self.get_backplane(key)

#===============================================================================
def _fill_ra_dec(self, event_key, apparent, direction):
    """Fill internal backplanes of RA and dec."""

    if direction not in ('arr', 'dep'):
        raise ValueError('invalid photon direction: ' + direction)

    if not event_key:
        event = self.get_obs_event(event_key)
    else:
        event = self.get_surface_event(event_key, arrivals=True)

    (ra, dec) = event.ra_and_dec(apparent=apparent, subfield=direction,
                                 derivs=self.ALL_DERIVS)
    etc = (event_key, apparent, direction)
    self.register_backplane(('right_ascension',) + etc, ra)
    self.register_backplane(('declination',)     + etc, dec)

#===============================================================================
def celestial_north_angle(self, event_key=()):
    """Direction of celestial north at each pixel in the image.

    The angle is measured from the U-axis toward the V-axis. This varies across
    the field of view due to spherical distortion and also any distortion in the
    FOV.

    Input:
        event_key       key defining the surface event, typically () to refer
                        refer to the observation.
    """

    event_key = Backplane.standardize_event_key(event_key)
    key = ('celestial_north_angle', event_key)
    if key in self.backplanes:
        return self.get_backplane(key)

    temp_key = ('_dlos_ddec', event_key)
    if temp_key not in self.backplanes:
        self._fill_dlos_dradec(event_key)

    dlos_ddec = self.get_backplane(temp_key)
    duv_ddec = self.duv_dlos.chain(dlos_ddec)
    return self.register_backplane(key, duv_ddec.angle())

#===============================================================================
def celestial_east_angle(self, event_key=()):
    """Direction of celestial north at each pixel in the image.

    The angle is measured from the U-axis toward the V-axis. This varies
    across the field of view due to spherical distortion and also any
    distortion in the FOV.

    Input:
        event_key       key defining the surface event, typically () to
                        refer to the observation.
    """

    event_key = Backplane.standardize_event_key(event_key)
    key = ('celestial_east_angle', event_key)
    if key in self.backplanes:
        return self.get_backplane(key)

    temp_key = ('_dlos_dra', event_key)
    if temp_key not in self.backplanes:
        self._fill_dlos_dradec(event_key)

    dlos_dra = self.get_backplane(temp_key)
    duv_dra = self.duv_dlos.chain(dlos_dra)
    return self.register_backplane(key, duv_dra.angle())

#===============================================================================
def _fill_dlos_dradec(self, event_key):
    """Fill internal backplanes with derivatives with respect to RA and dec.
    """

    ra = self.right_ascension(event_key)
    dec = self.declination(event_key)

    # Derivatives of...
    #   los[0] = cos(dec) * cos(ra)
    #   los[1] = cos(dec) * sin(ra)
    #   los[2] = sin(dec)
    cos_dec = np.cos(dec.vals)
    sin_dec = np.sin(dec.vals)

    cos_ra = np.cos(ra.vals)
    sin_ra = np.sin(ra.vals)

    dlos_dradec_vals = np.zeros(ra.shape + (3,2))
    dlos_dradec_vals[...,0,0] = -sin_ra * cos_dec
    dlos_dradec_vals[...,1,0] =  cos_ra * cos_dec
    dlos_dradec_vals[...,0,1] = -sin_dec * cos_ra
    dlos_dradec_vals[...,1,1] = -sin_dec * sin_ra
    dlos_dradec_vals[...,2,1] =  cos_dec

    dlos_dradec_j2000 = Vector3(dlos_dradec_vals, ra.mask, drank=1)

    # Rotate dlos from the J2000 frame to the image coordinate frame
    frame = self.obs.frame.wrt(Frame.J2000)
    xform = frame.transform_at_time(self.obs_event.time)

    dlos_dradec = xform.rotate(dlos_dradec_j2000)

    # Convert to column vectors and save
    (dlos_dra, dlos_ddec) = dlos_dradec.extract_denoms()

    self.register_backplane(('_dlos_dra',  event_key), dlos_dra)
    self.register_backplane(('_dlos_ddec', event_key), dlos_ddec)

#===============================================================================
def center_right_ascension(self, event_key, apparent=True, direction='arr'):
    """Gridless right ascension of a photon from the body center to the
    detector.

    Input:
        event_key       key defining the event at the body's path.
        apparent        True to return the apparent direction of photons in the
                        the frame of the event; False to return the purely
                        geometric directions of the photons.
        direction       'arr' to return the direction of an arriving photon;
                        'dep' to return the direction of a departing photon.
    """

    gridless_key = Backplane.gridless_event_key(event_key)
    key = ('center_right_ascension', gridless_key, apparent, direction)
    if key not in self.backplanes:
        self._fill_center_ra_dec(gridless_key, apparent, direction)

    return self.get_backplane(key)

#===============================================================================
def center_declination(self, event_key, apparent=True, direction='arr'):
    """Gridless declination of a photon from the body center to the detector.

    Input:
        event_key       key defining the event at the body's path.
        apparent        True to return the apparent direction of photons in
                        the frame of the event; False to return the purely
                        geometric directions of the photons.
        direction       'arr' to return the direction of an arriving photon;
                        'dep' to return the direction of a departing photon.
    """

    gridless_key = Backplane.gridless_event_key(event_key)
    key = ('center_declination', gridless_key, apparent, direction)
    if key not in self.backplanes:
        self._fill_center_ra_dec(gridless_key, apparent, direction)

    return self.get_backplane(key)

#===============================================================================
def _fill_center_ra_dec(self, event_key, apparent, direction):
    """Internal method to fill in RA and dec for the center of a body."""

    if direction not in ('arr', 'dep'):
        raise ValueError('invalid photon direction: ' + direction)

    gridless_key = Backplane.gridless_event_key(event_key)
    event = self.get_obs_event(gridless_key)
    (ra, dec) = event.ra_and_dec(apparent=apparent, subfield=direction,
                                 derivs=self.ALL_DERIVS)
    etc = (gridless_key, apparent, direction)
    self.register_backplane(('center_right_ascension',) + etc, ra)
    self.register_backplane(('center_declination',)     + etc, dec)

################################################################################

# Add these functions to the Backplane module
Backplane._define_backplane_names(globals().copy())

################################################################################
