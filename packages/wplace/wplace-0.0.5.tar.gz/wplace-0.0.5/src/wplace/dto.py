from __future__ import annotations
import base64
from dataclasses import dataclass
import io
from PIL import Image
import re

from .country import Country, from_id


@dataclass(order=True)
class UserInfo:
    id: int
    name: str
    alliance_id: int | None
    alliance_name: str | None
    country: Country | None = None
    discord_name: str | None = None
    picture: Image.Image | None = None

    @classmethod
    def from_dict(cls, info: dict[str, str | int]) -> UserInfo:
        alliance_id = info["allianceId"]
        if alliance_id == 0:
            alliance_id = None

        alliance_name = info["allianceName"]
        if alliance_name == "":
            alliance_name = None

        country_id = info["equippedFlag"]
        if country_id == 0:
            country = None
        else:
            country = from_id(country_id)

        pic_str = info.get("picture")
        if pic_str is None:
            picture = None
        else:
            pic_str = re.sub("^data:image/.+;base64,", "", pic_str)
            pic_data = base64.b64decode(pic_str)
            picture = Image.open(io.BytesIO(pic_data))

        return cls(
            id=info["id"],
            name=info["name"],
            alliance_id=alliance_id,
            alliance_name=alliance_name,
            country=country,
            discord_name=info.get("discord", None),
            picture=picture,
        )


@dataclass(frozen=True, order=True)
class RegionInfo:
    id: int
    city_id: int
    name: str
    number: int
    country: Country | None = None

    def __str__(self) -> str:
        return f"{self.name} #{self.number}"

    @classmethod
    def from_dict(cls, info: dict[str, str | int]) -> RegionInfo:
        country_id = info["countryId"]
        if country_id == 0:
            country = None
        else:
            country = from_id(country_id)

        return cls(
            id=info["id"],
            city_id=info["cityId"],
            name=info["name"],
            number=info["number"],
            country=country,
        )


@dataclass
class PixelInfo:
    painted_by: UserInfo | None
    region: RegionInfo

    @classmethod
    def from_dict(cls, info: dict[str, dict[str, str | int]]) -> PixelInfo:
        user = UserInfo.from_dict(info["paintedBy"])
        if user.id == 0:
            user = None

        region = RegionInfo.from_dict(info["region"])

        return cls(painted_by=user, region=region)
