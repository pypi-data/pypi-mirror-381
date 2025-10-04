from google.ads.googleads.v20.common import additional_application_info_pb2 as _additional_application_info_pb2
from google.ads.googleads.v20.common import audience_insights_attribute_pb2 as _audience_insights_attribute_pb2
from google.ads.googleads.v20.common import criteria_pb2 as _criteria_pb2
from google.ads.googleads.v20.common import dates_pb2 as _dates_pb2
from google.ads.googleads.v20.enums import audience_insights_dimension_pb2 as _audience_insights_dimension_pb2
from google.ads.googleads.v20.enums import audience_insights_marketing_objective_pb2 as _audience_insights_marketing_objective_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenerateInsightsFinderReportRequest(_message.Message):
    __slots__ = ('customer_id', 'baseline_audience', 'specific_audience', 'customer_insights_group', 'insights_application_info')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    BASELINE_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    SPECIFIC_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_INSIGHTS_GROUP_FIELD_NUMBER: _ClassVar[int]
    INSIGHTS_APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    baseline_audience: BasicInsightsAudience
    specific_audience: BasicInsightsAudience
    customer_insights_group: str
    insights_application_info: _additional_application_info_pb2.AdditionalApplicationInfo

    def __init__(self, customer_id: _Optional[str]=..., baseline_audience: _Optional[_Union[BasicInsightsAudience, _Mapping]]=..., specific_audience: _Optional[_Union[BasicInsightsAudience, _Mapping]]=..., customer_insights_group: _Optional[str]=..., insights_application_info: _Optional[_Union[_additional_application_info_pb2.AdditionalApplicationInfo, _Mapping]]=...) -> None:
        ...

class GenerateInsightsFinderReportResponse(_message.Message):
    __slots__ = ('saved_report_url',)
    SAVED_REPORT_URL_FIELD_NUMBER: _ClassVar[int]
    saved_report_url: str

    def __init__(self, saved_report_url: _Optional[str]=...) -> None:
        ...

class GenerateAudienceCompositionInsightsRequest(_message.Message):
    __slots__ = ('customer_id', 'audience', 'baseline_audience', 'data_month', 'dimensions', 'customer_insights_group', 'insights_application_info')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    BASELINE_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    DATA_MONTH_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_INSIGHTS_GROUP_FIELD_NUMBER: _ClassVar[int]
    INSIGHTS_APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    audience: InsightsAudience
    baseline_audience: InsightsAudience
    data_month: str
    dimensions: _containers.RepeatedScalarFieldContainer[_audience_insights_dimension_pb2.AudienceInsightsDimensionEnum.AudienceInsightsDimension]
    customer_insights_group: str
    insights_application_info: _additional_application_info_pb2.AdditionalApplicationInfo

    def __init__(self, customer_id: _Optional[str]=..., audience: _Optional[_Union[InsightsAudience, _Mapping]]=..., baseline_audience: _Optional[_Union[InsightsAudience, _Mapping]]=..., data_month: _Optional[str]=..., dimensions: _Optional[_Iterable[_Union[_audience_insights_dimension_pb2.AudienceInsightsDimensionEnum.AudienceInsightsDimension, str]]]=..., customer_insights_group: _Optional[str]=..., insights_application_info: _Optional[_Union[_additional_application_info_pb2.AdditionalApplicationInfo, _Mapping]]=...) -> None:
        ...

class GenerateAudienceCompositionInsightsResponse(_message.Message):
    __slots__ = ('sections',)
    SECTIONS_FIELD_NUMBER: _ClassVar[int]
    sections: _containers.RepeatedCompositeFieldContainer[AudienceCompositionSection]

    def __init__(self, sections: _Optional[_Iterable[_Union[AudienceCompositionSection, _Mapping]]]=...) -> None:
        ...

class GenerateSuggestedTargetingInsightsRequest(_message.Message):
    __slots__ = ('customer_id', 'customer_insights_group', 'insights_application_info', 'audience_definition', 'audience_description')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_INSIGHTS_GROUP_FIELD_NUMBER: _ClassVar[int]
    INSIGHTS_APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    customer_insights_group: str
    insights_application_info: _additional_application_info_pb2.AdditionalApplicationInfo
    audience_definition: InsightsAudienceDefinition
    audience_description: InsightsAudienceDescription

    def __init__(self, customer_id: _Optional[str]=..., customer_insights_group: _Optional[str]=..., insights_application_info: _Optional[_Union[_additional_application_info_pb2.AdditionalApplicationInfo, _Mapping]]=..., audience_definition: _Optional[_Union[InsightsAudienceDefinition, _Mapping]]=..., audience_description: _Optional[_Union[InsightsAudienceDescription, _Mapping]]=...) -> None:
        ...

