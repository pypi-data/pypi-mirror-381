from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.capacityplanner.v1beta import location_pb2 as _location_pb2
from google.cloud.capacityplanner.v1beta import resource_pb2 as _resource_pb2_1
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATE_UNSPECIFIED: _ClassVar[State]
    PENDING_REVIEW: _ClassVar[State]
    IN_REVIEW: _ClassVar[State]
    APPROVED_PROVISIONAL: _ClassVar[State]
    OBSOLETE: _ClassVar[State]
    CANNOT_BE_FULFILLED: _ClassVar[State]
    ON_HOLD_CONTACT_SALES: _ClassVar[State]
    IN_FULFILLMENT: _ClassVar[State]

class CapacityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CAPACITY_TYPE_UNKNOWN: _ClassVar[CapacityType]
    CAPACITY_TYPE_INORGANIC_DRAFT: _ClassVar[CapacityType]
    CAPACITY_TYPE_INORGANIC_PENDING: _ClassVar[CapacityType]
    CAPACITY_TYPE_INORGANIC_APPROVED: _ClassVar[CapacityType]
STATE_UNSPECIFIED: State
PENDING_REVIEW: State
IN_REVIEW: State
APPROVED_PROVISIONAL: State
OBSOLETE: State
CANNOT_BE_FULFILLED: State
ON_HOLD_CONTACT_SALES: State
IN_FULFILLMENT: State
CAPACITY_TYPE_UNKNOWN: CapacityType
CAPACITY_TYPE_INORGANIC_DRAFT: CapacityType
CAPACITY_TYPE_INORGANIC_PENDING: CapacityType
CAPACITY_TYPE_INORGANIC_APPROVED: CapacityType

class GetCapacityPlanRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class QueryCapacityPlansRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'location')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    location: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., location: _Optional[str]=...) -> None:
        ...

