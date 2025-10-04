from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class EventAllocate(_message.Message):
    __slots__ = ('subscription_id', 'acc_address', 'granted_bytes', 'utilised_bytes')
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GRANTED_BYTES_FIELD_NUMBER: _ClassVar[int]
    UTILISED_BYTES_FIELD_NUMBER: _ClassVar[int]
    subscription_id: int
    acc_address: str
    granted_bytes: str
    utilised_bytes: str

    def __init__(self, subscription_id: _Optional[int]=..., acc_address: _Optional[str]=..., granted_bytes: _Optional[str]=..., utilised_bytes: _Optional[str]=...) -> None:
        ...

class EventCreate(_message.Message):
    __slots__ = ('subscription_id', 'plan_id', 'acc_address', 'price')
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    subscription_id: int
    plan_id: int
    acc_address: str
    price: str

    def __init__(self, subscription_id: _Optional[int]=..., plan_id: _Optional[int]=..., acc_address: _Optional[str]=..., price: _Optional[str]=...) -> None:
        ...

class EventCreateSession(_message.Message):
    __slots__ = ('session_id', 'subscription_id', 'acc_address', 'node_address')
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    subscription_id: int
    acc_address: str
    node_address: str

    def __init__(self, session_id: _Optional[int]=..., subscription_id: _Optional[int]=..., acc_address: _Optional[str]=..., node_address: _Optional[str]=...) -> None:
        ...

class EventEnd(_message.Message):
    __slots__ = ('subscription_id', 'plan_id', 'acc_address')
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    subscription_id: int
    plan_id: int
    acc_address: str

    def __init__(self, subscription_id: _Optional[int]=..., plan_id: _Optional[int]=..., acc_address: _Optional[str]=...) -> None:
        ...

class EventPay(_message.Message):
    __slots__ = ('subscription_id', 'plan_id', 'acc_address', 'prov_address', 'payment', 'staking_reward')
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PROV_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    STAKING_REWARD_FIELD_NUMBER: _ClassVar[int]
    subscription_id: int
    plan_id: int
    acc_address: str
    prov_address: str
    payment: str
    staking_reward: str

    def __init__(self, subscription_id: _Optional[int]=..., plan_id: _Optional[int]=..., acc_address: _Optional[str]=..., prov_address: _Optional[str]=..., payment: _Optional[str]=..., staking_reward: _Optional[str]=...) -> None:
        ...

class EventRenew(_message.Message):
    __slots__ = ('subscription_id', 'plan_id', 'acc_address', 'price')
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    subscription_id: int
    plan_id: int
    acc_address: str
    price: str

    def __init__(self, subscription_id: _Optional[int]=..., plan_id: _Optional[int]=..., acc_address: _Optional[str]=..., price: _Optional[str]=...) -> None:
        ...

class EventUpdateDetails(_message.Message):
    __slots__ = ('subscription_id', 'plan_id', 'acc_address', 'renewal_price_policy')
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_PRICE_POLICY_FIELD_NUMBER: _ClassVar[int]
    subscription_id: int
    plan_id: int
    acc_address: str
    renewal_price_policy: str

    def __init__(self, subscription_id: _Optional[int]=..., plan_id: _Optional[int]=..., acc_address: _Optional[str]=..., renewal_price_policy: _Optional[str]=...) -> None:
        ...

class EventUpdateStatus(_message.Message):
    __slots__ = ('subscription_id', 'plan_id', 'acc_address', 'status')
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    subscription_id: int
    plan_id: int
    acc_address: str
    status: str

    def __init__(self, subscription_id: _Optional[int]=..., plan_id: _Optional[int]=..., acc_address: _Optional[str]=..., status: _Optional[str]=...) -> None:
        ...