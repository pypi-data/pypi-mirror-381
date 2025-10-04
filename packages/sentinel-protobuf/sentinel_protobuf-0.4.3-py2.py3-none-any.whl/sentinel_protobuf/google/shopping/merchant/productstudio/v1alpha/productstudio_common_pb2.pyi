from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class InputImage(_message.Message):
    __slots__ = ('image_uri', 'image_bytes')
    IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    IMAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    image_uri: str
    image_bytes: bytes

    def __init__(self, image_uri: _Optional[str]=..., image_bytes: _Optional[bytes]=...) -> None:
        ...