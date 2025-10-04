"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/services/conversion_value_rule_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v19.resources import conversion_value_rule_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_resources_dot_conversion__value__rule__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/ads/googleads/v19/services/conversion_value_rule_service.proto\x12!google.ads.googleads.v19.services\x1a:google/ads/googleads/v19/enums/response_content_type.proto\x1a>google/ads/googleads/v19/resources/conversion_value_rule.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\xb3\x02\n!MutateConversionValueRulesRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12X\n\noperations\x18\x02 \x03(\x0b2?.google.ads.googleads.v19.services.ConversionValueRuleOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x05 \x01(\x08\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08\x12j\n\x15response_content_type\x18\x04 \x01(\x0e2K.google.ads.googleads.v19.enums.ResponseContentTypeEnum.ResponseContentType"\xb7\x02\n\x1cConversionValueRuleOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12I\n\x06create\x18\x01 \x01(\x0b27.google.ads.googleads.v19.resources.ConversionValueRuleH\x00\x12I\n\x06update\x18\x02 \x01(\x0b27.google.ads.googleads.v19.resources.ConversionValueRuleH\x00\x12C\n\x06remove\x18\x03 \x01(\tB1\xfaA.\n,googleads.googleapis.com/ConversionValueRuleH\x00B\x0b\n\toperation"\xac\x01\n"MutateConversionValueRulesResponse\x12S\n\x07results\x18\x02 \x03(\x0b2B.google.ads.googleads.v19.services.MutateConversionValueRuleResult\x121\n\x15partial_failure_error\x18\x03 \x01(\x0b2\x12.google.rpc.Status"\xc3\x01\n\x1fMutateConversionValueRuleResult\x12H\n\rresource_name\x18\x01 \x01(\tB1\xfaA.\n,googleads.googleapis.com/ConversionValueRule\x12V\n\x15conversion_value_rule\x18\x02 \x01(\x0b27.google.ads.googleads.v19.resources.ConversionValueRule2\xef\x02\n\x1aConversionValueRuleService\x12\x89\x02\n\x1aMutateConversionValueRules\x12D.google.ads.googleads.v19.services.MutateConversionValueRulesRequest\x1aE.google.ads.googleads.v19.services.MutateConversionValueRulesResponse"^\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02?":/v19/customers/{customer_id=*}/conversionValueRules:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8b\x02\n%com.google.ads.googleads.v19.servicesB\x1fConversionValueRuleServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.services.conversion_value_rule_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v19.servicesB\x1fConversionValueRuleServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Services'
    _globals['_MUTATECONVERSIONVALUERULESREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECONVERSIONVALUERULESREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECONVERSIONVALUERULESREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATECONVERSIONVALUERULESREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_CONVERSIONVALUERULEOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_CONVERSIONVALUERULEOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA.\n,googleads.googleapis.com/ConversionValueRule'
    _globals['_MUTATECONVERSIONVALUERULERESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECONVERSIONVALUERULERESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA.\n,googleads.googleapis.com/ConversionValueRule'
    _globals['_CONVERSIONVALUERULESERVICE']._loaded_options = None
    _globals['_CONVERSIONVALUERULESERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CONVERSIONVALUERULESERVICE'].methods_by_name['MutateConversionValueRules']._loaded_options = None
    _globals['_CONVERSIONVALUERULESERVICE'].methods_by_name['MutateConversionValueRules']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02?":/v19/customers/{customer_id=*}/conversionValueRules:mutate:\x01*'
    _globals['_MUTATECONVERSIONVALUERULESREQUEST']._serialized_start = 407
    _globals['_MUTATECONVERSIONVALUERULESREQUEST']._serialized_end = 714
    _globals['_CONVERSIONVALUERULEOPERATION']._serialized_start = 717
    _globals['_CONVERSIONVALUERULEOPERATION']._serialized_end = 1028
    _globals['_MUTATECONVERSIONVALUERULESRESPONSE']._serialized_start = 1031
    _globals['_MUTATECONVERSIONVALUERULESRESPONSE']._serialized_end = 1203
    _globals['_MUTATECONVERSIONVALUERULERESULT']._serialized_start = 1206
    _globals['_MUTATECONVERSIONVALUERULERESULT']._serialized_end = 1401
    _globals['_CONVERSIONVALUERULESERVICE']._serialized_start = 1404
    _globals['_CONVERSIONVALUERULESERVICE']._serialized_end = 1771