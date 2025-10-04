from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class JobReference(_message.Message):
    __slots__ = ('project_id', 'job_id', 'location')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    job_id: str
    location: _wrappers_pb2.StringValue

    def __init__(self, project_id: _Optional[str]=..., job_id: _Optional[str]=..., location: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]]=...) -> None:
        ...