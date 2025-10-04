from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class AssetCoverageVideoAspectRatioRequirementEnum(_message.Message):
    __slots__ = ()

    class AssetCoverageVideoAspectRatioRequirement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AssetCoverageVideoAspectRatioRequirementEnum.AssetCoverageVideoAspectRatioRequirement]
        UNKNOWN: _ClassVar[AssetCoverageVideoAspectRatioRequirementEnum.AssetCoverageVideoAspectRatioRequirement]
        HORIZONTAL: _ClassVar[AssetCoverageVideoAspectRatioRequirementEnum.AssetCoverageVideoAspectRatioRequirement]
        SQUARE: _ClassVar[AssetCoverageVideoAspectRatioRequirementEnum.AssetCoverageVideoAspectRatioRequirement]
        VERTICAL: _ClassVar[AssetCoverageVideoAspectRatioRequirementEnum.AssetCoverageVideoAspectRatioRequirement]
    UNSPECIFIED: AssetCoverageVideoAspectRatioRequirementEnum.AssetCoverageVideoAspectRatioRequirement
    UNKNOWN: AssetCoverageVideoAspectRatioRequirementEnum.AssetCoverageVideoAspectRatioRequirement
    HORIZONTAL: AssetCoverageVideoAspectRatioRequirementEnum.AssetCoverageVideoAspectRatioRequirement
    SQUARE: AssetCoverageVideoAspectRatioRequirementEnum.AssetCoverageVideoAspectRatioRequirement
    VERTICAL: AssetCoverageVideoAspectRatioRequirementEnum.AssetCoverageVideoAspectRatioRequirement

    def __init__(self) -> None:
        ...