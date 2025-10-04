from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import code_pb2 as _code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TransferType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSFER_TYPE_UNSPECIFIED: _ClassVar[TransferType]
    IMPORT: _ClassVar[TransferType]
    EXPORT: _ClassVar[TransferType]
TRANSFER_TYPE_UNSPECIFIED: TransferType
IMPORT: TransferType
EXPORT: TransferType

class ImportDataRequest(_message.Message):
    __slots__ = ('gcs_path', 'lustre_path', 'name', 'request_id', 'service_account')
    GCS_PATH_FIELD_NUMBER: _ClassVar[int]
    LUSTRE_PATH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    gcs_path: GcsPath
    lustre_path: LustrePath
    name: str
    request_id: str
    service_account: str

    def __init__(self, gcs_path: _Optional[_Union[GcsPath, _Mapping]]=..., lustre_path: _Optional[_Union[LustrePath, _Mapping]]=..., name: _Optional[str]=..., request_id: _Optional[str]=..., service_account: _Optional[str]=...) -> None:
        ...

class ExportDataRequest(_message.Message):
    __slots__ = ('lustre_path', 'gcs_path', 'name', 'request_id', 'service_account')
    LUSTRE_PATH_FIELD_NUMBER: _ClassVar[int]
    GCS_PATH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    lustre_path: LustrePath
    gcs_path: GcsPath
    name: str
    request_id: str
    service_account: str

    def __init__(self, lustre_path: _Optional[_Union[LustrePath, _Mapping]]=..., gcs_path: _Optional[_Union[GcsPath, _Mapping]]=..., name: _Optional[str]=..., request_id: _Optional[str]=..., service_account: _Optional[str]=...) -> None:
        ...

class ExportDataResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ImportDataResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ExportDataMetadata(_message.Message):
    __slots__ = ('operation_metadata', 'create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    OPERATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    operation_metadata: TransferOperationMetadata
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, operation_metadata: _Optional[_Union[TransferOperationMetadata, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class ImportDataMetadata(_message.Message):
    __slots__ = ('operation_metadata', 'create_time', 'end_time', 'target', 'status_message', 'requested_cancellation', 'api_version')
    OPERATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    operation_metadata: TransferOperationMetadata
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, operation_metadata: _Optional[_Union[TransferOperationMetadata, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class GcsPath(_message.Message):
    __slots__ = ('uri',)
    URI_FIELD_NUMBER: _ClassVar[int]
    uri: str

    def __init__(self, uri: _Optional[str]=...) -> None:
        ...

class LustrePath(_message.Message):
    __slots__ = ('path',)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str

    def __init__(self, path: _Optional[str]=...) -> None:
        ...

class TransferCounters(_message.Message):
    __slots__ = ('found_objects_count', 'bytes_found_count', 'objects_skipped_count', 'bytes_skipped_count', 'objects_copied_count', 'bytes_copied_count', 'objects_failed_count', 'bytes_failed_count')
    FOUND_OBJECTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    BYTES_FOUND_COUNT_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_SKIPPED_COUNT_FIELD_NUMBER: _ClassVar[int]
    BYTES_SKIPPED_COUNT_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_COPIED_COUNT_FIELD_NUMBER: _ClassVar[int]
    BYTES_COPIED_COUNT_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FAILED_COUNT_FIELD_NUMBER: _ClassVar[int]
    BYTES_FAILED_COUNT_FIELD_NUMBER: _ClassVar[int]
    found_objects_count: int
    bytes_found_count: int
    objects_skipped_count: int
    bytes_skipped_count: int
    objects_copied_count: int
    bytes_copied_count: int
    objects_failed_count: int
    bytes_failed_count: int

    def __init__(self, found_objects_count: _Optional[int]=..., bytes_found_count: _Optional[int]=..., objects_skipped_count: _Optional[int]=..., bytes_skipped_count: _Optional[int]=..., objects_copied_count: _Optional[int]=..., bytes_copied_count: _Optional[int]=..., objects_failed_count: _Optional[int]=..., bytes_failed_count: _Optional[int]=...) -> None:
        ...

class ErrorLogEntry(_message.Message):
    __slots__ = ('uri', 'error_details')
    URI_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
    uri: str
    error_details: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, uri: _Optional[str]=..., error_details: _Optional[_Iterable[str]]=...) -> None:
        ...

class ErrorSummary(_message.Message):
    __slots__ = ('error_code', 'error_count', 'error_log_entries')
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_LOG_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    error_code: _code_pb2.Code
    error_count: int
    error_log_entries: _containers.RepeatedCompositeFieldContainer[ErrorLogEntry]

    def __init__(self, error_code: _Optional[_Union[_code_pb2.Code, str]]=..., error_count: _Optional[int]=..., error_log_entries: _Optional[_Iterable[_Union[ErrorLogEntry, _Mapping]]]=...) -> None:
        ...

class TransferOperationMetadata(_message.Message):
    __slots__ = ('source_lustre_path', 'source_gcs_path', 'destination_gcs_path', 'destination_lustre_path', 'counters', 'transfer_type', 'error_summaries')
    SOURCE_LUSTRE_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_GCS_PATH_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_GCS_PATH_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_LUSTRE_PATH_FIELD_NUMBER: _ClassVar[int]
    COUNTERS_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    source_lustre_path: LustrePath
    source_gcs_path: GcsPath
    destination_gcs_path: GcsPath
    destination_lustre_path: LustrePath
    counters: TransferCounters
    transfer_type: TransferType
    error_summaries: _containers.RepeatedCompositeFieldContainer[ErrorSummary]

    def __init__(self, source_lustre_path: _Optional[_Union[LustrePath, _Mapping]]=..., source_gcs_path: _Optional[_Union[GcsPath, _Mapping]]=..., destination_gcs_path: _Optional[_Union[GcsPath, _Mapping]]=..., destination_lustre_path: _Optional[_Union[LustrePath, _Mapping]]=..., counters: _Optional[_Union[TransferCounters, _Mapping]]=..., transfer_type: _Optional[_Union[TransferType, str]]=..., error_summaries: _Optional[_Iterable[_Union[ErrorSummary, _Mapping]]]=...) -> None:
        ...