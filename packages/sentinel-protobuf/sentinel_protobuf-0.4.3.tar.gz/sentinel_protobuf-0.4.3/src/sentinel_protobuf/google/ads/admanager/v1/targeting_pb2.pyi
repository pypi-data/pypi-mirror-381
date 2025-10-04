from google.ads.admanager.v1 import request_platform_enum_pb2 as _request_platform_enum_pb2
from google.ads.admanager.v1 import targeted_video_bumper_type_enum_pb2 as _targeted_video_bumper_type_enum_pb2
from google.ads.admanager.v1 import video_position_enum_pb2 as _video_position_enum_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Targeting(_message.Message):
    __slots__ = ('geo_targeting', 'technology_targeting', 'inventory_targeting', 'request_platform_targeting', 'custom_targeting', 'user_domain_targeting', 'video_position_targeting', 'data_segment_targeting')
    GEO_TARGETING_FIELD_NUMBER: _ClassVar[int]
    TECHNOLOGY_TARGETING_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_TARGETING_FIELD_NUMBER: _ClassVar[int]
    REQUEST_PLATFORM_TARGETING_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TARGETING_FIELD_NUMBER: _ClassVar[int]
    USER_DOMAIN_TARGETING_FIELD_NUMBER: _ClassVar[int]
    VIDEO_POSITION_TARGETING_FIELD_NUMBER: _ClassVar[int]
    DATA_SEGMENT_TARGETING_FIELD_NUMBER: _ClassVar[int]
    geo_targeting: GeoTargeting
    technology_targeting: TechnologyTargeting
    inventory_targeting: InventoryTargeting
    request_platform_targeting: RequestPlatformTargeting
    custom_targeting: CustomTargeting
    user_domain_targeting: UserDomainTargeting
    video_position_targeting: VideoPositionTargeting
    data_segment_targeting: DataSegmentTargeting

    def __init__(self, geo_targeting: _Optional[_Union[GeoTargeting, _Mapping]]=..., technology_targeting: _Optional[_Union[TechnologyTargeting, _Mapping]]=..., inventory_targeting: _Optional[_Union[InventoryTargeting, _Mapping]]=..., request_platform_targeting: _Optional[_Union[RequestPlatformTargeting, _Mapping]]=..., custom_targeting: _Optional[_Union[CustomTargeting, _Mapping]]=..., user_domain_targeting: _Optional[_Union[UserDomainTargeting, _Mapping]]=..., video_position_targeting: _Optional[_Union[VideoPositionTargeting, _Mapping]]=..., data_segment_targeting: _Optional[_Union[DataSegmentTargeting, _Mapping]]=...) -> None:
        ...

class GeoTargeting(_message.Message):
    __slots__ = ('targeted_geos', 'excluded_geos')
    TARGETED_GEOS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_GEOS_FIELD_NUMBER: _ClassVar[int]
    targeted_geos: _containers.RepeatedScalarFieldContainer[str]
    excluded_geos: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, targeted_geos: _Optional[_Iterable[str]]=..., excluded_geos: _Optional[_Iterable[str]]=...) -> None:
        ...

class TechnologyTargeting(_message.Message):
    __slots__ = ('bandwidth_targeting', 'device_category_targeting', 'operating_system_targeting')
    BANDWIDTH_TARGETING_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CATEGORY_TARGETING_FIELD_NUMBER: _ClassVar[int]
    OPERATING_SYSTEM_TARGETING_FIELD_NUMBER: _ClassVar[int]
    bandwidth_targeting: BandwidthTargeting
    device_category_targeting: DeviceCategoryTargeting
    operating_system_targeting: OperatingSystemTargeting

    def __init__(self, bandwidth_targeting: _Optional[_Union[BandwidthTargeting, _Mapping]]=..., device_category_targeting: _Optional[_Union[DeviceCategoryTargeting, _Mapping]]=..., operating_system_targeting: _Optional[_Union[OperatingSystemTargeting, _Mapping]]=...) -> None:
        ...

