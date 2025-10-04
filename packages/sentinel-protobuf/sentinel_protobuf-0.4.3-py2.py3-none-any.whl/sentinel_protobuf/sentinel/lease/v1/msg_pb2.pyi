from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.lease.v1 import params_pb2 as _params_pb2
from sentinel.types.v1 import price_pb2 as _price_pb2
from sentinel.types.v1 import renewal_pb2 as _renewal_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgEndLeaseRequest(_message.Message):
    __slots__ = ('frm', 'id')
    FRM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    frm: str
    id: int

    def __init__(self, frm: _Optional[str]=..., id: _Optional[int]=...) -> None:
        ...

class MsgRenewLeaseRequest(_message.Message):
    __slots__ = ('frm', 'id', 'hours', 'max_price')
    FRM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    MAX_PRICE_FIELD_NUMBER: _ClassVar[int]
    frm: str
    id: int
    hours: int
    max_price: _price_pb2.Price

    def __init__(self, frm: _Optional[str]=..., id: _Optional[int]=..., hours: _Optional[int]=..., max_price: _Optional[_Union[_price_pb2.Price, _Mapping]]=...) -> None:
        ...

class MsgStartLeaseRequest(_message.Message):
    __slots__ = ('frm', 'node_address', 'hours', 'max_price', 'renewal_price_policy')
    FRM_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    MAX_PRICE_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_PRICE_POLICY_FIELD_NUMBER: _ClassVar[int]
    frm: str
    node_address: str
    hours: int
    max_price: _price_pb2.Price
    renewal_price_policy: _renewal_pb2.RenewalPricePolicy

    def __init__(self, frm: _Optional[str]=..., node_address: _Optional[str]=..., hours: _Optional[int]=..., max_price: _Optional[_Union[_price_pb2.Price, _Mapping]]=..., renewal_price_policy: _Optional[_Union[_renewal_pb2.RenewalPricePolicy, str]]=...) -> None:
        ...

class MsgUpdateLeaseRequest(_message.Message):
    __slots__ = ('frm', 'id', 'renewal_price_policy')
    FRM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_PRICE_POLICY_FIELD_NUMBER: _ClassVar[int]
    frm: str
    id: int
    renewal_price_policy: _renewal_pb2.RenewalPricePolicy

    def __init__(self, frm: _Optional[str]=..., id: _Optional[int]=..., renewal_price_policy: _Optional[_Union[_renewal_pb2.RenewalPricePolicy, str]]=...) -> None:
        ...

class MsgUpdateParamsRequest(_message.Message):
    __slots__ = ('frm', 'params')
    FRM_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    frm: str
    params: _params_pb2.Params

    def __init__(self, frm: _Optional[str]=..., params: _Optional[_Union[_params_pb2.Params, _Mapping]]=...) -> None:
        ...

class MsgEndLeaseResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgRenewLeaseResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgStartLeaseResponse(_message.Message):
    __slots__ = ('id',)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int

    def __init__(self, id: _Optional[int]=...) -> None:
        ...

class MsgUpdateLeaseResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgUpdateParamsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...