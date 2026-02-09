from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from .game_state import GameState, Province


DEFAULT_DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "provinces.json"


def load_provinces(path: Path | str = DEFAULT_DATA_PATH) -> GameState:
    """Load province data from JSON into a GameState."""

    data_path = Path(path)
    payload = json.loads(data_path.read_text(encoding="utf-8"))

    state = GameState()
    state.factions = payload.get("factions", {})

    for province_data in payload.get("provinces", []):
        province = Province(
            name=province_data["name"],
            terrain=province_data["terrain"],
            neighbors=list(province_data.get("neighbors", [])),
            owner=province_data["owner"],
        )
        state.add_province(province)

    return state


def list_neighbors(state: GameState, province_name: str) -> Iterable[str]:
    province = state.provinces.get(province_name)
    if not province:
        return []
    return province.neighbors
