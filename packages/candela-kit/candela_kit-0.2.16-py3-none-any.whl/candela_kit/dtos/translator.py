from .circuits import (
    ResponseDTO,
    IntentDTO,
    ConfirmDTO,
    NoOpDTO,
    UseToolDTO,
    InsertContextDTO,
    SwitchDTO,
    ActionRouterDTO,
    ChainOfThoughtDTO,
    CircuitDTO,
)

from ..ignite.states import (
    ResponseState,
    IntentState,
    ConfirmState,
    NoOpState,
    UseToolState,
    InsertContextState,
    SwitchState,
    ActionRouter,
    ChainOfThoughtState,
)
from ..ignite.circuits import Circuit
from typing import Union
from .circuits import (
    DTOEnum,
    DTOInt,
    DTOReal,
    DTOBool,
    DTOConst,
    DTOObj,
    DTOArr,
    DTODict,
    DTOStr,
)

# Import your intent field classes (adjust import path as needed)
from ..ignite.intent import (
    IField,
    IStr,
    IEnum,
    IInt,
    IReal,
    IBool,
    IConst,
    IObj,
    IArr,
    IDict,
)


class IntentFieldToDTO:
    @staticmethod
    def str_dto(x: IStr) -> DTOStr:
        return DTOStr(
            type="string",
            is_nullable=x.is_nullable,
            min_length=x.min_length,
            max_length=x.max_length,
            regex=x.regex,
            format=x.format,
            default_value=x.default_value,
        )

    @staticmethod
    def enum_dto(x: IEnum) -> DTOEnum:
        return DTOEnum(
            type="enum",
            is_nullable=x.is_nullable,
            options=x.options,
            default_value=x.default_value,
        )

    @staticmethod
    def int_dto(x: IInt) -> DTOInt:
        return DTOInt(
            type="int",
            is_nullable=x.is_nullable,
            values=x.values or [],
            default_value=x.default_value,
            min_value=x.min_value,
            max_value=x.max_value,
            lower_bound=x.lower_bound,
            upper_bound=x.upper_bound,
        )

    @staticmethod
    def real_dto(x: IReal) -> DTOReal:
        return DTOReal(
            type="real",
            is_nullable=x.is_nullable,
            default_value=x.default_value,
            min_value=x.min_value,
            max_value=x.max_value,
            lower_bound=x.lower_bound,
            upper_bound=x.upper_bound,
        )

    @staticmethod
    def bool_dto(x: IBool) -> DTOBool:
        return DTOBool(
            type="bool",
            is_nullable=x.is_nullable,
            default_value=x.default_value,
        )

    @staticmethod
    def const_dto(x: IConst) -> DTOConst:
        return DTOConst(
            type="constant",
            is_nullable=x.is_nullable,
            value=x.value,
        )

    @staticmethod
    def obj_dto(x: IObj) -> DTOObj:
        converter = IntentFieldToDTO()
        converted_fields = {}
        for field_name, field_obj in x.fields.items():
            converted_fields[field_name] = converter.convert_field(field_obj)

        return DTOObj(
            type="object",
            is_nullable=x.is_nullable,
            fields=converted_fields,
        )

    @staticmethod
    def arr_dto(x: IArr) -> DTOArr:
        converter = IntentFieldToDTO()
        return DTOArr(
            type="array",
            is_nullable=x.is_nullable,
            min_len=x.min_length or 0,
            max_len=x.max_length,
            obj=converter.convert_field(x.obj),
        )

    @staticmethod
    def dict_dto(x: IDict) -> DTODict:
        converter = IntentFieldToDTO()
        return DTODict(
            type="dictionary",
            is_nullable=x.is_nullable,
            obj=converter.convert_field(x.obj),
            keys=converter.convert_field(x.keys),
            min_size=x.min_length,
            max_size=x.max_length,
        )

    def __init__(self):
        self.mappers = {
            IStr.__name__: self.str_dto,
            IEnum.__name__: self.enum_dto,
            IInt.__name__: self.int_dto,
            IReal.__name__: self.real_dto,
            IBool.__name__: self.bool_dto,
            IConst.__name__: self.const_dto,
            IObj.__name__: self.obj_dto,
            IArr.__name__: self.arr_dto,
            IDict.__name__: self.dict_dto,
        }

    def convert_field(
        self, field: IField
    ) -> Union[
        DTOStr, DTOEnum, DTOInt, DTOReal, DTOBool, DTOConst, DTOObj, DTOArr, DTODict
    ]:
        """Convert an intent field object to its corresponding Pydantic DTO"""
        mapper = self.mappers.get(type(field).__name__)
        if mapper is None:
            raise NotImplementedError(
                f"There is no mapper for intent field type {type(field).__name__}"
            )
        return mapper(field)


