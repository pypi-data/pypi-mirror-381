from gogoproto import gogo_pb2 as _gogo_pb2
from sentinel.node.v3 import params_pb2 as _params_pb2
from sentinel.types.v1 import price_pb2 as _price_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgRegisterNodeRequest(_message.Message):
    __slots__ = ('frm', 'gigabyte_prices', 'hourly_prices', 'remote_addrs')
    FRM_FIELD_NUMBER: _ClassVar[int]
    GIGABYTE_PRICES_FIELD_NUMBER: _ClassVar[int]
    HOURLY_PRICES_FIELD_NUMBER: _ClassVar[int]
    REMOTE_ADDRS_FIELD_NUMBER: _ClassVar[int]
    frm: str
    gigabyte_prices: _containers.RepeatedCompositeFieldContainer[_price_pb2.Price]
    hourly_prices: _containers.RepeatedCompositeFieldContainer[_price_pb2.Price]
    remote_addrs: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, frm: _Optional[str]=..., gigabyte_prices: _Optional[_Iterable[_Union[_price_pb2.Price, _Mapping]]]=..., hourly_prices: _Optional[_Iterable[_Union[_price_pb2.Price, _Mapping]]]=..., remote_addrs: _Optional[_Iterable[str]]=...) -> None:
        ...

class MsgUpdateNodeDetailsRequest(_message.Message):
    __slots__ = ('frm', 'gigabyte_prices', 'hourly_prices', 'remote_addrs')
    FRM_FIELD_NUMBER: _ClassVar[int]
    GIGABYTE_PRICES_FIELD_NUMBER: _ClassVar[int]
    HOURLY_PRICES_FIELD_NUMBER: _ClassVar[int]
    REMOTE_ADDRS_FIELD_NUMBER: _ClassVar[int]
    frm: str
    gigabyte_prices: _containers.RepeatedCompositeFieldContainer[_price_pb2.Price]
    hourly_prices: _containers.RepeatedCompositeFieldContainer[_price_pb2.Price]
    remote_addrs: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, frm: _Optional[str]=..., gigabyte_prices: _Optional[_Iterable[_Union[_price_pb2.Price, _Mapping]]]=..., hourly_prices: _Optional[_Iterable[_Union[_price_pb2.Price, _Mapping]]]=..., remote_addrs: _Optional[_Iterable[str]]=...) -> None:
        ...

class MsgUpdateNodeStatusRequest(_message.Message):
    __slots__ = ('frm', 'status')
    FRM_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    frm: str
    status: _status_pb2.Status

    def __init__(self, frm: _Optional[str]=..., status: _Optional[_Union[_status_pb2.Status, str]]=...) -> None:
        ...

class MsgStartSessionRequest(_message.Message):
    __slots__ = ('frm', 'node_address', 'gigabytes', 'hours', 'max_price')
    FRM_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GIGABYTES_FIELD_NUMBER: _ClassVar[int]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    MAX_PRICE_FIELD_NUMBER: _ClassVar[int]
    frm: str
    node_address: str
    gigabytes: int
    hours: int
    max_price: _price_pb2.Price

    def __init__(self, frm: _Optional[str]=..., node_address: _Optional[str]=..., gigabytes: _Optional[int]=..., hours: _Optional[int]=..., max_price: _Optional[_Union[_price_pb2.Price, _Mapping]]=...) -> None:
        ...

class MsgUpdateParamsRequest(_message.Message):
    __slots__ = ('frm', 'params')
    FRM_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    frm: str
    params: _params_pb2.Params

    def __init__(self, frm: _Optional[str]=..., params: _Optional[_Union[_params_pb2.Params, _Mapping]]=...) -> None:
        ...

class MsgRegisterNodeResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgUpdateNodeDetailsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgUpdateNodeStatusResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgStartSessionResponse(_message.Message):
    __slots__ = ('id',)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int

    def __init__(self, id: _Optional[int]=...) -> None:
        ...

class MsgUpdateParamsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...