from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class AiMaxSearchTermAdCombinationView(_message.Message):
    __slots__ = ('resource_name', 'ad_group', 'search_term', 'landing_page', 'headline')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    AD_GROUP_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TERM_FIELD_NUMBER: _ClassVar[int]
    LANDING_PAGE_FIELD_NUMBER: _ClassVar[int]
    HEADLINE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    ad_group: str
    search_term: str
    landing_page: str
    headline: str

    def __init__(self, resource_name: _Optional[str]=..., ad_group: _Optional[str]=..., search_term: _Optional[str]=..., landing_page: _Optional[str]=..., headline: _Optional[str]=...) -> None:
        ...