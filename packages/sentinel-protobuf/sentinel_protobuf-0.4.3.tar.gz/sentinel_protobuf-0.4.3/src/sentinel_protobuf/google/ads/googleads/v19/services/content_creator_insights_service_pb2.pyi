from google.ads.googleads.v19.common import audience_insights_attribute_pb2 as _audience_insights_attribute_pb2
from google.ads.googleads.v19.common import criteria_pb2 as _criteria_pb2
from google.ads.googleads.v19.enums import insights_trend_pb2 as _insights_trend_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenerateCreatorInsightsRequest(_message.Message):
    __slots__ = ('customer_id', 'customer_insights_group', 'country_locations', 'search_attributes', 'search_brand', 'search_channels')

    class SearchAttributes(_message.Message):
        __slots__ = ('audience_attributes', 'creator_attributes')
        AUDIENCE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        CREATOR_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        audience_attributes: _containers.RepeatedCompositeFieldContainer[_audience_insights_attribute_pb2.AudienceInsightsAttribute]
        creator_attributes: _containers.RepeatedCompositeFieldContainer[_audience_insights_attribute_pb2.AudienceInsightsAttribute]

        def __init__(self, audience_attributes: _Optional[_Iterable[_Union[_audience_insights_attribute_pb2.AudienceInsightsAttribute, _Mapping]]]=..., creator_attributes: _Optional[_Iterable[_Union[_audience_insights_attribute_pb2.AudienceInsightsAttribute, _Mapping]]]=...) -> None:
            ...

    class SearchBrand(_message.Message):
        __slots__ = ('brand_entities', 'include_related_topics')
        BRAND_ENTITIES_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_RELATED_TOPICS_FIELD_NUMBER: _ClassVar[int]
        brand_entities: _containers.RepeatedCompositeFieldContainer[_audience_insights_attribute_pb2.AudienceInsightsAttribute]
        include_related_topics: bool

        def __init__(self, brand_entities: _Optional[_Iterable[_Union[_audience_insights_attribute_pb2.AudienceInsightsAttribute, _Mapping]]]=..., include_related_topics: bool=...) -> None:
            ...

    class YouTubeChannels(_message.Message):
        __slots__ = ('youtube_channels',)
        YOUTUBE_CHANNELS_FIELD_NUMBER: _ClassVar[int]
        youtube_channels: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.YouTubeChannelInfo]

        def __init__(self, youtube_channels: _Optional[_Iterable[_Union[_criteria_pb2.YouTubeChannelInfo, _Mapping]]]=...) -> None:
            ...
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_INSIGHTS_GROUP_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    SEARCH_BRAND_FIELD_NUMBER: _ClassVar[int]
    SEARCH_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    customer_insights_group: str
    country_locations: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.LocationInfo]
    search_attributes: GenerateCreatorInsightsRequest.SearchAttributes
    search_brand: GenerateCreatorInsightsRequest.SearchBrand
    search_channels: GenerateCreatorInsightsRequest.YouTubeChannels

    def __init__(self, customer_id: _Optional[str]=..., customer_insights_group: _Optional[str]=..., country_locations: _Optional[_Iterable[_Union[_criteria_pb2.LocationInfo, _Mapping]]]=..., search_attributes: _Optional[_Union[GenerateCreatorInsightsRequest.SearchAttributes, _Mapping]]=..., search_brand: _Optional[_Union[GenerateCreatorInsightsRequest.SearchBrand, _Mapping]]=..., search_channels: _Optional[_Union[GenerateCreatorInsightsRequest.YouTubeChannels, _Mapping]]=...) -> None:
        ...

class GenerateCreatorInsightsResponse(_message.Message):
    __slots__ = ('creator_insights',)
    CREATOR_INSIGHTS_FIELD_NUMBER: _ClassVar[int]
    creator_insights: _containers.RepeatedCompositeFieldContainer[YouTubeCreatorInsights]

    def __init__(self, creator_insights: _Optional[_Iterable[_Union[YouTubeCreatorInsights, _Mapping]]]=...) -> None:
        ...

class GenerateTrendingInsightsRequest(_message.Message):
    __slots__ = ('customer_id', 'customer_insights_group', 'country_location', 'search_audience', 'search_topics')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_INSIGHTS_GROUP_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SEARCH_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TOPICS_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    customer_insights_group: str
    country_location: _criteria_pb2.LocationInfo
    search_audience: SearchAudience
    search_topics: SearchTopics

    def __init__(self, customer_id: _Optional[str]=..., customer_insights_group: _Optional[str]=..., country_location: _Optional[_Union[_criteria_pb2.LocationInfo, _Mapping]]=..., search_audience: _Optional[_Union[SearchAudience, _Mapping]]=..., search_topics: _Optional[_Union[SearchTopics, _Mapping]]=...) -> None:
        ...

