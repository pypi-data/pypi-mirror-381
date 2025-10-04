"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/asset_group_signal.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.common import criteria_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_criteria__pb2
from ......google.ads.googleads.v20.enums import asset_group_signal_approval_status_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__group__signal__approval__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/ads/googleads/v20/resources/asset_group_signal.proto\x12"google.ads.googleads.v20.resources\x1a.google/ads/googleads/v20/common/criteria.proto\x1aGgoogle/ads/googleads/v20/enums/asset_group_signal_approval_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xdd\x04\n\x10AssetGroupSignal\x12H\n\rresource_name\x18\x01 \x01(\tB1\xe0A\x05\xfaA+\n)googleads.googleapis.com/AssetGroupSignal\x12@\n\x0basset_group\x18\x02 \x01(\tB+\xe0A\x05\xfaA%\n#googleads.googleapis.com/AssetGroup\x12\x7f\n\x0fapproval_status\x18\x06 \x01(\x0e2a.google.ads.googleads.v20.enums.AssetGroupSignalApprovalStatusEnum.AssetGroupSignalApprovalStatusB\x03\xe0A\x03\x12 \n\x13disapproval_reasons\x18\x07 \x03(\tB\x03\xe0A\x03\x12F\n\x08audience\x18\x04 \x01(\x0b2-.google.ads.googleads.v20.common.AudienceInfoB\x03\xe0A\x05H\x00\x12M\n\x0csearch_theme\x18\x05 \x01(\x0b20.google.ads.googleads.v20.common.SearchThemeInfoB\x03\xe0A\x05H\x00:y\xeaAv\n)googleads.googleapis.com/AssetGroupSignal\x12Icustomers/{customer_id}/assetGroupSignals/{asset_group_id}~{criterion_id}B\x08\n\x06signalB\x87\x02\n&com.google.ads.googleads.v20.resourcesB\x15AssetGroupSignalProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.asset_group_signal_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x15AssetGroupSignalProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_ASSETGROUPSIGNAL'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ASSETGROUPSIGNAL'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA+\n)googleads.googleapis.com/AssetGroupSignal'
    _globals['_ASSETGROUPSIGNAL'].fields_by_name['asset_group']._loaded_options = None
    _globals['_ASSETGROUPSIGNAL'].fields_by_name['asset_group']._serialized_options = b'\xe0A\x05\xfaA%\n#googleads.googleapis.com/AssetGroup'
    _globals['_ASSETGROUPSIGNAL'].fields_by_name['approval_status']._loaded_options = None
    _globals['_ASSETGROUPSIGNAL'].fields_by_name['approval_status']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUPSIGNAL'].fields_by_name['disapproval_reasons']._loaded_options = None
    _globals['_ASSETGROUPSIGNAL'].fields_by_name['disapproval_reasons']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETGROUPSIGNAL'].fields_by_name['audience']._loaded_options = None
    _globals['_ASSETGROUPSIGNAL'].fields_by_name['audience']._serialized_options = b'\xe0A\x05'
    _globals['_ASSETGROUPSIGNAL'].fields_by_name['search_theme']._loaded_options = None
    _globals['_ASSETGROUPSIGNAL'].fields_by_name['search_theme']._serialized_options = b'\xe0A\x05'
    _globals['_ASSETGROUPSIGNAL']._loaded_options = None
    _globals['_ASSETGROUPSIGNAL']._serialized_options = b'\xeaAv\n)googleads.googleapis.com/AssetGroupSignal\x12Icustomers/{customer_id}/assetGroupSignals/{asset_group_id}~{criterion_id}'
    _globals['_ASSETGROUPSIGNAL']._serialized_start = 281
    _globals['_ASSETGROUPSIGNAL']._serialized_end = 886