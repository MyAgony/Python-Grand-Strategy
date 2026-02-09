from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(frozen=True)
class Province:
    """Represents a playable province on the campaign map."""

    name: str
    terrain: str
    neighbors: List[str]
    owner: str


@dataclass
class GameState:
    """Holds the state of the running campaign."""

    provinces: Dict[str, Province] = field(default_factory=dict)
    factions: Dict[str, Dict[str, str]] = field(default_factory=dict)

    def add_province(self, province: Province) -> None:
        self.provinces[province.name] = province

    def province_summary(self) -> List[str]:
        return [
            f"{province.name} ({province.terrain}) - Owner: {province.owner}"
            for province in self.provinces.values()
        ]
