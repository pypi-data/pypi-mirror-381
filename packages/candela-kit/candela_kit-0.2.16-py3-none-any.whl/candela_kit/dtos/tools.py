from datetime import datetime
from typing import Literal

import black
from pygments import highlight
from pygments.formatters import Terminal256Formatter
from pygments.lexers import PythonLexer
from pydantic import BaseModel, Field, AliasChoices

from candela_kit.dtos.common import ObjectId


class ToolModule(BaseModel):
    content: str

    def __repr__(self) -> str:
        exp_str = black.format_str(self.content, mode=black.FileMode())
        exp_str = highlight(exp_str, PythonLexer(), Terminal256Formatter())
        return exp_str


class ToolModuleDefinition(BaseModel):
    tool_module_id: ObjectId = Field(
        alias="ToolModuleId",
        validation_alias=AliasChoices("toolModuleId", "tool_module_id"),
    )
    content: str = Field(
        alias="Content", validation_alias=AliasChoices("content", "content")
    )
    version: str = Field(
        alias="Version", validation_alias=AliasChoices("version", "version")
    )
    description: str = Field(
        alias="Description", validation_alias=AliasChoices("description", "description")
    )
    created_at: datetime = Field(
        alias="CreatedAt", validation_alias=AliasChoices("createdAt", "created_at")
    )
    created_by: str = Field(
        alias="CreatedBy", validation_alias=AliasChoices("createdBy", "created_by")
    )


class ToolDefinition(BaseModel):
    tool_code: str = Field(
        alias="ToolCode", validation_alias=AliasChoices("toolCode", "tool_code")
    )
    module_code: str = Field(
        alias="ModuleCode", validation_alias=AliasChoices("moduleCode", "module_code")
    )
    module_version: str = Field(
        alias="ModuleVersion",
        validation_alias=AliasChoices("moduleVersion", "module_version"),
    )


class AddToolModuleRequest(BaseModel):
    code: str = Field(alias="Code", validation_alias=AliasChoices("code", "code"))
    description: str = Field(
        alias="Description", validation_alias=AliasChoices("description", "description")
    )
    version_bump: Literal["Major", "Minor", "Patch"] = Field(
        alias="VersionBump",
        validation_alias=AliasChoices("versionBump", "version_bump"),
    )
    content: str = Field(
        alias="Content", validation_alias=AliasChoices("content", "content")
    )
