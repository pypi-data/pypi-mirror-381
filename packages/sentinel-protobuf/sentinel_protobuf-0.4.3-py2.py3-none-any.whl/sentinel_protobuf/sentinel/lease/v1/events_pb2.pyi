from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class EventCreate(_message.Message):
    __slots__ = ('lease_id', 'node_address', 'prov_address', 'max_hours', 'price', 'renewal_price_policy')
    LEASE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MAX_HOURS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_PRICE_POLICY_FIELD_NUMBER: _ClassVar[int]
    lease_id: int
    node_address: str
    prov_address: str
    max_hours: int
    price: str
    renewal_price_policy: str

    def __init__(self, lease_id: _Optional[int]=..., node_address: _Optional[str]=..., prov_address: _Optional[str]=..., max_hours: _Optional[int]=..., price: _Optional[str]=..., renewal_price_policy: _Optional[str]=...) -> None:
        ...

class EventEnd(_message.Message):
    __slots__ = ('lease_id', 'node_address', 'prov_address')
    LEASE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    lease_id: int
    node_address: str
    prov_address: str

    def __init__(self, lease_id: _Optional[int]=..., node_address: _Optional[str]=..., prov_address: _Optional[str]=...) -> None:
        ...

class EventPay(_message.Message):
    __slots__ = ('lease_id', 'node_address', 'prov_address', 'payment', 'staking_reward')
    LEASE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    STAKING_REWARD_FIELD_NUMBER: _ClassVar[int]
    lease_id: int
    node_address: str
    prov_address: str
    payment: str
    staking_reward: str

    def __init__(self, lease_id: _Optional[int]=..., node_address: _Optional[str]=..., prov_address: _Optional[str]=..., payment: _Optional[str]=..., staking_reward: _Optional[str]=...) -> None:
        ...

class EventRefund(_message.Message):
    __slots__ = ('lease_id', 'prov_address', 'value')
    LEASE_ID_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    lease_id: int
    prov_address: str
    value: str

    def __init__(self, lease_id: _Optional[int]=..., prov_address: _Optional[str]=..., value: _Optional[str]=...) -> None:
        ...

class EventRenew(_message.Message):
    __slots__ = ('lease_id', 'node_address', 'prov_address', 'max_hours', 'price')
    LEASE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MAX_HOURS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    lease_id: int
    node_address: str
    prov_address: str
    max_hours: int
    price: str

    def __init__(self, lease_id: _Optional[int]=..., node_address: _Optional[str]=..., prov_address: _Optional[str]=..., max_hours: _Optional[int]=..., price: _Optional[str]=...) -> None:
        ...

class EventUpdateDetails(_message.Message):
    __slots__ = ('lease_id', 'node_address', 'prov_address', 'renewal_price_policy')
    LEASE_ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_PRICE_POLICY_FIELD_NUMBER: _ClassVar[int]
    lease_id: int
    node_address: str
    prov_address: str
    renewal_price_policy: str

    def __init__(self, lease_id: _Optional[int]=..., node_address: _Optional[str]=..., prov_address: _Optional[str]=..., renewal_price_policy: _Optional[str]=...) -> None:
        ...