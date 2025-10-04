from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class FeatureSpec(_message.Message):
    __slots__ = ('config_membership',)
    CONFIG_MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
    config_membership: str

    def __init__(self, config_membership: _Optional[str]=...) -> None:
        ...