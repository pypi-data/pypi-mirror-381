from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AdStrengthActionItemTypeEnum(_message.Message):
    __slots__ = ()

    class AdStrengthActionItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AdStrengthActionItemTypeEnum.AdStrengthActionItemType]
        UNKNOWN: _ClassVar[AdStrengthActionItemTypeEnum.AdStrengthActionItemType]
        ADD_ASSET: _ClassVar[AdStrengthActionItemTypeEnum.AdStrengthActionItemType]
    UNSPECIFIED: AdStrengthActionItemTypeEnum.AdStrengthActionItemType
    UNKNOWN: AdStrengthActionItemTypeEnum.AdStrengthActionItemType
    ADD_ASSET: AdStrengthActionItemTypeEnum.AdStrengthActionItemType

    def __init__(self) -> None:
        ...