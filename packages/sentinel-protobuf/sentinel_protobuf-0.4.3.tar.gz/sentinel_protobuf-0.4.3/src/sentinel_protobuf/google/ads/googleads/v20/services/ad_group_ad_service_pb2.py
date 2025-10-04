"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/services/ad_group_ad_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.common import policy_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_policy__pb2
from ......google.ads.googleads.v20.enums import asset_field_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__field__type__pb2
from ......google.ads.googleads.v20.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v20.resources import ad_group_ad_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_resources_dot_ad__group__ad__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/ads/googleads/v20/services/ad_group_ad_service.proto\x12!google.ads.googleads.v20.services\x1a,google/ads/googleads/v20/common/policy.proto\x1a5google/ads/googleads/v20/enums/asset_field_type.proto\x1a:google/ads/googleads/v20/enums/response_content_type.proto\x1a4google/ads/googleads/v20/resources/ad_group_ad.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\x9f\x02\n\x17MutateAdGroupAdsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12N\n\noperations\x18\x02 \x03(\x0b25.google.ads.googleads.v20.services.AdGroupAdOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v20.enums.ResponseContentTypeEnum.ResponseContentType"\xf0\x02\n\x12AdGroupAdOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12_\n\x1bpolicy_validation_parameter\x18\x05 \x01(\x0b2:.google.ads.googleads.v20.common.PolicyValidationParameter\x12?\n\x06create\x18\x01 \x01(\x0b2-.google.ads.googleads.v20.resources.AdGroupAdH\x00\x12?\n\x06update\x18\x02 \x01(\x0b2-.google.ads.googleads.v20.resources.AdGroupAdH\x00\x129\n\x06remove\x18\x03 \x01(\tB\'\xfaA$\n"googleads.googleapis.com/AdGroupAdH\x00B\x0b\n\toperation"\x98\x01\n\x18MutateAdGroupAdsResponse\x121\n\x15partial_failure_error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12I\n\x07results\x18\x02 \x03(\x0b28.google.ads.googleads.v20.services.MutateAdGroupAdResult"\x9b\x01\n\x15MutateAdGroupAdResult\x12>\n\rresource_name\x18\x01 \x01(\tB\'\xfaA$\n"googleads.googleapis.com/AdGroupAd\x12B\n\x0bad_group_ad\x18\x02 \x01(\x0b2-.google.ads.googleads.v20.resources.AdGroupAd"\xc7\x01\n\'RemoveAutomaticallyCreatedAssetsRequest\x12?\n\x0bad_group_ad\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"googleads.googleapis.com/AdGroupAd\x12[\n\x16assets_with_field_type\x18\x02 \x03(\x0b26.google.ads.googleads.v20.services.AssetsWithFieldTypeB\x03\xe0A\x02"\xae\x01\n\x13AssetsWithFieldType\x125\n\x05asset\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1egoogleads.googleapis.com/Asset\x12`\n\x10asset_field_type\x18\x02 \x01(\x0e2A.google.ads.googleads.v20.enums.AssetFieldTypeEnum.AssetFieldTypeB\x03\xe0A\x022\xc4\x04\n\x10AdGroupAdService\x12\xe1\x01\n\x10MutateAdGroupAds\x12:.google.ads.googleads.v20.services.MutateAdGroupAdsRequest\x1a;.google.ads.googleads.v20.services.MutateAdGroupAdsResponse"T\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x025"0/v20/customers/{customer_id=*}/adGroupAds:mutate:\x01*\x12\x84\x02\n RemoveAutomaticallyCreatedAssets\x12J.google.ads.googleads.v20.services.RemoveAutomaticallyCreatedAssetsRequest\x1a\x16.google.protobuf.Empty"|\xdaA"ad_group_ad,assets_with_field_type\x82\xd3\xe4\x93\x02Q"L/v20/{ad_group_ad=customers/*/adGroupAds/*}:removeAutomaticallyCreatedAssets:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x81\x02\n%com.google.ads.googleads.v20.servicesB\x15AdGroupAdServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.services.ad_group_ad_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v20.servicesB\x15AdGroupAdServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Services'
    _globals['_MUTATEADGROUPADSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEADGROUPADSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEADGROUPADSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATEADGROUPADSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_ADGROUPADOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_ADGROUPADOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA$\n"googleads.googleapis.com/AdGroupAd'
    _globals['_MUTATEADGROUPADRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEADGROUPADRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA$\n"googleads.googleapis.com/AdGroupAd'
    _globals['_REMOVEAUTOMATICALLYCREATEDASSETSREQUEST'].fields_by_name['ad_group_ad']._loaded_options = None
    _globals['_REMOVEAUTOMATICALLYCREATEDASSETSREQUEST'].fields_by_name['ad_group_ad']._serialized_options = b'\xe0A\x02\xfaA$\n"googleads.googleapis.com/AdGroupAd'
    _globals['_REMOVEAUTOMATICALLYCREATEDASSETSREQUEST'].fields_by_name['assets_with_field_type']._loaded_options = None
    _globals['_REMOVEAUTOMATICALLYCREATEDASSETSREQUEST'].fields_by_name['assets_with_field_type']._serialized_options = b'\xe0A\x02'
    _globals['_ASSETSWITHFIELDTYPE'].fields_by_name['asset']._loaded_options = None
    _globals['_ASSETSWITHFIELDTYPE'].fields_by_name['asset']._serialized_options = b'\xe0A\x02\xfaA \n\x1egoogleads.googleapis.com/Asset'
    _globals['_ASSETSWITHFIELDTYPE'].fields_by_name['asset_field_type']._loaded_options = None
    _globals['_ASSETSWITHFIELDTYPE'].fields_by_name['asset_field_type']._serialized_options = b'\xe0A\x02'
    _globals['_ADGROUPADSERVICE']._loaded_options = None
    _globals['_ADGROUPADSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_ADGROUPADSERVICE'].methods_by_name['MutateAdGroupAds']._loaded_options = None
    _globals['_ADGROUPADSERVICE'].methods_by_name['MutateAdGroupAds']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x025"0/v20/customers/{customer_id=*}/adGroupAds:mutate:\x01*'
    _globals['_ADGROUPADSERVICE'].methods_by_name['RemoveAutomaticallyCreatedAssets']._loaded_options = None
    _globals['_ADGROUPADSERVICE'].methods_by_name['RemoveAutomaticallyCreatedAssets']._serialized_options = b'\xdaA"ad_group_ad,assets_with_field_type\x82\xd3\xe4\x93\x02Q"L/v20/{ad_group_ad=customers/*/adGroupAds/*}:removeAutomaticallyCreatedAssets:\x01*'
    _globals['_MUTATEADGROUPADSREQUEST']._serialized_start = 517
    _globals['_MUTATEADGROUPADSREQUEST']._serialized_end = 804
    _globals['_ADGROUPADOPERATION']._serialized_start = 807
    _globals['_ADGROUPADOPERATION']._serialized_end = 1175
    _globals['_MUTATEADGROUPADSRESPONSE']._serialized_start = 1178
    _globals['_MUTATEADGROUPADSRESPONSE']._serialized_end = 1330
    _globals['_MUTATEADGROUPADRESULT']._serialized_start = 1333
    _globals['_MUTATEADGROUPADRESULT']._serialized_end = 1488
    _globals['_REMOVEAUTOMATICALLYCREATEDASSETSREQUEST']._serialized_start = 1491
    _globals['_REMOVEAUTOMATICALLYCREATEDASSETSREQUEST']._serialized_end = 1690
    _globals['_ASSETSWITHFIELDTYPE']._serialized_start = 1693
    _globals['_ASSETSWITHFIELDTYPE']._serialized_end = 1867
    _globals['_ADGROUPADSERVICE']._serialized_start = 1870
    _globals['_ADGROUPADSERVICE']._serialized_end = 2450