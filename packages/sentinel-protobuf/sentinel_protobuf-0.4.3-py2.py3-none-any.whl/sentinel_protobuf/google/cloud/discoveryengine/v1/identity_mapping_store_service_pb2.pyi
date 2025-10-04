from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1 import identity_mapping_store_pb2 as _identity_mapping_store_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateIdentityMappingStoreRequest(_message.Message):
    __slots__ = ('cmek_config_name', 'disable_cmek', 'parent', 'identity_mapping_store_id', 'identity_mapping_store')
    CMEK_CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    DISABLE_CMEK_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_MAPPING_STORE_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_MAPPING_STORE_FIELD_NUMBER: _ClassVar[int]
    cmek_config_name: str
    disable_cmek: bool
    parent: str
    identity_mapping_store_id: str
    identity_mapping_store: _identity_mapping_store_pb2.IdentityMappingStore

    def __init__(self, cmek_config_name: _Optional[str]=..., disable_cmek: bool=..., parent: _Optional[str]=..., identity_mapping_store_id: _Optional[str]=..., identity_mapping_store: _Optional[_Union[_identity_mapping_store_pb2.IdentityMappingStore, _Mapping]]=...) -> None:
        ...

class GetIdentityMappingStoreRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteIdentityMappingStoreRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ImportIdentityMappingsRequest(_message.Message):
    __slots__ = ('inline_source', 'identity_mapping_store')

    class InlineSource(_message.Message):
        __slots__ = ('identity_mapping_entries',)
        IDENTITY_MAPPING_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        identity_mapping_entries: _containers.RepeatedCompositeFieldContainer[_identity_mapping_store_pb2.IdentityMappingEntry]

        def __init__(self, identity_mapping_entries: _Optional[_Iterable[_Union[_identity_mapping_store_pb2.IdentityMappingEntry, _Mapping]]]=...) -> None:
            ...
    INLINE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_MAPPING_STORE_FIELD_NUMBER: _ClassVar[int]
    inline_source: ImportIdentityMappingsRequest.InlineSource
    identity_mapping_store: str

    def __init__(self, inline_source: _Optional[_Union[ImportIdentityMappingsRequest.InlineSource, _Mapping]]=..., identity_mapping_store: _Optional[str]=...) -> None:
        ...

class ImportIdentityMappingsResponse(_message.Message):
    __slots__ = ('error_samples',)
    ERROR_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    error_samples: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]

    def __init__(self, error_samples: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=...) -> None:
        ...

class PurgeIdentityMappingsRequest(_message.Message):
    __slots__ = ('inline_source', 'identity_mapping_store', 'filter', 'force')

    class InlineSource(_message.Message):
        __slots__ = ('identity_mapping_entries',)
        IDENTITY_MAPPING_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        identity_mapping_entries: _containers.RepeatedCompositeFieldContainer[_identity_mapping_store_pb2.IdentityMappingEntry]

        def __init__(self, identity_mapping_entries: _Optional[_Iterable[_Union[_identity_mapping_store_pb2.IdentityMappingEntry, _Mapping]]]=...) -> None:
            ...
    INLINE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_MAPPING_STORE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    inline_source: PurgeIdentityMappingsRequest.InlineSource
    identity_mapping_store: str
    filter: str
    force: bool

    def __init__(self, inline_source: _Optional[_Union[PurgeIdentityMappingsRequest.InlineSource, _Mapping]]=..., identity_mapping_store: _Optional[str]=..., filter: _Optional[str]=..., force: bool=...) -> None:
        ...

class ListIdentityMappingsRequest(_message.Message):
    __slots__ = ('identity_mapping_store', 'page_size', 'page_token')
    IDENTITY_MAPPING_STORE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    identity_mapping_store: str
    page_size: int
    page_token: str

    def __init__(self, identity_mapping_store: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListIdentityMappingsResponse(_message.Message):
    __slots__ = ('identity_mapping_entries', 'next_page_token')
    IDENTITY_MAPPING_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    identity_mapping_entries: _containers.RepeatedCompositeFieldContainer[_identity_mapping_store_pb2.IdentityMappingEntry]
    next_page_token: str

    def __init__(self, identity_mapping_entries: _Optional[_Iterable[_Union[_identity_mapping_store_pb2.IdentityMappingEntry, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ListIdentityMappingStoresRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListIdentityMappingStoresResponse(_message.Message):
    __slots__ = ('identity_mapping_stores', 'next_page_token')
    IDENTITY_MAPPING_STORES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    identity_mapping_stores: _containers.RepeatedCompositeFieldContainer[_identity_mapping_store_pb2.IdentityMappingStore]
    next_page_token: str

    def __init__(self, identity_mapping_stores: _Optional[_Iterable[_Union[_identity_mapping_store_pb2.IdentityMappingStore, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class IdentityMappingEntryOperationMetadata(_message.Message):
    __slots__ = ('success_count', 'failure_count', 'total_count')
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    success_count: int
    failure_count: int
    total_count: int

    def __init__(self, success_count: _Optional[int]=..., failure_count: _Optional[int]=..., total_count: _Optional[int]=...) -> None:
        ...

class DeleteIdentityMappingStoreMetadata(_message.Message):
    __slots__ = ('create_time', 'update_time')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...