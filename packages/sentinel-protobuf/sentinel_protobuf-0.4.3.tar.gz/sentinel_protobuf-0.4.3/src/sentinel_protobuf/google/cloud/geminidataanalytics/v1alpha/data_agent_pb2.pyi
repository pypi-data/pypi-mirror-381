from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.geminidataanalytics.v1alpha import data_analytics_agent_pb2 as _data_analytics_agent_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataAgent(_message.Message):
    __slots__ = ('data_analytics_agent', 'name', 'display_name', 'description', 'labels', 'create_time', 'update_time', 'delete_time', 'purge_time')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    DATA_ANALYTICS_AGENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    PURGE_TIME_FIELD_NUMBER: _ClassVar[int]
    data_analytics_agent: _data_analytics_agent_pb2.DataAnalyticsAgent
    name: str
    display_name: str
    description: str
    labels: _containers.ScalarMap[str, str]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    delete_time: _timestamp_pb2.Timestamp
    purge_time: _timestamp_pb2.Timestamp

    def __init__(self, data_analytics_agent: _Optional[_Union[_data_analytics_agent_pb2.DataAnalyticsAgent, _Mapping]]=..., name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., purge_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...