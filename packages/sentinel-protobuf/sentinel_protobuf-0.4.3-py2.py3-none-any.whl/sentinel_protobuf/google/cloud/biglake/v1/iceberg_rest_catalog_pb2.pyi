from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import httpbody_pb2 as _httpbody_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RegisterIcebergTableRequest(_message.Message):
    __slots__ = ('parent', 'name', 'metadata_location', 'overwrite')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_LOCATION_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    name: str
    metadata_location: str
    overwrite: str

    def __init__(self, parent: _Optional[str]=..., name: _Optional[str]=..., metadata_location: _Optional[str]=..., overwrite: _Optional[str]=...) -> None:
        ...

class IcebergCatalog(_message.Message):
    __slots__ = ('name', 'credential_mode', 'biglake_service_account', 'catalog_type', 'default_location', 'catalog_regions', 'create_time', 'update_time')

    class CatalogType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CATALOG_TYPE_UNSPECIFIED: _ClassVar[IcebergCatalog.CatalogType]
        CATALOG_TYPE_GCS_BUCKET: _ClassVar[IcebergCatalog.CatalogType]
    CATALOG_TYPE_UNSPECIFIED: IcebergCatalog.CatalogType
    CATALOG_TYPE_GCS_BUCKET: IcebergCatalog.CatalogType

    class CredentialMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CREDENTIAL_MODE_UNSPECIFIED: _ClassVar[IcebergCatalog.CredentialMode]
        CREDENTIAL_MODE_END_USER: _ClassVar[IcebergCatalog.CredentialMode]
        CREDENTIAL_MODE_VENDED_CREDENTIALS: _ClassVar[IcebergCatalog.CredentialMode]
    CREDENTIAL_MODE_UNSPECIFIED: IcebergCatalog.CredentialMode
    CREDENTIAL_MODE_END_USER: IcebergCatalog.CredentialMode
    CREDENTIAL_MODE_VENDED_CREDENTIALS: IcebergCatalog.CredentialMode
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_MODE_FIELD_NUMBER: _ClassVar[int]
    BIGLAKE_SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CATALOG_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    CATALOG_REGIONS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    credential_mode: IcebergCatalog.CredentialMode
    biglake_service_account: str
    catalog_type: IcebergCatalog.CatalogType
    default_location: str
    catalog_regions: _containers.RepeatedScalarFieldContainer[str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., credential_mode: _Optional[_Union[IcebergCatalog.CredentialMode, str]]=..., biglake_service_account: _Optional[str]=..., catalog_type: _Optional[_Union[IcebergCatalog.CatalogType, str]]=..., default_location: _Optional[str]=..., catalog_regions: _Optional[_Iterable[str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CreateIcebergCatalogRequest(_message.Message):
    __slots__ = ('parent', 'iceberg_catalog_id', 'iceberg_catalog')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ICEBERG_CATALOG_ID_FIELD_NUMBER: _ClassVar[int]
    ICEBERG_CATALOG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    iceberg_catalog_id: str
    iceberg_catalog: IcebergCatalog

    def __init__(self, parent: _Optional[str]=..., iceberg_catalog_id: _Optional[str]=..., iceberg_catalog: _Optional[_Union[IcebergCatalog, _Mapping]]=...) -> None:
        ...

class DeleteIcebergCatalogRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateIcebergCatalogRequest(_message.Message):
    __slots__ = ('iceberg_catalog', 'update_mask')
    ICEBERG_CATALOG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    iceberg_catalog: IcebergCatalog
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, iceberg_catalog: _Optional[_Union[IcebergCatalog, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class GetIcebergCatalogRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListIcebergCatalogsRequest(_message.Message):
    __slots__ = ('parent', 'view', 'page_size', 'page_token')

    class CatalogView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CATALOG_VIEW_UNSPECIFIED: _ClassVar[ListIcebergCatalogsRequest.CatalogView]
        CATALOG_VIEW_BASIC: _ClassVar[ListIcebergCatalogsRequest.CatalogView]
        CATALOG_VIEW_FULL: _ClassVar[ListIcebergCatalogsRequest.CatalogView]
    CATALOG_VIEW_UNSPECIFIED: ListIcebergCatalogsRequest.CatalogView
    CATALOG_VIEW_BASIC: ListIcebergCatalogsRequest.CatalogView
    CATALOG_VIEW_FULL: ListIcebergCatalogsRequest.CatalogView
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    view: ListIcebergCatalogsRequest.CatalogView
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., view: _Optional[_Union[ListIcebergCatalogsRequest.CatalogView, str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListIcebergCatalogsResponse(_message.Message):
    __slots__ = ('iceberg_catalogs', 'next_page_token', 'unreachable')
    ICEBERG_CATALOGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    iceberg_catalogs: _containers.RepeatedCompositeFieldContainer[IcebergCatalog]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, iceberg_catalogs: _Optional[_Iterable[_Union[IcebergCatalog, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class FailoverIcebergCatalogRequest(_message.Message):
    __slots__ = ('name', 'primary_replica', 'validate_only', 'conditional_failover_replication_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_REPLICA_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    CONDITIONAL_FAILOVER_REPLICATION_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    primary_replica: str
    validate_only: bool
    conditional_failover_replication_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., primary_replica: _Optional[str]=..., validate_only: bool=..., conditional_failover_replication_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class FailoverIcebergCatalogResponse(_message.Message):
    __slots__ = ('replication_time',)
    REPLICATION_TIME_FIELD_NUMBER: _ClassVar[int]
    replication_time: _timestamp_pb2.Timestamp

    def __init__(self, replication_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class UpdateIcebergTableRequest(_message.Message):
    __slots__ = ('name', 'http_body')
    NAME_FIELD_NUMBER: _ClassVar[int]
    HTTP_BODY_FIELD_NUMBER: _ClassVar[int]
    name: str
    http_body: _httpbody_pb2.HttpBody

    def __init__(self, name: _Optional[str]=..., http_body: _Optional[_Union[_httpbody_pb2.HttpBody, _Mapping]]=...) -> None:
        ...

class GetIcebergTableRequest(_message.Message):
    __slots__ = ('name', 'snapshots')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    snapshots: str

    def __init__(self, name: _Optional[str]=..., snapshots: _Optional[str]=...) -> None:
        ...

class DeleteIcebergTableRequest(_message.Message):
    __slots__ = ('name', 'purge_requested')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PURGE_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    name: str
    purge_requested: bool

    def __init__(self, name: _Optional[str]=..., purge_requested: bool=...) -> None:
        ...

class CreateIcebergTableRequest(_message.Message):
    __slots__ = ('parent', 'http_body')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HTTP_BODY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    http_body: _httpbody_pb2.HttpBody

    def __init__(self, parent: _Optional[str]=..., http_body: _Optional[_Union[_httpbody_pb2.HttpBody, _Mapping]]=...) -> None:
        ...

class ListIcebergTableIdentifiersRequest(_message.Message):
    __slots__ = ('page_token', 'page_size', 'parent')
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    page_token: str
    page_size: int
    parent: str

    def __init__(self, page_token: _Optional[str]=..., page_size: _Optional[int]=..., parent: _Optional[str]=...) -> None:
        ...

class TableIdentifier(_message.Message):
    __slots__ = ('namespace', 'name')
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    namespace: _containers.RepeatedScalarFieldContainer[str]
    name: str

    def __init__(self, namespace: _Optional[_Iterable[str]]=..., name: _Optional[str]=...) -> None:
        ...

class ListIcebergTableIdentifiersResponse(_message.Message):
    __slots__ = ('identifiers', 'next_page_token')
    IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    identifiers: _containers.RepeatedCompositeFieldContainer[TableIdentifier]
    next_page_token: str

    def __init__(self, identifiers: _Optional[_Iterable[_Union[TableIdentifier, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class IcebergNamespaceUpdate(_message.Message):
    __slots__ = ('removals', 'updates')

    class UpdatesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    REMOVALS_FIELD_NUMBER: _ClassVar[int]
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    removals: _containers.RepeatedScalarFieldContainer[str]
    updates: _containers.ScalarMap[str, str]

    def __init__(self, removals: _Optional[_Iterable[str]]=..., updates: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class UpdateIcebergNamespaceRequest(_message.Message):
    __slots__ = ('name', 'iceberg_namespace_update')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICEBERG_NAMESPACE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    iceberg_namespace_update: IcebergNamespaceUpdate

    def __init__(self, name: _Optional[str]=..., iceberg_namespace_update: _Optional[_Union[IcebergNamespaceUpdate, _Mapping]]=...) -> None:
        ...

class UpdateIcebergNamespaceResponse(_message.Message):
    __slots__ = ('removed', 'updated', 'missing')
    REMOVED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    MISSING_FIELD_NUMBER: _ClassVar[int]
    removed: _containers.RepeatedScalarFieldContainer[str]
    updated: _containers.RepeatedScalarFieldContainer[str]
    missing: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, removed: _Optional[_Iterable[str]]=..., updated: _Optional[_Iterable[str]]=..., missing: _Optional[_Iterable[str]]=...) -> None:
        ...

class DeleteIcebergNamespaceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class IcebergNamespace(_message.Message):
    __slots__ = ('namespace', 'properties')

    class PropertiesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    namespace: _containers.RepeatedScalarFieldContainer[str]
    properties: _containers.ScalarMap[str, str]

    def __init__(self, namespace: _Optional[_Iterable[str]]=..., properties: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class CreateIcebergNamespaceRequest(_message.Message):
    __slots__ = ('parent', 'iceberg_namespace')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ICEBERG_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    iceberg_namespace: IcebergNamespace

    def __init__(self, parent: _Optional[str]=..., iceberg_namespace: _Optional[_Union[IcebergNamespace, _Mapping]]=...) -> None:
        ...

class GetIcebergCatalogConfigRequest(_message.Message):
    __slots__ = ('warehouse',)
    WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    warehouse: str

    def __init__(self, warehouse: _Optional[str]=...) -> None:
        ...

class IcebergCatalogConfig(_message.Message):
    __slots__ = ('overrides', 'defaults', 'endpoints')

    class OverridesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class DefaultsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    DEFAULTS_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    overrides: _containers.ScalarMap[str, str]
    defaults: _containers.ScalarMap[str, str]
    endpoints: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, overrides: _Optional[_Mapping[str, str]]=..., defaults: _Optional[_Mapping[str, str]]=..., endpoints: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetIcebergNamespaceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListIcebergNamespacesRequest(_message.Message):
    __slots__ = ('page_token', 'page_size', 'api_parent', 'parent')
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    API_PARENT_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    page_token: str
    page_size: int
    api_parent: str
    parent: str

    def __init__(self, page_token: _Optional[str]=..., page_size: _Optional[int]=..., api_parent: _Optional[str]=..., parent: _Optional[str]=...) -> None:
        ...

class ListIcebergNamespacesResponse(_message.Message):
    __slots__ = ('namespaces', 'next_page_token')
    NAMESPACES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    namespaces: _containers.RepeatedCompositeFieldContainer[_struct_pb2.ListValue]
    next_page_token: str

    def __init__(self, namespaces: _Optional[_Iterable[_Union[_struct_pb2.ListValue, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class StorageCredential(_message.Message):
    __slots__ = ('prefix', 'config')

    class ConfigEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    prefix: str
    config: _containers.ScalarMap[str, str]

    def __init__(self, prefix: _Optional[str]=..., config: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class LoadIcebergTableCredentialsResponse(_message.Message):
    __slots__ = ('storage_credentials',)
    STORAGE_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    storage_credentials: _containers.RepeatedCompositeFieldContainer[StorageCredential]

    def __init__(self, storage_credentials: _Optional[_Iterable[_Union[StorageCredential, _Mapping]]]=...) -> None:
        ...