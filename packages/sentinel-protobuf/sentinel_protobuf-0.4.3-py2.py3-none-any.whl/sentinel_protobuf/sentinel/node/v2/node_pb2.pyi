from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Node(_message.Message):
    __slots__ = ('address', 'gigabyte_prices', 'hourly_prices', 'remote_url', 'inactive_at', 'status', 'status_at')
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GIGABYTE_PRICES_FIELD_NUMBER: _ClassVar[int]
    HOURLY_PRICES_FIELD_NUMBER: _ClassVar[int]
    REMOTE_URL_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_AT_FIELD_NUMBER: _ClassVar[int]
    address: str
    gigabyte_prices: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    hourly_prices: _containers.RepeatedCompositeFieldContainer[_coin_pb2.Coin]
    remote_url: str
    inactive_at: _timestamp_pb2.Timestamp
    status: _status_pb2.Status
    status_at: _timestamp_pb2.Timestamp

    def __init__(self, address: _Optional[str]=..., gigabyte_prices: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=..., hourly_prices: _Optional[_Iterable[_Union[_coin_pb2.Coin, _Mapping]]]=..., remote_url: _Optional[str]=..., inactive_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., status: _Optional[_Union[_status_pb2.Status, str]]=..., status_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...