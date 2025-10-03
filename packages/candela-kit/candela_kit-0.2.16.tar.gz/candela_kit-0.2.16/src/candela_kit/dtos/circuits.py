from typing import Annotated, Dict, List, Literal, Optional, Union
from candela_kit.tools import BaseTool

from pydantic import BaseModel, Field, AliasChoices


class DTOStr(BaseModel):
    type: Literal["string"] = "string"
    model_config = {"json_schema_extra": {"discriminator": {"propertyName": "type"}}}

    is_nullable: Optional[bool] = Field(
        default=False,
        alias="isNullable",
        validation_alias=AliasChoices("isNullable", "is_nullable"),
    )

    min_length: Optional[int] = Field(
        default=None,
        alias="minLength",
        validation_alias=AliasChoices("minLength", "min_length"),
    )
    max_length: Optional[int] = Field(
        default=None,
        alias="maxLength",
        validation_alias=AliasChoices("maxLength", "max_length"),
    )
    regex: Optional[str] = None
    format: Optional[str] = None
    description: Optional[str] = None
    default_value: Optional[str] = Field(
        default=None,
        alias="defaultValue",
        validation_alias=AliasChoices("defaultValue", "default_value"),
    )

    # todo: deprecate once bedrock hosts are deployed
    stop: Union[str, List[str], None] = None
    max_tokens: Optional[int] = Field(
        default=1000,
        alias="maxTokens",
        validation_alias=AliasChoices("maxTokens", "max_tokens"),
    )


class DTOEnum(BaseModel):
    type: Literal["enum"] = "enum"
    model_config = {"json_schema_extra": {"discriminator": {"propertyName": "type"}}}

    options: List[str]
    is_nullable: Optional[bool] = Field(
        default=False,
        alias="isNullable",
        validation_alias=AliasChoices("isNullable", "is_nullable"),
    )
    description: Optional[str] = None
    default_value: Optional[str] = Field(
        default=None,
        alias="defaultValue",
        validation_alias=AliasChoices("defaultValue", "default_value"),
    )


class DTOInt(BaseModel):
    type: Literal["int"] = "int"
    model_config = {"json_schema_extra": {"discriminator": {"propertyName": "type"}}}

    values: List[int] = Field(default_factory=list)

    is_nullable: Optional[bool] = Field(
        default=False,
        alias="isNullable",
        validation_alias=AliasChoices("isNullable", "is_nullable"),
    )
    description: Optional[str] = None
    default_value: Optional[int] = Field(
        default=None,
        alias="defaultValue",
        validation_alias=AliasChoices("defaultValue", "default_value"),
    )

    min_value: Optional[int] = Field(
        default=None,
        alias="minValue",
        validation_alias=AliasChoices("minValue", "min_value"),
    )
    max_value: Optional[int] = Field(
        default=None,
        alias="maxValue",
        validation_alias=AliasChoices("maxValue", "max_value"),
    )
    lower_bound: Optional[Literal["inclusive", "exclusive"]] = Field(
        default="inclusive",
        alias="lowerBound",
        validation_alias=AliasChoices("lowerBound", "lower_bound"),
    )
    upper_bound: Optional[Literal["inclusive", "exclusive"]] = Field(
        default="inclusive",
        alias="upperBound",
        validation_alias=AliasChoices("upperBound", "upper_bound"),
    )

    # todo: deprecate once bedrock hosts are deployed
    allow_negative: Optional[bool] = Field(
        default=True,
        alias="allowNegative",
        validation_alias=AliasChoices("allowNegative", "allow_negative"),
    )


class DTOReal(BaseModel):
    type: Literal["real"] = "real"
    model_config = {"json_schema_extra": {"discriminator": {"propertyName": "type"}}}

    is_nullable: Optional[bool] = Field(
        default=False,
        alias="isNullable",
        validation_alias=AliasChoices("isNullable", "is_nullable"),
    )
    description: Optional[str] = None
    default_value: Optional[float] = Field(
        default=None,
        alias="defaultValue",
        validation_alias=AliasChoices("defaultValue", "default_value"),
    )

    min_value: Optional[float] = Field(
        default=None,
        alias="minValue",
        validation_alias=AliasChoices("minValue", "min_value"),
    )
    max_value: Optional[float] = Field(
        default=None,
        alias="maxValue",
        validation_alias=AliasChoices("maxValue", "max_value"),
    )
    lower_bound: Optional[Literal["inclusive", "exclusive"]] = Field(
        default="inclusive",
        alias="lowerBound",
        validation_alias=AliasChoices("lowerBound", "lower_bound"),
    )
    upper_bound: Optional[Literal["inclusive", "exclusive"]] = Field(
        default="inclusive",
        alias="upperBound",
        validation_alias=AliasChoices("upperBound", "upper_bound"),
    )

    # todo: deprecate once bedrock hosts are deployed
    allow_negative: Optional[bool] = Field(
        default=True,
        alias="allowNegative",
        validation_alias=AliasChoices("allowNegative", "allow_negative"),
    )


