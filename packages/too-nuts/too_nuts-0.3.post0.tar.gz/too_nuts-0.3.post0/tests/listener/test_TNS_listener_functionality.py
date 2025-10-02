import pytest

from nuts.alert_listeners import TNS_download, TNS_parser
from nuts.config.config import ToOConfig

####################################################################################################
# Fixtures
####################################################################################################


@pytest.fixture(autouse=True)
def no_http_requests(monkeypatch):
    class MyResponse:
        def __init__(self, text="", status_code=200):
            self.text = text
            self.status_code = 200
            self.counter = 0

        def __call__(self, *args, **kwds):
            self.counter += 1
            with open(
                f"tests/test_data/tns_request/tns_search_results_{self.counter}.dat"
            ) as f:
                self.text = f.read()
            with open(
                f"tests/test_data/tns_request/tns_search_results_{self.counter}.status"
            ) as f:
                self.status_code = int(f.read())

            return self

    response = MyResponse()
    monkeypatch.setattr("requests.post", response)


####################################################################################################
# Test the TNS listener functionality
####################################################################################################


def test_run_TNS(config: ToOConfig):
    """Test run of TNS listener

    Assumption: The downloaded list of sources after it is parsed is not empty

    Args:
        config (fixture): loads config file
    """

    tns_filename = TNS_download.search_tns(config)
    tns_events = TNS_parser.read_TNS_table(
        tns_filename,
    )
    assert tns_events is not None
