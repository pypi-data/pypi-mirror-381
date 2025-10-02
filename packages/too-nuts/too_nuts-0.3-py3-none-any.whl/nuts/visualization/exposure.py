"""
Functions for changing coordinate systems.

Created on Fri Feb 17 12:53:28 2023

@author: claireguepin
"""

import astropy.constants as const
import astropy.coordinates as acoord
import astropy.units as u
import numpy as np
from astropy.coordinates import get_body
from scipy import interpolate

from nuts.observation_period.sun_moon_cuts import moon_illumination
from nuts.visualization.functions import EquatorialToGalactic

# =============================================================================
# Grid for Earth's rotation
grid_orbit = 400.0  # 200


def func(th, ph):
    """Spherical th,ph to cartesian x,y,z coordinates.

    Args:
        th: theta angle (spherical)
        ph: phi angle (spherical)

    Returns:
        numpy array of x,y,z coordinates
    """
    return np.array(
        [np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), np.cos(th) * np.sin(ph) ** 0]
    )


def eff_fov(OM_calc, nsat, axloc, theta_em, h, n1, n2):
    """Geometrical conditions to estimate the fov.

    Args:
        OM_calc: array of sky locations
        nsat: vector defining the detector's location
        axloc: axis used in scalar product
        theta_inc_loc: angle depending on the maximum emergence angle
        n1, n2: shape of OM_calc to account for solid angle

    Returns:
        solid angle, if observable, i.e. in the field of view
    """
    R_E = const.R_earth
    y = np.sum(OM_calc * (-nsat), axis=axloc)
    #    theta_inc_loc = np.pi/2. - theta_em
    #    bool2 = np.arccos(y) > np.arcsin(R_E / (R_E + h) * np.sin(theta_inc_loc))
    bool2 = np.arccos(y) > np.arcsin((R_E / (R_E + h)).value) - theta_em
    bool3 = np.arccos(y) < np.arcsin((R_E / (R_E + h)).value)
    return (bool2 * bool3).astype(int) * 2.0 / n1 * 2.0 * np.pi / n2


def exp_gal(alpha_tab, delta_tab, exp_equ):
    """Transform acceptance in Galactic coordinates.

    Args:
        alpha_tab, delta_tab: arrays of coordinates
        exp_equ: exposure in equatorial coordinates

    Returns:
        acceptance in Galactic coordinates
    """
    long_tab, lat_tab = EquatorialToGalactic(
        np.ndarray.flatten(delta_tab), np.ndarray.flatten(alpha_tab)
    )
    points_ini = np.array([lat_tab, long_tab]).T
    Aeff_galactic = interpolate.griddata(
        points_ini,
        np.ndarray.flatten(exp_equ),
        (delta_tab, alpha_tab),
        method="nearest",
    )
    Aeff_gal = np.nan_to_num(Aeff_galactic)
    # Aeff_gal = gaussian_filter(Aeff_gal, 2)
    long_tab = np.concatenate(
        (
            alpha_tab[:, int(len(alpha_tab[0, :]) / 2) :] - 2 * np.pi,
            alpha_tab[:, : int(len(alpha_tab[0, :]) / 2)],
        ),
        axis=1,
    )
    Aeff_gal = np.concatenate(
        (
            Aeff_gal[:, int(len(Aeff_gal[0, :]) / 2) :],
            Aeff_gal[:, : int(len(Aeff_gal[0, :]) / 2)],
        ),
        axis=1,
    )
    Aeff_gal = Aeff_gal[:, ::-1]
    return Aeff_gal


