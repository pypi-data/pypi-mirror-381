from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class ProgrammaticBuyer(_message.Message):
    __slots__ = ('name', 'buyer_account_id', 'display_name', 'parent_account_id', 'partner_client_id', 'agency', 'preferred_deals_enabled', 'programmatic_guaranteed_enabled')
    NAME_FIELD_NUMBER: _ClassVar[int]
    BUYER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    PARTNER_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    AGENCY_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_DEALS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PROGRAMMATIC_GUARANTEED_ENABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    buyer_account_id: int
    display_name: str
    parent_account_id: int
    partner_client_id: str
    agency: bool
    preferred_deals_enabled: bool
    programmatic_guaranteed_enabled: bool

    def __init__(self, name: _Optional[str]=..., buyer_account_id: _Optional[int]=..., display_name: _Optional[str]=..., parent_account_id: _Optional[int]=..., partner_client_id: _Optional[str]=..., agency: bool=..., preferred_deals_enabled: bool=..., programmatic_guaranteed_enabled: bool=...) -> None:
        ...