from google.cloud.capacityplanner.v1beta import allocation_pb2 as _allocation_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FutureReservation(_message.Message):
    __slots__ = ('specific_sku_properties', 'id', 'create_time', 'zone', 'description', 'future_reservation', 'owner_project_id', 'time_window', 'share_settings', 'name_prefix', 'status', 'auto_created_reservations_delete_time', 'auto_delete_auto_created_reservations')

    class SpecificSKUProperties(_message.Message):
        __slots__ = ('instance_properties', 'total_count')
        INSTANCE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
        instance_properties: _allocation_pb2.Allocation.SpecificSKUAllocation.AllocatedInstanceProperties
        total_count: int

        def __init__(self, instance_properties: _Optional[_Union[_allocation_pb2.Allocation.SpecificSKUAllocation.AllocatedInstanceProperties, _Mapping]]=..., total_count: _Optional[int]=...) -> None:
            ...

    class TimeWindow(_message.Message):
        __slots__ = ('start_time', 'end_time')
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        start_time: _timestamp_pb2.Timestamp
        end_time: _timestamp_pb2.Timestamp

        def __init__(self, start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class Status(_message.Message):
        __slots__ = ('procurement_status', 'lock_time', 'auto_created_reservations', 'fulfilled_count')

        class ProcurementStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PROCUREMENT_STATUS_UNSPECIFIED: _ClassVar[FutureReservation.Status.ProcurementStatus]
            PENDING_APPROVAL: _ClassVar[FutureReservation.Status.ProcurementStatus]
            APPROVED: _ClassVar[FutureReservation.Status.ProcurementStatus]
            COMMITTED: _ClassVar[FutureReservation.Status.ProcurementStatus]
            DECLINED: _ClassVar[FutureReservation.Status.ProcurementStatus]
            CANCELLED: _ClassVar[FutureReservation.Status.ProcurementStatus]
            PROCURING: _ClassVar[FutureReservation.Status.ProcurementStatus]
            PROVISIONING: _ClassVar[FutureReservation.Status.ProcurementStatus]
            FULFILLED: _ClassVar[FutureReservation.Status.ProcurementStatus]
            FAILED: _ClassVar[FutureReservation.Status.ProcurementStatus]
            FAILED_PARTIALLY_FULFILLED: _ClassVar[FutureReservation.Status.ProcurementStatus]
            DRAFTING: _ClassVar[FutureReservation.Status.ProcurementStatus]
            PENDING_AMENDMENT_APPROVAL: _ClassVar[FutureReservation.Status.ProcurementStatus]
        PROCUREMENT_STATUS_UNSPECIFIED: FutureReservation.Status.ProcurementStatus
        PENDING_APPROVAL: FutureReservation.Status.ProcurementStatus
        APPROVED: FutureReservation.Status.ProcurementStatus
        COMMITTED: FutureReservation.Status.ProcurementStatus
        DECLINED: FutureReservation.Status.ProcurementStatus
        CANCELLED: FutureReservation.Status.ProcurementStatus
        PROCURING: FutureReservation.Status.ProcurementStatus
        PROVISIONING: FutureReservation.Status.ProcurementStatus
        FULFILLED: FutureReservation.Status.ProcurementStatus
        FAILED: FutureReservation.Status.ProcurementStatus
        FAILED_PARTIALLY_FULFILLED: FutureReservation.Status.ProcurementStatus
        DRAFTING: FutureReservation.Status.ProcurementStatus
        PENDING_AMENDMENT_APPROVAL: FutureReservation.Status.ProcurementStatus
        PROCUREMENT_STATUS_FIELD_NUMBER: _ClassVar[int]
        LOCK_TIME_FIELD_NUMBER: _ClassVar[int]
        AUTO_CREATED_RESERVATIONS_FIELD_NUMBER: _ClassVar[int]
        FULFILLED_COUNT_FIELD_NUMBER: _ClassVar[int]
        procurement_status: FutureReservation.Status.ProcurementStatus
        lock_time: _timestamp_pb2.Timestamp
        auto_created_reservations: _containers.RepeatedScalarFieldContainer[str]
        fulfilled_count: int

        def __init__(self, procurement_status: _Optional[_Union[FutureReservation.Status.ProcurementStatus, str]]=..., lock_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., auto_created_reservations: _Optional[_Iterable[str]]=..., fulfilled_count: _Optional[int]=...) -> None:
            ...
    SPECIFIC_SKU_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FUTURE_RESERVATION_FIELD_NUMBER: _ClassVar[int]
    OWNER_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    TIME_WINDOW_FIELD_NUMBER: _ClassVar[int]
    SHARE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AUTO_CREATED_RESERVATIONS_DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    AUTO_DELETE_AUTO_CREATED_RESERVATIONS_FIELD_NUMBER: _ClassVar[int]
    specific_sku_properties: FutureReservation.SpecificSKUProperties
    id: int
    create_time: _timestamp_pb2.Timestamp
    zone: str
    description: str
    future_reservation: str
    owner_project_id: str
    time_window: FutureReservation.TimeWindow
    share_settings: _allocation_pb2.Allocation.ShareSettings
    name_prefix: str
    status: FutureReservation.Status
    auto_created_reservations_delete_time: _timestamp_pb2.Timestamp
    auto_delete_auto_created_reservations: bool

    def __init__(self, specific_sku_properties: _Optional[_Union[FutureReservation.SpecificSKUProperties, _Mapping]]=..., id: _Optional[int]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., zone: _Optional[str]=..., description: _Optional[str]=..., future_reservation: _Optional[str]=..., owner_project_id: _Optional[str]=..., time_window: _Optional[_Union[FutureReservation.TimeWindow, _Mapping]]=..., share_settings: _Optional[_Union[_allocation_pb2.Allocation.ShareSettings, _Mapping]]=..., name_prefix: _Optional[str]=..., status: _Optional[_Union[FutureReservation.Status, _Mapping]]=..., auto_created_reservations_delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., auto_delete_auto_created_reservations: bool=...) -> None:
        ...