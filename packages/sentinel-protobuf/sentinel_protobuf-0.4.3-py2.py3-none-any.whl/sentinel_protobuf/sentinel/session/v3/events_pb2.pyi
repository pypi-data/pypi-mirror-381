from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class EventEnd(_message.Message):
    __slots__ = ('session_id', 'acc_address', 'node_address')
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    acc_address: str
    node_address: str

    def __init__(self, session_id: _Optional[int]=..., acc_address: _Optional[str]=..., node_address: _Optional[str]=...) -> None:
        ...

class EventUpdateDetails(_message.Message):
    __slots__ = ('session_id', 'acc_address', 'node_address', 'download_bytes', 'upload_bytes', 'duration')
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_BYTES_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_BYTES_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    acc_address: str
    node_address: str
    download_bytes: str
    upload_bytes: str
    duration: str

    def __init__(self, session_id: _Optional[int]=..., acc_address: _Optional[str]=..., node_address: _Optional[str]=..., download_bytes: _Optional[str]=..., upload_bytes: _Optional[str]=..., duration: _Optional[str]=...) -> None:
        ...

class EventUpdateStatus(_message.Message):
    __slots__ = ('session_id', 'acc_address', 'node_address', 'status')
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ACC_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NODE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    session_id: int
    acc_address: str
    node_address: str
    status: str

    def __init__(self, session_id: _Optional[int]=..., acc_address: _Optional[str]=..., node_address: _Optional[str]=..., status: _Optional[str]=...) -> None:
        ...