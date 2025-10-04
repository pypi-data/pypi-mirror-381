from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class FinalUrlExpansionAssetViewErrorEnum(_message.Message):
    __slots__ = ()

    class FinalUrlExpansionAssetViewError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[FinalUrlExpansionAssetViewErrorEnum.FinalUrlExpansionAssetViewError]
        UNKNOWN: _ClassVar[FinalUrlExpansionAssetViewErrorEnum.FinalUrlExpansionAssetViewError]
        MISSING_REQUIRED_FILTER: _ClassVar[FinalUrlExpansionAssetViewErrorEnum.FinalUrlExpansionAssetViewError]
        REQUIRES_ADVERTISING_CHANNEL_TYPE_FILTER: _ClassVar[FinalUrlExpansionAssetViewErrorEnum.FinalUrlExpansionAssetViewError]
        INVALID_ADVERTISING_CHANNEL_TYPE_IN_FILTER: _ClassVar[FinalUrlExpansionAssetViewErrorEnum.FinalUrlExpansionAssetViewError]
        CANNOT_SELECT_ASSET_GROUP: _ClassVar[FinalUrlExpansionAssetViewErrorEnum.FinalUrlExpansionAssetViewError]
        CANNOT_SELECT_AD_GROUP: _ClassVar[FinalUrlExpansionAssetViewErrorEnum.FinalUrlExpansionAssetViewError]
        REQUIRES_FILTER_BY_SINGLE_RESOURCE: _ClassVar[FinalUrlExpansionAssetViewErrorEnum.FinalUrlExpansionAssetViewError]
        CANNOT_SELECT_BOTH_AD_GROUP_AND_ASSET_GROUP: _ClassVar[FinalUrlExpansionAssetViewErrorEnum.FinalUrlExpansionAssetViewError]
        CANNOT_FILTER_BY_BOTH_AD_GROUP_AND_ASSET_GROUP: _ClassVar[FinalUrlExpansionAssetViewErrorEnum.FinalUrlExpansionAssetViewError]
    UNSPECIFIED: FinalUrlExpansionAssetViewErrorEnum.FinalUrlExpansionAssetViewError
    UNKNOWN: FinalUrlExpansionAssetViewErrorEnum.FinalUrlExpansionAssetViewError
    MISSING_REQUIRED_FILTER: FinalUrlExpansionAssetViewErrorEnum.FinalUrlExpansionAssetViewError
    REQUIRES_ADVERTISING_CHANNEL_TYPE_FILTER: FinalUrlExpansionAssetViewErrorEnum.FinalUrlExpansionAssetViewError
    INVALID_ADVERTISING_CHANNEL_TYPE_IN_FILTER: FinalUrlExpansionAssetViewErrorEnum.FinalUrlExpansionAssetViewError
    CANNOT_SELECT_ASSET_GROUP: FinalUrlExpansionAssetViewErrorEnum.FinalUrlExpansionAssetViewError
    CANNOT_SELECT_AD_GROUP: FinalUrlExpansionAssetViewErrorEnum.FinalUrlExpansionAssetViewError
    REQUIRES_FILTER_BY_SINGLE_RESOURCE: FinalUrlExpansionAssetViewErrorEnum.FinalUrlExpansionAssetViewError
    CANNOT_SELECT_BOTH_AD_GROUP_AND_ASSET_GROUP: FinalUrlExpansionAssetViewErrorEnum.FinalUrlExpansionAssetViewError
    CANNOT_FILTER_BY_BOTH_AD_GROUP_AND_ASSET_GROUP: FinalUrlExpansionAssetViewErrorEnum.FinalUrlExpansionAssetViewError

    def __init__(self) -> None:
        ...