from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateDataAccessLabelRequest(_message.Message):
    __slots__ = ('parent', 'data_access_label', 'data_access_label_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATA_ACCESS_LABEL_FIELD_NUMBER: _ClassVar[int]
    DATA_ACCESS_LABEL_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    data_access_label: DataAccessLabel
    data_access_label_id: str

    def __init__(self, parent: _Optional[str]=..., data_access_label: _Optional[_Union[DataAccessLabel, _Mapping]]=..., data_access_label_id: _Optional[str]=...) -> None:
        ...

class GetDataAccessLabelRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDataAccessLabelsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListDataAccessLabelsResponse(_message.Message):
    __slots__ = ('data_access_labels', 'next_page_token')
    DATA_ACCESS_LABELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data_access_labels: _containers.RepeatedCompositeFieldContainer[DataAccessLabel]
    next_page_token: str

    def __init__(self, data_access_labels: _Optional[_Iterable[_Union[DataAccessLabel, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateDataAccessLabelRequest(_message.Message):
    __slots__ = ('data_access_label', 'update_mask')
    DATA_ACCESS_LABEL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    data_access_label: DataAccessLabel
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, data_access_label: _Optional[_Union[DataAccessLabel, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteDataAccessLabelRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateDataAccessScopeRequest(_message.Message):
    __slots__ = ('parent', 'data_access_scope', 'data_access_scope_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATA_ACCESS_SCOPE_FIELD_NUMBER: _ClassVar[int]
    DATA_ACCESS_SCOPE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    data_access_scope: DataAccessScope
    data_access_scope_id: str

    def __init__(self, parent: _Optional[str]=..., data_access_scope: _Optional[_Union[DataAccessScope, _Mapping]]=..., data_access_scope_id: _Optional[str]=...) -> None:
        ...

class GetDataAccessScopeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDataAccessScopesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListDataAccessScopesResponse(_message.Message):
    __slots__ = ('data_access_scopes', 'global_data_access_scope_granted', 'next_page_token')
    DATA_ACCESS_SCOPES_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_DATA_ACCESS_SCOPE_GRANTED_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data_access_scopes: _containers.RepeatedCompositeFieldContainer[DataAccessScope]
    global_data_access_scope_granted: bool
    next_page_token: str

    def __init__(self, data_access_scopes: _Optional[_Iterable[_Union[DataAccessScope, _Mapping]]]=..., global_data_access_scope_granted: bool=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateDataAccessScopeRequest(_message.Message):
    __slots__ = ('data_access_scope', 'update_mask')
    DATA_ACCESS_SCOPE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    data_access_scope: DataAccessScope
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, data_access_scope: _Optional[_Union[DataAccessScope, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteDataAccessScopeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DataAccessLabel(_message.Message):
    __slots__ = ('udm_query', 'name', 'display_name', 'create_time', 'update_time', 'author', 'last_editor', 'description')
    UDM_QUERY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    LAST_EDITOR_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    udm_query: str
    name: str
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    author: str
    last_editor: str
    description: str

    def __init__(self, udm_query: _Optional[str]=..., name: _Optional[str]=..., display_name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., author: _Optional[str]=..., last_editor: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class DataAccessScope(_message.Message):
    __slots__ = ('name', 'allowed_data_access_labels', 'denied_data_access_labels', 'display_name', 'create_time', 'update_time', 'author', 'last_editor', 'description', 'allow_all')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_DATA_ACCESS_LABELS_FIELD_NUMBER: _ClassVar[int]
    DENIED_DATA_ACCESS_LABELS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    LAST_EDITOR_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ALLOW_ALL_FIELD_NUMBER: _ClassVar[int]
    name: str
    allowed_data_access_labels: _containers.RepeatedCompositeFieldContainer[DataAccessLabelReference]
    denied_data_access_labels: _containers.RepeatedCompositeFieldContainer[DataAccessLabelReference]
    display_name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    author: str
    last_editor: str
    description: str
    allow_all: bool

    def __init__(self, name: _Optional[str]=..., allowed_data_access_labels: _Optional[_Iterable[_Union[DataAccessLabelReference, _Mapping]]]=..., denied_data_access_labels: _Optional[_Iterable[_Union[DataAccessLabelReference, _Mapping]]]=..., display_name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., author: _Optional[str]=..., last_editor: _Optional[str]=..., description: _Optional[str]=..., allow_all: bool=...) -> None:
        ...

class DataAccessLabelReference(_message.Message):
    __slots__ = ('data_access_label', 'log_type', 'asset_namespace', 'ingestion_label', 'display_name')
    DATA_ACCESS_LABEL_FIELD_NUMBER: _ClassVar[int]
    LOG_TYPE_FIELD_NUMBER: _ClassVar[int]
    ASSET_NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    INGESTION_LABEL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    data_access_label: str
    log_type: str
    asset_namespace: str
    ingestion_label: IngestionLabel
    display_name: str

    def __init__(self, data_access_label: _Optional[str]=..., log_type: _Optional[str]=..., asset_namespace: _Optional[str]=..., ingestion_label: _Optional[_Union[IngestionLabel, _Mapping]]=..., display_name: _Optional[str]=...) -> None:
        ...

class IngestionLabel(_message.Message):
    __slots__ = ('ingestion_label_key', 'ingestion_label_value')
    INGESTION_LABEL_KEY_FIELD_NUMBER: _ClassVar[int]
    INGESTION_LABEL_VALUE_FIELD_NUMBER: _ClassVar[int]
    ingestion_label_key: str
    ingestion_label_value: str

    def __init__(self, ingestion_label_key: _Optional[str]=..., ingestion_label_value: _Optional[str]=...) -> None:
        ...