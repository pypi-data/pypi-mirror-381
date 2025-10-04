from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LfpProvider(_message.Message):
    __slots__ = ('name', 'region_code', 'display_name')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    region_code: str
    display_name: str

    def __init__(self, name: _Optional[str]=..., region_code: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
        ...

class FindLfpProvidersRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class FindLfpProvidersResponse(_message.Message):
    __slots__ = ('lfp_providers', 'next_page_token')
    LFP_PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    lfp_providers: _containers.RepeatedCompositeFieldContainer[LfpProvider]
    next_page_token: str

    def __init__(self, lfp_providers: _Optional[_Iterable[_Union[LfpProvider, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class LinkLfpProviderRequest(_message.Message):
    __slots__ = ('name', 'external_account_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    external_account_id: str

    def __init__(self, name: _Optional[str]=..., external_account_id: _Optional[str]=...) -> None:
        ...

class LinkLfpProviderResponse(_message.Message):
    __slots__ = ('response',)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _empty_pb2.Empty

    def __init__(self, response: _Optional[_Union[_empty_pb2.Empty, _Mapping]]=...) -> None:
        ...