class BandwidthTargeting(_message.Message):
    __slots__ = ('targeted_bandwidth_groups', 'excluded_bandwidth_groups')
    TARGETED_BANDWIDTH_GROUPS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_BANDWIDTH_GROUPS_FIELD_NUMBER: _ClassVar[int]
    targeted_bandwidth_groups: _containers.RepeatedScalarFieldContainer[str]
    excluded_bandwidth_groups: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, targeted_bandwidth_groups: _Optional[_Iterable[str]]=..., excluded_bandwidth_groups: _Optional[_Iterable[str]]=...) -> None:
        ...

class DeviceCategoryTargeting(_message.Message):
    __slots__ = ('targeted_categories', 'excluded_categories')
    TARGETED_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    targeted_categories: _containers.RepeatedScalarFieldContainer[str]
    excluded_categories: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, targeted_categories: _Optional[_Iterable[str]]=..., excluded_categories: _Optional[_Iterable[str]]=...) -> None:
        ...

class OperatingSystemTargeting(_message.Message):
    __slots__ = ('targeted_operating_systems', 'excluded_operating_systems', 'targeted_operating_system_versions', 'excluded_operating_system_versions')
    TARGETED_OPERATING_SYSTEMS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_OPERATING_SYSTEMS_FIELD_NUMBER: _ClassVar[int]
    TARGETED_OPERATING_SYSTEM_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_OPERATING_SYSTEM_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    targeted_operating_systems: _containers.RepeatedScalarFieldContainer[str]
    excluded_operating_systems: _containers.RepeatedScalarFieldContainer[str]
    targeted_operating_system_versions: _containers.RepeatedScalarFieldContainer[str]
    excluded_operating_system_versions: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, targeted_operating_systems: _Optional[_Iterable[str]]=..., excluded_operating_systems: _Optional[_Iterable[str]]=..., targeted_operating_system_versions: _Optional[_Iterable[str]]=..., excluded_operating_system_versions: _Optional[_Iterable[str]]=...) -> None:
        ...

class InventoryTargeting(_message.Message):
    __slots__ = ('targeted_ad_units', 'excluded_ad_units', 'targeted_placements')
    TARGETED_AD_UNITS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_AD_UNITS_FIELD_NUMBER: _ClassVar[int]
    TARGETED_PLACEMENTS_FIELD_NUMBER: _ClassVar[int]
    targeted_ad_units: _containers.RepeatedCompositeFieldContainer[AdUnitTargeting]
    excluded_ad_units: _containers.RepeatedCompositeFieldContainer[AdUnitTargeting]
    targeted_placements: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, targeted_ad_units: _Optional[_Iterable[_Union[AdUnitTargeting, _Mapping]]]=..., excluded_ad_units: _Optional[_Iterable[_Union[AdUnitTargeting, _Mapping]]]=..., targeted_placements: _Optional[_Iterable[str]]=...) -> None:
        ...

class AdUnitTargeting(_message.Message):
    __slots__ = ('include_descendants', 'ad_unit')
    INCLUDE_DESCENDANTS_FIELD_NUMBER: _ClassVar[int]
    AD_UNIT_FIELD_NUMBER: _ClassVar[int]
    include_descendants: bool
    ad_unit: str

    def __init__(self, include_descendants: bool=..., ad_unit: _Optional[str]=...) -> None:
        ...

class RequestPlatformTargeting(_message.Message):
    __slots__ = ('request_platforms',)
    REQUEST_PLATFORMS_FIELD_NUMBER: _ClassVar[int]
    request_platforms: _containers.RepeatedScalarFieldContainer[_request_platform_enum_pb2.RequestPlatformEnum.RequestPlatform]

    def __init__(self, request_platforms: _Optional[_Iterable[_Union[_request_platform_enum_pb2.RequestPlatformEnum.RequestPlatform, str]]]=...) -> None:
        ...

