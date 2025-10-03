from __future__ import annotations

from typing import Any, Dict, Iterable, List

try:
    from ccsdspy import Packet
except Exception:  # pragma: no cover - optional dependency
    Packet = None  # type: ignore


def decode_ccsds_packets(packet_definition: Dict[str, Any], data_stream: bytes) -> List[Dict[str, Any]]:
    """Decode CCSDS packets using a field definition compatible with ccsdspy.

    Parameters
    ----------
    packet_definition : Dict[str, Any]
        Definition dict (fields, types, lengths) acceptable to ccsdspy.Packet.
    data_stream : bytes
        Raw concatenated packet bytes.

    Returns
    -------
    List[Dict[str, Any]]
        A list of decoded field dicts for each packet.
    """
    if Packet is None:
        raise ImportError("ccsdspy is required for CCSDS decoding; install pyro-ops and ccsdspy")

    pkt = Packet(fields=packet_definition["fields"])  # type: ignore[index]
    decoded = pkt.unpack(data_stream)

    # ccsdspy returns dict of field->np.array; convert to list of dicts row-wise
    num_rows = len(next(iter(decoded.values()))) if decoded else 0
    results: List[Dict[str, Any]] = []
    for i in range(num_rows):
        row = {k: v[i].item() if hasattr(v[i], "item") else v[i] for k, v in decoded.items()}
        results.append(row)
    return results