class GenerateSuggestedTargetingInsightsResponse(_message.Message):
    __slots__ = ('suggestions',)
    SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    suggestions: _containers.RepeatedCompositeFieldContainer[TargetingSuggestionMetrics]

    def __init__(self, suggestions: _Optional[_Iterable[_Union[TargetingSuggestionMetrics, _Mapping]]]=...) -> None:
        ...

class TargetingSuggestionMetrics(_message.Message):
    __slots__ = ('locations', 'age_ranges', 'gender', 'parental_status', 'user_interests', 'coverage', 'index', 'potential_youtube_reach')
    LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    AGE_RANGES_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_INTERESTS_FIELD_NUMBER: _ClassVar[int]
    COVERAGE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    POTENTIAL_YOUTUBE_REACH_FIELD_NUMBER: _ClassVar[int]
    locations: _containers.RepeatedCompositeFieldContainer[_audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata]
    age_ranges: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.AgeRangeInfo]
    gender: _criteria_pb2.GenderInfo
    parental_status: _criteria_pb2.ParentalStatusInfo
    user_interests: _containers.RepeatedCompositeFieldContainer[_audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata]
    coverage: float
    index: float
    potential_youtube_reach: int

    def __init__(self, locations: _Optional[_Iterable[_Union[_audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata, _Mapping]]]=..., age_ranges: _Optional[_Iterable[_Union[_criteria_pb2.AgeRangeInfo, _Mapping]]]=..., gender: _Optional[_Union[_criteria_pb2.GenderInfo, _Mapping]]=..., parental_status: _Optional[_Union[_criteria_pb2.ParentalStatusInfo, _Mapping]]=..., user_interests: _Optional[_Iterable[_Union[_audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata, _Mapping]]]=..., coverage: _Optional[float]=..., index: _Optional[float]=..., potential_youtube_reach: _Optional[int]=...) -> None:
        ...

class ListAudienceInsightsAttributesRequest(_message.Message):
    __slots__ = ('customer_id', 'dimensions', 'query_text', 'customer_insights_group', 'insights_application_info', 'location_country_filters', 'youtube_reach_location')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    QUERY_TEXT_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_INSIGHTS_GROUP_FIELD_NUMBER: _ClassVar[int]
    INSIGHTS_APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    LOCATION_COUNTRY_FILTERS_FIELD_NUMBER: _ClassVar[int]
    YOUTUBE_REACH_LOCATION_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    dimensions: _containers.RepeatedScalarFieldContainer[_audience_insights_dimension_pb2.AudienceInsightsDimensionEnum.AudienceInsightsDimension]
    query_text: str
    customer_insights_group: str
    insights_application_info: _additional_application_info_pb2.AdditionalApplicationInfo
    location_country_filters: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.LocationInfo]
    youtube_reach_location: _criteria_pb2.LocationInfo

    def __init__(self, customer_id: _Optional[str]=..., dimensions: _Optional[_Iterable[_Union[_audience_insights_dimension_pb2.AudienceInsightsDimensionEnum.AudienceInsightsDimension, str]]]=..., query_text: _Optional[str]=..., customer_insights_group: _Optional[str]=..., insights_application_info: _Optional[_Union[_additional_application_info_pb2.AdditionalApplicationInfo, _Mapping]]=..., location_country_filters: _Optional[_Iterable[_Union[_criteria_pb2.LocationInfo, _Mapping]]]=..., youtube_reach_location: _Optional[_Union[_criteria_pb2.LocationInfo, _Mapping]]=...) -> None:
        ...

class ListAudienceInsightsAttributesResponse(_message.Message):
    __slots__ = ('attributes',)
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[_audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata]

    def __init__(self, attributes: _Optional[_Iterable[_Union[_audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata, _Mapping]]]=...) -> None:
        ...

class ListInsightsEligibleDatesRequest(_message.Message):
    __slots__ = ('insights_application_info',)
    INSIGHTS_APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    insights_application_info: _additional_application_info_pb2.AdditionalApplicationInfo

    def __init__(self, insights_application_info: _Optional[_Union[_additional_application_info_pb2.AdditionalApplicationInfo, _Mapping]]=...) -> None:
        ...

