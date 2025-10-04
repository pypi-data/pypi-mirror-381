from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PrivateAuction(_message.Message):
    __slots__ = ('name', 'private_auction_id', 'display_name', 'description', 'seller_contact_users', 'archived', 'create_time', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_AUCTION_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SELLER_CONTACT_USERS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    private_auction_id: int
    display_name: str
    description: str
    seller_contact_users: _containers.RepeatedScalarFieldContainer[str]
    archived: bool
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., private_auction_id: _Optional[int]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., seller_contact_users: _Optional[_Iterable[str]]=..., archived: bool=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...