from time import sleep
from typing import Optional, Literal, Iterator, Callable

from pandas import DataFrame

from candela_kit import CandelaApiError
from candela_kit._api.api_client import CandelaApiClient
from candela_kit._api.websocket_client import sync_stream_prompt
from candela_kit.event import Event
from candela_kit.dtos import (
    CreateAppRequestDTO,
    AddSessionRequest,
    CreateModelRequest,
    AddToolModuleRequest,
    ToolModule,
    AppDTO,
)
from candela_kit.dtos import CreateCircuitRequest, CircuitDTO, CircuitDefinition
from candela_kit.dtos import CreateDirectiveRequest, DirectiveDefinition
from candela_kit.dtos import ObjectMetadata
from candela_kit.dtos.sessions import Session
from candela_kit.dtos.traces import Trace
from candela_kit.dtos.translator import CircuitToDTO
from candela_kit.app import App
from candela_kit.directive import Directive
from candela_kit.ignite.circuits import Circuit

from candela_kit.profiles import get_profiles, UserProfile


def _exists_check(get_fn: Callable, code, scope, version):
    try:
        get_fn(code, scope, version)
        return True
    except CandelaApiError as ce:
        if ce.status_code == 404:
            return False
        raise


def _df_postprocess(df: DataFrame, all_versions: bool):
    if not all_versions:
        return (
            df.sort_values("version", ascending=False)
            .groupby(["code", "scope"], as_index=False)
            .first()
        )
    return df


def map_tool_module(module: ToolModule | None) -> ToolModule | None:
    if module is None:
        return None

    map_dict = [
        (
            "from candela_kit.ignite import intent",
            "from candela.ignite.intent import intent",
        ),
        (
            "from candela_kit.ignite.intent import",
            "from candela.ignite.intent import",
        ),
        ("candela_kit.ignite", "candela.ignite"),
        ("candela_kit.tools", "candela.tools"),
        ("candela_kit as", "candela as"),
        ("IObj", "DTOObj"),
    ]

    content = module.content
    for s1, s2 in map_dict:
        content = content.replace(s1, s2)

    return ToolModule(content=content)


