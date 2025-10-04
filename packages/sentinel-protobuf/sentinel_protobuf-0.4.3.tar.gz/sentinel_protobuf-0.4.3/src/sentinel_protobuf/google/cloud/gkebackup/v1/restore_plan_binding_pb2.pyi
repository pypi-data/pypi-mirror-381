from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RestorePlanBinding(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'restore_plan', 'etag', 'backup_plan')
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PLAN_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    BACKUP_PLAN_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    restore_plan: str
    etag: str
    backup_plan: str

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., restore_plan: _Optional[str]=..., etag: _Optional[str]=..., backup_plan: _Optional[str]=...) -> None:
        ...