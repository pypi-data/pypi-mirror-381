from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Iterable, Mapping, Optional

import h5py
import numpy as np
import pandas as pd


@dataclass
class HDF5Store:
    """Lightweight HDF5 wrapper for tabular telemetry and metadata.

    Paths use POSIX-style groups, e.g., "/subsystem/parameter".
    """

    path: str

    def write_table(
        self,
        dataset_path: str,
        table: pd.DataFrame,
        metadata: Optional[Mapping[str, Any]] = None,
        overwrite: bool = True,
    ) -> None:
        if not dataset_path.startswith("/"):
            raise ValueError("dataset_path must be absolute, e.g., '/subsystem/param'")

        # Convert DataFrame to a structured numpy array
        array = self._dataframe_to_struct_array(table)

        with h5py.File(self.path, "a") as f:
            # Ensure group exists
            group_path = "/".join(dataset_path.rstrip("/").split("/")[:-1]) or "/"
            if group_path != "/" and group_path not in f:
                f.require_group(group_path)

            if dataset_path in f:
                if not overwrite:
                    raise FileExistsError(f"Dataset '{dataset_path}' already exists")
                del f[dataset_path]

            dset = f.create_dataset(dataset_path, data=array, maxshape=(None,))
            # Attach column names as attribute for round-trip
            dset.attrs["columns"] = np.array(table.columns.tolist(), dtype=object)
            if metadata:
                for key, value in metadata.items():
                    # h5py requires basic types; store JSON-serializable as string if needed
                    try:
                        dset.attrs[key] = value
                    except TypeError:
                        dset.attrs[key] = str(value)

    def append_rows(self, dataset_path: str, rows: pd.DataFrame) -> None:
        with h5py.File(self.path, "a") as f:
            if dataset_path not in f:
                raise KeyError(f"Dataset '{dataset_path}' not found")
            dset = f[dataset_path]
            array = self._dataframe_to_struct_array(rows)
            old_len = dset.shape[0]
            new_len = old_len + array.shape[0]
            dset.resize((new_len,))
            dset[old_len:new_len] = array

    def read_table(self, dataset_path: str) -> pd.DataFrame:
        with h5py.File(self.path, "r") as f:
            if dataset_path not in f:
                raise KeyError(f"Dataset '{dataset_path}' not found")
            dset = f[dataset_path]
            array = dset[...]
            columns_attr = dset.attrs.get("columns")
            if columns_attr is not None:
                columns = [str(c) for c in columns_attr.tolist()]
            else:
                columns = list(array.dtype.names or [])
            df = pd.DataFrame.from_records(array, columns=columns)
        return df

    @staticmethod
    def _dataframe_to_struct_array(df: pd.DataFrame) -> np.ndarray:
        # Create a structured dtype based on dataframe dtypes
        dtype_desc = []
        for col in df.columns:
            series = df[col]
            if pd.api.types.is_integer_dtype(series):
                dtype_desc.append((col, np.int64))
            elif pd.api.types.is_float_dtype(series):
                dtype_desc.append((col, np.float64))
            elif pd.api.types.is_bool_dtype(series):
                dtype_desc.append((col, np.bool_))
            else:
                # Store strings as fixed-length UTF-8; compute max length
                maxlen = int(series.astype(str).map(len).max() or 1)
                dtype_desc.append((col, f"S{maxlen}"))

        structured = np.zeros(len(df), dtype=np.dtype(dtype_desc))
        for col in df.columns:
            if structured[col].dtype.kind == "S":
                structured[col] = df[col].astype(str).str.encode("utf-8")
            else:
                structured[col] = df[col].to_numpy()
        return structured