class GenerateTrendingInsightsResponse(_message.Message):
    __slots__ = ('trend_insights',)
    TREND_INSIGHTS_FIELD_NUMBER: _ClassVar[int]
    trend_insights: _containers.RepeatedCompositeFieldContainer[TrendInsight]

    def __init__(self, trend_insights: _Optional[_Iterable[_Union[TrendInsight, _Mapping]]]=...) -> None:
        ...

class YouTubeCreatorInsights(_message.Message):
    __slots__ = ('creator_name', 'creator_channels')
    CREATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATOR_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    creator_name: str
    creator_channels: _containers.RepeatedCompositeFieldContainer[YouTubeChannelInsights]

    def __init__(self, creator_name: _Optional[str]=..., creator_channels: _Optional[_Iterable[_Union[YouTubeChannelInsights, _Mapping]]]=...) -> None:
        ...

class YouTubeMetrics(_message.Message):
    __slots__ = ('subscriber_count', 'views_count', 'video_count', 'is_active_shorts_creator')
    SUBSCRIBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    VIEWS_COUNT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_SHORTS_CREATOR_FIELD_NUMBER: _ClassVar[int]
    subscriber_count: int
    views_count: int
    video_count: int
    is_active_shorts_creator: bool

    def __init__(self, subscriber_count: _Optional[int]=..., views_count: _Optional[int]=..., video_count: _Optional[int]=..., is_active_shorts_creator: bool=...) -> None:
        ...

class YouTubeChannelInsights(_message.Message):
    __slots__ = ('display_name', 'youtube_channel', 'channel_url', 'channel_description', 'channel_metrics', 'channel_audience_attributes', 'channel_attributes', 'top_videos', 'channel_type')
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_URL_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_METRICS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_AUDIENCE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    TOP_VIDEOS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    youtube_channel: _criteria_pb2.YouTubeChannelInfo
    channel_url: str
    channel_description: str
    channel_metrics: YouTubeMetrics
    channel_audience_attributes: _containers.RepeatedCompositeFieldContainer[_audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata]
    channel_attributes: _containers.RepeatedCompositeFieldContainer[_audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata]
    top_videos: _containers.RepeatedCompositeFieldContainer[_audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata]
    channel_type: str

    def __init__(self, display_name: _Optional[str]=..., youtube_channel: _Optional[_Union[_criteria_pb2.YouTubeChannelInfo, _Mapping]]=..., channel_url: _Optional[str]=..., channel_description: _Optional[str]=..., channel_metrics: _Optional[_Union[YouTubeMetrics, _Mapping]]=..., channel_audience_attributes: _Optional[_Iterable[_Union[_audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata, _Mapping]]]=..., channel_attributes: _Optional[_Iterable[_Union[_audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata, _Mapping]]]=..., top_videos: _Optional[_Iterable[_Union[_audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata, _Mapping]]]=..., channel_type: _Optional[str]=...) -> None:
        ...

class SearchAudience(_message.Message):
    __slots__ = ('audience_attributes',)
    AUDIENCE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    audience_attributes: _containers.RepeatedCompositeFieldContainer[_audience_insights_attribute_pb2.AudienceInsightsAttribute]

    def __init__(self, audience_attributes: _Optional[_Iterable[_Union[_audience_insights_attribute_pb2.AudienceInsightsAttribute, _Mapping]]]=...) -> None:
        ...

class SearchTopics(_message.Message):
    __slots__ = ('entities',)
    ENTITIES_FIELD_NUMBER: _ClassVar[int]
    entities: _containers.RepeatedCompositeFieldContainer[_audience_insights_attribute_pb2.AudienceInsightsEntity]

    def __init__(self, entities: _Optional[_Iterable[_Union[_audience_insights_attribute_pb2.AudienceInsightsEntity, _Mapping]]]=...) -> None:
        ...

class TrendInsight(_message.Message):
    __slots__ = ('trend_attribute', 'trend_metrics', 'trend')
    TREND_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    TREND_METRICS_FIELD_NUMBER: _ClassVar[int]
    TREND_FIELD_NUMBER: _ClassVar[int]
    trend_attribute: _audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata
    trend_metrics: TrendInsightMetrics
    trend: _insights_trend_pb2.InsightsTrendEnum.InsightsTrend

    def __init__(self, trend_attribute: _Optional[_Union[_audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata, _Mapping]]=..., trend_metrics: _Optional[_Union[TrendInsightMetrics, _Mapping]]=..., trend: _Optional[_Union[_insights_trend_pb2.InsightsTrendEnum.InsightsTrend, str]]=...) -> None:
        ...

class TrendInsightMetrics(_message.Message):
    __slots__ = ('views_count',)
    VIEWS_COUNT_FIELD_NUMBER: _ClassVar[int]
    views_count: int

    def __init__(self, views_count: _Optional[int]=...) -> None:
        ...