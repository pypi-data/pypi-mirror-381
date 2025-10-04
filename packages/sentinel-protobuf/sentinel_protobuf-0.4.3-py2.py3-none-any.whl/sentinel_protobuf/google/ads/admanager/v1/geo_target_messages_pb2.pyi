from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class GeoTarget(_message.Message):
    __slots__ = ('name', 'display_name', 'canonical_parent', 'parent_names', 'region_code', 'type', 'targetable')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_PARENT_FIELD_NUMBER: _ClassVar[int]
    PARENT_NAMES_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGETABLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    canonical_parent: str
    parent_names: _containers.RepeatedScalarFieldContainer[str]
    region_code: str
    type: str
    targetable: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., canonical_parent: _Optional[str]=..., parent_names: _Optional[_Iterable[str]]=..., region_code: _Optional[str]=..., type: _Optional[str]=..., targetable: bool=...) -> None:
        ...