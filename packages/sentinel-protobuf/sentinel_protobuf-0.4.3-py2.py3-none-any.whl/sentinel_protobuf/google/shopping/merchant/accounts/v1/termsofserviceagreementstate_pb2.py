"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1/termsofserviceagreementstate.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.shopping.merchant.accounts.v1 import termsofservicekind_pb2 as google_dot_shopping_dot_merchant_dot_accounts_dot_v1_dot_termsofservicekind__pb2
from ......google.type import date_pb2 as google_dot_type_dot_date__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGgoogle/shopping/merchant/accounts/v1/termsofserviceagreementstate.proto\x12$google.shopping.merchant.accounts.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a=google/shopping/merchant/accounts/v1/termsofservicekind.proto\x1a\x16google/type/date.proto"\x97\x04\n\x1cTermsOfServiceAgreementState\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x18\n\x0bregion_code\x18\x02 \x01(\tB\x03\xe0A\x02\x12\\\n\x15terms_of_service_kind\x18\x03 \x01(\x0e28.google.shopping.merchant.accounts.v1.TermsOfServiceKindB\x03\xe0A\x02\x12J\n\x08accepted\x18\x04 \x01(\x0b2..google.shopping.merchant.accounts.v1.AcceptedB\x03\xe0A\x01H\x00\x88\x01\x01\x12J\n\x08required\x18\x05 \x01(\x0b2..google.shopping.merchant.accounts.v1.RequiredB\x03\xe0A\x01H\x01\x88\x01\x01:\xb9\x01\xeaA\xb5\x01\n7merchantapi.googleapis.com/TermsOfServiceAgreementState\x12=accounts/{account}/termsOfServiceAgreementStates/{identifier}*\x1dtermsOfServiceAgreementStates2\x1ctermsOfServiceAgreementStateB\x0b\n\t_acceptedB\x0b\n\t_required"\xda\x01\n\x08Accepted\x12K\n\x10terms_of_service\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/TermsOfService\x12?\n\x0baccepted_by\x18\x02 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x120\n\x0bvalid_until\x18\x03 \x01(\x0b2\x11.google.type.DateB\x03\xe0A\x01H\x00\x88\x01\x01B\x0e\n\x0c_valid_until"r\n\x08Required\x12K\n\x10terms_of_service\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/TermsOfService\x12\x19\n\x0ctos_file_uri\x18\x02 \x01(\tB\x03\xe0A\x02"w\n&GetTermsOfServiceAgreementStateRequest\x12M\n\x04name\x18\x01 \x01(\tB?\xe0A\x02\xfaA9\n7merchantapi.googleapis.com/TermsOfServiceAgreementState"\x8c\x01\n9RetrieveForApplicationTermsOfServiceAgreementStateRequest\x12O\n\x06parent\x18\x01 \x01(\tB?\xe0A\x02\xfaA9\x127merchantapi.googleapis.com/TermsOfServiceAgreementState2\xb7\x05\n#TermsOfServiceAgreementStateService\x12\x82\x02\n\x1fGetTermsOfServiceAgreementState\x12L.google.shopping.merchant.accounts.v1.GetTermsOfServiceAgreementStateRequest\x1aB.google.shopping.merchant.accounts.v1.TermsOfServiceAgreementState"M\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/accounts/v1/{name=accounts/*/termsOfServiceAgreementStates/*}\x12\xc1\x02\n2RetrieveForApplicationTermsOfServiceAgreementState\x12_.google.shopping.merchant.accounts.v1.RetrieveForApplicationTermsOfServiceAgreementStateRequest\x1aB.google.shopping.merchant.accounts.v1.TermsOfServiceAgreementState"f\xdaA\x06parent\x82\xd3\xe4\x93\x02W\x12U/accounts/v1/{parent=accounts/*}/termsOfServiceAgreementStates:retrieveForApplication\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x94\x02\n(com.google.shopping.merchant.accounts.v1B!TermsOfServiceAgreementStateProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1.termsofserviceagreementstate_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.shopping.merchant.accounts.v1B!TermsOfServiceAgreementStateProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1'
    _globals['_TERMSOFSERVICEAGREEMENTSTATE'].fields_by_name['name']._loaded_options = None
    _globals['_TERMSOFSERVICEAGREEMENTSTATE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_TERMSOFSERVICEAGREEMENTSTATE'].fields_by_name['region_code']._loaded_options = None
    _globals['_TERMSOFSERVICEAGREEMENTSTATE'].fields_by_name['region_code']._serialized_options = b'\xe0A\x02'
    _globals['_TERMSOFSERVICEAGREEMENTSTATE'].fields_by_name['terms_of_service_kind']._loaded_options = None
    _globals['_TERMSOFSERVICEAGREEMENTSTATE'].fields_by_name['terms_of_service_kind']._serialized_options = b'\xe0A\x02'
    _globals['_TERMSOFSERVICEAGREEMENTSTATE'].fields_by_name['accepted']._loaded_options = None
    _globals['_TERMSOFSERVICEAGREEMENTSTATE'].fields_by_name['accepted']._serialized_options = b'\xe0A\x01'
    _globals['_TERMSOFSERVICEAGREEMENTSTATE'].fields_by_name['required']._loaded_options = None
    _globals['_TERMSOFSERVICEAGREEMENTSTATE'].fields_by_name['required']._serialized_options = b'\xe0A\x01'
    _globals['_TERMSOFSERVICEAGREEMENTSTATE']._loaded_options = None
    _globals['_TERMSOFSERVICEAGREEMENTSTATE']._serialized_options = b'\xeaA\xb5\x01\n7merchantapi.googleapis.com/TermsOfServiceAgreementState\x12=accounts/{account}/termsOfServiceAgreementStates/{identifier}*\x1dtermsOfServiceAgreementStates2\x1ctermsOfServiceAgreementState'
    _globals['_ACCEPTED'].fields_by_name['terms_of_service']._loaded_options = None
    _globals['_ACCEPTED'].fields_by_name['terms_of_service']._serialized_options = b'\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/TermsOfService'
    _globals['_ACCEPTED'].fields_by_name['accepted_by']._loaded_options = None
    _globals['_ACCEPTED'].fields_by_name['accepted_by']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_ACCEPTED'].fields_by_name['valid_until']._loaded_options = None
    _globals['_ACCEPTED'].fields_by_name['valid_until']._serialized_options = b'\xe0A\x01'
    _globals['_REQUIRED'].fields_by_name['terms_of_service']._loaded_options = None
    _globals['_REQUIRED'].fields_by_name['terms_of_service']._serialized_options = b'\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/TermsOfService'
    _globals['_REQUIRED'].fields_by_name['tos_file_uri']._loaded_options = None
    _globals['_REQUIRED'].fields_by_name['tos_file_uri']._serialized_options = b'\xe0A\x02'
    _globals['_GETTERMSOFSERVICEAGREEMENTSTATEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTERMSOFSERVICEAGREEMENTSTATEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA9\n7merchantapi.googleapis.com/TermsOfServiceAgreementState'
    _globals['_RETRIEVEFORAPPLICATIONTERMSOFSERVICEAGREEMENTSTATEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_RETRIEVEFORAPPLICATIONTERMSOFSERVICEAGREEMENTSTATEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA9\x127merchantapi.googleapis.com/TermsOfServiceAgreementState'
    _globals['_TERMSOFSERVICEAGREEMENTSTATESERVICE']._loaded_options = None
    _globals['_TERMSOFSERVICEAGREEMENTSTATESERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_TERMSOFSERVICEAGREEMENTSTATESERVICE'].methods_by_name['GetTermsOfServiceAgreementState']._loaded_options = None
    _globals['_TERMSOFSERVICEAGREEMENTSTATESERVICE'].methods_by_name['GetTermsOfServiceAgreementState']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/accounts/v1/{name=accounts/*/termsOfServiceAgreementStates/*}'
    _globals['_TERMSOFSERVICEAGREEMENTSTATESERVICE'].methods_by_name['RetrieveForApplicationTermsOfServiceAgreementState']._loaded_options = None
    _globals['_TERMSOFSERVICEAGREEMENTSTATESERVICE'].methods_by_name['RetrieveForApplicationTermsOfServiceAgreementState']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02W\x12U/accounts/v1/{parent=accounts/*}/termsOfServiceAgreementStates:retrieveForApplication'
    _globals['_TERMSOFSERVICEAGREEMENTSTATE']._serialized_start = 316
    _globals['_TERMSOFSERVICEAGREEMENTSTATE']._serialized_end = 851
    _globals['_ACCEPTED']._serialized_start = 854
    _globals['_ACCEPTED']._serialized_end = 1072
    _globals['_REQUIRED']._serialized_start = 1074
    _globals['_REQUIRED']._serialized_end = 1188
    _globals['_GETTERMSOFSERVICEAGREEMENTSTATEREQUEST']._serialized_start = 1190
    _globals['_GETTERMSOFSERVICEAGREEMENTSTATEREQUEST']._serialized_end = 1309
    _globals['_RETRIEVEFORAPPLICATIONTERMSOFSERVICEAGREEMENTSTATEREQUEST']._serialized_start = 1312
    _globals['_RETRIEVEFORAPPLICATIONTERMSOFSERVICEAGREEMENTSTATEREQUEST']._serialized_end = 1452
    _globals['_TERMSOFSERVICEAGREEMENTSTATESERVICE']._serialized_start = 1455
    _globals['_TERMSOFSERVICEAGREEMENTSTATESERVICE']._serialized_end = 2150