from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.apihub.v1 import common_fields_pb2 as _common_fields_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CollectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COLLECTION_TYPE_UNSPECIFIED: _ClassVar[CollectionType]
    COLLECTION_TYPE_UPSERT: _ClassVar[CollectionType]
    COLLECTION_TYPE_DELETE: _ClassVar[CollectionType]
COLLECTION_TYPE_UNSPECIFIED: CollectionType
COLLECTION_TYPE_UPSERT: CollectionType
COLLECTION_TYPE_DELETE: CollectionType

class CollectApiDataRequest(_message.Message):
    __slots__ = ('location', 'collection_type', 'plugin_instance', 'action_id', 'api_data')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    API_DATA_FIELD_NUMBER: _ClassVar[int]
    location: str
    collection_type: CollectionType
    plugin_instance: str
    action_id: str
    api_data: ApiData

    def __init__(self, location: _Optional[str]=..., collection_type: _Optional[_Union[CollectionType, str]]=..., plugin_instance: _Optional[str]=..., action_id: _Optional[str]=..., api_data: _Optional[_Union[ApiData, _Mapping]]=...) -> None:
        ...

class ApiData(_message.Message):
    __slots__ = ('api_metadata_list',)
    API_METADATA_LIST_FIELD_NUMBER: _ClassVar[int]
    api_metadata_list: ApiMetadataList

    def __init__(self, api_metadata_list: _Optional[_Union[ApiMetadataList, _Mapping]]=...) -> None:
        ...

class ApiMetadataList(_message.Message):
    __slots__ = ('api_metadata',)
    API_METADATA_FIELD_NUMBER: _ClassVar[int]
    api_metadata: _containers.RepeatedCompositeFieldContainer[APIMetadata]

    def __init__(self, api_metadata: _Optional[_Iterable[_Union[APIMetadata, _Mapping]]]=...) -> None:
        ...

class APIMetadata(_message.Message):
    __slots__ = ('api', 'versions', 'original_id', 'original_create_time', 'original_update_time')
    API_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    api: _common_fields_pb2.Api
    versions: _containers.RepeatedCompositeFieldContainer[VersionMetadata]
    original_id: str
    original_create_time: _timestamp_pb2.Timestamp
    original_update_time: _timestamp_pb2.Timestamp

    def __init__(self, api: _Optional[_Union[_common_fields_pb2.Api, _Mapping]]=..., versions: _Optional[_Iterable[_Union[VersionMetadata, _Mapping]]]=..., original_id: _Optional[str]=..., original_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., original_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class VersionMetadata(_message.Message):
    __slots__ = ('version', 'specs', 'deployments', 'original_id', 'original_create_time', 'original_update_time')
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SPECS_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    version: _common_fields_pb2.Version
    specs: _containers.RepeatedCompositeFieldContainer[SpecMetadata]
    deployments: _containers.RepeatedCompositeFieldContainer[DeploymentMetadata]
    original_id: str
    original_create_time: _timestamp_pb2.Timestamp
    original_update_time: _timestamp_pb2.Timestamp

    def __init__(self, version: _Optional[_Union[_common_fields_pb2.Version, _Mapping]]=..., specs: _Optional[_Iterable[_Union[SpecMetadata, _Mapping]]]=..., deployments: _Optional[_Iterable[_Union[DeploymentMetadata, _Mapping]]]=..., original_id: _Optional[str]=..., original_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., original_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class SpecMetadata(_message.Message):
    __slots__ = ('spec', 'original_id', 'original_create_time', 'original_update_time')
    SPEC_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    spec: _common_fields_pb2.Spec
    original_id: str
    original_create_time: _timestamp_pb2.Timestamp
    original_update_time: _timestamp_pb2.Timestamp

    def __init__(self, spec: _Optional[_Union[_common_fields_pb2.Spec, _Mapping]]=..., original_id: _Optional[str]=..., original_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., original_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class DeploymentMetadata(_message.Message):
    __slots__ = ('deployment', 'original_id', 'original_create_time', 'original_update_time')
    DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    deployment: _common_fields_pb2.Deployment
    original_id: str
    original_create_time: _timestamp_pb2.Timestamp
    original_update_time: _timestamp_pb2.Timestamp

    def __init__(self, deployment: _Optional[_Union[_common_fields_pb2.Deployment, _Mapping]]=..., original_id: _Optional[str]=..., original_create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., original_update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class CollectApiDataResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...