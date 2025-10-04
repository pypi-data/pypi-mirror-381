from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PromotionBarcodeTypeEnum(_message.Message):
    __slots__ = ()

    class PromotionBarcodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PromotionBarcodeTypeEnum.PromotionBarcodeType]
        UNKNOWN: _ClassVar[PromotionBarcodeTypeEnum.PromotionBarcodeType]
        AZTEC: _ClassVar[PromotionBarcodeTypeEnum.PromotionBarcodeType]
        CODABAR: _ClassVar[PromotionBarcodeTypeEnum.PromotionBarcodeType]
        CODE39: _ClassVar[PromotionBarcodeTypeEnum.PromotionBarcodeType]
        CODE128: _ClassVar[PromotionBarcodeTypeEnum.PromotionBarcodeType]
        DATA_MATRIX: _ClassVar[PromotionBarcodeTypeEnum.PromotionBarcodeType]
        EAN8: _ClassVar[PromotionBarcodeTypeEnum.PromotionBarcodeType]
        EAN13: _ClassVar[PromotionBarcodeTypeEnum.PromotionBarcodeType]
        ITF: _ClassVar[PromotionBarcodeTypeEnum.PromotionBarcodeType]
        PDF417: _ClassVar[PromotionBarcodeTypeEnum.PromotionBarcodeType]
        UPC_A: _ClassVar[PromotionBarcodeTypeEnum.PromotionBarcodeType]
    UNSPECIFIED: PromotionBarcodeTypeEnum.PromotionBarcodeType
    UNKNOWN: PromotionBarcodeTypeEnum.PromotionBarcodeType
    AZTEC: PromotionBarcodeTypeEnum.PromotionBarcodeType
    CODABAR: PromotionBarcodeTypeEnum.PromotionBarcodeType
    CODE39: PromotionBarcodeTypeEnum.PromotionBarcodeType
    CODE128: PromotionBarcodeTypeEnum.PromotionBarcodeType
    DATA_MATRIX: PromotionBarcodeTypeEnum.PromotionBarcodeType
    EAN8: PromotionBarcodeTypeEnum.PromotionBarcodeType
    EAN13: PromotionBarcodeTypeEnum.PromotionBarcodeType
    ITF: PromotionBarcodeTypeEnum.PromotionBarcodeType
    PDF417: PromotionBarcodeTypeEnum.PromotionBarcodeType
    UPC_A: PromotionBarcodeTypeEnum.PromotionBarcodeType

    def __init__(self) -> None:
        ...