from google.ads.googleads.v20.common import criteria_pb2 as _criteria_pb2
from google.ads.googleads.v20.enums import audience_insights_dimension_pb2 as _audience_insights_dimension_pb2
from google.ads.googleads.v20.enums import insights_knowledge_graph_entity_capabilities_pb2 as _insights_knowledge_graph_entity_capabilities_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AudienceInsightsAttributeMetadata(_message.Message):
    __slots__ = ('dimension', 'attribute', 'display_name', 'display_info', 'potential_youtube_reach', 'subscriber_share', 'viewer_share', 'youtube_channel_metadata', 'youtube_video_metadata', 'lineup_attribute_metadata', 'location_attribute_metadata', 'user_interest_attribute_metadata', 'knowledge_graph_attribute_metadata')
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_INFO_FIELD_NUMBER: _ClassVar[int]
    POTENTIAL_YOUTUBE_REACH_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBER_SHARE_FIELD_NUMBER: _ClassVar[int]
    VIEWER_SHARE_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_CHANNEL_METADATA_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_VIDEO_METADATA_FIELD_NUMBER: _ClassVar[int]
    LINEUP_ATTRIBUTE_METADATA_FIELD_NUMBER: _ClassVar[int]
    LOCATION_ATTRIBUTE_METADATA_FIELD_NUMBER: _ClassVar[int]
    USER_INTEREST_ATTRIBUTE_METADATA_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGE_GRAPH_ATTRIBUTE_METADATA_FIELD_NUMBER: _ClassVar[int]
    dimension: _audience_insights_dimension_pb2.AudienceInsightsDimensionEnum.AudienceInsightsDimension
    attribute: AudienceInsightsAttribute
    display_name: str
    display_info: str
    potential_youtube_reach: int
    subscriber_share: float
    viewer_share: float
    youtube_channel_metadata: YouTubeChannelAttributeMetadata
    youtube_video_metadata: YouTubeVideoAttributeMetadata
    lineup_attribute_metadata: LineupAttributeMetadata
    location_attribute_metadata: LocationAttributeMetadata
    user_interest_attribute_metadata: UserInterestAttributeMetadata
    knowledge_graph_attribute_metadata: KnowledgeGraphAttributeMetadata

    def __init__(self, dimension: _Optional[_Union[_audience_insights_dimension_pb2.AudienceInsightsDimensionEnum.AudienceInsightsDimension, str]]=..., attribute: _Optional[_Union[AudienceInsightsAttribute, _Mapping]]=..., display_name: _Optional[str]=..., display_info: _Optional[str]=..., potential_youtube_reach: _Optional[int]=..., subscriber_share: _Optional[float]=..., viewer_share: _Optional[float]=..., youtube_channel_metadata: _Optional[_Union[YouTubeChannelAttributeMetadata, _Mapping]]=..., youtube_video_metadata: _Optional[_Union[YouTubeVideoAttributeMetadata, _Mapping]]=..., lineup_attribute_metadata: _Optional[_Union[LineupAttributeMetadata, _Mapping]]=..., location_attribute_metadata: _Optional[_Union[LocationAttributeMetadata, _Mapping]]=..., user_interest_attribute_metadata: _Optional[_Union[UserInterestAttributeMetadata, _Mapping]]=..., knowledge_graph_attribute_metadata: _Optional[_Union[KnowledgeGraphAttributeMetadata, _Mapping]]=...) -> None:
        ...

class AudienceInsightsAttribute(_message.Message):
    __slots__ = ('age_range', 'gender', 'location', 'user_interest', 'entity', 'category', 'lineup', 'parental_status', 'income_range', 'youtube_channel', 'youtube_video', 'device')
    AGE_RANGE_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    USER_INTEREST_FIELD_NUMBER: _ClassVar[int]
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    LINEUP_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    INCOME_RANGE_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_VIDEO_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    age_range: _criteria_pb2.AgeRangeInfo
    gender: _criteria_pb2.GenderInfo
    location: _criteria_pb2.LocationInfo
    user_interest: _criteria_pb2.UserInterestInfo
    entity: AudienceInsightsEntity
    category: AudienceInsightsCategory
    lineup: AudienceInsightsLineup
    parental_status: _criteria_pb2.ParentalStatusInfo
    income_range: _criteria_pb2.IncomeRangeInfo
    youtube_channel: _criteria_pb2.YouTubeChannelInfo
    youtube_video: _criteria_pb2.YouTubeVideoInfo
    device: _criteria_pb2.DeviceInfo

    def __init__(self, age_range: _Optional[_Union[_criteria_pb2.AgeRangeInfo, _Mapping]]=..., gender: _Optional[_Union[_criteria_pb2.GenderInfo, _Mapping]]=..., location: _Optional[_Union[_criteria_pb2.LocationInfo, _Mapping]]=..., user_interest: _Optional[_Union[_criteria_pb2.UserInterestInfo, _Mapping]]=..., entity: _Optional[_Union[AudienceInsightsEntity, _Mapping]]=..., category: _Optional[_Union[AudienceInsightsCategory, _Mapping]]=..., lineup: _Optional[_Union[AudienceInsightsLineup, _Mapping]]=..., parental_status: _Optional[_Union[_criteria_pb2.ParentalStatusInfo, _Mapping]]=..., income_range: _Optional[_Union[_criteria_pb2.IncomeRangeInfo, _Mapping]]=..., youtube_channel: _Optional[_Union[_criteria_pb2.YouTubeChannelInfo, _Mapping]]=..., youtube_video: _Optional[_Union[_criteria_pb2.YouTubeVideoInfo, _Mapping]]=..., device: _Optional[_Union[_criteria_pb2.DeviceInfo, _Mapping]]=...) -> None:
        ...

