"""Library with functions to do the poorly localized optimization.


original author: Luke Kupari (luke-kupari@uiowa.edu)

.. autofunction:: extract_pix
.. autofunction:: object_interpolation
.. autofunction:: pointing_optimization
"""

import logging

import healpy as hp
import numpy as np
from astropy.coordinates import AltAz, SkyCoord
from astropy.time import Time, TimeDelta

from nuts.config.config import ToOConfig
from nuts.detector_motion import detector_init
from nuts.observation_period.observation import ObservationPeriod
from nuts.poorly_localized import GW_visualization as gviz
from nuts.poorly_localized.db_call import gracedb_call
from nuts.poorly_localized.pixel import source_pixel


def extract_pix(event_name: str, downsample: float, confidence_region: float):
    """Function to extract RA and DEC values for a given healpy map

    Args:
        event_name (str): Name of event for example (S190521r)
        downsample (float): Downsample factor for healpy map always should always be 2^n, lower means faster performance
        confidence_region (float): region of the GW event you want to constrain

    Returns:
        [np.array()]: list of extracted values in arrays
    """

    fits = gracedb_call(event_name)
    probs, header = hp.read_map(fits, h=True)
    dprobs = hp.ud_grade(probs, downsample, power=-2)
    ns = hp.npix2nside(len(dprobs))

    # generating sorted array used for confidence region
    sorting = np.flipud(np.argsort(dprobs))
    credible_sorted = np.cumsum(dprobs[sorting])
    region = np.empty_like(credible_sorted)
    region[sorting] = credible_sorted

    pix_region = list()
    for i in range(len(region)):
        if region[i] <= confidence_region / 100:
            pix_region.append(i)

    theta, phi = hp.pix2ang(ns, pix_region)
    ra_values = np.rad2deg(phi)
    dec_values = np.rad2deg(0.5 * np.pi - theta)

    pixel_list = []
    for prob, ra, dec, pix in zip(
        dprobs[pix_region], ra_values, dec_values, pix_region
    ):
        # Construct a source_pixel object for each pixel in the credible region
        sp = source_pixel(probability=prob, ra=ra, dec=dec, pixel=pix)
        pixel_list.append(sp)

    return (
        np.array(ra_values),
        np.array(dec_values),
        np.array(pix_region),
        np.array(dprobs[pix_region]),
        pixel_list,
    )


def object_interpolation(
    observable: ObservationPeriod, detector: detector_init, point: source_pixel, dt
):
    """Does interpolation between initial and final values taken from get_observation_times

    Args:
        observable (ObservationPeriod): Observation periods from get_observation times
        detector (DetectorLocation): Detector object
        point (source_pixel): values taken directly from the healpy map
        dt (Float): Time increment

    Returns:
        [astropy.SkyCoord] : Interpolated traces for GW event crossing FOV
    """
    # list to store all "point sourcesgermany elec"
    altaz_object = []
    for i in range(len(observable)):
        # Need to check if the start and end time are the same
        if observable[i].start_time == observable[i].end_time:
            time_step = np.array([observable[i].start_time])
        else:
            n_steps = int(
                (
                    (observable[i].end_time - observable[i].start_time) / TimeDelta(dt)
                ).value
            )
            time_step = observable[i].start_time + TimeDelta(np.arange(n_steps) * dt)

        frame_time = AltAz(obstime=time_step, location=detector.loc(Time(time_step)))

        object = SkyCoord(frame="icrs", unit="deg", ra=point.ra, dec=point.dec)

        altaz_object.append(object.transform_to(frame_time))

    return altaz_object


