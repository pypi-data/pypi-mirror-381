from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.saasplatform.saasservicemgmt.v1beta1 import deployments_resources_pb2 as _deployments_resources_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListSaasRequest(_message.Message):
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

class ListSaasResponse(_message.Message):
    __slots__ = ('saas', 'next_page_token', 'unreachable')
    SAAS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    saas: _containers.RepeatedCompositeFieldContainer[_deployments_resources_pb2.Saas]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, saas: _Optional[_Iterable[_Union[_deployments_resources_pb2.Saas, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetSaasRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateSaasRequest(_message.Message):
    __slots__ = ('parent', 'saas_id', 'saas', 'validate_only', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SAAS_ID_FIELD_NUMBER: _ClassVar[int]
    SAAS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    saas_id: str
    saas: _deployments_resources_pb2.Saas
    validate_only: bool
    request_id: str

    def __init__(self, parent: _Optional[str]=..., saas_id: _Optional[str]=..., saas: _Optional[_Union[_deployments_resources_pb2.Saas, _Mapping]]=..., validate_only: bool=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateSaasRequest(_message.Message):
    __slots__ = ('saas', 'validate_only', 'request_id', 'update_mask')
    SAAS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    saas: _deployments_resources_pb2.Saas
    validate_only: bool
    request_id: str
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, saas: _Optional[_Union[_deployments_resources_pb2.Saas, _Mapping]]=..., validate_only: bool=..., request_id: _Optional[str]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteSaasRequest(_message.Message):
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

class ListTenantsRequest(_message.Message):
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

class ListTenantsResponse(_message.Message):
    __slots__ = ('tenants', 'next_page_token', 'unreachable')
    TENANTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    tenants: _containers.RepeatedCompositeFieldContainer[_deployments_resources_pb2.Tenant]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, tenants: _Optional[_Iterable[_Union[_deployments_resources_pb2.Tenant, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetTenantRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateTenantRequest(_message.Message):
    __slots__ = ('parent', 'tenant_id', 'tenant', 'validate_only', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    tenant_id: str
    tenant: _deployments_resources_pb2.Tenant
    validate_only: bool
    request_id: str

    def __init__(self, parent: _Optional[str]=..., tenant_id: _Optional[str]=..., tenant: _Optional[_Union[_deployments_resources_pb2.Tenant, _Mapping]]=..., validate_only: bool=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateTenantRequest(_message.Message):
    __slots__ = ('tenant', 'validate_only', 'request_id', 'update_mask')
    TENANT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    tenant: _deployments_resources_pb2.Tenant
    validate_only: bool
    request_id: str
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, tenant: _Optional[_Union[_deployments_resources_pb2.Tenant, _Mapping]]=..., validate_only: bool=..., request_id: _Optional[str]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteTenantRequest(_message.Message):
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

class ListUnitKindsRequest(_message.Message):
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

class ListUnitKindsResponse(_message.Message):
    __slots__ = ('unit_kinds', 'next_page_token', 'unreachable')
    UNIT_KINDS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    unit_kinds: _containers.RepeatedCompositeFieldContainer[_deployments_resources_pb2.UnitKind]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, unit_kinds: _Optional[_Iterable[_Union[_deployments_resources_pb2.UnitKind, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetUnitKindRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateUnitKindRequest(_message.Message):
    __slots__ = ('parent', 'unit_kind_id', 'unit_kind', 'validate_only', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    UNIT_KIND_ID_FIELD_NUMBER: _ClassVar[int]
    UNIT_KIND_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    unit_kind_id: str
    unit_kind: _deployments_resources_pb2.UnitKind
    validate_only: bool
    request_id: str

    def __init__(self, parent: _Optional[str]=..., unit_kind_id: _Optional[str]=..., unit_kind: _Optional[_Union[_deployments_resources_pb2.UnitKind, _Mapping]]=..., validate_only: bool=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateUnitKindRequest(_message.Message):
    __slots__ = ('unit_kind', 'validate_only', 'request_id', 'update_mask')
    UNIT_KIND_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    unit_kind: _deployments_resources_pb2.UnitKind
    validate_only: bool
    request_id: str
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, unit_kind: _Optional[_Union[_deployments_resources_pb2.UnitKind, _Mapping]]=..., validate_only: bool=..., request_id: _Optional[str]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteUnitKindRequest(_message.Message):
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

class ListUnitsRequest(_message.Message):
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

class ListUnitsResponse(_message.Message):
    __slots__ = ('units', 'next_page_token', 'unreachable')
    UNITS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    units: _containers.RepeatedCompositeFieldContainer[_deployments_resources_pb2.Unit]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, units: _Optional[_Iterable[_Union[_deployments_resources_pb2.Unit, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetUnitRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateUnitRequest(_message.Message):
    __slots__ = ('parent', 'unit_id', 'unit', 'validate_only', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    UNIT_ID_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    unit_id: str
    unit: _deployments_resources_pb2.Unit
    validate_only: bool
    request_id: str

    def __init__(self, parent: _Optional[str]=..., unit_id: _Optional[str]=..., unit: _Optional[_Union[_deployments_resources_pb2.Unit, _Mapping]]=..., validate_only: bool=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateUnitRequest(_message.Message):
    __slots__ = ('unit', 'validate_only', 'request_id', 'update_mask')
    UNIT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    unit: _deployments_resources_pb2.Unit
    validate_only: bool
    request_id: str
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, unit: _Optional[_Union[_deployments_resources_pb2.Unit, _Mapping]]=..., validate_only: bool=..., request_id: _Optional[str]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteUnitRequest(_message.Message):
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

class ListUnitOperationsRequest(_message.Message):
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

class ListUnitOperationsResponse(_message.Message):
    __slots__ = ('unit_operations', 'next_page_token', 'unreachable')
    UNIT_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    unit_operations: _containers.RepeatedCompositeFieldContainer[_deployments_resources_pb2.UnitOperation]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, unit_operations: _Optional[_Iterable[_Union[_deployments_resources_pb2.UnitOperation, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetUnitOperationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateUnitOperationRequest(_message.Message):
    __slots__ = ('parent', 'unit_operation_id', 'unit_operation', 'validate_only', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    UNIT_OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    UNIT_OPERATION_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    unit_operation_id: str
    unit_operation: _deployments_resources_pb2.UnitOperation
    validate_only: bool
    request_id: str

    def __init__(self, parent: _Optional[str]=..., unit_operation_id: _Optional[str]=..., unit_operation: _Optional[_Union[_deployments_resources_pb2.UnitOperation, _Mapping]]=..., validate_only: bool=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateUnitOperationRequest(_message.Message):
    __slots__ = ('unit_operation', 'validate_only', 'request_id', 'update_mask')
    UNIT_OPERATION_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    unit_operation: _deployments_resources_pb2.UnitOperation
    validate_only: bool
    request_id: str
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, unit_operation: _Optional[_Union[_deployments_resources_pb2.UnitOperation, _Mapping]]=..., validate_only: bool=..., request_id: _Optional[str]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteUnitOperationRequest(_message.Message):
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

class ListReleasesRequest(_message.Message):
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

class ListReleasesResponse(_message.Message):
    __slots__ = ('releases', 'next_page_token', 'unreachable')
    RELEASES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    releases: _containers.RepeatedCompositeFieldContainer[_deployments_resources_pb2.Release]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, releases: _Optional[_Iterable[_Union[_deployments_resources_pb2.Release, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetReleaseRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateReleaseRequest(_message.Message):
    __slots__ = ('parent', 'release_id', 'release', 'validate_only', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RELEASE_ID_FIELD_NUMBER: _ClassVar[int]
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    release_id: str
    release: _deployments_resources_pb2.Release
    validate_only: bool
    request_id: str

    def __init__(self, parent: _Optional[str]=..., release_id: _Optional[str]=..., release: _Optional[_Union[_deployments_resources_pb2.Release, _Mapping]]=..., validate_only: bool=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateReleaseRequest(_message.Message):
    __slots__ = ('release', 'validate_only', 'request_id', 'update_mask')
    RELEASE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    release: _deployments_resources_pb2.Release
    validate_only: bool
    request_id: str
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, release: _Optional[_Union[_deployments_resources_pb2.Release, _Mapping]]=..., validate_only: bool=..., request_id: _Optional[str]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteReleaseRequest(_message.Message):
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