class AudienceInsightsTopic(_message.Message):
    __slots__ = ('entity', 'category')
    ENTITY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    entity: AudienceInsightsEntity
    category: AudienceInsightsCategory

    def __init__(self, entity: _Optional[_Union[AudienceInsightsEntity, _Mapping]]=..., category: _Optional[_Union[AudienceInsightsCategory, _Mapping]]=...) -> None:
        ...

class AudienceInsightsEntity(_message.Message):
    __slots__ = ('knowledge_graph_machine_id',)
    KNOWLEDGE_GRAPH_MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    knowledge_graph_machine_id: str

    def __init__(self, knowledge_graph_machine_id: _Optional[str]=...) -> None:
        ...

class AudienceInsightsCategory(_message.Message):
    __slots__ = ('category_id',)
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    category_id: str

    def __init__(self, category_id: _Optional[str]=...) -> None:
        ...

class AudienceInsightsLineup(_message.Message):
    __slots__ = ('lineup_id',)
    LINEUP_ID_FIELD_NUMBER: _ClassVar[int]
    lineup_id: str

    def __init__(self, lineup_id: _Optional[str]=...) -> None:
        ...

class YouTubeChannelAttributeMetadata(_message.Message):
    __slots__ = ('subscriber_count',)
    SUBSCRIBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    subscriber_count: int

    def __init__(self, subscriber_count: _Optional[int]=...) -> None:
        ...

class YouTubeVideoAttributeMetadata(_message.Message):
    __slots__ = ('thumbnail_url', 'video_url')
    THUMBNAIL_URL_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    thumbnail_url: str
    video_url: str

    def __init__(self, thumbnail_url: _Optional[str]=..., video_url: _Optional[str]=...) -> None:
        ...

class LineupAttributeMetadata(_message.Message):
    __slots__ = ('inventory_country', 'median_monthly_inventory', 'channel_count_lower_bound', 'channel_count_upper_bound', 'sample_channels')

    class SampleChannel(_message.Message):
        __slots__ = ('youtube_channel', 'display_name', 'youtube_channel_metadata')
        YOUTUBE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        YOUTUBE_CHANNEL_METADATA_FIELD_NUMBER: _ClassVar[int]
        youtube_channel: _criteria_pb2.YouTubeChannelInfo
        display_name: str
        youtube_channel_metadata: YouTubeChannelAttributeMetadata

        def __init__(self, youtube_channel: _Optional[_Union[_criteria_pb2.YouTubeChannelInfo, _Mapping]]=..., display_name: _Optional[str]=..., youtube_channel_metadata: _Optional[_Union[YouTubeChannelAttributeMetadata, _Mapping]]=...) -> None:
            ...
    INVENTORY_COUNTRY_FIELD_NUMBER: _ClassVar[int]
    MEDIAN_MONTHLY_INVENTORY_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_COUNT_LOWER_BOUND_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_COUNT_UPPER_BOUND_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    inventory_country: _criteria_pb2.LocationInfo
    median_monthly_inventory: int
    channel_count_lower_bound: int
    channel_count_upper_bound: int
    sample_channels: _containers.RepeatedCompositeFieldContainer[LineupAttributeMetadata.SampleChannel]

    def __init__(self, inventory_country: _Optional[_Union[_criteria_pb2.LocationInfo, _Mapping]]=..., median_monthly_inventory: _Optional[int]=..., channel_count_lower_bound: _Optional[int]=..., channel_count_upper_bound: _Optional[int]=..., sample_channels: _Optional[_Iterable[_Union[LineupAttributeMetadata.SampleChannel, _Mapping]]]=...) -> None:
        ...

class LocationAttributeMetadata(_message.Message):
    __slots__ = ('country_location',)
    COUNTRY_LOCATION_FIELD_NUMBER: _ClassVar[int]
    country_location: _criteria_pb2.LocationInfo

    def __init__(self, country_location: _Optional[_Union[_criteria_pb2.LocationInfo, _Mapping]]=...) -> None:
        ...

class UserInterestAttributeMetadata(_message.Message):
    __slots__ = ('user_interest_description',)
    USER_INTEREST_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    user_interest_description: str

    def __init__(self, user_interest_description: _Optional[str]=...) -> None:
        ...

class KnowledgeGraphAttributeMetadata(_message.Message):
    __slots__ = ('entity_capabilities',)
    ENTITY_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    entity_capabilities: _containers.RepeatedScalarFieldContainer[_insights_knowledge_graph_entity_capabilities_pb2.InsightsKnowledgeGraphEntityCapabilitiesEnum.InsightsKnowledgeGraphEntityCapabilities]

    def __init__(self, entity_capabilities: _Optional[_Iterable[_Union[_insights_knowledge_graph_entity_capabilities_pb2.InsightsKnowledgeGraphEntityCapabilitiesEnum.InsightsKnowledgeGraphEntityCapabilities, str]]]=...) -> None:
        ...