class Client:
    @staticmethod
    def build(access_token: str, domain: str) -> "Client":
        api_client = CandelaApiClient.build(access_token, domain)
        return Client(api_client)

    @staticmethod
    def localhost(access_token: str, port: int = 8282) -> "Client":
        api_client = CandelaApiClient.localhost(access_token, port)
        return Client(api_client)

    def __init__(self, api_client: CandelaApiClient):
        self.api_client = api_client
        self.circuit_to_dto = CircuitToDTO()

    def __repr__(self):
        name = type(self).__name__
        n = 10
        censored_token = (
            f"{self.api_client.token[:3]}{n * '-'}{self.api_client.token[-5:]}"
        )
        return f"{name}(\n    token: {censored_token},\n    api_url: {self.api_client.base_url}\n)"

    @property
    def access_token(self) -> str:
        return self.api_client.token

    @property
    def api_url(self) -> str:
        return self.api_client.base_url

    def assign_slot(self, slot_type: str):
        try:
            self.get_slot_state()
        except CandelaApiError as ce:
            if ce.status_code == 404:
                self.api_client.put_slot(slot_type=slot_type)
                sleep(2)
            elif ce.status_code == 400 and ce.details["code"] == 149:
                print("User already assigned a slot.")
                return
            else:
                raise ce from None

    def delete_slot(self):
        return self.api_client.delete_slot()

    def get_slot_state(self):
        return self.api_client.get_slot_state()

    def has_slot(self):
        try:
            self.get_slot_state()
            return True
        except CandelaApiError as ce:
            if ce.status_code == 404:
                return False
            raise ce from None

    def list_apps(self, all_versions: Optional[bool] = False) -> DataFrame:
        def row_map(app):
            return {
                "scope": app.scope,
                "code": app.code,
                "version": app.version,
                "type": app.type,
                "circuit_scope": app.circuit.scope,
                "circuit_code": app.circuit.code,
                "circuit_version": app.circuit.version,
                "directive_scope": app.directive.scope,
                "directive_code": app.directive.code,
                "directive_version": app.directive.version,
                "description": app.description,
                "created_at": app.created_at,
                "created_by": app.created_by,
            }

        df = DataFrame((row_map(a) for a in self.api_client.get_apps()))
        return _df_postprocess(df, all_versions)

    def get_app(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ) -> App:
        app_dto = self.api_client.get_app(code=code, scope=scope, version=version)
        return App(
            app_dto.type,
            app_dto.circuit,
            app_dto.directive,
        )

    def app_exists(
        self, code: str, scope: str = "default", version: Optional[str] = None
    ) -> bool:
        return _exists_check(self.get_app, code, scope, version)

    def get_app_metadata(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ):
        app_dto = self.api_client.get_app(code=code, scope=scope, version=version)
        return ObjectMetadata(
            code=app_dto.code,
            scope=app_dto.scope,
            version=app_dto.version,
            description=app_dto.description,
            created_at=app_dto.created_at,
            created_by=app_dto.created_by,
        )

    def delete_app(self, code: str, scope: str, version: Optional[str] = None):
        return self.api_client.delete_app(code=code, scope=scope, version=version)

    def add_app(
        self,
        app: App,
        code,
        scope: Optional[str] = "default",
        version_bump: Literal["Major", "Minor", "Patch"] = "Patch",
        description: Optional[str] = "No description",
    ) -> AppDTO:
        req = CreateAppRequestDTO(
            code=code,
            description=description,
            version_bump=version_bump,
            type=app.type,
            circuit=app.circuit_id,
            directive=app.directive_id,
        )
        res = self.api_client.put_app(scope=scope, request=req)
        return res

    def start_session(
        self,
        app_code: str,
        app_scope: str,
        model_code: str,
        model_scope: str,
        app_version: Optional[str] = None,
        model_version: Optional[str] = None,
        parent_session_id: Optional[str] = None,
        description: Optional[str] = "No description",
        version_bump: Literal["Major", "Minor", "Patch"] = "Major",
        session_scope: Optional[str] = "default",
    ):
        req = AddSessionRequest(
            description=description,
            version_bump=version_bump,
            parent_session_id=parent_session_id,
            app_code=app_code,
            app_scope=app_scope,
            app_version=app_version,
            model_code=model_code,
            model_scope=model_scope,
            model_version=model_version,
        )
        return self.api_client.put_session(scope=session_scope, request=req)

    def stop_session(self):
        return self.api_client.stop_session()

    def delete_session(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ):
        return self.api_client.delete_session(code=code, scope=scope, version=version)

    def list_sessions(self) -> DataFrame:
        def row_map(s):
            return {
                "scope": s.scope,
                "code": s.code,
                "created_at": s.created_at,
                "created_by": s.created_by,
                "description": s.description,
                "parent_session_id": s.parent_session_id,
                "app_code": s.app_code,
                "app_scope": s.app_scope,
                "app_version": s.app_version,
                "model_code": s.model_code,
                "model_scope": s.model_scope,
                "model_version": s.model_version,
            }

        return DataFrame((row_map(val) for val in self.api_client.get_sessions()))

    def get_session(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ) -> Session:
        session_dto = self.api_client.get_session(
            code=code, scope=scope, version=version
        )
        return session_dto

    def session_exists(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ) -> bool:
        return _exists_check(self.get_session, code, scope, version)

    def get_session_metadata(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ) -> ObjectMetadata:
        session_dto = self.api_client.get_session(
            code=code, scope=scope, version=version
        )
        return ObjectMetadata(
            code=session_dto.code,
            scope=session_dto.scope,
            version=session_dto.version,
            description=session_dto.description,
            created_at=session_dto.created_at,
            created_by=session_dto.created_by,
        )

    def submit_prompt_to_agent(self, prompt, session: Session) -> Iterator[Event]:
        stream = sync_stream_prompt(
            self.api_client.token, self.api_client.domain, prompt, session
        )
        return stream

    def list_circuits(self, all_versions: bool = False) -> DataFrame:
        def row_map(c):
            return {
                "scope": c.scope,
                "code": c.code,
                "version": c.version,
                "description": c.description,
            }

        df = DataFrame((row_map(val) for val in self.api_client.get_circuits()))
        return _df_postprocess(df, all_versions)

    def get_circuit(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ) -> CircuitDTO:
        circ_dto = self.api_client.get_circuit(code=code, scope=scope, version=version)
        return CircuitDTO(
            first=circ_dto.first,
            nodes=circ_dto.nodes,
        )

    def circuit_exists(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ) -> bool:
        return _exists_check(self.get_circuit, code, scope, version)

    def get_circuit_metadata(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ):
        circ_def = self.api_client.get_circuit(code=code, scope=scope, version=version)
        return ObjectMetadata(
            code=circ_def.code,
            scope=circ_def.scope,
            version=circ_def.version,
            description=circ_def.description,
            created_at=None,
            created_by=None,
        )

    def delete_circuit(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ):
        return self.api_client.delete_circuit(code=code, scope=scope, version=version)

    def add_circuit(
        self,
        circuit: Circuit,
        code: str,
        scope: Optional[str] = "default",
        description: Optional[str] = "No description",
        version_bump: Literal["Major", "Minor", "Patch"] = "Patch",
    ) -> CircuitDefinition:
        circuit_dto = self.circuit_to_dto.translate(circuit)
        request = CreateCircuitRequest(
            code=code,
            version_bump=version_bump,
            description=description,
            first=circuit_dto.first,
            nodes=circuit_dto.nodes,
        )
        return self.api_client.put_circuit(scope=scope, request=request)

    def list_directives(self, all_versions: Optional[bool] = False) -> DataFrame:
        def row_map(c):
            return {
                "scope": c.scope,
                "code": c.code,
                "version": c.version,
                "description": c.description,
                "created_at": c.created_at,
                "created_by": c.created_by,
            }

        df = DataFrame((row_map(val) for val in self.api_client.get_directives()))
        return _df_postprocess(df, all_versions)

    def get_directive(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ) -> Directive:
        directive_def = self.api_client.get_directive(
            code=code, scope=scope, version=version
        )
        return Directive(
            identity=directive_def.identity,
            purpose=directive_def.purpose,
            style=directive_def.style,
            restriction=directive_def.restriction,
            context_vals=directive_def.context_vals,
        )

    def directive_exists(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ) -> bool:
        return _exists_check(self.get_directive, code, scope, version)

    def get_directive_metadata(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ) -> ObjectMetadata:
        directive_def = self.api_client.get_directive(
            code=code, scope=scope, version=version
        )
        return ObjectMetadata(
            code=directive_def.code,
            scope=directive_def.scope,
            version=directive_def.version,
            description=directive_def.description,
            created_at=directive_def.created_at,
            created_by=directive_def.created_by,
        )

    def delete_directive(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ) -> str:
        return self.api_client.delete_directive(code=code, scope=scope, version=version)

    def add_directive(
        self,
        directive: Directive,
        code: str,
        scope: Optional[str] = "default",
        description: Optional[str] = "No Description",
        version_bump: Literal["Major", "Minor", "Patch"] = "Patch",
    ) -> DirectiveDefinition:
        request = CreateDirectiveRequest(
            code=code,
            version_bump=version_bump,
            description=description,
            identity=directive.identity,
            purpose=directive.purpose,
            style=directive.style,
            restriction=directive.restriction,
        )
        return self.api_client.put_directive(scope=scope, request=request)

    def list_models(self, all_versions: Optional[bool] = False) -> DataFrame:
        def row_map(m):
            return {
                "scope": m.model_id.scope,
                "code": m.model_id.code,
                "version": m.version,
                "model_type": m.model_type,
                "created_at": m.created_at,
                "created_by": m.created_by,
                "description": m.description,
                "model_path": m.custom_model_path,
            }

        df = DataFrame((row_map(val) for val in self.api_client.get_models()))
        return _df_postprocess(df, all_versions)

    def get_model(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ):
        model = self.api_client.get_model(code=code, scope=scope, version=version)
        return model

    def model_exists(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ) -> bool:
        return _exists_check(self.get_model, code, scope, version)

    def get_model_metadata(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ):
        model = self.api_client.get_model(code=code, scope=scope, version=version)
        return ObjectMetadata(
            code=model.model_id.code,
            scope=model.model_id.scope,
            version=model.version,
            description=model.description,
            created_at=model.created_at,
            created_by=model.created_by,
        )

    def delete_model(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ):
        return self.api_client.delete_model(code=code, scope=scope, version=version)

    def add_model(
        self,
        model_type: str,
        code: str,
        scope: Optional[str] = "default",
        custom_model_path: Optional[str] = None,
        version_bump: Literal["Major", "Minor", "Patch"] = "Patch",
        description: Optional[str] = "No description",
    ):
        req = CreateModelRequest(
            code=code,
            version_bump=version_bump,
            model_type=model_type,
            custom_model_path=custom_model_path,
            description=description,
        )
        return self.api_client.put_model(scope=scope, request=req)

    def list_tool_modules(self, all_versions: Optional[bool] = False) -> DataFrame:
        def row_map(m):
            return {
                "scope": m.tool_module_id.scope,
                "code": m.tool_module_id.code,
                "version": m.version,
                "description": m.description,
                "created_at": m.created_at,
                "created_by": m.created_by,
            }

        df = DataFrame((row_map(val) for val in self.api_client.get_tool_modules()))
        return _df_postprocess(df, all_versions)

    def get_tool_module(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ) -> ToolModule:
        tool_module = self.api_client.get_tool_module(
            code=code, scope=scope, version=version
        )
        return ToolModule(content=tool_module.content)

    def tool_module_exists(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ) -> bool:
        return _exists_check(self.get_tool_module, code, scope, version)

    def get_tool_module_metadata(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ) -> ObjectMetadata:
        tool_module = self.api_client.get_tool_module(
            code=code, scope=scope, version=version
        )
        return ObjectMetadata(
            code=tool_module.tool_module_id.code,
            scope=tool_module.tool_module_id.scope,
            version=tool_module.version,
            description=tool_module.description,
            created_at=tool_module.created_at,
            created_by=tool_module.created_by,
        )

    def delete_tool_module(
        self, code: str, scope: Optional[str] = "default", version: Optional[str] = None
    ):
        return self.api_client.delete_tool_module(
            code=code, scope=scope, version=version
        )

    def add_tool_module(
        self,
        module: ToolModule,
        code: str,
        scope: Optional[str] = "default",
        version_bump: Literal["Major", "Minor", "Patch"] = "Patch",
        description: Optional[str] = "No description",
    ):
        module = map_tool_module(module)
        req = AddToolModuleRequest(
            code=code,
            content=module.content,
            version_bump=version_bump,
            description=description,
        )
        return self.api_client.put_tool_module(scope=scope, request=req)

    def list_tools_in_module(self, code: str, scope: Optional[str] = "default"):
        return self.api_client.get_tool_module_tools(code=code, scope=scope)

    def list_traces(self):
        def row_map(c):
            return {
                "scope": c.scope,
                "trace_id": c.trace_id,
                "description": c.description,
                "created_at": c.created_at,
                "user_id": c.user_id,
            }

        return DataFrame((row_map(val) for val in self.api_client.get_traces()))

    def get_trace(self, trace_id: str, scope: Optional[str] = "default") -> Trace:
        trace = self.api_client.get_trace(trace_id=trace_id, scope=scope)
        events = self.api_client.get_trace_events(trace_id=trace_id, scope=scope)
        return Trace(trace_def=trace, event_defs=events)

    def trace_exists(
        self,
        trace_id: str,
        scope: Optional[str] = "default",
        version: Optional[str] = None,
    ) -> bool:
        return _exists_check(self.get_trace, trace_id, scope, version)

    def get_trace_metadata(
        self,
        trace_id: str,
        scope: Optional[str] = "default",
        version: Optional[str] = None,
    ):
        trace = self.api_client.get_trace(trace_id=trace_id, scope=scope)
        return ObjectMetadata(
            code=trace.code,
            scope=trace.scope,
            version="0.0.1",
            description=trace.description,
            created_at=trace.created_at,
            created_by=trace.user_id,
        )

    def delete_trace(self, trace_id: str, scope: Optional[str] = "default"):
        return self.api_client.delete_trace(trace_id=trace_id, scope=scope)

    @classmethod
    def from_profile(cls, profile: UserProfile) -> "Client":
        token = profile.access_token.get_secret_value()
        #        if "localhost.lusid.com" in profile.api_url:
        #            return Client.localhost(token)

        return Client.build(token, profile.domain)


def client(profile_name: str = None) -> Client:
    profile = get_profiles().get(profile_name)
    return Client.from_profile(profile)