def compute_geo_exp_day(config, alpha_tab, delta_tab, time_start):
    """Geometrical acceptance for one day.

    Args:
        alpha_tab (array): right ascension
        delta_tab (array): declination
        config (dict): config file
        time_start: beginning of observation window

    Returns:
        acceptance
    """
    num1, num2 = np.shape(alpha_tab)
    OM_tab1 = func(np.pi / 2.0 - delta_tab, alpha_tab)
    Acceptance_fov = np.zeros(shape=(int(num1), int(num2)))
    Acceptance_sun = np.zeros(shape=(int(num1), int(num2)))
    Acceptance = np.zeros(shape=(int(num1), int(num2)))

    # Loop over observation window times (with time buffer)
    times = config._runtime.all_times
    timemed = (
        config._runtime.observation_starts
        + (config._runtime.observation_ends - config._runtime.observation_starts) / 2.0
    )
    time = timemed - 12 * u.hour
    timeend = timemed + 12 * u.hour
    deltatime = 5.0 * u.min
    while time < timeend:
        detector = config._runtime.detector
        locations = detector.loc(times)
        ittime = np.argmin(np.abs(times - time))
        lon = locations.lon.to(u.deg)[ittime]
        lat = locations.lat.to(u.deg)[ittime]
        height = locations.height[ittime]

        if config.settings.observation.horizontal_offset_angle == "limb":
            alpha = np.arcsin(const.R_earth / (height + const.R_earth)).value
        else:
            alpha = np.pi / 2.0 - (
                u.Quantity(config.settings.observation.horizontal_offset_angle)
                .to("rad")
                .value
            )

        detector_location = acoord.EarthLocation.from_geodetic(
            lon=lon, lat=lat, height=height
        )
        detector_gcrs = detector_location.get_gcrs(time)
        Phis = detector_gcrs.ra.rad
        Thetas = np.pi / 2.0 - detector_gcrs.dec.rad
        nsat = np.array(
            [
                np.sin(Thetas) * np.cos(Phis),
                np.sin(Thetas) * np.sin(Phis),
                np.cos(Thetas),
            ]
        )

        # position of the sun
        theta_sun = np.pi / 2.0 - get_body("sun", time).dec.rad
        phi_sun = get_body("sun", time).ra.rad
        usun = np.array(
            [
                np.sin(theta_sun) * np.cos(phi_sun),
                np.sin(theta_sun) * np.sin(phi_sun),
                np.cos(theta_sun),
            ]
        )

        # position of the moon
        theta_mo = np.pi / 2.0 - get_body("moon", time).dec.rad
        phi_mo = get_body("moon", time).ra.rad
        umo = np.array(
            [
                np.sin(theta_mo) * np.cos(phi_mo),
                np.sin(theta_mo) * np.sin(phi_mo),
                np.cos(theta_mo),
            ]
        )
        D_TM = get_body("moon", time).distance.m

        # illumination of the moon
        moon_il = moon_illumination(time)
        moon_il_max = config.settings.observation.moon_illumination_cut
        prod_sun = np.dot(-nsat, usun)
        bool_sun = (prod_sun > 0) * (
            np.arccos(prod_sun)
            < alpha + config.settings.observation.sun_altitude_cut.to(u.rad).value
        )

        vSMo = -(height + const.R_earth).value * nsat + D_TM * umo
        SMo = np.dot(vSMo, vSMo) ** 0.5
        prod_mo = np.dot(-nsat, vSMo / SMo)

        bool_moon = (
            np.arccos(prod_mo)
            < alpha + config.settings.observation.moon_altitude_cut.to(u.rad).value
        ) + (moon_il < moon_il_max)

        nsat_tab = np.reshape(
            np.repeat(nsat, int(num1) * int(num2)), (3, int(num1), int(num2))
        )

        theta_em = config.settings.observation.fov_alt.to(u.rad).value
        Exp_temp = eff_fov(OM_tab1, nsat_tab, 0, theta_em, height, num1, num2)
        Acceptance_fov += Exp_temp * deltatime.value
        Acceptance_sun += Exp_temp * deltatime.value * bool_sun
        Acceptance += Exp_temp * deltatime.value * bool_sun * bool_moon
        # Increment time
        time += deltatime

    return Acceptance, Acceptance_fov, Acceptance_sun