class ListInsightsEligibleDatesResponse(_message.Message):
    __slots__ = ('data_months', 'last_thirty_days')
    DATA_MONTHS_FIELD_NUMBER: _ClassVar[int]
    LAST_THIRTY_DAYS_FIELD_NUMBER: _ClassVar[int]
    data_months: _containers.RepeatedScalarFieldContainer[str]
    last_thirty_days: _dates_pb2.DateRange

    def __init__(self, data_months: _Optional[_Iterable[str]]=..., last_thirty_days: _Optional[_Union[_dates_pb2.DateRange, _Mapping]]=...) -> None:
        ...

class GenerateAudienceOverlapInsightsRequest(_message.Message):
    __slots__ = ('customer_id', 'country_location', 'primary_attribute', 'dimensions', 'customer_insights_group', 'insights_application_info')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_LOCATION_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    DIMENSIONS_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_INSIGHTS_GROUP_FIELD_NUMBER: _ClassVar[int]
    INSIGHTS_APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    country_location: _criteria_pb2.LocationInfo
    primary_attribute: _audience_insights_attribute_pb2.AudienceInsightsAttribute
    dimensions: _containers.RepeatedScalarFieldContainer[_audience_insights_dimension_pb2.AudienceInsightsDimensionEnum.AudienceInsightsDimension]
    customer_insights_group: str
    insights_application_info: _additional_application_info_pb2.AdditionalApplicationInfo

    def __init__(self, customer_id: _Optional[str]=..., country_location: _Optional[_Union[_criteria_pb2.LocationInfo, _Mapping]]=..., primary_attribute: _Optional[_Union[_audience_insights_attribute_pb2.AudienceInsightsAttribute, _Mapping]]=..., dimensions: _Optional[_Iterable[_Union[_audience_insights_dimension_pb2.AudienceInsightsDimensionEnum.AudienceInsightsDimension, str]]]=..., customer_insights_group: _Optional[str]=..., insights_application_info: _Optional[_Union[_additional_application_info_pb2.AdditionalApplicationInfo, _Mapping]]=...) -> None:
        ...

class GenerateAudienceOverlapInsightsResponse(_message.Message):
    __slots__ = ('primary_attribute_metadata', 'dimension_results')
    PRIMARY_ATTRIBUTE_METADATA_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    primary_attribute_metadata: _audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata
    dimension_results: _containers.RepeatedCompositeFieldContainer[DimensionOverlapResult]

    def __init__(self, primary_attribute_metadata: _Optional[_Union[_audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata, _Mapping]]=..., dimension_results: _Optional[_Iterable[_Union[DimensionOverlapResult, _Mapping]]]=...) -> None:
        ...

class DimensionOverlapResult(_message.Message):
    __slots__ = ('dimension', 'items')
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    dimension: _audience_insights_dimension_pb2.AudienceInsightsDimensionEnum.AudienceInsightsDimension
    items: _containers.RepeatedCompositeFieldContainer[AudienceOverlapItem]

    def __init__(self, dimension: _Optional[_Union[_audience_insights_dimension_pb2.AudienceInsightsDimensionEnum.AudienceInsightsDimension, str]]=..., items: _Optional[_Iterable[_Union[AudienceOverlapItem, _Mapping]]]=...) -> None:
        ...

class AudienceOverlapItem(_message.Message):
    __slots__ = ('attribute_metadata', 'potential_youtube_reach_intersection')
    ATTRIBUTE_METADATA_FIELD_NUMBER: _ClassVar[int]
    POTENTIAL_YOUTUBE_REACH_INTERSECTION_FIELD_NUMBER: _ClassVar[int]
    attribute_metadata: _audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata
    potential_youtube_reach_intersection: int

    def __init__(self, attribute_metadata: _Optional[_Union[_audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata, _Mapping]]=..., potential_youtube_reach_intersection: _Optional[int]=...) -> None:
        ...

class GenerateTargetingSuggestionMetricsRequest(_message.Message):
    __slots__ = ('customer_id', 'audiences', 'customer_insights_group', 'insights_application_info')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIENCES_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_INSIGHTS_GROUP_FIELD_NUMBER: _ClassVar[int]
    INSIGHTS_APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    audiences: _containers.RepeatedCompositeFieldContainer[BasicInsightsAudience]
    customer_insights_group: str
    insights_application_info: _additional_application_info_pb2.AdditionalApplicationInfo

    def __init__(self, customer_id: _Optional[str]=..., audiences: _Optional[_Iterable[_Union[BasicInsightsAudience, _Mapping]]]=..., customer_insights_group: _Optional[str]=..., insights_application_info: _Optional[_Union[_additional_application_info_pb2.AdditionalApplicationInfo, _Mapping]]=...) -> None:
        ...

