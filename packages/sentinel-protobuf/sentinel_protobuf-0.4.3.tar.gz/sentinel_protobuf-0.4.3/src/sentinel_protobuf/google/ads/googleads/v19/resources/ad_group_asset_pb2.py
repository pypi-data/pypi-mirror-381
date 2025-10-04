"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/ad_group_asset.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.common import asset_policy_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_asset__policy__pb2
from ......google.ads.googleads.v19.enums import asset_field_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_asset__field__type__pb2
from ......google.ads.googleads.v19.enums import asset_link_primary_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_asset__link__primary__status__pb2
from ......google.ads.googleads.v19.enums import asset_link_primary_status_reason_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_asset__link__primary__status__reason__pb2
from ......google.ads.googleads.v19.enums import asset_link_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_asset__link__status__pb2
from ......google.ads.googleads.v19.enums import asset_source_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_asset__source__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/ads/googleads/v19/resources/ad_group_asset.proto\x12"google.ads.googleads.v19.resources\x1a2google/ads/googleads/v19/common/asset_policy.proto\x1a5google/ads/googleads/v19/enums/asset_field_type.proto\x1a>google/ads/googleads/v19/enums/asset_link_primary_status.proto\x1aEgoogle/ads/googleads/v19/enums/asset_link_primary_status_reason.proto\x1a6google/ads/googleads/v19/enums/asset_link_status.proto\x1a1google/ads/googleads/v19/enums/asset_source.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa6\x07\n\x0cAdGroupAsset\x12D\n\rresource_name\x18\x01 \x01(\tB-\xe0A\x05\xfaA\'\n%googleads.googleapis.com/AdGroupAsset\x12=\n\x08ad_group\x18\x02 \x01(\tB+\xe0A\x02\xe0A\x05\xfaA"\n googleads.googleapis.com/AdGroup\x128\n\x05asset\x18\x03 \x01(\tB)\xe0A\x02\xe0A\x05\xfaA \n\x1egoogleads.googleapis.com/Asset\x12]\n\nfield_type\x18\x04 \x01(\x0e2A.google.ads.googleads.v19.enums.AssetFieldTypeEnum.AssetFieldTypeB\x06\xe0A\x02\xe0A\x05\x12P\n\x06source\x18\x06 \x01(\x0e2;.google.ads.googleads.v19.enums.AssetSourceEnum.AssetSourceB\x03\xe0A\x03\x12S\n\x06status\x18\x05 \x01(\x0e2C.google.ads.googleads.v19.enums.AssetLinkStatusEnum.AssetLinkStatus\x12n\n\x0eprimary_status\x18\x07 \x01(\x0e2Q.google.ads.googleads.v19.enums.AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatusB\x03\xe0A\x03\x12c\n\x16primary_status_details\x18\x08 \x03(\x0b2>.google.ads.googleads.v19.common.AssetLinkPrimaryStatusDetailsB\x03\xe0A\x03\x12\x82\x01\n\x16primary_status_reasons\x18\t \x03(\x0e2].google.ads.googleads.v19.enums.AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReasonB\x03\xe0A\x03:w\xeaAt\n%googleads.googleapis.com/AdGroupAsset\x12Kcustomers/{customer_id}/adGroupAssets/{ad_group_id}~{asset_id}~{field_type}B\x83\x02\n&com.google.ads.googleads.v19.resourcesB\x11AdGroupAssetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.ad_group_asset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x11AdGroupAssetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_ADGROUPASSET'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADGROUPASSET'].fields_by_name['resource_name']._serialized_options = b"\xe0A\x05\xfaA'\n%googleads.googleapis.com/AdGroupAsset"
    _globals['_ADGROUPASSET'].fields_by_name['ad_group']._loaded_options = None
    _globals['_ADGROUPASSET'].fields_by_name['ad_group']._serialized_options = b'\xe0A\x02\xe0A\x05\xfaA"\n googleads.googleapis.com/AdGroup'
    _globals['_ADGROUPASSET'].fields_by_name['asset']._loaded_options = None
    _globals['_ADGROUPASSET'].fields_by_name['asset']._serialized_options = b'\xe0A\x02\xe0A\x05\xfaA \n\x1egoogleads.googleapis.com/Asset'
    _globals['_ADGROUPASSET'].fields_by_name['field_type']._loaded_options = None
    _globals['_ADGROUPASSET'].fields_by_name['field_type']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_ADGROUPASSET'].fields_by_name['source']._loaded_options = None
    _globals['_ADGROUPASSET'].fields_by_name['source']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPASSET'].fields_by_name['primary_status']._loaded_options = None
    _globals['_ADGROUPASSET'].fields_by_name['primary_status']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPASSET'].fields_by_name['primary_status_details']._loaded_options = None
    _globals['_ADGROUPASSET'].fields_by_name['primary_status_details']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPASSET'].fields_by_name['primary_status_reasons']._loaded_options = None
    _globals['_ADGROUPASSET'].fields_by_name['primary_status_reasons']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPASSET']._loaded_options = None
    _globals['_ADGROUPASSET']._serialized_options = b'\xeaAt\n%googleads.googleapis.com/AdGroupAsset\x12Kcustomers/{customer_id}/adGroupAssets/{ad_group_id}~{asset_id}~{field_type}'
    _globals['_ADGROUPASSET']._serialized_start = 505
    _globals['_ADGROUPASSET']._serialized_end = 1439