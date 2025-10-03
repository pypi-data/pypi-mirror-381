from datetime import datetime

from pydantic import BaseModel, Field, AliasChoices


class TraceDefinition(BaseModel):
    scope: str = Field(alias="Scope", validation_alias=AliasChoices("scope", "scope"))
    trace_id: str = Field(
        alias="TraceId", validation_alias=AliasChoices("traceId", "trace_id")
    )
    description: str = Field(
        alias="Description", validation_alias=AliasChoices("description", "description")
    )
    created_at: datetime = Field(
        alias="CreatedAt", validation_alias=AliasChoices("createdAt", "created_at")
    )
    user_id: str = Field(
        alias="UserId", validation_alias=AliasChoices("userId", "user_id")
    )


class TraceEventDefinition(BaseModel):
    scope: str = Field(alias="Scope", validation_alias=AliasChoices("scope", "scope"))
    trace_id: str = Field(
        alias="TraceId", validation_alias=AliasChoices("traceId", "trace_id")
    )
    trace_event_id: str = Field(
        alias="TraceEventId",
        validation_alias=AliasChoices("traceEventId", "trace_event_id"),
    )
    session_id: str = Field(
        alias="SessionId", validation_alias=AliasChoices("sessionId", "session_id")
    )
    created_at: datetime = Field(
        alias="CreatedAt", validation_alias=AliasChoices("createdAt", "created_at")
    )
    user_id: str = Field(
        alias="UserId", validation_alias=AliasChoices("userId", "user_id")
    )
    event_type: str = Field(
        alias="EventType", validation_alias=AliasChoices("eventType", "event_type")
    )
    content: str = Field(
        alias="Content", validation_alias=AliasChoices("content", "content")
    )
    circuit_id: str = Field(
        alias="CircuitId", validation_alias=AliasChoices("circuitId", "circuit_id")
    )
    circuit_version: str = Field(
        alias="CircuitVersion",
        validation_alias=AliasChoices("circuitVersion", "circuit_version"),
    )
    node_id: str = Field(
        alias="NodeId", validation_alias=AliasChoices("nodeId", "node_id")
    )


class Trace:
    def __init__(
        self, *, trace_def: TraceDefinition, event_defs: list[TraceEventDefinition]
    ):
        self.trace_id = trace_def.trace_id
        self.scope = trace_def.scope
        self.sessions = set([e.session_id for e in event_defs])
        self.events = event_defs
