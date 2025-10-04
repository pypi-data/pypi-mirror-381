from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ServiceLbPolicy(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'description', 'load_balancing_algorithm', 'auto_capacity_drain', 'failover_config', 'isolation_config')

    class LoadBalancingAlgorithm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOAD_BALANCING_ALGORITHM_UNSPECIFIED: _ClassVar[ServiceLbPolicy.LoadBalancingAlgorithm]
        SPRAY_TO_WORLD: _ClassVar[ServiceLbPolicy.LoadBalancingAlgorithm]
        SPRAY_TO_REGION: _ClassVar[ServiceLbPolicy.LoadBalancingAlgorithm]
        WATERFALL_BY_REGION: _ClassVar[ServiceLbPolicy.LoadBalancingAlgorithm]
        WATERFALL_BY_ZONE: _ClassVar[ServiceLbPolicy.LoadBalancingAlgorithm]
    LOAD_BALANCING_ALGORITHM_UNSPECIFIED: ServiceLbPolicy.LoadBalancingAlgorithm
    SPRAY_TO_WORLD: ServiceLbPolicy.LoadBalancingAlgorithm
    SPRAY_TO_REGION: ServiceLbPolicy.LoadBalancingAlgorithm
    WATERFALL_BY_REGION: ServiceLbPolicy.LoadBalancingAlgorithm
    WATERFALL_BY_ZONE: ServiceLbPolicy.LoadBalancingAlgorithm

    class IsolationGranularity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ISOLATION_GRANULARITY_UNSPECIFIED: _ClassVar[ServiceLbPolicy.IsolationGranularity]
        REGION: _ClassVar[ServiceLbPolicy.IsolationGranularity]
    ISOLATION_GRANULARITY_UNSPECIFIED: ServiceLbPolicy.IsolationGranularity
    REGION: ServiceLbPolicy.IsolationGranularity

    class IsolationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ISOLATION_MODE_UNSPECIFIED: _ClassVar[ServiceLbPolicy.IsolationMode]
        NEAREST: _ClassVar[ServiceLbPolicy.IsolationMode]
        STRICT: _ClassVar[ServiceLbPolicy.IsolationMode]
    ISOLATION_MODE_UNSPECIFIED: ServiceLbPolicy.IsolationMode
    NEAREST: ServiceLbPolicy.IsolationMode
    STRICT: ServiceLbPolicy.IsolationMode

    class AutoCapacityDrain(_message.Message):
        __slots__ = ('enable',)
        ENABLE_FIELD_NUMBER: _ClassVar[int]
        enable: bool

        def __init__(self, enable: bool=...) -> None:
            ...

    class FailoverConfig(_message.Message):
        __slots__ = ('failover_health_threshold',)
        FAILOVER_HEALTH_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
        failover_health_threshold: int

        def __init__(self, failover_health_threshold: _Optional[int]=...) -> None:
            ...

    class IsolationConfig(_message.Message):
        __slots__ = ('isolation_granularity', 'isolation_mode')
        ISOLATION_GRANULARITY_FIELD_NUMBER: _ClassVar[int]
        ISOLATION_MODE_FIELD_NUMBER: _ClassVar[int]
        isolation_granularity: ServiceLbPolicy.IsolationGranularity
        isolation_mode: ServiceLbPolicy.IsolationMode

        def __init__(self, isolation_granularity: _Optional[_Union[ServiceLbPolicy.IsolationGranularity, str]]=..., isolation_mode: _Optional[_Union[ServiceLbPolicy.IsolationMode, str]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOAD_BALANCING_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    AUTO_CAPACITY_DRAIN_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ISOLATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    load_balancing_algorithm: ServiceLbPolicy.LoadBalancingAlgorithm
    auto_capacity_drain: ServiceLbPolicy.AutoCapacityDrain
    failover_config: ServiceLbPolicy.FailoverConfig
    isolation_config: ServiceLbPolicy.IsolationConfig

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., load_balancing_algorithm: _Optional[_Union[ServiceLbPolicy.LoadBalancingAlgorithm, str]]=..., auto_capacity_drain: _Optional[_Union[ServiceLbPolicy.AutoCapacityDrain, _Mapping]]=..., failover_config: _Optional[_Union[ServiceLbPolicy.FailoverConfig, _Mapping]]=..., isolation_config: _Optional[_Union[ServiceLbPolicy.IsolationConfig, _Mapping]]=...) -> None:
        ...

class ListServiceLbPoliciesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListServiceLbPoliciesResponse(_message.Message):
    __slots__ = ('service_lb_policies', 'next_page_token', 'unreachable')
    SERVICE_LB_POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    service_lb_policies: _containers.RepeatedCompositeFieldContainer[ServiceLbPolicy]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, service_lb_policies: _Optional[_Iterable[_Union[ServiceLbPolicy, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetServiceLbPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateServiceLbPolicyRequest(_message.Message):
    __slots__ = ('parent', 'service_lb_policy_id', 'service_lb_policy')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LB_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LB_POLICY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    service_lb_policy_id: str
    service_lb_policy: ServiceLbPolicy

    def __init__(self, parent: _Optional[str]=..., service_lb_policy_id: _Optional[str]=..., service_lb_policy: _Optional[_Union[ServiceLbPolicy, _Mapping]]=...) -> None:
        ...

class UpdateServiceLbPolicyRequest(_message.Message):
    __slots__ = ('update_mask', 'service_lb_policy')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SERVICE_LB_POLICY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    service_lb_policy: ServiceLbPolicy

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., service_lb_policy: _Optional[_Union[ServiceLbPolicy, _Mapping]]=...) -> None:
        ...

class DeleteServiceLbPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...