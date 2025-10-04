from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AddressGroup(_message.Message):
    __slots__ = ('name', 'description', 'create_time', 'update_time', 'labels', 'type', 'items', 'capacity', 'self_link', 'purpose')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[AddressGroup.Type]
        IPV4: _ClassVar[AddressGroup.Type]
        IPV6: _ClassVar[AddressGroup.Type]
    TYPE_UNSPECIFIED: AddressGroup.Type
    IPV4: AddressGroup.Type
    IPV6: AddressGroup.Type

    class Purpose(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PURPOSE_UNSPECIFIED: _ClassVar[AddressGroup.Purpose]
        DEFAULT: _ClassVar[AddressGroup.Purpose]
        CLOUD_ARMOR: _ClassVar[AddressGroup.Purpose]
    PURPOSE_UNSPECIFIED: AddressGroup.Purpose
    DEFAULT: AddressGroup.Purpose
    CLOUD_ARMOR: AddressGroup.Purpose

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    SELF_LINK_FIELD_NUMBER: _ClassVar[int]
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    type: AddressGroup.Type
    items: _containers.RepeatedScalarFieldContainer[str]
    capacity: int
    self_link: str
    purpose: _containers.RepeatedScalarFieldContainer[AddressGroup.Purpose]

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., type: _Optional[_Union[AddressGroup.Type, str]]=..., items: _Optional[_Iterable[str]]=..., capacity: _Optional[int]=..., self_link: _Optional[str]=..., purpose: _Optional[_Iterable[_Union[AddressGroup.Purpose, str]]]=...) -> None:
        ...

class ListAddressGroupsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'return_partial_success')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RETURN_PARTIAL_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    return_partial_success: bool

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., return_partial_success: bool=...) -> None:
        ...

class ListAddressGroupsResponse(_message.Message):
    __slots__ = ('address_groups', 'next_page_token', 'unreachable')
    ADDRESS_GROUPS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    address_groups: _containers.RepeatedCompositeFieldContainer[AddressGroup]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, address_groups: _Optional[_Iterable[_Union[AddressGroup, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetAddressGroupRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateAddressGroupRequest(_message.Message):
    __slots__ = ('parent', 'address_group_id', 'address_group', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_GROUP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    address_group_id: str
    address_group: AddressGroup
    request_id: str

    def __init__(self, parent: _Optional[str]=..., address_group_id: _Optional[str]=..., address_group: _Optional[_Union[AddressGroup, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateAddressGroupRequest(_message.Message):
    __slots__ = ('update_mask', 'address_group', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_GROUP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    address_group: AddressGroup
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., address_group: _Optional[_Union[AddressGroup, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteAddressGroupRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class AddAddressGroupItemsRequest(_message.Message):
    __slots__ = ('address_group', 'items', 'request_id')
    ADDRESS_GROUP_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    address_group: str
    items: _containers.RepeatedScalarFieldContainer[str]
    request_id: str

    def __init__(self, address_group: _Optional[str]=..., items: _Optional[_Iterable[str]]=..., request_id: _Optional[str]=...) -> None:
        ...

class RemoveAddressGroupItemsRequest(_message.Message):
    __slots__ = ('address_group', 'items', 'request_id')
    ADDRESS_GROUP_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    address_group: str
    items: _containers.RepeatedScalarFieldContainer[str]
    request_id: str

    def __init__(self, address_group: _Optional[str]=..., items: _Optional[_Iterable[str]]=..., request_id: _Optional[str]=...) -> None:
        ...

class CloneAddressGroupItemsRequest(_message.Message):
    __slots__ = ('address_group', 'source_address_group', 'request_id')
    ADDRESS_GROUP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ADDRESS_GROUP_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    address_group: str
    source_address_group: str
    request_id: str

    def __init__(self, address_group: _Optional[str]=..., source_address_group: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListAddressGroupReferencesRequest(_message.Message):
    __slots__ = ('address_group', 'page_size', 'page_token')
    ADDRESS_GROUP_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    address_group: str
    page_size: int
    page_token: str

    def __init__(self, address_group: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListAddressGroupReferencesResponse(_message.Message):
    __slots__ = ('address_group_references', 'next_page_token')

    class AddressGroupReference(_message.Message):
        __slots__ = ('firewall_policy', 'security_policy', 'rule_priority')
        FIREWALL_POLICY_FIELD_NUMBER: _ClassVar[int]
        SECURITY_POLICY_FIELD_NUMBER: _ClassVar[int]
        RULE_PRIORITY_FIELD_NUMBER: _ClassVar[int]
        firewall_policy: str
        security_policy: str
        rule_priority: int

        def __init__(self, firewall_policy: _Optional[str]=..., security_policy: _Optional[str]=..., rule_priority: _Optional[int]=...) -> None:
            ...
    ADDRESS_GROUP_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    address_group_references: _containers.RepeatedCompositeFieldContainer[ListAddressGroupReferencesResponse.AddressGroupReference]
    next_page_token: str

    def __init__(self, address_group_references: _Optional[_Iterable[_Union[ListAddressGroupReferencesResponse.AddressGroupReference, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...