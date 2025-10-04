from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ('max_gigabytes', 'min_gigabytes', 'max_hours', 'min_hours', 'proof_verification_enabled', 'staking_share', 'status_timeout')
    MAX_GIGABYTES_FIELD_NUMBER: _ClassVar[int]
    MIN_GIGABYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_HOURS_FIELD_NUMBER: _ClassVar[int]
    MIN_HOURS_FIELD_NUMBER: _ClassVar[int]
    PROOF_VERIFICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    STAKING_SHARE_FIELD_NUMBER: _ClassVar[int]
    STATUS_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    max_gigabytes: int
    min_gigabytes: int
    max_hours: int
    min_hours: int
    proof_verification_enabled: bool
    staking_share: str
    status_timeout: _duration_pb2.Duration

    def __init__(self, max_gigabytes: _Optional[int]=..., min_gigabytes: _Optional[int]=..., max_hours: _Optional[int]=..., min_hours: _Optional[int]=..., proof_verification_enabled: bool=..., staking_share: _Optional[str]=..., status_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...