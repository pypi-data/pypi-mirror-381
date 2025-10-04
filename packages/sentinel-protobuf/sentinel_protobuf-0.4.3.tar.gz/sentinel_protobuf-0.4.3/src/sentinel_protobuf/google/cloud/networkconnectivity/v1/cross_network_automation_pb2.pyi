from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.networkconnectivity.v1 import common_pb2 as _common_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import error_details_pb2 as _error_details_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Infrastructure(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INFRASTRUCTURE_UNSPECIFIED: _ClassVar[Infrastructure]
    PSC: _ClassVar[Infrastructure]

class ConnectionErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONNECTION_ERROR_TYPE_UNSPECIFIED: _ClassVar[ConnectionErrorType]
    ERROR_INTERNAL: _ClassVar[ConnectionErrorType]
    ERROR_CONSUMER_SIDE: _ClassVar[ConnectionErrorType]
    ERROR_PRODUCER_SIDE: _ClassVar[ConnectionErrorType]

class IPVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IP_VERSION_UNSPECIFIED: _ClassVar[IPVersion]
    IPV4: _ClassVar[IPVersion]
    IPV6: _ClassVar[IPVersion]
INFRASTRUCTURE_UNSPECIFIED: Infrastructure
PSC: Infrastructure
CONNECTION_ERROR_TYPE_UNSPECIFIED: ConnectionErrorType
ERROR_INTERNAL: ConnectionErrorType
ERROR_CONSUMER_SIDE: ConnectionErrorType
ERROR_PRODUCER_SIDE: ConnectionErrorType
IP_VERSION_UNSPECIFIED: IPVersion
IPV4: IPVersion
IPV6: IPVersion

class ServiceConnectionMap(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'description', 'service_class', 'service_class_uri', 'infrastructure', 'producer_psc_configs', 'consumer_psc_configs', 'consumer_psc_connections', 'token', 'etag')

    class ProducerPscConfig(_message.Message):
        __slots__ = ('service_attachment_uri',)
        SERVICE_ATTACHMENT_URI_FIELD_NUMBER: _ClassVar[int]
        service_attachment_uri: str

        def __init__(self, service_attachment_uri: _Optional[str]=...) -> None:
            ...

    class ConsumerPscConfig(_message.Message):
        __slots__ = ('project', 'network', 'disable_global_access', 'state', 'producer_instance_id', 'service_attachment_ip_address_map', 'consumer_instance_project', 'producer_instance_metadata', 'ip_version')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[ServiceConnectionMap.ConsumerPscConfig.State]
            VALID: _ClassVar[ServiceConnectionMap.ConsumerPscConfig.State]
            CONNECTION_POLICY_MISSING: _ClassVar[ServiceConnectionMap.ConsumerPscConfig.State]
            POLICY_LIMIT_REACHED: _ClassVar[ServiceConnectionMap.ConsumerPscConfig.State]
            CONSUMER_INSTANCE_PROJECT_NOT_ALLOWLISTED: _ClassVar[ServiceConnectionMap.ConsumerPscConfig.State]
        STATE_UNSPECIFIED: ServiceConnectionMap.ConsumerPscConfig.State
        VALID: ServiceConnectionMap.ConsumerPscConfig.State
        CONNECTION_POLICY_MISSING: ServiceConnectionMap.ConsumerPscConfig.State
        POLICY_LIMIT_REACHED: ServiceConnectionMap.ConsumerPscConfig.State
        CONSUMER_INSTANCE_PROJECT_NOT_ALLOWLISTED: ServiceConnectionMap.ConsumerPscConfig.State

        class ServiceAttachmentIpAddressMapEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...

        class ProducerInstanceMetadataEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        PROJECT_FIELD_NUMBER: _ClassVar[int]
        NETWORK_FIELD_NUMBER: _ClassVar[int]
        DISABLE_GLOBAL_ACCESS_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        PRODUCER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        SERVICE_ATTACHMENT_IP_ADDRESS_MAP_FIELD_NUMBER: _ClassVar[int]
        CONSUMER_INSTANCE_PROJECT_FIELD_NUMBER: _ClassVar[int]
        PRODUCER_INSTANCE_METADATA_FIELD_NUMBER: _ClassVar[int]
        IP_VERSION_FIELD_NUMBER: _ClassVar[int]
        project: str
        network: str
        disable_global_access: bool
        state: ServiceConnectionMap.ConsumerPscConfig.State
        producer_instance_id: str
        service_attachment_ip_address_map: _containers.ScalarMap[str, str]
        consumer_instance_project: str
        producer_instance_metadata: _containers.ScalarMap[str, str]
        ip_version: IPVersion

        def __init__(self, project: _Optional[str]=..., network: _Optional[str]=..., disable_global_access: bool=..., state: _Optional[_Union[ServiceConnectionMap.ConsumerPscConfig.State, str]]=..., producer_instance_id: _Optional[str]=..., service_attachment_ip_address_map: _Optional[_Mapping[str, str]]=..., consumer_instance_project: _Optional[str]=..., producer_instance_metadata: _Optional[_Mapping[str, str]]=..., ip_version: _Optional[_Union[IPVersion, str]]=...) -> None:
            ...

    class ConsumerPscConnection(_message.Message):
        __slots__ = ('service_attachment_uri', 'state', 'project', 'network', 'psc_connection_id', 'ip', 'error_type', 'error', 'gce_operation', 'forwarding_rule', 'error_info', 'selected_subnetwork', 'producer_instance_id', 'producer_instance_metadata', 'ip_version')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[ServiceConnectionMap.ConsumerPscConnection.State]
            ACTIVE: _ClassVar[ServiceConnectionMap.ConsumerPscConnection.State]
            FAILED: _ClassVar[ServiceConnectionMap.ConsumerPscConnection.State]
            CREATING: _ClassVar[ServiceConnectionMap.ConsumerPscConnection.State]
            DELETING: _ClassVar[ServiceConnectionMap.ConsumerPscConnection.State]
            CREATE_REPAIRING: _ClassVar[ServiceConnectionMap.ConsumerPscConnection.State]
            DELETE_REPAIRING: _ClassVar[ServiceConnectionMap.ConsumerPscConnection.State]
        STATE_UNSPECIFIED: ServiceConnectionMap.ConsumerPscConnection.State
        ACTIVE: ServiceConnectionMap.ConsumerPscConnection.State
        FAILED: ServiceConnectionMap.ConsumerPscConnection.State
        CREATING: ServiceConnectionMap.ConsumerPscConnection.State
        DELETING: ServiceConnectionMap.ConsumerPscConnection.State
        CREATE_REPAIRING: ServiceConnectionMap.ConsumerPscConnection.State
        DELETE_REPAIRING: ServiceConnectionMap.ConsumerPscConnection.State

        class ProducerInstanceMetadataEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        SERVICE_ATTACHMENT_URI_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        PROJECT_FIELD_NUMBER: _ClassVar[int]
        NETWORK_FIELD_NUMBER: _ClassVar[int]
        PSC_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
        IP_FIELD_NUMBER: _ClassVar[int]
        ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        GCE_OPERATION_FIELD_NUMBER: _ClassVar[int]
        FORWARDING_RULE_FIELD_NUMBER: _ClassVar[int]
        ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
        SELECTED_SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
        PRODUCER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        PRODUCER_INSTANCE_METADATA_FIELD_NUMBER: _ClassVar[int]
        IP_VERSION_FIELD_NUMBER: _ClassVar[int]
        service_attachment_uri: str
        state: ServiceConnectionMap.ConsumerPscConnection.State
        project: str
        network: str
        psc_connection_id: str
        ip: str
        error_type: ConnectionErrorType
        error: _status_pb2.Status
        gce_operation: str
        forwarding_rule: str
        error_info: _error_details_pb2.ErrorInfo
        selected_subnetwork: str
        producer_instance_id: str
        producer_instance_metadata: _containers.ScalarMap[str, str]
        ip_version: IPVersion

        def __init__(self, service_attachment_uri: _Optional[str]=..., state: _Optional[_Union[ServiceConnectionMap.ConsumerPscConnection.State, str]]=..., project: _Optional[str]=..., network: _Optional[str]=..., psc_connection_id: _Optional[str]=..., ip: _Optional[str]=..., error_type: _Optional[_Union[ConnectionErrorType, str]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., gce_operation: _Optional[str]=..., forwarding_rule: _Optional[str]=..., error_info: _Optional[_Union[_error_details_pb2.ErrorInfo, _Mapping]]=..., selected_subnetwork: _Optional[str]=..., producer_instance_id: _Optional[str]=..., producer_instance_metadata: _Optional[_Mapping[str, str]]=..., ip_version: _Optional[_Union[IPVersion, str]]=...) -> None:
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
    SERVICE_CLASS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CLASS_URI_FIELD_NUMBER: _ClassVar[int]
    INFRASTRUCTURE_FIELD_NUMBER: _ClassVar[int]
    PRODUCER_PSC_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_PSC_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    CONSUMER_PSC_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    service_class: str
    service_class_uri: str
    infrastructure: Infrastructure
    producer_psc_configs: _containers.RepeatedCompositeFieldContainer[ServiceConnectionMap.ProducerPscConfig]
    consumer_psc_configs: _containers.RepeatedCompositeFieldContainer[ServiceConnectionMap.ConsumerPscConfig]
    consumer_psc_connections: _containers.RepeatedCompositeFieldContainer[ServiceConnectionMap.ConsumerPscConnection]
    token: str
    etag: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., service_class: _Optional[str]=..., service_class_uri: _Optional[str]=..., infrastructure: _Optional[_Union[Infrastructure, str]]=..., producer_psc_configs: _Optional[_Iterable[_Union[ServiceConnectionMap.ProducerPscConfig, _Mapping]]]=..., consumer_psc_configs: _Optional[_Iterable[_Union[ServiceConnectionMap.ConsumerPscConfig, _Mapping]]]=..., consumer_psc_connections: _Optional[_Iterable[_Union[ServiceConnectionMap.ConsumerPscConnection, _Mapping]]]=..., token: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class ListServiceConnectionMapsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListServiceConnectionMapsResponse(_message.Message):
    __slots__ = ('service_connection_maps', 'next_page_token', 'unreachable')
    SERVICE_CONNECTION_MAPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    service_connection_maps: _containers.RepeatedCompositeFieldContainer[ServiceConnectionMap]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, service_connection_maps: _Optional[_Iterable[_Union[ServiceConnectionMap, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetServiceConnectionMapRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateServiceConnectionMapRequest(_message.Message):
    __slots__ = ('parent', 'service_connection_map_id', 'service_connection_map', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CONNECTION_MAP_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CONNECTION_MAP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    service_connection_map_id: str
    service_connection_map: ServiceConnectionMap
    request_id: str

    def __init__(self, parent: _Optional[str]=..., service_connection_map_id: _Optional[str]=..., service_connection_map: _Optional[_Union[ServiceConnectionMap, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateServiceConnectionMapRequest(_message.Message):
    __slots__ = ('update_mask', 'service_connection_map', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CONNECTION_MAP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    service_connection_map: ServiceConnectionMap
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., service_connection_map: _Optional[_Union[ServiceConnectionMap, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteServiceConnectionMapRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    etag: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class ServiceConnectionPolicy(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'description', 'network', 'service_class', 'infrastructure', 'psc_config', 'psc_connections', 'etag')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ServiceConnectionPolicy.State]
        ACTIVE: _ClassVar[ServiceConnectionPolicy.State]
        FAILED: _ClassVar[ServiceConnectionPolicy.State]
        CREATING: _ClassVar[ServiceConnectionPolicy.State]
        DELETING: _ClassVar[ServiceConnectionPolicy.State]
        CREATE_REPAIRING: _ClassVar[ServiceConnectionPolicy.State]
        DELETE_REPAIRING: _ClassVar[ServiceConnectionPolicy.State]
    STATE_UNSPECIFIED: ServiceConnectionPolicy.State
    ACTIVE: ServiceConnectionPolicy.State
    FAILED: ServiceConnectionPolicy.State
    CREATING: ServiceConnectionPolicy.State
    DELETING: ServiceConnectionPolicy.State
    CREATE_REPAIRING: ServiceConnectionPolicy.State
    DELETE_REPAIRING: ServiceConnectionPolicy.State

    class PscConfig(_message.Message):
        __slots__ = ('subnetworks', 'limit', 'producer_instance_location', 'allowed_google_producers_resource_hierarchy_level')

        class ProducerInstanceLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PRODUCER_INSTANCE_LOCATION_UNSPECIFIED: _ClassVar[ServiceConnectionPolicy.PscConfig.ProducerInstanceLocation]
            CUSTOM_RESOURCE_HIERARCHY_LEVELS: _ClassVar[ServiceConnectionPolicy.PscConfig.ProducerInstanceLocation]
        PRODUCER_INSTANCE_LOCATION_UNSPECIFIED: ServiceConnectionPolicy.PscConfig.ProducerInstanceLocation
        CUSTOM_RESOURCE_HIERARCHY_LEVELS: ServiceConnectionPolicy.PscConfig.ProducerInstanceLocation
        SUBNETWORKS_FIELD_NUMBER: _ClassVar[int]
        LIMIT_FIELD_NUMBER: _ClassVar[int]
        PRODUCER_INSTANCE_LOCATION_FIELD_NUMBER: _ClassVar[int]
        ALLOWED_GOOGLE_PRODUCERS_RESOURCE_HIERARCHY_LEVEL_FIELD_NUMBER: _ClassVar[int]
        subnetworks: _containers.RepeatedScalarFieldContainer[str]
        limit: int
        producer_instance_location: ServiceConnectionPolicy.PscConfig.ProducerInstanceLocation
        allowed_google_producers_resource_hierarchy_level: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, subnetworks: _Optional[_Iterable[str]]=..., limit: _Optional[int]=..., producer_instance_location: _Optional[_Union[ServiceConnectionPolicy.PscConfig.ProducerInstanceLocation, str]]=..., allowed_google_producers_resource_hierarchy_level: _Optional[_Iterable[str]]=...) -> None:
            ...

    class PscConnection(_message.Message):
        __slots__ = ('state', 'consumer_forwarding_rule', 'consumer_address', 'error_type', 'error', 'gce_operation', 'consumer_target_project', 'psc_connection_id', 'error_info', 'selected_subnetwork', 'producer_instance_id', 'producer_instance_metadata', 'service_class', 'ip_version')

        class ProducerInstanceMetadataEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        STATE_FIELD_NUMBER: _ClassVar[int]
        CONSUMER_FORWARDING_RULE_FIELD_NUMBER: _ClassVar[int]
        CONSUMER_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
        ERROR_FIELD_NUMBER: _ClassVar[int]
        GCE_OPERATION_FIELD_NUMBER: _ClassVar[int]
        CONSUMER_TARGET_PROJECT_FIELD_NUMBER: _ClassVar[int]
        PSC_CONNECTION_ID_FIELD_NUMBER: _ClassVar[int]
        ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
        SELECTED_SUBNETWORK_FIELD_NUMBER: _ClassVar[int]
        PRODUCER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
        PRODUCER_INSTANCE_METADATA_FIELD_NUMBER: _ClassVar[int]
        SERVICE_CLASS_FIELD_NUMBER: _ClassVar[int]
        IP_VERSION_FIELD_NUMBER: _ClassVar[int]
        state: ServiceConnectionPolicy.State
        consumer_forwarding_rule: str
        consumer_address: str
        error_type: ConnectionErrorType
        error: _status_pb2.Status
        gce_operation: str
        consumer_target_project: str
        psc_connection_id: str
        error_info: _error_details_pb2.ErrorInfo
        selected_subnetwork: str
        producer_instance_id: str
        producer_instance_metadata: _containers.ScalarMap[str, str]
        service_class: str
        ip_version: IPVersion

        def __init__(self, state: _Optional[_Union[ServiceConnectionPolicy.State, str]]=..., consumer_forwarding_rule: _Optional[str]=..., consumer_address: _Optional[str]=..., error_type: _Optional[_Union[ConnectionErrorType, str]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., gce_operation: _Optional[str]=..., consumer_target_project: _Optional[str]=..., psc_connection_id: _Optional[str]=..., error_info: _Optional[_Union[_error_details_pb2.ErrorInfo, _Mapping]]=..., selected_subnetwork: _Optional[str]=..., producer_instance_id: _Optional[str]=..., producer_instance_metadata: _Optional[_Mapping[str, str]]=..., service_class: _Optional[str]=..., ip_version: _Optional[_Union[IPVersion, str]]=...) -> None:
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
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CLASS_FIELD_NUMBER: _ClassVar[int]
    INFRASTRUCTURE_FIELD_NUMBER: _ClassVar[int]
    PSC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PSC_CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    network: str
    service_class: str
    infrastructure: Infrastructure
    psc_config: ServiceConnectionPolicy.PscConfig
    psc_connections: _containers.RepeatedCompositeFieldContainer[ServiceConnectionPolicy.PscConnection]
    etag: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., network: _Optional[str]=..., service_class: _Optional[str]=..., infrastructure: _Optional[_Union[Infrastructure, str]]=..., psc_config: _Optional[_Union[ServiceConnectionPolicy.PscConfig, _Mapping]]=..., psc_connections: _Optional[_Iterable[_Union[ServiceConnectionPolicy.PscConnection, _Mapping]]]=..., etag: _Optional[str]=...) -> None:
        ...

class ListServiceConnectionPoliciesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListServiceConnectionPoliciesResponse(_message.Message):
    __slots__ = ('service_connection_policies', 'next_page_token', 'unreachable')
    SERVICE_CONNECTION_POLICIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    service_connection_policies: _containers.RepeatedCompositeFieldContainer[ServiceConnectionPolicy]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, service_connection_policies: _Optional[_Iterable[_Union[ServiceConnectionPolicy, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetServiceConnectionPolicyRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateServiceConnectionPolicyRequest(_message.Message):
    __slots__ = ('parent', 'service_connection_policy_id', 'service_connection_policy', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CONNECTION_POLICY_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CONNECTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    service_connection_policy_id: str
    service_connection_policy: ServiceConnectionPolicy
    request_id: str

    def __init__(self, parent: _Optional[str]=..., service_connection_policy_id: _Optional[str]=..., service_connection_policy: _Optional[_Union[ServiceConnectionPolicy, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateServiceConnectionPolicyRequest(_message.Message):
    __slots__ = ('update_mask', 'service_connection_policy', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CONNECTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    service_connection_policy: ServiceConnectionPolicy
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., service_connection_policy: _Optional[_Union[ServiceConnectionPolicy, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteServiceConnectionPolicyRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    etag: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class ServiceClass(_message.Message):
    __slots__ = ('name', 'service_class', 'create_time', 'update_time', 'labels', 'description', 'etag')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CLASS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    service_class: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    etag: str

    def __init__(self, name: _Optional[str]=..., service_class: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class ListServiceClassesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListServiceClassesResponse(_message.Message):
    __slots__ = ('service_classes', 'next_page_token', 'unreachable')
    SERVICE_CLASSES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    service_classes: _containers.RepeatedCompositeFieldContainer[ServiceClass]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, service_classes: _Optional[_Iterable[_Union[ServiceClass, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetServiceClassRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateServiceClassRequest(_message.Message):
    __slots__ = ('update_mask', 'service_class', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CLASS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    service_class: ServiceClass
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., service_class: _Optional[_Union[ServiceClass, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteServiceClassRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    etag: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class ServiceConnectionToken(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'description', 'network', 'token', 'expire_time', 'etag')

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
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    description: str
    network: str
    token: str
    expire_time: _timestamp_pb2.Timestamp
    etag: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., description: _Optional[str]=..., network: _Optional[str]=..., token: _Optional[str]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=...) -> None:
        ...

class ListServiceConnectionTokensRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListServiceConnectionTokensResponse(_message.Message):
    __slots__ = ('service_connection_tokens', 'next_page_token', 'unreachable')
    SERVICE_CONNECTION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    service_connection_tokens: _containers.RepeatedCompositeFieldContainer[ServiceConnectionToken]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, service_connection_tokens: _Optional[_Iterable[_Union[ServiceConnectionToken, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetServiceConnectionTokenRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateServiceConnectionTokenRequest(_message.Message):
    __slots__ = ('parent', 'service_connection_token_id', 'service_connection_token', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CONNECTION_TOKEN_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_CONNECTION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    service_connection_token_id: str
    service_connection_token: ServiceConnectionToken
    request_id: str

    def __init__(self, parent: _Optional[str]=..., service_connection_token_id: _Optional[str]=..., service_connection_token: _Optional[_Union[ServiceConnectionToken, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteServiceConnectionTokenRequest(_message.Message):
    __slots__ = ('name', 'request_id', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str
    etag: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...