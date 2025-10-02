"""Templates for GCN alerts."""

import logging
from typing import Callable

from nuts import too_event
from nuts.alert_listeners import GCN_parser_methods


class GCNTemplates:
    def __init__(self) -> None:
        """Initialization of the Templates with a list of
        all the templates that are currently implemented
        """
        self.parser = GCN_parser_methods.GCNParserMethods()
        self.publishers = {
            "LVC Preliminary": self.LVC_Preliminary_template(),
            "LVC Initial Skymap": self.LVC_init_skymap(),
            "LVC Update Skymap": self.LVC_init_skymap(),
            "LVC Retraction": self.LVC_retraction(),
            "TEST LVC Preliminary": self.LVC_Preliminary_template(),
            "TEST LVC Initial Skymap": self.LVC_init_skymap(),
            "TEST LVC Update Skymap": self.LVC_init_skymap(),
            "MAXI Position": self.MAXI_Position(),
            "MAXI Test Position": self.MAXI_Position(),
            "MAXI Known Source Position": self.MAXI_known(),
            "MAXI Unknown Source Position": self.MAXI_unknown(),
            "SuperAGILE GRB Position": self.SuperAGILE_GRB_Position(),
            "SuperAGILE GRB Ground Position": self.SuperAGILE_GRB_Position(),
            "SuperAGILE GRB Test Position": self.SuperAGILE_GRB_Position(),
            "ICECUBE Astrotrack Bronze": self.icecube(),
            "ICECUBE Astrotrack Gold": self.icecube(),
            "HAWC Burst Monitor": self.HAWC(),
            "Fermi-LAT Position": self.Fermi_LAT_Position(),
            "Fermi-LAT Test Position": self.Fermi_LAT_Position(),
            "Fermi-GBM Position": self.Fermi_GBM_Position(),
            "Fermi-GBM Flight Position": self.Fermi_GBM_Flight_Position(),
            "Fermi-GBM Ground Position": self.Fermi_GBM_Position(),
            "Fermi-GBM Final Position": self.Fermi_GBM_Position(),
            "Fermi-GBM Test Position": self.Fermi_GBM_Position(),
            "TEST INTEGRAL Refined": self.Integral_notice(),
            "TEST INTEGRAL Offline": self.Integral_notice(),
            "TEST INTEGRAL Wakeup": self.Integral_notice(),
            "INTEGRAL Refined": self.Integral_notice(),
            "INTEGRAL Offline": self.Integral_notice(),
            "INTEGRAL Wakeup": self.Integral_notice(),
            "Swift-BAT GRB Position": self.SWIFT_BAT(),
            "Swift-BAT GRB Test Position": self.SWIFT_BAT(),
            "Swift-FOM Will_Observe": self.SWIFT_FOM(),
            "Swift-XRT Position": self.SWIFT_XRT(),
            "Swift-XRT Position UPDATE": self.SWIFT_XRT_update(),
            "Swift-UVOT Position": self.SWIFT_UVOT(),
            "AMON Neutrino-EM Coincidence": self.nu_em_coincidence(),
        }

    def get_template(self, alert: list[str]) -> str:
        """Select the template based on the publisher name

        Args:
            alert (list[str]): input alert

        Returns:
            str: selectes template corresponds to publisher name
        """
        return self.parser.get_publisher(alert[2])

    def __call__(self, alert: list[str]) -> too_event.ToOEvent:
        """Function that selects the template function and applies it to the
        given alert to return a parsed event

        Args:
            alert (list[str]): input alert

        Returns:
            too_event.ToOEvent: output ToOEvent
        """
        template_name = self.get_template(alert)
        logging.info(f"Parsing alert using the template: {template_name}")
        template = self.publishers[template_name]
        return self.parse_alert(alert, template)

    def parse_alert(self, alert: list[str], template: Callable) -> too_event.ToOEvent:
        """Function to iterate through all lines in the alert and run the corresponding function
        to populate an event

        Args:
            alert (list[str]): input alert
            template (Callable): alert template

        Returns:
            too_event.ToOEvent: output ToOEvent
        """
        for line in alert:
            self.apply_function(line, template)
        self.parser.combine_date_coords()
        return self.parser.event

    def apply_function(self, line: str, template: dict) -> None:
        """Function to check if the line can be parsed and if so apply the
        corresponding function

        Args:
            line (str): input_lint
            template (dict): template
        """
        if line.startswith("   "):
            return
        if line == "\n" or line == " \n":
            return
        key = line.split(":")[0]
        if key is not None:
            method = template[key]
        if method is not None:
            method(line)

    def LVC_Preliminary_template(self):
        return {
            "TITLE": None,
            "NOTICE_DATE": None,
            "NOTICE_TYPE": self.parser.get_publisher,
            "TRIGGER_NUM": self.parser.get_trigger_num,
            "TRIGGER_DATE": self.parser.get_trigger_date,
            "TRIGGER_TIME": self.parser.get_trigger_time,
            "SEQUENCE_NUM": None,
            "GROUP_TYPE": None,
            "SEARCH_TYPE": None,
            "PIPELINE_TYPE": None,
            "FAR": self.parser.get_far,
            "PROB_NS": self.parser.get_porb_ns,
            "PROB_REMNANT": self.parser.get_porb_remnant,
            "PROB_BNS": self.parser.get_porb_bns,
            "PROB_NSBH": self.parser.get_porb_nsbh,
            "PROB_BBH": self.parser.get_porb_bbh,
            "PROB_MassGap": self.parser.get_porb_massgap,
            "PROB_TERRES": self.parser.get_porb_terres,
            "TRIGGER_ID": None,
            "MISC": None,
            "SKYMAP_FITS_URL": self.parser.get_skymap,
            "EVENTPAGE_URL": self.parser.get_eventpage,
            "COMMENTS": None,
        }

    def MAXI_Position(self):
        return {
            "TITLE": None,
            "NOTICE_DATE": None,
            "NOTICE_TYPE": self.parser.get_publisher,
            "EVENT_ID_NUM": self.parser.get_trigger_num,
            "EVENT_RA": self.parser.get_ra,
            "EVENT_DEC": self.parser.get_dec,
            "EVENT_ERROR": self.parser.get_error,
            "EVENT_FLUX": self.parser.get_flux,
            "EVENT_DATE": self.parser.get_trigger_date,
            "EVENT_TIME": self.parser.get_trigger_time,
            "EVENT_TSCALE": self.parser.get_tscale,
            "EVENT_EBAND": self.parser.get_eband,
            "SUN_POSTN": None,
            "SUN_DIST": self.parser.get_sun_dist,
            "MOON_POSTN": None,
            "MOON_DIST": self.parser.get_moon_dist,
            "MOON_ILLUM": self.parser.get_moon_illum,
            "GAL_COORDS": None,
            "ECL_COORDS": None,
            "COMMENTS": None,
        }

    def MAXI_known(self):
        return {
            "TITLE": None,
            "NOTICE_DATE": None,
            "NOTICE_TYPE": self.parser.get_publisher,
            "SRC_ID_NUM": self.parser.get_trigger_num,
            "SRC_RA": self.parser.get_ra,
            "SRC_DEC": self.parser.get_dec,
            "SRC_ERROR": None,
            "SRC_FLUX": None,
            "SRC_DATE": self.parser.get_trigger_date,
            "SRC_TIME": self.parser.get_trigger_time,
            "SRC_TSCALE": None,
            "SRC_EBAND": None,
            "SRC_CLASS": self.parser.set_eventtype_maxi,
            "SRC_NAME": self.parser.set_eventid,
            "BAND_FLUX": None,
            "ISS_LON_LAT": None,
            "SUN_POSTN": None,
            "SUN_DIST": self.parser.get_sun_dist,
            "MOON_POSTN": None,
            "MOON_DIST": self.parser.get_moon_dist,
            "MOON_ILLUM": self.parser.get_moon_illum,
            "GAL_COORDS": None,
            "ECL_COORDS": None,
            "COMMENTS": None,
        }

    def MAXI_unknown(self):
        return {
            "TITLE": None,
            "NOTICE_DATE": None,
            "NOTICE_TYPE": self.parser.get_publisher,
            "EVENT_ID_NUM": self.parser.get_trigger_num,
            "EVENT_RA": self.parser.get_ra,
            "EVENT_DEC": self.parser.get_dec,
            "EVENT_ERROR": None,
            "EVENT_FLUX": None,
            "EVENT_DATE": self.parser.get_trigger_date,
            "EVENT_TIME": self.parser.get_trigger_time,
            "EVENT_TSCALE": None,
            "EVENT_EBAND": None,
            "SUN_POSTN": None,
            "SUN_DIST": self.parser.get_sun_dist,
            "MOON_POSTN": None,
            "MOON_DIST": self.parser.get_moon_dist,
            "MOON_ILLUM": self.parser.get_moon_illum,
            "GAL_COORDS": None,
            "ECL_COORDS": None,
            "COMMENTS": None,
        }

    def SuperAGILE_GRB_Position(self):
        return {
            "TITLE": self.parser.set_type_grb,
            "NOTICE_DATE": None,
            "NOTICE_TYPE": self.parser.get_publisher,
            "TRIGGER_NUM": self.parser.get_trigger_num,
            "GRB_RA": self.parser.get_ra,
            "GRB_DEC": self.parser.get_dec,
            "GRB_ERROR": self.parser.get_error,
            "GRB_INTEN": self.parser.get_intensity_agile,
            "GRB_SIGNIF": self.parser.get_significance_agile,
            "GRB_DATE": self.parser.get_trigger_date,
            "GRB_TIME": self.parser.get_trigger_time,
            "SUN_POSTN": None,
            "SUN_DIST": self.parser.get_sun_dist,
            "MOON_POSTN": None,
            "MOON_DIST": self.parser.get_moon_dist,
            "MOON_ILLUM": self.parser.get_moon_illum,
            "GAL_COORDS": None,
            "ECL_COORDS": None,
            "COMMENTS": None,
        }

    def icecube(self):
        return {
            "TITLE": None,
            "NOTICE_DATE": None,
            "NOTICE_TYPE": self.parser.get_publisher,
            "STREAM": None,
            "RUN_NUM": None,
            "EVENT_NUM": self.parser.get_trigger_num,
            "SRC_RA": self.parser.get_ra,
            "SRC_DEC": self.parser.get_dec,
            "SRC_ERROR": self.parser.get_error,
            "SRC_ERROR50": None,
            "DISCOVERY_DATE": self.parser.get_trigger_date,
            "DISCOVERY_TIME": self.parser.get_trigger_time,
            "REVISION": self.parser.get_revision,
            "ENERGY": self.parser.get_energy,
            "SIGNALNESS": self.parser.get_signalness,
            "FAR": self.parser.get_far,
            "SUN_POSTN": None,
            "SUN_DIST": self.parser.get_sun_dist,
            "MOON_POSTN": None,
            "MOON_DIST": self.parser.get_moon_dist,
            "GAL_COORDS": None,
            "ECL_COORDS": None,
            "COMMENTS": None,
        }

    def HAWC(self):
        return {
            "TITLE": None,
            "NOTICE_DATE": None,
            "NOTICE_TYPE": self.parser.get_publisher,
            "STREAM": None,
            "RUN_NUM": None,
            "EVENT_NUM": self.parser.get_trigger_num,
            "SRC_RA": self.parser.get_ra,
            "SRC_DEC": self.parser.get_dec,
            "SRC_ERROR": self.parser.get_error,
            "DISCOVERY_DATE": self.parser.get_trigger_date,
            "DISCOVERY_TIME": self.parser.get_trigger_time,
            "REVISION": self.parser.get_revision,
            "FAR": self.parser.get_far,
            "Pvalue": self.parser.get_pvalue,
            "delta_T": self.parser.get_delta_t,
            "SKYMAP_FITS_URL": self.parser.get_skymap,
            "SUN_POSTN": None,
            "SUN_DIST": self.parser.get_sun_dist,
            "MOON_POSTN": None,
            "MOON_DIST": self.parser.get_moon_dist,
            "GAL_COORDS": None,
            "ECL_COORDS": None,
            "COMMENTS": None,
        }

    def LVC_init_skymap(self):
        return {
            "TITLE": None,
            "NOTICE_DATE": None,
            "NOTICE_TYPE": self.parser.get_publisher,
            "TRIGGER_NUM": self.parser.get_trigger_num,
            "TRIGGER_DATE": self.parser.get_trigger_date,
            "TRIGGER_TIME": self.parser.get_trigger_time,
            "SEQUENCE_NUM": None,
            "GROUP_TYPE": None,
            "SEARCH_TYPE": None,
            "PIPELINE_TYPE": None,
            "FAR": self.parser.get_far,
            "PROB_NS": self.parser.get_porb_ns,
            "PROB_REMNANT": self.parser.get_porb_remnant,
            "PROB_BNS": self.parser.get_porb_bns,
            "PROB_NSBH": self.parser.get_porb_nsbh,
            "PROB_BBH": self.parser.get_porb_bbh,
            "PROB_MassGap": self.parser.get_porb_massgap,
            "PROB_TERRES": self.parser.get_porb_terres,
            "TRIGGER_ID": None,
            "MISC": None,
            "SKYMAP_FITS_URL": self.parser.get_skymap,
            "EVENTPAGE_URL": self.parser.get_eventpage,
            "COMMENTS": None,
        }

    def nu_em_coincidence(self):
        return {
            "TITLE": None,
            "NOTICE_DATE": None,
            "NOTICE_TYPE": self.parser.get_publisher,
            "AMON_STREAM": None,
            "EVENT_DATE": None,
            "EVENT_NUM": self.parser.get_trigger_num,
            "REVISION": None,
            "RUN_NUM": None,
            "SRC_RA": self.parser.get_ra,
            "SRC_DEC": self.parser.get_dec,
            "SRC_ERROR": self.parser.get_error,
            "SRC_ERROR50": None,
            "DISCOVERY_DATE": self.parser.get_trigger_date,
            "DISCOVERY_TIME": self.parser.get_trigger_time,
            "COINC_PAIR": None,
            "DELTA_T": self.parser.get_delta_t,
            "FAR": self.parser.get_far,
            "TRIG_ID18": None,
            "MISC19": None,
            "SUN_POSTN": None,
            "SUN_DIST": self.parser.get_sun_dist,
            "MOON_POSTN": None,
            "MOON_DIST": self.parser.get_moon_dist,
            "GAL_COORDS": None,
            "ECL_COORDS": None,
            "COMMENTS": None,
        }

    def Fermi_LAT_Position(self):
        return {
            "TITLE": None,
            "NOTICE_DATE": None,
            "NOTICE_TYPE": self.parser.get_publisher,
            "RECORD_NUM": self.parser.get_revision,
            "TRIGGER_NUM": self.parser.get_trigger_num_swift,
            "GRB_RA": self.parser.get_ra,
            "GRB_DEC": self.parser.get_dec,
            "GRB_ERROR": self.parser.get_error,
            "GRB_INTEN_TOT": self.parser.get_total_intens_fermi,
            "GRB_INTEN1": self.parser.get_intens_ebin1_fermi,
            "GRB_INTEN2": self.parser.get_intens_ebin2_fermi,
            "GRB_INTEN3": self.parser.get_intens_ebin3_fermi,
            "GRB_INTEN4": self.parser.get_intens_ebin4_fermi,
            "INTEG_DUR": self.parser.get_integr_dur,
            "FIRST_PHOTON": None,
            "LAST_PHOTON": None,
            "GRB_DATE": self.parser.get_trigger_date,
            "GRB_TIME": self.parser.get_trigger_time,
            "GRB_PHI": None,
            "GRB_THETA": None,
            "SOLN_STATUS": None,
            "BURST_ID": None,
            "TEMP_TEST_STAT": self.parser.get_temp_test_stat,
            "IMAGE_TEST_STAT": self.parser.get_img_test_stat,
            "LOC_QUALITY": None,
            "SUN_POSTN": None,
            "SUN_DIST": self.parser.get_sun_dist,
            "MOON_POSTN": None,
            "MOON_DIST": self.parser.get_moon_dist,
            "MOON_ILLUM": self.parser.get_moon_illum,
            "GAL_COORDS": None,
            "ECL_COORDS": None,
            "COMMENTS": None,
        }

    def Fermi_GBM_Position(self):
        return {
            "TITLE": None,
            "NOTICE_DATE": None,
            "NOTICE_TYPE": self.parser.get_publisher,
            "RECORD_NUM": self.parser.get_revision,
            "TRIGGER_NUM": self.parser.get_trigger_num,
            "GRB_RA": self.parser.get_ra,
            "GRB_DEC": self.parser.get_dec,
            "GRB_ERROR": self.parser.get_error,
            "GRB_INTEN": self.parser.get_total_intens_fermi,
            "DATA_SIGNIF": self.parser.get_significance_agile,
            "DATA_INTERVAL": None,
            "INTEG_TIME": self.parser.get_integr_dur,
            "GRB_DATE": self.parser.get_trigger_date,
            "GRB_TIME": self.parser.get_trigger_time,
            "GRB_PHI": None,
            "GRB_THETA": None,
            "E_RANGE": None,
            "DATA_TIME_SCALE": None,
            "HARD_RATIO": None,
            "LOC_ALGORITHM": None,
            "MOST_LIKELY": self.parser.get_eventtype_likely,
            "2nd_MOST_LIKELY": None,
            "DETECTORS": None,
            "SUN_POSTN": None,
            "SUN_DIST": self.parser.get_sun_dist,
            "MOON_POSTN": None,
            "MOON_DIST": self.parser.get_moon_dist,
            "MOON_ILLUM": self.parser.get_moon_illum,
            "GAL_COORDS": None,
            "ECL_COORDS": None,
            "LC_URL": self.parser.get_eventpage,
            "POS_MAP_URL": None,
            "LOC_URL": None,
            "COMMENTS": None,
        }

    def Fermi_GBM_Flight_Position(self):
        return {
            "TITLE": None,
            "NOTICE_DATE": None,
            "NOTICE_TYPE": self.parser.get_publisher,
            "RECORD_NUM": self.parser.get_revision,
            "TRIGGER_NUM": self.parser.get_trigger_num,
            "GRB_RA": self.parser.get_ra,
            "GRB_DEC": self.parser.get_dec,
            "GRB_ERROR": self.parser.get_error,
            "GRB_INTEN": self.parser.get_total_intens_fermi,
            "DATA_SIGNIF": self.parser.get_significance_agile,
            "INTEG_TIME": self.parser.get_integr_dur,
            "GRB_DATE": self.parser.get_trigger_date,
            "GRB_TIME": self.parser.get_trigger_time,
            "GRB_PHI": None,
            "GRB_THETA": None,
            "DATA_TIME_SCALE": None,
            "HARD_RATIO": None,
            "LOC_ALGORITHM": None,
            "MOST_LIKELY": self.parser.get_eventtype_likely,
            "2nd_MOST_LIKELY": None,
            "DETECTORS": None,
            "SUN_POSTN": None,
            "SUN_DIST": self.parser.get_sun_dist,
            "MOON_POSTN": None,
            "MOON_DIST": self.parser.get_moon_dist,
            "MOON_ILLUM": self.parser.get_moon_illum,
            "GAL_COORDS": None,
            "ECL_COORDS": None,
            "LC_URL": self.parser.get_eventpage,
            "COMMENTS": None,
        }

    def Integral_notice(self):
        return {
            "TITLE": None,
            "NOTICE_DATE": None,
            "NOTICE_TYPE": self.parser.get_publisher,
            "TRIGGER_NUM": self.parser.get_trigger_num,
            "GRB_RA": self.parser.get_ra,
            "GRB_DEC": self.parser.get_dec,
            "GRB_ERROR": self.parser.get_error,
            "GRB_INTEN": self.parser.get_intensity_agile,
            "GRB_TIME": self.parser.get_trigger_time,
            "GRB_DATE": self.parser.get_trigger_date,
            "SC_RA": None,
            "SC_DEC": None,
            "SUN_POSTN": None,
            "SUN_DIST": self.parser.get_sun_dist,
            "MOON_POSTN": None,
            "MOON_DIST": self.parser.get_moon_dist,
            "GAL_COORDS": None,
            "ECL_COORDS": None,
            "COMMENTS": None,
        }

    def LVC_retraction(self):
        return {
            "TITLE": None,
            "NOTICE_DATE": None,
            "NOTICE_TYPE": self.parser.get_publisher,
            "TRIGGER_NUM": self.parser.get_trigger_num,
            "TRIGGER_DATE": self.parser.get_trigger_date,
            "TRIGGER_TIME": self.parser.get_trigger_time,
            "SEQUENCE_NUM": self.parser.get_revision,
            "TRIGGER_ID": None,
            "MISC": None,
            "COMMENTS": None,
        }

    def SWIFT_BAT(self):
        return {
            "TITLE": None,
            "NOTICE_DATE": None,
            "NOTICE_TYPE": self.parser.get_publisher,
            "TRIGGER_NUM": self.parser.get_trigger_num_swift,
            "GRB_RA": self.parser.get_ra,
            "GRB_DEC": self.parser.get_dec,
            "GRB_ERROR": self.parser.get_error,
            "GRB_INTEN": self.parser.get_total_intens_fermi,
            "TRIGGER_DUR": self.parser.get_integr_dur,
            "TRIGGER_INDEX": None,
            "BKG_INTEN": self.parser.get_bkg_intens,
            "BKG_TIME": None,
            "BKG_DUR": self.parser.get_integr_bkg_dur,
            "GRB_DATE": self.parser.get_trigger_date,
            "GRB_TIME": self.parser.get_trigger_time,
            "GRB_PHI": None,
            "GRB_THETA": None,
            "SOLN_STATUS": None,
            "RATE_SIGNIF": self.parser.get_rate_signif,
            "IMAGE_SIGNIF": self.parser.get_image_signif,
            "MERIT_PARAMS": None,
            "SUN_POSTN": None,
            "SUN_DIST": self.parser.get_sun_dist,
            "MOON_POSTN": None,
            "MOON_DIST": self.parser.get_moon_dist,
            "MOON_ILLUM": self.parser.get_moon_illum,
            "GAL_COORDS": None,
            "ECL_COORDS": None,
            "COMMENTS": None,
        }

    def SWIFT_XRT(self):
        return {
            "TITLE": None,
            "NOTICE_DATE": None,
            "NOTICE_TYPE": self.parser.get_publisher,
            "TRIGGER_NUM": self.parser.get_trigger_num_swift,
            "GRB_RA": self.parser.get_ra,
            "GRB_DEC": self.parser.get_dec,
            "GRB_ERROR": self.parser.get_error,
            "GRB_INTEN": self.parser.get_total_intens_fermi,
            "GRB_SIGNIF": self.parser.get_significance_agile,
            "IMG_START_DATE": self.parser.get_trigger_date,
            "IMG_START_TIME": self.parser.get_trigger_time,
            "TAM[0-3]": None,
            "AMPLIFIER": None,
            "WAVEFORM": None,
            "TRIGGER_DUR": self.parser.get_integr_dur,
            "TRIGGER_INDEX": None,
            "BKG_INTEN": self.parser.get_bkg_intens,
            "BKG_TIME": None,
            "BKG_DUR": self.parser.get_integr_bkg_dur,
            "GRB_DATE": self.parser.get_trigger_date,
            "GRB_TIME": self.parser.get_trigger_time,
            "GRB_PHI": None,
            "GRB_THETA": None,
            "SOLN_STATUS": None,
            "RATE_SIGNIF": self.parser.get_rate_signif,
            "IMAGE_SIGNIF": self.parser.get_image_signif,
            "MERIT_PARAMS": None,
            "SUN_POSTN": None,
            "SUN_DIST": self.parser.get_sun_dist,
            "MOON_POSTN": None,
            "MOON_DIST": self.parser.get_moon_dist,
            "MOON_ILLUM": self.parser.get_moon_illum,
            "GAL_COORDS": None,
            "ECL_COORDS": None,
            "COMMENTS": None,
        }

    def SWIFT_XRT_update(self):
        return {
            "TITLE": None,
            "NOTICE_DATE": None,
            "NOTICE_TYPE": self.parser.get_publisher,
            "TRIGGER_NUM": self.parser.get_trigger_num_swift,
            "GRB_RA": self.parser.get_ra,
            "GRB_DEC": self.parser.get_dec,
            "GRB_ERROR": self.parser.get_error,
            "GRB_INTEN": self.parser.get_total_intens_fermi,
            "GRB_SIGNIF": self.parser.get_significance_agile,
            "IMG_START_DATE": self.parser.get_trigger_date,
            "IMG_START_TIME": self.parser.get_trigger_time,
            "TAM[0-3]": None,
            "AMPLIFIER": None,
            "WAVEFORM": None,
            "SUN_POSTN": None,
            "SUN_DIST": self.parser.get_sun_dist,
            "MOON_POSTN": None,
            "MOON_DIST": self.parser.get_moon_dist,
            "MOON_ILLUM": self.parser.get_moon_illum,
            "GAL_COORDS": None,
            "ECL_COORDS": None,
            "COMMENTS": None,
        }

    def SWIFT_UVOT(self):
        return {
            "TITLE": None,
            "NOTICE_DATE": None,
            "NOTICE_TYPE": self.parser.get_publisher,
            "TRIGGER_NUM": self.parser.get_trigger_num_swift,
            "GRB_RA": self.parser.get_ra,
            "GRB_DEC": self.parser.get_dec,
            "GRB_ERROR": self.parser.get_error,
            "GRB_MAG": None,
            "FILTER": None,
            "IMG_START_DATE": self.parser.get_trigger_date,
            "IMG_START_TIME": self.parser.get_trigger_time,
            "SUN_POSTN": None,
            "SUN_DIST": self.parser.get_sun_dist,
            "MOON_POSTN": None,
            "MOON_DIST": self.parser.get_moon_dist,
            "MOON_ILLUM": self.parser.get_moon_illum,
            "GAL_COORDS": None,
            "ECL_COORDS": None,
            "COMMENTS": None,
        }

    def SWIFT_FOM(self):
        return {
            "TITLE": None,
            "NOTICE_DATE": None,
            "NOTICE_TYPE": self.parser.get_publisher,
            "TRIGGER_NUM": self.parser.get_trigger_num_swift,
            "GRB_RA": self.parser.get_ra,
            "GRB_DEC": self.parser.get_dec,
            "GRB_DATE": self.parser.get_trigger_date,
            "GRB_TIME": self.parser.get_trigger_time,
            "TRIGGER_INDEX": None,
            "RATE_SIGNIF": self.parser.get_rate_signif,
            "IMAGE_SIGNIF": self.parser.get_image_signif,
            "FLAGS": None,
            "MERIT": None,
            "SUN_POSTN": None,
            "SUN_DIST": self.parser.get_sun_dist,
            "MOON_POSTN": None,
            "MOON_DIST": self.parser.get_moon_dist,
            "MOON_ILLUM": self.parser.get_moon_illum,
            "GAL_COORDS": None,
            "ECL_COORDS": None,
            "COMMENTS": None,
        }
