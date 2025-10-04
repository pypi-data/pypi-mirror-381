"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/services/customer_negative_criterion_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v19.resources import customer_negative_criterion_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_resources_dot_customer__negative__criterion__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nKgoogle/ads/googleads/v19/services/customer_negative_criterion_service.proto\x12!google.ads.googleads.v19.services\x1a:google/ads/googleads/v19/enums/response_content_type.proto\x1aDgoogle/ads/googleads/v19/resources/customer_negative_criterion.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto"\xbd\x02\n%MutateCustomerNegativeCriteriaRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12^\n\noperations\x18\x02 \x03(\x0b2E.google.ads.googleads.v19.services.CustomerNegativeCriterionOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v19.enums.ResponseContentTypeEnum.ResponseContentType"\xcd\x01\n"CustomerNegativeCriterionOperation\x12O\n\x06create\x18\x01 \x01(\x0b2=.google.ads.googleads.v19.resources.CustomerNegativeCriterionH\x00\x12I\n\x06remove\x18\x02 \x01(\tB7\xfaA4\n2googleads.googleapis.com/CustomerNegativeCriterionH\x00B\x0b\n\toperation"\xb5\x01\n&MutateCustomerNegativeCriteriaResponse\x121\n\x15partial_failure_error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12X\n\x07results\x18\x02 \x03(\x0b2G.google.ads.googleads.v19.services.MutateCustomerNegativeCriteriaResult"\xda\x01\n$MutateCustomerNegativeCriteriaResult\x12N\n\rresource_name\x18\x01 \x01(\tB7\xfaA4\n2googleads.googleapis.com/CustomerNegativeCriterion\x12b\n\x1bcustomer_negative_criterion\x18\x02 \x01(\x0b2=.google.ads.googleads.v19.resources.CustomerNegativeCriterion2\x85\x03\n CustomerNegativeCriterionService\x12\x99\x02\n\x1eMutateCustomerNegativeCriteria\x12H.google.ads.googleads.v19.services.MutateCustomerNegativeCriteriaRequest\x1aI.google.ads.googleads.v19.services.MutateCustomerNegativeCriteriaResponse"b\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02C">/v19/customers/{customer_id=*}/customerNegativeCriteria:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x91\x02\n%com.google.ads.googleads.v19.servicesB%CustomerNegativeCriterionServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.services.customer_negative_criterion_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v19.servicesB%CustomerNegativeCriterionServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Services'
    _globals['_MUTATECUSTOMERNEGATIVECRITERIAREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECUSTOMERNEGATIVECRITERIAREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECUSTOMERNEGATIVECRITERIAREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATECUSTOMERNEGATIVECRITERIAREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMERNEGATIVECRITERIONOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_CUSTOMERNEGATIVECRITERIONOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA4\n2googleads.googleapis.com/CustomerNegativeCriterion'
    _globals['_MUTATECUSTOMERNEGATIVECRITERIARESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECUSTOMERNEGATIVECRITERIARESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA4\n2googleads.googleapis.com/CustomerNegativeCriterion'
    _globals['_CUSTOMERNEGATIVECRITERIONSERVICE']._loaded_options = None
    _globals['_CUSTOMERNEGATIVECRITERIONSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CUSTOMERNEGATIVECRITERIONSERVICE'].methods_by_name['MutateCustomerNegativeCriteria']._loaded_options = None
    _globals['_CUSTOMERNEGATIVECRITERIONSERVICE'].methods_by_name['MutateCustomerNegativeCriteria']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02C">/v19/customers/{customer_id=*}/customerNegativeCriteria:mutate:\x01*'
    _globals['_MUTATECUSTOMERNEGATIVECRITERIAREQUEST']._serialized_start = 385
    _globals['_MUTATECUSTOMERNEGATIVECRITERIAREQUEST']._serialized_end = 702
    _globals['_CUSTOMERNEGATIVECRITERIONOPERATION']._serialized_start = 705
    _globals['_CUSTOMERNEGATIVECRITERIONOPERATION']._serialized_end = 910
    _globals['_MUTATECUSTOMERNEGATIVECRITERIARESPONSE']._serialized_start = 913
    _globals['_MUTATECUSTOMERNEGATIVECRITERIARESPONSE']._serialized_end = 1094
    _globals['_MUTATECUSTOMERNEGATIVECRITERIARESULT']._serialized_start = 1097
    _globals['_MUTATECUSTOMERNEGATIVECRITERIARESULT']._serialized_end = 1315
    _globals['_CUSTOMERNEGATIVECRITERIONSERVICE']._serialized_start = 1318
    _globals['_CUSTOMERNEGATIVECRITERIONSERVICE']._serialized_end = 1707