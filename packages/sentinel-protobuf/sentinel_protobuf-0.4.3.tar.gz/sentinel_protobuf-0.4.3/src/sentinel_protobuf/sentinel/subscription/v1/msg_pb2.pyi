from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MsgAddQuotaRequest(_message.Message):
    __slots__ = ('frm', 'id', 'address', 'bytes')
    FRM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    frm: str
    id: int
    address: str
    bytes: str

    def __init__(self, frm: _Optional[str]=..., id: _Optional[int]=..., address: _Optional[str]=..., bytes: _Optional[str]=...) -> None:
        ...

class MsgCancelRequest(_message.Message):
    __slots__ = ('frm', 'id')
    FRM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    frm: str
    id: int

    def __init__(self, frm: _Optional[str]=..., id: _Optional[int]=...) -> None:
        ...

class MsgSubscribeToNodeRequest(_message.Message):
    __slots__ = ('frm', 'address', 'deposit')
    FRM_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_FIELD_NUMBER: _ClassVar[int]
    frm: str
    address: str
    deposit: _coin_pb2.Coin

    def __init__(self, frm: _Optional[str]=..., address: _Optional[str]=..., deposit: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=...) -> None:
        ...

class MsgSubscribeToPlanRequest(_message.Message):
    __slots__ = ('frm', 'id', 'denom')
    FRM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DENOM_FIELD_NUMBER: _ClassVar[int]
    frm: str
    id: int
    denom: str

    def __init__(self, frm: _Optional[str]=..., id: _Optional[int]=..., denom: _Optional[str]=...) -> None:
        ...

class MsgUpdateQuotaRequest(_message.Message):
    __slots__ = ('frm', 'id', 'address', 'bytes')
    FRM_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    frm: str
    id: int
    address: str
    bytes: str

    def __init__(self, frm: _Optional[str]=..., id: _Optional[int]=..., address: _Optional[str]=..., bytes: _Optional[str]=...) -> None:
        ...

class MsgAddQuotaResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgCancelResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgSubscribeToNodeResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgSubscribeToPlanResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MsgUpdateQuotaResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...