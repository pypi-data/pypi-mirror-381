from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import code_pb2 as _code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Job(_message.Message):
    __slots__ = ('name', 'description', 'bucket_list', 'put_object_hold', 'delete_object', 'put_metadata', 'rewrite_object', 'logging_config', 'create_time', 'schedule_time', 'complete_time', 'counters', 'error_summaries', 'state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Job.State]
        RUNNING: _ClassVar[Job.State]
        SUCCEEDED: _ClassVar[Job.State]
        CANCELED: _ClassVar[Job.State]
        FAILED: _ClassVar[Job.State]
    STATE_UNSPECIFIED: Job.State
    RUNNING: Job.State
    SUCCEEDED: Job.State
    CANCELED: Job.State
    FAILED: Job.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BUCKET_LIST_FIELD_NUMBER: _ClassVar[int]
    PUT_OBJECT_HOLD_FIELD_NUMBER: _ClassVar[int]
    DELETE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    PUT_METADATA_FIELD_NUMBER: _ClassVar[int]
    REWRITE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    LOGGING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TIME_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_TIME_FIELD_NUMBER: _ClassVar[int]
    COUNTERS_FIELD_NUMBER: _ClassVar[int]
    ERROR_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    bucket_list: BucketList
    put_object_hold: PutObjectHold
    delete_object: DeleteObject
    put_metadata: PutMetadata
    rewrite_object: RewriteObject
    logging_config: LoggingConfig
    create_time: _timestamp_pb2.Timestamp
    schedule_time: _timestamp_pb2.Timestamp
    complete_time: _timestamp_pb2.Timestamp
    counters: Counters
    error_summaries: _containers.RepeatedCompositeFieldContainer[ErrorSummary]
    state: Job.State

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., bucket_list: _Optional[_Union[BucketList, _Mapping]]=..., put_object_hold: _Optional[_Union[PutObjectHold, _Mapping]]=..., delete_object: _Optional[_Union[DeleteObject, _Mapping]]=..., put_metadata: _Optional[_Union[PutMetadata, _Mapping]]=..., rewrite_object: _Optional[_Union[RewriteObject, _Mapping]]=..., logging_config: _Optional[_Union[LoggingConfig, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., schedule_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., complete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., counters: _Optional[_Union[Counters, _Mapping]]=..., error_summaries: _Optional[_Iterable[_Union[ErrorSummary, _Mapping]]]=..., state: _Optional[_Union[Job.State, str]]=...) -> None:
        ...

class BucketList(_message.Message):
    __slots__ = ('buckets',)

    class Bucket(_message.Message):
        __slots__ = ('bucket', 'prefix_list', 'manifest')
        BUCKET_FIELD_NUMBER: _ClassVar[int]
        PREFIX_LIST_FIELD_NUMBER: _ClassVar[int]
        MANIFEST_FIELD_NUMBER: _ClassVar[int]
        bucket: str
        prefix_list: PrefixList
        manifest: Manifest

        def __init__(self, bucket: _Optional[str]=..., prefix_list: _Optional[_Union[PrefixList, _Mapping]]=..., manifest: _Optional[_Union[Manifest, _Mapping]]=...) -> None:
            ...
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    buckets: _containers.RepeatedCompositeFieldContainer[BucketList.Bucket]

    def __init__(self, buckets: _Optional[_Iterable[_Union[BucketList.Bucket, _Mapping]]]=...) -> None:
        ...

class Manifest(_message.Message):
    __slots__ = ('manifest_location',)
    MANIFEST_LOCATION_FIELD_NUMBER: _ClassVar[int]
    manifest_location: str

    def __init__(self, manifest_location: _Optional[str]=...) -> None:
        ...

class PrefixList(_message.Message):
    __slots__ = ('included_object_prefixes',)
    INCLUDED_OBJECT_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    included_object_prefixes: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, included_object_prefixes: _Optional[_Iterable[str]]=...) -> None:
        ...

class PutObjectHold(_message.Message):
    __slots__ = ('temporary_hold', 'event_based_hold')

    class HoldStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HOLD_STATUS_UNSPECIFIED: _ClassVar[PutObjectHold.HoldStatus]
        SET: _ClassVar[PutObjectHold.HoldStatus]
        UNSET: _ClassVar[PutObjectHold.HoldStatus]
    HOLD_STATUS_UNSPECIFIED: PutObjectHold.HoldStatus
    SET: PutObjectHold.HoldStatus
    UNSET: PutObjectHold.HoldStatus
    TEMPORARY_HOLD_FIELD_NUMBER: _ClassVar[int]
    EVENT_BASED_HOLD_FIELD_NUMBER: _ClassVar[int]
    temporary_hold: PutObjectHold.HoldStatus
    event_based_hold: PutObjectHold.HoldStatus

    def __init__(self, temporary_hold: _Optional[_Union[PutObjectHold.HoldStatus, str]]=..., event_based_hold: _Optional[_Union[PutObjectHold.HoldStatus, str]]=...) -> None:
        ...

class DeleteObject(_message.Message):
    __slots__ = ('permanent_object_deletion_enabled',)
    PERMANENT_OBJECT_DELETION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    permanent_object_deletion_enabled: bool

    def __init__(self, permanent_object_deletion_enabled: bool=...) -> None:
        ...

class RewriteObject(_message.Message):
    __slots__ = ('kms_key',)
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    kms_key: str

    def __init__(self, kms_key: _Optional[str]=...) -> None:
        ...

class PutMetadata(_message.Message):
    __slots__ = ('content_disposition', 'content_encoding', 'content_language', 'content_type', 'cache_control', 'custom_time', 'custom_metadata')

    class CustomMetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    CONTENT_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_ENCODING_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CACHE_CONTROL_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TIME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_METADATA_FIELD_NUMBER: _ClassVar[int]
    content_disposition: str
    content_encoding: str
    content_language: str
    content_type: str
    cache_control: str
    custom_time: str
    custom_metadata: _containers.ScalarMap[str, str]

    def __init__(self, content_disposition: _Optional[str]=..., content_encoding: _Optional[str]=..., content_language: _Optional[str]=..., content_type: _Optional[str]=..., cache_control: _Optional[str]=..., custom_time: _Optional[str]=..., custom_metadata: _Optional[_Mapping[str, str]]=...) -> None:
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

class ErrorLogEntry(_message.Message):
    __slots__ = ('object_uri', 'error_details')
    OBJECT_URI_FIELD_NUMBER: _ClassVar[int]
    ERROR_DETAILS_FIELD_NUMBER: _ClassVar[int]
    object_uri: str
    error_details: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, object_uri: _Optional[str]=..., error_details: _Optional[_Iterable[str]]=...) -> None:
        ...

