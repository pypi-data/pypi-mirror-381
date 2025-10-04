"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1beta/termsofservice.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ......google.shopping.merchant.accounts.v1beta import termsofservicekind_pb2 as google_dot_shopping_dot_merchant_dot_accounts_dot_v1beta_dot_termsofservicekind__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/shopping/merchant/accounts/v1beta/termsofservice.proto\x12(google.shopping.merchant.accounts.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1aAgoogle/shopping/merchant/accounts/v1beta/termsofservicekind.proto"\xb2\x02\n\x0eTermsOfService\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x08\xfaA+\n)merchantapi.googleapis.com/TermsOfService\x12\x13\n\x0bregion_code\x18\x02 \x01(\t\x12J\n\x04kind\x18\x03 \x01(\x0e2<.google.shopping.merchant.accounts.v1beta.TermsOfServiceKind\x12\x15\n\x08file_uri\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x08external\x18\x05 \x01(\x08:H\xeaAE\n)merchantapi.googleapis.com/TermsOfService\x12\x18termsOfService/{version}B\x0b\n\t_file_uri"[\n\x18GetTermsOfServiceRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/TermsOfService"\x90\x01\n#RetrieveLatestTermsOfServiceRequest\x12\x18\n\x0bregion_code\x18\x01 \x01(\tB\x03\xe0A\x02\x12O\n\x04kind\x18\x02 \x01(\x0e2<.google.shopping.merchant.accounts.v1beta.TermsOfServiceKindB\x03\xe0A\x02"\xb5\x01\n\x1bAcceptTermsOfServiceRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/TermsOfService\x12;\n\x07account\x18\x02 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12\x18\n\x0bregion_code\x18\x03 \x01(\tB\x03\xe0A\x022\xc7\x05\n\x15TermsOfServiceService\x12\xca\x01\n\x11GetTermsOfService\x12B.google.shopping.merchant.accounts.v1beta.GetTermsOfServiceRequest\x1a8.google.shopping.merchant.accounts.v1beta.TermsOfService"7\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/accounts/v1beta/{name=termsOfService/*}\x12\xdf\x01\n\x1cRetrieveLatestTermsOfService\x12M.google.shopping.merchant.accounts.v1beta.RetrieveLatestTermsOfServiceRequest\x1a8.google.shopping.merchant.accounts.v1beta.TermsOfService"6\x82\xd3\xe4\x93\x020\x12./accounts/v1beta/termsOfService:retrieveLatest\x12\xb5\x01\n\x14AcceptTermsOfService\x12E.google.shopping.merchant.accounts.v1beta.AcceptTermsOfServiceRequest\x1a\x16.google.protobuf.Empty">\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//accounts/v1beta/{name=termsOfService/*}:accept\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x95\x01\n,com.google.shopping.merchant.accounts.v1betaB\x13TermsOfServiceProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1beta.termsofservice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.shopping.merchant.accounts.v1betaB\x13TermsOfServiceProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspb'
    _globals['_TERMSOFSERVICE'].fields_by_name['name']._loaded_options = None
    _globals['_TERMSOFSERVICE'].fields_by_name['name']._serialized_options = b'\xe0A\x08\xfaA+\n)merchantapi.googleapis.com/TermsOfService'
    _globals['_TERMSOFSERVICE']._loaded_options = None
    _globals['_TERMSOFSERVICE']._serialized_options = b'\xeaAE\n)merchantapi.googleapis.com/TermsOfService\x12\x18termsOfService/{version}'
    _globals['_GETTERMSOFSERVICEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTERMSOFSERVICEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/TermsOfService'
    _globals['_RETRIEVELATESTTERMSOFSERVICEREQUEST'].fields_by_name['region_code']._loaded_options = None
    _globals['_RETRIEVELATESTTERMSOFSERVICEREQUEST'].fields_by_name['region_code']._serialized_options = b'\xe0A\x02'
    _globals['_RETRIEVELATESTTERMSOFSERVICEREQUEST'].fields_by_name['kind']._loaded_options = None
    _globals['_RETRIEVELATESTTERMSOFSERVICEREQUEST'].fields_by_name['kind']._serialized_options = b'\xe0A\x02'
    _globals['_ACCEPTTERMSOFSERVICEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ACCEPTTERMSOFSERVICEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/TermsOfService'
    _globals['_ACCEPTTERMSOFSERVICEREQUEST'].fields_by_name['account']._loaded_options = None
    _globals['_ACCEPTTERMSOFSERVICEREQUEST'].fields_by_name['account']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_ACCEPTTERMSOFSERVICEREQUEST'].fields_by_name['region_code']._loaded_options = None
    _globals['_ACCEPTTERMSOFSERVICEREQUEST'].fields_by_name['region_code']._serialized_options = b'\xe0A\x02'
    _globals['_TERMSOFSERVICESERVICE']._loaded_options = None
    _globals['_TERMSOFSERVICESERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_TERMSOFSERVICESERVICE'].methods_by_name['GetTermsOfService']._loaded_options = None
    _globals['_TERMSOFSERVICESERVICE'].methods_by_name['GetTermsOfService']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/accounts/v1beta/{name=termsOfService/*}'
    _globals['_TERMSOFSERVICESERVICE'].methods_by_name['RetrieveLatestTermsOfService']._loaded_options = None
    _globals['_TERMSOFSERVICESERVICE'].methods_by_name['RetrieveLatestTermsOfService']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./accounts/v1beta/termsOfService:retrieveLatest'
    _globals['_TERMSOFSERVICESERVICE'].methods_by_name['AcceptTermsOfService']._loaded_options = None
    _globals['_TERMSOFSERVICESERVICE'].methods_by_name['AcceptTermsOfService']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//accounts/v1beta/{name=termsOfService/*}:accept'
    _globals['_TERMSOFSERVICE']._serialized_start = 319
    _globals['_TERMSOFSERVICE']._serialized_end = 625
    _globals['_GETTERMSOFSERVICEREQUEST']._serialized_start = 627
    _globals['_GETTERMSOFSERVICEREQUEST']._serialized_end = 718
    _globals['_RETRIEVELATESTTERMSOFSERVICEREQUEST']._serialized_start = 721
    _globals['_RETRIEVELATESTTERMSOFSERVICEREQUEST']._serialized_end = 865
    _globals['_ACCEPTTERMSOFSERVICEREQUEST']._serialized_start = 868
    _globals['_ACCEPTTERMSOFSERVICEREQUEST']._serialized_end = 1049
    _globals['_TERMSOFSERVICESERVICE']._serialized_start = 1052
    _globals['_TERMSOFSERVICESERVICE']._serialized_end = 1763