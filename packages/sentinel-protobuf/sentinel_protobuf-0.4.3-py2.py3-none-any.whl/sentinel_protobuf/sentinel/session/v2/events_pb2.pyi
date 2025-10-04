from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EventStart(_message.Message):
    __slots__ = ('address', 'node_address', 'id', 'plan_id', 'subscription_id')
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    address: str
    node_address: str
    id: int
    plan_id: int
    subscription_id: int

    def __init__(self, address: _Optional[str]=..., node_address: _Optional[str]=..., id: _Optional[int]=..., plan_id: _Optional[int]=..., subscription_id: _Optional[int]=...) -> None:
        ...

class EventUpdateDetails(_message.Message):
    __slots__ = ('address', 'node_address', 'id', 'plan_id', 'subscription_id')
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    address: str
    node_address: str
    id: int
    plan_id: int
    subscription_id: int

    def __init__(self, address: _Optional[str]=..., node_address: _Optional[str]=..., id: _Optional[int]=..., plan_id: _Optional[int]=..., subscription_id: _Optional[int]=...) -> None:
        ...

class EventUpdateStatus(_message.Message):
    __slots__ = ('status', 'address', 'node_address', 'id', 'plan_id', 'subscription_id')
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    status: _status_pb2.Status
    address: str
    node_address: str
    id: int
    plan_id: int
    subscription_id: int

    def __init__(self, status: _Optional[_Union[_status_pb2.Status, str]]=..., address: _Optional[str]=..., node_address: _Optional[str]=..., id: _Optional[int]=..., plan_id: _Optional[int]=..., subscription_id: _Optional[int]=...) -> None:
        ...