from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataFlowEvent(_message.Message):
    __slots__ = ('event_id', 'principal_email', 'operation', 'violated_location', 'event_time')

    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATION_UNSPECIFIED: _ClassVar[DataFlowEvent.Operation]
        READ: _ClassVar[DataFlowEvent.Operation]
        MOVE: _ClassVar[DataFlowEvent.Operation]
        COPY: _ClassVar[DataFlowEvent.Operation]
    OPERATION_UNSPECIFIED: DataFlowEvent.Operation
    READ: DataFlowEvent.Operation
    MOVE: DataFlowEvent.Operation
    COPY: DataFlowEvent.Operation
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    PRINCIPAL_EMAIL_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    VIOLATED_LOCATION_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    event_id: str
    principal_email: str
    operation: DataFlowEvent.Operation
    violated_location: str
    event_time: _timestamp_pb2.Timestamp

    def __init__(self, event_id: _Optional[str]=..., principal_email: _Optional[str]=..., operation: _Optional[_Union[DataFlowEvent.Operation, str]]=..., violated_location: _Optional[str]=..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...