class CustomTargeting(_message.Message):
    __slots__ = ('custom_targeting_clauses',)
    CUSTOM_TARGETING_CLAUSES_FIELD_NUMBER: _ClassVar[int]
    custom_targeting_clauses: _containers.RepeatedCompositeFieldContainer[CustomTargetingClause]

    def __init__(self, custom_targeting_clauses: _Optional[_Iterable[_Union[CustomTargetingClause, _Mapping]]]=...) -> None:
        ...

class CustomTargetingClause(_message.Message):
    __slots__ = ('custom_targeting_literals',)
    CUSTOM_TARGETING_LITERALS_FIELD_NUMBER: _ClassVar[int]
    custom_targeting_literals: _containers.RepeatedCompositeFieldContainer[CustomTargetingLiteral]

    def __init__(self, custom_targeting_literals: _Optional[_Iterable[_Union[CustomTargetingLiteral, _Mapping]]]=...) -> None:
        ...

class CustomTargetingLiteral(_message.Message):
    __slots__ = ('negative', 'custom_targeting_key', 'custom_targeting_values')
    NEGATIVE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TARGETING_KEY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TARGETING_VALUES_FIELD_NUMBER: _ClassVar[int]
    negative: bool
    custom_targeting_key: str
    custom_targeting_values: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, negative: bool=..., custom_targeting_key: _Optional[str]=..., custom_targeting_values: _Optional[_Iterable[str]]=...) -> None:
        ...

class UserDomainTargeting(_message.Message):
    __slots__ = ('targeted_user_domains', 'excluded_user_domains')
    TARGETED_USER_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_USER_DOMAINS_FIELD_NUMBER: _ClassVar[int]
    targeted_user_domains: _containers.RepeatedScalarFieldContainer[str]
    excluded_user_domains: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, targeted_user_domains: _Optional[_Iterable[str]]=..., excluded_user_domains: _Optional[_Iterable[str]]=...) -> None:
        ...

class VideoPositionTargeting(_message.Message):
    __slots__ = ('video_positions',)
    VIDEO_POSITIONS_FIELD_NUMBER: _ClassVar[int]
    video_positions: _containers.RepeatedCompositeFieldContainer[VideoPosition]

    def __init__(self, video_positions: _Optional[_Iterable[_Union[VideoPosition, _Mapping]]]=...) -> None:
        ...

class VideoPosition(_message.Message):
    __slots__ = ('midroll_index', 'reverse_midroll_index', 'pod_position', 'position_type', 'bumper_type')
    MIDROLL_INDEX_FIELD_NUMBER: _ClassVar[int]
    REVERSE_MIDROLL_INDEX_FIELD_NUMBER: _ClassVar[int]
    POD_POSITION_FIELD_NUMBER: _ClassVar[int]
    POSITION_TYPE_FIELD_NUMBER: _ClassVar[int]
    BUMPER_TYPE_FIELD_NUMBER: _ClassVar[int]
    midroll_index: int
    reverse_midroll_index: int
    pod_position: int
    position_type: _video_position_enum_pb2.VideoPositionEnum.VideoPosition
    bumper_type: _targeted_video_bumper_type_enum_pb2.TargetedVideoBumperTypeEnum.TargetedVideoBumperType

    def __init__(self, midroll_index: _Optional[int]=..., reverse_midroll_index: _Optional[int]=..., pod_position: _Optional[int]=..., position_type: _Optional[_Union[_video_position_enum_pb2.VideoPositionEnum.VideoPosition, str]]=..., bumper_type: _Optional[_Union[_targeted_video_bumper_type_enum_pb2.TargetedVideoBumperTypeEnum.TargetedVideoBumperType, str]]=...) -> None:
        ...

class DataSegmentTargeting(_message.Message):
    __slots__ = ('has_data_segment_targeting',)
    HAS_DATA_SEGMENT_TARGETING_FIELD_NUMBER: _ClassVar[int]
    has_data_segment_targeting: bool

    def __init__(self, has_data_segment_targeting: bool=...) -> None:
        ...