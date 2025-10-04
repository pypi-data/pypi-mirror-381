from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BusinessMessageCallToActionTypeEnum(_message.Message):
    __slots__ = ()

    class BusinessMessageCallToActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType]
        UNKNOWN: _ClassVar[BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType]
        APPLY_NOW: _ClassVar[BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType]
        BOOK_NOW: _ClassVar[BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType]
        CONTACT_US: _ClassVar[BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType]
        GET_INFO: _ClassVar[BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType]
        GET_OFFER: _ClassVar[BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType]
        GET_QUOTE: _ClassVar[BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType]
        GET_STARTED: _ClassVar[BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType]
        LEARN_MORE: _ClassVar[BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType]
    UNSPECIFIED: BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType
    UNKNOWN: BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType
    APPLY_NOW: BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType
    BOOK_NOW: BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType
    CONTACT_US: BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType
    GET_INFO: BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType
    GET_OFFER: BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType
    GET_QUOTE: BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType
    GET_STARTED: BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType
    LEARN_MORE: BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionType

    def __init__(self) -> None:
        ...