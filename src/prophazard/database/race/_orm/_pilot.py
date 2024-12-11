"""
ORM classes for Pilot data
"""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..._base import _RaceAttribute, _RaceBase


class PilotAttribute(_RaceAttribute, _RaceBase):
    """
    Unique and stored individually stored values for each pilot.
    """

    __tablename__ = "pilot_attribute"

    id: Mapped[int] = mapped_column(
        ForeignKey("pilot.id"), nullable=False, primary_key=True
    )
    """ID of pilot to which this attribute is assigned"""


class Pilot(_RaceBase):
    """
    A pilot is an individual participant. In order to participate in races,
    pilots can be assigned to multiple heats.

    The sentinel value :atts:`RHUtils.PILOT_ID_NONE` should be used when no pilot is defined.
    """

    __tablename__ = "pilot"

    callsign: Mapped[str] = mapped_column(String(80))
    """Pilot callsign"""
    phonetic: Mapped[str] = mapped_column(String(80))
    """Phonetically-spelled callsign, used for text-to-speech"""
    name: Mapped[str] = mapped_column(String(120))
    """Pilot name"""
    used_frequencies: Mapped[str | None] = mapped_column()
    """Serialized list of frequencies this pilot has been assigned when starting a race, ordered by recency"""
    active: Mapped[bool] = mapped_column(default=True)
    """Not yet implemented"""
    attributes: Mapped[list[PilotAttribute]] = relationship()
    """PilotAttributes for this pilot. Access through awaitable attributes."""

    def __init__(
        self, *, name: str = "", callsign: str = "", phonetic: str = ""
    ) -> None:
        """
        Class initalizer

        :param str name: _description_, defaults to ""
        :param str callsign: _description_, defaults to ""
        :param str phonetic: _description_, defaults to ""
        """
        self.name = name
        self.callsign = callsign
        self.phonetic = phonetic

    @property
    def display_callsign(self):
        if self.callsign:
            return self.callsign
        if self.name:
            return self.name
        return "{} {}".format(("Pilot"), id)

    @property
    def display_name(self):
        if self.name:
            return self.name
        if self.callsign:
            return self.callsign
        return "{} {}".format(("Pilot"), id)

    @property
    def spoken_callsign(self):
        if self.phonetic:
            return self.phonetic
        if self.callsign:
            return self.callsign
        if self.name:
            return self.name
        return "{} {}".format(("Pilot"), id)

    def __repr__(self):
        return "<Pilot %r>" % self.id
