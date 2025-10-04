from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class NoneValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE_VALUE_UNSPECIFIED: _ClassVar[NoneValue]
NONE_VALUE_UNSPECIFIED: NoneValue

class Entity(_message.Message):
    __slots__ = ('id',)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str

    def __init__(self, id: _Optional[str]=...) -> None:
        ...

class CurrencyValue(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int

    def __init__(self, value: _Optional[int]=...) -> None:
        ...

class StringList(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, value: _Optional[_Iterable[str]]=...) -> None:
        ...

class Int64List(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, value: _Optional[_Iterable[int]]=...) -> None:
        ...

class BoolList(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[bool]

    def __init__(self, value: _Optional[_Iterable[bool]]=...) -> None:
        ...

class DictList(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[DictValue]

    def __init__(self, value: _Optional[_Iterable[_Union[DictValue, _Mapping]]]=...) -> None:
        ...

class DictValue(_message.Message):
    __slots__ = ('bool_keys', 'string_keys', 'int64_keys', 'bool_values', 'string_values', 'int64_values', 'dict_values')
    BOOL_KEYS_FIELD_NUMBER: _ClassVar[int]
    STRING_KEYS_FIELD_NUMBER: _ClassVar[int]
    INT64_KEYS_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUES_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUES_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUES_FIELD_NUMBER: _ClassVar[int]
    DICT_VALUES_FIELD_NUMBER: _ClassVar[int]
    bool_keys: BoolList
    string_keys: StringList
    int64_keys: Int64List
    bool_values: BoolList
    string_values: StringList
    int64_values: Int64List
    dict_values: DictList

    def __init__(self, bool_keys: _Optional[_Union[BoolList, _Mapping]]=..., string_keys: _Optional[_Union[StringList, _Mapping]]=..., int64_keys: _Optional[_Union[Int64List, _Mapping]]=..., bool_values: _Optional[_Union[BoolList, _Mapping]]=..., string_values: _Optional[_Union[StringList, _Mapping]]=..., int64_values: _Optional[_Union[Int64List, _Mapping]]=..., dict_values: _Optional[_Union[DictList, _Mapping]]=...) -> None:
        ...

class Value(_message.Message):
    __slots__ = ('none_value', 'bool_value', 'int64_value', 'string_value', 'account_id', 'dict_value')
    NONE_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    DICT_VALUE_FIELD_NUMBER: _ClassVar[int]
    none_value: NoneValue
    bool_value: bool
    int64_value: int
    string_value: str
    account_id: str
    dict_value: DictValue

    def __init__(self, none_value: _Optional[_Union[NoneValue, str]]=..., bool_value: bool=..., int64_value: _Optional[int]=..., string_value: _Optional[str]=..., account_id: _Optional[str]=..., dict_value: _Optional[_Union[DictValue, _Mapping]]=...) -> None:
        ...