class DTOBool(BaseModel):
    type: Literal["bool"] = "bool"
    model_config = {"json_schema_extra": {"discriminator": {"propertyName": "type"}}}

    is_nullable: Optional[bool] = False
    description: Optional[str] = None
    default_value: Optional[bool] = None


class DTOConst(BaseModel):
    type: Literal["constant"] = "constant"
    model_config = {"json_schema_extra": {"discriminator": {"propertyName": "type"}}}

    value: str
    is_nullable: Optional[bool] = Field(
        default=False,
        alias="isNullable",
        validation_alias=AliasChoices("isNullable", "is_nullable"),
    )
    description: Optional[str] = None


class DTOObj(BaseModel):
    type: Literal["object"] = "object"
    model_config = {"json_schema_extra": {"discriminator": {"propertyName": "type"}}}

    is_nullable: Optional[bool] = Field(
        default=False,
        alias="isNullable",
        validation_alias=AliasChoices("isNullable", "is_nullable"),
    )
    description: Optional[str] = None

    fields: Dict[
        str,
        Annotated[
            Union[
                "DTODict",
                "DTOArr",
                "DTOObj",
                "DTOEnum",
                "DTOStr",
                "DTOBool",
                "DTOReal",
                "DTOInt",
                "DTOConst",
            ],
            Field(discriminator="type"),
        ],
    ]


class DTODict(BaseModel):
    type: Literal["dictionary"] = "dictionary"
    model_config = {"json_schema_extra": {"discriminator": {"propertyName": "type"}}}

    is_nullable: Optional[bool] = Field(
        default=False,
        alias="isNullable",
        validation_alias=AliasChoices("isNullable", "is_nullable"),
    )

    obj: Annotated[
        Union[
            "DTODict",
            "DTOArr",
            "DTOObj",
            "DTOEnum",
            "DTOStr",
            "DTOBool",
            "DTOReal",
            "DTOInt",
            "DTOConst",
        ],
        Field(discriminator="type"),
    ]
    keys: Annotated[Union["DTOStr", "DTOEnum"], Field(discriminator="type")]
    min_size: Optional[int] = Field(
        default=None,
        alias="minSize",
        validation_alias=AliasChoices("minSize", "min_size"),
    )
    max_size: Optional[int] = Field(
        default=None,
        alias="maxSize",
        validation_alias=AliasChoices("maxSize", "max_size"),
    )

    description: Optional[str] = None


class DTOArr(BaseModel):
    type: Literal["array"] = "array"
    model_config = {"json_schema_extra": {"discriminator": {"propertyName": "type"}}}

    is_nullable: Optional[bool] = Field(
        default=False,
        alias="isNullable",
        validation_alias=AliasChoices("isNullable", "is_nullable"),
    )
    min_len: int = Field(
        alias="minLen", validation_alias=AliasChoices("minLen", "min_len")
    )
    max_len: Union[None, int] = Field(
        alias="maxLen", validation_alias=AliasChoices("maxLen", "max_len")
    )
    obj: Annotated[
        Union[
            "DTODict",
            "DTOArr",
            "DTOObj",
            "DTOEnum",
            "DTOStr",
            "DTOBool",
            "DTOReal",
            "DTOInt",
        ],
        Field(discriminator="type"),
    ]
    description: Optional[str] = None


class ResponseDTO(BaseModel):
    type: Literal["Response"] = "Response"

    node_id: str = Field(
        alias="nodeId", validation_alias=AliasChoices("nodeId", "node_id")
    )
    child_id: str | None = Field(
        default=None,
        alias="childId",
        validation_alias=AliasChoices("childId", "child_id"),
    )
    as_block: bool = Field(
        alias="asBlock", validation_alias=AliasChoices("asBlock", "as_block")
    )

    template: Optional[str] = None
    context: Optional[str] = None
    inserts: Dict[str, str] = Field(default_factory=dict)


class IntentDTO(BaseModel):
    type: Literal["Intent"] = "Intent"

    node_id: str = Field(
        alias="nodeId", validation_alias=AliasChoices("nodeId", "node_id")
    )
    child_id: str | None = Field(
        default=None,
        alias="childId",
        validation_alias=AliasChoices("childId", "child_id"),
    )

    spec: Annotated[
        Union[
            "DTODict",
            "DTOArr",
            "DTOObj",
            "DTOEnum",
            "DTOStr",
            "DTOBool",
            "DTOReal",
            "DTOInt",
        ],
        Field(discriminator="type"),
    ]
    instruction: Optional[str] = Field(None)


class ConfirmDTO(BaseModel):
    type: Literal["Confirm"] = "Confirm"

    node_id: str = Field(
        alias="nodeId", validation_alias=AliasChoices("nodeId", "node_id")
    )
    child_id: str | None = Field(
        default=None,
        alias="childId",
        validation_alias=AliasChoices("childId", "child_id"),
    )

    instruction: Optional[str] = Field(None)
    options: List[str]


