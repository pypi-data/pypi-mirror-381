"""Data-related information"""
# pylint: disable=no-member,no-name-in-module

import curses
from enum import IntEnum
from typing import NamedTuple, Generic, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from .scene import Scene

T = TypeVar("T")

class ReturnType(IntEnum):
    """Return type"""

    OK = 0
    ERR = 1
    ERR_BACK = 2
    RETURN_TO_MAIN = 3
    BACK = 4
    CONTINUE = 5
    EXIT = -1

    OVERRIDE = 99
    REVERT_OVERRIDE = 100

class ReturnInfo(Generic[T], NamedTuple):
    """Return info"""
    type: ReturnType
    reason: str
    additional_info: T

class _StatusInfo:
    """Set status bar (bottom bar) information"""
    def __init__(self) -> None:
        self._data = " "

    def get(self) -> str:
        """Get current status info"""
        return self._data

    def set(self, value: str):
        """Set status info"""
        self._data = value

    def reset(self):
        """Reset status info"""
        self._data = " "

class SceneResult(NamedTuple):
    """Scene result, usable when returning Scene"""
    scene: "Scene"
    target: curses.window | None = None

status = _StatusInfo()
