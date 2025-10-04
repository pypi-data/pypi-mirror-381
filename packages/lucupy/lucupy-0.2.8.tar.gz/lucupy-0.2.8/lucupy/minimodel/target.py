# Copyright (c) 2016-2024 Association of Universities for Research in Astronomy, Inc. (AURA)
# For license information see LICENSE or https://opensource.org/licenses/BSD-3-Clause

from abc import ABC
from dataclasses import dataclass
from enum import Enum, IntEnum, auto
from typing import NewType, NoReturn, final

from ..decorators import immutable
from .magnitude import Magnitudes

__all__ = [
    'GuideSpeed',
    'NonsiderealTarget',
    'SiderealTarget',
    'Target',
    'TargetName',
    'TargetTag',
    'TargetType',
]


TargetName = NewType('TargetName', str)


@final
class TargetType(Enum):
    """The type associated with a target in an observation.

    Members:
        - BASE
        - USER
        - BLIND_OFFSET
        - OFF_AXIS
        - TUNING_STAR
        - GUIDESTAR
        - OTHER
    """
    BASE = auto()
    USER = auto()
    BLIND_OFFSET = auto()
    OFF_AXIS = auto()
    TUNING_STAR = auto()
    GUIDESTAR = auto()
    OTHER = auto()


@final
class GuideSpeed(IntEnum):
    """
    How quickly a guider can guide on a guide star.

    Members:
        - SLOW
        - MEDIUM
        - FAST

    """
    SLOW = auto()
    MEDIUM = auto()
    FAST = auto()


@final
class TargetTag(Enum):
    """
    A tag used by nonsidereal targets to indicate their type.
    """
    COMET = auto()
    ASTEROID = auto()
    MAJORBODY = auto()


@immutable
@dataclass(frozen=True)
class Target(ABC):
    """
    Basic target information.

    Attributes:
        - name: TargetName
        - magnitudes: Magnitudes
        - type: TargetType
    """
    name: TargetName
    magnitudes: Magnitudes
    type: TargetType

    def guide_speed(self) -> NoReturn:
        """
        Calculate the guide speed for this target.
        """
        raise NotImplementedError


@final
@immutable
@dataclass(frozen=True)
class SiderealTarget(Target):
    """
    For a SiderealTarget, we have an RA and Dec and then proper motion information
    to calculate the exact position.

    RA and Dec should be specified in decimal degrees.
    Proper motion must be specified in milliarcseconds / year.
    Epoch must be the decimal year.

    NOTE: The proper motion adjusted coordinates can be found in the TargetInfo in coord.

    Attributes:
        ra (float): Right Ascension
        dec (float): Declination
        pm_ra (float): Proper motion of the right ascension component.
        pm_dec (float): Proper motion of the declination component.
        epoch (float): The epoch in which the ra / dec were measured.

    """
    ra: float
    dec: float
    pm_ra: float
    pm_dec: float
    epoch: float


@final
@immutable
@dataclass(frozen=True)
class NonsiderealTarget(Target):
    """
    For a NonsiderealTarget, we have a JPL/Horizons designation to indicate the lookup
    information and a tag to determine the type of target.
    Ephemeris data will be looked up as necessary.

    Attributes:
        des (str): Horizon designation
        tag (TargetTag): TargetTag
    """
    des: str
    tag: TargetTag
