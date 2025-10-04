"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/asset_set.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.common import asset_set_types_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_asset__set__types__pb2
from ......google.ads.googleads.v21.enums import asset_set_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_asset__set__status__pb2
from ......google.ads.googleads.v21.enums import asset_set_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_asset__set__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/ads/googleads/v21/resources/asset_set.proto\x12"google.ads.googleads.v21.resources\x1a5google/ads/googleads/v21/common/asset_set_types.proto\x1a5google/ads/googleads/v21/enums/asset_set_status.proto\x1a3google/ads/googleads/v21/enums/asset_set_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xdc\x08\n\x08AssetSet\x12\x0f\n\x02id\x18\x06 \x01(\x03B\x03\xe0A\x03\x12@\n\rresource_name\x18\x01 \x01(\tB)\xe0A\x05\xfaA#\n!googleads.googleapis.com/AssetSet\x12\x11\n\x04name\x18\x02 \x01(\tB\x03\xe0A\x02\x12S\n\x04type\x18\x03 \x01(\x0e2=.google.ads.googleads.v21.enums.AssetSetTypeEnum.AssetSetTypeB\x06\xe0A\x02\xe0A\x05\x12V\n\x06status\x18\x04 \x01(\x0e2A.google.ads.googleads.v21.enums.AssetSetStatusEnum.AssetSetStatusB\x03\xe0A\x03\x12]\n\x14merchant_center_feed\x18\x05 \x01(\x0b2?.google.ads.googleads.v21.resources.AssetSet.MerchantCenterFeed\x12/\n"location_group_parent_asset_set_id\x18\n \x01(\x03B\x03\xe0A\x05\x12`\n\x13hotel_property_data\x18\x0b \x01(\x0b2>.google.ads.googleads.v21.resources.AssetSet.HotelPropertyDataB\x03\xe0A\x03\x12D\n\x0clocation_set\x18\x07 \x01(\x0b2,.google.ads.googleads.v21.common.LocationSetH\x00\x12h\n\x1fbusiness_profile_location_group\x18\x08 \x01(\x0b2=.google.ads.googleads.v21.common.BusinessProfileLocationGroupH\x00\x12S\n\x14chain_location_group\x18\t \x01(\x0b23.google.ads.googleads.v21.common.ChainLocationGroupH\x00\x1a[\n\x12MerchantCenterFeed\x12\x18\n\x0bmerchant_id\x18\x01 \x01(\x03B\x03\xe0A\x02\x12\x1c\n\nfeed_label\x18\x02 \x01(\tB\x03\xe0A\x01H\x00\x88\x01\x01B\r\n\x0b_feed_label\x1a{\n\x11HotelPropertyData\x12!\n\x0fhotel_center_id\x18\x01 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1e\n\x0cpartner_name\x18\x02 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01B\x12\n\x10_hotel_center_idB\x0f\n\r_partner_name:X\xeaAU\n!googleads.googleapis.com/AssetSet\x120customers/{customer_id}/assetSets/{asset_set_id}B\x12\n\x10asset_set_sourceB\xff\x01\n&com.google.ads.googleads.v21.resourcesB\rAssetSetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.asset_set_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\rAssetSetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_ASSETSET_MERCHANTCENTERFEED'].fields_by_name['merchant_id']._loaded_options = None
    _globals['_ASSETSET_MERCHANTCENTERFEED'].fields_by_name['merchant_id']._serialized_options = b'\xe0A\x02'
    _globals['_ASSETSET_MERCHANTCENTERFEED'].fields_by_name['feed_label']._loaded_options = None
    _globals['_ASSETSET_MERCHANTCENTERFEED'].fields_by_name['feed_label']._serialized_options = b'\xe0A\x01'
    _globals['_ASSETSET_HOTELPROPERTYDATA'].fields_by_name['hotel_center_id']._loaded_options = None
    _globals['_ASSETSET_HOTELPROPERTYDATA'].fields_by_name['hotel_center_id']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETSET_HOTELPROPERTYDATA'].fields_by_name['partner_name']._loaded_options = None
    _globals['_ASSETSET_HOTELPROPERTYDATA'].fields_by_name['partner_name']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETSET'].fields_by_name['id']._loaded_options = None
    _globals['_ASSETSET'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETSET'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ASSETSET'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA#\n!googleads.googleapis.com/AssetSet'
    _globals['_ASSETSET'].fields_by_name['name']._loaded_options = None
    _globals['_ASSETSET'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_ASSETSET'].fields_by_name['type']._loaded_options = None
    _globals['_ASSETSET'].fields_by_name['type']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_ASSETSET'].fields_by_name['status']._loaded_options = None
    _globals['_ASSETSET'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETSET'].fields_by_name['location_group_parent_asset_set_id']._loaded_options = None
    _globals['_ASSETSET'].fields_by_name['location_group_parent_asset_set_id']._serialized_options = b'\xe0A\x05'
    _globals['_ASSETSET'].fields_by_name['hotel_property_data']._loaded_options = None
    _globals['_ASSETSET'].fields_by_name['hotel_property_data']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETSET']._loaded_options = None
    _globals['_ASSETSET']._serialized_options = b'\xeaAU\n!googleads.googleapis.com/AssetSet\x120customers/{customer_id}/assetSets/{asset_set_id}'
    _globals['_ASSETSET']._serialized_start = 314
    _globals['_ASSETSET']._serialized_end = 1430
    _globals['_ASSETSET_MERCHANTCENTERFEED']._serialized_start = 1104
    _globals['_ASSETSET_MERCHANTCENTERFEED']._serialized_end = 1195
    _globals['_ASSETSET_HOTELPROPERTYDATA']._serialized_start = 1197
    _globals['_ASSETSET_HOTELPROPERTYDATA']._serialized_end = 1320