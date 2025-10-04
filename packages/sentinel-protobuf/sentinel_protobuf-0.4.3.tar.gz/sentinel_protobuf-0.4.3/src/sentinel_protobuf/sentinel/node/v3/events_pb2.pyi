from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class EventCreate(_message.Message):
    __slots__ = ('node_address', 'gigabyte_prices', 'hourly_prices', 'remote_addrs')
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GIGABYTE_PRICES_FIELD_NUMBER: _ClassVar[int]
    HOURLY_PRICES_FIELD_NUMBER: _ClassVar[int]
    REMOTE_ADDRS_FIELD_NUMBER: _ClassVar[int]
    node_address: str
    gigabyte_prices: str
    hourly_prices: str
    remote_addrs: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, node_address: _Optional[str]=..., gigabyte_prices: _Optional[str]=..., hourly_prices: _Optional[str]=..., remote_addrs: _Optional[_Iterable[str]]=...) -> None:
        ...

class EventPay(_message.Message):
    __slots__ = ('session_id', 'acc_address', 'node_address', 'payment', 'staking_reward')
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    STAKING_REWARD_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    acc_address: str
    node_address: str
    payment: str
    staking_reward: str

    def __init__(self, session_id: _Optional[int]=..., acc_address: _Optional[str]=..., node_address: _Optional[str]=..., payment: _Optional[str]=..., staking_reward: _Optional[str]=...) -> None:
        ...

class EventRefund(_message.Message):
    __slots__ = ('session_id', 'acc_address', 'value')
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    acc_address: str
    value: str

    def __init__(self, session_id: _Optional[int]=..., acc_address: _Optional[str]=..., value: _Optional[str]=...) -> None:
        ...

class EventUpdateDetails(_message.Message):
    __slots__ = ('node_address', 'gigabyte_prices', 'hourly_prices', 'remote_addrs')
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GIGABYTE_PRICES_FIELD_NUMBER: _ClassVar[int]
    HOURLY_PRICES_FIELD_NUMBER: _ClassVar[int]
    REMOTE_ADDRS_FIELD_NUMBER: _ClassVar[int]
    node_address: str
    gigabyte_prices: str
    hourly_prices: str
    remote_addrs: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, node_address: _Optional[str]=..., gigabyte_prices: _Optional[str]=..., hourly_prices: _Optional[str]=..., remote_addrs: _Optional[_Iterable[str]]=...) -> None:
        ...

class EventUpdateStatus(_message.Message):
    __slots__ = ('node_address', 'status')
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    node_address: str
    status: str

    def __init__(self, node_address: _Optional[str]=..., status: _Optional[str]=...) -> None:
        ...

class EventCreateSession(_message.Message):
    __slots__ = ('session_id', 'acc_address', 'node_address', 'price', 'max_bytes', 'max_duration')
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    MAX_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_DURATION_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    acc_address: str
    node_address: str
    price: str
    max_bytes: str
    max_duration: str

    def __init__(self, session_id: _Optional[int]=..., acc_address: _Optional[str]=..., node_address: _Optional[str]=..., price: _Optional[str]=..., max_bytes: _Optional[str]=..., max_duration: _Optional[str]=...) -> None:
        ...