"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/change_status.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import change_status_operation_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_change__status__operation__pb2
from ......google.ads.googleads.v21.enums import change_status_resource_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_change__status__resource__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/ads/googleads/v21/resources/change_status.proto\x12"google.ads.googleads.v21.resources\x1a<google/ads/googleads/v21/enums/change_status_operation.proto\x1a@google/ads/googleads/v21/enums/change_status_resource_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa1\x0e\n\x0cChangeStatus\x12D\n\rresource_name\x18\x01 \x01(\tB-\xe0A\x03\xfaA\'\n%googleads.googleapis.com/ChangeStatus\x12\'\n\x15last_change_date_time\x18\x18 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12q\n\rresource_type\x18\x04 \x01(\x0e2U.google.ads.googleads.v21.enums.ChangeStatusResourceTypeEnum.ChangeStatusResourceTypeB\x03\xe0A\x03\x12@\n\x08campaign\x18\x11 \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/CampaignH\x01\x88\x01\x01\x12?\n\x08ad_group\x18\x12 \x01(\tB(\xe0A\x03\xfaA"\n googleads.googleapis.com/AdGroupH\x02\x88\x01\x01\x12m\n\x0fresource_status\x18\x08 \x01(\x0e2O.google.ads.googleads.v21.enums.ChangeStatusOperationEnum.ChangeStatusOperationB\x03\xe0A\x03\x12D\n\x0bad_group_ad\x18\x19 \x01(\tB*\xe0A\x03\xfaA$\n"googleads.googleapis.com/AdGroupAdH\x03\x88\x01\x01\x12R\n\x12ad_group_criterion\x18\x1a \x01(\tB1\xe0A\x03\xfaA+\n)googleads.googleapis.com/AdGroupCriterionH\x04\x88\x01\x01\x12S\n\x12campaign_criterion\x18\x1b \x01(\tB2\xe0A\x03\xfaA,\n*googleads.googleapis.com/CampaignCriterionH\x05\x88\x01\x01\x12W\n\x15ad_group_bid_modifier\x18  \x01(\tB3\xe0A\x03\xfaA-\n+googleads.googleapis.com/AdGroupBidModifierH\x06\x88\x01\x01\x12>\n\nshared_set\x18! \x01(\tB*\xe0A\x03\xfaA$\n"googleads.googleapis.com/SharedSet\x12O\n\x13campaign_shared_set\x18" \x01(\tB2\xe0A\x03\xfaA,\n*googleads.googleapis.com/CampaignSharedSet\x125\n\x05asset\x18# \x01(\tB&\xe0A\x03\xfaA \n\x1egoogleads.googleapis.com/Asset\x12F\n\x0ecustomer_asset\x18$ \x01(\tB.\xe0A\x03\xfaA(\n&googleads.googleapis.com/CustomerAsset\x12F\n\x0ecampaign_asset\x18% \x01(\tB.\xe0A\x03\xfaA(\n&googleads.googleapis.com/CampaignAsset\x12E\n\x0ead_group_asset\x18& \x01(\tB-\xe0A\x03\xfaA\'\n%googleads.googleapis.com/AdGroupAsset\x12L\n\x11combined_audience\x18( \x01(\tB1\xe0A\x03\xfaA+\n)googleads.googleapis.com/CombinedAudience\x12@\n\x0basset_group\x18) \x01(\tB+\xe0A\x03\xfaA%\n#googleads.googleapis.com/AssetGroup\x12<\n\tasset_set\x18+ \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/AssetSet\x12H\n\x0fcampaign_budget\x18* \x01(\tB/\xe0A\x03\xfaA)\n\'googleads.googleapis.com/CampaignBudget\x12M\n\x12campaign_asset_set\x18, \x01(\tB1\xe0A\x03\xfaA+\n)googleads.googleapis.com/CampaignAssetSet:c\xeaA`\n%googleads.googleapis.com/ChangeStatus\x127customers/{customer_id}/changeStatus/{change_status_id}B\x18\n\x16_last_change_date_timeB\x0b\n\t_campaignB\x0b\n\t_ad_groupB\x0e\n\x0c_ad_group_adB\x15\n\x13_ad_group_criterionB\x15\n\x13_campaign_criterionB\x18\n\x16_ad_group_bid_modifierB\x83\x02\n&com.google.ads.googleads.v21.resourcesB\x11ChangeStatusProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.change_status_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\x11ChangeStatusProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_CHANGESTATUS'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['resource_name']._serialized_options = b"\xe0A\x03\xfaA'\n%googleads.googleapis.com/ChangeStatus"
    _globals['_CHANGESTATUS'].fields_by_name['last_change_date_time']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['last_change_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGESTATUS'].fields_by_name['resource_type']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['resource_type']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGESTATUS'].fields_by_name['campaign']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['campaign']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_CHANGESTATUS'].fields_by_name['ad_group']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['ad_group']._serialized_options = b'\xe0A\x03\xfaA"\n googleads.googleapis.com/AdGroup'
    _globals['_CHANGESTATUS'].fields_by_name['resource_status']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['resource_status']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGESTATUS'].fields_by_name['ad_group_ad']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['ad_group_ad']._serialized_options = b'\xe0A\x03\xfaA$\n"googleads.googleapis.com/AdGroupAd'
    _globals['_CHANGESTATUS'].fields_by_name['ad_group_criterion']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['ad_group_criterion']._serialized_options = b'\xe0A\x03\xfaA+\n)googleads.googleapis.com/AdGroupCriterion'
    _globals['_CHANGESTATUS'].fields_by_name['campaign_criterion']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['campaign_criterion']._serialized_options = b'\xe0A\x03\xfaA,\n*googleads.googleapis.com/CampaignCriterion'
    _globals['_CHANGESTATUS'].fields_by_name['ad_group_bid_modifier']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['ad_group_bid_modifier']._serialized_options = b'\xe0A\x03\xfaA-\n+googleads.googleapis.com/AdGroupBidModifier'
    _globals['_CHANGESTATUS'].fields_by_name['shared_set']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['shared_set']._serialized_options = b'\xe0A\x03\xfaA$\n"googleads.googleapis.com/SharedSet'
    _globals['_CHANGESTATUS'].fields_by_name['campaign_shared_set']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['campaign_shared_set']._serialized_options = b'\xe0A\x03\xfaA,\n*googleads.googleapis.com/CampaignSharedSet'
    _globals['_CHANGESTATUS'].fields_by_name['asset']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['asset']._serialized_options = b'\xe0A\x03\xfaA \n\x1egoogleads.googleapis.com/Asset'
    _globals['_CHANGESTATUS'].fields_by_name['customer_asset']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['customer_asset']._serialized_options = b'\xe0A\x03\xfaA(\n&googleads.googleapis.com/CustomerAsset'
    _globals['_CHANGESTATUS'].fields_by_name['campaign_asset']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['campaign_asset']._serialized_options = b'\xe0A\x03\xfaA(\n&googleads.googleapis.com/CampaignAsset'
    _globals['_CHANGESTATUS'].fields_by_name['ad_group_asset']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['ad_group_asset']._serialized_options = b"\xe0A\x03\xfaA'\n%googleads.googleapis.com/AdGroupAsset"
    _globals['_CHANGESTATUS'].fields_by_name['combined_audience']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['combined_audience']._serialized_options = b'\xe0A\x03\xfaA+\n)googleads.googleapis.com/CombinedAudience'
    _globals['_CHANGESTATUS'].fields_by_name['asset_group']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['asset_group']._serialized_options = b'\xe0A\x03\xfaA%\n#googleads.googleapis.com/AssetGroup'
    _globals['_CHANGESTATUS'].fields_by_name['asset_set']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['asset_set']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/AssetSet'
    _globals['_CHANGESTATUS'].fields_by_name['campaign_budget']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['campaign_budget']._serialized_options = b"\xe0A\x03\xfaA)\n'googleads.googleapis.com/CampaignBudget"
    _globals['_CHANGESTATUS'].fields_by_name['campaign_asset_set']._loaded_options = None
    _globals['_CHANGESTATUS'].fields_by_name['campaign_asset_set']._serialized_options = b'\xe0A\x03\xfaA+\n)googleads.googleapis.com/CampaignAssetSet'
    _globals['_CHANGESTATUS']._loaded_options = None
    _globals['_CHANGESTATUS']._serialized_options = b'\xeaA`\n%googleads.googleapis.com/ChangeStatus\x127customers/{customer_id}/changeStatus/{change_status_id}'
    _globals['_CHANGESTATUS']._serialized_start = 283
    _globals['_CHANGESTATUS']._serialized_end = 2108