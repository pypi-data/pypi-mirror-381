from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ConversionCustomerTypeEnum(_message.Message):
    __slots__ = ()

    class ConversionCustomerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ConversionCustomerTypeEnum.ConversionCustomerType]
        UNKNOWN: _ClassVar[ConversionCustomerTypeEnum.ConversionCustomerType]
        NEW: _ClassVar[ConversionCustomerTypeEnum.ConversionCustomerType]
        RETURNING: _ClassVar[ConversionCustomerTypeEnum.ConversionCustomerType]
    UNSPECIFIED: ConversionCustomerTypeEnum.ConversionCustomerType
    UNKNOWN: ConversionCustomerTypeEnum.ConversionCustomerType
    NEW: ConversionCustomerTypeEnum.ConversionCustomerType
    RETURNING: ConversionCustomerTypeEnum.ConversionCustomerType

    def __init__(self) -> None:
        ...