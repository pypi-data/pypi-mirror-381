from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from sentinel.types.v1 import price_pb2 as _price_pb2
from sentinel.types.v1 import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Node(_message.Message):
    __slots__ = ('address', 'gigabyte_prices', 'hourly_prices', 'remote_addrs', 'inactive_at', 'status', 'status_at')
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    GIGABYTE_PRICES_FIELD_NUMBER: _ClassVar[int]
    HOURLY_PRICES_FIELD_NUMBER: _ClassVar[int]
    REMOTE_ADDRS_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_AT_FIELD_NUMBER: _ClassVar[int]
    address: str
    gigabyte_prices: _containers.RepeatedCompositeFieldContainer[_price_pb2.Price]
    hourly_prices: _containers.RepeatedCompositeFieldContainer[_price_pb2.Price]
    remote_addrs: _containers.RepeatedScalarFieldContainer[str]
    inactive_at: _timestamp_pb2.Timestamp
    status: _status_pb2.Status
    status_at: _timestamp_pb2.Timestamp

    def __init__(self, address: _Optional[str]=..., gigabyte_prices: _Optional[_Iterable[_Union[_price_pb2.Price, _Mapping]]]=..., hourly_prices: _Optional[_Iterable[_Union[_price_pb2.Price, _Mapping]]]=..., remote_addrs: _Optional[_Iterable[str]]=..., inactive_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., status: _Optional[_Union[_status_pb2.Status, str]]=..., status_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...