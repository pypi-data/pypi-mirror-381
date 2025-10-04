from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Unit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNIT_UNSPECIFIED: _ClassVar[Unit]
    UNIT_COUNT: _ClassVar[Unit]
    KB: _ClassVar[Unit]
    GB: _ClassVar[Unit]
    TB: _ClassVar[Unit]
    MIB: _ClassVar[Unit]
    GIB: _ClassVar[Unit]
    TIB: _ClassVar[Unit]
    QPS: _ClassVar[Unit]
    MB: _ClassVar[Unit]
    PIB: _ClassVar[Unit]
    TBPS: _ClassVar[Unit]
    GBPS_BITS: _ClassVar[Unit]
    GIB_BITS: _ClassVar[Unit]
    MBPS_BITS: _ClassVar[Unit]
    MBPS_BYTES: _ClassVar[Unit]
    TBPS_BITS: _ClassVar[Unit]
    TBPS_BYTES: _ClassVar[Unit]
    KOPS: _ClassVar[Unit]
UNIT_UNSPECIFIED: Unit
UNIT_COUNT: Unit
KB: Unit
GB: Unit
TB: Unit
MIB: Unit
GIB: Unit
TIB: Unit
QPS: Unit
MB: Unit
PIB: Unit
TBPS: Unit
GBPS_BITS: Unit
GIB_BITS: Unit
MBPS_BITS: Unit
MBPS_BYTES: Unit
TBPS_BITS: Unit
TBPS_BYTES: Unit
KOPS: Unit

class ResourceContainer(_message.Message):
    __slots__ = ('type', 'id')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[ResourceContainer.Type]
        PROJECT: _ClassVar[ResourceContainer.Type]
        FOLDER: _ClassVar[ResourceContainer.Type]
        ORG: _ClassVar[ResourceContainer.Type]
    TYPE_UNSPECIFIED: ResourceContainer.Type
    PROJECT: ResourceContainer.Type
    FOLDER: ResourceContainer.Type
    ORG: ResourceContainer.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    type: ResourceContainer.Type
    id: str

    def __init__(self, type: _Optional[_Union[ResourceContainer.Type, str]]=..., id: _Optional[str]=...) -> None:
        ...

class ResourceIdKey(_message.Message):
    __slots__ = ('resource_code', 'resource_id')
    RESOURCE_CODE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    resource_code: str
    resource_id: ResourceIdentifier

    def __init__(self, resource_code: _Optional[str]=..., resource_id: _Optional[_Union[ResourceIdentifier, _Mapping]]=...) -> None:
        ...

class ResourceIdentifier(_message.Message):
    __slots__ = ('service_name', 'resource_name', 'resource_attributes')
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    service_name: str
    resource_name: str
    resource_attributes: _containers.RepeatedCompositeFieldContainer[ResourceAttribute]

    def __init__(self, service_name: _Optional[str]=..., resource_name: _Optional[str]=..., resource_attributes: _Optional[_Iterable[_Union[ResourceAttribute, _Mapping]]]=...) -> None:
        ...

class ResourceAttribute(_message.Message):
    __slots__ = ('key', 'value')
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: ResourceValue

    def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ResourceValue, _Mapping]]=...) -> None:
        ...

class ResourceValue(_message.Message):
    __slots__ = ('unit', 'value')
    UNIT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    unit: Unit
    value: Value

    def __init__(self, unit: _Optional[_Union[Unit, str]]=..., value: _Optional[_Union[Value, _Mapping]]=...) -> None:
        ...

class Value(_message.Message):
    __slots__ = ('int64_value', 'string_value', 'double_value', 'bool_value')
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    int64_value: int
    string_value: str
    double_value: float
    bool_value: bool

    def __init__(self, int64_value: _Optional[int]=..., string_value: _Optional[str]=..., double_value: _Optional[float]=..., bool_value: bool=...) -> None:
        ...