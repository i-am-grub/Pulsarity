"""
Enums for race management
"""

from enum import Flag, auto


class RaceStatus(Flag):
    """
    Current status of system.
    """

    READY = auto()
    """Ready to start a new race, no race running"""
    SCHEDULED = auto()
    """The race is scheduled to occur"""
    STAGING = auto()
    """System is staging; Race begins imminently"""
    RACING = auto()
    """Racing is underway"""
    OVERTIME = auto()
    """The duration of the race has been exceeded; Racing is still underway"""
    PAUSED = auto()
    """Racing is paused"""
    STOPPED = auto()
    """System no longer listening for lap crossings; Race results must be saved or discarded"""
    UNDERWAY = RACING | OVERTIME
    """Shortcut for `RACING` or `OVERTIME`"""
    FINISHED = OVERTIME | STOPPED
    """Shortcut for `OVERTIME` or `STOPPED`"""
    SUSPENDED = READY | SCHEDULED | STAGING | PAUSED | STOPPED
    """Shortcut for a race not being actively underway"""
    PRERACE = READY | SCHEDULED | STAGING
    """Shortcut for pre-race statuses"""
    PREPERATION = SCHEDULED | STAGING
    """Shortcut for race preperation statuses"""
