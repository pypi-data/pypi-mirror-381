from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1 import user_license_pb2 as _user_license_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListUserLicensesRequest(_message.Message):
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

class ListUserLicensesResponse(_message.Message):
    __slots__ = ('user_licenses', 'next_page_token')
    USER_LICENSES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    user_licenses: _containers.RepeatedCompositeFieldContainer[_user_license_pb2.UserLicense]
    next_page_token: str

    def __init__(self, user_licenses: _Optional[_Iterable[_Union[_user_license_pb2.UserLicense, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class BatchUpdateUserLicensesRequest(_message.Message):
    __slots__ = ('inline_source', 'parent', 'delete_unassigned_user_licenses')

    class InlineSource(_message.Message):
        __slots__ = ('user_licenses', 'update_mask')
        USER_LICENSES_FIELD_NUMBER: _ClassVar[int]
        UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
        user_licenses: _containers.RepeatedCompositeFieldContainer[_user_license_pb2.UserLicense]
        update_mask: _field_mask_pb2.FieldMask

        def __init__(self, user_licenses: _Optional[_Iterable[_Union[_user_license_pb2.UserLicense, _Mapping]]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
            ...
    INLINE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DELETE_UNASSIGNED_USER_LICENSES_FIELD_NUMBER: _ClassVar[int]
    inline_source: BatchUpdateUserLicensesRequest.InlineSource
    parent: str
    delete_unassigned_user_licenses: bool

    def __init__(self, inline_source: _Optional[_Union[BatchUpdateUserLicensesRequest.InlineSource, _Mapping]]=..., parent: _Optional[str]=..., delete_unassigned_user_licenses: bool=...) -> None:
        ...

class BatchUpdateUserLicensesMetadata(_message.Message):
    __slots__ = ('create_time', 'update_time', 'success_count', 'failure_count')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    success_count: int
    failure_count: int

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., success_count: _Optional[int]=..., failure_count: _Optional[int]=...) -> None:
        ...

class BatchUpdateUserLicensesResponse(_message.Message):
    __slots__ = ('user_licenses', 'error_samples')
    USER_LICENSES_FIELD_NUMBER: _ClassVar[int]
    ERROR_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    user_licenses: _containers.RepeatedCompositeFieldContainer[_user_license_pb2.UserLicense]
    error_samples: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]

    def __init__(self, user_licenses: _Optional[_Iterable[_Union[_user_license_pb2.UserLicense, _Mapping]]]=..., error_samples: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]]=...) -> None:
        ...