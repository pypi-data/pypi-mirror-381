from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class EventCreate(_message.Message):
    __slots__ = ('plan_id', 'prov_address', 'bytes', 'duration', 'prices', 'private')
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    PRICES_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_FIELD_NUMBER: _ClassVar[int]
    plan_id: int
    prov_address: str
    bytes: str
    duration: str
    prices: str
    private: bool

    def __init__(self, plan_id: _Optional[int]=..., prov_address: _Optional[str]=..., bytes: _Optional[str]=..., duration: _Optional[str]=..., prices: _Optional[str]=..., private: bool=...) -> None:
        ...

class EventLinkNode(_message.Message):
    __slots__ = ('plan_id', 'prov_address', 'node_address')
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    plan_id: int
    prov_address: str
    node_address: str

    def __init__(self, plan_id: _Optional[int]=..., prov_address: _Optional[str]=..., node_address: _Optional[str]=...) -> None:
        ...

class EventUnlinkNode(_message.Message):
    __slots__ = ('plan_id', 'prov_address', 'node_address')
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    plan_id: int
    prov_address: str
    node_address: str

    def __init__(self, plan_id: _Optional[int]=..., prov_address: _Optional[str]=..., node_address: _Optional[str]=...) -> None:
        ...

class EventUpdateDetails(_message.Message):
    __slots__ = ('plan_id', 'prov_address', 'private')
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_FIELD_NUMBER: _ClassVar[int]
    plan_id: int
    prov_address: str
    private: bool

    def __init__(self, plan_id: _Optional[int]=..., prov_address: _Optional[str]=..., private: bool=...) -> None:
        ...

class EventUpdateStatus(_message.Message):
    __slots__ = ('plan_id', 'prov_address', 'status')
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    plan_id: int
    prov_address: str
    status: str

    def __init__(self, plan_id: _Optional[int]=..., prov_address: _Optional[str]=..., status: _Optional[str]=...) -> None:
        ...