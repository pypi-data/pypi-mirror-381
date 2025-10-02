"""ATELS reader. To be developed.

.. autosummary::

   float_conv
   input_coordinates
   manual_input

"""

import logging

from nuts import too_event


def float_conv(input_str: str) -> float:
    """Function to check if provided input is a float

    Args:
        input_str (str): input

    Returns:
        float: once a float is input return that value
    """
    try:
        return float(input_str)
    except ValueError:
        error_message = f"Your input: {input_str} can not be converted to a float. Please try again!"
        logging.warning(error_message)
        print(error_message)
        float_conv(input())


def input_coordinates() -> tuple[float, float, str]:
    """Function to query for input coordinates

    Returns:
        tuple[float, float, str]: (RA, DEC, reference frame)
    """
    ra = float_conv(input("Please enter the event RA (deg):"))
    dec = float_conv(input("Please enter the event DEC (deg):"))
    allowed_frames = [
        "altaz",
        "barycentricmeanecliptic",
        "barycentrictrueecliptic",
        "cirs",
        "custombarycentricecliptic",
        "fk4",
        "fk4noeterms",
        "fk5",
        "galactic",
        "galacticlsr",
        "galactocentric",
        "gcrs",
        "geocentricmeanecliptic",
        "geocentrictrueecliptic",
        "hadec",
        "hcrs",
        "heliocentriceclipticiau76",
        "heliocentricmeanecliptic",
        "heliocentrictrueecliptic",
        "icrs",
        "itrs",
        "lsr",
        "lsrd",
        "lsrk",
        "precessedgeocentric",
        "supergalactic",
        "teme",
        "tete",
    ]
    frame = input("Please enter the coordinate frame type (icrs, fk5, ...): ")
    if frame not in allowed_frames:
        error_message = (
            f"Error: Unknown frame: {frame}! Use one of these: {allowed_frames}"
        )
        logging.warning(error_message)
        print(error_message)
        ra, dec, frame = input_coordinates()
    return ra, dec, frame


def manual_input() -> too_event.ToOEvent:
    """
    Function to manually input an alert into a database that queries for all needed information

    Returns:
        too_event.ToOEvent: Event that was input
    """
    print("Enter an alert: ")
    event = too_event.ToOEvent()
    event.event_type = input("Please enter the event type:")
    event.event_id = input("Please enter the event ID:")
    event.publisher = input("Please enter the publisher:")
    event.publisher_id = input("Please enter the publisher ID:")

    ra, dec, frame = input_coordinates()
    event.set_coordinates(ra, dec, frame=frame)

    time = input(
        "Please input the time in isot format (default: 2023-05-01T00:00:00): "
    )
    if time == "":
        time = "2023-05-01T00:00:00"
    event.set_time(time)
    print(f"Detection time: {event.detection_time}")

    parameter = input("Please enter the name of the parameter: ")
    while parameter != "x":
        parameter = parameter.lower()
        param_value = input(f"Enter the value of the {parameter}: ")
        event.params[parameter] = param_value
        parameter = input(
            "Please enter the name of the next parameter or 'x' to quit: "
        )

    print(event)
    edit = input("Do you want to edit your input? (y/n)")
    if edit == "y":
        logging.info(f"New event added: {event.save_dict()}")
        return event
    manual_input()
