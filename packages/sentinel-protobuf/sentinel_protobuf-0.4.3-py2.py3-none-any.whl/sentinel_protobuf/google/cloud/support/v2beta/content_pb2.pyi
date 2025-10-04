from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class TextContent(_message.Message):
    __slots__ = ('plain_text',)
    PLAIN_TEXT_FIELD_NUMBER: _ClassVar[int]
    plain_text: str

    def __init__(self, plain_text: _Optional[str]=...) -> None:
        ...