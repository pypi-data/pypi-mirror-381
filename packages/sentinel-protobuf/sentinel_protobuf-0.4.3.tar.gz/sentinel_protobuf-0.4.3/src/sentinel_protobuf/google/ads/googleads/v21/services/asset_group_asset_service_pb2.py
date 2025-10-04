"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/services/asset_group_asset_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.resources import asset_group_asset_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_asset__group__asset__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/ads/googleads/v21/services/asset_group_asset_service.proto\x12!google.ads.googleads.v21.services\x1a:google/ads/googleads/v21/resources/asset_group_asset.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\xbf\x01\n\x1dMutateAssetGroupAssetsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12T\n\noperations\x18\x02 \x03(\x0b2;.google.ads.googleads.v21.services.AssetGroupAssetOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08"\xa7\x02\n\x18AssetGroupAssetOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12E\n\x06create\x18\x01 \x01(\x0b23.google.ads.googleads.v21.resources.AssetGroupAssetH\x00\x12E\n\x06update\x18\x02 \x01(\x0b23.google.ads.googleads.v21.resources.AssetGroupAssetH\x00\x12?\n\x06remove\x18\x03 \x01(\tB-\xfaA*\n(googleads.googleapis.com/AssetGroupAssetH\x00B\x0b\n\toperation"\xa4\x01\n\x1eMutateAssetGroupAssetsResponse\x12O\n\x07results\x18\x01 \x03(\x0b2>.google.ads.googleads.v21.services.MutateAssetGroupAssetResult\x121\n\x15partial_failure_error\x18\x02 \x01(\x0b2\x12.google.rpc.Status"c\n\x1bMutateAssetGroupAssetResult\x12D\n\rresource_name\x18\x01 \x01(\tB-\xfaA*\n(googleads.googleapis.com/AssetGroupAsset2\xdb\x02\n\x16AssetGroupAssetService\x12\xf9\x01\n\x16MutateAssetGroupAssets\x12@.google.ads.googleads.v21.services.MutateAssetGroupAssetsRequest\x1aA.google.ads.googleads.v21.services.MutateAssetGroupAssetsResponse"Z\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02;"6/v21/customers/{customer_id=*}/assetGroupAssets:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x87\x02\n%com.google.ads.googleads.v21.servicesB\x1bAssetGroupAssetServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.services.asset_group_asset_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v21.servicesB\x1bAssetGroupAssetServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Services'
    _globals['_MUTATEASSETGROUPASSETSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEASSETGROUPASSETSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEASSETGROUPASSETSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATEASSETGROUPASSETSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_ASSETGROUPASSETOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_ASSETGROUPASSETOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA*\n(googleads.googleapis.com/AssetGroupAsset'
    _globals['_MUTATEASSETGROUPASSETRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEASSETGROUPASSETRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA*\n(googleads.googleapis.com/AssetGroupAsset'
    _globals['_ASSETGROUPASSETSERVICE']._loaded_options = None
    _globals['_ASSETGROUPASSETSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_ASSETGROUPASSETSERVICE'].methods_by_name['MutateAssetGroupAssets']._loaded_options = None
    _globals['_ASSETGROUPASSETSERVICE'].methods_by_name['MutateAssetGroupAssets']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02;"6/v21/customers/{customer_id=*}/assetGroupAssets:mutate:\x01*'
    _globals['_MUTATEASSETGROUPASSETSREQUEST']._serialized_start = 339
    _globals['_MUTATEASSETGROUPASSETSREQUEST']._serialized_end = 530
    _globals['_ASSETGROUPASSETOPERATION']._serialized_start = 533
    _globals['_ASSETGROUPASSETOPERATION']._serialized_end = 828
    _globals['_MUTATEASSETGROUPASSETSRESPONSE']._serialized_start = 831
    _globals['_MUTATEASSETGROUPASSETSRESPONSE']._serialized_end = 995
    _globals['_MUTATEASSETGROUPASSETRESULT']._serialized_start = 997
    _globals['_MUTATEASSETGROUPASSETRESULT']._serialized_end = 1096
    _globals['_ASSETGROUPASSETSERVICE']._serialized_start = 1099
    _globals['_ASSETGROUPASSETSERVICE']._serialized_end = 1446