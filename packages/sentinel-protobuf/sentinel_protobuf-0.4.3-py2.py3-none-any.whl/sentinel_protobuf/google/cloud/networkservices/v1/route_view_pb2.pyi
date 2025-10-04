from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GatewayRouteView(_message.Message):
    __slots__ = ('name', 'route_project_number', 'route_location', 'route_type', 'route_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROUTE_PROJECT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ROUTE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    ROUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROUTE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    route_project_number: int
    route_location: str
    route_type: str
    route_id: str

    def __init__(self, name: _Optional[str]=..., route_project_number: _Optional[int]=..., route_location: _Optional[str]=..., route_type: _Optional[str]=..., route_id: _Optional[str]=...) -> None:
        ...

class MeshRouteView(_message.Message):
    __slots__ = ('name', 'route_project_number', 'route_location', 'route_type', 'route_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROUTE_PROJECT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ROUTE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    ROUTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROUTE_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    route_project_number: int
    route_location: str
    route_type: str
    route_id: str

    def __init__(self, name: _Optional[str]=..., route_project_number: _Optional[int]=..., route_location: _Optional[str]=..., route_type: _Optional[str]=..., route_id: _Optional[str]=...) -> None:
        ...

class GetGatewayRouteViewRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetMeshRouteViewRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListGatewayRouteViewsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListMeshRouteViewsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListGatewayRouteViewsResponse(_message.Message):
    __slots__ = ('gateway_route_views', 'next_page_token', 'unreachable')
    GATEWAY_ROUTE_VIEWS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    gateway_route_views: _containers.RepeatedCompositeFieldContainer[GatewayRouteView]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, gateway_route_views: _Optional[_Iterable[_Union[GatewayRouteView, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class ListMeshRouteViewsResponse(_message.Message):
    __slots__ = ('mesh_route_views', 'next_page_token', 'unreachable')
    MESH_ROUTE_VIEWS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    mesh_route_views: _containers.RepeatedCompositeFieldContainer[MeshRouteView]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, mesh_route_views: _Optional[_Iterable[_Union[MeshRouteView, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...