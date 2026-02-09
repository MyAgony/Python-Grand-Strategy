"""Core package for the Python Grand Strategy prototype."""

from .game_state import GameState, Province
from .map_loader import load_provinces

__all__ = ["GameState", "Province", "load_provinces"]