class GenerateTargetingSuggestionMetricsResponse(_message.Message):
    __slots__ = ('suggestions',)
    SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
    suggestions: _containers.RepeatedCompositeFieldContainer[TargetingSuggestionMetrics]

    def __init__(self, suggestions: _Optional[_Iterable[_Union[TargetingSuggestionMetrics, _Mapping]]]=...) -> None:
        ...

class BasicInsightsAudience(_message.Message):
    __slots__ = ('country_location', 'sub_country_locations', 'gender', 'age_ranges', 'user_interests', 'topics')
    COUNTRY_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SUB_COUNTRY_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    AGE_RANGES_FIELD_NUMBER: _ClassVar[int]
    USER_INTERESTS_FIELD_NUMBER: _ClassVar[int]
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    country_location: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.LocationInfo]
    sub_country_locations: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.LocationInfo]
    gender: _criteria_pb2.GenderInfo
    age_ranges: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.AgeRangeInfo]
    user_interests: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.UserInterestInfo]
    topics: _containers.RepeatedCompositeFieldContainer[_audience_insights_attribute_pb2.AudienceInsightsTopic]

    def __init__(self, country_location: _Optional[_Iterable[_Union[_criteria_pb2.LocationInfo, _Mapping]]]=..., sub_country_locations: _Optional[_Iterable[_Union[_criteria_pb2.LocationInfo, _Mapping]]]=..., gender: _Optional[_Union[_criteria_pb2.GenderInfo, _Mapping]]=..., age_ranges: _Optional[_Iterable[_Union[_criteria_pb2.AgeRangeInfo, _Mapping]]]=..., user_interests: _Optional[_Iterable[_Union[_criteria_pb2.UserInterestInfo, _Mapping]]]=..., topics: _Optional[_Iterable[_Union[_audience_insights_attribute_pb2.AudienceInsightsTopic, _Mapping]]]=...) -> None:
        ...

class InsightsAudienceDefinition(_message.Message):
    __slots__ = ('audience', 'baseline_audience', 'data_month')
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    BASELINE_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    DATA_MONTH_FIELD_NUMBER: _ClassVar[int]
    audience: InsightsAudience
    baseline_audience: InsightsAudience
    data_month: str

    def __init__(self, audience: _Optional[_Union[InsightsAudience, _Mapping]]=..., baseline_audience: _Optional[_Union[InsightsAudience, _Mapping]]=..., data_month: _Optional[str]=...) -> None:
        ...

class InsightsAudienceDescription(_message.Message):
    __slots__ = ('country_locations', 'audience_description', 'marketing_objective')
    COUNTRY_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MARKETING_OBJECTIVE_FIELD_NUMBER: _ClassVar[int]
    country_locations: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.LocationInfo]
    audience_description: str
    marketing_objective: _audience_insights_marketing_objective_pb2.AudienceInsightsMarketingObjectiveEnum.AudienceInsightsMarketingObjective

    def __init__(self, country_locations: _Optional[_Iterable[_Union[_criteria_pb2.LocationInfo, _Mapping]]]=..., audience_description: _Optional[str]=..., marketing_objective: _Optional[_Union[_audience_insights_marketing_objective_pb2.AudienceInsightsMarketingObjectiveEnum.AudienceInsightsMarketingObjective, str]]=...) -> None:
        ...

