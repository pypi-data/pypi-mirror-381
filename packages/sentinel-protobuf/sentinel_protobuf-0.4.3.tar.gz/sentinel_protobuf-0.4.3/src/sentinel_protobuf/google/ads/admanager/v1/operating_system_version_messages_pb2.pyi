from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class OperatingSystemVersion(_message.Message):
    __slots__ = ('name', 'major_version', 'minor_version', 'micro_version')
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAJOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    MINOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    MICRO_VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    major_version: int
    minor_version: int
    micro_version: int

    def __init__(self, name: _Optional[str]=..., major_version: _Optional[int]=..., minor_version: _Optional[int]=..., micro_version: _Optional[int]=...) -> None:
        ...