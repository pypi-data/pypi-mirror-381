"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/asset_group_asset.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.common import asset_policy_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_asset__policy__pb2
from ......google.ads.googleads.v20.common import policy_summary_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_policy__summary__pb2
from ......google.ads.googleads.v20.enums import asset_field_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__field__type__pb2
from ......google.ads.googleads.v20.enums import asset_link_primary_status_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__link__primary__status__pb2
from ......google.ads.googleads.v20.enums import asset_link_primary_status_reason_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__link__primary__status__reason__pb2
from ......google.ads.googleads.v20.enums import asset_link_status_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__link__status__pb2
from ......google.ads.googleads.v20.enums import asset_performance_label_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__performance__label__pb2
from ......google.ads.googleads.v20.enums import asset_source_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__source__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/ads/googleads/v20/resources/asset_group_asset.proto\x12"google.ads.googleads.v20.resources\x1a2google/ads/googleads/v20/common/asset_policy.proto\x1a4google/ads/googleads/v20/common/policy_summary.proto\x1a5google/ads/googleads/v20/enums/asset_field_type.proto\x1a>google/ads/googleads/v20/enums/asset_link_primary_status.proto\x1aEgoogle/ads/googleads/v20/enums/asset_link_primary_status_reason.proto\x1a6google/ads/googleads/v20/enums/asset_link_status.proto\x1a<google/ads/googleads/v20/enums/asset_performance_label.proto\x1a1google/ads/googleads/v20/enums/asset_source.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xec\x08\n\x0fAssetGroupAsset\x12G\n\rresource_name\x18\x01 \x01(\tB0\xe0A\x05\xfaA*\n(googleads.googleapis.com/AssetGroupAsset\x12@\n\x0basset_group\x18\x02 \x01(\tB+\xe0A\x05\xfaA%\n#googleads.googleapis.com/AssetGroup\x125\n\x05asset\x18\x03 \x01(\tB&\xe0A\x05\xfaA \n\x1egoogleads.googleapis.com/Asset\x12U\n\nfield_type\x18\x04 \x01(\x0e2A.google.ads.googleads.v20.enums.AssetFieldTypeEnum.AssetFieldType\x12S\n\x06status\x18\x05 \x01(\x0e2C.google.ads.googleads.v20.enums.AssetLinkStatusEnum.AssetLinkStatus\x12n\n\x0eprimary_status\x18\x08 \x01(\x0e2Q.google.ads.googleads.v20.enums.AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatusB\x03\xe0A\x03\x12\x82\x01\n\x16primary_status_reasons\x18\t \x03(\x0e2].google.ads.googleads.v20.enums.AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReasonB\x03\xe0A\x03\x12c\n\x16primary_status_details\x18\n \x03(\x0b2>.google.ads.googleads.v20.common.AssetLinkPrimaryStatusDetailsB\x03\xe0A\x03\x12o\n\x11performance_label\x18\x06 \x01(\x0e2O.google.ads.googleads.v20.enums.AssetPerformanceLabelEnum.AssetPerformanceLabelB\x03\xe0A\x03\x12K\n\x0epolicy_summary\x18\x07 \x01(\x0b2..google.ads.googleads.v20.common.PolicySummaryB\x03\xe0A\x03\x12P\n\x06source\x18\x0b \x01(\x0e2;.google.ads.googleads.v20.enums.AssetSourceEnum.AssetSourceB\x03\xe0A\x03:\x80\x01\xeaA}\n(googleads.googleapis.com/AssetGroupAsset\x12Qcustomers/{customer_id}/assetGroupAssets/{asset_group_id}~{asset_id}~{field_type}B\x86\x02\n&com.google.ads.googleads.v20.resourcesB\x14AssetGroupAssetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.asset_group_asset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x14AssetGroupAssetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_ASSETGROUPASSET'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ASSETGROUPASSET'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA*\n(googleads.googleapis.com/AssetGroupAsset'
    _globals['_ASSETGROUPASSET'].fields_by_name['asset_group']._loaded_options = None
    _globals['_ASSETGROUPASSET'].fields_by_name['asset_group']._serialized_options = b'\xe0A\x05\xfaA%\n#googleads.googleapis.com/AssetGroup'
    _globals['_ASSETGROUPASSET'].fields_by_name['asset']._loaded_options = None
    _globals['_ASSETGROUPASSET'].fields_by_name['asset']._serialized_options = b'\xe0A\x05\xfaA \n\x1egoogleads.googleapis.com/Asset'
    _globals['_ASSETGROUPASSET'].fields_by_name['primary_status']._loaded_options = None
    _globals['_ASSETGROUPASSET'].fields_by_name['primary_status']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUPASSET'].fields_by_name['primary_status_reasons']._loaded_options = None
    _globals['_ASSETGROUPASSET'].fields_by_name['primary_status_reasons']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUPASSET'].fields_by_name['primary_status_details']._loaded_options = None
    _globals['_ASSETGROUPASSET'].fields_by_name['primary_status_details']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUPASSET'].fields_by_name['performance_label']._loaded_options = None
    _globals['_ASSETGROUPASSET'].fields_by_name['performance_label']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUPASSET'].fields_by_name['policy_summary']._loaded_options = None
    _globals['_ASSETGROUPASSET'].fields_by_name['policy_summary']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUPASSET'].fields_by_name['source']._loaded_options = None
    _globals['_ASSETGROUPASSET'].fields_by_name['source']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUPASSET']._loaded_options = None
    _globals['_ASSETGROUPASSET']._serialized_options = b'\xeaA}\n(googleads.googleapis.com/AssetGroupAsset\x12Qcustomers/{customer_id}/assetGroupAssets/{asset_group_id}~{asset_id}~{field_type}'
    _globals['_ASSETGROUPASSET']._serialized_start = 624
    _globals['_ASSETGROUPASSET']._serialized_end = 1756