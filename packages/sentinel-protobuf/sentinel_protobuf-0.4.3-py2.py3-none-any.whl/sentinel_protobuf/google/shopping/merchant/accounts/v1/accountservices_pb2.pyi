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

class AccountService(_message.Message):
    __slots__ = ('products_management', 'campaigns_management', 'account_management', 'account_aggregation', 'local_listing_management', 'name', 'provider', 'provider_display_name', 'handshake', 'mutability', 'external_account_id')

    class Mutability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MUTABILITY_UNSPECIFIED: _ClassVar[AccountService.Mutability]
        MUTABLE: _ClassVar[AccountService.Mutability]
        IMMUTABLE: _ClassVar[AccountService.Mutability]
    MUTABILITY_UNSPECIFIED: AccountService.Mutability
    MUTABLE: AccountService.Mutability
    IMMUTABLE: AccountService.Mutability
    PRODUCTS_MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGNS_MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_AGGREGATION_FIELD_NUMBER: _ClassVar[int]
    LOCAL_LISTING_MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    HANDSHAKE_FIELD_NUMBER: _ClassVar[int]
    MUTABILITY_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    products_management: ProductsManagement
    campaigns_management: CampaignsManagement
    account_management: AccountManagement
    account_aggregation: AccountAggregation
    local_listing_management: LocalListingManagement
    name: str
    provider: str
    provider_display_name: str
    handshake: Handshake
    mutability: AccountService.Mutability
    external_account_id: str

    def __init__(self, products_management: _Optional[_Union[ProductsManagement, _Mapping]]=..., campaigns_management: _Optional[_Union[CampaignsManagement, _Mapping]]=..., account_management: _Optional[_Union[AccountManagement, _Mapping]]=..., account_aggregation: _Optional[_Union[AccountAggregation, _Mapping]]=..., local_listing_management: _Optional[_Union[LocalListingManagement, _Mapping]]=..., name: _Optional[str]=..., provider: _Optional[str]=..., provider_display_name: _Optional[str]=..., handshake: _Optional[_Union[Handshake, _Mapping]]=..., mutability: _Optional[_Union[AccountService.Mutability, str]]=..., external_account_id: _Optional[str]=...) -> None:
        ...

class GetAccountServiceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListAccountServicesRequest(_message.Message):
    __slots__ = ('parent', 'page_token', 'page_size')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_token: str
    page_size: int

    def __init__(self, parent: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class ListAccountServicesResponse(_message.Message):
    __slots__ = ('account_services', 'next_page_token')
    ACCOUNT_SERVICES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    account_services: _containers.RepeatedCompositeFieldContainer[AccountService]
    next_page_token: str

    def __init__(self, account_services: _Optional[_Iterable[_Union[AccountService, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class ProposeAccountServiceRequest(_message.Message):
    __slots__ = ('parent', 'provider', 'account_service')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_SERVICE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    provider: str
    account_service: AccountService

    def __init__(self, parent: _Optional[str]=..., provider: _Optional[str]=..., account_service: _Optional[_Union[AccountService, _Mapping]]=...) -> None:
        ...

class ApproveAccountServiceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RejectAccountServiceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ProductsManagement(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CampaignsManagement(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class AccountManagement(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class AccountAggregation(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class LocalListingManagement(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class Handshake(_message.Message):
    __slots__ = ('approval_state', 'actor')

    class ApprovalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        APPROVAL_STATE_UNSPECIFIED: _ClassVar[Handshake.ApprovalState]
        PENDING: _ClassVar[Handshake.ApprovalState]
        ESTABLISHED: _ClassVar[Handshake.ApprovalState]
        REJECTED: _ClassVar[Handshake.ApprovalState]
    APPROVAL_STATE_UNSPECIFIED: Handshake.ApprovalState
    PENDING: Handshake.ApprovalState
    ESTABLISHED: Handshake.ApprovalState
    REJECTED: Handshake.ApprovalState

    class Actor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTOR_UNSPECIFIED: _ClassVar[Handshake.Actor]
        ACCOUNT: _ClassVar[Handshake.Actor]
        OTHER_PARTY: _ClassVar[Handshake.Actor]
    ACTOR_UNSPECIFIED: Handshake.Actor
    ACCOUNT: Handshake.Actor
    OTHER_PARTY: Handshake.Actor
    APPROVAL_STATE_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    approval_state: Handshake.ApprovalState
    actor: Handshake.Actor

    def __init__(self, approval_state: _Optional[_Union[Handshake.ApprovalState, str]]=..., actor: _Optional[_Union[Handshake.Actor, str]]=...) -> None:
        ...