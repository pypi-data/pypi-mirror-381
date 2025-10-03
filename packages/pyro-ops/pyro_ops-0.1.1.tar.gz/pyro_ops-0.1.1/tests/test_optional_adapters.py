import datetime as dt
import importlib
import numpy as np
import pytest

from pyro_ops.analysis_core import SKIsolationForestDetector, RiverHSTDetector
from pyro_ops.ground_integration import propagate_tle_sgp4


@pytest.mark.skipif(SKIsolationForestDetector is None, reason="sklearn not installed")
def test_sklearn_adapter_smoke():
    X = np.random.randn(50, 3)
    det = SKIsolationForestDetector(n_estimators=10, random_state=0)
    det.fit(X)
    scores = det.score(X[:5])
    assert scores.shape == (5,)


@pytest.mark.skipif(RiverHSTDetector is None, reason="river not installed")
def test_river_adapter_smoke():
    X = np.random.randn(10, 2)
    det = RiverHSTDetector()
    det.fit(X)
    s = det.score(X[:3])
    assert s.shape == (3,)


@pytest.mark.skipif(importlib.util.find_spec("sgp4") is None, reason="sgp4 not installed")
def test_sgp4_propagation_smoke():
    tle1 = "1 25544U 98067A   20029.54791435  .00001264  00000-0  29621-4 0  9996"
    tle2 = "2 25544  51.6438  58.2212 0007415  63.3338  51.2746 15.49108619210616"
    pos = propagate_tle_sgp4(tle1, tle2, at_time=dt.datetime(2020, 1, 29, 13, 9, 0))
    assert set(pos.keys()) == {"x", "y", "z"}
