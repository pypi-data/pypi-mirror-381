"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/ad_group.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.common import custom_parameter_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_custom__parameter__pb2
from ......google.ads.googleads.v20.common import targeting_setting_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_targeting__setting__pb2
from ......google.ads.googleads.v20.enums import ad_group_ad_rotation_mode_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_ad__group__ad__rotation__mode__pb2
from ......google.ads.googleads.v20.enums import ad_group_primary_status_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_ad__group__primary__status__pb2
from ......google.ads.googleads.v20.enums import ad_group_primary_status_reason_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_ad__group__primary__status__reason__pb2
from ......google.ads.googleads.v20.enums import ad_group_status_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_ad__group__status__pb2
from ......google.ads.googleads.v20.enums import ad_group_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_ad__group__type__pb2
from ......google.ads.googleads.v20.enums import asset_field_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__field__type__pb2
from ......google.ads.googleads.v20.enums import asset_set_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__set__type__pb2
from ......google.ads.googleads.v20.enums import bidding_source_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_bidding__source__pb2
from ......google.ads.googleads.v20.enums import demand_gen_channel_config_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_demand__gen__channel__config__pb2
from ......google.ads.googleads.v20.enums import demand_gen_channel_strategy_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_demand__gen__channel__strategy__pb2
from ......google.ads.googleads.v20.enums import targeting_dimension_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_targeting__dimension__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/ads/googleads/v20/resources/ad_group.proto\x12"google.ads.googleads.v20.resources\x1a6google/ads/googleads/v20/common/custom_parameter.proto\x1a7google/ads/googleads/v20/common/targeting_setting.proto\x1a>google/ads/googleads/v20/enums/ad_group_ad_rotation_mode.proto\x1a<google/ads/googleads/v20/enums/ad_group_primary_status.proto\x1aCgoogle/ads/googleads/v20/enums/ad_group_primary_status_reason.proto\x1a4google/ads/googleads/v20/enums/ad_group_status.proto\x1a2google/ads/googleads/v20/enums/ad_group_type.proto\x1a5google/ads/googleads/v20/enums/asset_field_type.proto\x1a3google/ads/googleads/v20/enums/asset_set_type.proto\x1a3google/ads/googleads/v20/enums/bidding_source.proto\x1a>google/ads/googleads/v20/enums/demand_gen_channel_config.proto\x1a@google/ads/googleads/v20/enums/demand_gen_channel_strategy.proto\x1a8google/ads/googleads/v20/enums/targeting_dimension.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xbe\x1b\n\x07AdGroup\x12?\n\rresource_name\x18\x01 \x01(\tB(\xe0A\x05\xfaA"\n googleads.googleapis.com/AdGroup\x12\x14\n\x02id\x18" \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x11\n\x04name\x18# \x01(\tH\x01\x88\x01\x01\x12O\n\x06status\x18\x05 \x01(\x0e2?.google.ads.googleads.v20.enums.AdGroupStatusEnum.AdGroupStatus\x12N\n\x04type\x18\x0c \x01(\x0e2;.google.ads.googleads.v20.enums.AdGroupTypeEnum.AdGroupTypeB\x03\xe0A\x05\x12i\n\x10ad_rotation_mode\x18\x16 \x01(\x0e2O.google.ads.googleads.v20.enums.AdGroupAdRotationModeEnum.AdGroupAdRotationMode\x12D\n\rbase_ad_group\x18$ \x01(\tB(\xe0A\x03\xfaA"\n googleads.googleapis.com/AdGroupH\x02\x88\x01\x01\x12"\n\x15tracking_url_template\x18% \x01(\tH\x03\x88\x01\x01\x12O\n\x15url_custom_parameters\x18\x06 \x03(\x0b20.google.ads.googleads.v20.common.CustomParameter\x12@\n\x08campaign\x18& \x01(\tB)\xe0A\x05\xfaA#\n!googleads.googleapis.com/CampaignH\x04\x88\x01\x01\x12\x1b\n\x0ecpc_bid_micros\x18\' \x01(\x03H\x05\x88\x01\x01\x12*\n\x18effective_cpc_bid_micros\x189 \x01(\x03B\x03\xe0A\x03H\x06\x88\x01\x01\x12\x1b\n\x0ecpm_bid_micros\x18( \x01(\x03H\x07\x88\x01\x01\x12\x1e\n\x11target_cpa_micros\x18) \x01(\x03H\x08\x88\x01\x01\x12\x1b\n\x0ecpv_bid_micros\x18* \x01(\x03H\t\x88\x01\x01\x12\x1e\n\x11target_cpm_micros\x18+ \x01(\x03H\n\x88\x01\x01\x12\x18\n\x0btarget_roas\x18, \x01(\x01H\x0b\x88\x01\x01\x12#\n\x16percent_cpc_bid_micros\x18- \x01(\x03H\x0c\x88\x01\x01\x12\x1d\n\x10fixed_cpm_micros\x18@ \x01(\x03H\r\x88\x01\x01\x12\x1e\n\x11target_cpv_micros\x18A \x01(\x03H\x0e\x88\x01\x01\x12#\n\x1boptimized_targeting_enabled\x18; \x01(\x08\x12%\n\x1dexclude_demographic_expansion\x18C \x01(\x08\x12o\n\x1cdisplay_custom_bid_dimension\x18\x17 \x01(\x0e2I.google.ads.googleads.v20.enums.TargetingDimensionEnum.TargetingDimension\x12\x1d\n\x10final_url_suffix\x18. \x01(\tH\x0f\x88\x01\x01\x12L\n\x11targeting_setting\x18\x19 \x01(\x0b21.google.ads.googleads.v20.common.TargetingSetting\x12Z\n\x10audience_setting\x188 \x01(\x0b2;.google.ads.googleads.v20.resources.AdGroup.AudienceSettingB\x03\xe0A\x05\x12-\n\x1beffective_target_cpa_micros\x18/ \x01(\x03B\x03\xe0A\x03H\x10\x88\x01\x01\x12i\n\x1beffective_target_cpa_source\x18\x1d \x01(\x0e2?.google.ads.googleads.v20.enums.BiddingSourceEnum.BiddingSourceB\x03\xe0A\x03\x12\'\n\x15effective_target_roas\x180 \x01(\x01B\x03\xe0A\x03H\x11\x88\x01\x01\x12j\n\x1ceffective_target_roas_source\x18  \x01(\x0e2?.google.ads.googleads.v20.enums.BiddingSourceEnum.BiddingSourceB\x03\xe0A\x03\x12=\n\x06labels\x181 \x03(\tB-\xe0A\x03\xfaA\'\n%googleads.googleapis.com/AdGroupLabel\x12l\n!excluded_parent_asset_field_types\x186 \x03(\x0e2A.google.ads.googleads.v20.enums.AssetFieldTypeEnum.AssetFieldType\x12f\n\x1fexcluded_parent_asset_set_types\x18: \x03(\x0e2=.google.ads.googleads.v20.enums.AssetSetTypeEnum.AssetSetType\x12j\n\x0eprimary_status\x18> \x01(\x0e2M.google.ads.googleads.v20.enums.AdGroupPrimaryStatusEnum.AdGroupPrimaryStatusB\x03\xe0A\x03\x12~\n\x16primary_status_reasons\x18? \x03(\x0e2Y.google.ads.googleads.v20.enums.AdGroupPrimaryStatusReasonEnum.AdGroupPrimaryStatusReasonB\x03\xe0A\x03\x12j\n\x1cdemand_gen_ad_group_settings\x18[ \x01(\x0b2D.google.ads.googleads.v20.resources.AdGroup.DemandGenAdGroupSettings\x1a4\n\x0fAudienceSetting\x12!\n\x14use_audience_grouped\x18\x01 \x01(\x08B\x03\xe0A\x05\x1a\xdf\x05\n\x18DemandGenAdGroupSettings\x12w\n\x10channel_controls\x18\x01 \x01(\x0b2].google.ads.googleads.v20.resources.AdGroup.DemandGenAdGroupSettings.DemandGenChannelControls\x1a\xc9\x04\n\x18DemandGenChannelControls\x12n\n\x0echannel_config\x18\x01 \x01(\x0e2Q.google.ads.googleads.v20.enums.DemandGenChannelConfigEnum.DemandGenChannelConfigB\x03\xe0A\x03\x12q\n\x10channel_strategy\x18\x02 \x01(\x0e2U.google.ads.googleads.v20.enums.DemandGenChannelStrategyEnum.DemandGenChannelStrategyH\x00\x12\x94\x01\n\x11selected_channels\x18\x03 \x01(\x0b2w.google.ads.googleads.v20.resources.AdGroup.DemandGenAdGroupSettings.DemandGenChannelControls.DemandGenSelectedChannelsH\x00\x1a\x99\x01\n\x19DemandGenSelectedChannels\x12\x19\n\x11youtube_in_stream\x18\x01 \x01(\x08\x12\x17\n\x0fyoutube_in_feed\x18\x02 \x01(\x08\x12\x16\n\x0eyoutube_shorts\x18\x03 \x01(\x08\x12\x10\n\x08discover\x18\x04 \x01(\x08\x12\r\n\x05gmail\x18\x05 \x01(\x08\x12\x0f\n\x07display\x18\x06 \x01(\x08B\x17\n\x15channel_configuration:U\xeaAR\n googleads.googleapis.com/AdGroup\x12.customers/{customer_id}/adGroups/{ad_group_id}B\x05\n\x03_idB\x07\n\x05_nameB\x10\n\x0e_base_ad_groupB\x18\n\x16_tracking_url_templateB\x0b\n\t_campaignB\x11\n\x0f_cpc_bid_microsB\x1b\n\x19_effective_cpc_bid_microsB\x11\n\x0f_cpm_bid_microsB\x14\n\x12_target_cpa_microsB\x11\n\x0f_cpv_bid_microsB\x14\n\x12_target_cpm_microsB\x0e\n\x0c_target_roasB\x19\n\x17_percent_cpc_bid_microsB\x13\n\x11_fixed_cpm_microsB\x14\n\x12_target_cpv_microsB\x13\n\x11_final_url_suffixB\x1e\n\x1c_effective_target_cpa_microsB\x18\n\x16_effective_target_roasB\xfe\x01\n&com.google.ads.googleads.v20.resourcesB\x0cAdGroupProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.ad_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x0cAdGroupProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_ADGROUP_AUDIENCESETTING'].fields_by_name['use_audience_grouped']._loaded_options = None
    _globals['_ADGROUP_AUDIENCESETTING'].fields_by_name['use_audience_grouped']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUP_DEMANDGENADGROUPSETTINGS_DEMANDGENCHANNELCONTROLS'].fields_by_name['channel_config']._loaded_options = None
    _globals['_ADGROUP_DEMANDGENADGROUPSETTINGS_DEMANDGENCHANNELCONTROLS'].fields_by_name['channel_config']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUP'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA"\n googleads.googleapis.com/AdGroup'
    _globals['_ADGROUP'].fields_by_name['id']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUP'].fields_by_name['type']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['type']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUP'].fields_by_name['base_ad_group']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['base_ad_group']._serialized_options = b'\xe0A\x03\xfaA"\n googleads.googleapis.com/AdGroup'
    _globals['_ADGROUP'].fields_by_name['campaign']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['campaign']._serialized_options = b'\xe0A\x05\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_ADGROUP'].fields_by_name['effective_cpc_bid_micros']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['effective_cpc_bid_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUP'].fields_by_name['audience_setting']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['audience_setting']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUP'].fields_by_name['effective_target_cpa_micros']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['effective_target_cpa_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUP'].fields_by_name['effective_target_cpa_source']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['effective_target_cpa_source']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUP'].fields_by_name['effective_target_roas']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['effective_target_roas']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUP'].fields_by_name['effective_target_roas_source']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['effective_target_roas_source']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUP'].fields_by_name['labels']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['labels']._serialized_options = b"\xe0A\x03\xfaA'\n%googleads.googleapis.com/AdGroupLabel"
    _globals['_ADGROUP'].fields_by_name['primary_status']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['primary_status']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUP'].fields_by_name['primary_status_reasons']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['primary_status_reasons']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUP']._loaded_options = None
    _globals['_ADGROUP']._serialized_options = b'\xeaAR\n googleads.googleapis.com/AdGroup\x12.customers/{customer_id}/adGroups/{ad_group_id}'
    _globals['_ADGROUP']._serialized_start = 913
    _globals['_ADGROUP']._serialized_end = 4431
    _globals['_ADGROUP_AUDIENCESETTING']._serialized_start = 3186
    _globals['_ADGROUP_AUDIENCESETTING']._serialized_end = 3238
    _globals['_ADGROUP_DEMANDGENADGROUPSETTINGS']._serialized_start = 3241
    _globals['_ADGROUP_DEMANDGENADGROUPSETTINGS']._serialized_end = 3976
    _globals['_ADGROUP_DEMANDGENADGROUPSETTINGS_DEMANDGENCHANNELCONTROLS']._serialized_start = 3391
    _globals['_ADGROUP_DEMANDGENADGROUPSETTINGS_DEMANDGENCHANNELCONTROLS']._serialized_end = 3976
    _globals['_ADGROUP_DEMANDGENADGROUPSETTINGS_DEMANDGENCHANNELCONTROLS_DEMANDGENSELECTEDCHANNELS']._serialized_start = 3798
    _globals['_ADGROUP_DEMANDGENADGROUPSETTINGS_DEMANDGENCHANNELCONTROLS_DEMANDGENSELECTEDCHANNELS']._serialized_end = 3951