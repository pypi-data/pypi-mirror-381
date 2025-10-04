from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ChannelConnection(_message.Message):
    __slots__ = ('name', 'uid', 'channel', 'create_time', 'update_time', 'activation_token', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ACTIVATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    channel: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    activation_token: str
    labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., channel: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., activation_token: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...