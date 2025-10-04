"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/services/conversion_upload_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.common import consent_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_consent__pb2
from ......google.ads.googleads.v19.common import offline_user_data_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_offline__user__data__pb2
from ......google.ads.googleads.v19.enums import conversion_customer_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_conversion__customer__type__pb2
from ......google.ads.googleads.v19.enums import conversion_environment_enum_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_conversion__environment__enum__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/ads/googleads/v19/services/conversion_upload_service.proto\x12!google.ads.googleads.v19.services\x1a-google/ads/googleads/v19/common/consent.proto\x1a7google/ads/googleads/v19/common/offline_user_data.proto\x1a=google/ads/googleads/v19/enums/conversion_customer_type.proto\x1a@google/ads/googleads/v19/enums/conversion_environment_enum.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto"\xf8\x01\n\x1dUploadClickConversionsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12L\n\x0bconversions\x18\x02 \x03(\x0b22.google.ads.googleads.v19.services.ClickConversionB\x03\xe0A\x02\x12\x1c\n\x0fpartial_failure\x18\x03 \x01(\x08B\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12\x15\n\rdebug_enabled\x18\x05 \x01(\x08\x12\x18\n\x06job_id\x18\x06 \x01(\x05B\x03\xe0A\x01H\x00\x88\x01\x01B\t\n\x07_job_id"\xae\x01\n\x1eUploadClickConversionsResponse\x121\n\x15partial_failure_error\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x12I\n\x07results\x18\x02 \x03(\x0b28.google.ads.googleads.v19.services.ClickConversionResult\x12\x0e\n\x06job_id\x18\x03 \x01(\x03"\xba\x01\n\x1cUploadCallConversionsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12K\n\x0bconversions\x18\x02 \x03(\x0b21.google.ads.googleads.v19.services.CallConversionB\x03\xe0A\x02\x12\x1c\n\x0fpartial_failure\x18\x03 \x01(\x08B\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08"\x9c\x01\n\x1dUploadCallConversionsResponse\x121\n\x15partial_failure_error\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x12H\n\x07results\x18\x02 \x03(\x0b27.google.ads.googleads.v19.services.CallConversionResult"\xc1\x08\n\x0fClickConversion\x12\x12\n\x05gclid\x18\t \x01(\tH\x01\x88\x01\x01\x12\x0e\n\x06gbraid\x18\x12 \x01(\t\x12\x0e\n\x06wbraid\x18\x13 \x01(\t\x12\x1e\n\x11conversion_action\x18\n \x01(\tH\x02\x88\x01\x01\x12!\n\x14conversion_date_time\x18\x0b \x01(\tH\x03\x88\x01\x01\x12\x1d\n\x10conversion_value\x18\x0c \x01(\x01H\x04\x88\x01\x01\x12\x1a\n\rcurrency_code\x18\r \x01(\tH\x05\x88\x01\x01\x12\x15\n\x08order_id\x18\x0e \x01(\tH\x06\x88\x01\x01\x12]\n\x19external_attribution_data\x18\x07 \x01(\x0b2:.google.ads.googleads.v19.services.ExternalAttributionData\x12K\n\x10custom_variables\x18\x0f \x03(\x0b21.google.ads.googleads.v19.services.CustomVariable\x12>\n\tcart_data\x18\x10 \x01(\x0b2+.google.ads.googleads.v19.services.CartData\x12I\n\x10user_identifiers\x18\x11 \x03(\x0b2/.google.ads.googleads.v19.common.UserIdentifier\x12o\n\x16conversion_environment\x18\x14 \x01(\x0e2O.google.ads.googleads.v19.enums.ConversionEnvironmentEnum.ConversionEnvironment\x129\n\x07consent\x18\x17 \x01(\x0b2(.google.ads.googleads.v19.common.Consent\x12h\n\rcustomer_type\x18\x1a \x01(\x0e2Q.google.ads.googleads.v19.enums.ConversionCustomerTypeEnum.ConversionCustomerType\x12$\n\x1asession_attributes_encoded\x18\x18 \x01(\x0cH\x00\x12o\n"session_attributes_key_value_pairs\x18\x19 \x01(\x0b2A.google.ads.googleads.v19.services.SessionAttributesKeyValuePairsH\x00B\x14\n\x12session_attributesB\x08\n\x06_gclidB\x14\n\x12_conversion_actionB\x17\n\x15_conversion_date_timeB\x13\n\x11_conversion_valueB\x10\n\x0e_currency_codeB\x0b\n\t_order_id"\xce\x03\n\x0eCallConversion\x12\x16\n\tcaller_id\x18\x07 \x01(\tH\x00\x88\x01\x01\x12!\n\x14call_start_date_time\x18\x08 \x01(\tH\x01\x88\x01\x01\x12\x1e\n\x11conversion_action\x18\t \x01(\tH\x02\x88\x01\x01\x12!\n\x14conversion_date_time\x18\n \x01(\tH\x03\x88\x01\x01\x12\x1d\n\x10conversion_value\x18\x0b \x01(\x01H\x04\x88\x01\x01\x12\x1a\n\rcurrency_code\x18\x0c \x01(\tH\x05\x88\x01\x01\x12K\n\x10custom_variables\x18\r \x03(\x0b21.google.ads.googleads.v19.services.CustomVariable\x129\n\x07consent\x18\x0e \x01(\x0b2(.google.ads.googleads.v19.common.ConsentB\x0c\n\n_caller_idB\x17\n\x15_call_start_date_timeB\x14\n\x12_conversion_actionB\x17\n\x15_conversion_date_timeB\x13\n\x11_conversion_valueB\x10\n\x0e_currency_code"\xab\x01\n\x17ExternalAttributionData\x12(\n\x1bexternal_attribution_credit\x18\x03 \x01(\x01H\x00\x88\x01\x01\x12\'\n\x1aexternal_attribution_model\x18\x04 \x01(\tH\x01\x88\x01\x01B\x1e\n\x1c_external_attribution_creditB\x1d\n\x1b_external_attribution_model"\x92\x02\n\x15ClickConversionResult\x12\x12\n\x05gclid\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x0e\n\x06gbraid\x18\x08 \x01(\t\x12\x0e\n\x06wbraid\x18\t \x01(\t\x12\x1e\n\x11conversion_action\x18\x05 \x01(\tH\x01\x88\x01\x01\x12!\n\x14conversion_date_time\x18\x06 \x01(\tH\x02\x88\x01\x01\x12I\n\x10user_identifiers\x18\x07 \x03(\x0b2/.google.ads.googleads.v19.common.UserIdentifierB\x08\n\x06_gclidB\x14\n\x12_conversion_actionB\x17\n\x15_conversion_date_time"\xea\x01\n\x14CallConversionResult\x12\x16\n\tcaller_id\x18\x05 \x01(\tH\x00\x88\x01\x01\x12!\n\x14call_start_date_time\x18\x06 \x01(\tH\x01\x88\x01\x01\x12\x1e\n\x11conversion_action\x18\x07 \x01(\tH\x02\x88\x01\x01\x12!\n\x14conversion_date_time\x18\x08 \x01(\tH\x03\x88\x01\x01B\x0c\n\n_caller_idB\x17\n\x15_call_start_date_timeB\x14\n\x12_conversion_actionB\x17\n\x15_conversion_date_time"{\n\x0eCustomVariable\x12Z\n\x1aconversion_custom_variable\x18\x01 \x01(\tB6\xfaA3\n1googleads.googleapis.com/ConversionCustomVariable\x12\r\n\x05value\x18\x02 \x01(\t"\xf9\x01\n\x08CartData\x12\x13\n\x0bmerchant_id\x18\x06 \x01(\x03\x12\x19\n\x11feed_country_code\x18\x02 \x01(\t\x12\x1a\n\x12feed_language_code\x18\x03 \x01(\t\x12\x1e\n\x16local_transaction_cost\x18\x04 \x01(\x01\x12?\n\x05items\x18\x05 \x03(\x0b20.google.ads.googleads.v19.services.CartData.Item\x1a@\n\x04Item\x12\x12\n\nproduct_id\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x05\x12\x12\n\nunit_price\x18\x03 \x01(\x01"h\n\x1cSessionAttributeKeyValuePair\x12"\n\x15session_attribute_key\x18\x01 \x01(\tB\x03\xe0A\x02\x12$\n\x17session_attribute_value\x18\x02 \x01(\tB\x03\xe0A\x02"\x7f\n\x1eSessionAttributesKeyValuePairs\x12]\n\x0fkey_value_pairs\x18\x01 \x03(\x0b2?.google.ads.googleads.v19.services.SessionAttributeKeyValuePairB\x03\xe0A\x022\xf4\x04\n\x17ConversionUploadService\x12\x89\x02\n\x16UploadClickConversions\x12@.google.ads.googleads.v19.services.UploadClickConversionsRequest\x1aA.google.ads.googleads.v19.services.UploadClickConversionsResponse"j\xdaA\'customer_id,conversions,partial_failure\x82\xd3\xe4\x93\x02:"5/v19/customers/{customer_id=*}:uploadClickConversions:\x01*\x12\x85\x02\n\x15UploadCallConversions\x12?.google.ads.googleads.v19.services.UploadCallConversionsRequest\x1a@.google.ads.googleads.v19.services.UploadCallConversionsResponse"i\xdaA\'customer_id,conversions,partial_failure\x82\xd3\xe4\x93\x029"4/v19/customers/{customer_id=*}:uploadCallConversions:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x88\x02\n%com.google.ads.googleads.v19.servicesB\x1cConversionUploadServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.services.conversion_upload_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v19.servicesB\x1cConversionUploadServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Services'
    _globals['_UPLOADCLICKCONVERSIONSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_UPLOADCLICKCONVERSIONSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPLOADCLICKCONVERSIONSREQUEST'].fields_by_name['conversions']._loaded_options = None
    _globals['_UPLOADCLICKCONVERSIONSREQUEST'].fields_by_name['conversions']._serialized_options = b'\xe0A\x02'
    _globals['_UPLOADCLICKCONVERSIONSREQUEST'].fields_by_name['partial_failure']._loaded_options = None
    _globals['_UPLOADCLICKCONVERSIONSREQUEST'].fields_by_name['partial_failure']._serialized_options = b'\xe0A\x02'
    _globals['_UPLOADCLICKCONVERSIONSREQUEST'].fields_by_name['job_id']._loaded_options = None
    _globals['_UPLOADCLICKCONVERSIONSREQUEST'].fields_by_name['job_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPLOADCALLCONVERSIONSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_UPLOADCALLCONVERSIONSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPLOADCALLCONVERSIONSREQUEST'].fields_by_name['conversions']._loaded_options = None
    _globals['_UPLOADCALLCONVERSIONSREQUEST'].fields_by_name['conversions']._serialized_options = b'\xe0A\x02'
    _globals['_UPLOADCALLCONVERSIONSREQUEST'].fields_by_name['partial_failure']._loaded_options = None
    _globals['_UPLOADCALLCONVERSIONSREQUEST'].fields_by_name['partial_failure']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMVARIABLE'].fields_by_name['conversion_custom_variable']._loaded_options = None
    _globals['_CUSTOMVARIABLE'].fields_by_name['conversion_custom_variable']._serialized_options = b'\xfaA3\n1googleads.googleapis.com/ConversionCustomVariable'
    _globals['_SESSIONATTRIBUTEKEYVALUEPAIR'].fields_by_name['session_attribute_key']._loaded_options = None
    _globals['_SESSIONATTRIBUTEKEYVALUEPAIR'].fields_by_name['session_attribute_key']._serialized_options = b'\xe0A\x02'
    _globals['_SESSIONATTRIBUTEKEYVALUEPAIR'].fields_by_name['session_attribute_value']._loaded_options = None
    _globals['_SESSIONATTRIBUTEKEYVALUEPAIR'].fields_by_name['session_attribute_value']._serialized_options = b'\xe0A\x02'
    _globals['_SESSIONATTRIBUTESKEYVALUEPAIRS'].fields_by_name['key_value_pairs']._loaded_options = None
    _globals['_SESSIONATTRIBUTESKEYVALUEPAIRS'].fields_by_name['key_value_pairs']._serialized_options = b'\xe0A\x02'
    _globals['_CONVERSIONUPLOADSERVICE']._loaded_options = None
    _globals['_CONVERSIONUPLOADSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CONVERSIONUPLOADSERVICE'].methods_by_name['UploadClickConversions']._loaded_options = None
    _globals['_CONVERSIONUPLOADSERVICE'].methods_by_name['UploadClickConversions']._serialized_options = b'\xdaA\'customer_id,conversions,partial_failure\x82\xd3\xe4\x93\x02:"5/v19/customers/{customer_id=*}:uploadClickConversions:\x01*'
    _globals['_CONVERSIONUPLOADSERVICE'].methods_by_name['UploadCallConversions']._loaded_options = None
    _globals['_CONVERSIONUPLOADSERVICE'].methods_by_name['UploadCallConversions']._serialized_options = b'\xdaA\'customer_id,conversions,partial_failure\x82\xd3\xe4\x93\x029"4/v19/customers/{customer_id=*}:uploadCallConversions:\x01*'
    _globals['_UPLOADCLICKCONVERSIONSREQUEST']._serialized_start = 478
    _globals['_UPLOADCLICKCONVERSIONSREQUEST']._serialized_end = 726
    _globals['_UPLOADCLICKCONVERSIONSRESPONSE']._serialized_start = 729
    _globals['_UPLOADCLICKCONVERSIONSRESPONSE']._serialized_end = 903
    _globals['_UPLOADCALLCONVERSIONSREQUEST']._serialized_start = 906
    _globals['_UPLOADCALLCONVERSIONSREQUEST']._serialized_end = 1092
    _globals['_UPLOADCALLCONVERSIONSRESPONSE']._serialized_start = 1095
    _globals['_UPLOADCALLCONVERSIONSRESPONSE']._serialized_end = 1251
    _globals['_CLICKCONVERSION']._serialized_start = 1254
    _globals['_CLICKCONVERSION']._serialized_end = 2343
    _globals['_CALLCONVERSION']._serialized_start = 2346
    _globals['_CALLCONVERSION']._serialized_end = 2808
    _globals['_EXTERNALATTRIBUTIONDATA']._serialized_start = 2811
    _globals['_EXTERNALATTRIBUTIONDATA']._serialized_end = 2982
    _globals['_CLICKCONVERSIONRESULT']._serialized_start = 2985
    _globals['_CLICKCONVERSIONRESULT']._serialized_end = 3259
    _globals['_CALLCONVERSIONRESULT']._serialized_start = 3262
    _globals['_CALLCONVERSIONRESULT']._serialized_end = 3496
    _globals['_CUSTOMVARIABLE']._serialized_start = 3498
    _globals['_CUSTOMVARIABLE']._serialized_end = 3621
    _globals['_CARTDATA']._serialized_start = 3624
    _globals['_CARTDATA']._serialized_end = 3873
    _globals['_CARTDATA_ITEM']._serialized_start = 3809
    _globals['_CARTDATA_ITEM']._serialized_end = 3873
    _globals['_SESSIONATTRIBUTEKEYVALUEPAIR']._serialized_start = 3875
    _globals['_SESSIONATTRIBUTEKEYVALUEPAIR']._serialized_end = 3979
    _globals['_SESSIONATTRIBUTESKEYVALUEPAIRS']._serialized_start = 3981
    _globals['_SESSIONATTRIBUTESKEYVALUEPAIRS']._serialized_end = 4108
    _globals['_CONVERSIONUPLOADSERVICE']._serialized_start = 4111
    _globals['_CONVERSIONUPLOADSERVICE']._serialized_end = 4739