class QueryCapacityPlansResponse(_message.Message):
    __slots__ = ('capacity_plans', 'next_page_token')
    CAPACITY_PLANS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    capacity_plans: _containers.RepeatedCompositeFieldContainer[CapacityPlan]
    next_page_token: str

    def __init__(self, capacity_plans: _Optional[_Iterable[_Union[CapacityPlan, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class QueryCapacityPlanInsightsRequest(_message.Message):
    __slots__ = ('parent', 'capacity_plan_filters')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_PLAN_FILTERS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    capacity_plan_filters: CapacityPlanFilters

    def __init__(self, parent: _Optional[str]=..., capacity_plan_filters: _Optional[_Union[CapacityPlanFilters, _Mapping]]=...) -> None:
        ...

class QueryCapacityPlanInsightsResponse(_message.Message):
    __slots__ = ('aggregated_capacity_plan_view',)
    AGGREGATED_CAPACITY_PLAN_VIEW_FIELD_NUMBER: _ClassVar[int]
    aggregated_capacity_plan_view: CapacityPlanView

    def __init__(self, aggregated_capacity_plan_view: _Optional[_Union[CapacityPlanView, _Mapping]]=...) -> None:
        ...

class CapacityPlanFilters(_message.Message):
    __slots__ = ('keys', 'capacity_types', 'capacity_plan_id')
    KEYS_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_TYPES_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[CapacityPlanKey]
    capacity_types: _containers.RepeatedScalarFieldContainer[CapacityType]
    capacity_plan_id: str

    def __init__(self, keys: _Optional[_Iterable[_Union[CapacityPlanKey, _Mapping]]]=..., capacity_types: _Optional[_Iterable[_Union[CapacityType, str]]]=..., capacity_plan_id: _Optional[str]=...) -> None:
        ...

class CapacityPlanKey(_message.Message):
    __slots__ = ('resource_container', 'resource_id_key', 'location_id')
    RESOURCE_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_KEY_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    resource_container: _resource_pb2_1.ResourceContainer
    resource_id_key: _resource_pb2_1.ResourceIdKey
    location_id: _location_pb2.LocationIdentifier

    def __init__(self, resource_container: _Optional[_Union[_resource_pb2_1.ResourceContainer, _Mapping]]=..., resource_id_key: _Optional[_Union[_resource_pb2_1.ResourceIdKey, _Mapping]]=..., location_id: _Optional[_Union[_location_pb2.LocationIdentifier, _Mapping]]=...) -> None:
        ...

class CapacityPlanView(_message.Message):
    __slots__ = ('key', 'time_series_views')
    KEY_FIELD_NUMBER: _ClassVar[int]
    TIME_SERIES_VIEWS_FIELD_NUMBER: _ClassVar[int]
    key: CapacityPlanKey
    time_series_views: _containers.RepeatedCompositeFieldContainer[TimeSeriesView]

    def __init__(self, key: _Optional[_Union[CapacityPlanKey, _Mapping]]=..., time_series_views: _Optional[_Iterable[_Union[TimeSeriesView, _Mapping]]]=...) -> None:
        ...

class TimeSeriesView(_message.Message):
    __slots__ = ('type', 'capacity_value')
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_VALUE_FIELD_NUMBER: _ClassVar[int]
    type: CapacityType
    capacity_value: DemandValue

    def __init__(self, type: _Optional[_Union[CapacityType, str]]=..., capacity_value: _Optional[_Union[DemandValue, _Mapping]]=...) -> None:
        ...

class CapacityPlan(_message.Message):
    __slots__ = ('name', 'capacity_demand_metadata', 'service_demands', 'reporter', 'state', 'create_time', 'update_time', 'description', 'title')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_DEMAND_METADATA_FIELD_NUMBER: _ClassVar[int]
    SERVICE_DEMANDS_FIELD_NUMBER: _ClassVar[int]
    REPORTER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    capacity_demand_metadata: DemandMetadata
    service_demands: _containers.RepeatedCompositeFieldContainer[ServiceDemand]
    reporter: User
    state: State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    title: str

    def __init__(self, name: _Optional[str]=..., capacity_demand_metadata: _Optional[_Union[DemandMetadata, _Mapping]]=..., service_demands: _Optional[_Iterable[_Union[ServiceDemand, _Mapping]]]=..., reporter: _Optional[_Union[User, _Mapping]]=..., state: _Optional[_Union[State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., title: _Optional[str]=...) -> None:
        ...

class DemandMetadata(_message.Message):
    __slots__ = ('demand_preferences',)
    DEMAND_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    demand_preferences: _containers.RepeatedCompositeFieldContainer[DemandPreference]

    def __init__(self, demand_preferences: _Optional[_Iterable[_Union[DemandPreference, _Mapping]]]=...) -> None:
        ...

class DemandPreference(_message.Message):
    __slots__ = ('preference_id', 'value')
    PREFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    preference_id: str
    value: _resource_pb2_1.Value

    def __init__(self, preference_id: _Optional[str]=..., value: _Optional[_Union[_resource_pb2_1.Value, _Mapping]]=...) -> None:
        ...

class ServiceDemand(_message.Message):
    __slots__ = ('service', 'demand_metadata', 'resource_demands')
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    DEMAND_METADATA_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_DEMANDS_FIELD_NUMBER: _ClassVar[int]
    service: str
    demand_metadata: DemandMetadata
    resource_demands: _containers.RepeatedCompositeFieldContainer[ResourceDemand]

    def __init__(self, service: _Optional[str]=..., demand_metadata: _Optional[_Union[DemandMetadata, _Mapping]]=..., resource_demands: _Optional[_Iterable[_Union[ResourceDemand, _Mapping]]]=...) -> None:
        ...

class ResourceDemand(_message.Message):
    __slots__ = ('id', 'resource_container', 'resource_id', 'location_id', 'state', 'reporter', 'create_time', 'update_time', 'demand_values', 'demand_metadata', 'child_resource_demands')
    ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    REPORTER_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DEMAND_VALUES_FIELD_NUMBER: _ClassVar[int]
    DEMAND_METADATA_FIELD_NUMBER: _ClassVar[int]
    CHILD_RESOURCE_DEMANDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    resource_container: _resource_pb2_1.ResourceContainer
    resource_id: _resource_pb2_1.ResourceIdentifier
    location_id: _location_pb2.LocationIdentifier
    state: State
    reporter: User
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    demand_values: DemandValues
    demand_metadata: DemandMetadata
    child_resource_demands: _containers.RepeatedCompositeFieldContainer[ChildResourceDemand]

    def __init__(self, id: _Optional[str]=..., resource_container: _Optional[_Union[_resource_pb2_1.ResourceContainer, _Mapping]]=..., resource_id: _Optional[_Union[_resource_pb2_1.ResourceIdentifier, _Mapping]]=..., location_id: _Optional[_Union[_location_pb2.LocationIdentifier, _Mapping]]=..., state: _Optional[_Union[State, str]]=..., reporter: _Optional[_Union[User, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., demand_values: _Optional[_Union[DemandValues, _Mapping]]=..., demand_metadata: _Optional[_Union[DemandMetadata, _Mapping]]=..., child_resource_demands: _Optional[_Iterable[_Union[ChildResourceDemand, _Mapping]]]=...) -> None:
        ...

class User(_message.Message):
    __slots__ = ('email',)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str

    def __init__(self, email: _Optional[str]=...) -> None:
        ...

class DemandValues(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[DemandValue]

    def __init__(self, values: _Optional[_Iterable[_Union[DemandValue, _Mapping]]]=...) -> None:
        ...

class DemandValue(_message.Message):
    __slots__ = ('name', 'time_values', 'unit')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TIME_VALUES_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    name: str
    time_values: _containers.RepeatedCompositeFieldContainer[TimeValue]
    unit: _resource_pb2_1.Unit

    def __init__(self, name: _Optional[str]=..., time_values: _Optional[_Iterable[_Union[TimeValue, _Mapping]]]=..., unit: _Optional[_Union[_resource_pb2_1.Unit, str]]=...) -> None:
        ...

class TimeValue(_message.Message):
    __slots__ = ('time', 'value')
    TIME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    time: _timestamp_pb2.Timestamp
    value: float

    def __init__(self, time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., value: _Optional[float]=...) -> None:
        ...

class ChildResourceDemand(_message.Message):
    __slots__ = ('resource_id', 'demand_values', 'demand_metadata')
    RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    DEMAND_VALUES_FIELD_NUMBER: _ClassVar[int]
    DEMAND_METADATA_FIELD_NUMBER: _ClassVar[int]
    resource_id: _resource_pb2_1.ResourceIdentifier
    demand_values: DemandValues
    demand_metadata: DemandMetadata

    def __init__(self, resource_id: _Optional[_Union[_resource_pb2_1.ResourceIdentifier, _Mapping]]=..., demand_values: _Optional[_Union[DemandValues, _Mapping]]=..., demand_metadata: _Optional[_Union[DemandMetadata, _Mapping]]=...) -> None:
        ...