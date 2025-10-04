"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/services/ad_group_label_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.resources import ad_group_label_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_resources_dot_ad__group__label__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/ads/googleads/v20/services/ad_group_label_service.proto\x12!google.ads.googleads.v20.services\x1a7google/ads/googleads/v20/resources/ad_group_label.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto"\xb9\x01\n\x1aMutateAdGroupLabelsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12Q\n\noperations\x18\x02 \x03(\x0b28.google.ads.googleads.v20.services.AdGroupLabelOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08"\xa6\x01\n\x15AdGroupLabelOperation\x12B\n\x06create\x18\x01 \x01(\x0b20.google.ads.googleads.v20.resources.AdGroupLabelH\x00\x12<\n\x06remove\x18\x02 \x01(\tB*\xfaA\'\n%googleads.googleapis.com/AdGroupLabelH\x00B\x0b\n\toperation"\x9e\x01\n\x1bMutateAdGroupLabelsResponse\x121\n\x15partial_failure_error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12L\n\x07results\x18\x02 \x03(\x0b2;.google.ads.googleads.v20.services.MutateAdGroupLabelResult"]\n\x18MutateAdGroupLabelResult\x12A\n\rresource_name\x18\x01 \x01(\tB*\xfaA\'\n%googleads.googleapis.com/AdGroupLabel2\xcc\x02\n\x13AdGroupLabelService\x12\xed\x01\n\x13MutateAdGroupLabels\x12=.google.ads.googleads.v20.services.MutateAdGroupLabelsRequest\x1a>.google.ads.googleads.v20.services.MutateAdGroupLabelsResponse"W\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x028"3/v20/customers/{customer_id=*}/adGroupLabels:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x84\x02\n%com.google.ads.googleads.v20.servicesB\x18AdGroupLabelServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.services.ad_group_label_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v20.servicesB\x18AdGroupLabelServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Services'
    _globals['_MUTATEADGROUPLABELSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEADGROUPLABELSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEADGROUPLABELSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATEADGROUPLABELSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_ADGROUPLABELOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_ADGROUPLABELOPERATION'].fields_by_name['remove']._serialized_options = b"\xfaA'\n%googleads.googleapis.com/AdGroupLabel"
    _globals['_MUTATEADGROUPLABELRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEADGROUPLABELRESULT'].fields_by_name['resource_name']._serialized_options = b"\xfaA'\n%googleads.googleapis.com/AdGroupLabel"
    _globals['_ADGROUPLABELSERVICE']._loaded_options = None
    _globals['_ADGROUPLABELSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_ADGROUPLABELSERVICE'].methods_by_name['MutateAdGroupLabels']._loaded_options = None
    _globals['_ADGROUPLABELSERVICE'].methods_by_name['MutateAdGroupLabels']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x028"3/v20/customers/{customer_id=*}/adGroupLabels:mutate:\x01*'
    _globals['_MUTATEADGROUPLABELSREQUEST']._serialized_start = 299
    _globals['_MUTATEADGROUPLABELSREQUEST']._serialized_end = 484
    _globals['_ADGROUPLABELOPERATION']._serialized_start = 487
    _globals['_ADGROUPLABELOPERATION']._serialized_end = 653
    _globals['_MUTATEADGROUPLABELSRESPONSE']._serialized_start = 656
    _globals['_MUTATEADGROUPLABELSRESPONSE']._serialized_end = 814
    _globals['_MUTATEADGROUPLABELRESULT']._serialized_start = 816
    _globals['_MUTATEADGROUPLABELRESULT']._serialized_end = 909
    _globals['_ADGROUPLABELSERVICE']._serialized_start = 912
    _globals['_ADGROUPLABELSERVICE']._serialized_end = 1244