class InsightsAudience(_message.Message):
    __slots__ = ('country_locations', 'sub_country_locations', 'gender', 'age_ranges', 'parental_status', 'income_ranges', 'lineups', 'topic_audience_combinations')
    COUNTRY_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    SUB_COUNTRY_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    AGE_RANGES_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    INCOME_RANGES_FIELD_NUMBER: _ClassVar[int]
    LINEUPS_FIELD_NUMBER: _ClassVar[int]
    TOPIC_AUDIENCE_COMBINATIONS_FIELD_NUMBER: _ClassVar[int]
    country_locations: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.LocationInfo]
    sub_country_locations: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.LocationInfo]
    gender: _criteria_pb2.GenderInfo
    age_ranges: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.AgeRangeInfo]
    parental_status: _criteria_pb2.ParentalStatusInfo
    income_ranges: _containers.RepeatedCompositeFieldContainer[_criteria_pb2.IncomeRangeInfo]
    lineups: _containers.RepeatedCompositeFieldContainer[_audience_insights_attribute_pb2.AudienceInsightsLineup]
    topic_audience_combinations: _containers.RepeatedCompositeFieldContainer[InsightsAudienceAttributeGroup]

    def __init__(self, country_locations: _Optional[_Iterable[_Union[_criteria_pb2.LocationInfo, _Mapping]]]=..., sub_country_locations: _Optional[_Iterable[_Union[_criteria_pb2.LocationInfo, _Mapping]]]=..., gender: _Optional[_Union[_criteria_pb2.GenderInfo, _Mapping]]=..., age_ranges: _Optional[_Iterable[_Union[_criteria_pb2.AgeRangeInfo, _Mapping]]]=..., parental_status: _Optional[_Union[_criteria_pb2.ParentalStatusInfo, _Mapping]]=..., income_ranges: _Optional[_Iterable[_Union[_criteria_pb2.IncomeRangeInfo, _Mapping]]]=..., lineups: _Optional[_Iterable[_Union[_audience_insights_attribute_pb2.AudienceInsightsLineup, _Mapping]]]=..., topic_audience_combinations: _Optional[_Iterable[_Union[InsightsAudienceAttributeGroup, _Mapping]]]=...) -> None:
        ...

class InsightsAudienceAttributeGroup(_message.Message):
    __slots__ = ('attributes',)
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    attributes: _containers.RepeatedCompositeFieldContainer[_audience_insights_attribute_pb2.AudienceInsightsAttribute]

    def __init__(self, attributes: _Optional[_Iterable[_Union[_audience_insights_attribute_pb2.AudienceInsightsAttribute, _Mapping]]]=...) -> None:
        ...

class AudienceCompositionSection(_message.Message):
    __slots__ = ('dimension', 'top_attributes', 'clustered_attributes')
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    TOP_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CLUSTERED_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    dimension: _audience_insights_dimension_pb2.AudienceInsightsDimensionEnum.AudienceInsightsDimension
    top_attributes: _containers.RepeatedCompositeFieldContainer[AudienceCompositionAttribute]
    clustered_attributes: _containers.RepeatedCompositeFieldContainer[AudienceCompositionAttributeCluster]

    def __init__(self, dimension: _Optional[_Union[_audience_insights_dimension_pb2.AudienceInsightsDimensionEnum.AudienceInsightsDimension, str]]=..., top_attributes: _Optional[_Iterable[_Union[AudienceCompositionAttribute, _Mapping]]]=..., clustered_attributes: _Optional[_Iterable[_Union[AudienceCompositionAttributeCluster, _Mapping]]]=...) -> None:
        ...

class AudienceCompositionAttributeCluster(_message.Message):
    __slots__ = ('cluster_display_name', 'cluster_metrics', 'attributes')
    CLUSTER_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_METRICS_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    cluster_display_name: str
    cluster_metrics: AudienceCompositionMetrics
    attributes: _containers.RepeatedCompositeFieldContainer[AudienceCompositionAttribute]

    def __init__(self, cluster_display_name: _Optional[str]=..., cluster_metrics: _Optional[_Union[AudienceCompositionMetrics, _Mapping]]=..., attributes: _Optional[_Iterable[_Union[AudienceCompositionAttribute, _Mapping]]]=...) -> None:
        ...

class AudienceCompositionMetrics(_message.Message):
    __slots__ = ('baseline_audience_share', 'audience_share', 'index', 'score')
    BASELINE_AUDIENCE_SHARE_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_SHARE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    baseline_audience_share: float
    audience_share: float
    index: float
    score: float

    def __init__(self, baseline_audience_share: _Optional[float]=..., audience_share: _Optional[float]=..., index: _Optional[float]=..., score: _Optional[float]=...) -> None:
        ...

class AudienceCompositionAttribute(_message.Message):
    __slots__ = ('attribute_metadata', 'metrics')
    ATTRIBUTE_METADATA_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    attribute_metadata: _audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata
    metrics: AudienceCompositionMetrics

    def __init__(self, attribute_metadata: _Optional[_Union[_audience_insights_attribute_pb2.AudienceInsightsAttributeMetadata, _Mapping]]=..., metrics: _Optional[_Union[AudienceCompositionMetrics, _Mapping]]=...) -> None:
        ...