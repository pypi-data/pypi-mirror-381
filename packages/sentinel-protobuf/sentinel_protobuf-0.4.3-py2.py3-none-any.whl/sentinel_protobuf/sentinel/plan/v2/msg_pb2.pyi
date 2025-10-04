from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgCreateRequest(_message.Message):
    __slots__ = ('frm', 'duration', 'gigabytes', 'prices')
    FRM_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    GIGABYTES_FIELD_NUMBER: _ClassVar[int]
    PRICES_FIELD_NUMBER: _ClassVar[int]
    frm: str
    duration: _duration_pb2.Duration
    gigabytes: int
    prices: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]

    def __init__(self, frm: _Optional[str]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., gigabytes: _Optional[int]=..., prices: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=...) -> None:
        ...

class MsgLinkNodeRequest(_message.Message):
    __slots__ = ('frm', 'id', 'node_address')
    FRM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    frm: str
    id: int
    node_address: str

    def __init__(self, frm: _Optional[str]=..., id: _Optional[int]=..., node_address: _Optional[str]=...) -> None:
        ...

class MsgUnlinkNodeRequest(_message.Message):
    __slots__ = ('frm', 'id', 'node_address')
    FRM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    frm: str
    id: int
    node_address: str

    def __init__(self, frm: _Optional[str]=..., id: _Optional[int]=..., node_address: _Optional[str]=...) -> None:
        ...

class MsgUpdateStatusRequest(_message.Message):
    __slots__ = ('frm', 'id', 'status')
    FRM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    frm: str
    id: int
    status: _status_pb2.Status

    def __init__(self, frm: _Optional[str]=..., id: _Optional[int]=..., status: _Optional[_Union[_status_pb2.Status, str]]=...) -> None:
        ...

class MsgSubscribeRequest(_message.Message):
    __slots__ = ('frm', 'id', 'denom')
    FRM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    frm: str
    id: int
    denom: str

    def __init__(self, frm: _Optional[str]=..., id: _Optional[int]=..., denom: _Optional[str]=...) -> None:
        ...

class MsgCreateResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgLinkNodeResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgUnlinkNodeResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgUpdateStatusResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgSubscribeResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...