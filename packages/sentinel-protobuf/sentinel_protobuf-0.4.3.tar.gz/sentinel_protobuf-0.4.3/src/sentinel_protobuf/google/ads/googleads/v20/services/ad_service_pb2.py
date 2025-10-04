"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/services/ad_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.common import policy_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_policy__pb2
from ......google.ads.googleads.v20.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v20.resources import ad_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_resources_dot_ad__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/ads/googleads/v20/services/ad_service.proto\x12!google.ads.googleads.v20.services\x1a,google/ads/googleads/v20/common/policy.proto\x1a:google/ads/googleads/v20/enums/response_content_type.proto\x1a+google/ads/googleads/v20/resources/ad.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\x91\x02\n\x10MutateAdsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12G\n\noperations\x18\x02 \x03(\x0b2..google.ads.googleads.v20.services.AdOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v20.enums.ResponseContentTypeEnum.ResponseContentType\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08"\xe6\x01\n\x0bAdOperation\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12_\n\x1bpolicy_validation_parameter\x18\x03 \x01(\x0b2:.google.ads.googleads.v20.common.PolicyValidationParameter\x128\n\x06update\x18\x01 \x01(\x0b2&.google.ads.googleads.v20.resources.AdH\x00B\x0b\n\toperation"\x8a\x01\n\x11MutateAdsResponse\x121\n\x15partial_failure_error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12B\n\x07results\x18\x02 \x03(\x0b21.google.ads.googleads.v20.services.MutateAdResult"}\n\x0eMutateAdResult\x127\n\rresource_name\x18\x01 \x01(\tB \xfaA\x1d\n\x1bgoogleads.googleapis.com/Ad\x122\n\x02ad\x18\x02 \x01(\x0b2&.google.ads.googleads.v20.resources.Ad2\x9a\x02\n\tAdService\x12\xc5\x01\n\tMutateAds\x123.google.ads.googleads.v20.services.MutateAdsRequest\x1a4.google.ads.googleads.v20.services.MutateAdsResponse"M\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02.")/v20/customers/{customer_id=*}/ads:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\xfa\x01\n%com.google.ads.googleads.v20.servicesB\x0eAdServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.services.ad_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v20.servicesB\x0eAdServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Services'
    _globals['_MUTATEADSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEADSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEADSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATEADSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEADRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEADRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA\x1d\n\x1bgoogleads.googleapis.com/Ad'
    _globals['_ADSERVICE']._loaded_options = None
    _globals['_ADSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_ADSERVICE'].methods_by_name['MutateAds']._loaded_options = None
    _globals['_ADSERVICE'].methods_by_name['MutateAds']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02.")/v20/customers/{customer_id=*}/ads:mutate:\x01*'
    _globals['_MUTATEADSREQUEST']._serialized_start = 415
    _globals['_MUTATEADSREQUEST']._serialized_end = 688
    _globals['_ADOPERATION']._serialized_start = 691
    _globals['_ADOPERATION']._serialized_end = 921
    _globals['_MUTATEADSRESPONSE']._serialized_start = 924
    _globals['_MUTATEADSRESPONSE']._serialized_end = 1062
    _globals['_MUTATEADRESULT']._serialized_start = 1064
    _globals['_MUTATEADRESULT']._serialized_end = 1189
    _globals['_ADSERVICE']._serialized_start = 1192
    _globals['_ADSERVICE']._serialized_end = 1474