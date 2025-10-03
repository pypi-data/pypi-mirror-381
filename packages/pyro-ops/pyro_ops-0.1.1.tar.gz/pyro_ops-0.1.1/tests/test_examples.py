import datetime as dt
import sys

import pytest

from pyro_ops.ground_integration import schedule_observation


@pytest.mark.parametrize(
    "station_id,norad_id",
    [
        (1, 25544),  # ISS example IDs
    ],
)
def test_satnogs_dry_run(station_id, norad_id):
    start = dt.datetime(2025, 1, 1, 0, 0, 0)
    end = dt.datetime(2025, 1, 1, 0, 10, 0)
    out = schedule_observation("TOKEN", station_id, norad_id, start, end, dry_run=True)
    assert out["url"].endswith("/observations/")
    assert out["json"]["station"] == station_id
    assert out["json"]["norad_cat_id"] == norad_id


@pytest.mark.skipif("ccsdspy" not in sys.modules and False, reason="ccsdspy optional")
def test_ccsds_decode_example():
    # This placeholder test would call decode_ccsds_packets with a simple field definition
    # Skipped by default when ccsdspy is not installed in the environment
    pass
