from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class SearchTermMatchSourceEnum(_message.Message):
    __slots__ = ()

    class SearchTermMatchSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[SearchTermMatchSourceEnum.SearchTermMatchSource]
        UNKNOWN: _ClassVar[SearchTermMatchSourceEnum.SearchTermMatchSource]
        ADVERTISER_PROVIDED_KEYWORD: _ClassVar[SearchTermMatchSourceEnum.SearchTermMatchSource]
        AI_MAX_KEYWORDLESS: _ClassVar[SearchTermMatchSourceEnum.SearchTermMatchSource]
        AI_MAX_BROAD_MATCH: _ClassVar[SearchTermMatchSourceEnum.SearchTermMatchSource]
        DYNAMIC_SEARCH_ADS: _ClassVar[SearchTermMatchSourceEnum.SearchTermMatchSource]
        PERFORMANCE_MAX: _ClassVar[SearchTermMatchSourceEnum.SearchTermMatchSource]
    UNSPECIFIED: SearchTermMatchSourceEnum.SearchTermMatchSource
    UNKNOWN: SearchTermMatchSourceEnum.SearchTermMatchSource
    ADVERTISER_PROVIDED_KEYWORD: SearchTermMatchSourceEnum.SearchTermMatchSource
    AI_MAX_KEYWORDLESS: SearchTermMatchSourceEnum.SearchTermMatchSource
    AI_MAX_BROAD_MATCH: SearchTermMatchSourceEnum.SearchTermMatchSource
    DYNAMIC_SEARCH_ADS: SearchTermMatchSourceEnum.SearchTermMatchSource
    PERFORMANCE_MAX: SearchTermMatchSourceEnum.SearchTermMatchSource

    def __init__(self) -> None:
        ...