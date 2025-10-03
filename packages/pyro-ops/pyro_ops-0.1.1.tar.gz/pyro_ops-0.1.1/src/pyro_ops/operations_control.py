from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

try:
    from lxml import etree  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    etree = None  # type: ignore


@dataclass
class Command:
    name: str
    params: Dict[str, Any]

    def serialize(self) -> bytes:
        # Placeholder serialization; real implementation would use XTCE constraints
        payload = ",".join(f"{k}={v}" for k, v in self.params.items())
        return f"{self.name}:{payload}".encode("utf-8")


class CommandSequence:
    def __init__(self) -> None:
        self._commands: List[Command] = []

    def add(self, name: str, **params: Any) -> "CommandSequence":
        self._commands.append(Command(name=name, params=params))
        return self

    def serialize(self) -> List[bytes]:
        return [cmd.serialize() for cmd in self._commands]


def load_xtce(path: str) -> Any:
    """Load an XTCE XML file to an in-memory tree for validation/lookup.

    Returns an XML tree; callers can normalize to an internal schema.
    """
    if etree is None:
        raise ImportError("XTCE support requires 'lxml'. Install pyro-ops[xtce].")
    parser = etree.XMLParser(remove_comments=True, resolve_entities=False)
    with open(path, "rb") as f:
        return etree.parse(f, parser)
