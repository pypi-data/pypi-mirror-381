from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GbpAccount(_message.Message):
    __slots__ = ('name', 'gbp_account_id', 'type', 'gbp_account_name', 'listing_count')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[GbpAccount.Type]
        USER: _ClassVar[GbpAccount.Type]
        BUSINESS_ACCOUNT: _ClassVar[GbpAccount.Type]
    TYPE_UNSPECIFIED: GbpAccount.Type
    USER: GbpAccount.Type
    BUSINESS_ACCOUNT: GbpAccount.Type
    NAME_FIELD_NUMBER: _ClassVar[int]
    GBP_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    GBP_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    LISTING_COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    gbp_account_id: str
    type: GbpAccount.Type
    gbp_account_name: str
    listing_count: int

    def __init__(self, name: _Optional[str]=..., gbp_account_id: _Optional[str]=..., type: _Optional[_Union[GbpAccount.Type, str]]=..., gbp_account_name: _Optional[str]=..., listing_count: _Optional[int]=...) -> None:
        ...

class ListGbpAccountsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListGbpAccountsResponse(_message.Message):
    __slots__ = ('gbp_accounts', 'next_page_token')
    GBP_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    gbp_accounts: _containers.RepeatedCompositeFieldContainer[GbpAccount]
    next_page_token: str

    def __init__(self, gbp_accounts: _Optional[_Iterable[_Union[GbpAccount, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class LinkGbpAccountRequest(_message.Message):
    __slots__ = ('parent', 'gbp_email')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GBP_EMAIL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    gbp_email: str

    def __init__(self, parent: _Optional[str]=..., gbp_email: _Optional[str]=...) -> None:
        ...

class LinkGbpAccountResponse(_message.Message):
    __slots__ = ('response',)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _empty_pb2.Empty

    def __init__(self, response: _Optional[_Union[_empty_pb2.Empty, _Mapping]]=...) -> None:
        ...