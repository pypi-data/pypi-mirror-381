from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.shopping.merchant.inventories.v1 import inventories_common_pb2 as _inventories_common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LocalInventory(_message.Message):
    __slots__ = ('name', 'account', 'store_code', 'local_inventory_attributes')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    STORE_CODE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_INVENTORY_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    name: str
    account: int
    store_code: str
    local_inventory_attributes: _inventories_common_pb2.LocalInventoryAttributes

    def __init__(self, name: _Optional[str]=..., account: _Optional[int]=..., store_code: _Optional[str]=..., local_inventory_attributes: _Optional[_Union[_inventories_common_pb2.LocalInventoryAttributes, _Mapping]]=...) -> None:
        ...

class ListLocalInventoriesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListLocalInventoriesResponse(_message.Message):
    __slots__ = ('local_inventories', 'next_page_token')
    LOCAL_INVENTORIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    local_inventories: _containers.RepeatedCompositeFieldContainer[LocalInventory]
    next_page_token: str

    def __init__(self, local_inventories: _Optional[_Iterable[_Union[LocalInventory, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class InsertLocalInventoryRequest(_message.Message):
    __slots__ = ('parent', 'local_inventory')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    LOCAL_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    local_inventory: LocalInventory

    def __init__(self, parent: _Optional[str]=..., local_inventory: _Optional[_Union[LocalInventory, _Mapping]]=...) -> None:
        ...

class DeleteLocalInventoryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...