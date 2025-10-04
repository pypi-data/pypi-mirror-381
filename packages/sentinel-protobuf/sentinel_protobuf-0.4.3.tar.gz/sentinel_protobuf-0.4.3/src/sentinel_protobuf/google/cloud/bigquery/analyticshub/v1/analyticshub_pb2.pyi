from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.bigquery.analyticshub.v1 import pubsub_pb2 as _pubsub_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DiscoveryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DISCOVERY_TYPE_UNSPECIFIED: _ClassVar[DiscoveryType]
    DISCOVERY_TYPE_PRIVATE: _ClassVar[DiscoveryType]
    DISCOVERY_TYPE_PUBLIC: _ClassVar[DiscoveryType]

class SharedResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SHARED_RESOURCE_TYPE_UNSPECIFIED: _ClassVar[SharedResourceType]
    BIGQUERY_DATASET: _ClassVar[SharedResourceType]
    PUBSUB_TOPIC: _ClassVar[SharedResourceType]
DISCOVERY_TYPE_UNSPECIFIED: DiscoveryType
DISCOVERY_TYPE_PRIVATE: DiscoveryType
DISCOVERY_TYPE_PUBLIC: DiscoveryType
SHARED_RESOURCE_TYPE_UNSPECIFIED: SharedResourceType
BIGQUERY_DATASET: SharedResourceType
PUBSUB_TOPIC: SharedResourceType

class DataExchange(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'primary_contact', 'documentation', 'listing_count', 'icon', 'sharing_environment_config', 'discovery_type', 'log_linked_dataset_query_user_email')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_CONTACT_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    LISTING_COUNT_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    SHARING_ENVIRONMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOG_LINKED_DATASET_QUERY_USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    primary_contact: str
    documentation: str
    listing_count: int
    icon: bytes
    sharing_environment_config: SharingEnvironmentConfig
    discovery_type: DiscoveryType
    log_linked_dataset_query_user_email: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., primary_contact: _Optional[str]=..., documentation: _Optional[str]=..., listing_count: _Optional[int]=..., icon: _Optional[bytes]=..., sharing_environment_config: _Optional[_Union[SharingEnvironmentConfig, _Mapping]]=..., discovery_type: _Optional[_Union[DiscoveryType, str]]=..., log_linked_dataset_query_user_email: bool=...) -> None:
        ...