class Counters(_message.Message):
    __slots__ = ('total_object_count', 'succeeded_object_count', 'failed_object_count')
    TOTAL_OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
    SUCCEEDED_OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
    FAILED_OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
    total_object_count: int
    succeeded_object_count: int
    failed_object_count: int

    def __init__(self, total_object_count: _Optional[int]=..., succeeded_object_count: _Optional[int]=..., failed_object_count: _Optional[int]=...) -> None:
        ...

class LoggingConfig(_message.Message):
    __slots__ = ('log_actions', 'log_action_states')

    class LoggableAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOGGABLE_ACTION_UNSPECIFIED: _ClassVar[LoggingConfig.LoggableAction]
        TRANSFORM: _ClassVar[LoggingConfig.LoggableAction]
    LOGGABLE_ACTION_UNSPECIFIED: LoggingConfig.LoggableAction
    TRANSFORM: LoggingConfig.LoggableAction

    class LoggableActionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOGGABLE_ACTION_STATE_UNSPECIFIED: _ClassVar[LoggingConfig.LoggableActionState]
        SUCCEEDED: _ClassVar[LoggingConfig.LoggableActionState]
        FAILED: _ClassVar[LoggingConfig.LoggableActionState]
    LOGGABLE_ACTION_STATE_UNSPECIFIED: LoggingConfig.LoggableActionState
    SUCCEEDED: LoggingConfig.LoggableActionState
    FAILED: LoggingConfig.LoggableActionState
    LOG_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    LOG_ACTION_STATES_FIELD_NUMBER: _ClassVar[int]
    log_actions: _containers.RepeatedScalarFieldContainer[LoggingConfig.LoggableAction]
    log_action_states: _containers.RepeatedScalarFieldContainer[LoggingConfig.LoggableActionState]

    def __init__(self, log_actions: _Optional[_Iterable[_Union[LoggingConfig.LoggableAction, str]]]=..., log_action_states: _Optional[_Iterable[_Union[LoggingConfig.LoggableActionState, str]]]=...) -> None:
        ...