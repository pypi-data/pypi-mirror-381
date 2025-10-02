"""Create functions to parse alerts."""

from .. import too_event


class GCNParserMethods:
    def __init__(self) -> None:
        self.event = too_event.ToOEvent()
        self.ra = 0
        self.dec = 0
        self.frame = "icrs"
        self.event.params = {}

    def set_eventtype(self, pub) -> None:
        lobs = [
            "Fermi-LAT",
            "Fermi-GBM",
            "LVC",
            "MAXI",
            "SuperAGILE",
            "INTEGRAL",
            "Swift-BAT",
            "Swift-FOM",
            "Swift-XRT",
        ]
        name = ""
        if any(item in ["test", "Test", "TEST"] for item in pub.split()):
            name += "TEST "
        if matches := [x for x in lobs if any(item in [x] for item in pub.split())]:
            name += matches[0]
        self.event.event_type = name

    def set_eventtype_maxi(self, line: str) -> None:
        self.event.event_type = str(line.split(":")[1].split()[0].strip())

    def set_eventid(self, line: str) -> None:
        self.event.event_id = str(line.split(":")[1].strip())

    def set_type_grb(self, type: str) -> None:
        self.event.event_type = "GRB"

    def combine_date_coords(self):
        year = self.trigger_date.split("-")[0]
        if len(year) == 2:
            self.trigger_date = self.trigger_date = f"20{self.trigger_date}"
        self.event.set_time(f"{self.trigger_date}T{self.trigger_time}")
        self.event.set_coordinates(self.ra, self.dec, frame=self.frame)

    def get_num_value(self, line: str) -> str:
        return str(line.split(":")[1].split()[0].strip())

    def get_unit_info(self, line: str) -> str:
        return str(line.split(":")[1].split()[1:])

    def strip_sq_bracket(self, line: str) -> str:
        return line.split("['[")[1].split("]")[0].strip()

    def strip_rd_bracket(self, line: str) -> str:
        return line.split("(")[1].split(")")[0].strip()

    def get_eventtype_likely(self, line: str) -> None:
        self.event.params["event_type_likely"] = (
            str(line.split(":")[1].split("%")[1].strip())
            + ","
            + str(line.split(":")[1].split("%")[0].strip())
            + "%"
        )
        self.event.event_type = str(line.split(":")[1].split("%")[1].strip())

    def get_publisher(self, line: str) -> str:
        self.event.publisher = line.split(":")[1].strip()
        self.set_eventtype(self.event.publisher)
        return self.event.publisher

    def get_trigger_num(self, line: str) -> None:
        self.event.publisher_id = line.split(":")[1].strip()

    def get_trigger_num_swift(self, line: str) -> None:
        self.event.publisher_id = line.split(":")[1].split(",")[0].strip()

    def get_trigger_date(self, line: str) -> None:
        self.trigger_date = line.split(";")[-1].split()[0].strip().replace("/", "-")

    def get_trigger_time(self, line: str) -> None:
        self.trigger_time = line.split("{")[1].split("}")[0]

    def get_far(self, line: str) -> None:
        self.event.params["false_alarm_rate"] = (
            str(line.split(":")[1].split()[0].strip())
            + ","
            + line.split(":")[1].split()[1].strip("[").strip("]")
        )

    def get_porb_ns(self, line: str) -> None:
        self.event.params["prob_ns"] = float(line.split(":")[1].split()[0].strip())

    def get_porb_remnant(self, line: str) -> None:
        self.event.params["prob_remnant"] = float(line.split(":")[1].split()[0].strip())

    def get_porb_bns(self, line: str) -> None:
        self.event.params["prob_bns"] = float(line.split(":")[1].split()[0].strip())

    def get_porb_nsbh(self, line: str) -> None:
        self.event.params["prob_nsbh"] = float(line.split(":")[1].split()[0].strip())

    def get_porb_bbh(self, line: str) -> None:
        self.event.params["prob_nsbh"] = float(line.split(":")[1].split()[0].strip())

    def get_porb_massgap(self, line: str) -> None:
        self.event.params["prob_massgap"] = float(line.split(":")[1].split()[0].strip())

    def get_porb_terres(self, line: str) -> None:
        self.event.params["prob_terres"] = float(line.split(":")[1].split()[0].strip())

    def get_skymap(self, line: str) -> None:
        self.event.params["skymap_url"] = line.split()[1].strip()

    def get_eventpage(self, line: str) -> None:
        self.event.params["eventpage_url"] = line.split()[1].strip()

    def get_ra(self, line: str) -> None:
        self.frame = "fk5"
        self.ra = float(line.split(":")[1].strip().split("d")[0])

    def get_dec(self, line: str) -> None:
        self.frame = "fk5"
        self.dec = float(line.split(":")[1].strip().split("d")[0])

    def get_error(self, line: str) -> None:
        self.event.params["localization_error"] = (
            str(line.split(":")[1].split("[")[0].strip())
            + line.split(":")[1].split("[")[1].split("]")[0]
        )

    def get_flux(self, line: str) -> None:
        self.event.params["flux"] = (
            str(line.split(":")[1].split("+")[0].strip())
            + ","
            + str(line.split(":")[1].split("-")[1].split("[")[0].strip())
            + ","
            + line.split(":")[1].split("[")[1].split("]")[0]
        )

    def get_tscale(self, line: str) -> None:
        self.event.params["time_scale_s"] = float(
            line.split(":")[1].split("s")[0].strip()
        )

    def get_eband(self, line: str) -> None:
        self.event.params["obs_energy_range"] = line.split(":")[1].strip()

    def get_sun_dist(self, line: str) -> None:
        self.event.params["sun_dist"] = (
            str(line.split(":")[1].split()[0].strip())
            + ","
            + line.split(":")[1].split()[1].strip().strip("[").strip("]")
        )

    def get_moon_dist(self, line: str) -> None:
        self.event.params["moon_dist"] = (
            str(line.split(":")[1].split()[0].strip())
            + ","
            + line.split(":")[1].split()[1].strip().strip("[").strip("]")
        )

    def get_moon_illum(self, line: str) -> None:
        self.event.params["moon_illum"] = (
            float(line.split(":")[1].split()[0].strip()) / 100
        )

    def get_intensity_agile(self, line: str) -> None:
        self.event.params["intensity"] = (
            str(line.split(":")[1].split()[0].strip())
            + ","
            + line.split(":")[1].split("[")[1].split("]")[0]
        )

    def get_significance_agile(self, line: str) -> None:
        self.event.params["significance"] = (
            str(line.split(":")[1].split()[0].strip())
            + ","
            + line.split(":")[1].split("[")[1].split("]")[0]
        )

    def get_revision(self, line: str) -> None:
        self.event.params["revision"] = float(line.split(":")[1].strip())

    def get_energy(self, line: str) -> None:
        self.event.params["energy"] = (
            str(float(line.split(":")[1].split()[0].strip()))
            + ","
            + line.split(":")[1].split("[")[1].split("]")[0]
        )

    def get_signalness(self, line: str) -> None:
        self.event.params["signalness"] = (
            str(line.split(":")[1].split()[0].strip())
            + ","
            + line.split(":")[1].split("[")[1].split("]")[0]
        )

    def get_pvalue(self, line: str) -> None:
        self.event.params["p_value"] = float(line.split(":")[1].split()[0].strip())

    def get_delta_t(self, line: str) -> None:
        self.event.params["delta_t"] = (
            str(line.split(":")[1].split()[0].strip())
            + ","
            + line.split(":")[1].split("[")[1].split("]")[0]
        )

    def get_total_intens_fermi(self, line: str) -> None:
        self.event.params["total_inten"] = (
            self.get_num_value(line)
            + ","
            + self.strip_sq_bracket(self.get_unit_info(line))
        )

    def get_intens_ebin1_fermi(self, line: str) -> None:
        self.event.params["inten_ebin_1"] = (
            self.get_num_value(line)
            + ","
            + line.split(":")[1].split("[")[1].split("]")[0]
            + line.split(":")[1].split("[")[1].split("]")[1].strip()
        )

    def get_intens_ebin2_fermi(self, line: str) -> None:
        self.event.params["inten_ebin_2"] = (
            self.get_num_value(line)
            + ","
            + line.split(":")[1].split("[")[1].split("]")[0]
            + line.split(":")[1].split("[")[1].split("]")[1].strip()
        )

    def get_intens_ebin3_fermi(self, line: str) -> None:
        self.event.params["inten_ebin_3"] = (
            self.get_num_value(line)
            + ","
            + line.split(":")[1].split("[")[1].split("]")[0]
            + line.split(":")[1].split("[")[1].split("]")[1].strip()
        )

    def get_intens_ebin4_fermi(self, line: str) -> None:
        self.event.params["inten_ebin_4"] = (
            self.get_num_value(line)
            + ","
            + line.split(":")[1].split("[")[1].split("]")[0]
            + line.split(":")[1].split("[")[1].split("]")[1].strip()
        )

    def get_integr_dur(self, line: str) -> None:
        self.event.params["integated_duration"] = (
            self.get_num_value(line)
            + ","
            + self.strip_sq_bracket(self.get_unit_info(line))
        )

    def get_temp_test_stat(self, line: str) -> None:
        self.event.params["temp_test_stat"] = (
            self.get_num_value(line)
            + ","
            + self.strip_rd_bracket(self.get_unit_info(line))
        )

    def get_img_test_stat(self, line: str) -> None:
        self.event.params["image_test_stat"] = (
            self.get_num_value(line)
            + ","
            + self.strip_rd_bracket(self.get_unit_info(line))
        )

    def get_bkg_intens(self, line: str) -> None:
        self.event.params["background_inten"] = (
            self.get_num_value(line)
            + ","
            + self.strip_sq_bracket(self.get_unit_info(line))
        )

    def get_integr_bkg_dur(self, line: str) -> None:
        self.event.params["integated_background_duration"] = (
            self.get_num_value(line)
            + ","
            + self.strip_sq_bracket(self.get_unit_info(line))
        )

    def get_rate_signif(self, line: str) -> None:
        self.event.params["rate_significance"] = (
            self.get_num_value(line)
            + ","
            + self.strip_sq_bracket(self.get_unit_info(line))
        )

    def get_image_signif(self, line: str) -> None:
        self.event.params["image_significance"] = (
            self.get_num_value(line)
            + ","
            + self.strip_sq_bracket(self.get_unit_info(line))
        )
