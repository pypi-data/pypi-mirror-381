from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.capacityplanner.v1beta import allocation_pb2 as _allocation_pb2
from google.cloud.capacityplanner.v1beta import future_reservation_pb2 as _future_reservation_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import date_pb2 as _date_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class QueryUsageHistoriesRequest(_message.Message):
    __slots__ = ('parent', 'location_level', 'is_spot', 'machine_family', 'machine_shape', 'disk_type', 'confidential_mode', 'gpu_type', 'tpu_type', 'cloud_resource_type', 'usage_aggregation_method', 'start_date', 'end_date')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    IS_SPOT_FIELD_NUMBER: _ClassVar[int]
    MACHINE_FAMILY_FIELD_NUMBER: _ClassVar[int]
    MACHINE_SHAPE_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENTIAL_MODE_FIELD_NUMBER: _ClassVar[int]
    GPU_TYPE_FIELD_NUMBER: _ClassVar[int]
    TPU_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    USAGE_AGGREGATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    location_level: TimeSeries.LocationType
    is_spot: bool
    machine_family: str
    machine_shape: MachineShape
    disk_type: str
    confidential_mode: bool
    gpu_type: str
    tpu_type: str
    cloud_resource_type: str
    usage_aggregation_method: UsageHistory.AggregationMethod
    start_date: _date_pb2.Date
    end_date: _date_pb2.Date

    def __init__(self, parent: _Optional[str]=..., location_level: _Optional[_Union[TimeSeries.LocationType, str]]=..., is_spot: bool=..., machine_family: _Optional[str]=..., machine_shape: _Optional[_Union[MachineShape, _Mapping]]=..., disk_type: _Optional[str]=..., confidential_mode: bool=..., gpu_type: _Optional[str]=..., tpu_type: _Optional[str]=..., cloud_resource_type: _Optional[str]=..., usage_aggregation_method: _Optional[_Union[UsageHistory.AggregationMethod, str]]=..., start_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., end_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=...) -> None:
        ...

class QueryUsageHistoriesResponse(_message.Message):
    __slots__ = ('usage_histories',)
    USAGE_HISTORIES_FIELD_NUMBER: _ClassVar[int]
    usage_histories: _containers.RepeatedCompositeFieldContainer[UsageHistory]

    def __init__(self, usage_histories: _Optional[_Iterable[_Union[UsageHistory, _Mapping]]]=...) -> None:
        ...

class QueryForecastsRequest(_message.Message):
    __slots__ = ('parent', 'machine_family', 'machine_shape', 'disk_type', 'confidential_mode', 'gpu_type', 'tpu_type', 'cloud_resource_type', 'forecast_type', 'prediction_interval', 'aggregation_method')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MACHINE_FAMILY_FIELD_NUMBER: _ClassVar[int]
    MACHINE_SHAPE_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENTIAL_MODE_FIELD_NUMBER: _ClassVar[int]
    GPU_TYPE_FIELD_NUMBER: _ClassVar[int]
    TPU_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FORECAST_TYPE_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    parent: str
    machine_family: str
    machine_shape: MachineShape
    disk_type: str
    confidential_mode: bool
    gpu_type: str
    tpu_type: str
    cloud_resource_type: str
    forecast_type: Forecast.ForecastType
    prediction_interval: Forecast.PredictionInterval
    aggregation_method: UsageHistory.AggregationMethod

    def __init__(self, parent: _Optional[str]=..., machine_family: _Optional[str]=..., machine_shape: _Optional[_Union[MachineShape, _Mapping]]=..., disk_type: _Optional[str]=..., confidential_mode: bool=..., gpu_type: _Optional[str]=..., tpu_type: _Optional[str]=..., cloud_resource_type: _Optional[str]=..., forecast_type: _Optional[_Union[Forecast.ForecastType, str]]=..., prediction_interval: _Optional[_Union[Forecast.PredictionInterval, str]]=..., aggregation_method: _Optional[_Union[UsageHistory.AggregationMethod, str]]=...) -> None:
        ...

