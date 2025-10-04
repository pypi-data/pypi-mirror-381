from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ReachPlanPlannableUserListStatusEnum(_message.Message):
    __slots__ = ()

    class ReachPlanPlannableUserListStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ReachPlanPlannableUserListStatusEnum.ReachPlanPlannableUserListStatus]
        UNKNOWN: _ClassVar[ReachPlanPlannableUserListStatusEnum.ReachPlanPlannableUserListStatus]
        PLANNABLE: _ClassVar[ReachPlanPlannableUserListStatusEnum.ReachPlanPlannableUserListStatus]
        UNPLANNABLE: _ClassVar[ReachPlanPlannableUserListStatusEnum.ReachPlanPlannableUserListStatus]
    UNSPECIFIED: ReachPlanPlannableUserListStatusEnum.ReachPlanPlannableUserListStatus
    UNKNOWN: ReachPlanPlannableUserListStatusEnum.ReachPlanPlannableUserListStatus
    PLANNABLE: ReachPlanPlannableUserListStatusEnum.ReachPlanPlannableUserListStatus
    UNPLANNABLE: ReachPlanPlannableUserListStatusEnum.ReachPlanPlannableUserListStatus

    def __init__(self) -> None:
        ...