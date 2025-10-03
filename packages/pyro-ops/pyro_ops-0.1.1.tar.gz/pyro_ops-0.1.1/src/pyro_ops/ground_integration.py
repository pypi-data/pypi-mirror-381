from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

import datetime as dt
import requests

try:
    from skyfield.api import EarthSatellite, load  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    EarthSatellite = None  # type: ignore
    load = None  # type: ignore

# Optional: sgp4 direct
try:  # pragma: no cover - optional import
    from sgp4.api import Satrec, jday
except Exception:
    Satrec = None  # type: ignore
    jday = None  # type: ignore

# Optional: SPICE
try:  # pragma: no cover - optional import
    import spiceypy as spice  # type: ignore
except Exception:
    spice = None  # type: ignore


SATNOGS_BASE = "https://network.satnogs.org/api/"


def schedule_observation(
    api_token: str,
    station_id: int,
    norad_id: int,
    start: dt.datetime,
    end: dt.datetime,
    *,
    dry_run: bool = False,
) -> Dict[str, Any]:
    headers = {"Authorization": f"Token {api_token}"}
    payload = {
        "station": station_id,
        "norad_cat_id": norad_id,
        "start": start.isoformat(),
        "end": end.isoformat(),
    }
    if dry_run:
        return {"url": f"{SATNOGS_BASE}observations/", "headers": headers, "json": payload}

    resp = requests.post(f"{SATNOGS_BASE}observations/", headers=headers, json=payload, timeout=30)
    resp.raise_for_status()
    return resp.json()


def propagate_tle(tle_line1: str, tle_line2: str, at_time: Optional[dt.datetime] = None) -> Dict[str, float]:
    """Propagate a TLE to a given time using skyfield; returns ECI position (km)."""
    if EarthSatellite is None or load is None:
        raise ImportError("Install pyro-ops[orbits] for skyfield propagation.")
    ts = load.timescale()
    t = ts.from_datetime(at_time or dt.datetime.utcnow())
    sat = EarthSatellite(tle_line1, tle_line2, "PYRO", ts)
    position = sat.at(t).position.km
    return {"x": float(position[0]), "y": float(position[1]), "z": float(position[2])}


def propagate_tle_sgp4(tle_line1: str, tle_line2: str, at_time: Optional[dt.datetime] = None) -> Dict[str, float]:
    """Propagate a TLE using pure sgp4 to ECI (km)."""
    if Satrec is None or jday is None:
        raise ImportError("Install pyro-ops[space] for sgp4 propagation.")
    at_time = at_time or dt.datetime.utcnow()
    sat = Satrec.twoline2rv(tle_line1, tle_line2)
    jd, fr = jday(at_time.year, at_time.month, at_time.day, at_time.hour, at_time.minute, at_time.second + at_time.microsecond * 1e-6)
    e, r, v = sat.sgp4(jd, fr)
    if e != 0:
        raise RuntimeError(f"SGP4 propagation error code: {e}")
    return {"x": float(r[0]), "y": float(r[1]), "z": float(r[2])}


def spice_position(body: str, et: float, frame: str = "J2000") -> Dict[str, float]:
    """Query SPICE position vector for a given body at ephemeris time (seconds past J2000)."""
    if spice is None:
        raise ImportError("Install pyro-ops[space] for SPICE queries (spiceypy).")
    state, _ = spice.spkezr(body, et, frame, "NONE", "SOLAR SYSTEM BARYCENTER")
    return {"x": float(state[0] / 1000.0), "y": float(state[1] / 1000.0), "z": float(state[2] / 1000.0)}
