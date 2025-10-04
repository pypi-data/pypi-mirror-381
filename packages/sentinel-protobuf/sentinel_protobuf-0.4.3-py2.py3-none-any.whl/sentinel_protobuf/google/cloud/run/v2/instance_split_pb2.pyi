from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class InstanceSplitAllocationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INSTANCE_SPLIT_ALLOCATION_TYPE_UNSPECIFIED: _ClassVar[InstanceSplitAllocationType]
    INSTANCE_SPLIT_ALLOCATION_TYPE_LATEST: _ClassVar[InstanceSplitAllocationType]
    INSTANCE_SPLIT_ALLOCATION_TYPE_REVISION: _ClassVar[InstanceSplitAllocationType]
INSTANCE_SPLIT_ALLOCATION_TYPE_UNSPECIFIED: InstanceSplitAllocationType
INSTANCE_SPLIT_ALLOCATION_TYPE_LATEST: InstanceSplitAllocationType
INSTANCE_SPLIT_ALLOCATION_TYPE_REVISION: InstanceSplitAllocationType

class InstanceSplit(_message.Message):
    __slots__ = ('type', 'revision', 'percent')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    PERCENT_FIELD_NUMBER: _ClassVar[int]
    type: InstanceSplitAllocationType
    revision: str
    percent: int

    def __init__(self, type: _Optional[_Union[InstanceSplitAllocationType, str]]=..., revision: _Optional[str]=..., percent: _Optional[int]=...) -> None:
        ...

class InstanceSplitStatus(_message.Message):
    __slots__ = ('type', 'revision', 'percent')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    PERCENT_FIELD_NUMBER: _ClassVar[int]
    type: InstanceSplitAllocationType
    revision: str
    percent: int

    def __init__(self, type: _Optional[_Union[InstanceSplitAllocationType, str]]=..., revision: _Optional[str]=..., percent: _Optional[int]=...) -> None:
        ...