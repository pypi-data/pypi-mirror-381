from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class LoggedRestorePlanMetadata(_message.Message):
    __slots__ = ('restore_channel',)
    RESTORE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    restore_channel: str

    def __init__(self, restore_channel: _Optional[str]=...) -> None:
        ...