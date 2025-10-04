from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.geminidataanalytics.v1beta import context_pb2 as _context_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataAnalyticsAgent(_message.Message):
    __slots__ = ('staging_context', 'published_context', 'last_published_context')
    STAGING_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    LAST_PUBLISHED_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    staging_context: _context_pb2.Context
    published_context: _context_pb2.Context
    last_published_context: _context_pb2.Context

    def __init__(self, staging_context: _Optional[_Union[_context_pb2.Context, _Mapping]]=..., published_context: _Optional[_Union[_context_pb2.Context, _Mapping]]=..., last_published_context: _Optional[_Union[_context_pb2.Context, _Mapping]]=...) -> None:
        ...