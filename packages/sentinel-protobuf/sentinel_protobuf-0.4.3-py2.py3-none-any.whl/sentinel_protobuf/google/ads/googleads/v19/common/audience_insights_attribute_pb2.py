"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/common/audience_insights_attribute.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.common import criteria_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_criteria__pb2
from ......google.ads.googleads.v19.enums import audience_insights_dimension_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_audience__insights__dimension__pb2
from ......google.ads.googleads.v19.enums import insights_knowledge_graph_entity_capabilities_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_insights__knowledge__graph__entity__capabilities__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/ads/googleads/v19/common/audience_insights_attribute.proto\x12\x1fgoogle.ads.googleads.v19.common\x1a.google/ads/googleads/v19/common/criteria.proto\x1a@google/ads/googleads/v19/enums/audience_insights_dimension.proto\x1aQgoogle/ads/googleads/v19/enums/insights_knowledge_graph_entity_capabilities.proto\x1a\x1fgoogle/api/field_behavior.proto"\xdf\x07\n!AudienceInsightsAttributeMetadata\x12j\n\tdimension\x18\x01 \x01(\x0e2W.google.ads.googleads.v19.enums.AudienceInsightsDimensionEnum.AudienceInsightsDimension\x12M\n\tattribute\x18\x02 \x01(\x0b2:.google.ads.googleads.v19.common.AudienceInsightsAttribute\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12\x14\n\x0cdisplay_info\x18\x04 \x01(\t\x12\x1f\n\x17potential_youtube_reach\x18\x08 \x01(\x03\x12\x18\n\x10subscriber_share\x18\t \x01(\x01\x12\x14\n\x0cviewer_share\x18\r \x01(\x01\x12d\n\x18youtube_channel_metadata\x18\x05 \x01(\x0b2@.google.ads.googleads.v19.common.YouTubeChannelAttributeMetadataH\x00\x12`\n\x16youtube_video_metadata\x18\n \x01(\x0b2>.google.ads.googleads.v19.common.YouTubeVideoAttributeMetadataH\x00\x12e\n\x1adynamic_attribute_metadata\x18\x06 \x01(\x0b2?.google.ads.googleads.v19.common.DynamicLineupAttributeMetadataH\x00\x12a\n\x1blocation_attribute_metadata\x18\x07 \x01(\x0b2:.google.ads.googleads.v19.common.LocationAttributeMetadataH\x00\x12j\n user_interest_attribute_metadata\x18\x0b \x01(\x0b2>.google.ads.googleads.v19.common.UserInterestAttributeMetadataH\x00\x12n\n"knowledge_graph_attribute_metadata\x18\x0c \x01(\x0b2@.google.ads.googleads.v19.common.KnowledgeGraphAttributeMetadataH\x00B\x14\n\x12dimension_metadata"\xe4\x06\n\x19AudienceInsightsAttribute\x12B\n\tage_range\x18\x01 \x01(\x0b2-.google.ads.googleads.v19.common.AgeRangeInfoH\x00\x12=\n\x06gender\x18\x02 \x01(\x0b2+.google.ads.googleads.v19.common.GenderInfoH\x00\x12A\n\x08location\x18\x03 \x01(\x0b2-.google.ads.googleads.v19.common.LocationInfoH\x00\x12J\n\ruser_interest\x18\x04 \x01(\x0b21.google.ads.googleads.v19.common.UserInterestInfoH\x00\x12I\n\x06entity\x18\x05 \x01(\x0b27.google.ads.googleads.v19.common.AudienceInsightsEntityH\x00\x12M\n\x08category\x18\x06 \x01(\x0b29.google.ads.googleads.v19.common.AudienceInsightsCategoryH\x00\x12X\n\x0edynamic_lineup\x18\x07 \x01(\x0b2>.google.ads.googleads.v19.common.AudienceInsightsDynamicLineupH\x00\x12N\n\x0fparental_status\x18\x08 \x01(\x0b23.google.ads.googleads.v19.common.ParentalStatusInfoH\x00\x12H\n\x0cincome_range\x18\t \x01(\x0b20.google.ads.googleads.v19.common.IncomeRangeInfoH\x00\x12N\n\x0fyoutube_channel\x18\n \x01(\x0b23.google.ads.googleads.v19.common.YouTubeChannelInfoH\x00\x12J\n\ryoutube_video\x18\x0b \x01(\x0b21.google.ads.googleads.v19.common.YouTubeVideoInfoH\x00B\x0b\n\tattribute"\xba\x01\n\x15AudienceInsightsTopic\x12I\n\x06entity\x18\x01 \x01(\x0b27.google.ads.googleads.v19.common.AudienceInsightsEntityH\x00\x12M\n\x08category\x18\x02 \x01(\x0b29.google.ads.googleads.v19.common.AudienceInsightsCategoryH\x00B\x07\n\x05topic"A\n\x16AudienceInsightsEntity\x12\'\n\x1aknowledge_graph_machine_id\x18\x01 \x01(\tB\x03\xe0A\x02"4\n\x18AudienceInsightsCategory\x12\x18\n\x0bcategory_id\x18\x01 \x01(\tB\x03\xe0A\x02"?\n\x1dAudienceInsightsDynamicLineup\x12\x1e\n\x11dynamic_lineup_id\x18\x01 \x01(\tB\x03\xe0A\x02";\n\x1fYouTubeChannelAttributeMetadata\x12\x18\n\x10subscriber_count\x18\x01 \x01(\x03"I\n\x1dYouTubeVideoAttributeMetadata\x12\x15\n\rthumbnail_url\x18\x01 \x01(\t\x12\x11\n\tvideo_url\x18\x02 \x01(\t"\xfc\x04\n\x1eDynamicLineupAttributeMetadata\x12H\n\x11inventory_country\x18\x01 \x01(\x0b2-.google.ads.googleads.v19.common.LocationInfo\x12%\n\x18median_monthly_inventory\x18\x02 \x01(\x03H\x00\x88\x01\x01\x12&\n\x19channel_count_lower_bound\x18\x03 \x01(\x03H\x01\x88\x01\x01\x12&\n\x19channel_count_upper_bound\x18\x04 \x01(\x03H\x02\x88\x01\x01\x12f\n\x0fsample_channels\x18\x05 \x03(\x0b2M.google.ads.googleads.v19.common.DynamicLineupAttributeMetadata.SampleChannel\x1a\xd7\x01\n\rSampleChannel\x12L\n\x0fyoutube_channel\x18\x01 \x01(\x0b23.google.ads.googleads.v19.common.YouTubeChannelInfo\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12b\n\x18youtube_channel_metadata\x18\x03 \x01(\x0b2@.google.ads.googleads.v19.common.YouTubeChannelAttributeMetadataB\x1b\n\x19_median_monthly_inventoryB\x1c\n\x1a_channel_count_lower_boundB\x1c\n\x1a_channel_count_upper_bound"d\n\x19LocationAttributeMetadata\x12G\n\x10country_location\x18\x01 \x01(\x0b2-.google.ads.googleads.v19.common.LocationInfo"B\n\x1dUserInterestAttributeMetadata\x12!\n\x19user_interest_description\x18\x01 \x01(\t"\xb6\x01\n\x1fKnowledgeGraphAttributeMetadata\x12\x92\x01\n\x13entity_capabilities\x18\x01 \x03(\x0e2u.google.ads.googleads.v19.enums.InsightsKnowledgeGraphEntityCapabilitiesEnum.InsightsKnowledgeGraphEntityCapabilitiesB\xfe\x01\n#com.google.ads.googleads.v19.commonB\x1eAudienceInsightsAttributeProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v19/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V19.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V19\\Common\xea\x02#Google::Ads::GoogleAds::V19::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.common.audience_insights_attribute_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v19.commonB\x1eAudienceInsightsAttributeProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v19/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V19.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V19\\Common\xea\x02#Google::Ads::GoogleAds::V19::Common'
    _globals['_AUDIENCEINSIGHTSENTITY'].fields_by_name['knowledge_graph_machine_id']._loaded_options = None
    _globals['_AUDIENCEINSIGHTSENTITY'].fields_by_name['knowledge_graph_machine_id']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCEINSIGHTSCATEGORY'].fields_by_name['category_id']._loaded_options = None
    _globals['_AUDIENCEINSIGHTSCATEGORY'].fields_by_name['category_id']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCEINSIGHTSDYNAMICLINEUP'].fields_by_name['dynamic_lineup_id']._loaded_options = None
    _globals['_AUDIENCEINSIGHTSDYNAMICLINEUP'].fields_by_name['dynamic_lineup_id']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCEINSIGHTSATTRIBUTEMETADATA']._serialized_start = 333
    _globals['_AUDIENCEINSIGHTSATTRIBUTEMETADATA']._serialized_end = 1324
    _globals['_AUDIENCEINSIGHTSATTRIBUTE']._serialized_start = 1327
    _globals['_AUDIENCEINSIGHTSATTRIBUTE']._serialized_end = 2195
    _globals['_AUDIENCEINSIGHTSTOPIC']._serialized_start = 2198
    _globals['_AUDIENCEINSIGHTSTOPIC']._serialized_end = 2384
    _globals['_AUDIENCEINSIGHTSENTITY']._serialized_start = 2386
    _globals['_AUDIENCEINSIGHTSENTITY']._serialized_end = 2451
    _globals['_AUDIENCEINSIGHTSCATEGORY']._serialized_start = 2453
    _globals['_AUDIENCEINSIGHTSCATEGORY']._serialized_end = 2505
    _globals['_AUDIENCEINSIGHTSDYNAMICLINEUP']._serialized_start = 2507
    _globals['_AUDIENCEINSIGHTSDYNAMICLINEUP']._serialized_end = 2570
    _globals['_YOUTUBECHANNELATTRIBUTEMETADATA']._serialized_start = 2572
    _globals['_YOUTUBECHANNELATTRIBUTEMETADATA']._serialized_end = 2631
    _globals['_YOUTUBEVIDEOATTRIBUTEMETADATA']._serialized_start = 2633
    _globals['_YOUTUBEVIDEOATTRIBUTEMETADATA']._serialized_end = 2706
    _globals['_DYNAMICLINEUPATTRIBUTEMETADATA']._serialized_start = 2709
    _globals['_DYNAMICLINEUPATTRIBUTEMETADATA']._serialized_end = 3345
    _globals['_DYNAMICLINEUPATTRIBUTEMETADATA_SAMPLECHANNEL']._serialized_start = 3041
    _globals['_DYNAMICLINEUPATTRIBUTEMETADATA_SAMPLECHANNEL']._serialized_end = 3256
    _globals['_LOCATIONATTRIBUTEMETADATA']._serialized_start = 3347
    _globals['_LOCATIONATTRIBUTEMETADATA']._serialized_end = 3447
    _globals['_USERINTERESTATTRIBUTEMETADATA']._serialized_start = 3449
    _globals['_USERINTERESTATTRIBUTEMETADATA']._serialized_end = 3515
    _globals['_KNOWLEDGEGRAPHATTRIBUTEMETADATA']._serialized_start = 3518
    _globals['_KNOWLEDGEGRAPHATTRIBUTEMETADATA']._serialized_end = 3700