class CircuitToDTO:
    @staticmethod
    def response_dto(x: ResponseState) -> ResponseDTO:
        return ResponseDTO(
            node_id=x.node_id,
            child_id=x.child_id,
            as_block=x.as_block,
            template=x.template,
            context=x.context,
            inserts=x.inserts,
        )

    @staticmethod
    def intent_dto(x: IntentState) -> IntentDTO:
        return IntentDTO(
            node_id=x.node_id,
            child_id=x.child_id,
            spec=IntentFieldToDTO().convert_field(x.spec),
            instruction=x.instruction,
        )

    @staticmethod
    def confirm_dto(x: ConfirmState) -> ConfirmDTO:
        return ConfirmDTO(
            node_id=x.node_id,
            child_id=x.child_id,
            instruction=x.instruction,
            options=x.options,
        )

    @staticmethod
    def noop_dto(x: NoOpState) -> NoOpDTO:
        return NoOpDTO(
            node_id=x.node_id,
            child_id=x.child_id,
            label=x.label,
        )

    @staticmethod
    def use_tool_dto(x: UseToolState) -> UseToolDTO:
        return UseToolDTO(
            node_id=x.node_id,
            child_id=x.child_id,
            intent_id=x.intent_id,
            tool_obj=x.tool_obj,
        )

    @staticmethod
    def insert_context_dto(x: InsertContextState) -> InsertContextDTO:
        return InsertContextDTO(
            node_id=x.node_id,
            child_id=x.child_id,
            label=x.label,
            context=x.context,
        )

    @staticmethod
    def switch_dto(x: SwitchState) -> SwitchDTO:
        return SwitchDTO(
            node_id=x.node_id,
            case_spec=x.case_spec,
            case_objs={nid: CircuitToDTO.noop_dto(n) for nid, n in x.case_objs.items()},
            isolate=x.isolate,
        )

    @staticmethod
    def chain_of_thought_dto(x: ChainOfThoughtState) -> ChainOfThoughtDTO:
        return ChainOfThoughtDTO(
            node_id=x.node_id,
            child_id=x.child_id,
            instructions=x.instructions,
        )

    @staticmethod
    def action_router_dto(x: ActionRouter) -> ActionRouterDTO:
        return ActionRouterDTO(
            node_id=x.node_id,
            plan_intent_id=x.plan_intent_id,
            action_id_map=x.action_id_map,
            done_node_id=x.done_node_id,
            stop_node_id=x.stop_node_id,
            error_node_id=x.error_node_id,
        )

    def __init__(self):
        self.mappers = {
            ResponseState.__name__: self.response_dto,
            IntentState.__name__: self.intent_dto,
            ConfirmState.__name__: self.confirm_dto,
            NoOpState.__name__: self.noop_dto,
            UseToolState.__name__: self.use_tool_dto,
            InsertContextState.__name__: self.insert_context_dto,
            SwitchState.__name__: self.switch_dto,
            ChainOfThoughtState.__name__: self.chain_of_thought_dto,
            ActionRouter.__name__: self.action_router_dto,
        }

    def translate(self, circuit: Circuit) -> CircuitDTO:
        node_dtos = {}
        for node_id, node in circuit.nodes.items():
            mapper = self.mappers.get(type(node).__name__)
            if mapper is None:
                raise NotImplementedError(
                    "There is no mapper for state type {}".format(type(node).__name__)
                )
            node_dtos[node_id] = mapper(node)

        return CircuitDTO(
            first=circuit.first,
            nodes=node_dtos,
        )
