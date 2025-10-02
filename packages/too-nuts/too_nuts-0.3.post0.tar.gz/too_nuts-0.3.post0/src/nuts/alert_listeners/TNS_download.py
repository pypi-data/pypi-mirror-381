import datetime
import json
import os
import time
from dataclasses import asdict
from pathlib import Path

import requests

from ..config.config import ToOConfig

# TNS                  = "sandbox.wis-tns.org"
TNS = "www.wis-tns.org"
url_tns_search = "https://" + TNS + "/search"


# external http errors
ext_http_errors = [403, 500, 503]
err_msg = [
    "Forbidden",
    "Internal Server Error: Something is broken",
    "Service Unavailable",
]

# all possible parameters for building TNS search url
URL_PARAMETERS = [
    "discovered_period_value",
    "discovered_period_units",
    "unclassified_at",
    "classified_sne",
    "include_frb",
    "name",
    "name_like",
    "isTNS_AT",
    "public",
    "ra",
    "decl",
    "radius",
    "coords_unit",
    "reporting_groupid[]",
    "groupid[]",
    "classifier_groupid[]",
    "objtype[]",
    "at_type[]",
    "date_start[date]",
    "date_end[date]",
    "discovery_mag_min",
    "discovery_mag_max",
    "internal_name",
    "discoverer",
    "classifier",
    "spectra_count",
    "redshift_min",
    "redshift_max",
    "hostname",
    "ext_catid",
    "ra_range_min",
    "ra_range_max",
    "decl_range_min",
    "decl_range_max",
    "discovery_instrument[]",
    "classification_instrument[]",
    "associated_groups[]",
    "official_discovery",
    "official_classification",
    "at_rep_remarks",
    "class_rep_remarks",
    "frb_repeat",
    "frb_repeater_of_objid",
    "frb_measured_redshift",
    "frb_dm_range_min",
    "frb_dm_range_max",
    "frb_rm_range_min",
    "frb_rm_range_max",
    "frb_snr_range_min",
    "frb_snr_range_max",
    "frb_flux_range_min",
    "frb_flux_range_max",
    "format",
    "num_page",
]


def set_user_tns_marker(config: ToOConfig) -> str:
    uid = config.settings.tns.user_id
    user_name = config.settings.tns.user_name
    tns_marker = (
        'tns_marker{"tns_id": "'
        + str(uid)
        + '", "type": "user", "name": "'
        + user_name
        + '"}'
    )
    return tns_marker


def is_string_json(string):
    try:
        json_object = json.loads(string)
    except Exception:
        return False
    return json_object


def response_status(response):
    json_string = is_string_json(response.text)
    if json_string is not False:
        return (
            "[ "
            + str(json_string["id_code"])
            + " - '"
            + str(json_string["id_message"])
            + "' ]"
        )
    status_code = response.status_code
    if status_code == 200:
        status_msg = "OK"
    elif status_code in ext_http_errors:
        status_msg = err_msg[ext_http_errors.index(status_code)]
    else:
        status_msg = "Undocumented error"
    return f"[{str(status_code)} - '{status_msg}']"


def print_response(response, page_num):
    status = response_status(response)
    if response.status_code == 200:
        stats = (
            "Page number "
            + str(page_num)
            + " | return code: "
            + status
            + " | Total Rate-Limit: "
            + str(response.headers.get("x-rate-limit-limit"))
            + " | Remaining: "
            + str(response.headers.get("x-rate-limit-remaining"))
            + " | Reset: "
            + str(response.headers.get("x-rate-limit-reset") + " sec")
        )

    else:
        stats = "Page number " + str(page_num) + " | return code: " + status
    print(stats)


def get_reset_time(response):
    # If any of the '...-remaining' values is zero, return the reset time
    try:
        for name in response.headers:
            value = response.headers.get(name)
            if name.endswith("-remaining") and value == "0":
                return int(response.headers.get(name.replace("remaining", "reset")))
        return None
    except AttributeError:
        return None


def valid_parameter_list(keywords: list[str]) -> bool:
    unknown_parameters = list(set(keywords) - set(URL_PARAMETERS))

    if not unknown_parameters:
        return True
    print(f"Unknown url keyword {unknown_parameters}\n")
    return False


def build_TNS_url(keywords, values) -> str:
    url_par = ["&" + x + "=" + str(y) for x, y in zip(keywords, values)]
    return url_tns_search + "?" + "".join(url_par)


def make_filename_and_path(config: ToOConfig):
    current_datetime = datetime.datetime.now()
    current_date_time = current_datetime.strftime("%Y%m%d_%H%M%S")

    output_path = config.files.listener.tns_file

    tns_file = f"{output_path.stem}_{current_date_time}{output_path.suffix}"
    return config.files.listener.tns_dir / Path(tns_file)


def search_tns(config: ToOConfig) -> str:
    merge_files = config.settings.tns.merge_files
    url_parameters = config.settings.tns.model_dump()

    ignore_args = ["user_id", "user_name", "merge_files", "update_period"]
    url_parameters = {k: v for k, v in url_parameters.items() if k not in ignore_args}

    keywords = list(url_parameters.keys())
    values = list(url_parameters.values())

    if not valid_parameter_list(keywords):
        print("TNS search url is not in the correct format.\n")
        quit()

    tns_search_url = build_TNS_url(keywords, values)
    tns_output_file_path = make_filename_and_path(config)
    # Create TNS folder if it does not exist
    if not os.path.exists(config.files.listener.tns_dir):
        os.makedirs(config.files.listener.tns_dir)

    page_num = 0
    searched_data = []
    while page_num < 1000:
        url = tns_search_url + "&page=" + str(page_num)
        tns_marker = set_user_tns_marker(config)

        headers = {"User-Agent": tns_marker}

        response = requests.post(url, headers=headers, stream=True)
        data = (response.text).splitlines()

        if response.status_code != 200:
            print("status code is not 200")
            break

        if len(data) <= 1:
            break

        print(
            "Sending download search request for page num " + str(page_num + 1) + "..."
        )
        # print_response(response, page_num + 1)

        if page_num == 0:
            searched_data.append(data)
        else:
            searched_data.append(data[1:])
        reset = get_reset_time(response)
        if reset is not None:
            print("\nSleep for " + str(reset + 1) + " sec and then continue...\n")
            time.sleep(reset + 1)
        page_num = page_num + 1

    if searched_data != []:
        searched_data = [j for i in searched_data for j in i]
        if merge_files == 1:
            f = open(tns_output_file_path, "w")
            for el in searched_data:
                f.write(el + "\n")
            f.close()
            if len(searched_data) > 2:
                print(
                    "\nTNS searched data returned "
                    + str(len(searched_data) - 1)
                    + " rows. File '"
                    + str(tns_output_file_path)
                    + "' is successfully created.\n"
                )
            else:
                print(
                    "\nTNS searched data returned 1 row. File '"
                    + str(tns_output_file_path)
                    + "' is successfully created.\n"
                )
        else:
            if len(searched_data) > 2:
                print(
                    "TNS searched data returned "
                    + str(len(searched_data) - 1)
                    + " rows in total.\n"
                )
            else:
                print("TNS searched data returned 1 row in total.\n")
    else:
        if merge_files == 1:
            print("")
        print("TNS searched data returned empty list. No file(s) created.\n")

    return tns_output_file_path
