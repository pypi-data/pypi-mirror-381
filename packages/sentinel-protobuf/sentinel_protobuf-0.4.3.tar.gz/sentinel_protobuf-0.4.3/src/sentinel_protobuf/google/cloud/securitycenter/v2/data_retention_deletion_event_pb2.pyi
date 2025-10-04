from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataRetentionDeletionEvent(_message.Message):
    __slots__ = ('event_detection_time', 'data_object_count', 'max_retention_allowed', 'event_type')

    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_TYPE_UNSPECIFIED: _ClassVar[DataRetentionDeletionEvent.EventType]
        EVENT_TYPE_MAX_TTL_EXCEEDED: _ClassVar[DataRetentionDeletionEvent.EventType]
    EVENT_TYPE_UNSPECIFIED: DataRetentionDeletionEvent.EventType
    EVENT_TYPE_MAX_TTL_EXCEEDED: DataRetentionDeletionEvent.EventType
    EVENT_DETECTION_TIME_FIELD_NUMBER: _ClassVar[int]
    DATA_OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_RETENTION_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    event_detection_time: _timestamp_pb2.Timestamp
    data_object_count: int
    max_retention_allowed: _duration_pb2.Duration
    event_type: DataRetentionDeletionEvent.EventType

    def __init__(self, event_detection_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., data_object_count: _Optional[int]=..., max_retention_allowed: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., event_type: _Optional[_Union[DataRetentionDeletionEvent.EventType, str]]=...) -> None:
        ...