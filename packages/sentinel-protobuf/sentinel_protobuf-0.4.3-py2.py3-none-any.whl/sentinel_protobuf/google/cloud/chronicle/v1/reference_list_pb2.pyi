from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ReferenceListSyntaxType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REFERENCE_LIST_SYNTAX_TYPE_UNSPECIFIED: _ClassVar[ReferenceListSyntaxType]
    REFERENCE_LIST_SYNTAX_TYPE_PLAIN_TEXT_STRING: _ClassVar[ReferenceListSyntaxType]
    REFERENCE_LIST_SYNTAX_TYPE_REGEX: _ClassVar[ReferenceListSyntaxType]
    REFERENCE_LIST_SYNTAX_TYPE_CIDR: _ClassVar[ReferenceListSyntaxType]

class ReferenceListView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REFERENCE_LIST_VIEW_UNSPECIFIED: _ClassVar[ReferenceListView]
    REFERENCE_LIST_VIEW_BASIC: _ClassVar[ReferenceListView]
    REFERENCE_LIST_VIEW_FULL: _ClassVar[ReferenceListView]
REFERENCE_LIST_SYNTAX_TYPE_UNSPECIFIED: ReferenceListSyntaxType
REFERENCE_LIST_SYNTAX_TYPE_PLAIN_TEXT_STRING: ReferenceListSyntaxType
REFERENCE_LIST_SYNTAX_TYPE_REGEX: ReferenceListSyntaxType
REFERENCE_LIST_SYNTAX_TYPE_CIDR: ReferenceListSyntaxType
REFERENCE_LIST_VIEW_UNSPECIFIED: ReferenceListView
REFERENCE_LIST_VIEW_BASIC: ReferenceListView
REFERENCE_LIST_VIEW_FULL: ReferenceListView

class ScopeInfo(_message.Message):
    __slots__ = ('reference_list_scope',)
    REFERENCE_LIST_SCOPE_FIELD_NUMBER: _ClassVar[int]
    reference_list_scope: ReferenceListScope

    def __init__(self, reference_list_scope: _Optional[_Union[ReferenceListScope, _Mapping]]=...) -> None:
        ...

class ReferenceListScope(_message.Message):
    __slots__ = ('scope_names',)
    SCOPE_NAMES_FIELD_NUMBER: _ClassVar[int]
    scope_names: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, scope_names: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetReferenceListRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: ReferenceListView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[ReferenceListView, str]]=...) -> None:
        ...

class ListReferenceListsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'view')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    view: ReferenceListView

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., view: _Optional[_Union[ReferenceListView, str]]=...) -> None:
        ...

class ListReferenceListsResponse(_message.Message):
    __slots__ = ('reference_lists', 'next_page_token')
    REFERENCE_LISTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    reference_lists: _containers.RepeatedCompositeFieldContainer[ReferenceList]
    next_page_token: str

    def __init__(self, reference_lists: _Optional[_Iterable[_Union[ReferenceList, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateReferenceListRequest(_message.Message):
    __slots__ = ('parent', 'reference_list', 'reference_list_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_LIST_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_LIST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    reference_list: ReferenceList
    reference_list_id: str

    def __init__(self, parent: _Optional[str]=..., reference_list: _Optional[_Union[ReferenceList, _Mapping]]=..., reference_list_id: _Optional[str]=...) -> None:
        ...

class UpdateReferenceListRequest(_message.Message):
    __slots__ = ('reference_list', 'update_mask')
    REFERENCE_LIST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    reference_list: ReferenceList
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, reference_list: _Optional[_Union[ReferenceList, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ReferenceList(_message.Message):
    __slots__ = ('name', 'display_name', 'revision_create_time', 'description', 'entries', 'rules', 'syntax_type', 'rule_associations_count', 'scope_info')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    REVISION_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    SYNTAX_TYPE_FIELD_NUMBER: _ClassVar[int]
    RULE_ASSOCIATIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SCOPE_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    revision_create_time: _timestamp_pb2.Timestamp
    description: str
    entries: _containers.RepeatedCompositeFieldContainer[ReferenceListEntry]
    rules: _containers.RepeatedScalarFieldContainer[str]
    syntax_type: ReferenceListSyntaxType
    rule_associations_count: int
    scope_info: ScopeInfo

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., revision_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., entries: _Optional[_Iterable[_Union[ReferenceListEntry, _Mapping]]]=..., rules: _Optional[_Iterable[str]]=..., syntax_type: _Optional[_Union[ReferenceListSyntaxType, str]]=..., rule_associations_count: _Optional[int]=..., scope_info: _Optional[_Union[ScopeInfo, _Mapping]]=...) -> None:
        ...

class ReferenceListEntry(_message.Message):
    __slots__ = ('value',)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str

    def __init__(self, value: _Optional[str]=...) -> None:
        ...