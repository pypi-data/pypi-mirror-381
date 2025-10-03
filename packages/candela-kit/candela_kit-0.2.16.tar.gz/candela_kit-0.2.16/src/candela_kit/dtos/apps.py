from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, AliasChoices

from .common import ObjectId


class AppDTO(BaseModel):
    scope: str
    code: str
    version: str

    type: Literal["Agent", "Pipeline"]
    circuit: ObjectId
    directive: ObjectId

    description: str
    created_at: datetime = Field(
        alias="CreatedAt", validation_alias=AliasChoices("createdAt", "created_at")
    )
    created_by: str = Field(
        alias="CreatedBy", validation_alias=AliasChoices("createdBy", "created_by")
    )


class CreateAppRequestDTO(BaseModel):
    code: str
    description: str
    version_bump: Literal["Major", "Minor", "Patch"] = Field(
        alias="VersionBump",
        validation_alias=AliasChoices("versionBump", "version_bump"),
    )

    type: Literal["Agent", "Pipeline"]
    circuit: ObjectId
    directive: ObjectId
