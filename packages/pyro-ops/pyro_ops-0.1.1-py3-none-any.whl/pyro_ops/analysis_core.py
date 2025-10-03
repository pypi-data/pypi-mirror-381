from __future__ import annotations

from typing import Protocol, Any

import numpy as np
import pandas as pd


def rolling_zscore(series: pd.Series, window: int, min_periods: int | None = None) -> pd.Series:
    if min_periods is None:
        min_periods = window
    rolling_mean = series.rolling(window=window, min_periods=min_periods).mean()
    rolling_std = series.rolling(window=window, min_periods=min_periods).std(ddof=0)
    z = (series - rolling_mean) / rolling_std.replace({0.0: np.nan})
    z = z.fillna(0.0)
    return z


class AnomalyDetector(Protocol):
    def fit(self, X: np.ndarray) -> "AnomalyDetector":
        ...

    def score(self, X: np.ndarray) -> np.ndarray:
        ...


# scikit-learn adapter
try:  # pragma: no cover - optional import
    from sklearn.ensemble import IsolationForest as _SkIsolationForest  # type: ignore

    class SKIsolationForestDetector:
        def __init__(self, **kwargs: Any) -> None:
            self._model = _SkIsolationForest(**kwargs)

        def fit(self, X: np.ndarray) -> "SKIsolationForestDetector":
            self._model.fit(X)
            return self

        def score(self, X: np.ndarray) -> np.ndarray:
            # Higher score means more normal in sklearn; invert to anomaly score in [0, +)
            scores = -self._model.score_samples(X)
            return scores.astype(float)

except Exception:  # pragma: no cover
    SKIsolationForestDetector = None  # type: ignore


# PyOD adapter
try:  # pragma: no cover - optional import
    from pyod.models.ecod import ECOD as _PyodECOD  # type: ignore

    class PyODECODDetector:
        def __init__(self, **kwargs: Any) -> None:
            self._model = _PyodECOD(**kwargs)

        def fit(self, X: np.ndarray) -> "PyODECODDetector":
            self._model.fit(X)
            return self

        def score(self, X: np.ndarray) -> np.ndarray:
            return self._model.decision_function(X).astype(float)

except Exception:  # pragma: no cover
    PyODECODDetector = None  # type: ignore


# River (streaming) adapter
try:  # pragma: no cover - optional import
    from river.anomaly import HalfSpaceTrees as _RiverHST  # type: ignore

    class RiverHSTDetector:
        def __init__(self, **kwargs: Any) -> None:
            self._model = _RiverHST(**kwargs)

        def fit(self, X: np.ndarray) -> "RiverHSTDetector":
            # River is online; consume rows
            for row in X:
                features = {str(i): float(v) for i, v in enumerate(row)}
                # river models mutate in place and return self; avoid reassigning
                self._model.learn_one(features)
            return self

        def score(self, X: np.ndarray) -> np.ndarray:
            scores = []
            for row in X:
                features = {str(i): float(v) for i, v in enumerate(row)}
                scores.append(float(self._model.score_one(features)))
            return np.asarray(scores, dtype=float)

except Exception:  # pragma: no cover
    RiverHSTDetector = None  # type: ignore
