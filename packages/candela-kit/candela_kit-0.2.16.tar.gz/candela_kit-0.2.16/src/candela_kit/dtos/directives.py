from datetime import datetime
from typing import List, Literal, Optional, Dict

from pydantic import BaseModel, StrictBool, Field, AliasChoices


class DirectiveDefinition(BaseModel):
    scope: str
    code: str
    version: str
    description: str

    point: Literal[" * "] = " * "
    hide: StrictBool = True
    identity: Optional[List[str]] = None
    purpose: Optional[List[str]] = None
    style: Optional[List[str]] = None
    restriction: Optional[List[str]] = None
    context_vals: Dict[str, str] = Field(
        default_factory=dict,
        alias="ContextVals",
        validation_alias=AliasChoices("contextVals", "context_vals"),
    )

    created_at: datetime = Field(
        alias="CreatedAt", validation_alias=AliasChoices("createdAt", "created_at")
    )
    created_by: str = Field(
        alias="CreatedBy", validation_alias=AliasChoices("createdBy", "created_by")
    )


class CreateDirectiveRequest(BaseModel):
    code: str
    version_bump: Literal["Major", "Minor", "Patch"] = Field(
        alias="VersionBump",
        validation_alias=AliasChoices("versionBump", "version_bump"),
    )
    description: str

    point: Literal[" * "] = " * "
    hide: StrictBool = True
    identity: Optional[List[str]] = None
    purpose: Optional[List[str]] = None
    style: Optional[List[str]] = None
    restriction: Optional[List[str]] = None
    context_vals: Dict[str, str] = Field(
        default_factory=dict,
        alias="ContextVals",
        validation_alias=AliasChoices("contextVals", "context_vals"),
    )
