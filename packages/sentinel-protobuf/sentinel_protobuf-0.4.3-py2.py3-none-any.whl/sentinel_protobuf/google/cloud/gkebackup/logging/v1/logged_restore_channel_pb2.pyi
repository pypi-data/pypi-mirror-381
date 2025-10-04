from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class LoggedRestoreChannel(_message.Message):
    __slots__ = ('destination_project', 'labels', 'description')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    DESTINATION_PROJECT_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    destination_project: str
    labels: _containers.ScalarMap[str, str]
    description: str

    def __init__(self, destination_project: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=...) -> None:
        ...