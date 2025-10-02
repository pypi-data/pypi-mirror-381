"""Models for Open Data Platform of Brussel."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any


@dataclass
class Garage:
    """Object representing a garage."""

    garage_id: str
    name: dict[str, str]
    capacity: int
    provider: str

    longitude: float
    latitude: float

    updated_at: datetime

    @classmethod
    def from_dict(cls: type[Garage], data: dict[str, Any]) -> Garage:
        """Return a Garage object from a dictionary.

        Args:
        ----
            data: The data from the API.

        Returns:
        -------
            A Garage object.

        """
        attr = data["fields"]
        geo = data["geometry"]["coordinates"]
        return cls(
            garage_id=str(data.get("recordid")),
            name={lang: attr.get(f"name_{lang}") for lang in ["fr", "nl"]},
            capacity=attr.get("capacity"),
            provider=attr.get("operator_fr"),
            longitude=geo[0],
            latitude=geo[1],
            updated_at=datetime.strptime(
                str(data.get("record_timestamp")),
                "%Y-%m-%dT%H:%M:%S.%fZ",
            ).replace(tzinfo=UTC),
        )


@dataclass
class DisabledParking:
    """Object representing a disabled parking."""

    spot_id: str
    number: int
    orientation: str
    area: dict[str, str]

    longitude: float
    latitude: float

    updated_at: datetime

    @classmethod
    def from_dict(cls: type[DisabledParking], data: dict[str, Any]) -> DisabledParking:
        """Return a DisabledParking object from a dictionary.

        Args:
        ----
            data: The data from the API.

        Returns:
        -------
            A DisabledParking object.

        """
        attr = data["fields"]
        geo = data["geometry"]["coordinates"]
        return cls(
            spot_id=str(data.get("recordid")),
            number=attr.get("evp"),
            orientation=attr.get("orientation_en"),
            area={
                "en": attr.get("area"),
                "fr": attr.get("zones_fr"),
                "nl": attr.get("zones_nl"),
            },
            longitude=geo[0],
            latitude=geo[1],
            updated_at=datetime.strptime(
                str(data.get("record_timestamp")),
                "%Y-%m-%dT%H:%M:%S.%fZ",
            ).replace(tzinfo=UTC),
        )
