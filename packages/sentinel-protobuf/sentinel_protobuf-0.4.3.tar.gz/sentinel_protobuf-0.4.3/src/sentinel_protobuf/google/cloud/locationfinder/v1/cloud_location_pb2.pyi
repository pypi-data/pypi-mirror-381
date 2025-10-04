from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CloudLocation(_message.Message):
    __slots__ = ('name', 'containing_cloud_location', 'display_name', 'cloud_provider', 'territory_code', 'cloud_location_type', 'carbon_free_energy_percentage')

    class CloudProvider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLOUD_PROVIDER_UNSPECIFIED: _ClassVar[CloudLocation.CloudProvider]
        CLOUD_PROVIDER_GCP: _ClassVar[CloudLocation.CloudProvider]
        CLOUD_PROVIDER_AWS: _ClassVar[CloudLocation.CloudProvider]
        CLOUD_PROVIDER_AZURE: _ClassVar[CloudLocation.CloudProvider]
        CLOUD_PROVIDER_OCI: _ClassVar[CloudLocation.CloudProvider]
    CLOUD_PROVIDER_UNSPECIFIED: CloudLocation.CloudProvider
    CLOUD_PROVIDER_GCP: CloudLocation.CloudProvider
    CLOUD_PROVIDER_AWS: CloudLocation.CloudProvider
    CLOUD_PROVIDER_AZURE: CloudLocation.CloudProvider
    CLOUD_PROVIDER_OCI: CloudLocation.CloudProvider

    class CloudLocationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLOUD_LOCATION_TYPE_UNSPECIFIED: _ClassVar[CloudLocation.CloudLocationType]
        CLOUD_LOCATION_TYPE_REGION: _ClassVar[CloudLocation.CloudLocationType]
        CLOUD_LOCATION_TYPE_ZONE: _ClassVar[CloudLocation.CloudLocationType]
        CLOUD_LOCATION_TYPE_REGION_EXTENSION: _ClassVar[CloudLocation.CloudLocationType]
        CLOUD_LOCATION_TYPE_GDCC_ZONE: _ClassVar[CloudLocation.CloudLocationType]
    CLOUD_LOCATION_TYPE_UNSPECIFIED: CloudLocation.CloudLocationType
    CLOUD_LOCATION_TYPE_REGION: CloudLocation.CloudLocationType
    CLOUD_LOCATION_TYPE_ZONE: CloudLocation.CloudLocationType
    CLOUD_LOCATION_TYPE_REGION_EXTENSION: CloudLocation.CloudLocationType
    CLOUD_LOCATION_TYPE_GDCC_ZONE: CloudLocation.CloudLocationType
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTAINING_CLOUD_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CLOUD_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    TERRITORY_CODE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_LOCATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CARBON_FREE_ENERGY_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    containing_cloud_location: str
    display_name: str
    cloud_provider: CloudLocation.CloudProvider
    territory_code: str
    cloud_location_type: CloudLocation.CloudLocationType
    carbon_free_energy_percentage: float

    def __init__(self, name: _Optional[str]=..., containing_cloud_location: _Optional[str]=..., display_name: _Optional[str]=..., cloud_provider: _Optional[_Union[CloudLocation.CloudProvider, str]]=..., territory_code: _Optional[str]=..., cloud_location_type: _Optional[_Union[CloudLocation.CloudLocationType, str]]=..., carbon_free_energy_percentage: _Optional[float]=...) -> None:
        ...

class ListCloudLocationsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListCloudLocationsResponse(_message.Message):
    __slots__ = ('cloud_locations', 'next_page_token')
    CLOUD_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    cloud_locations: _containers.RepeatedCompositeFieldContainer[CloudLocation]
    next_page_token: str

    def __init__(self, cloud_locations: _Optional[_Iterable[_Union[CloudLocation, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetCloudLocationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class SearchCloudLocationsRequest(_message.Message):
    __slots__ = ('parent', 'source_cloud_location', 'page_size', 'page_token', 'query')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CLOUD_LOCATION_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    source_cloud_location: str
    page_size: int
    page_token: str
    query: str

    def __init__(self, parent: _Optional[str]=..., source_cloud_location: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., query: _Optional[str]=...) -> None:
        ...

class SearchCloudLocationsResponse(_message.Message):
    __slots__ = ('cloud_locations', 'next_page_token')
    CLOUD_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    cloud_locations: _containers.RepeatedCompositeFieldContainer[CloudLocation]
    next_page_token: str

    def __init__(self, cloud_locations: _Optional[_Iterable[_Union[CloudLocation, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...