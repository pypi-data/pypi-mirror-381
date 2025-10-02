"""Obtain pointing information for GW Events.

Will be run automatically for any LVC events in the cleaned database.

original author: Luke Kupari (luke-kupari@uiowa.edu)

.. autofunction:: gw_localization_pointing

"""

import warnings

import astropy.units as u
from astropy.coordinates import AltAz
from astropy.time import Time, TimeDeltaMissingUnitWarning

import nuts.poorly_localized.ext_lib as extendedlib
from nuts.config.config import ToOConfig
from nuts.detector_motion.detector_init import detector_init
from nuts.IO_funcs.too_database import DataBaseIO
from nuts.observation_period.observation import ObservationPeriod
from nuts.observation_period.source_observability import get_observation_times
from nuts.too_event import ToOEvent
from nuts.too_observation import ToOObservation

warnings.filterwarnings("ignore", category=TimeDeltaMissingUnitWarning)


def gw_localization_pointing(config: ToOConfig):
    """Function that runs the GW localization module

    Args:
        config (ToOConfig): config file

    Returns:
        [ToOObservation]: List of ToOObservation objects
    """

    dt = config.settings.gwaves.time_increment
    plot_traj = config.settings.gwaves.visualize

    database = DataBaseIO(config.files.database.cleaned)
    database.read()
    events = database.get_events()
    detector = detector_init(config)
    coords_interp = []
    period_list = []

    for ev in events:

        # ignore non LVC events in the database
        if "lvc" not in ev.event_type.lower():
            continue

        event_list = []
        period_list = []
        coords_interp = []
        # extract event_name from database
        name_event = ev.publisher_id.split()[0]
        (
            ra_values,
            dec_values,
            pix_that_matter,
            prob,
            pix_list,
        ) = extendedlib.extract_pix(
            name_event,
            config.settings.gwaves.downsample,
            config.settings.gwaves.confidence,
        )

        for i in range(len(ra_values)):
            # create list of ToOEvents for each pixel in the localization
            temp_event = ToOEvent()
            temp_event.set_coordinates(ra_values[i], dec_values[i], units="deg")
            event_list.append(temp_event)

            # throw each pixel in get_observation_times() to get observability conditions
            periods = get_observation_times(config, event_list[i])
            period_list.append(periods[0])

            # interpolate between the (start,final) alt/az of each pixel
            coords_interp.append(
                extendedlib.object_interpolation(
                    period_list[i], detector, pix_list[i], dt
                )
            )

        tmp_obs = extendedlib.pointing_optimization(
            name_event,
            period_list,
            altaz=coords_interp,
            points=pix_list,
            plot=plot_traj,
            config=config,
        )

        obs_period = ObservationPeriod()
        obs_period.start_time = Time(tmp_obs[1])
        obs_period.end_time = Time(tmp_obs[2])
        obs_period.start_loc = AltAz(az=0.0 * u.deg, alt=0.0 * u.deg)
        obs_period.end_loc = AltAz(az=0.0 * u.deg, alt=0.0 * u.deg)
        obs_period.pointing_dir = AltAz(az=tmp_obs[0] * u.deg, alt=-9.2 * u.deg)

        ret_obs = []
        observation = ToOObservation()
        observation.event = ev
        observation.detector = detector
        observation.observations = [obs_period]
        ret_obs.append(observation)

    return ret_obs
