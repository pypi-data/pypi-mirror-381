from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Chokepoint(_message.Message):
    __slots__ = ('related_findings',)
    RELATED_FINDINGS_FIELD_NUMBER: _ClassVar[int]
    related_findings: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, related_findings: _Optional[_Iterable[str]]=...) -> None:
        ...