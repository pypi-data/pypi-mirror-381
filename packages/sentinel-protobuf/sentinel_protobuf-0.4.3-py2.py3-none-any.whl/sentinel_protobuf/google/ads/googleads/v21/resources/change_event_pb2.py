"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/change_event.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import change_client_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_change__client__type__pb2
from ......google.ads.googleads.v21.enums import change_event_resource_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_change__event__resource__type__pb2
from ......google.ads.googleads.v21.enums import resource_change_operation_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_resource__change__operation__pb2
from ......google.ads.googleads.v21.resources import ad_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_ad__pb2
from ......google.ads.googleads.v21.resources import ad_group_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_ad__group__pb2
from ......google.ads.googleads.v21.resources import ad_group_ad_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_ad__group__ad__pb2
from ......google.ads.googleads.v21.resources import ad_group_asset_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_ad__group__asset__pb2
from ......google.ads.googleads.v21.resources import ad_group_bid_modifier_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_ad__group__bid__modifier__pb2
from ......google.ads.googleads.v21.resources import ad_group_criterion_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_ad__group__criterion__pb2
from ......google.ads.googleads.v21.resources import asset_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_asset__pb2
from ......google.ads.googleads.v21.resources import asset_set_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_asset__set__pb2
from ......google.ads.googleads.v21.resources import asset_set_asset_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_asset__set__asset__pb2
from ......google.ads.googleads.v21.resources import campaign_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_campaign__pb2
from ......google.ads.googleads.v21.resources import campaign_asset_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_campaign__asset__pb2
from ......google.ads.googleads.v21.resources import campaign_asset_set_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_campaign__asset__set__pb2
from ......google.ads.googleads.v21.resources import campaign_budget_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_campaign__budget__pb2
from ......google.ads.googleads.v21.resources import campaign_criterion_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_campaign__criterion__pb2
from ......google.ads.googleads.v21.resources import customer_asset_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_customer__asset__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/ads/googleads/v21/resources/change_event.proto\x12"google.ads.googleads.v21.resources\x1a7google/ads/googleads/v21/enums/change_client_type.proto\x1a?google/ads/googleads/v21/enums/change_event_resource_type.proto\x1a>google/ads/googleads/v21/enums/resource_change_operation.proto\x1a+google/ads/googleads/v21/resources/ad.proto\x1a1google/ads/googleads/v21/resources/ad_group.proto\x1a4google/ads/googleads/v21/resources/ad_group_ad.proto\x1a7google/ads/googleads/v21/resources/ad_group_asset.proto\x1a>google/ads/googleads/v21/resources/ad_group_bid_modifier.proto\x1a;google/ads/googleads/v21/resources/ad_group_criterion.proto\x1a.google/ads/googleads/v21/resources/asset.proto\x1a2google/ads/googleads/v21/resources/asset_set.proto\x1a8google/ads/googleads/v21/resources/asset_set_asset.proto\x1a1google/ads/googleads/v21/resources/campaign.proto\x1a7google/ads/googleads/v21/resources/campaign_asset.proto\x1a;google/ads/googleads/v21/resources/campaign_asset_set.proto\x1a8google/ads/googleads/v21/resources/campaign_budget.proto\x1a;google/ads/googleads/v21/resources/campaign_criterion.proto\x1a7google/ads/googleads/v21/resources/customer_asset.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xc0\x11\n\x0bChangeEvent\x12C\n\rresource_name\x18\x01 \x01(\tB,\xe0A\x03\xfaA&\n$googleads.googleapis.com/ChangeEvent\x12\x1d\n\x10change_date_time\x18\x02 \x01(\tB\x03\xe0A\x03\x12v\n\x14change_resource_type\x18\x03 \x01(\x0e2S.google.ads.googleads.v21.enums.ChangeEventResourceTypeEnum.ChangeEventResourceTypeB\x03\xe0A\x03\x12!\n\x14change_resource_name\x18\x04 \x01(\tB\x03\xe0A\x03\x12_\n\x0bclient_type\x18\x05 \x01(\x0e2E.google.ads.googleads.v21.enums.ChangeClientTypeEnum.ChangeClientTypeB\x03\xe0A\x03\x12\x17\n\nuser_email\x18\x06 \x01(\tB\x03\xe0A\x03\x12Z\n\x0cold_resource\x18\x07 \x01(\x0b2?.google.ads.googleads.v21.resources.ChangeEvent.ChangedResourceB\x03\xe0A\x03\x12Z\n\x0cnew_resource\x18\x08 \x01(\x0b2?.google.ads.googleads.v21.resources.ChangeEvent.ChangedResourceB\x03\xe0A\x03\x12{\n\x19resource_change_operation\x18\t \x01(\x0e2S.google.ads.googleads.v21.enums.ResourceChangeOperationEnum.ResourceChangeOperationB\x03\xe0A\x03\x127\n\x0echanged_fields\x18\n \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x03\x12;\n\x08campaign\x18\x0b \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign\x12:\n\x08ad_group\x18\x0c \x01(\tB(\xe0A\x03\xfaA"\n googleads.googleapis.com/AdGroup\x125\n\x05asset\x18\x14 \x01(\tB&\xe0A\x03\xfaA \n\x1egoogleads.googleapis.com/Asset\x1a\x95\t\n\x0fChangedResource\x127\n\x02ad\x18\x01 \x01(\x0b2&.google.ads.googleads.v21.resources.AdB\x03\xe0A\x03\x12B\n\x08ad_group\x18\x02 \x01(\x0b2+.google.ads.googleads.v21.resources.AdGroupB\x03\xe0A\x03\x12U\n\x12ad_group_criterion\x18\x03 \x01(\x0b24.google.ads.googleads.v21.resources.AdGroupCriterionB\x03\xe0A\x03\x12C\n\x08campaign\x18\x04 \x01(\x0b2,.google.ads.googleads.v21.resources.CampaignB\x03\xe0A\x03\x12P\n\x0fcampaign_budget\x18\x05 \x01(\x0b22.google.ads.googleads.v21.resources.CampaignBudgetB\x03\xe0A\x03\x12Z\n\x15ad_group_bid_modifier\x18\x06 \x01(\x0b26.google.ads.googleads.v21.resources.AdGroupBidModifierB\x03\xe0A\x03\x12V\n\x12campaign_criterion\x18\x07 \x01(\x0b25.google.ads.googleads.v21.resources.CampaignCriterionB\x03\xe0A\x03\x12G\n\x0bad_group_ad\x18\x0c \x01(\x0b2-.google.ads.googleads.v21.resources.AdGroupAdB\x03\xe0A\x03\x12=\n\x05asset\x18\r \x01(\x0b2).google.ads.googleads.v21.resources.AssetB\x03\xe0A\x03\x12N\n\x0ecustomer_asset\x18\x0e \x01(\x0b21.google.ads.googleads.v21.resources.CustomerAssetB\x03\xe0A\x03\x12N\n\x0ecampaign_asset\x18\x0f \x01(\x0b21.google.ads.googleads.v21.resources.CampaignAssetB\x03\xe0A\x03\x12M\n\x0ead_group_asset\x18\x10 \x01(\x0b20.google.ads.googleads.v21.resources.AdGroupAssetB\x03\xe0A\x03\x12D\n\tasset_set\x18\x11 \x01(\x0b2,.google.ads.googleads.v21.resources.AssetSetB\x03\xe0A\x03\x12O\n\x0fasset_set_asset\x18\x12 \x01(\x0b21.google.ads.googleads.v21.resources.AssetSetAssetB\x03\xe0A\x03\x12U\n\x12campaign_asset_set\x18\x13 \x01(\x0b24.google.ads.googleads.v21.resources.CampaignAssetSetB\x03\xe0A\x03:\x81\x01\xeaA~\n$googleads.googleapis.com/ChangeEvent\x12Vcustomers/{customer_id}/changeEvents/{timestamp_micros}~{command_index}~{mutate_index}B\x82\x02\n&com.google.ads.googleads.v21.resourcesB\x10ChangeEventProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.change_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\x10ChangeEventProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['ad']._loaded_options = None
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['ad']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['ad_group']._loaded_options = None
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['ad_group']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['ad_group_criterion']._loaded_options = None
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['ad_group_criterion']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['campaign']._loaded_options = None
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['campaign']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['campaign_budget']._loaded_options = None
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['campaign_budget']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['ad_group_bid_modifier']._loaded_options = None
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['ad_group_bid_modifier']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['campaign_criterion']._loaded_options = None
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['campaign_criterion']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['ad_group_ad']._loaded_options = None
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['ad_group_ad']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['asset']._loaded_options = None
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['asset']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['customer_asset']._loaded_options = None
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['customer_asset']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['campaign_asset']._loaded_options = None
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['campaign_asset']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['ad_group_asset']._loaded_options = None
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['ad_group_asset']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['asset_set']._loaded_options = None
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['asset_set']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['asset_set_asset']._loaded_options = None
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['asset_set_asset']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['campaign_asset_set']._loaded_options = None
    _globals['_CHANGEEVENT_CHANGEDRESOURCE'].fields_by_name['campaign_asset_set']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CHANGEEVENT'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA&\n$googleads.googleapis.com/ChangeEvent'
    _globals['_CHANGEEVENT'].fields_by_name['change_date_time']._loaded_options = None
    _globals['_CHANGEEVENT'].fields_by_name['change_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT'].fields_by_name['change_resource_type']._loaded_options = None
    _globals['_CHANGEEVENT'].fields_by_name['change_resource_type']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT'].fields_by_name['change_resource_name']._loaded_options = None
    _globals['_CHANGEEVENT'].fields_by_name['change_resource_name']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT'].fields_by_name['client_type']._loaded_options = None
    _globals['_CHANGEEVENT'].fields_by_name['client_type']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT'].fields_by_name['user_email']._loaded_options = None
    _globals['_CHANGEEVENT'].fields_by_name['user_email']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT'].fields_by_name['old_resource']._loaded_options = None
    _globals['_CHANGEEVENT'].fields_by_name['old_resource']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT'].fields_by_name['new_resource']._loaded_options = None
    _globals['_CHANGEEVENT'].fields_by_name['new_resource']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT'].fields_by_name['resource_change_operation']._loaded_options = None
    _globals['_CHANGEEVENT'].fields_by_name['resource_change_operation']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT'].fields_by_name['changed_fields']._loaded_options = None
    _globals['_CHANGEEVENT'].fields_by_name['changed_fields']._serialized_options = b'\xe0A\x03'
    _globals['_CHANGEEVENT'].fields_by_name['campaign']._loaded_options = None
    _globals['_CHANGEEVENT'].fields_by_name['campaign']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_CHANGEEVENT'].fields_by_name['ad_group']._loaded_options = None
    _globals['_CHANGEEVENT'].fields_by_name['ad_group']._serialized_options = b'\xe0A\x03\xfaA"\n googleads.googleapis.com/AdGroup'
    _globals['_CHANGEEVENT'].fields_by_name['asset']._loaded_options = None
    _globals['_CHANGEEVENT'].fields_by_name['asset']._serialized_options = b'\xe0A\x03\xfaA \n\x1egoogleads.googleapis.com/Asset'
    _globals['_CHANGEEVENT']._loaded_options = None
    _globals['_CHANGEEVENT']._serialized_options = b'\xeaA~\n$googleads.googleapis.com/ChangeEvent\x12Vcustomers/{customer_id}/changeEvents/{timestamp_micros}~{command_index}~{mutate_index}'
    _globals['_CHANGEEVENT']._serialized_start = 1209
    _globals['_CHANGEEVENT']._serialized_end = 3449
    _globals['_CHANGEEVENT_CHANGEDRESOURCE']._serialized_start = 2144
    _globals['_CHANGEEVENT_CHANGEDRESOURCE']._serialized_end = 3317