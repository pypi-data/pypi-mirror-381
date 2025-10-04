"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/ad_group_asset_set.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import asset_set_link_status_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__set__link__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/ads/googleads/v20/resources/ad_group_asset_set.proto\x12"google.ads.googleads.v20.resources\x1a:google/ads/googleads/v20/enums/asset_set_link_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xaa\x03\n\x0fAdGroupAssetSet\x12G\n\rresource_name\x18\x01 \x01(\tB0\xe0A\x05\xfaA*\n(googleads.googleapis.com/AdGroupAssetSet\x12:\n\x08ad_group\x18\x02 \x01(\tB(\xe0A\x05\xfaA"\n googleads.googleapis.com/AdGroup\x12<\n\tasset_set\x18\x03 \x01(\tB)\xe0A\x05\xfaA#\n!googleads.googleapis.com/AssetSet\x12^\n\x06status\x18\x04 \x01(\x0e2I.google.ads.googleads.v20.enums.AssetSetLinkStatusEnum.AssetSetLinkStatusB\x03\xe0A\x03:t\xeaAq\n(googleads.googleapis.com/AdGroupAssetSet\x12Ecustomers/{customer_id}/adGroupAssetSets/{ad_group_id}~{asset_set_id}B\x86\x02\n&com.google.ads.googleads.v20.resourcesB\x14AdGroupAssetSetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.ad_group_asset_set_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x14AdGroupAssetSetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_ADGROUPASSETSET'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADGROUPASSETSET'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA*\n(googleads.googleapis.com/AdGroupAssetSet'
    _globals['_ADGROUPASSETSET'].fields_by_name['ad_group']._loaded_options = None
    _globals['_ADGROUPASSETSET'].fields_by_name['ad_group']._serialized_options = b'\xe0A\x05\xfaA"\n googleads.googleapis.com/AdGroup'
    _globals['_ADGROUPASSETSET'].fields_by_name['asset_set']._loaded_options = None
    _globals['_ADGROUPASSETSET'].fields_by_name['asset_set']._serialized_options = b'\xe0A\x05\xfaA#\n!googleads.googleapis.com/AssetSet'
    _globals['_ADGROUPASSETSET'].fields_by_name['status']._loaded_options = None
    _globals['_ADGROUPASSETSET'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPASSETSET']._loaded_options = None
    _globals['_ADGROUPASSETSET']._serialized_options = b'\xeaAq\n(googleads.googleapis.com/AdGroupAssetSet\x12Ecustomers/{customer_id}/adGroupAssetSets/{ad_group_id}~{asset_set_id}'
    _globals['_ADGROUPASSETSET']._serialized_start = 220
    _globals['_ADGROUPASSETSET']._serialized_end = 646