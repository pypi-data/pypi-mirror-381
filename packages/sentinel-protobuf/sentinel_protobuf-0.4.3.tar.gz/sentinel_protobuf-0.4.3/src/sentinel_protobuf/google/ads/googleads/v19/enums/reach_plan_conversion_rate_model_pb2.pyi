from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ReachPlanConversionRateModelEnum(_message.Message):
    __slots__ = ()

    class ReachPlanConversionRateModel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ReachPlanConversionRateModelEnum.ReachPlanConversionRateModel]
        UNKNOWN: _ClassVar[ReachPlanConversionRateModelEnum.ReachPlanConversionRateModel]
        CUSTOMER_HISTORY: _ClassVar[ReachPlanConversionRateModelEnum.ReachPlanConversionRateModel]
        INVENTORY_AGGRESSIVE: _ClassVar[ReachPlanConversionRateModelEnum.ReachPlanConversionRateModel]
        INVENTORY_CONSERVATIVE: _ClassVar[ReachPlanConversionRateModelEnum.ReachPlanConversionRateModel]
        INVENTORY_MEDIAN: _ClassVar[ReachPlanConversionRateModelEnum.ReachPlanConversionRateModel]
    UNSPECIFIED: ReachPlanConversionRateModelEnum.ReachPlanConversionRateModel
    UNKNOWN: ReachPlanConversionRateModelEnum.ReachPlanConversionRateModel
    CUSTOMER_HISTORY: ReachPlanConversionRateModelEnum.ReachPlanConversionRateModel
    INVENTORY_AGGRESSIVE: ReachPlanConversionRateModelEnum.ReachPlanConversionRateModel
    INVENTORY_CONSERVATIVE: ReachPlanConversionRateModelEnum.ReachPlanConversionRateModel
    INVENTORY_MEDIAN: ReachPlanConversionRateModelEnum.ReachPlanConversionRateModel

    def __init__(self) -> None:
        ...