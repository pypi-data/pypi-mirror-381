from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PhoneNumber(_message.Message):
    __slots__ = ('name', 'phone_number', 'conversation_profile', 'lifecycle_state')

    class LifecycleState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LIFECYCLE_STATE_UNSPECIFIED: _ClassVar[PhoneNumber.LifecycleState]
        ACTIVE: _ClassVar[PhoneNumber.LifecycleState]
        DELETE_REQUESTED: _ClassVar[PhoneNumber.LifecycleState]
    LIFECYCLE_STATE_UNSPECIFIED: PhoneNumber.LifecycleState
    ACTIVE: PhoneNumber.LifecycleState
    DELETE_REQUESTED: PhoneNumber.LifecycleState
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_PROFILE_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    phone_number: str
    conversation_profile: str
    lifecycle_state: PhoneNumber.LifecycleState

    def __init__(self, name: _Optional[str]=..., phone_number: _Optional[str]=..., conversation_profile: _Optional[str]=..., lifecycle_state: _Optional[_Union[PhoneNumber.LifecycleState, str]]=...) -> None:
        ...

class DeletePhoneNumberRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UndeletePhoneNumberRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListPhoneNumbersRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'show_deleted')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    show_deleted: bool

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., show_deleted: bool=...) -> None:
        ...

class ListPhoneNumbersResponse(_message.Message):
    __slots__ = ('phone_numbers', 'next_page_token')
    PHONE_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    phone_numbers: _containers.RepeatedCompositeFieldContainer[PhoneNumber]
    next_page_token: str

    def __init__(self, phone_numbers: _Optional[_Iterable[_Union[PhoneNumber, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdatePhoneNumberRequest(_message.Message):
    __slots__ = ('phone_number', 'update_mask')
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    phone_number: PhoneNumber
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, phone_number: _Optional[_Union[PhoneNumber, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...