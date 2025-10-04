from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class EventAdd(_message.Message):
    __slots__ = ('acc_address', 'value')
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    acc_address: str
    value: str

    def __init__(self, acc_address: _Optional[str]=..., value: _Optional[str]=...) -> None:
        ...

class EventSubtract(_message.Message):
    __slots__ = ('acc_address', 'value')
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    acc_address: str
    value: str

    def __init__(self, acc_address: _Optional[str]=..., value: _Optional[str]=...) -> None:
        ...