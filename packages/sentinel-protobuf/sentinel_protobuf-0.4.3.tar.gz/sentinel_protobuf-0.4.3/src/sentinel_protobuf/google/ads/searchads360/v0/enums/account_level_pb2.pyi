from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AccountLevelTypeEnum(_message.Message):
    __slots__ = ()

    class AccountLevelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AccountLevelTypeEnum.AccountLevelType]
        UNKNOWN: _ClassVar[AccountLevelTypeEnum.AccountLevelType]
        CLIENT_ACCOUNT_FACEBOOK: _ClassVar[AccountLevelTypeEnum.AccountLevelType]
        CLIENT_ACCOUNT_GOOGLE_ADS: _ClassVar[AccountLevelTypeEnum.AccountLevelType]
        CLIENT_ACCOUNT_MICROSOFT: _ClassVar[AccountLevelTypeEnum.AccountLevelType]
        CLIENT_ACCOUNT_YAHOO_JAPAN: _ClassVar[AccountLevelTypeEnum.AccountLevelType]
        CLIENT_ACCOUNT_ENGINE_TRACK: _ClassVar[AccountLevelTypeEnum.AccountLevelType]
        MANAGER: _ClassVar[AccountLevelTypeEnum.AccountLevelType]
        SUB_MANAGER: _ClassVar[AccountLevelTypeEnum.AccountLevelType]
        ASSOCIATE_MANAGER: _ClassVar[AccountLevelTypeEnum.AccountLevelType]
    UNSPECIFIED: AccountLevelTypeEnum.AccountLevelType
    UNKNOWN: AccountLevelTypeEnum.AccountLevelType
    CLIENT_ACCOUNT_FACEBOOK: AccountLevelTypeEnum.AccountLevelType
    CLIENT_ACCOUNT_GOOGLE_ADS: AccountLevelTypeEnum.AccountLevelType
    CLIENT_ACCOUNT_MICROSOFT: AccountLevelTypeEnum.AccountLevelType
    CLIENT_ACCOUNT_YAHOO_JAPAN: AccountLevelTypeEnum.AccountLevelType
    CLIENT_ACCOUNT_ENGINE_TRACK: AccountLevelTypeEnum.AccountLevelType
    MANAGER: AccountLevelTypeEnum.AccountLevelType
    SUB_MANAGER: AccountLevelTypeEnum.AccountLevelType
    ASSOCIATE_MANAGER: AccountLevelTypeEnum.AccountLevelType

    def __init__(self) -> None:
        ...