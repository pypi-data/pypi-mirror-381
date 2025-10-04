"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/ad_group_ad_asset_combination_view.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.common import asset_usage_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_asset__usage__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nKgoogle/ads/googleads/v20/resources/ad_group_ad_asset_combination_view.proto\x12"google.ads.googleads.v20.resources\x1a1google/ads/googleads/v20/common/asset_usage.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xab\x03\n\x1dAdGroupAdAssetCombinationView\x12U\n\rresource_name\x18\x01 \x01(\tB>\xe0A\x03\xfaA8\n6googleads.googleapis.com/AdGroupAdAssetCombinationView\x12G\n\rserved_assets\x18\x02 \x03(\x0b2+.google.ads.googleads.v20.common.AssetUsageB\x03\xe0A\x03\x12\x19\n\x07enabled\x18\x03 \x01(\x08B\x03\xe0A\x03H\x00\x88\x01\x01:\xc2\x01\xeaA\xbe\x01\n6googleads.googleapis.com/AdGroupAdAssetCombinationView\x12\x83\x01customers/{customer_id}/adGroupAdAssetCombinationViews/{ad_group_id}~{ad_id}~{asset_combination_id_low}~{asset_combination_id_high}B\n\n\x08_enabledB\x94\x02\n&com.google.ads.googleads.v20.resourcesB"AdGroupAdAssetCombinationViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.ad_group_ad_asset_combination_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB"AdGroupAdAssetCombinationViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_ADGROUPADASSETCOMBINATIONVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADGROUPADASSETCOMBINATIONVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA8\n6googleads.googleapis.com/AdGroupAdAssetCombinationView'
    _globals['_ADGROUPADASSETCOMBINATIONVIEW'].fields_by_name['served_assets']._loaded_options = None
    _globals['_ADGROUPADASSETCOMBINATIONVIEW'].fields_by_name['served_assets']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPADASSETCOMBINATIONVIEW'].fields_by_name['enabled']._loaded_options = None
    _globals['_ADGROUPADASSETCOMBINATIONVIEW'].fields_by_name['enabled']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPADASSETCOMBINATIONVIEW']._loaded_options = None
    _globals['_ADGROUPADASSETCOMBINATIONVIEW']._serialized_options = b'\xeaA\xbe\x01\n6googleads.googleapis.com/AdGroupAdAssetCombinationView\x12\x83\x01customers/{customer_id}/adGroupAdAssetCombinationViews/{ad_group_id}~{ad_id}~{asset_combination_id_low}~{asset_combination_id_high}'
    _globals['_ADGROUPADASSETCOMBINATIONVIEW']._serialized_start = 227
    _globals['_ADGROUPADASSETCOMBINATIONVIEW']._serialized_end = 654