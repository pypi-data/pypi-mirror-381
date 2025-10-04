from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class BrandGuidelinesMigrationErrorEnum(_message.Message):
    __slots__ = ()

    class BrandGuidelinesMigrationError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[BrandGuidelinesMigrationErrorEnum.BrandGuidelinesMigrationError]
        UNKNOWN: _ClassVar[BrandGuidelinesMigrationErrorEnum.BrandGuidelinesMigrationError]
        BRAND_GUIDELINES_ALREADY_ENABLED: _ClassVar[BrandGuidelinesMigrationErrorEnum.BrandGuidelinesMigrationError]
        CANNOT_ENABLE_BRAND_GUIDELINES_FOR_REMOVED_CAMPAIGN: _ClassVar[BrandGuidelinesMigrationErrorEnum.BrandGuidelinesMigrationError]
        BRAND_GUIDELINES_LOGO_LIMIT_EXCEEDED: _ClassVar[BrandGuidelinesMigrationErrorEnum.BrandGuidelinesMigrationError]
        CANNOT_AUTO_POPULATE_BRAND_ASSETS_WHEN_BRAND_ASSETS_PROVIDED: _ClassVar[BrandGuidelinesMigrationErrorEnum.BrandGuidelinesMigrationError]
        AUTO_POPULATE_BRAND_ASSETS_REQUIRED_WHEN_BRAND_ASSETS_OMITTED: _ClassVar[BrandGuidelinesMigrationErrorEnum.BrandGuidelinesMigrationError]
        TOO_MANY_ENABLE_OPERATIONS: _ClassVar[BrandGuidelinesMigrationErrorEnum.BrandGuidelinesMigrationError]
    UNSPECIFIED: BrandGuidelinesMigrationErrorEnum.BrandGuidelinesMigrationError
    UNKNOWN: BrandGuidelinesMigrationErrorEnum.BrandGuidelinesMigrationError
    BRAND_GUIDELINES_ALREADY_ENABLED: BrandGuidelinesMigrationErrorEnum.BrandGuidelinesMigrationError
    CANNOT_ENABLE_BRAND_GUIDELINES_FOR_REMOVED_CAMPAIGN: BrandGuidelinesMigrationErrorEnum.BrandGuidelinesMigrationError
    BRAND_GUIDELINES_LOGO_LIMIT_EXCEEDED: BrandGuidelinesMigrationErrorEnum.BrandGuidelinesMigrationError
    CANNOT_AUTO_POPULATE_BRAND_ASSETS_WHEN_BRAND_ASSETS_PROVIDED: BrandGuidelinesMigrationErrorEnum.BrandGuidelinesMigrationError
    AUTO_POPULATE_BRAND_ASSETS_REQUIRED_WHEN_BRAND_ASSETS_OMITTED: BrandGuidelinesMigrationErrorEnum.BrandGuidelinesMigrationError
    TOO_MANY_ENABLE_OPERATIONS: BrandGuidelinesMigrationErrorEnum.BrandGuidelinesMigrationError

    def __init__(self) -> None:
        ...