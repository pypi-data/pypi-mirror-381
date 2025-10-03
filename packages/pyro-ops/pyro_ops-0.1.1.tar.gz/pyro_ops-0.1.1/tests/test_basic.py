import datetime as dt

import pandas as pd

from pyro_ops.analysis_core import rolling_zscore
from pyro_ops.data_persistence import HDF5Store
from pyro_ops.operations_control import CommandSequence


def test_rolling_zscore_smoke():
    s = pd.Series([1, 1, 1, 10, 1, 1])
    z = rolling_zscore(s, window=3)
    assert len(z) == 6


def test_hdf5_store_roundtrip(tmp_path):
    path = tmp_path / "t.h5"
    store = HDF5Store(str(path))
    df = pd.DataFrame({"t": [1, 2, 3], "v": [0.1, 0.2, 0.3]})
    store.write_table("/subsystem/param", df, metadata={"unit": "V"})
    out = store.read_table("/subsystem/param")
    assert list(out.columns) == ["t", "v"]
    assert len(out) == 3


def test_command_sequence_serialize():
    seq = CommandSequence().add("SET_MODE", mode=3).add("PING")
    payloads = seq.serialize()
    assert isinstance(payloads, list)
    assert payloads[0].startswith(b"SET_MODE")
