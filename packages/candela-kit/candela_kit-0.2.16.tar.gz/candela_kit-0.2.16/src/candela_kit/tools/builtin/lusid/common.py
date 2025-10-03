import datetime as dt
from typing import Dict

import pytz
from lusid.models import ResourceId

from candela_kit.ignite.intent import intent as ci

id_types = [
    "ClientInternal",
    "EdiKey",
    "Figi",
    "QuotePermId",
    "CompositeFigi",
    "Cusip",
    "Isin",
    "RIC",
    "Sedol",
    "ShareClassFigi",
    "Ticker",
    "Wertpapier",
]


def to_datetime(x: str | None) -> dt.datetime | None:
    if x is None:
        return None

    return dt.datetime.fromisoformat(x).astimezone(pytz.utc)


def to_resource_id(x: Dict | None) -> ResourceId | None:
    if x is None:
        return None
    return ResourceId(**x)


resource_id = ci.obj(scope=ci.str(), code=ci.str())

ccy_code = ci.str(regex="^[A-Z]{3}$")
