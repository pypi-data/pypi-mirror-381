from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.api import routing_pb2 as _routing_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PendingRenameInfo(_message.Message):
    __slots__ = ('operation',)
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    operation: str

    def __init__(self, operation: _Optional[str]=...) -> None:
        ...

class Folder(_message.Message):
    __slots__ = ('name', 'metageneration', 'create_time', 'update_time', 'pending_rename_info')
    NAME_FIELD_NUMBER: _ClassVar[int]
    METAGENERATION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PENDING_RENAME_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    metageneration: int
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    pending_rename_info: PendingRenameInfo

    def __init__(self, name: _Optional[str]=..., metageneration: _Optional[int]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., pending_rename_info: _Optional[_Union[PendingRenameInfo, _Mapping]]=...) -> None:
        ...

class GetFolderRequest(_message.Message):
    __slots__ = ('name', 'if_metageneration_match', 'if_metageneration_not_match', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    if_metageneration_match: int
    if_metageneration_not_match: int
    request_id: str

    def __init__(self, name: _Optional[str]=..., if_metageneration_match: _Optional[int]=..., if_metageneration_not_match: _Optional[int]=..., request_id: _Optional[str]=...) -> None:
        ...

class CreateFolderRequest(_message.Message):
    __slots__ = ('parent', 'folder', 'folder_id', 'recursive', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    folder: Folder
    folder_id: str
    recursive: bool
    request_id: str

    def __init__(self, parent: _Optional[str]=..., folder: _Optional[_Union[Folder, _Mapping]]=..., folder_id: _Optional[str]=..., recursive: bool=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteFolderRequest(_message.Message):
    __slots__ = ('name', 'if_metageneration_match', 'if_metageneration_not_match', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    if_metageneration_match: int
    if_metageneration_not_match: int
    request_id: str

    def __init__(self, name: _Optional[str]=..., if_metageneration_match: _Optional[int]=..., if_metageneration_not_match: _Optional[int]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListFoldersRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'prefix', 'delimiter', 'lexicographic_start', 'lexicographic_end', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    DELIMITER_FIELD_NUMBER: _ClassVar[int]
    LEXICOGRAPHIC_START_FIELD_NUMBER: _ClassVar[int]
    LEXICOGRAPHIC_END_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    prefix: str
    delimiter: str
    lexicographic_start: str
    lexicographic_end: str
    request_id: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., prefix: _Optional[str]=..., delimiter: _Optional[str]=..., lexicographic_start: _Optional[str]=..., lexicographic_end: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListFoldersResponse(_message.Message):
    __slots__ = ('folders', 'next_page_token')
    FOLDERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    folders: _containers.RepeatedCompositeFieldContainer[Folder]
    next_page_token: str

    def __init__(self, folders: _Optional[_Iterable[_Union[Folder, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class RenameFolderRequest(_message.Message):
    __slots__ = ('name', 'destination_folder_id', 'if_metageneration_match', 'if_metageneration_not_match', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    destination_folder_id: str
    if_metageneration_match: int
    if_metageneration_not_match: int
    request_id: str

    def __init__(self, name: _Optional[str]=..., destination_folder_id: _Optional[str]=..., if_metageneration_match: _Optional[int]=..., if_metageneration_not_match: _Optional[int]=..., request_id: _Optional[str]=...) -> None:
        ...

class CommonLongRunningOperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'update_time', 'type', 'requested_cancellation', 'progress_percent')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_PERCENT_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    type: str
    requested_cancellation: bool
    progress_percent: int

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., type: _Optional[str]=..., requested_cancellation: bool=..., progress_percent: _Optional[int]=...) -> None:
        ...

class RenameFolderMetadata(_message.Message):
    __slots__ = ('common_metadata', 'source_folder_id', 'destination_folder_id')
    COMMON_METADATA_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    common_metadata: CommonLongRunningOperationMetadata
    source_folder_id: str
    destination_folder_id: str

    def __init__(self, common_metadata: _Optional[_Union[CommonLongRunningOperationMetadata, _Mapping]]=..., source_folder_id: _Optional[str]=..., destination_folder_id: _Optional[str]=...) -> None:
        ...

class StorageLayout(_message.Message):
    __slots__ = ('name', 'location', 'location_type', 'custom_placement_config', 'hierarchical_namespace')

    class CustomPlacementConfig(_message.Message):
        __slots__ = ('data_locations',)
        DATA_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        data_locations: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, data_locations: _Optional[_Iterable[str]]=...) -> None:
            ...

    class HierarchicalNamespace(_message.Message):
        __slots__ = ('enabled',)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool

        def __init__(self, enabled: bool=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_PLACEMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    HIERARCHICAL_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    name: str
    location: str
    location_type: str
    custom_placement_config: StorageLayout.CustomPlacementConfig
    hierarchical_namespace: StorageLayout.HierarchicalNamespace

    def __init__(self, name: _Optional[str]=..., location: _Optional[str]=..., location_type: _Optional[str]=..., custom_placement_config: _Optional[_Union[StorageLayout.CustomPlacementConfig, _Mapping]]=..., hierarchical_namespace: _Optional[_Union[StorageLayout.HierarchicalNamespace, _Mapping]]=...) -> None:
        ...

class GetStorageLayoutRequest(_message.Message):
    __slots__ = ('name', 'prefix', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    prefix: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., prefix: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ManagedFolder(_message.Message):
    __slots__ = ('name', 'metageneration', 'create_time', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    METAGENERATION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    metageneration: int
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., metageneration: _Optional[int]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetManagedFolderRequest(_message.Message):
    __slots__ = ('name', 'if_metageneration_match', 'if_metageneration_not_match', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    if_metageneration_match: int
    if_metageneration_not_match: int
    request_id: str

    def __init__(self, name: _Optional[str]=..., if_metageneration_match: _Optional[int]=..., if_metageneration_not_match: _Optional[int]=..., request_id: _Optional[str]=...) -> None:
        ...

class CreateManagedFolderRequest(_message.Message):
    __slots__ = ('parent', 'managed_folder', 'managed_folder_id', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MANAGED_FOLDER_FIELD_NUMBER: _ClassVar[int]
    MANAGED_FOLDER_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    managed_folder: ManagedFolder
    managed_folder_id: str
    request_id: str

    def __init__(self, parent: _Optional[str]=..., managed_folder: _Optional[_Union[ManagedFolder, _Mapping]]=..., managed_folder_id: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteManagedFolderRequest(_message.Message):
    __slots__ = ('name', 'if_metageneration_match', 'if_metageneration_not_match', 'allow_non_empty', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_MATCH_FIELD_NUMBER: _ClassVar[int]
    IF_METAGENERATION_NOT_MATCH_FIELD_NUMBER: _ClassVar[int]
    ALLOW_NON_EMPTY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    if_metageneration_match: int
    if_metageneration_not_match: int
    allow_non_empty: bool
    request_id: str

    def __init__(self, name: _Optional[str]=..., if_metageneration_match: _Optional[int]=..., if_metageneration_not_match: _Optional[int]=..., allow_non_empty: bool=..., request_id: _Optional[str]=...) -> None:
        ...

class ListManagedFoldersRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'prefix', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    prefix: str
    request_id: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., prefix: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListManagedFoldersResponse(_message.Message):
    __slots__ = ('managed_folders', 'next_page_token')
    MANAGED_FOLDERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    managed_folders: _containers.RepeatedCompositeFieldContainer[ManagedFolder]
    next_page_token: str

    def __init__(self, managed_folders: _Optional[_Iterable[_Union[ManagedFolder, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateAnywhereCacheMetadata(_message.Message):
    __slots__ = ('common_metadata', 'anywhere_cache_id', 'zone', 'ttl', 'admission_policy')
    COMMON_METADATA_FIELD_NUMBER: _ClassVar[int]
    ANYWHERE_CACHE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    ADMISSION_POLICY_FIELD_NUMBER: _ClassVar[int]
    common_metadata: CommonLongRunningOperationMetadata
    anywhere_cache_id: str
    zone: str
    ttl: _duration_pb2.Duration
    admission_policy: str

    def __init__(self, common_metadata: _Optional[_Union[CommonLongRunningOperationMetadata, _Mapping]]=..., anywhere_cache_id: _Optional[str]=..., zone: _Optional[str]=..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., admission_policy: _Optional[str]=...) -> None:
        ...

class UpdateAnywhereCacheMetadata(_message.Message):
    __slots__ = ('common_metadata', 'anywhere_cache_id', 'zone', 'ttl', 'admission_policy')
    COMMON_METADATA_FIELD_NUMBER: _ClassVar[int]
    ANYWHERE_CACHE_ID_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    ADMISSION_POLICY_FIELD_NUMBER: _ClassVar[int]
    common_metadata: CommonLongRunningOperationMetadata
    anywhere_cache_id: str
    zone: str
    ttl: _duration_pb2.Duration
    admission_policy: str

    def __init__(self, common_metadata: _Optional[_Union[CommonLongRunningOperationMetadata, _Mapping]]=..., anywhere_cache_id: _Optional[str]=..., zone: _Optional[str]=..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., admission_policy: _Optional[str]=...) -> None:
        ...

class AnywhereCache(_message.Message):
    __slots__ = ('name', 'zone', 'ttl', 'admission_policy', 'state', 'create_time', 'update_time', 'pending_update')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ZONE_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    ADMISSION_POLICY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PENDING_UPDATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    zone: str
    ttl: _duration_pb2.Duration
    admission_policy: str
    state: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    pending_update: bool

    def __init__(self, name: _Optional[str]=..., zone: _Optional[str]=..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., admission_policy: _Optional[str]=..., state: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., pending_update: bool=...) -> None:
        ...

class CreateAnywhereCacheRequest(_message.Message):
    __slots__ = ('parent', 'anywhere_cache', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ANYWHERE_CACHE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    anywhere_cache: AnywhereCache
    request_id: str

    def __init__(self, parent: _Optional[str]=..., anywhere_cache: _Optional[_Union[AnywhereCache, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateAnywhereCacheRequest(_message.Message):
    __slots__ = ('anywhere_cache', 'update_mask', 'request_id')
    ANYWHERE_CACHE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    anywhere_cache: AnywhereCache
    update_mask: _field_mask_pb2.FieldMask
    request_id: str

    def __init__(self, anywhere_cache: _Optional[_Union[AnywhereCache, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DisableAnywhereCacheRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class PauseAnywhereCacheRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ResumeAnywhereCacheRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class GetAnywhereCacheRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListAnywhereCachesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    request_id: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListAnywhereCachesResponse(_message.Message):
    __slots__ = ('anywhere_caches', 'next_page_token')
    ANYWHERE_CACHES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    anywhere_caches: _containers.RepeatedCompositeFieldContainer[AnywhereCache]
    next_page_token: str

    def __init__(self, anywhere_caches: _Optional[_Iterable[_Union[AnywhereCache, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class IntelligenceConfig(_message.Message):
    __slots__ = ('name', 'edition_config', 'update_time', 'filter', 'effective_intelligence_config', 'trial_config')

    class EditionConfig(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EDITION_CONFIG_UNSPECIFIED: _ClassVar[IntelligenceConfig.EditionConfig]
        INHERIT: _ClassVar[IntelligenceConfig.EditionConfig]
        DISABLED: _ClassVar[IntelligenceConfig.EditionConfig]
        STANDARD: _ClassVar[IntelligenceConfig.EditionConfig]
        TRIAL: _ClassVar[IntelligenceConfig.EditionConfig]
    EDITION_CONFIG_UNSPECIFIED: IntelligenceConfig.EditionConfig
    INHERIT: IntelligenceConfig.EditionConfig
    DISABLED: IntelligenceConfig.EditionConfig
    STANDARD: IntelligenceConfig.EditionConfig
    TRIAL: IntelligenceConfig.EditionConfig

    class Filter(_message.Message):
        __slots__ = ('included_cloud_storage_locations', 'excluded_cloud_storage_locations', 'included_cloud_storage_buckets', 'excluded_cloud_storage_buckets')

        class CloudStorageLocations(_message.Message):
            __slots__ = ('locations',)
            LOCATIONS_FIELD_NUMBER: _ClassVar[int]
            locations: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, locations: _Optional[_Iterable[str]]=...) -> None:
                ...

        class CloudStorageBuckets(_message.Message):
            __slots__ = ('bucket_id_regexes',)
            BUCKET_ID_REGEXES_FIELD_NUMBER: _ClassVar[int]
            bucket_id_regexes: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, bucket_id_regexes: _Optional[_Iterable[str]]=...) -> None:
                ...
        INCLUDED_CLOUD_STORAGE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        EXCLUDED_CLOUD_STORAGE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        INCLUDED_CLOUD_STORAGE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
        EXCLUDED_CLOUD_STORAGE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
        included_cloud_storage_locations: IntelligenceConfig.Filter.CloudStorageLocations
        excluded_cloud_storage_locations: IntelligenceConfig.Filter.CloudStorageLocations
        included_cloud_storage_buckets: IntelligenceConfig.Filter.CloudStorageBuckets
        excluded_cloud_storage_buckets: IntelligenceConfig.Filter.CloudStorageBuckets

        def __init__(self, included_cloud_storage_locations: _Optional[_Union[IntelligenceConfig.Filter.CloudStorageLocations, _Mapping]]=..., excluded_cloud_storage_locations: _Optional[_Union[IntelligenceConfig.Filter.CloudStorageLocations, _Mapping]]=..., included_cloud_storage_buckets: _Optional[_Union[IntelligenceConfig.Filter.CloudStorageBuckets, _Mapping]]=..., excluded_cloud_storage_buckets: _Optional[_Union[IntelligenceConfig.Filter.CloudStorageBuckets, _Mapping]]=...) -> None:
            ...

    class EffectiveIntelligenceConfig(_message.Message):
        __slots__ = ('effective_edition', 'intelligence_config')

        class EffectiveEdition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            EFFECTIVE_EDITION_UNSPECIFIED: _ClassVar[IntelligenceConfig.EffectiveIntelligenceConfig.EffectiveEdition]
            NONE: _ClassVar[IntelligenceConfig.EffectiveIntelligenceConfig.EffectiveEdition]
            STANDARD: _ClassVar[IntelligenceConfig.EffectiveIntelligenceConfig.EffectiveEdition]
        EFFECTIVE_EDITION_UNSPECIFIED: IntelligenceConfig.EffectiveIntelligenceConfig.EffectiveEdition
        NONE: IntelligenceConfig.EffectiveIntelligenceConfig.EffectiveEdition
        STANDARD: IntelligenceConfig.EffectiveIntelligenceConfig.EffectiveEdition
        EFFECTIVE_EDITION_FIELD_NUMBER: _ClassVar[int]
        INTELLIGENCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        effective_edition: IntelligenceConfig.EffectiveIntelligenceConfig.EffectiveEdition
        intelligence_config: str

        def __init__(self, effective_edition: _Optional[_Union[IntelligenceConfig.EffectiveIntelligenceConfig.EffectiveEdition, str]]=..., intelligence_config: _Optional[str]=...) -> None:
            ...

    class TrialConfig(_message.Message):
        __slots__ = ('expire_time',)
        EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
        expire_time: _timestamp_pb2.Timestamp

        def __init__(self, expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    EDITION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_INTELLIGENCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TRIAL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    edition_config: IntelligenceConfig.EditionConfig
    update_time: _timestamp_pb2.Timestamp
    filter: IntelligenceConfig.Filter
    effective_intelligence_config: IntelligenceConfig.EffectiveIntelligenceConfig
    trial_config: IntelligenceConfig.TrialConfig

    def __init__(self, name: _Optional[str]=..., edition_config: _Optional[_Union[IntelligenceConfig.EditionConfig, str]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., filter: _Optional[_Union[IntelligenceConfig.Filter, _Mapping]]=..., effective_intelligence_config: _Optional[_Union[IntelligenceConfig.EffectiveIntelligenceConfig, _Mapping]]=..., trial_config: _Optional[_Union[IntelligenceConfig.TrialConfig, _Mapping]]=...) -> None:
        ...

class UpdateOrganizationIntelligenceConfigRequest(_message.Message):
    __slots__ = ('intelligence_config', 'update_mask', 'request_id')
    INTELLIGENCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    intelligence_config: IntelligenceConfig
    update_mask: _field_mask_pb2.FieldMask
    request_id: str

    def __init__(self, intelligence_config: _Optional[_Union[IntelligenceConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateFolderIntelligenceConfigRequest(_message.Message):
    __slots__ = ('intelligence_config', 'update_mask', 'request_id')
    INTELLIGENCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    intelligence_config: IntelligenceConfig
    update_mask: _field_mask_pb2.FieldMask
    request_id: str

    def __init__(self, intelligence_config: _Optional[_Union[IntelligenceConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateProjectIntelligenceConfigRequest(_message.Message):
    __slots__ = ('intelligence_config', 'update_mask', 'request_id')
    INTELLIGENCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    intelligence_config: IntelligenceConfig
    update_mask: _field_mask_pb2.FieldMask
    request_id: str

    def __init__(self, intelligence_config: _Optional[_Union[IntelligenceConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class GetOrganizationIntelligenceConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetFolderIntelligenceConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetProjectIntelligenceConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...