from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Payout(_message.Message):
    __slots__ = ('id', 'address', 'node_address', 'hours', 'price', 'next_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    NEXT_AT_FIELD_NUMBER: _ClassVar[int]
    id: int
    address: str
    node_address: str
    hours: int
    price: _coin_pb2.Coin
    next_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[int]=..., address: _Optional[str]=..., node_address: _Optional[str]=..., hours: _Optional[int]=..., price: _Optional[_Union[_coin_pb2.Coin, _Mapping]]=..., next_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...