from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Actor(_message.Message):
    __slots__ = ('display_name', 'email', 'google_support', 'username')
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    email: str
    google_support: bool
    username: str

    def __init__(self, display_name: _Optional[str]=..., email: _Optional[str]=..., google_support: bool=..., username: _Optional[str]=...) -> None:
        ...