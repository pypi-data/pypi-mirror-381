from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, Field, AliasChoices, ConfigDict


class Session(BaseModel):
    model_config = ConfigDict(protected_namespaces=())

    scope: str
    code: str
    version: str
    description: str
    parent_session_id: Optional[str] = Field(
        default=None,
        alias="ParentSessionId",
        validation_alias=AliasChoices("parentSessionId", "parent_session_id"),
    )

    app_scope: str = Field(
        alias="AppScope", validation_alias=AliasChoices("appScope", "app_scope")
    )
    app_code: str = Field(
        alias="AppCode", validation_alias=AliasChoices("appCode", "app_code")
    )
    app_version: str = Field(
        alias="AppVersion", validation_alias=AliasChoices("appVersion", "app_version")
    )

    model_scope: str = Field(
        alias="ModelScope", validation_alias=AliasChoices("modelScope", "model_scope")
    )
    model_code: str = Field(
        alias="ModelCode", validation_alias=AliasChoices("modelCode", "model_code")
    )
    model_version: str = Field(
        alias="ModelVersion",
        validation_alias=AliasChoices("modelVersion", "model_version"),
    )

    created_at: datetime = Field(
        alias="CreatedAt", validation_alias=AliasChoices("createdAt", "created_at")
    )
    created_by: str = Field(
        alias="CreatedBy", validation_alias=AliasChoices("createdBy", "created_by")
    )


class AddSessionRequest(BaseModel):
    model_config = ConfigDict(protected_namespaces=())

    description: Optional[str] = None
    version_bump: Literal["Major", "Minor", "Patch"] = Field(
        alias="VersionBump",
        validation_alias=AliasChoices("versionBump", "version_bump"),
    )
    parent_session_id: Optional[str] = Field(
        default=None,
        alias="ParentSessionId",
        validation_alias=AliasChoices("parentSessionId", "parent_session_id"),
    )

    app_scope: str = Field(
        alias="AppScope", validation_alias=AliasChoices("appScope", "app_scope")
    )
    app_code: str = Field(
        alias="AppCode", validation_alias=AliasChoices("appCode", "app_code")
    )
    app_version: Optional[str] = Field(
        default=None,
        alias="AppVersion",
        validation_alias=AliasChoices("appVersion", "app_version"),
    )

    model_scope: str = Field(
        alias="ModelScope", validation_alias=AliasChoices("modelScope", "model_scope")
    )
    model_code: str = Field(
        alias="ModelCode", validation_alias=AliasChoices("modelCode", "model_code")
    )
    model_version: Optional[str] = Field(
        default=None,
        alias="ModelVersion",
        validation_alias=AliasChoices("modelVersion", "model_version"),
    )
