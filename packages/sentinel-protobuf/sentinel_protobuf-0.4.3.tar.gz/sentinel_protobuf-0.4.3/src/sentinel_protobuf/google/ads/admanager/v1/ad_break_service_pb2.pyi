from google.ads.admanager.v1 import ad_break_messages_pb2 as _ad_break_messages_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetAdBreakRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListAdBreaksRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by', 'skip')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    skip: int

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., skip: _Optional[int]=...) -> None:
        ...

class ListAdBreaksResponse(_message.Message):
    __slots__ = ('ad_breaks', 'next_page_token', 'total_size')
    AD_BREAKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    ad_breaks: _containers.RepeatedCompositeFieldContainer[_ad_break_messages_pb2.AdBreak]
    next_page_token: str
    total_size: int

    def __init__(self, ad_breaks: _Optional[_Iterable[_Union[_ad_break_messages_pb2.AdBreak, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class CreateAdBreakRequest(_message.Message):
    __slots__ = ('parent', 'ad_break')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    AD_BREAK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    ad_break: _ad_break_messages_pb2.AdBreak

    def __init__(self, parent: _Optional[str]=..., ad_break: _Optional[_Union[_ad_break_messages_pb2.AdBreak, _Mapping]]=...) -> None:
        ...

class UpdateAdBreakRequest(_message.Message):
    __slots__ = ('ad_break', 'update_mask')
    AD_BREAK_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ad_break: _ad_break_messages_pb2.AdBreak
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, ad_break: _Optional[_Union[_ad_break_messages_pb2.AdBreak, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteAdBreakRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...