class QueryForecastsResponse(_message.Message):
    __slots__ = ('forecasts',)
    FORECASTS_FIELD_NUMBER: _ClassVar[int]
    forecasts: _containers.RepeatedCompositeFieldContainer[Forecast]

    def __init__(self, forecasts: _Optional[_Iterable[_Union[Forecast, _Mapping]]]=...) -> None:
        ...

class QueryReservationsRequest(_message.Message):
    __slots__ = ('parent', 'location_level', 'machine_family', 'machine_shape', 'gpu_type', 'cloud_resource_type', 'reservation_type', 'share_type', 'ownership_type', 'reservation_data_level', 'include_unapproved_reservations', 'aggregation_method', 'start_date', 'end_date')

    class ReservationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESERVATION_TYPE_UNSPECIFIED: _ClassVar[QueryReservationsRequest.ReservationType]
        RESERVATION_TYPE_ALLOCATION: _ClassVar[QueryReservationsRequest.ReservationType]
        RESERVATION_TYPE_FUTURE_RESERVATION: _ClassVar[QueryReservationsRequest.ReservationType]
        RESERVATION_TYPE_ALL: _ClassVar[QueryReservationsRequest.ReservationType]
    RESERVATION_TYPE_UNSPECIFIED: QueryReservationsRequest.ReservationType
    RESERVATION_TYPE_ALLOCATION: QueryReservationsRequest.ReservationType
    RESERVATION_TYPE_FUTURE_RESERVATION: QueryReservationsRequest.ReservationType
    RESERVATION_TYPE_ALL: QueryReservationsRequest.ReservationType

    class ShareType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SHARE_TYPE_UNSPECIFIED: _ClassVar[QueryReservationsRequest.ShareType]
        SHARE_TYPE_LOCAL: _ClassVar[QueryReservationsRequest.ShareType]
        SHARE_TYPE_SPECIFIC_PROJECTS: _ClassVar[QueryReservationsRequest.ShareType]
    SHARE_TYPE_UNSPECIFIED: QueryReservationsRequest.ShareType
    SHARE_TYPE_LOCAL: QueryReservationsRequest.ShareType
    SHARE_TYPE_SPECIFIC_PROJECTS: QueryReservationsRequest.ShareType

    class OwnershipType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OWNERSHIP_TYPE_UNSPECIFIED: _ClassVar[QueryReservationsRequest.OwnershipType]
        OWNERSHIP_TYPE_OWNED: _ClassVar[QueryReservationsRequest.OwnershipType]
        OWNERSHIP_TYPE_SHARED_BY_OTHERS: _ClassVar[QueryReservationsRequest.OwnershipType]
    OWNERSHIP_TYPE_UNSPECIFIED: QueryReservationsRequest.OwnershipType
    OWNERSHIP_TYPE_OWNED: QueryReservationsRequest.OwnershipType
    OWNERSHIP_TYPE_SHARED_BY_OTHERS: QueryReservationsRequest.OwnershipType

    class ReservationDataLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESERVATION_DATA_LEVEL_UNSPECIFIED: _ClassVar[QueryReservationsRequest.ReservationDataLevel]
        RESERVATION_DATA_LEVEL_AGGREGATED: _ClassVar[QueryReservationsRequest.ReservationDataLevel]
        RESERVATION_DATA_LEVEL_PER_RESERVATION: _ClassVar[QueryReservationsRequest.ReservationDataLevel]
    RESERVATION_DATA_LEVEL_UNSPECIFIED: QueryReservationsRequest.ReservationDataLevel
    RESERVATION_DATA_LEVEL_AGGREGATED: QueryReservationsRequest.ReservationDataLevel
    RESERVATION_DATA_LEVEL_PER_RESERVATION: QueryReservationsRequest.ReservationDataLevel
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MACHINE_FAMILY_FIELD_NUMBER: _ClassVar[int]
    MACHINE_SHAPE_FIELD_NUMBER: _ClassVar[int]
    GPU_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHARE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OWNERSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESERVATION_DATA_LEVEL_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_UNAPPROVED_RESERVATIONS_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    location_level: TimeSeries.LocationType
    machine_family: str
    machine_shape: MachineShape
    gpu_type: str
    cloud_resource_type: str
    reservation_type: QueryReservationsRequest.ReservationType
    share_type: QueryReservationsRequest.ShareType
    ownership_type: QueryReservationsRequest.OwnershipType
    reservation_data_level: QueryReservationsRequest.ReservationDataLevel
    include_unapproved_reservations: bool
    aggregation_method: UsageHistory.AggregationMethod
    start_date: _date_pb2.Date
    end_date: _date_pb2.Date

    def __init__(self, parent: _Optional[str]=..., location_level: _Optional[_Union[TimeSeries.LocationType, str]]=..., machine_family: _Optional[str]=..., machine_shape: _Optional[_Union[MachineShape, _Mapping]]=..., gpu_type: _Optional[str]=..., cloud_resource_type: _Optional[str]=..., reservation_type: _Optional[_Union[QueryReservationsRequest.ReservationType, str]]=..., share_type: _Optional[_Union[QueryReservationsRequest.ShareType, str]]=..., ownership_type: _Optional[_Union[QueryReservationsRequest.OwnershipType, str]]=..., reservation_data_level: _Optional[_Union[QueryReservationsRequest.ReservationDataLevel, str]]=..., include_unapproved_reservations: bool=..., aggregation_method: _Optional[_Union[UsageHistory.AggregationMethod, str]]=..., start_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., end_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=...) -> None:
        ...