class QueryTemplate(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'proposer', 'primary_contact', 'documentation', 'state', 'routine', 'create_time', 'update_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[QueryTemplate.State]
        DRAFTED: _ClassVar[QueryTemplate.State]
        PENDING: _ClassVar[QueryTemplate.State]
        DELETED: _ClassVar[QueryTemplate.State]
        APPROVED: _ClassVar[QueryTemplate.State]
    STATE_UNSPECIFIED: QueryTemplate.State
    DRAFTED: QueryTemplate.State
    PENDING: QueryTemplate.State
    DELETED: QueryTemplate.State
    APPROVED: QueryTemplate.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PROPOSER_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_CONTACT_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ROUTINE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    proposer: str
    primary_contact: str
    documentation: str
    state: QueryTemplate.State
    routine: Routine
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., proposer: _Optional[str]=..., primary_contact: _Optional[str]=..., documentation: _Optional[str]=..., state: _Optional[_Union[QueryTemplate.State, str]]=..., routine: _Optional[_Union[Routine, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Routine(_message.Message):
    __slots__ = ('routine_type', 'definition_body')

    class RoutineType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ROUTINE_TYPE_UNSPECIFIED: _ClassVar[Routine.RoutineType]
        TABLE_VALUED_FUNCTION: _ClassVar[Routine.RoutineType]
    ROUTINE_TYPE_UNSPECIFIED: Routine.RoutineType
    TABLE_VALUED_FUNCTION: Routine.RoutineType
    ROUTINE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_BODY_FIELD_NUMBER: _ClassVar[int]
    routine_type: Routine.RoutineType
    definition_body: str

    def __init__(self, routine_type: _Optional[_Union[Routine.RoutineType, str]]=..., definition_body: _Optional[str]=...) -> None:
        ...

class CreateQueryTemplateRequest(_message.Message):
    __slots__ = ('parent', 'query_template_id', 'query_template')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    QUERY_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    query_template_id: str
    query_template: QueryTemplate

    def __init__(self, parent: _Optional[str]=..., query_template_id: _Optional[str]=..., query_template: _Optional[_Union[QueryTemplate, _Mapping]]=...) -> None:
        ...

class GetQueryTemplateRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListQueryTemplatesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListQueryTemplatesResponse(_message.Message):
    __slots__ = ('query_templates', 'next_page_token')
    QUERY_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    query_templates: _containers.RepeatedCompositeFieldContainer[QueryTemplate]
    next_page_token: str

    def __init__(self, query_templates: _Optional[_Iterable[_Union[QueryTemplate, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateQueryTemplateRequest(_message.Message):
    __slots__ = ('update_mask', 'query_template')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    QUERY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    query_template: QueryTemplate

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., query_template: _Optional[_Union[QueryTemplate, _Mapping]]=...) -> None:
        ...

class DeleteQueryTemplateRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class SubmitQueryTemplateRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ApproveQueryTemplateRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class SharingEnvironmentConfig(_message.Message):
    __slots__ = ('default_exchange_config', 'dcr_exchange_config')

    class DefaultExchangeConfig(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class DcrExchangeConfig(_message.Message):
        __slots__ = ('single_selected_resource_sharing_restriction', 'single_linked_dataset_per_cleanroom')
        SINGLE_SELECTED_RESOURCE_SHARING_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
        SINGLE_LINKED_DATASET_PER_CLEANROOM_FIELD_NUMBER: _ClassVar[int]
        single_selected_resource_sharing_restriction: bool
        single_linked_dataset_per_cleanroom: bool

        def __init__(self, single_selected_resource_sharing_restriction: bool=..., single_linked_dataset_per_cleanroom: bool=...) -> None:
            ...
    DEFAULT_EXCHANGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DCR_EXCHANGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    default_exchange_config: SharingEnvironmentConfig.DefaultExchangeConfig
    dcr_exchange_config: SharingEnvironmentConfig.DcrExchangeConfig

    def __init__(self, default_exchange_config: _Optional[_Union[SharingEnvironmentConfig.DefaultExchangeConfig, _Mapping]]=..., dcr_exchange_config: _Optional[_Union[SharingEnvironmentConfig.DcrExchangeConfig, _Mapping]]=...) -> None:
        ...

class DataProvider(_message.Message):
    __slots__ = ('name', 'primary_contact')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_CONTACT_FIELD_NUMBER: _ClassVar[int]
    name: str
    primary_contact: str

    def __init__(self, name: _Optional[str]=..., primary_contact: _Optional[str]=...) -> None:
        ...

class Publisher(_message.Message):
    __slots__ = ('name', 'primary_contact')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_CONTACT_FIELD_NUMBER: _ClassVar[int]
    name: str
    primary_contact: str

    def __init__(self, name: _Optional[str]=..., primary_contact: _Optional[str]=...) -> None:
        ...

class DestinationDatasetReference(_message.Message):
    __slots__ = ('dataset_id', 'project_id')
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    dataset_id: str
    project_id: str

    def __init__(self, dataset_id: _Optional[str]=..., project_id: _Optional[str]=...) -> None:
        ...

class DestinationDataset(_message.Message):
    __slots__ = ('dataset_reference', 'friendly_name', 'description', 'labels', 'location', 'replica_locations')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    DATASET_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    FRIENDLY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    REPLICA_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    dataset_reference: DestinationDatasetReference
    friendly_name: _wrappers_pb2.StringValue
    description: _wrappers_pb2.StringValue
    labels: _containers.ScalarMap[str, str]
    location: str
    replica_locations: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, dataset_reference: _Optional[_Union[DestinationDatasetReference, _Mapping]]=..., friendly_name: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]]=..., description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., location: _Optional[str]=..., replica_locations: _Optional[_Iterable[str]]=...) -> None:
        ...

class DestinationPubSubSubscription(_message.Message):
    __slots__ = ('pubsub_subscription',)
    PUBSUB_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    pubsub_subscription: _pubsub_pb2.PubSubSubscription

    def __init__(self, pubsub_subscription: _Optional[_Union[_pubsub_pb2.PubSubSubscription, _Mapping]]=...) -> None:
        ...

class Listing(_message.Message):
    __slots__ = ('bigquery_dataset', 'pubsub_topic', 'name', 'display_name', 'description', 'primary_contact', 'documentation', 'state', 'icon', 'data_provider', 'categories', 'publisher', 'request_access', 'restricted_export_config', 'discovery_type', 'resource_type', 'commercial_info', 'log_linked_dataset_query_user_email', 'allow_only_metadata_sharing')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Listing.State]
        ACTIVE: _ClassVar[Listing.State]
    STATE_UNSPECIFIED: Listing.State
    ACTIVE: Listing.State

    class Category(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CATEGORY_UNSPECIFIED: _ClassVar[Listing.Category]
        CATEGORY_OTHERS: _ClassVar[Listing.Category]
        CATEGORY_ADVERTISING_AND_MARKETING: _ClassVar[Listing.Category]
        CATEGORY_COMMERCE: _ClassVar[Listing.Category]
        CATEGORY_CLIMATE_AND_ENVIRONMENT: _ClassVar[Listing.Category]
        CATEGORY_DEMOGRAPHICS: _ClassVar[Listing.Category]
        CATEGORY_ECONOMICS: _ClassVar[Listing.Category]
        CATEGORY_EDUCATION: _ClassVar[Listing.Category]
        CATEGORY_ENERGY: _ClassVar[Listing.Category]
        CATEGORY_FINANCIAL: _ClassVar[Listing.Category]
        CATEGORY_GAMING: _ClassVar[Listing.Category]
        CATEGORY_GEOSPATIAL: _ClassVar[Listing.Category]
        CATEGORY_HEALTHCARE_AND_LIFE_SCIENCE: _ClassVar[Listing.Category]
        CATEGORY_MEDIA: _ClassVar[Listing.Category]
        CATEGORY_PUBLIC_SECTOR: _ClassVar[Listing.Category]
        CATEGORY_RETAIL: _ClassVar[Listing.Category]
        CATEGORY_SPORTS: _ClassVar[Listing.Category]
        CATEGORY_SCIENCE_AND_RESEARCH: _ClassVar[Listing.Category]
        CATEGORY_TRANSPORTATION_AND_LOGISTICS: _ClassVar[Listing.Category]
        CATEGORY_TRAVEL_AND_TOURISM: _ClassVar[Listing.Category]
        CATEGORY_GOOGLE_EARTH_ENGINE: _ClassVar[Listing.Category]
    CATEGORY_UNSPECIFIED: Listing.Category
    CATEGORY_OTHERS: Listing.Category
    CATEGORY_ADVERTISING_AND_MARKETING: Listing.Category
    CATEGORY_COMMERCE: Listing.Category
    CATEGORY_CLIMATE_AND_ENVIRONMENT: Listing.Category
    CATEGORY_DEMOGRAPHICS: Listing.Category
    CATEGORY_ECONOMICS: Listing.Category
    CATEGORY_EDUCATION: Listing.Category
    CATEGORY_ENERGY: Listing.Category
    CATEGORY_FINANCIAL: Listing.Category
    CATEGORY_GAMING: Listing.Category
    CATEGORY_GEOSPATIAL: Listing.Category
    CATEGORY_HEALTHCARE_AND_LIFE_SCIENCE: Listing.Category
    CATEGORY_MEDIA: Listing.Category
    CATEGORY_PUBLIC_SECTOR: Listing.Category
    CATEGORY_RETAIL: Listing.Category
    CATEGORY_SPORTS: Listing.Category
    CATEGORY_SCIENCE_AND_RESEARCH: Listing.Category
    CATEGORY_TRANSPORTATION_AND_LOGISTICS: Listing.Category
    CATEGORY_TRAVEL_AND_TOURISM: Listing.Category
    CATEGORY_GOOGLE_EARTH_ENGINE: Listing.Category

    class BigQueryDatasetSource(_message.Message):
        __slots__ = ('dataset', 'selected_resources', 'restricted_export_policy', 'replica_locations', 'effective_replicas')

        class SelectedResource(_message.Message):
            __slots__ = ('table', 'routine')
            TABLE_FIELD_NUMBER: _ClassVar[int]
            ROUTINE_FIELD_NUMBER: _ClassVar[int]
            table: str
            routine: str

            def __init__(self, table: _Optional[str]=..., routine: _Optional[str]=...) -> None:
                ...

        class RestrictedExportPolicy(_message.Message):
            __slots__ = ('enabled', 'restrict_direct_table_access', 'restrict_query_result')
            ENABLED_FIELD_NUMBER: _ClassVar[int]
            RESTRICT_DIRECT_TABLE_ACCESS_FIELD_NUMBER: _ClassVar[int]
            RESTRICT_QUERY_RESULT_FIELD_NUMBER: _ClassVar[int]
            enabled: _wrappers_pb2.BoolValue
            restrict_direct_table_access: _wrappers_pb2.BoolValue
            restrict_query_result: _wrappers_pb2.BoolValue

            def __init__(self, enabled: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., restrict_direct_table_access: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., restrict_query_result: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=...) -> None:
                ...

        class Replica(_message.Message):
            __slots__ = ('location', 'replica_state', 'primary_state')

            class ReplicaState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                REPLICA_STATE_UNSPECIFIED: _ClassVar[Listing.BigQueryDatasetSource.Replica.ReplicaState]
                READY_TO_USE: _ClassVar[Listing.BigQueryDatasetSource.Replica.ReplicaState]
                UNAVAILABLE: _ClassVar[Listing.BigQueryDatasetSource.Replica.ReplicaState]
            REPLICA_STATE_UNSPECIFIED: Listing.BigQueryDatasetSource.Replica.ReplicaState
            READY_TO_USE: Listing.BigQueryDatasetSource.Replica.ReplicaState
            UNAVAILABLE: Listing.BigQueryDatasetSource.Replica.ReplicaState

            class PrimaryState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                PRIMARY_STATE_UNSPECIFIED: _ClassVar[Listing.BigQueryDatasetSource.Replica.PrimaryState]
                PRIMARY_REPLICA: _ClassVar[Listing.BigQueryDatasetSource.Replica.PrimaryState]
            PRIMARY_STATE_UNSPECIFIED: Listing.BigQueryDatasetSource.Replica.PrimaryState
            PRIMARY_REPLICA: Listing.BigQueryDatasetSource.Replica.PrimaryState
            LOCATION_FIELD_NUMBER: _ClassVar[int]
            REPLICA_STATE_FIELD_NUMBER: _ClassVar[int]
            PRIMARY_STATE_FIELD_NUMBER: _ClassVar[int]
            location: str
            replica_state: Listing.BigQueryDatasetSource.Replica.ReplicaState
            primary_state: Listing.BigQueryDatasetSource.Replica.PrimaryState

            def __init__(self, location: _Optional[str]=..., replica_state: _Optional[_Union[Listing.BigQueryDatasetSource.Replica.ReplicaState, str]]=..., primary_state: _Optional[_Union[Listing.BigQueryDatasetSource.Replica.PrimaryState, str]]=...) -> None:
                ...
        DATASET_FIELD_NUMBER: _ClassVar[int]
        SELECTED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
        RESTRICTED_EXPORT_POLICY_FIELD_NUMBER: _ClassVar[int]
        REPLICA_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        EFFECTIVE_REPLICAS_FIELD_NUMBER: _ClassVar[int]
        dataset: str
        selected_resources: _containers.RepeatedCompositeFieldContainer[Listing.BigQueryDatasetSource.SelectedResource]
        restricted_export_policy: Listing.BigQueryDatasetSource.RestrictedExportPolicy
        replica_locations: _containers.RepeatedScalarFieldContainer[str]
        effective_replicas: _containers.RepeatedCompositeFieldContainer[Listing.BigQueryDatasetSource.Replica]

        def __init__(self, dataset: _Optional[str]=..., selected_resources: _Optional[_Iterable[_Union[Listing.BigQueryDatasetSource.SelectedResource, _Mapping]]]=..., restricted_export_policy: _Optional[_Union[Listing.BigQueryDatasetSource.RestrictedExportPolicy, _Mapping]]=..., replica_locations: _Optional[_Iterable[str]]=..., effective_replicas: _Optional[_Iterable[_Union[Listing.BigQueryDatasetSource.Replica, _Mapping]]]=...) -> None:
            ...

    class PubSubTopicSource(_message.Message):
        __slots__ = ('topic', 'data_affinity_regions')
        TOPIC_FIELD_NUMBER: _ClassVar[int]
        DATA_AFFINITY_REGIONS_FIELD_NUMBER: _ClassVar[int]
        topic: str
        data_affinity_regions: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, topic: _Optional[str]=..., data_affinity_regions: _Optional[_Iterable[str]]=...) -> None:
            ...

    class RestrictedExportConfig(_message.Message):
        __slots__ = ('enabled', 'restrict_direct_table_access', 'restrict_query_result')
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        RESTRICT_DIRECT_TABLE_ACCESS_FIELD_NUMBER: _ClassVar[int]
        RESTRICT_QUERY_RESULT_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        restrict_direct_table_access: bool
        restrict_query_result: bool

        def __init__(self, enabled: bool=..., restrict_direct_table_access: bool=..., restrict_query_result: bool=...) -> None:
            ...

    class CommercialInfo(_message.Message):
        __slots__ = ('cloud_marketplace',)

        class GoogleCloudMarketplaceInfo(_message.Message):
            __slots__ = ('service', 'commercial_state')

            class CommercialState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                COMMERCIAL_STATE_UNSPECIFIED: _ClassVar[Listing.CommercialInfo.GoogleCloudMarketplaceInfo.CommercialState]
                ONBOARDING: _ClassVar[Listing.CommercialInfo.GoogleCloudMarketplaceInfo.CommercialState]
                ACTIVE: _ClassVar[Listing.CommercialInfo.GoogleCloudMarketplaceInfo.CommercialState]
            COMMERCIAL_STATE_UNSPECIFIED: Listing.CommercialInfo.GoogleCloudMarketplaceInfo.CommercialState
            ONBOARDING: Listing.CommercialInfo.GoogleCloudMarketplaceInfo.CommercialState
            ACTIVE: Listing.CommercialInfo.GoogleCloudMarketplaceInfo.CommercialState
            SERVICE_FIELD_NUMBER: _ClassVar[int]
            COMMERCIAL_STATE_FIELD_NUMBER: _ClassVar[int]
            service: str
            commercial_state: Listing.CommercialInfo.GoogleCloudMarketplaceInfo.CommercialState

            def __init__(self, service: _Optional[str]=..., commercial_state: _Optional[_Union[Listing.CommercialInfo.GoogleCloudMarketplaceInfo.CommercialState, str]]=...) -> None:
                ...
        CLOUD_MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
        cloud_marketplace: Listing.CommercialInfo.GoogleCloudMarketplaceInfo

        def __init__(self, cloud_marketplace: _Optional[_Union[Listing.CommercialInfo.GoogleCloudMarketplaceInfo, _Mapping]]=...) -> None:
            ...
    BIGQUERY_DATASET_FIELD_NUMBER: _ClassVar[int]
    PUBSUB_TOPIC_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_CONTACT_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DATA_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ACCESS_FIELD_NUMBER: _ClassVar[int]
    RESTRICTED_EXPORT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMERCIAL_INFO_FIELD_NUMBER: _ClassVar[int]
    LOG_LINKED_DATASET_QUERY_USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    ALLOW_ONLY_METADATA_SHARING_FIELD_NUMBER: _ClassVar[int]
    bigquery_dataset: Listing.BigQueryDatasetSource
    pubsub_topic: Listing.PubSubTopicSource
    name: str
    display_name: str
    description: str
    primary_contact: str
    documentation: str
    state: Listing.State
    icon: bytes
    data_provider: DataProvider
    categories: _containers.RepeatedScalarFieldContainer[Listing.Category]
    publisher: Publisher
    request_access: str
    restricted_export_config: Listing.RestrictedExportConfig
    discovery_type: DiscoveryType
    resource_type: SharedResourceType
    commercial_info: Listing.CommercialInfo
    log_linked_dataset_query_user_email: bool
    allow_only_metadata_sharing: bool

    def __init__(self, bigquery_dataset: _Optional[_Union[Listing.BigQueryDatasetSource, _Mapping]]=..., pubsub_topic: _Optional[_Union[Listing.PubSubTopicSource, _Mapping]]=..., name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., primary_contact: _Optional[str]=..., documentation: _Optional[str]=..., state: _Optional[_Union[Listing.State, str]]=..., icon: _Optional[bytes]=..., data_provider: _Optional[_Union[DataProvider, _Mapping]]=..., categories: _Optional[_Iterable[_Union[Listing.Category, str]]]=..., publisher: _Optional[_Union[Publisher, _Mapping]]=..., request_access: _Optional[str]=..., restricted_export_config: _Optional[_Union[Listing.RestrictedExportConfig, _Mapping]]=..., discovery_type: _Optional[_Union[DiscoveryType, str]]=..., resource_type: _Optional[_Union[SharedResourceType, str]]=..., commercial_info: _Optional[_Union[Listing.CommercialInfo, _Mapping]]=..., log_linked_dataset_query_user_email: bool=..., allow_only_metadata_sharing: bool=...) -> None:
        ...

class Subscription(_message.Message):
    __slots__ = ('listing', 'data_exchange', 'name', 'creation_time', 'last_modify_time', 'organization_id', 'organization_display_name', 'state', 'linked_dataset_map', 'subscriber_contact', 'linked_resources', 'resource_type', 'commercial_info', 'log_linked_dataset_query_user_email', 'destination_dataset')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Subscription.State]
        STATE_ACTIVE: _ClassVar[Subscription.State]
        STATE_STALE: _ClassVar[Subscription.State]
        STATE_INACTIVE: _ClassVar[Subscription.State]
    STATE_UNSPECIFIED: Subscription.State
    STATE_ACTIVE: Subscription.State
    STATE_STALE: Subscription.State
    STATE_INACTIVE: Subscription.State

    class LinkedResource(_message.Message):
        __slots__ = ('linked_dataset', 'linked_pubsub_subscription', 'listing')
        LINKED_DATASET_FIELD_NUMBER: _ClassVar[int]
        LINKED_PUBSUB_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
        LISTING_FIELD_NUMBER: _ClassVar[int]
        linked_dataset: str
        linked_pubsub_subscription: str
        listing: str

        def __init__(self, linked_dataset: _Optional[str]=..., linked_pubsub_subscription: _Optional[str]=..., listing: _Optional[str]=...) -> None:
            ...

    class CommercialInfo(_message.Message):
        __slots__ = ('cloud_marketplace',)

        class GoogleCloudMarketplaceInfo(_message.Message):
            __slots__ = ('order',)
            ORDER_FIELD_NUMBER: _ClassVar[int]
            order: str

            def __init__(self, order: _Optional[str]=...) -> None:
                ...
        CLOUD_MARKETPLACE_FIELD_NUMBER: _ClassVar[int]
        cloud_marketplace: Subscription.CommercialInfo.GoogleCloudMarketplaceInfo

        def __init__(self, cloud_marketplace: _Optional[_Union[Subscription.CommercialInfo.GoogleCloudMarketplaceInfo, _Mapping]]=...) -> None:
            ...

    class LinkedDatasetMapEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Subscription.LinkedResource

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[Subscription.LinkedResource, _Mapping]]=...) -> None:
            ...
    LISTING_FIELD_NUMBER: _ClassVar[int]
    DATA_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_MODIFY_TIME_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_ID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    LINKED_DATASET_MAP_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBER_CONTACT_FIELD_NUMBER: _ClassVar[int]
    LINKED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMERCIAL_INFO_FIELD_NUMBER: _ClassVar[int]
    LOG_LINKED_DATASET_QUERY_USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_DATASET_FIELD_NUMBER: _ClassVar[int]
    listing: str
    data_exchange: str
    name: str
    creation_time: _timestamp_pb2.Timestamp
    last_modify_time: _timestamp_pb2.Timestamp
    organization_id: str
    organization_display_name: str
    state: Subscription.State
    linked_dataset_map: _containers.MessageMap[str, Subscription.LinkedResource]
    subscriber_contact: str
    linked_resources: _containers.RepeatedCompositeFieldContainer[Subscription.LinkedResource]
    resource_type: SharedResourceType
    commercial_info: Subscription.CommercialInfo
    log_linked_dataset_query_user_email: bool
    destination_dataset: DestinationDataset

    def __init__(self, listing: _Optional[str]=..., data_exchange: _Optional[str]=..., name: _Optional[str]=..., creation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_modify_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., organization_id: _Optional[str]=..., organization_display_name: _Optional[str]=..., state: _Optional[_Union[Subscription.State, str]]=..., linked_dataset_map: _Optional[_Mapping[str, Subscription.LinkedResource]]=..., subscriber_contact: _Optional[str]=..., linked_resources: _Optional[_Iterable[_Union[Subscription.LinkedResource, _Mapping]]]=..., resource_type: _Optional[_Union[SharedResourceType, str]]=..., commercial_info: _Optional[_Union[Subscription.CommercialInfo, _Mapping]]=..., log_linked_dataset_query_user_email: bool=..., destination_dataset: _Optional[_Union[DestinationDataset, _Mapping]]=...) -> None:
        ...

class ListDataExchangesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListDataExchangesResponse(_message.Message):
    __slots__ = ('data_exchanges', 'next_page_token')
    DATA_EXCHANGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data_exchanges: _containers.RepeatedCompositeFieldContainer[DataExchange]
    next_page_token: str

    def __init__(self, data_exchanges: _Optional[_Iterable[_Union[DataExchange, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListOrgDataExchangesRequest(_message.Message):
    __slots__ = ('organization', 'page_size', 'page_token')
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    organization: str
    page_size: int
    page_token: str

    def __init__(self, organization: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListOrgDataExchangesResponse(_message.Message):
    __slots__ = ('data_exchanges', 'next_page_token')
    DATA_EXCHANGES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data_exchanges: _containers.RepeatedCompositeFieldContainer[DataExchange]
    next_page_token: str

    def __init__(self, data_exchanges: _Optional[_Iterable[_Union[DataExchange, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetDataExchangeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateDataExchangeRequest(_message.Message):
    __slots__ = ('parent', 'data_exchange_id', 'data_exchange')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATA_EXCHANGE_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    data_exchange_id: str
    data_exchange: DataExchange

    def __init__(self, parent: _Optional[str]=..., data_exchange_id: _Optional[str]=..., data_exchange: _Optional[_Union[DataExchange, _Mapping]]=...) -> None:
        ...

class UpdateDataExchangeRequest(_message.Message):
    __slots__ = ('update_mask', 'data_exchange')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    DATA_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    data_exchange: DataExchange

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., data_exchange: _Optional[_Union[DataExchange, _Mapping]]=...) -> None:
        ...

class DeleteDataExchangeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListListingsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListListingsResponse(_message.Message):
    __slots__ = ('listings', 'next_page_token')
    LISTINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    listings: _containers.RepeatedCompositeFieldContainer[Listing]
    next_page_token: str

    def __init__(self, listings: _Optional[_Iterable[_Union[Listing, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetListingRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateListingRequest(_message.Message):
    __slots__ = ('parent', 'listing_id', 'listing')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LISTING_ID_FIELD_NUMBER: _ClassVar[int]
    LISTING_FIELD_NUMBER: _ClassVar[int]
    parent: str
    listing_id: str
    listing: Listing

    def __init__(self, parent: _Optional[str]=..., listing_id: _Optional[str]=..., listing: _Optional[_Union[Listing, _Mapping]]=...) -> None:
        ...

class UpdateListingRequest(_message.Message):
    __slots__ = ('update_mask', 'listing')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    LISTING_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    listing: Listing

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., listing: _Optional[_Union[Listing, _Mapping]]=...) -> None:
        ...

class DeleteListingRequest(_message.Message):
    __slots__ = ('name', 'delete_commercial')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DELETE_COMMERCIAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    delete_commercial: bool

    def __init__(self, name: _Optional[str]=..., delete_commercial: bool=...) -> None:
        ...

class SubscribeListingRequest(_message.Message):
    __slots__ = ('destination_dataset', 'destination_pubsub_subscription', 'name')
    DESTINATION_DATASET_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PUBSUB_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    destination_dataset: DestinationDataset
    destination_pubsub_subscription: DestinationPubSubSubscription
    name: str

    def __init__(self, destination_dataset: _Optional[_Union[DestinationDataset, _Mapping]]=..., destination_pubsub_subscription: _Optional[_Union[DestinationPubSubSubscription, _Mapping]]=..., name: _Optional[str]=...) -> None:
        ...

class SubscribeListingResponse(_message.Message):
    __slots__ = ('subscription',)
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: Subscription

    def __init__(self, subscription: _Optional[_Union[Subscription, _Mapping]]=...) -> None:
        ...

class SubscribeDataExchangeRequest(_message.Message):
    __slots__ = ('name', 'destination', 'destination_dataset', 'subscription', 'subscriber_contact')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_DATASET_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBER_CONTACT_FIELD_NUMBER: _ClassVar[int]
    name: str
    destination: str
    destination_dataset: DestinationDataset
    subscription: str
    subscriber_contact: str

    def __init__(self, name: _Optional[str]=..., destination: _Optional[str]=..., destination_dataset: _Optional[_Union[DestinationDataset, _Mapping]]=..., subscription: _Optional[str]=..., subscriber_contact: _Optional[str]=...) -> None:
        ...

class SubscribeDataExchangeResponse(_message.Message):
    __slots__ = ('subscription',)
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: Subscription

    def __init__(self, subscription: _Optional[_Union[Subscription, _Mapping]]=...) -> None:
        ...

class RefreshSubscriptionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RefreshSubscriptionResponse(_message.Message):
    __slots__ = ('subscription',)
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: Subscription

    def __init__(self, subscription: _Optional[_Union[Subscription, _Mapping]]=...) -> None:
        ...

class GetSubscriptionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListSubscriptionsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListSubscriptionsResponse(_message.Message):
    __slots__ = ('subscriptions', 'next_page_token')
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedCompositeFieldContainer[Subscription]
    next_page_token: str

    def __init__(self, subscriptions: _Optional[_Iterable[_Union[Subscription, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListSharedResourceSubscriptionsRequest(_message.Message):
    __slots__ = ('resource', 'include_deleted_subscriptions', 'page_size', 'page_token')
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DELETED_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    resource: str
    include_deleted_subscriptions: bool
    page_size: int
    page_token: str

    def __init__(self, resource: _Optional[str]=..., include_deleted_subscriptions: bool=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListSharedResourceSubscriptionsResponse(_message.Message):
    __slots__ = ('shared_resource_subscriptions', 'next_page_token')
    SHARED_RESOURCE_SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    shared_resource_subscriptions: _containers.RepeatedCompositeFieldContainer[Subscription]
    next_page_token: str

    def __init__(self, shared_resource_subscriptions: _Optional[_Iterable[_Union[Subscription, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class RevokeSubscriptionRequest(_message.Message):
    __slots__ = ('name', 'revoke_commercial')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REVOKE_COMMERCIAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    revoke_commercial: bool

    def __init__(self, name: _Optional[str]=..., revoke_commercial: bool=...) -> None:
        ...

class RevokeSubscriptionResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DeleteSubscriptionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...