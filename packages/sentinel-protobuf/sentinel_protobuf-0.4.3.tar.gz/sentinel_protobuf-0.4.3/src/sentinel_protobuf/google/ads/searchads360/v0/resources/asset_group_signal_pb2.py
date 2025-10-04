"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/asset_group_signal.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.common import criteria_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_common_dot_criteria__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/ads/searchads360/v0/resources/asset_group_signal.proto\x12$google.ads.searchads360.v0.resources\x1a0google/ads/searchads360/v0/common/criteria.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xf6\x02\n\x10AssetGroupSignal\x12K\n\rresource_name\x18\x01 \x01(\tB4\xe0A\x05\xfaA.\n,searchads360.googleapis.com/AssetGroupSignal\x12C\n\x0basset_group\x18\x02 \x01(\tB.\xe0A\x05\xfaA(\n&searchads360.googleapis.com/AssetGroup\x12H\n\x08audience\x18\x04 \x01(\x0b2/.google.ads.searchads360.v0.common.AudienceInfoB\x03\xe0A\x05H\x00:|\xeaAy\n,searchads360.googleapis.com/AssetGroupSignal\x12Icustomers/{customer_id}/assetGroupSignals/{asset_group_id}~{criterion_id}B\x08\n\x06signalB\x95\x02\n(com.google.ads.searchads360.v0.resourcesB\x15AssetGroupSignalProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.asset_group_signal_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x15AssetGroupSignalProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_ASSETGROUPSIGNAL'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ASSETGROUPSIGNAL'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA.\n,searchads360.googleapis.com/AssetGroupSignal'
    _globals['_ASSETGROUPSIGNAL'].fields_by_name['asset_group']._loaded_options = None
    _globals['_ASSETGROUPSIGNAL'].fields_by_name['asset_group']._serialized_options = b'\xe0A\x05\xfaA(\n&searchads360.googleapis.com/AssetGroup'
    _globals['_ASSETGROUPSIGNAL'].fields_by_name['audience']._loaded_options = None
    _globals['_ASSETGROUPSIGNAL'].fields_by_name['audience']._serialized_options = b'\xe0A\x05'
    _globals['_ASSETGROUPSIGNAL']._loaded_options = None
    _globals['_ASSETGROUPSIGNAL']._serialized_options = b'\xeaAy\n,searchads360.googleapis.com/AssetGroupSignal\x12Icustomers/{customer_id}/assetGroupSignals/{asset_group_id}~{criterion_id}'
    _globals['_ASSETGROUPSIGNAL']._serialized_start = 214
    _globals['_ASSETGROUPSIGNAL']._serialized_end = 588