class NoOpDTO(BaseModel):
    type: Literal["NoOp"] = "NoOp"

    node_id: str = Field(
        alias="nodeId", validation_alias=AliasChoices("nodeId", "node_id")
    )
    child_id: str | None = Field(
        default=None,
        alias="childId",
        validation_alias=AliasChoices("childId", "child_id"),
    )

    label: str


class UseToolDTO(BaseModel):
    type: Literal["UseTool"] = "UseTool"

    node_id: str = Field(
        alias="nodeId", validation_alias=AliasChoices("nodeId", "node_id")
    )
    child_id: str | None = Field(
        default=None,
        alias="childId",
        validation_alias=AliasChoices("childId", "child_id"),
    )

    intent_id: str = Field(
        alias="intentId", validation_alias=AliasChoices("intentId", "intent_id")
    )
    tool_obj: Union[Dict, BaseTool] = Field(
        alias="toolObject", validation_alias=AliasChoices("toolObject", "tool_obj")
    )


class SwitchDTO(BaseModel):
    type: Literal["Switch"] = "Switch"

    node_id: str = Field(
        alias="nodeId", validation_alias=AliasChoices("nodeId", "node_id")
    )

    case_spec: Dict[str, str] = Field(
        alias="caseSpec", validation_alias=AliasChoices("caseSpec", "case_spec")
    )
    case_objs: Dict[str, NoOpDTO] = Field(
        alias="caseObjects", validation_alias=AliasChoices("caseObjects", "case_objs")
    )
    isolate: Optional[bool] = False


class ChainOfThoughtDTO(BaseModel):
    type: Literal["ChainOfThought"] = "ChainOfThought"

    node_id: str = Field(
        alias="nodeId", validation_alias=AliasChoices("nodeId", "node_id")
    )

    child_id: str | None = Field(
        default=None,
        alias="childId",
        validation_alias=AliasChoices("childId", "child_id"),
    )

    instructions: list[str]


class ActionRouterDTO(BaseModel):
    type: Literal["ActionRouter"] = "ActionRouter"

    node_id: str = Field(
        alias="nodeId", validation_alias=AliasChoices("nodeId", "node_id")
    )
    plan_intent_id: str = Field(
        alias="planIntentId",
        validation_alias=AliasChoices("planIntentId", "plan_intent_id"),
    )
    action_id_map: Dict[str, str] = Field(
        alias="actionIdMap",
        validation_alias=AliasChoices("actionIdMap", "action_id_map"),
    )
    done_node_id: str = Field(
        alias="doneNodeId", validation_alias=AliasChoices("doneNodeId", "done_node_id")
    )
    stop_node_id: str = Field(
        alias="stopNodeId", validation_alias=AliasChoices("stopNodeId", "stop_node_id")
    )
    error_node_id: str = Field(
        alias="errorNodeId",
        validation_alias=AliasChoices("errorNodeId", "error_node_id"),
    )


class InsertContextDTO(BaseModel):
    type: Literal["Insert"] = "Insert"

    node_id: str = Field(
        alias="nodeId", validation_alias=AliasChoices("nodeId", "node_id")
    )
    child_id: str | None = Field(
        default=None,
        alias="childId",
        validation_alias=AliasChoices("childId", "child_id"),
    )

    label: str
    context: str


class CircuitDTO(BaseModel):
    first: str
    nodes: Dict[
        str,
        Annotated[
            Union[
                "ResponseDTO",
                "IntentDTO",
                "ConfirmDTO",
                "NoOpDTO",
                "UseToolDTO",
                "SwitchDTO",
                "InsertContextDTO",
                "ActionRouterDTO",
                "ChainOfThoughtDTO",
            ],
            Field(discriminator="type"),
        ],
    ]


class CircuitDefinition(BaseModel):
    code: str
    scope: str
    version: str
    description: str

    first: str
    nodes: Dict[
        str,
        Annotated[
            Union[
                "ResponseDTO",
                "IntentDTO",
                "ConfirmDTO",
                "NoOpDTO",
                "UseToolDTO",
                "SwitchDTO",
                "InsertContextDTO",
                "ActionRouterDTO",
                "ChainOfThoughtDTO",
            ],
            Field(discriminator="type"),
        ],
    ]

    description: str


class CreateCircuitRequest(BaseModel):
    code: str
    version_bump: Literal["Major", "Minor", "Patch"] = Field(
        alias="VersionBump",
        validation_alias=AliasChoices("versionBump", "version_bump"),
    )
    description: str
    first: str
    nodes: Dict[
        str,
        Annotated[
            Union[
                "ResponseDTO",
                "IntentDTO",
                "ConfirmDTO",
                "NoOpDTO",
                "UseToolDTO",
                "SwitchDTO",
                "InsertContextDTO",
                "ActionRouterDTO",
                "ChainOfThoughtDTO",
            ],
            Field(discriminator="type"),
        ],
    ]
