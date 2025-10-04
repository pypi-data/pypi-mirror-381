from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class DeviceInfo(_message.Message):
    __slots__ = ('user_agent', 'ip_address')
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    user_agent: str
    ip_address: str

    def __init__(self, user_agent: _Optional[str]=..., ip_address: _Optional[str]=...) -> None:
        ...