from copy import deepcopy
from typing import Optional, Literal, Dict
from dataclasses import dataclass


@dataclass()
class IField:
    def __init__(self):
        self.is_nullable = False

    def as_nullable(self):
        copy = deepcopy(self)
        copy.is_nullable = True
        return copy


class IStr(IField):
    def __init__(
        self,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        regex: Optional[str] = None,
        format: Optional[str] = None,
        default_value: Optional[str] = None,
    ):
        super().__init__()
        self.min_length = min_length
        self.max_length = max_length
        self.regex = regex
        self.format = format
        self.default_value = default_value


class IEnum(IField):
    def __init__(
        self,
        options: list[str],
        default_value: Optional[str] = None,
    ):
        self.options = options
        self.default_value = default_value
        super().__init__()


class IInt(IField):
    def __init__(
        self,
        values: Optional[list[int]] = None,
        default_value: Optional[int] = None,
        min_value: Optional[int] = None,
        max_value: Optional[int] = None,
        lower_bound: Optional[Literal["inclusive", "exclusive"]] = None,
        upper_bound: Optional[Literal["inclusive", "exclusive"]] = None,
    ):
        self.values = values
        self.default_value = default_value
        self.min_value = min_value
        self.max_value = max_value
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        super().__init__()


class IReal(IField):
    def __init__(
        self,
        default_value: Optional[float] = None,
        min_value: Optional[float] = None,
        max_value: Optional[float] = None,
        lower_bound: Optional[Literal["inclusive", "exclusive"]] = None,
        upper_bound: Optional[Literal["inclusive", "exclusive"]] = None,
    ):
        self.default_value = default_value
        self.min_value = min_value
        self.max_value = max_value
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        super().__init__()


class IBool(IField):
    def __init__(
        self,
        default_value: Optional[bool] = None,
    ):
        self.default_value = default_value
        super().__init__()


class IConst(IField):
    def __init__(self, value: str):
        self.value = value
        super().__init__()


class IObj(IField):
    def __init__(
        self,
        fields: Dict[str, IField],
    ):
        self.fields = {}
        for name, field in fields.items():
            if isinstance(field, str):
                field = IConst(field)
            self.fields[name] = field
        super().__init__()


class IArr(IField):
    def __init__(
        self,
        obj: IField,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
    ):
        self.obj = obj
        self.min_length = min_length
        self.max_length = max_length
        super().__init__()


class IDict(IField):
    def __init__(
        self,
        obj: IField,
        keys: IStr | IEnum,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
    ):
        self.obj = obj
        self.keys = keys
        self.min_length = min_length
        self.max_length = max_length
        super().__init__()


class Fns:
    @staticmethod
    def str(
        min_length: Optional[int] = 0,
        max_length: Optional[int] = None,
        regex: Optional[str] = None,
        format: Optional[str] = None,
        default_value: Optional[str] = None,
    ) -> IStr:
        return IStr(
            min_length=min_length,
            max_length=max_length,
            regex=regex,
            format=format,
            default_value=default_value,
        )

    @staticmethod
    def enum(
        *options,
        default_value: Optional[bool] = None,
    ) -> IEnum:
        if len(options) < 2:
            raise ValueError("at least 2 options are required")
        return IEnum(options=list(options), default_value=default_value)

    @staticmethod
    def int(
        values: Optional[list[int]] = None,
        default_value: Optional[int] = None,
        min_value: Optional[int] = None,
        max_value: Optional[int] = None,
        lower_bound: Optional[Literal["inclusive", "exclusive"]] = None,
        upper_bound: Optional[Literal["inclusive", "exclusive"]] = None,
    ) -> IInt:
        return IInt(
            values=values,
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            lower_bound=lower_bound,
            upper_bound=upper_bound,
        )

    @staticmethod
    def real(
        default_value: Optional[float] = None,
        min_value: Optional[float] = None,
        max_value: Optional[float] = None,
        lower_bound: Optional[Literal["inclusive", "exclusive"]] = "inclusive",
        upper_bound: Optional[Literal["inclusive", "exclusive"]] = "inclusive",
    ) -> IReal:
        return IReal(
            default_value=default_value,
            min_value=min_value,
            max_value=max_value,
            lower_bound=lower_bound,
            upper_bound=upper_bound,
        )

    @staticmethod
    def bool(default_value: Optional[bool] = None) -> IBool:
        return IBool(default_value=default_value)

    @staticmethod
    def date() -> IStr:
        return Fns.str(regex=r"\d{4}-\d{2}-\d{2}")

    @staticmethod
    def datetime() -> IStr:
        return Fns.str(regex=r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}")

    @staticmethod
    def obj(**fields: IField) -> IObj:
        if len(fields) == 0:
            raise ValueError("Obj must have at least one field.")
        return IObj(fields=dict(fields))

    @staticmethod
    def arr(
        obj: IField,
        min_length: Optional[int] = 0,
        max_length: Optional[int] = None,
    ) -> IArr:
        return IArr(obj=obj, min_length=min_length, max_length=max_length)

    @staticmethod
    def dict(obj: IField, keys: Optional[IStr | IEnum | list[str]] = None) -> IDict:
        keys = keys or Fns.str()

        if isinstance(keys, list):
            keys = Fns.enum(*keys)

        return IDict(obj=obj, keys=keys)


intent = Fns()
