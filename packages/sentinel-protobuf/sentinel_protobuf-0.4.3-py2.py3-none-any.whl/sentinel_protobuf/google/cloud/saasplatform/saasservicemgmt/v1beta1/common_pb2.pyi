from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UnitOperationErrorCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNIT_OPERATION_ERROR_CATEGORY_UNSPECIFIED: _ClassVar[UnitOperationErrorCategory]
    NOT_APPLICABLE: _ClassVar[UnitOperationErrorCategory]
    FATAL: _ClassVar[UnitOperationErrorCategory]
    RETRIABLE: _ClassVar[UnitOperationErrorCategory]
    IGNORABLE: _ClassVar[UnitOperationErrorCategory]
    STANDARD: _ClassVar[UnitOperationErrorCategory]
UNIT_OPERATION_ERROR_CATEGORY_UNSPECIFIED: UnitOperationErrorCategory
NOT_APPLICABLE: UnitOperationErrorCategory
FATAL: UnitOperationErrorCategory
RETRIABLE: UnitOperationErrorCategory
IGNORABLE: UnitOperationErrorCategory
STANDARD: UnitOperationErrorCategory

class Blueprint(_message.Message):
    __slots__ = ('package', 'engine', 'version')
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    ENGINE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    package: str
    engine: str
    version: str

    def __init__(self, package: _Optional[str]=..., engine: _Optional[str]=..., version: _Optional[str]=...) -> None:
        ...

class UnitVariable(_message.Message):
    __slots__ = ('variable', 'type', 'value')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[UnitVariable.Type]
        STRING: _ClassVar[UnitVariable.Type]
        INT: _ClassVar[UnitVariable.Type]
        BOOL: _ClassVar[UnitVariable.Type]
    TYPE_UNSPECIFIED: UnitVariable.Type
    STRING: UnitVariable.Type
    INT: UnitVariable.Type
    BOOL: UnitVariable.Type
    VARIABLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    variable: str
    type: UnitVariable.Type
    value: str

    def __init__(self, variable: _Optional[str]=..., type: _Optional[_Union[UnitVariable.Type, str]]=..., value: _Optional[str]=...) -> None:
        ...

class UnitCondition(_message.Message):
    __slots__ = ('status', 'type', 'last_transition_time', 'message', 'reason')

    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[UnitCondition.Status]
        STATUS_UNKNOWN: _ClassVar[UnitCondition.Status]
        STATUS_TRUE: _ClassVar[UnitCondition.Status]
        STATUS_FALSE: _ClassVar[UnitCondition.Status]
    STATUS_UNSPECIFIED: UnitCondition.Status
    STATUS_UNKNOWN: UnitCondition.Status
    STATUS_TRUE: UnitCondition.Status
    STATUS_FALSE: UnitCondition.Status

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[UnitCondition.Type]
        TYPE_READY: _ClassVar[UnitCondition.Type]
        TYPE_UPDATING: _ClassVar[UnitCondition.Type]
        TYPE_PROVISIONED: _ClassVar[UnitCondition.Type]
        TYPE_OPERATION_ERROR: _ClassVar[UnitCondition.Type]
    TYPE_UNSPECIFIED: UnitCondition.Type
    TYPE_READY: UnitCondition.Type
    TYPE_UPDATING: UnitCondition.Type
    TYPE_PROVISIONED: UnitCondition.Type
    TYPE_OPERATION_ERROR: UnitCondition.Type
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LAST_TRANSITION_TIME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    status: UnitCondition.Status
    type: UnitCondition.Type
    last_transition_time: _timestamp_pb2.Timestamp
    message: str
    reason: str

    def __init__(self, status: _Optional[_Union[UnitCondition.Status, str]]=..., type: _Optional[_Union[UnitCondition.Type, str]]=..., last_transition_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., message: _Optional[str]=..., reason: _Optional[str]=...) -> None:
        ...

class UnitOperationCondition(_message.Message):
    __slots__ = ('status', 'type', 'last_transition_time', 'message', 'reason')

    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[UnitOperationCondition.Status]
        STATUS_UNKNOWN: _ClassVar[UnitOperationCondition.Status]
        STATUS_TRUE: _ClassVar[UnitOperationCondition.Status]
        STATUS_FALSE: _ClassVar[UnitOperationCondition.Status]
    STATUS_UNSPECIFIED: UnitOperationCondition.Status
    STATUS_UNKNOWN: UnitOperationCondition.Status
    STATUS_TRUE: UnitOperationCondition.Status
    STATUS_FALSE: UnitOperationCondition.Status

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[UnitOperationCondition.Type]
        TYPE_SCHEDULED: _ClassVar[UnitOperationCondition.Type]
        TYPE_RUNNING: _ClassVar[UnitOperationCondition.Type]
        TYPE_SUCCEEDED: _ClassVar[UnitOperationCondition.Type]
        TYPE_CANCELLED: _ClassVar[UnitOperationCondition.Type]
    TYPE_UNSPECIFIED: UnitOperationCondition.Type
    TYPE_SCHEDULED: UnitOperationCondition.Type
    TYPE_RUNNING: UnitOperationCondition.Type
    TYPE_SUCCEEDED: UnitOperationCondition.Type
    TYPE_CANCELLED: UnitOperationCondition.Type
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LAST_TRANSITION_TIME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    status: UnitOperationCondition.Status
    type: UnitOperationCondition.Type
    last_transition_time: _timestamp_pb2.Timestamp
    message: str
    reason: str

    def __init__(self, status: _Optional[_Union[UnitOperationCondition.Status, str]]=..., type: _Optional[_Union[UnitOperationCondition.Type, str]]=..., last_transition_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., message: _Optional[str]=..., reason: _Optional[str]=...) -> None:
        ...

class Aggregate(_message.Message):
    __slots__ = ('group', 'count')
    GROUP_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    group: str
    count: int

    def __init__(self, group: _Optional[str]=..., count: _Optional[int]=...) -> None:
        ...