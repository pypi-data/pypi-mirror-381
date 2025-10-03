import requests as r
from pydantic import BaseModel
from requests import Response

from candela_kit.dtos import AppDTO, CreateAppRequestDTO
from candela_kit.dtos import CircuitDefinition, CreateCircuitRequest
from candela_kit.dtos import DirectiveDefinition, CreateDirectiveRequest
from candela_kit.dtos import Model, CreateModelRequest
from candela_kit.dtos import Session, AddSessionRequest
from candela_kit.dtos import AddToolModuleRequest, ToolModuleDefinition, ToolDefinition
from candela_kit.dtos import TraceDefinition, TraceEventDefinition
from candela_kit.exceptions import CandelaApiError


def json_body(x: BaseModel) -> dict:
    return x.model_dump(by_alias=True)


class CandelaApiClient:
    @staticmethod
    def build(token: str, domain: str) -> "CandelaApiClient":
        url = f"https://{domain}.lusid.com/candela/api"
        return CandelaApiClient(token, url, domain)

    @staticmethod
    def localhost(token: str, port: int = 8282) -> "CandelaApiClient":
        url = f"http://localhost.lusid.com:{port}/api"
        return CandelaApiClient(token, url, domain=None)

    def __init__(self, token, base_url, domain):
        self.token = token
        self.domain = domain
        self.base_url = base_url.rstrip("/")

    @staticmethod
    def raise_for_status(response: Response):
        if isinstance(response, Response):
            if not response.ok:
                raise CandelaApiError.from_requests_response(response)
        else:
            raise TypeError(
                f"Unexpected response type in raise_for_status: {type(response).__name__}"
            )

    def _make_url(self, *parts) -> str:
        return f"{self.base_url}/{'/'.join(parts)}"

    def _headers(self) -> dict:
        return {"Authorization": f"Bearer {self.token}"}

    # region apps
    def get_apps(self) -> list[AppDTO]:
        url = self._make_url("apps")
        res = r.get(url, headers=self._headers())
        self.raise_for_status(res)
        values = [AppDTO.model_validate(v) for v in res.json()["values"]]
        return values

    def get_app(self, *, code: str, scope: str, version: str) -> AppDTO:
        url = self._make_url("apps", scope, code)
        params = {"version": version} if version else {}
        res = r.get(url, params=params, headers=self._headers())
        self.raise_for_status(res)
        return AppDTO.model_validate(res.json())

    def put_app(self, *, scope: str, request: CreateAppRequestDTO) -> AppDTO:
        url = self._make_url("apps", scope)
        res = r.put(url, json=json_body(request), headers=self._headers())
        self.raise_for_status(res)
        return AppDTO.model_validate(res.json())

    def delete_app(self, *, scope: str, code: str, version: str) -> str:
        url = self._make_url("apps", scope, code)
        params = {"version": version} if version else {}
        res = r.delete(url, params=params, headers=self._headers())
        self.raise_for_status(res)
        return res.json()

    # endregion

    # region circuits
    def get_circuits(self) -> list[CircuitDefinition]:
        url = self._make_url("circuits")
        res = r.get(url, headers=self._headers())
        self.raise_for_status(res)
        values = res.json()["values"]
        values = [CircuitDefinition.model_validate(v) for v in values]
        return values

    def get_circuit(
        self, *, code: str, scope: str, version: str = None
    ) -> CircuitDefinition:
        url = self._make_url("circuits", scope, code)
        params = {"version": version} if version else {}
        res = r.get(url, params=params, headers=self._headers())
        self.raise_for_status(res)
        return CircuitDefinition.model_validate(res.json())

    def put_circuit(
        self, *, scope: str, request: CreateCircuitRequest
    ) -> CircuitDefinition:
        url = self._make_url("circuits", scope)
        res = r.put(url, json=json_body(request), headers=self._headers())
        self.raise_for_status(res)
        return CircuitDefinition.model_validate(res.json())

    def delete_circuit(self, *, scope: str, code: str, version: str) -> str:
        url = self._make_url("circuits", scope, code)
        params = {"version": version} if version else {}
        res = r.delete(url, params=params, headers=self._headers())
        self.raise_for_status(res)
        return res.json()

    # endregion

    # region directives
    def get_directives(self) -> list[DirectiveDefinition]:
        url = self._make_url("directives")
        res = r.get(url, headers=self._headers())
        self.raise_for_status(res)
        values = res.json()["values"]
        values = [DirectiveDefinition.model_validate(v) for v in values]
        return values

    def get_directive(
        self, *, code: str, scope: str, version: str = None
    ) -> DirectiveDefinition:
        url = self._make_url("directives", scope, code)
        params = {"version": version} if version else {}
        res = r.get(url, params=params, headers=self._headers())
        self.raise_for_status(res)
        return DirectiveDefinition.model_validate(res.json())

    def put_directive(
        self, *, scope: str, request: CreateDirectiveRequest
    ) -> DirectiveDefinition:
        url = self._make_url("directives", scope)
        res = r.put(url, json=json_body(request), headers=self._headers())
        self.raise_for_status(res)
        return DirectiveDefinition.model_validate(res.json())

    def delete_directive(self, *, scope: str, code: str, version: str):
        url = self._make_url("directives", scope, code)
        params = {"version": version} if version else {}
        res = r.delete(url, params=params, headers=self._headers())
        self.raise_for_status(res)
        return res.json()

    # endregion

    # region models
    def get_models(self) -> list[Model]:
        url = self._make_url("models")
        res = r.get(url, headers=self._headers())
        self.raise_for_status(res)
        values = [Model.model_validate(v) for v in res.json()["values"]]
        return values

    def get_model(self, *, code: str, scope: str, version) -> Model:
        url = self._make_url("models", scope, code)
        params = {"version": version} if version else {}
        res = r.get(url, params=params, headers=self._headers())
        self.raise_for_status(res)
        return Model.model_validate(res.json())

    def put_model(self, *, scope: str, request: CreateModelRequest) -> Model:
        url = self._make_url("models", scope)
        res = r.put(url, json=json_body(request), headers=self._headers())
        self.raise_for_status(res)
        return Model.model_validate(res.json())

    def delete_model(self, *, scope: str, code: str, version: str) -> str:
        url = self._make_url("models", scope, code)
        params = {"version": version} if version else {}
        res = r.delete(url, params=params, headers=self._headers())
        self.raise_for_status(res)
        return res.json()

    # endregion models

    # region sessions
    def get_sessions(self) -> list[Session]:
        url = self._make_url("sessions")
        res = r.get(url, headers=self._headers())
        self.raise_for_status(res)
        values = [Session.model_validate(v) for v in res.json()["values"]]
        return values

    def get_session(self, *, code: str, scope: str, version: str) -> Session:
        url = self._make_url("sessions", scope, code)
        params = {"version": version} if version else {}
        res = r.get(url, params=params, headers=self._headers())
        self.raise_for_status(res)
        return Session.model_validate(res.json())

    def put_session(self, *, scope: str, request: AddSessionRequest) -> Session:
        url = self._make_url("sessions", scope)
        res = r.put(url, json=json_body(request), headers=self._headers())
        self.raise_for_status(res)
        return Session.model_validate(res.json())

    def delete_session(self, *, scope: str, code: str, version: str) -> str:
        url = self._make_url("sessions", scope, code)
        params = {"version": version} if version else {}
        res = r.delete(url, params=params, headers=self._headers())
        self.raise_for_status(res)
        return res.json()

    def stop_session(self) -> str:
        url = self._make_url("sessions", "stop")
        res = r.put(url, headers=self._headers())
        self.raise_for_status(res)
        return res.json()

    # endregion sessions

    # region slots
    def put_slot(self, *, slot_type: str):
        url = self._make_url("slots")
        params = {"slotType": slot_type}
        res = r.put(url, params=params, headers=self._headers())
        self.raise_for_status(res)
        return res.json()

    def delete_slot(self):
        url = self._make_url("slots")
        res = r.delete(url, headers=self._headers())
        self.raise_for_status(res)
        return res.json()

    def get_slot_state(self):
        url = self._make_url("slots", "state")
        res = r.get(url, headers=self._headers())
        self.raise_for_status(res)
        return res.json()

    # endregion slots

    # region tool_modules
    def get_tool_modules(self) -> list[ToolModuleDefinition]:
        url = self._make_url("tool-modules")
        res = r.get(url, headers=self._headers())
        self.raise_for_status(res)
        vals = res.json()["values"]
        values = [ToolModuleDefinition.model_validate(v) for v in vals]
        return values

    def get_tool_module(
        self, *, code: str, scope: str, version: str
    ) -> ToolModuleDefinition:
        url = self._make_url("tool-modules", scope, code)
        params = {"version": version} if version else {}
        res = r.get(url, params=params, headers=self._headers())
        self.raise_for_status(res)
        return ToolModuleDefinition.model_validate(res.json())

    def put_tool_module(
        self, *, scope: str, request: AddToolModuleRequest
    ) -> ToolModuleDefinition:
        url = self._make_url("tool-modules", scope)
        res = r.put(url, json=json_body(request), headers=self._headers())
        self.raise_for_status(res)
        return ToolModuleDefinition.model_validate(res.json())

    def delete_tool_module(self, *, scope: str, code: str, version: str) -> str:
        url = self._make_url("tool-modules", scope, code)
        params = {"version": version} if version else {}
        res = r.delete(url, params=params, headers=self._headers())
        self.raise_for_status(res)
        return res.json()

    def get_tool_module_tools(self, *, code: str, scope: str) -> list[ToolDefinition]:
        url = self._make_url("tool-modules", scope, code, "tools")
        res = r.get(url, headers=self._headers())
        self.raise_for_status(res)
        values = [ToolDefinition.model_validate(v) for v in res.json()["values"]]
        return values

    def get_tool_module_tool(
        self, *, code: str, scope: str, tool_code: str
    ) -> ToolDefinition:
        url = self._make_url("tool-modules", scope, code, "tools", tool_code)
        res = r.get(url, headers=self._headers())
        self.raise_for_status(res)
        return ToolDefinition.model_validate(res.json())

    # endregion

    # region traces
    def get_traces(self) -> list[TraceDefinition]:
        url = self._make_url("traces")
        res = r.get(url, headers=self._headers())
        res.raise_for_status()
        values = [TraceDefinition.model_validate(v) for v in res.json()["values"]]
        return values

    def get_trace(self, *, scope: str, trace_id: str):
        url = self._make_url("traces", scope, trace_id)
        res = r.get(url, headers=self._headers())
        res.raise_for_status()
        return Session.model_validate(res.json())

    def get_trace_events(self, *, scope: str, trace_id: str):
        url = self._make_url("traces", "events", scope, trace_id)
        res = r.get(url, headers=self._headers())
        res.raise_for_status()
        values = [TraceEventDefinition.model_validate(v) for v in res.json()["values"]]
        return values

    def delete_trace(self, *, scope: str, trace_id: str):
        url = self._make_url("traces", scope, trace_id)
        res = r.delete(url, headers=self._headers())
        res.raise_for_status()
        return res.json()

    # endregion traces
