from datetime import datetime
from typing import Optional, Literal

from pydantic import BaseModel, Field, AliasChoices, ConfigDict

from .common import ObjectId


class Model(BaseModel):
    model_config = ConfigDict(protected_namespaces=())

    model_id: ObjectId = Field(
        alias="ModelId", validation_alias=AliasChoices("modelId", "model_id")
    )
    model_type: str = Field(
        alias="ModelType", validation_alias=AliasChoices("modelType", "model_type")
    )
    custom_model_path: Optional[str] = Field(
        default=None,
        alias="CustomModelPath",
        validation_alias=AliasChoices("customModelPath", "custom_model_path"),
    )
    description: str
    version: str
    created_at: datetime = Field(
        alias="CreatedAt", validation_alias=AliasChoices("createdAt", "created_at")
    )
    created_by: str = Field(
        alias="CreatedBy", validation_alias=AliasChoices("createdBy", "created_by")
    )
    updated_at: datetime = Field(
        alias="UpdatedAt", validation_alias=AliasChoices("updatedAt", "updated_at")
    )


class CreateModelRequest(BaseModel):
    model_config = ConfigDict(protected_namespaces=())

    code: str
    model_type: str = Field(
        alias="ModelType", validation_alias=AliasChoices("modelType", "model_type")
    )
    custom_model_path: Optional[str] = Field(
        default=None,
        alias="CustomModelPath",
        validation_alias=AliasChoices("customModelPath", "custom_model_path"),
    )
    description: str
    version_bump: Literal["Major", "Minor", "Patch"] = Field(
        alias="VersionBump",
        validation_alias=AliasChoices("versionBump", "version_bump"),
    )
