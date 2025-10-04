"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/asset_group.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import ad_strength_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_ad__strength__pb2
from ......google.ads.googleads.v20.enums import ad_strength_action_item_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_ad__strength__action__item__type__pb2
from ......google.ads.googleads.v20.enums import asset_coverage_video_aspect_ratio_requirement_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__coverage__video__aspect__ratio__requirement__pb2
from ......google.ads.googleads.v20.enums import asset_field_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__field__type__pb2
from ......google.ads.googleads.v20.enums import asset_group_primary_status_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__group__primary__status__pb2
from ......google.ads.googleads.v20.enums import asset_group_primary_status_reason_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__group__primary__status__reason__pb2
from ......google.ads.googleads.v20.enums import asset_group_status_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__group__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/ads/googleads/v20/resources/asset_group.proto\x12"google.ads.googleads.v20.resources\x1a0google/ads/googleads/v20/enums/ad_strength.proto\x1aAgoogle/ads/googleads/v20/enums/ad_strength_action_item_type.proto\x1aRgoogle/ads/googleads/v20/enums/asset_coverage_video_aspect_ratio_requirement.proto\x1a5google/ads/googleads/v20/enums/asset_field_type.proto\x1a?google/ads/googleads/v20/enums/asset_group_primary_status.proto\x1aFgoogle/ads/googleads/v20/enums/asset_group_primary_status_reason.proto\x1a7google/ads/googleads/v20/enums/asset_group_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xec\x06\n\nAssetGroup\x12B\n\rresource_name\x18\x01 \x01(\tB+\xe0A\x05\xfaA%\n#googleads.googleapis.com/AssetGroup\x12\x0f\n\x02id\x18\t \x01(\x03B\x03\xe0A\x03\x12;\n\x08campaign\x18\x02 \x01(\tB)\xe0A\x05\xfaA#\n!googleads.googleapis.com/Campaign\x12\x11\n\x04name\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x12\n\nfinal_urls\x18\x04 \x03(\t\x12\x19\n\x11final_mobile_urls\x18\x05 \x03(\t\x12U\n\x06status\x18\x06 \x01(\x0e2E.google.ads.googleads.v20.enums.AssetGroupStatusEnum.AssetGroupStatus\x12p\n\x0eprimary_status\x18\x0b \x01(\x0e2S.google.ads.googleads.v20.enums.AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatusB\x03\xe0A\x03\x12\x84\x01\n\x16primary_status_reasons\x18\x0c \x03(\x0e2_.google.ads.googleads.v20.enums.AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReasonB\x03\xe0A\x03\x12\r\n\x05path1\x18\x07 \x01(\t\x12\r\n\x05path2\x18\x08 \x01(\t\x12S\n\x0bad_strength\x18\n \x01(\x0e29.google.ads.googleads.v20.enums.AdStrengthEnum.AdStrengthB\x03\xe0A\x03\x12N\n\x0easset_coverage\x18\r \x01(\x0b21.google.ads.googleads.v20.resources.AssetCoverageB\x03\xe0A\x03:w\xeaAt\n#googleads.googleapis.com/AssetGroup\x124customers/{customer_id}/assetGroups/{asset_group_id}*\x0bassetGroups2\nassetGroup"p\n\rAssetCoverage\x12_\n\x18ad_strength_action_items\x18\x01 \x03(\x0b28.google.ads.googleads.v20.resources.AdStrengthActionItemB\x03\xe0A\x03"\xfc\x04\n\x14AdStrengthActionItem\x12t\n\x10action_item_type\x18\x01 \x01(\x0e2U.google.ads.googleads.v20.enums.AdStrengthActionItemTypeEnum.AdStrengthActionItemTypeB\x03\xe0A\x03\x12j\n\x11add_asset_details\x18\x02 \x01(\x0b2H.google.ads.googleads.v20.resources.AdStrengthActionItem.AddAssetDetailsB\x03\xe0A\x03H\x00\x1a\xef\x02\n\x0fAddAssetDetails\x12`\n\x10asset_field_type\x18\x01 \x01(\x0e2A.google.ads.googleads.v20.enums.AssetFieldTypeEnum.AssetFieldTypeB\x03\xe0A\x03\x12\x1d\n\x0basset_count\x18\x02 \x01(\x05B\x03\xe0A\x03H\x00\x88\x01\x01\x12\xa7\x01\n\x1evideo_aspect_ratio_requirement\x18\x03 \x01(\x0e2u.google.ads.googleads.v20.enums.AssetCoverageVideoAspectRatioRequirementEnum.AssetCoverageVideoAspectRatioRequirementB\x03\xe0A\x03H\x01\x88\x01\x01B\x0e\n\x0c_asset_countB!\n\x1f_video_aspect_ratio_requirementB\x10\n\x0eaction_detailsB\x81\x02\n&com.google.ads.googleads.v20.resourcesB\x0fAssetGroupProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.asset_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x0fAssetGroupProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_ASSETGROUP'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ASSETGROUP'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA%\n#googleads.googleapis.com/AssetGroup'
    _globals['_ASSETGROUP'].fields_by_name['id']._loaded_options = None
    _globals['_ASSETGROUP'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUP'].fields_by_name['campaign']._loaded_options = None
    _globals['_ASSETGROUP'].fields_by_name['campaign']._serialized_options = b'\xe0A\x05\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_ASSETGROUP'].fields_by_name['name']._loaded_options = None
    _globals['_ASSETGROUP'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_ASSETGROUP'].fields_by_name['primary_status']._loaded_options = None
    _globals['_ASSETGROUP'].fields_by_name['primary_status']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUP'].fields_by_name['primary_status_reasons']._loaded_options = None
    _globals['_ASSETGROUP'].fields_by_name['primary_status_reasons']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUP'].fields_by_name['ad_strength']._loaded_options = None
    _globals['_ASSETGROUP'].fields_by_name['ad_strength']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUP'].fields_by_name['asset_coverage']._loaded_options = None
    _globals['_ASSETGROUP'].fields_by_name['asset_coverage']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUP']._loaded_options = None
    _globals['_ASSETGROUP']._serialized_options = b'\xeaAt\n#googleads.googleapis.com/AssetGroup\x124customers/{customer_id}/assetGroups/{asset_group_id}*\x0bassetGroups2\nassetGroup'
    _globals['_ASSETCOVERAGE'].fields_by_name['ad_strength_action_items']._loaded_options = None
    _globals['_ASSETCOVERAGE'].fields_by_name['ad_strength_action_items']._serialized_options = b'\xe0A\x03'
    _globals['_ADSTRENGTHACTIONITEM_ADDASSETDETAILS'].fields_by_name['asset_field_type']._loaded_options = None
    _globals['_ADSTRENGTHACTIONITEM_ADDASSETDETAILS'].fields_by_name['asset_field_type']._serialized_options = b'\xe0A\x03'
    _globals['_ADSTRENGTHACTIONITEM_ADDASSETDETAILS'].fields_by_name['asset_count']._loaded_options = None
    _globals['_ADSTRENGTHACTIONITEM_ADDASSETDETAILS'].fields_by_name['asset_count']._serialized_options = b'\xe0A\x03'
    _globals['_ADSTRENGTHACTIONITEM_ADDASSETDETAILS'].fields_by_name['video_aspect_ratio_requirement']._loaded_options = None
    _globals['_ADSTRENGTHACTIONITEM_ADDASSETDETAILS'].fields_by_name['video_aspect_ratio_requirement']._serialized_options = b'\xe0A\x03'
    _globals['_ADSTRENGTHACTIONITEM'].fields_by_name['action_item_type']._loaded_options = None
    _globals['_ADSTRENGTHACTIONITEM'].fields_by_name['action_item_type']._serialized_options = b'\xe0A\x03'
    _globals['_ADSTRENGTHACTIONITEM'].fields_by_name['add_asset_details']._loaded_options = None
    _globals['_ADSTRENGTHACTIONITEM'].fields_by_name['add_asset_details']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUP']._serialized_start = 603
    _globals['_ASSETGROUP']._serialized_end = 1479
    _globals['_ASSETCOVERAGE']._serialized_start = 1481
    _globals['_ASSETCOVERAGE']._serialized_end = 1593
    _globals['_ADSTRENGTHACTIONITEM']._serialized_start = 1596
    _globals['_ADSTRENGTHACTIONITEM']._serialized_end = 2232
    _globals['_ADSTRENGTHACTIONITEM_ADDASSETDETAILS']._serialized_start = 1847
    _globals['_ADSTRENGTHACTIONITEM_ADDASSETDETAILS']._serialized_end = 2214