def pointing_optimization(
    event_name: str,
    period: list[ObservationPeriod],
    altaz: list[SkyCoord],
    points: source_pixel,
    plot: bool,
    config: ToOConfig,
):

    """This will generate a pointing time as well as azimuth for all observable points within observation period

    Args:
        event_name (str): name of event for example (S190521r)
        period (list[ObservationPeriod]): list of observation periods taken from get_observation_period
        altaz (list[SkyCoord]): list of interpolated SkyCoord objects from object_interpolation()
        points (source_pixel): Values taken directly from the healpy map
        plot (bool): Boolean to either plot or not
        config (ToOConfig): Config for ToO

    Returns:
        tuple : Optimal azimuth, start time, end time
    """

    filtered_altaz = []
    filtered_points = []
    filter_indices = []
    filter_periods = []
    az_values = []

    for i in range(len(altaz)):
        # The idea here is to filter all points from observable vs non-observable
        if len(altaz[i]) != 0:
            # if observable then we care about it
            # could probably combine all of these into one object
            filter_value = i
            filtered_altaz.append(altaz[i])
            filter_periods.append(period[i])
            az_values.append(altaz[i][0].az.deg)
            filtered_points.append(points[i])
            filter_indices.append(filter_value)
        else:
            continue

    # defining azimuth bounds based off of min and max azimuth object appears in fov
    az_fov = config.settings.observation.fov_az.value
    az_flat = np.concatenate(az_values).ravel()
    min_az = round(min(az_flat), ndigits=0)
    max_az = round(max(az_flat), ndigits=0)
    fov_r = np.arange(max_az - az_fov / 2, min_az + az_fov / 2, -0.1)
    fov_l = fov_r - az_fov

    pointing_time = []
    pointing_fov = []
    for i in range(len(fov_l)):
        # loop over fov range
        weighted_time = 0
        for j in range(len(filtered_altaz)):
            # loop over all traces
            altaz_tmp = filtered_altaz[j]
            point_tmp = filtered_points[j]
            points_l = np.where(np.array(altaz_tmp[0].az.deg) > fov_l[i])
            points_r = np.where(np.array(altaz_tmp[0].az.deg) < fov_r[i])
            Npoints = len(np.intersect1d(points_l, points_r))
            if Npoints > 0:
                weighted_time += (
                    Npoints * point_tmp.probability * (1 / (60 * 24))
                )  # dependent on time scale 1min

        pointing_time.append(weighted_time)
        pointing_fov.append(fov_r[i] - az_fov / 2)

    tmax_index = np.argmax(pointing_time)
    optimal_fov = pointing_fov[tmax_index]
    fov_range = [optimal_fov - az_fov, optimal_fov + az_fov]
    pointing_time_user = []
    pointing_az = []

    # Check if the trace is within the FOV
    # If it has any points within the FOV, we count it
    # Now we determine the time when the trace is within the FOV
    for i in range(len(filtered_altaz)):
        altaz_tmp = filtered_altaz[i]
        points_l = np.where(np.array(altaz_tmp[0].az.deg) > fov_range[0])
        points_r = np.where(np.array(altaz_tmp[0].az.deg) < fov_range[1])
        Npoints = len(np.intersect1d(points_l, points_r))
        # Now want to see if Npoints > 0 what time the trace is in fov
        if Npoints > 0:
            temp = filter_periods[i]
            pointing_time_user.append(temp[0].start_time)
            pointing_az.append(filtered_altaz[i])
        else:
            continue

    # calculate start and end time of observation with x minute window
    datetime_objects = np.array([time.unix for time in pointing_time_user])
    median_timestamp = np.median(datetime_objects)
    median_datetime = Time(median_timestamp, format="unix", scale="utc")
    time_delta = TimeDelta(config.settings.gwaves.obs_timewindow, format="sec")
    start_time = median_datetime - time_delta
    end_time = median_datetime + time_delta

    logging.info("***************************************************")
    logging.info("GW module results")
    logging.info("Start Time of Observation: %s", start_time.isot)
    logging.info("End Time of Observation: %s", end_time.isot)
    logging.info("Optimal pointing is at: %s", optimal_fov)
    logging.info("Points in FOV start at: %s", min(pointing_time_user))
    logging.info("Points in FOV end at: %s", max(pointing_time_user))
    logging.info("***************************************************")

    if plot:
        gviz.plot_traces_unoptimized(event_name, filtered_altaz, config)
        gviz.plot_traces_optimized(event_name, pointing_az, optimal_fov, az_fov, config)
        gviz.plot_azimuth(event_name, pointing_fov, pointing_time, config)

    return max(pointing_fov), start_time.isot, end_time.isot
