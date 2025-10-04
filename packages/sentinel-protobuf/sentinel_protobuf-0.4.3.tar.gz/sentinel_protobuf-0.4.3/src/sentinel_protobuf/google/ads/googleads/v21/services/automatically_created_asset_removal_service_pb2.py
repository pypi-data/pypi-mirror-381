"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/services/automatically_created_asset_removal_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import asset_field_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_asset__field__type__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nSgoogle/ads/googleads/v21/services/automatically_created_asset_removal_service.proto\x12!google.ads.googleads.v21.services\x1a5google/ads/googleads/v21/enums/asset_field_type.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x17google/rpc/status.proto"\xd6\x01\n.RemoveCampaignAutomaticallyCreatedAssetRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12l\n\noperations\x18\x02 \x03(\x0b2S.google.ads.googleads.v21.services.RemoveCampaignAutomaticallyCreatedAssetOperationB\x03\xe0A\x02\x12\x1c\n\x0fpartial_failure\x18\x03 \x01(\x08B\x03\xe0A\x02"\xb9\x01\n0RemoveCampaignAutomaticallyCreatedAssetOperation\x12\x15\n\x08campaign\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05asset\x18\x02 \x01(\tB\x03\xe0A\x02\x12Z\n\nfield_type\x18\x03 \x01(\x0e2A.google.ads.googleads.v21.enums.AssetFieldTypeEnum.AssetFieldTypeB\x03\xe0A\x02"d\n/RemoveCampaignAutomaticallyCreatedAssetResponse\x121\n\x15partial_failure_error\x18\x01 \x01(\x0b2\x12.google.rpc.Status2\xbf\x03\n\'AutomaticallyCreatedAssetRemovalService\x12\xcc\x02\n\'RemoveCampaignAutomaticallyCreatedAsset\x12Q.google.ads.googleads.v21.services.RemoveCampaignAutomaticallyCreatedAssetRequest\x1aR.google.ads.googleads.v21.services.RemoveCampaignAutomaticallyCreatedAssetResponse"z\xdaA&customer_id,operations,partial_failure\x82\xd3\xe4\x93\x02K"F/v21/customers/{customer_id=*}:removeCampaignAutomaticallyCreatedAsset:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x98\x02\n%com.google.ads.googleads.v21.servicesB,AutomaticallyCreatedAssetRemovalServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.services.automatically_created_asset_removal_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v21.servicesB,AutomaticallyCreatedAssetRemovalServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Services'
    _globals['_REMOVECAMPAIGNAUTOMATICALLYCREATEDASSETREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_REMOVECAMPAIGNAUTOMATICALLYCREATEDASSETREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVECAMPAIGNAUTOMATICALLYCREATEDASSETREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_REMOVECAMPAIGNAUTOMATICALLYCREATEDASSETREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVECAMPAIGNAUTOMATICALLYCREATEDASSETREQUEST'].fields_by_name['partial_failure']._loaded_options = None
    _globals['_REMOVECAMPAIGNAUTOMATICALLYCREATEDASSETREQUEST'].fields_by_name['partial_failure']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVECAMPAIGNAUTOMATICALLYCREATEDASSETOPERATION'].fields_by_name['campaign']._loaded_options = None
    _globals['_REMOVECAMPAIGNAUTOMATICALLYCREATEDASSETOPERATION'].fields_by_name['campaign']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVECAMPAIGNAUTOMATICALLYCREATEDASSETOPERATION'].fields_by_name['asset']._loaded_options = None
    _globals['_REMOVECAMPAIGNAUTOMATICALLYCREATEDASSETOPERATION'].fields_by_name['asset']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVECAMPAIGNAUTOMATICALLYCREATEDASSETOPERATION'].fields_by_name['field_type']._loaded_options = None
    _globals['_REMOVECAMPAIGNAUTOMATICALLYCREATEDASSETOPERATION'].fields_by_name['field_type']._serialized_options = b'\xe0A\x02'
    _globals['_AUTOMATICALLYCREATEDASSETREMOVALSERVICE']._loaded_options = None
    _globals['_AUTOMATICALLYCREATEDASSETREMOVALSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_AUTOMATICALLYCREATEDASSETREMOVALSERVICE'].methods_by_name['RemoveCampaignAutomaticallyCreatedAsset']._loaded_options = None
    _globals['_AUTOMATICALLYCREATEDASSETREMOVALSERVICE'].methods_by_name['RemoveCampaignAutomaticallyCreatedAsset']._serialized_options = b'\xdaA&customer_id,operations,partial_failure\x82\xd3\xe4\x93\x02K"F/v21/customers/{customer_id=*}:removeCampaignAutomaticallyCreatedAsset:\x01*'
    _globals['_REMOVECAMPAIGNAUTOMATICALLYCREATEDASSETREQUEST']._serialized_start = 291
    _globals['_REMOVECAMPAIGNAUTOMATICALLYCREATEDASSETREQUEST']._serialized_end = 505
    _globals['_REMOVECAMPAIGNAUTOMATICALLYCREATEDASSETOPERATION']._serialized_start = 508
    _globals['_REMOVECAMPAIGNAUTOMATICALLYCREATEDASSETOPERATION']._serialized_end = 693
    _globals['_REMOVECAMPAIGNAUTOMATICALLYCREATEDASSETRESPONSE']._serialized_start = 695
    _globals['_REMOVECAMPAIGNAUTOMATICALLYCREATEDASSETRESPONSE']._serialized_end = 795
    _globals['_AUTOMATICALLYCREATEDASSETREMOVALSERVICE']._serialized_start = 798
    _globals['_AUTOMATICALLYCREATEDASSETREMOVALSERVICE']._serialized_end = 1245