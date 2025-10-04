from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AccountRelationship(_message.Message):
    __slots__ = ('name', 'provider', 'provider_display_name', 'account_id_alias')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_ALIAS_FIELD_NUMBER: _ClassVar[int]
    name: str
    provider: str
    provider_display_name: str
    account_id_alias: str

    def __init__(self, name: _Optional[str]=..., provider: _Optional[str]=..., provider_display_name: _Optional[str]=..., account_id_alias: _Optional[str]=...) -> None:
        ...

class GetAccountRelationshipRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateAccountRelationshipRequest(_message.Message):
    __slots__ = ('account_relationship', 'update_mask')
    ACCOUNT_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    account_relationship: AccountRelationship
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, account_relationship: _Optional[_Union[AccountRelationship, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListAccountRelationshipsRequest(_message.Message):
    __slots__ = ('parent', 'page_token', 'page_size')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int

    def __init__(self, parent: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class ListAccountRelationshipsResponse(_message.Message):
    __slots__ = ('account_relationships', 'next_page_token')
    ACCOUNT_RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    account_relationships: _containers.RepeatedCompositeFieldContainer[AccountRelationship]
    next_page_token: str

    def __init__(self, account_relationships: _Optional[_Iterable[_Union[AccountRelationship, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...