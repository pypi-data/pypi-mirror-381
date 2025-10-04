from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UserData(_message.Message):
    __slots__ = ('user_identifiers',)
    USER_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    user_identifiers: _containers.RepeatedCompositeFieldContainer[UserIdentifier]

    def __init__(self, user_identifiers: _Optional[_Iterable[_Union[UserIdentifier, _Mapping]]]=...) -> None:
        ...

class UserIdentifier(_message.Message):
    __slots__ = ('email_address', 'phone_number', 'address')
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    email_address: str
    phone_number: str
    address: AddressInfo

    def __init__(self, email_address: _Optional[str]=..., phone_number: _Optional[str]=..., address: _Optional[_Union[AddressInfo, _Mapping]]=...) -> None:
        ...

class AddressInfo(_message.Message):
    __slots__ = ('given_name', 'family_name', 'region_code', 'postal_code')
    GIVEN_NAME_FIELD_NUMBER: _ClassVar[int]
    FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    given_name: str
    family_name: str
    region_code: str
    postal_code: str

    def __init__(self, given_name: _Optional[str]=..., family_name: _Optional[str]=..., region_code: _Optional[str]=..., postal_code: _Optional[str]=...) -> None:
        ...