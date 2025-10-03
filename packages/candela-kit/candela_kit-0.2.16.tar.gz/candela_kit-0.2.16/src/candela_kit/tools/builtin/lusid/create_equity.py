from typing import Dict

from lusid.api import InstrumentsApi
from lusid.models import InstrumentDefinition, Equity, InstrumentIdValue

from candela_kit.ignite import intent as ci
from candela_kit.ignite.intent import IObj
from candela_kit.tools.base import BaseTool
from .common import id_types, ccy_code


class CreateEquity(BaseTool):
    def intent(self) -> IObj:
        return ci.obj(
            inputs=ci.arr(
                ci.obj(
                    identifiers=ci.dict(ci.str(), id_types),
                    name=ci.str(),
                    dom_ccy=ccy_code,
                    scope=ci.str().as_nullable(),
                ),
                min_length=1,
            )
        )

    def apply(self, intent: Dict) -> Dict:
        api = self.lusid_api(InstrumentsApi)

        vals = intent["inputs"]

        created = {}

        for i, val in enumerate(vals):
            label = f"equity_{i}"
            ins_def = InstrumentDefinition(
                name=val["name"],
                identifiers={
                    k: InstrumentIdValue(value=v) for k, v in val["identifiers"].items()
                },
                definition=Equity(instrument_type="Equity", dom_ccy=val["dom_ccy"]),
            )

            res = api.upsert_instruments(
                {label: ins_def}, scope=val.get("scope", "default")
            )

            if len(res.failed) == 1:
                created[label] = res.failed[label]
                self.push_wait_msg(
                    f"Instrument creation failed:\n\n{res.failed[label]}"
                )
                continue

            ins = res.values[label]

            created[label] = {
                "asset_class": ins.asset_class,
                "dom_ccy": ins.dom_ccy,
                "identifiers": ins.identifiers,
                "name": ins.name,
                "scope": ins.scope,
                "state": ins.state,
            }
            self.push_wait_msg(f"{ins.name} Created")

        return created
