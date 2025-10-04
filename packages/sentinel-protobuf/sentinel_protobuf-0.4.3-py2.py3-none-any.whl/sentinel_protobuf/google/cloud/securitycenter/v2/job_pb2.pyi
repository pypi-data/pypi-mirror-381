from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class JobState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOB_STATE_UNSPECIFIED: _ClassVar[JobState]
    PENDING: _ClassVar[JobState]
    RUNNING: _ClassVar[JobState]
    SUCCEEDED: _ClassVar[JobState]
    FAILED: _ClassVar[JobState]
JOB_STATE_UNSPECIFIED: JobState
PENDING: JobState
RUNNING: JobState
SUCCEEDED: JobState
FAILED: JobState

class Job(_message.Message):
    __slots__ = ('name', 'state', 'error_code', 'location')
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: JobState
    error_code: int
    location: str

    def __init__(self, name: _Optional[str]=..., state: _Optional[_Union[JobState, str]]=..., error_code: _Optional[int]=..., location: _Optional[str]=...) -> None:
        ...