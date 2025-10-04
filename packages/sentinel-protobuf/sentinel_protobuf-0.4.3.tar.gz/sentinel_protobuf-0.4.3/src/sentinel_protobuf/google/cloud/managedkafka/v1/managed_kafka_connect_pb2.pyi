from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.managedkafka.v1 import resources_pb2 as _resources_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetConnectClusterRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateConnectClusterRequest(_message.Message):
    __slots__ = ('parent', 'connect_cluster_id', 'connect_cluster', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONNECT_CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECT_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    connect_cluster_id: str
    connect_cluster: _resources_pb2.ConnectCluster
    request_id: str

    def __init__(self, parent: _Optional[str]=..., connect_cluster_id: _Optional[str]=..., connect_cluster: _Optional[_Union[_resources_pb2.ConnectCluster, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateConnectClusterRequest(_message.Message):
    __slots__ = ('update_mask', 'connect_cluster', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CONNECT_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    connect_cluster: _resources_pb2.ConnectCluster
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., connect_cluster: _Optional[_Union[_resources_pb2.ConnectCluster, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteConnectClusterRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class ListConnectClustersRequest(_message.Message):
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

class ListConnectClustersResponse(_message.Message):
    __slots__ = ('connect_clusters', 'next_page_token', 'unreachable')
    CONNECT_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    connect_clusters: _containers.RepeatedCompositeFieldContainer[_resources_pb2.ConnectCluster]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, connect_clusters: _Optional[_Iterable[_Union[_resources_pb2.ConnectCluster, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetConnectorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateConnectorRequest(_message.Message):
    __slots__ = ('parent', 'connector_id', 'connector')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    parent: str
    connector_id: str
    connector: _resources_pb2.Connector

    def __init__(self, parent: _Optional[str]=..., connector_id: _Optional[str]=..., connector: _Optional[_Union[_resources_pb2.Connector, _Mapping]]=...) -> None:
        ...

class UpdateConnectorRequest(_message.Message):
    __slots__ = ('update_mask', 'connector')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    connector: _resources_pb2.Connector

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., connector: _Optional[_Union[_resources_pb2.Connector, _Mapping]]=...) -> None:
        ...

class DeleteConnectorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListConnectorsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListConnectorsResponse(_message.Message):
    __slots__ = ('connectors', 'next_page_token')
    CONNECTORS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    connectors: _containers.RepeatedCompositeFieldContainer[_resources_pb2.Connector]
    next_page_token: str

    def __init__(self, connectors: _Optional[_Iterable[_Union[_resources_pb2.Connector, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class PauseConnectorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class PauseConnectorResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ResumeConnectorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ResumeConnectorResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class RestartConnectorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RestartConnectorResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class StopConnectorRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class StopConnectorResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...