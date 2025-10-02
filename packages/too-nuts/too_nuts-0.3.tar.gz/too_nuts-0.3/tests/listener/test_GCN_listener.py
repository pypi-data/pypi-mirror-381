"""Tests for GCN alerts."""

import datetime as dt

from nuts.alert_listeners.GCN_alerts_template import GCNTemplates


def save_alert(alert_message: str, alert_store_directory: str) -> str:
    """Save the text of an alert to a file.

    Args:
        alert_message (str): input alert
        alert_store_directory (str): path to where the alert is stored

    Returns:
        str: full path + filename to the alert
    """
    now = dt.datetime.now().isoformat("T", "seconds")
    filename = f"gcn_alert_text_{now}.txt"
    alert_path = alert_store_directory + "/" + filename
    with open(alert_path, "w+") as f:
        f.write(alert_message)
    return alert_path


def load_alert(filename: str) -> list[str]:
    """Load an alert given a path to the alert.

    Args:
        filename (str): path + filename to the alert

    Returns:
        list[str]: alert message
    """
    with open(filename) as f:
        lines = f.readlines()
    return lines


# def test_alert(alert_dir, alert_name):
#     """Parse alert and save in database."""
#     # Database setup
#     database_dir = "./"
#     database_name = "ToO_TEST.db"
#     database_table = "GCN"
#     # Alert
#     alert_content = load_alert(alert_dir + alert_name)
#     gcn_parser = GCNTemplates()
#     too_event = gcn_parser(alert_content)

#     spb2_database = DataBaseIO(database_dir, database_name)
#     logging.info(spb2_database)
#     spb2_database(database_table, too_event.save_dict())
#     spb2_database.close()
#     logging.info(f"New alert saved as: {too_event.save_dict()}")


# def test_listener(config: dict) -> None:
#     """Test parser on various alert types.

#     Args:
#         config (dict): config file
#     """
#     # Get directories to save the raw alerts
#     alert_directory = "./GCN_alerts_testing/"

#     # FERMI GBM
#     alert_name = "gcn_alert_Fermi_FLT.txt"
#     test_alert(alert_directory, alert_name)
#     alert_name = "gcn_alert_Fermi_GDN.txt"
#     test_alert(alert_directory, alert_name)
#     alert_name = "gcn_alert_Fermi_FIN.txt"
#     test_alert(alert_directory, alert_name)

#     # MAXI
#     alert_name = "gcn_alert_MAXI_known.txt"
#     test_alert(alert_directory, alert_name)

#     # SWIFT
#     alert_name = "gcn_alert_Swift_XRT.txt"
#     test_alert(alert_directory, alert_name)
#     alert_name = "gcn_alert_Swift_FOM.txt"
#     test_alert(alert_directory, alert_name)

#     # AMON
#     alert_name = "gcn_alert_AMON.txt"
#     test_alert(alert_directory, alert_name)

#     # ICECUBE
#     alert_name = "gcn_alert_IceCube.txt"
#     test_alert(alert_directory, alert_name)

#     # FERMI TEST
#     alert_name = "gcn_alert_Fermi_LAT_TestPos.txt"
#     test_alert(alert_directory, alert_name)

#     # SWIFT TEST
#     alert_name = "gcn_alert_Swift_BAT_TestPos.txt"
#     test_alert(alert_directory, alert_name)

#     # LVC TEST
#     alert_name = "gcn_alert_LVC_Test.txt"
#     test_alert(alert_directory, alert_name)


# if __name__ == "__main__":
#     config_path = sys.argv[1]
#     config = config_parser.load_config(config_path)
#     test_listener(config)
