# Pyro-Ops

Ground-segment operations toolkit for SmallSat missions: CCSDS telemetry ingestion, standardized HDF5 persistence with mission metadata, basic FDIR analytics, a safe-by-design command DSL validated against mission definitions, and ground network integration hooks.

## Install

```bash
pip install pyro-ops
```

Optional extras:

- Orbits: `pip install pyro-ops[orbits]`
- XTCE: `pip install pyro-ops[xtce]`
- ML (batch): `pip install pyro-ops[ml]`
- ML (streaming): `pip install pyro-ops[ml_stream]`
- Space (astropy/sgp4/spiceypy): `pip install pyro-ops[space]`
- PUS tools: `pip install pyro-ops[pus]`
- Docs: `pip install pyro-ops[docs]`

## Quickstart

```python
from pyro_ops.analysis_core import rolling_zscore
from pyro_ops.data_persistence import HDF5Store

import pandas as pd

series = pd.Series([1, 1, 1, 10, 1, 1])
z = rolling_zscore(series, window=3)

store = HDF5Store("telemetry.h5")
store.write_table("/payload/temp", pd.DataFrame({"t": [1,2,3], "temp": [20.1, 20.5, 21.0]}), metadata={"unit": "C"})
```

## Architecture

- Data Interface: CCSDS packet decode wrappers
- Data Persistence: HDF5 + MetaSat JSON-LD metadata
- Analysis Core: FDIR utilities and ML hooks
- Operations Control: DSL + XTCE/eICD ingestion stubs
- Ground Integration: SatNOGS API and orbit propagation helpers

## License

Apache-2.0
