from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1 import cmek_config_service_pb2 as _cmek_config_service_pb2
from google.cloud.discoveryengine.v1 import common_pb2 as _common_pb2
from google.cloud.discoveryengine.v1 import document_processing_config_pb2 as _document_processing_config_pb2
from google.cloud.discoveryengine.v1 import schema_pb2 as _schema_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataStore(_message.Message):
    __slots__ = ('name', 'display_name', 'industry_vertical', 'solution_types', 'default_schema_id', 'content_config', 'create_time', 'advanced_site_search_config', 'kms_key_name', 'cmek_config', 'billing_estimation', 'acl_enabled', 'workspace_config', 'document_processing_config', 'starting_schema', 'healthcare_fhir_config', 'identity_mapping_store')

    class ContentConfig(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONTENT_CONFIG_UNSPECIFIED: _ClassVar[DataStore.ContentConfig]
        NO_CONTENT: _ClassVar[DataStore.ContentConfig]
        CONTENT_REQUIRED: _ClassVar[DataStore.ContentConfig]
        PUBLIC_WEBSITE: _ClassVar[DataStore.ContentConfig]
        GOOGLE_WORKSPACE: _ClassVar[DataStore.ContentConfig]
    CONTENT_CONFIG_UNSPECIFIED: DataStore.ContentConfig
    NO_CONTENT: DataStore.ContentConfig
    CONTENT_REQUIRED: DataStore.ContentConfig
    PUBLIC_WEBSITE: DataStore.ContentConfig
    GOOGLE_WORKSPACE: DataStore.ContentConfig

    class BillingEstimation(_message.Message):
        __slots__ = ('structured_data_size', 'unstructured_data_size', 'website_data_size', 'structured_data_update_time', 'unstructured_data_update_time', 'website_data_update_time')
        STRUCTURED_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
        UNSTRUCTURED_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
        WEBSITE_DATA_SIZE_FIELD_NUMBER: _ClassVar[int]
        STRUCTURED_DATA_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        UNSTRUCTURED_DATA_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        WEBSITE_DATA_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        structured_data_size: int
        unstructured_data_size: int
        website_data_size: int
        structured_data_update_time: _timestamp_pb2.Timestamp
        unstructured_data_update_time: _timestamp_pb2.Timestamp
        website_data_update_time: _timestamp_pb2.Timestamp

        def __init__(self, structured_data_size: _Optional[int]=..., unstructured_data_size: _Optional[int]=..., website_data_size: _Optional[int]=..., structured_data_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., unstructured_data_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., website_data_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    INDUSTRY_VERTICAL_FIELD_NUMBER: _ClassVar[int]
    SOLUTION_TYPES_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SCHEMA_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_SITE_SEARCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    CMEK_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BILLING_ESTIMATION_FIELD_NUMBER: _ClassVar[int]
    ACL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_PROCESSING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STARTING_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    HEALTHCARE_FHIR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_MAPPING_STORE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    industry_vertical: _common_pb2.IndustryVertical
    solution_types: _containers.RepeatedScalarFieldContainer[_common_pb2.SolutionType]
    default_schema_id: str
    content_config: DataStore.ContentConfig
    create_time: _timestamp_pb2.Timestamp
    advanced_site_search_config: AdvancedSiteSearchConfig
    kms_key_name: str
    cmek_config: _cmek_config_service_pb2.CmekConfig
    billing_estimation: DataStore.BillingEstimation
    acl_enabled: bool
    workspace_config: WorkspaceConfig
    document_processing_config: _document_processing_config_pb2.DocumentProcessingConfig
    starting_schema: _schema_pb2.Schema
    healthcare_fhir_config: _common_pb2.HealthcareFhirConfig
    identity_mapping_store: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., industry_vertical: _Optional[_Union[_common_pb2.IndustryVertical, str]]=..., solution_types: _Optional[_Iterable[_Union[_common_pb2.SolutionType, str]]]=..., default_schema_id: _Optional[str]=..., content_config: _Optional[_Union[DataStore.ContentConfig, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., advanced_site_search_config: _Optional[_Union[AdvancedSiteSearchConfig, _Mapping]]=..., kms_key_name: _Optional[str]=..., cmek_config: _Optional[_Union[_cmek_config_service_pb2.CmekConfig, _Mapping]]=..., billing_estimation: _Optional[_Union[DataStore.BillingEstimation, _Mapping]]=..., acl_enabled: bool=..., workspace_config: _Optional[_Union[WorkspaceConfig, _Mapping]]=..., document_processing_config: _Optional[_Union[_document_processing_config_pb2.DocumentProcessingConfig, _Mapping]]=..., starting_schema: _Optional[_Union[_schema_pb2.Schema, _Mapping]]=..., healthcare_fhir_config: _Optional[_Union[_common_pb2.HealthcareFhirConfig, _Mapping]]=..., identity_mapping_store: _Optional[str]=...) -> None:
        ...

class AdvancedSiteSearchConfig(_message.Message):
    __slots__ = ('disable_initial_index', 'disable_automatic_refresh')
    DISABLE_INITIAL_INDEX_FIELD_NUMBER: _ClassVar[int]
    DISABLE_AUTOMATIC_REFRESH_FIELD_NUMBER: _ClassVar[int]
    disable_initial_index: bool
    disable_automatic_refresh: bool

    def __init__(self, disable_initial_index: bool=..., disable_automatic_refresh: bool=...) -> None:
        ...

class WorkspaceConfig(_message.Message):
    __slots__ = ('type', 'dasher_customer_id', 'super_admin_service_account', 'super_admin_email_address')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[WorkspaceConfig.Type]
        GOOGLE_DRIVE: _ClassVar[WorkspaceConfig.Type]
        GOOGLE_MAIL: _ClassVar[WorkspaceConfig.Type]
        GOOGLE_SITES: _ClassVar[WorkspaceConfig.Type]
        GOOGLE_CALENDAR: _ClassVar[WorkspaceConfig.Type]
        GOOGLE_CHAT: _ClassVar[WorkspaceConfig.Type]
        GOOGLE_GROUPS: _ClassVar[WorkspaceConfig.Type]
        GOOGLE_KEEP: _ClassVar[WorkspaceConfig.Type]
        GOOGLE_PEOPLE: _ClassVar[WorkspaceConfig.Type]
    TYPE_UNSPECIFIED: WorkspaceConfig.Type
    GOOGLE_DRIVE: WorkspaceConfig.Type
    GOOGLE_MAIL: WorkspaceConfig.Type
    GOOGLE_SITES: WorkspaceConfig.Type
    GOOGLE_CALENDAR: WorkspaceConfig.Type
    GOOGLE_CHAT: WorkspaceConfig.Type
    GOOGLE_GROUPS: WorkspaceConfig.Type
    GOOGLE_KEEP: WorkspaceConfig.Type
    GOOGLE_PEOPLE: WorkspaceConfig.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DASHER_CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    SUPER_ADMIN_SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    SUPER_ADMIN_EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    type: WorkspaceConfig.Type
    dasher_customer_id: str
    super_admin_service_account: str
    super_admin_email_address: str

    def __init__(self, type: _Optional[_Union[WorkspaceConfig.Type, str]]=..., dasher_customer_id: _Optional[str]=..., super_admin_service_account: _Optional[str]=..., super_admin_email_address: _Optional[str]=...) -> None:
        ...