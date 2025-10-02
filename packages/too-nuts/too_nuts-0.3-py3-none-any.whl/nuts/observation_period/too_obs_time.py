"""Compute observation window using input date.

.. autosummary::
   :toctree:
   :recursive:

.. autofunction:: get_window, get_next_window

"""

import logging

import astropy.units as u
import numpy as np
from astropy.time import Time


def get_observation_windows(
    observation_possible: np.ndarray[bool], times: Time, one_window=False
) -> tuple[Time, Time]:
    """Determine start and end of an observation window.

    Args:
        observation_possible (np.ndarray[bool]): Array of booleans indicating if source is observable

    Returns:
        tuple[Time, Time]: Start and end of observation window
    """

    # Calculate times when source would be visible
    observation_possible = np.append(np.array([0]), observation_possible)
    observation_possible = np.append(observation_possible, np.array([0, 0]))

    # Extract times when source moves in and out of detectable region
    start = np.flatnonzero(np.diff(observation_possible) == 1)
    end = np.flatnonzero(np.diff(observation_possible) == -1)

    if len(start) == 0:
        logging.error("No observation can be scheduled.")

    for e in range(len(end)):
        end[e] = np.min((len(times) - 2, end[e]))
        start[e] = np.min((len(times) - 2, start[e]))

    if one_window:
        start, end = get_next_window(observation_possible, times, start, end)

    return start, end, times[start], times[end]


def get_next_window(
    observation_possible: np.ndarray[bool],
    times: Time,
    start: np.ndarray[int],
    end: np.ndarray[int],
) -> tuple[np.ndarray[int], np.ndarray[int]]:
    """Determine start and end of next observation window.

    Args:
        observation_possible (np.ndarray[bool]): Array of booleans
        times: array of Times
        start: array of time indexes for obs window start
        end: array of time indexes for obs window end

    Returns:
        tuple[int, int]: Start and end indexes of observation window
    """

    # Make sure start and end times are correctly chosen
    # Ex. if first observation window is truncated, use second
    if observation_possible[1] == 1:
        if times[start[1]] > times[0] + 24.0 * u.h:
            start_time_observable = start[0]
            end_time_observable = end[0]
        else:
            start_time_observable = start[1]
            end_time_observable = end[1]
    else:
        start_time_observable = start[0]
        if end[0] > start[0]:
            end_time_observable = end[0]
        else:
            end_time_observable = end[1]

    start = start_time_observable
    end = end_time_observable
    return start, end
