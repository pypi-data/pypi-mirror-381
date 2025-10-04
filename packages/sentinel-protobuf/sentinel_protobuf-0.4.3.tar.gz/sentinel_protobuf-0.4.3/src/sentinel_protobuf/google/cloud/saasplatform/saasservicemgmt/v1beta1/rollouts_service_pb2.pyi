from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.saasplatform.saasservicemgmt.v1beta1 import rollouts_resources_pb2 as _rollouts_resources_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListRolloutsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListRolloutsResponse(_message.Message):
    __slots__ = ('rollouts', 'next_page_token', 'unreachable')
    ROLLOUTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    rollouts: _containers.RepeatedCompositeFieldContainer[_rollouts_resources_pb2.Rollout]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, rollouts: _Optional[_Iterable[_Union[_rollouts_resources_pb2.Rollout, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetRolloutRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateRolloutRequest(_message.Message):
    __slots__ = ('parent', 'rollout_id', 'rollout', 'validate_only', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_ID_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    rollout_id: str
    rollout: _rollouts_resources_pb2.Rollout
    validate_only: bool
    request_id: str

    def __init__(self, parent: _Optional[str]=..., rollout_id: _Optional[str]=..., rollout: _Optional[_Union[_rollouts_resources_pb2.Rollout, _Mapping]]=..., validate_only: bool=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateRolloutRequest(_message.Message):
    __slots__ = ('rollout', 'validate_only', 'request_id', 'update_mask')
    ROLLOUT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    rollout: _rollouts_resources_pb2.Rollout
    validate_only: bool
    request_id: str
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, rollout: _Optional[_Union[_rollouts_resources_pb2.Rollout, _Mapping]]=..., validate_only: bool=..., request_id: _Optional[str]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteRolloutRequest(_message.Message):
    __slots__ = ('name', 'etag', 'validate_only', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str
    validate_only: bool
    request_id: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=..., validate_only: bool=..., request_id: _Optional[str]=...) -> None:
        ...

class ListRolloutKindsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListRolloutKindsResponse(_message.Message):
    __slots__ = ('rollout_kinds', 'next_page_token', 'unreachable')
    ROLLOUT_KINDS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    rollout_kinds: _containers.RepeatedCompositeFieldContainer[_rollouts_resources_pb2.RolloutKind]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, rollout_kinds: _Optional[_Iterable[_Union[_rollouts_resources_pb2.RolloutKind, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetRolloutKindRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateRolloutKindRequest(_message.Message):
    __slots__ = ('parent', 'rollout_kind_id', 'rollout_kind', 'validate_only', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_KIND_ID_FIELD_NUMBER: _ClassVar[int]
    ROLLOUT_KIND_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    rollout_kind_id: str
    rollout_kind: _rollouts_resources_pb2.RolloutKind
    validate_only: bool
    request_id: str

    def __init__(self, parent: _Optional[str]=..., rollout_kind_id: _Optional[str]=..., rollout_kind: _Optional[_Union[_rollouts_resources_pb2.RolloutKind, _Mapping]]=..., validate_only: bool=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateRolloutKindRequest(_message.Message):
    __slots__ = ('rollout_kind', 'validate_only', 'request_id', 'update_mask')
    ROLLOUT_KIND_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    rollout_kind: _rollouts_resources_pb2.RolloutKind
    validate_only: bool
    request_id: str
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, rollout_kind: _Optional[_Union[_rollouts_resources_pb2.RolloutKind, _Mapping]]=..., validate_only: bool=..., request_id: _Optional[str]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteRolloutKindRequest(_message.Message):
    __slots__ = ('name', 'etag', 'validate_only', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str
    validate_only: bool
    request_id: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=..., validate_only: bool=..., request_id: _Optional[str]=...) -> None:
        ...