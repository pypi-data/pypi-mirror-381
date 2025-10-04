from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.networkconnectivity.v1 import common_pb2 as _common_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MulticloudDataTransferConfig(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'etag', 'description', 'destinations_count', 'destinations_active_count', 'services', 'uid')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class ServicesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: StateTimeline

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[StateTimeline, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_ACTIVE_COUNT_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    etag: str
    description: str
    destinations_count: int
    destinations_active_count: int
    services: _containers.MessageMap[str, StateTimeline]
    uid: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., description: _Optional[str]=..., destinations_count: _Optional[int]=..., destinations_active_count: _Optional[int]=..., services: _Optional[_Mapping[str, StateTimeline]]=..., uid: _Optional[str]=...) -> None:
        ...

class ListMulticloudDataTransferConfigsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by', 'return_partial_success')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    RETURN_PARTIAL_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    return_partial_success: bool

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., return_partial_success: bool=...) -> None:
        ...

class ListMulticloudDataTransferConfigsResponse(_message.Message):
    __slots__ = ('multicloud_data_transfer_configs', 'next_page_token', 'unreachable')
    MULTICLOUD_DATA_TRANSFER_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    multicloud_data_transfer_configs: _containers.RepeatedCompositeFieldContainer[MulticloudDataTransferConfig]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, multicloud_data_transfer_configs: _Optional[_Iterable[_Union[MulticloudDataTransferConfig, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetMulticloudDataTransferConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateMulticloudDataTransferConfigRequest(_message.Message):
    __slots__ = ('parent', 'multicloud_data_transfer_config_id', 'multicloud_data_transfer_config', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MULTICLOUD_DATA_TRANSFER_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    MULTICLOUD_DATA_TRANSFER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    multicloud_data_transfer_config_id: str
    multicloud_data_transfer_config: MulticloudDataTransferConfig
    request_id: str

    def __init__(self, parent: _Optional[str]=..., multicloud_data_transfer_config_id: _Optional[str]=..., multicloud_data_transfer_config: _Optional[_Union[MulticloudDataTransferConfig, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateMulticloudDataTransferConfigRequest(_message.Message):
    __slots__ = ('update_mask', 'multicloud_data_transfer_config', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    MULTICLOUD_DATA_TRANSFER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    multicloud_data_transfer_config: MulticloudDataTransferConfig
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., multicloud_data_transfer_config: _Optional[_Union[MulticloudDataTransferConfig, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteMulticloudDataTransferConfigRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    etag: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class Destination(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'etag', 'description', 'ip_prefix', 'endpoints', 'state_timeline', 'uid')

    class DestinationEndpoint(_message.Message):
        __slots__ = ('asn', 'csp', 'state', 'update_time')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[Destination.DestinationEndpoint.State]
            VALID: _ClassVar[Destination.DestinationEndpoint.State]
            INVALID: _ClassVar[Destination.DestinationEndpoint.State]
        STATE_UNSPECIFIED: Destination.DestinationEndpoint.State
        VALID: Destination.DestinationEndpoint.State
        INVALID: Destination.DestinationEndpoint.State
        ASN_FIELD_NUMBER: _ClassVar[int]
        CSP_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        asn: int
        csp: str
        state: Destination.DestinationEndpoint.State
        update_time: _timestamp_pb2.Timestamp

        def __init__(self, asn: _Optional[int]=..., csp: _Optional[str]=..., state: _Optional[_Union[Destination.DestinationEndpoint.State, str]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
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
    ETAG_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IP_PREFIX_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    STATE_TIMELINE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    etag: str
    description: str
    ip_prefix: str
    endpoints: _containers.RepeatedCompositeFieldContainer[Destination.DestinationEndpoint]
    state_timeline: StateTimeline
    uid: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., description: _Optional[str]=..., ip_prefix: _Optional[str]=..., endpoints: _Optional[_Iterable[_Union[Destination.DestinationEndpoint, _Mapping]]]=..., state_timeline: _Optional[_Union[StateTimeline, _Mapping]]=..., uid: _Optional[str]=...) -> None:
        ...

class ListDestinationsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by', 'return_partial_success')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    RETURN_PARTIAL_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    return_partial_success: bool

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., return_partial_success: bool=...) -> None:
        ...

class ListDestinationsResponse(_message.Message):
    __slots__ = ('destinations', 'next_page_token', 'unreachable')
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    destinations: _containers.RepeatedCompositeFieldContainer[Destination]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, destinations: _Optional[_Iterable[_Union[Destination, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetDestinationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateDestinationRequest(_message.Message):
    __slots__ = ('parent', 'destination_id', 'destination', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    destination_id: str
    destination: Destination
    request_id: str

    def __init__(self, parent: _Optional[str]=..., destination_id: _Optional[str]=..., destination: _Optional[_Union[Destination, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateDestinationRequest(_message.Message):
    __slots__ = ('update_mask', 'destination', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    destination: Destination
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., destination: _Optional[_Union[Destination, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteDestinationRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    etag: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class StateTimeline(_message.Message):
    __slots__ = ('states',)

    class StateMetadata(_message.Message):
        __slots__ = ('state', 'effective_time')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[StateTimeline.StateMetadata.State]
            ADDING: _ClassVar[StateTimeline.StateMetadata.State]
            ACTIVE: _ClassVar[StateTimeline.StateMetadata.State]
            DELETING: _ClassVar[StateTimeline.StateMetadata.State]
            SUSPENDING: _ClassVar[StateTimeline.StateMetadata.State]
            SUSPENDED: _ClassVar[StateTimeline.StateMetadata.State]
        STATE_UNSPECIFIED: StateTimeline.StateMetadata.State
        ADDING: StateTimeline.StateMetadata.State
        ACTIVE: StateTimeline.StateMetadata.State
        DELETING: StateTimeline.StateMetadata.State
        SUSPENDING: StateTimeline.StateMetadata.State
        SUSPENDED: StateTimeline.StateMetadata.State
        STATE_FIELD_NUMBER: _ClassVar[int]
        EFFECTIVE_TIME_FIELD_NUMBER: _ClassVar[int]
        state: StateTimeline.StateMetadata.State
        effective_time: _timestamp_pb2.Timestamp

        def __init__(self, state: _Optional[_Union[StateTimeline.StateMetadata.State, str]]=..., effective_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...
    STATES_FIELD_NUMBER: _ClassVar[int]
    states: _containers.RepeatedCompositeFieldContainer[StateTimeline.StateMetadata]

    def __init__(self, states: _Optional[_Iterable[_Union[StateTimeline.StateMetadata, _Mapping]]]=...) -> None:
        ...

class MulticloudDataTransferSupportedService(_message.Message):
    __slots__ = ('name', 'service_configs')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    service_configs: _containers.RepeatedCompositeFieldContainer[ServiceConfig]

    def __init__(self, name: _Optional[str]=..., service_configs: _Optional[_Iterable[_Union[ServiceConfig, _Mapping]]]=...) -> None:
        ...

class ServiceConfig(_message.Message):
    __slots__ = ('eligibility_criteria', 'support_end_time')

    class EligibilityCriteria(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ELIGIBILITY_CRITERIA_UNSPECIFIED: _ClassVar[ServiceConfig.EligibilityCriteria]
        NETWORK_SERVICE_TIER_PREMIUM_ONLY: _ClassVar[ServiceConfig.EligibilityCriteria]
        NETWORK_SERVICE_TIER_STANDARD_ONLY: _ClassVar[ServiceConfig.EligibilityCriteria]
        REQUEST_ENDPOINT_REGIONAL_ENDPOINT_ONLY: _ClassVar[ServiceConfig.EligibilityCriteria]
    ELIGIBILITY_CRITERIA_UNSPECIFIED: ServiceConfig.EligibilityCriteria
    NETWORK_SERVICE_TIER_PREMIUM_ONLY: ServiceConfig.EligibilityCriteria
    NETWORK_SERVICE_TIER_STANDARD_ONLY: ServiceConfig.EligibilityCriteria
    REQUEST_ENDPOINT_REGIONAL_ENDPOINT_ONLY: ServiceConfig.EligibilityCriteria
    ELIGIBILITY_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_END_TIME_FIELD_NUMBER: _ClassVar[int]
    eligibility_criteria: ServiceConfig.EligibilityCriteria
    support_end_time: _timestamp_pb2.Timestamp

    def __init__(self, eligibility_criteria: _Optional[_Union[ServiceConfig.EligibilityCriteria, str]]=..., support_end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetMulticloudDataTransferSupportedServiceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListMulticloudDataTransferSupportedServicesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListMulticloudDataTransferSupportedServicesResponse(_message.Message):
    __slots__ = ('multicloud_data_transfer_supported_services', 'next_page_token')
    MULTICLOUD_DATA_TRANSFER_SUPPORTED_SERVICES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    multicloud_data_transfer_supported_services: _containers.RepeatedCompositeFieldContainer[MulticloudDataTransferSupportedService]
    next_page_token: str

    def __init__(self, multicloud_data_transfer_supported_services: _Optional[_Iterable[_Union[MulticloudDataTransferSupportedService, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...