class QueryReservationsResponse(_message.Message):
    __slots__ = ('reservations',)
    RESERVATIONS_FIELD_NUMBER: _ClassVar[int]
    reservations: _containers.RepeatedCompositeFieldContainer[ReservationData]

    def __init__(self, reservations: _Optional[_Iterable[_Union[ReservationData, _Mapping]]]=...) -> None:
        ...

class Point(_message.Message):
    __slots__ = ('event_time', 'value')
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    event_time: _timestamp_pb2.Timestamp
    value: float

    def __init__(self, event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., value: _Optional[float]=...) -> None:
        ...

class Forecast(_message.Message):
    __slots__ = ('name', 'time_series', 'forecast_type', 'bounds', 'prediction_interval', 'aggregation_method')

    class ForecastType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FORECAST_TYPE_UNSPECIFIED: _ClassVar[Forecast.ForecastType]
        STATISTICAL: _ClassVar[Forecast.ForecastType]
        STATISTICAL_WITH_BFCM: _ClassVar[Forecast.ForecastType]
        YEARLY_SEASONALITY: _ClassVar[Forecast.ForecastType]
    FORECAST_TYPE_UNSPECIFIED: Forecast.ForecastType
    STATISTICAL: Forecast.ForecastType
    STATISTICAL_WITH_BFCM: Forecast.ForecastType
    YEARLY_SEASONALITY: Forecast.ForecastType

    class Bounds(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BOUNDS_UNSPECIFIED: _ClassVar[Forecast.Bounds]
        LOWER_BOUND: _ClassVar[Forecast.Bounds]
        MEDIAN: _ClassVar[Forecast.Bounds]
        UPPER_BOUND: _ClassVar[Forecast.Bounds]
    BOUNDS_UNSPECIFIED: Forecast.Bounds
    LOWER_BOUND: Forecast.Bounds
    MEDIAN: Forecast.Bounds
    UPPER_BOUND: Forecast.Bounds

    class PredictionInterval(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PREDICTION_INTERVAL_UNSPECIFIED: _ClassVar[Forecast.PredictionInterval]
        PREDICTION_INTERVAL_90: _ClassVar[Forecast.PredictionInterval]
        PREDICTION_INTERVAL_50: _ClassVar[Forecast.PredictionInterval]
    PREDICTION_INTERVAL_UNSPECIFIED: Forecast.PredictionInterval
    PREDICTION_INTERVAL_90: Forecast.PredictionInterval
    PREDICTION_INTERVAL_50: Forecast.PredictionInterval
    NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    FORECAST_TYPE_FIELD_NUMBER: _ClassVar[int]
    BOUNDS_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    name: str
    time_series: TimeSeries
    forecast_type: Forecast.ForecastType
    bounds: Forecast.Bounds
    prediction_interval: Forecast.PredictionInterval
    aggregation_method: UsageHistory.AggregationMethod

    def __init__(self, name: _Optional[str]=..., time_series: _Optional[_Union[TimeSeries, _Mapping]]=..., forecast_type: _Optional[_Union[Forecast.ForecastType, str]]=..., bounds: _Optional[_Union[Forecast.Bounds, str]]=..., prediction_interval: _Optional[_Union[Forecast.PredictionInterval, str]]=..., aggregation_method: _Optional[_Union[UsageHistory.AggregationMethod, str]]=...) -> None:
        ...

class UsageHistory(_message.Message):
    __slots__ = ('time_series', 'aggregation_method')

    class AggregationMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AGGREGATION_METHOD_UNSPECIFIED: _ClassVar[UsageHistory.AggregationMethod]
        MEDIAN: _ClassVar[UsageHistory.AggregationMethod]
        PEAK: _ClassVar[UsageHistory.AggregationMethod]
        P50: _ClassVar[UsageHistory.AggregationMethod]
        P75: _ClassVar[UsageHistory.AggregationMethod]
        P99: _ClassVar[UsageHistory.AggregationMethod]
    AGGREGATION_METHOD_UNSPECIFIED: UsageHistory.AggregationMethod
    MEDIAN: UsageHistory.AggregationMethod
    PEAK: UsageHistory.AggregationMethod
    P50: UsageHistory.AggregationMethod
    P75: UsageHistory.AggregationMethod
    P99: UsageHistory.AggregationMethod
    TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    time_series: TimeSeries
    aggregation_method: UsageHistory.AggregationMethod

    def __init__(self, time_series: _Optional[_Union[TimeSeries, _Mapping]]=..., aggregation_method: _Optional[_Union[UsageHistory.AggregationMethod, str]]=...) -> None:
        ...

class TimeSeries(_message.Message):
    __slots__ = ('location_type', 'location', 'is_spot', 'machine_family', 'disk_type', 'confidential_mode', 'gpu_type', 'tpu_type', 'machine_shape', 'cloud_resource_type', 'points', 'unit')

    class LocationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOCATION_TYPE_UNSPECIFIED: _ClassVar[TimeSeries.LocationType]
        REGIONAL: _ClassVar[TimeSeries.LocationType]
        ZONAL: _ClassVar[TimeSeries.LocationType]
    LOCATION_TYPE_UNSPECIFIED: TimeSeries.LocationType
    REGIONAL: TimeSeries.LocationType
    ZONAL: TimeSeries.LocationType
    LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    IS_SPOT_FIELD_NUMBER: _ClassVar[int]
    MACHINE_FAMILY_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENTIAL_MODE_FIELD_NUMBER: _ClassVar[int]
    GPU_TYPE_FIELD_NUMBER: _ClassVar[int]
    TPU_TYPE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_SHAPE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    location_type: TimeSeries.LocationType
    location: str
    is_spot: bool
    machine_family: str
    disk_type: str
    confidential_mode: bool
    gpu_type: str
    tpu_type: str
    machine_shape: MachineShape
    cloud_resource_type: str
    points: _containers.RepeatedCompositeFieldContainer[Point]
    unit: str

    def __init__(self, location_type: _Optional[_Union[TimeSeries.LocationType, str]]=..., location: _Optional[str]=..., is_spot: bool=..., machine_family: _Optional[str]=..., disk_type: _Optional[str]=..., confidential_mode: bool=..., gpu_type: _Optional[str]=..., tpu_type: _Optional[str]=..., machine_shape: _Optional[_Union[MachineShape, _Mapping]]=..., cloud_resource_type: _Optional[str]=..., points: _Optional[_Iterable[_Union[Point, _Mapping]]]=..., unit: _Optional[str]=...) -> None:
        ...

class ReservationData(_message.Message):
    __slots__ = ('name', 'time_series', 'used_reservation_values', 'future_reservations', 'allocations')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_SERIES_FIELD_NUMBER: _ClassVar[int]
    USED_RESERVATION_VALUES_FIELD_NUMBER: _ClassVar[int]
    FUTURE_RESERVATIONS_FIELD_NUMBER: _ClassVar[int]
    ALLOCATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    time_series: TimeSeries
    used_reservation_values: TimeSeries
    future_reservations: _containers.RepeatedCompositeFieldContainer[_future_reservation_pb2.FutureReservation]
    allocations: _containers.RepeatedCompositeFieldContainer[_allocation_pb2.Allocation]

    def __init__(self, name: _Optional[str]=..., time_series: _Optional[_Union[TimeSeries, _Mapping]]=..., used_reservation_values: _Optional[_Union[TimeSeries, _Mapping]]=..., future_reservations: _Optional[_Iterable[_Union[_future_reservation_pb2.FutureReservation, _Mapping]]]=..., allocations: _Optional[_Iterable[_Union[_allocation_pb2.Allocation, _Mapping]]]=...) -> None:
        ...

class MachineShape(_message.Message):
    __slots__ = ('machine_family', 'machine_type', 'machine_shape', 'cpu_cores', 'gpu_type', 'gpu_compute_type', 'gpu_cores', 'local_ssd_partitions', 'local_ssd_gb', 'memory_gb', 'local_ssd_interface', 'min_cpu_platform')
    MACHINE_FAMILY_FIELD_NUMBER: _ClassVar[int]
    MACHINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_SHAPE_FIELD_NUMBER: _ClassVar[int]
    CPU_CORES_FIELD_NUMBER: _ClassVar[int]
    GPU_TYPE_FIELD_NUMBER: _ClassVar[int]
    GPU_COMPUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    GPU_CORES_FIELD_NUMBER: _ClassVar[int]
    LOCAL_SSD_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    LOCAL_SSD_GB_FIELD_NUMBER: _ClassVar[int]
    MEMORY_GB_FIELD_NUMBER: _ClassVar[int]
    LOCAL_SSD_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    MIN_CPU_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    machine_family: str
    machine_type: str
    machine_shape: str
    cpu_cores: float
    gpu_type: str
    gpu_compute_type: str
    gpu_cores: int
    local_ssd_partitions: int
    local_ssd_gb: float
    memory_gb: float
    local_ssd_interface: str
    min_cpu_platform: str

    def __init__(self, machine_family: _Optional[str]=..., machine_type: _Optional[str]=..., machine_shape: _Optional[str]=..., cpu_cores: _Optional[float]=..., gpu_type: _Optional[str]=..., gpu_compute_type: _Optional[str]=..., gpu_cores: _Optional[int]=..., local_ssd_partitions: _Optional[int]=..., local_ssd_gb: _Optional[float]=..., memory_gb: _Optional[float]=..., local_ssd_interface: _Optional[str]=..., min_cpu_platform: _Optional[str]=...) -> None:
        ...

class ExportUsageHistoriesRequest(_message.Message):
    __slots__ = ('parent', 'is_spot', 'machine_family', 'machine_shape', 'disk_type', 'gpu_type', 'tpu_type', 'resource_type', 'usage_aggregation_method', 'start_date', 'end_date', 'output_config')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IS_SPOT_FIELD_NUMBER: _ClassVar[int]
    MACHINE_FAMILY_FIELD_NUMBER: _ClassVar[int]
    MACHINE_SHAPE_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    GPU_TYPE_FIELD_NUMBER: _ClassVar[int]
    TPU_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    USAGE_AGGREGATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    is_spot: bool
    machine_family: str
    machine_shape: MachineShape
    disk_type: str
    gpu_type: str
    tpu_type: str
    resource_type: str
    usage_aggregation_method: UsageHistory.AggregationMethod
    start_date: _date_pb2.Date
    end_date: _date_pb2.Date
    output_config: OutputConfig

    def __init__(self, parent: _Optional[str]=..., is_spot: bool=..., machine_family: _Optional[str]=..., machine_shape: _Optional[_Union[MachineShape, _Mapping]]=..., disk_type: _Optional[str]=..., gpu_type: _Optional[str]=..., tpu_type: _Optional[str]=..., resource_type: _Optional[str]=..., usage_aggregation_method: _Optional[_Union[UsageHistory.AggregationMethod, str]]=..., start_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., end_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., output_config: _Optional[_Union[OutputConfig, _Mapping]]=...) -> None:
        ...

class ExportForecastsRequest(_message.Message):
    __slots__ = ('parent', 'machine_family', 'machine_shape', 'disk_type', 'gpu_type', 'tpu_type', 'resource_type', 'prediction_interval', 'aggregation_method', 'start_date', 'end_date', 'output_config')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MACHINE_FAMILY_FIELD_NUMBER: _ClassVar[int]
    MACHINE_SHAPE_FIELD_NUMBER: _ClassVar[int]
    DISK_TYPE_FIELD_NUMBER: _ClassVar[int]
    GPU_TYPE_FIELD_NUMBER: _ClassVar[int]
    TPU_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PREDICTION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    machine_family: str
    machine_shape: MachineShape
    disk_type: str
    gpu_type: str
    tpu_type: str
    resource_type: str
    prediction_interval: Forecast.PredictionInterval
    aggregation_method: UsageHistory.AggregationMethod
    start_date: _date_pb2.Date
    end_date: _date_pb2.Date
    output_config: OutputConfig

    def __init__(self, parent: _Optional[str]=..., machine_family: _Optional[str]=..., machine_shape: _Optional[_Union[MachineShape, _Mapping]]=..., disk_type: _Optional[str]=..., gpu_type: _Optional[str]=..., tpu_type: _Optional[str]=..., resource_type: _Optional[str]=..., prediction_interval: _Optional[_Union[Forecast.PredictionInterval, str]]=..., aggregation_method: _Optional[_Union[UsageHistory.AggregationMethod, str]]=..., start_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., end_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., output_config: _Optional[_Union[OutputConfig, _Mapping]]=...) -> None:
        ...

class ExportReservationsUsageRequest(_message.Message):
    __slots__ = ('machine_family', 'machine_shape', 'gpu_type', 'parent', 'location_level', 'cloud_resource_type', 'usage_aggregation_method', 'share_type', 'start_date', 'end_date', 'output_config')

    class ShareType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SHARE_TYPE_UNSPECIFIED: _ClassVar[ExportReservationsUsageRequest.ShareType]
        SHARE_TYPE_LOCAL: _ClassVar[ExportReservationsUsageRequest.ShareType]
        SHARE_TYPE_SPECIFIC_PROJECTS: _ClassVar[ExportReservationsUsageRequest.ShareType]
    SHARE_TYPE_UNSPECIFIED: ExportReservationsUsageRequest.ShareType
    SHARE_TYPE_LOCAL: ExportReservationsUsageRequest.ShareType
    SHARE_TYPE_SPECIFIC_PROJECTS: ExportReservationsUsageRequest.ShareType
    MACHINE_FAMILY_FIELD_NUMBER: _ClassVar[int]
    MACHINE_SHAPE_FIELD_NUMBER: _ClassVar[int]
    GPU_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    CLOUD_RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    USAGE_AGGREGATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    SHARE_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    machine_family: str
    machine_shape: MachineShape
    gpu_type: str
    parent: str
    location_level: TimeSeries.LocationType
    cloud_resource_type: str
    usage_aggregation_method: UsageHistory.AggregationMethod
    share_type: ExportReservationsUsageRequest.ShareType
    start_date: _date_pb2.Date
    end_date: _date_pb2.Date
    output_config: OutputConfig

    def __init__(self, machine_family: _Optional[str]=..., machine_shape: _Optional[_Union[MachineShape, _Mapping]]=..., gpu_type: _Optional[str]=..., parent: _Optional[str]=..., location_level: _Optional[_Union[TimeSeries.LocationType, str]]=..., cloud_resource_type: _Optional[str]=..., usage_aggregation_method: _Optional[_Union[UsageHistory.AggregationMethod, str]]=..., share_type: _Optional[_Union[ExportReservationsUsageRequest.ShareType, str]]=..., start_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., end_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., output_config: _Optional[_Union[OutputConfig, _Mapping]]=...) -> None:
        ...

class OutputConfig(_message.Message):
    __slots__ = ('gcs_destination', 'bigquery_destination')
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: GcsDestination
    bigquery_destination: BigQueryDestination

    def __init__(self, gcs_destination: _Optional[_Union[GcsDestination, _Mapping]]=..., bigquery_destination: _Optional[_Union[BigQueryDestination, _Mapping]]=...) -> None:
        ...

class GcsDestination(_message.Message):
    __slots__ = ('uri', 'bucket', 'object', 'force')
    URI_FIELD_NUMBER: _ClassVar[int]
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    uri: str
    bucket: str
    object: str
    force: bool

    def __init__(self, uri: _Optional[str]=..., bucket: _Optional[str]=..., object: _Optional[str]=..., force: bool=...) -> None:
        ...

class BigQueryDestination(_message.Message):
    __slots__ = ('dataset', 'table', 'partition_key', 'write_disposition', 'create_disposition', 'gcs_location')

    class PartitionKey(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PARTITION_KEY_UNSPECIFIED: _ClassVar[BigQueryDestination.PartitionKey]
        REQUEST_TIME: _ClassVar[BigQueryDestination.PartitionKey]
    PARTITION_KEY_UNSPECIFIED: BigQueryDestination.PartitionKey
    REQUEST_TIME: BigQueryDestination.PartitionKey

    class WriteDisposition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WRITE_DISPOSITION_UNSPECIFIED: _ClassVar[BigQueryDestination.WriteDisposition]
        WRITE_APPEND: _ClassVar[BigQueryDestination.WriteDisposition]
        WRITE_TRUNCATE: _ClassVar[BigQueryDestination.WriteDisposition]
        WRITE_EMPTY: _ClassVar[BigQueryDestination.WriteDisposition]
    WRITE_DISPOSITION_UNSPECIFIED: BigQueryDestination.WriteDisposition
    WRITE_APPEND: BigQueryDestination.WriteDisposition
    WRITE_TRUNCATE: BigQueryDestination.WriteDisposition
    WRITE_EMPTY: BigQueryDestination.WriteDisposition

    class CreateDisposition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CREATE_DISPOSITION_UNSPECIFIED: _ClassVar[BigQueryDestination.CreateDisposition]
        CREATE_IF_NEEDED: _ClassVar[BigQueryDestination.CreateDisposition]
        CREATE_NEVER: _ClassVar[BigQueryDestination.CreateDisposition]
    CREATE_DISPOSITION_UNSPECIFIED: BigQueryDestination.CreateDisposition
    CREATE_IF_NEEDED: BigQueryDestination.CreateDisposition
    CREATE_NEVER: BigQueryDestination.CreateDisposition
    DATASET_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    PARTITION_KEY_FIELD_NUMBER: _ClassVar[int]
    WRITE_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    CREATE_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    GCS_LOCATION_FIELD_NUMBER: _ClassVar[int]
    dataset: str
    table: str
    partition_key: BigQueryDestination.PartitionKey
    write_disposition: BigQueryDestination.WriteDisposition
    create_disposition: BigQueryDestination.CreateDisposition
    gcs_location: str

    def __init__(self, dataset: _Optional[str]=..., table: _Optional[str]=..., partition_key: _Optional[_Union[BigQueryDestination.PartitionKey, str]]=..., write_disposition: _Optional[_Union[BigQueryDestination.WriteDisposition, str]]=..., create_disposition: _Optional[_Union[BigQueryDestination.CreateDisposition, str]]=..., gcs_location: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ExportUsageHistoriesResponse(_message.Message):
    __slots__ = ('response',)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: str

    def __init__(self, response: _Optional[str]=...) -> None:
        ...

class ExportForecastsResponse(_message.Message):
    __slots__ = ('response',)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: str

    def __init__(self, response: _Optional[str]=...) -> None:
        ...

class ExportReservationsUsageResponse(_message.Message):
    __slots__ = ('response',)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: str

    def __init__(self, response: _Optional[str]=...) -> None:
        ...