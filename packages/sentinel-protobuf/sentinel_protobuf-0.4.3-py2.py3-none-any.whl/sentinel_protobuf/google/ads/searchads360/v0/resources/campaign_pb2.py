"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/campaign.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.common import bidding_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_common_dot_bidding__pb2
from ......google.ads.searchads360.v0.common import custom_parameter_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_common_dot_custom__parameter__pb2
from ......google.ads.searchads360.v0.common import frequency_cap_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_common_dot_frequency__cap__pb2
from ......google.ads.searchads360.v0.common import real_time_bidding_setting_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_common_dot_real__time__bidding__setting__pb2
from ......google.ads.searchads360.v0.enums import ad_serving_optimization_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_ad__serving__optimization__status__pb2
from ......google.ads.searchads360.v0.enums import advertising_channel_sub_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_advertising__channel__sub__type__pb2
from ......google.ads.searchads360.v0.enums import advertising_channel_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_advertising__channel__type__pb2
from ......google.ads.searchads360.v0.enums import asset_field_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_asset__field__type__pb2
from ......google.ads.searchads360.v0.enums import bidding_strategy_system_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_bidding__strategy__system__status__pb2
from ......google.ads.searchads360.v0.enums import bidding_strategy_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_bidding__strategy__type__pb2
from ......google.ads.searchads360.v0.enums import campaign_serving_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_campaign__serving__status__pb2
from ......google.ads.searchads360.v0.enums import campaign_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_campaign__status__pb2
from ......google.ads.searchads360.v0.enums import negative_geo_target_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_negative__geo__target__type__pb2
from ......google.ads.searchads360.v0.enums import optimization_goal_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_optimization__goal__type__pb2
from ......google.ads.searchads360.v0.enums import positive_geo_target_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_positive__geo__target__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/ads/searchads360/v0/resources/campaign.proto\x12$google.ads.searchads360.v0.resources\x1a/google/ads/searchads360/v0/common/bidding.proto\x1a8google/ads/searchads360/v0/common/custom_parameter.proto\x1a5google/ads/searchads360/v0/common/frequency_cap.proto\x1aAgoogle/ads/searchads360/v0/common/real_time_bidding_setting.proto\x1aEgoogle/ads/searchads360/v0/enums/ad_serving_optimization_status.proto\x1aCgoogle/ads/searchads360/v0/enums/advertising_channel_sub_type.proto\x1a?google/ads/searchads360/v0/enums/advertising_channel_type.proto\x1a7google/ads/searchads360/v0/enums/asset_field_type.proto\x1aEgoogle/ads/searchads360/v0/enums/bidding_strategy_system_status.proto\x1a<google/ads/searchads360/v0/enums/bidding_strategy_type.proto\x1a>google/ads/searchads360/v0/enums/campaign_serving_status.proto\x1a6google/ads/searchads360/v0/enums/campaign_status.proto\x1a?google/ads/searchads360/v0/enums/negative_geo_target_type.proto\x1a=google/ads/searchads360/v0/enums/optimization_goal_type.proto\x1a?google/ads/searchads360/v0/enums/positive_geo_target_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xc3\'\n\x08Campaign\x12C\n\rresource_name\x18\x01 \x01(\tB,\xe0A\x05\xfaA&\n$searchads360.googleapis.com/Campaign\x12\x14\n\x02id\x18; \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x11\n\x04name\x18: \x01(\tH\x02\x88\x01\x01\x12S\n\x06status\x18\x05 \x01(\x0e2C.google.ads.searchads360.v0.enums.CampaignStatusEnum.CampaignStatus\x12n\n\x0eserving_status\x18\x15 \x01(\x0e2Q.google.ads.searchads360.v0.enums.CampaignServingStatusEnum.CampaignServingStatusB\x03\xe0A\x03\x12\x8a\x01\n\x1ebidding_strategy_system_status\x18N \x01(\x0e2].google.ads.searchads360.v0.enums.BiddingStrategySystemStatusEnum.BiddingStrategySystemStatusB\x03\xe0A\x03\x12\x85\x01\n\x1ead_serving_optimization_status\x18\x08 \x01(\x0e2].google.ads.searchads360.v0.enums.AdServingOptimizationStatusEnum.AdServingOptimizationStatus\x12z\n\x18advertising_channel_type\x18\t \x01(\x0e2S.google.ads.searchads360.v0.enums.AdvertisingChannelTypeEnum.AdvertisingChannelTypeB\x03\xe0A\x05\x12\x84\x01\n\x1cadvertising_channel_sub_type\x18\n \x01(\x0e2Y.google.ads.searchads360.v0.enums.AdvertisingChannelSubTypeEnum.AdvertisingChannelSubTypeB\x03\xe0A\x05\x12"\n\x15tracking_url_template\x18< \x01(\tH\x03\x88\x01\x01\x12Q\n\x15url_custom_parameters\x18\x0c \x03(\x0b22.google.ads.searchads360.v0.common.CustomParameter\x12\\\n\x19real_time_bidding_setting\x18\' \x01(\x0b29.google.ads.searchads360.v0.common.RealTimeBiddingSetting\x12X\n\x10network_settings\x18\x0e \x01(\x0b2>.google.ads.searchads360.v0.resources.Campaign.NetworkSettings\x12j\n\x1adynamic_search_ads_setting\x18! \x01(\x0b2F.google.ads.searchads360.v0.resources.Campaign.DynamicSearchAdsSetting\x12X\n\x10shopping_setting\x18$ \x01(\x0b2>.google.ads.searchads360.v0.resources.Campaign.ShoppingSetting\x12d\n\x17geo_target_type_setting\x18/ \x01(\x0b2C.google.ads.searchads360.v0.resources.Campaign.GeoTargetTypeSetting\x12T\n\x10effective_labels\x18_ \x03(\tB:\xe0A\x03\xfaA4\n2searchads360.googleapis.com/CampaignEffectiveLabel\x12A\n\x06labels\x18= \x03(\tB1\xe0A\x03\xfaA+\n)searchads360.googleapis.com/CampaignLabel\x12M\n\x0fcampaign_budget\x18> \x01(\tB/\xfaA,\n*searchads360.googleapis.com/CampaignBudgetH\x04\x88\x01\x01\x12q\n\x15bidding_strategy_type\x18\x16 \x01(\x0e2M.google.ads.searchads360.v0.enums.BiddingStrategyTypeEnum.BiddingStrategyTypeB\x03\xe0A\x03\x12b\n\x1baccessible_bidding_strategy\x18G \x01(\tB=\xe0A\x03\xfaA7\n5searchads360.googleapis.com/AccessibleBiddingStrategy\x12\x17\n\nstart_date\x18? \x01(\tH\x05\x88\x01\x01\x12\x15\n\x08end_date\x18@ \x01(\tH\x06\x88\x01\x01\x12\x1d\n\x10final_url_suffix\x18A \x01(\tH\x07\x88\x01\x01\x12L\n\x0efrequency_caps\x18( \x03(\x0b24.google.ads.searchads360.v0.common.FrequencyCapEntry\x12d\n\x16selective_optimization\x18- \x01(\x0b2D.google.ads.searchads360.v0.resources.Campaign.SelectiveOptimization\x12i\n\x19optimization_goal_setting\x186 \x01(\x0b2F.google.ads.searchads360.v0.resources.Campaign.OptimizationGoalSetting\x12]\n\x10tracking_setting\x18. \x01(\x0b2>.google.ads.searchads360.v0.resources.Campaign.TrackingSettingB\x03\xe0A\x03\x12\x16\n\tengine_id\x18D \x01(\tB\x03\xe0A\x03\x12n\n!excluded_parent_asset_field_types\x18E \x03(\x0e2C.google.ads.searchads360.v0.enums.AssetFieldTypeEnum.AssetFieldType\x12\x18\n\x0bcreate_time\x18O \x01(\tB\x03\xe0A\x03\x12\x1a\n\rcreation_time\x18T \x01(\tB\x03\xe0A\x03\x12\x1f\n\x12last_modified_time\x18F \x01(\tB\x03\xe0A\x03\x12"\n\x15url_expansion_opt_out\x18H \x01(\x08H\x08\x88\x01\x01\x12L\n\x10bidding_strategy\x18C \x01(\tB0\xfaA-\n+searchads360.googleapis.com/BiddingStrategyH\x00\x12B\n\nmanual_cpa\x18J \x01(\x0b2,.google.ads.searchads360.v0.common.ManualCpaH\x00\x12B\n\nmanual_cpc\x18\x18 \x01(\x0b2,.google.ads.searchads360.v0.common.ManualCpcH\x00\x12B\n\nmanual_cpm\x18\x19 \x01(\x0b2,.google.ads.searchads360.v0.common.ManualCpmH\x00\x12V\n\x14maximize_conversions\x18\x1e \x01(\x0b26.google.ads.searchads360.v0.common.MaximizeConversionsH\x00\x12_\n\x19maximize_conversion_value\x18\x1f \x01(\x0b2:.google.ads.searchads360.v0.common.MaximizeConversionValueH\x00\x12B\n\ntarget_cpa\x18\x1a \x01(\x0b2,.google.ads.searchads360.v0.common.TargetCpaH\x00\x12[\n\x17target_impression_share\x180 \x01(\x0b28.google.ads.searchads360.v0.common.TargetImpressionShareH\x00\x12D\n\x0btarget_roas\x18\x1d \x01(\x0b2-.google.ads.searchads360.v0.common.TargetRoasH\x00\x12F\n\x0ctarget_spend\x18\x1b \x01(\x0b2..google.ads.searchads360.v0.common.TargetSpendH\x00\x12D\n\x0bpercent_cpc\x18" \x01(\x0b2-.google.ads.searchads360.v0.common.PercentCpcH\x00\x12B\n\ntarget_cpm\x18) \x01(\x0b2,.google.ads.searchads360.v0.common.TargetCpmH\x00\x1a\x99\x02\n\x0fNetworkSettings\x12!\n\x14target_google_search\x18\x05 \x01(\x08H\x00\x88\x01\x01\x12"\n\x15target_search_network\x18\x06 \x01(\x08H\x01\x88\x01\x01\x12#\n\x16target_content_network\x18\x07 \x01(\x08H\x02\x88\x01\x01\x12*\n\x1dtarget_partner_search_network\x18\x08 \x01(\x08H\x03\x88\x01\x01B\x17\n\x15_target_google_searchB\x18\n\x16_target_search_networkB\x19\n\x17_target_content_networkB \n\x1e_target_partner_search_network\x1a\x8f\x01\n\x17DynamicSearchAdsSetting\x12\x18\n\x0bdomain_name\x18\x06 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rlanguage_code\x18\x07 \x01(\tB\x03\xe0A\x02\x12#\n\x16use_supplied_urls_only\x18\x08 \x01(\x08H\x00\x88\x01\x01B\x19\n\x17_use_supplied_urls_only\x1a\x88\x02\n\x0fShoppingSetting\x12\x1d\n\x0bmerchant_id\x18\x05 \x01(\x03B\x03\xe0A\x05H\x00\x88\x01\x01\x12\x1a\n\rsales_country\x18\x06 \x01(\tH\x01\x88\x01\x01\x12\x12\n\nfeed_label\x18\n \x01(\t\x12\x1e\n\x11campaign_priority\x18\x07 \x01(\x05H\x02\x88\x01\x01\x12\x19\n\x0cenable_local\x18\x08 \x01(\x08H\x03\x88\x01\x01\x12"\n\x15use_vehicle_inventory\x18\t \x01(\x08B\x03\xe0A\x05B\x0e\n\x0c_merchant_idB\x10\n\x0e_sales_countryB\x14\n\x12_campaign_priorityB\x0f\n\r_enable_local\x1aB\n\x0fTrackingSetting\x12\x1e\n\x0ctracking_url\x18\x02 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01B\x0f\n\r_tracking_url\x1a\x80\x02\n\x14GeoTargetTypeSetting\x12s\n\x18positive_geo_target_type\x18\x01 \x01(\x0e2Q.google.ads.searchads360.v0.enums.PositiveGeoTargetTypeEnum.PositiveGeoTargetType\x12s\n\x18negative_geo_target_type\x18\x02 \x01(\x0e2Q.google.ads.searchads360.v0.enums.NegativeGeoTargetTypeEnum.NegativeGeoTargetType\x1af\n\x15SelectiveOptimization\x12M\n\x12conversion_actions\x18\x02 \x03(\tB1\xfaA.\n,searchads360.googleapis.com/ConversionAction\x1a\x8b\x01\n\x17OptimizationGoalSetting\x12p\n\x17optimization_goal_types\x18\x01 \x03(\x0e2O.google.ads.searchads360.v0.enums.OptimizationGoalTypeEnum.OptimizationGoalType:Z\xeaAW\n$searchads360.googleapis.com/Campaign\x12/customers/{customer_id}/campaigns/{campaign_id}B\x1b\n\x19campaign_bidding_strategyB\x05\n\x03_idB\x07\n\x05_nameB\x18\n\x16_tracking_url_templateB\x12\n\x10_campaign_budgetB\r\n\x0b_start_dateB\x0b\n\t_end_dateB\x13\n\x11_final_url_suffixB\x18\n\x16_url_expansion_opt_outB\x8d\x02\n(com.google.ads.searchads360.v0.resourcesB\rCampaignProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.campaign_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\rCampaignProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_CAMPAIGN_DYNAMICSEARCHADSSETTING'].fields_by_name['domain_name']._loaded_options = None
    _globals['_CAMPAIGN_DYNAMICSEARCHADSSETTING'].fields_by_name['domain_name']._serialized_options = b'\xe0A\x02'
    _globals['_CAMPAIGN_DYNAMICSEARCHADSSETTING'].fields_by_name['language_code']._loaded_options = None
    _globals['_CAMPAIGN_DYNAMICSEARCHADSSETTING'].fields_by_name['language_code']._serialized_options = b'\xe0A\x02'
    _globals['_CAMPAIGN_SHOPPINGSETTING'].fields_by_name['merchant_id']._loaded_options = None
    _globals['_CAMPAIGN_SHOPPINGSETTING'].fields_by_name['merchant_id']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGN_SHOPPINGSETTING'].fields_by_name['use_vehicle_inventory']._loaded_options = None
    _globals['_CAMPAIGN_SHOPPINGSETTING'].fields_by_name['use_vehicle_inventory']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGN_TRACKINGSETTING'].fields_by_name['tracking_url']._loaded_options = None
    _globals['_CAMPAIGN_TRACKINGSETTING'].fields_by_name['tracking_url']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGN_SELECTIVEOPTIMIZATION'].fields_by_name['conversion_actions']._loaded_options = None
    _globals['_CAMPAIGN_SELECTIVEOPTIMIZATION'].fields_by_name['conversion_actions']._serialized_options = b'\xfaA.\n,searchads360.googleapis.com/ConversionAction'
    _globals['_CAMPAIGN'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CAMPAIGN'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA&\n$searchads360.googleapis.com/Campaign'
    _globals['_CAMPAIGN'].fields_by_name['id']._loaded_options = None
    _globals['_CAMPAIGN'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGN'].fields_by_name['serving_status']._loaded_options = None
    _globals['_CAMPAIGN'].fields_by_name['serving_status']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGN'].fields_by_name['bidding_strategy_system_status']._loaded_options = None
    _globals['_CAMPAIGN'].fields_by_name['bidding_strategy_system_status']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGN'].fields_by_name['advertising_channel_type']._loaded_options = None
    _globals['_CAMPAIGN'].fields_by_name['advertising_channel_type']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGN'].fields_by_name['advertising_channel_sub_type']._loaded_options = None
    _globals['_CAMPAIGN'].fields_by_name['advertising_channel_sub_type']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGN'].fields_by_name['effective_labels']._loaded_options = None
    _globals['_CAMPAIGN'].fields_by_name['effective_labels']._serialized_options = b'\xe0A\x03\xfaA4\n2searchads360.googleapis.com/CampaignEffectiveLabel'
    _globals['_CAMPAIGN'].fields_by_name['labels']._loaded_options = None
    _globals['_CAMPAIGN'].fields_by_name['labels']._serialized_options = b'\xe0A\x03\xfaA+\n)searchads360.googleapis.com/CampaignLabel'
    _globals['_CAMPAIGN'].fields_by_name['campaign_budget']._loaded_options = None
    _globals['_CAMPAIGN'].fields_by_name['campaign_budget']._serialized_options = b'\xfaA,\n*searchads360.googleapis.com/CampaignBudget'
    _globals['_CAMPAIGN'].fields_by_name['bidding_strategy_type']._loaded_options = None
    _globals['_CAMPAIGN'].fields_by_name['bidding_strategy_type']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGN'].fields_by_name['accessible_bidding_strategy']._loaded_options = None
    _globals['_CAMPAIGN'].fields_by_name['accessible_bidding_strategy']._serialized_options = b'\xe0A\x03\xfaA7\n5searchads360.googleapis.com/AccessibleBiddingStrategy'
    _globals['_CAMPAIGN'].fields_by_name['tracking_setting']._loaded_options = None
    _globals['_CAMPAIGN'].fields_by_name['tracking_setting']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGN'].fields_by_name['engine_id']._loaded_options = None
    _globals['_CAMPAIGN'].fields_by_name['engine_id']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGN'].fields_by_name['create_time']._loaded_options = None
    _globals['_CAMPAIGN'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGN'].fields_by_name['creation_time']._loaded_options = None
    _globals['_CAMPAIGN'].fields_by_name['creation_time']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGN'].fields_by_name['last_modified_time']._loaded_options = None
    _globals['_CAMPAIGN'].fields_by_name['last_modified_time']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGN'].fields_by_name['bidding_strategy']._loaded_options = None
    _globals['_CAMPAIGN'].fields_by_name['bidding_strategy']._serialized_options = b'\xfaA-\n+searchads360.googleapis.com/BiddingStrategy'
    _globals['_CAMPAIGN']._loaded_options = None
    _globals['_CAMPAIGN']._serialized_options = b'\xeaAW\n$searchads360.googleapis.com/Campaign\x12/customers/{customer_id}/campaigns/{campaign_id}'
    _globals['_CAMPAIGN']._serialized_start = 1091
    _globals['_CAMPAIGN']._serialized_end = 6150
    _globals['_CAMPAIGN_NETWORKSETTINGS']._serialized_start = 4625
    _globals['_CAMPAIGN_NETWORKSETTINGS']._serialized_end = 4906
    _globals['_CAMPAIGN_DYNAMICSEARCHADSSETTING']._serialized_start = 4909
    _globals['_CAMPAIGN_DYNAMICSEARCHADSSETTING']._serialized_end = 5052
    _globals['_CAMPAIGN_SHOPPINGSETTING']._serialized_start = 5055
    _globals['_CAMPAIGN_SHOPPINGSETTING']._serialized_end = 5319
    _globals['_CAMPAIGN_TRACKINGSETTING']._serialized_start = 5321
    _globals['_CAMPAIGN_TRACKINGSETTING']._serialized_end = 5387
    _globals['_CAMPAIGN_GEOTARGETTYPESETTING']._serialized_start = 5390
    _globals['_CAMPAIGN_GEOTARGETTYPESETTING']._serialized_end = 5646
    _globals['_CAMPAIGN_SELECTIVEOPTIMIZATION']._serialized_start = 5648
    _globals['_CAMPAIGN_SELECTIVEOPTIMIZATION']._serialized_end = 5750
    _globals['_CAMPAIGN_OPTIMIZATIONGOALSETTING']._serialized_start = 5753
    _globals['_CAMPAIGN_OPTIMIZATIONGOALSETTING']._serialized_end = 5892