"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1beta/termsofserviceagreementstate.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.shopping.merchant.accounts.v1beta import termsofservicekind_pb2 as google_dot_shopping_dot_merchant_dot_accounts_dot_v1beta_dot_termsofservicekind__pb2
from ......google.type import date_pb2 as google_dot_type_dot_date__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nKgoogle/shopping/merchant/accounts/v1beta/termsofserviceagreementstate.proto\x12(google.shopping.merchant.accounts.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1aAgoogle/shopping/merchant/accounts/v1beta/termsofservicekind.proto\x1a\x16google/type/date.proto"\x8f\x04\n\x1cTermsOfServiceAgreementState\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x13\n\x0bregion_code\x18\x02 \x01(\t\x12[\n\x15terms_of_service_kind\x18\x03 \x01(\x0e2<.google.shopping.merchant.accounts.v1beta.TermsOfServiceKind\x12I\n\x08accepted\x18\x04 \x01(\x0b22.google.shopping.merchant.accounts.v1beta.AcceptedH\x00\x88\x01\x01\x12I\n\x08required\x18\x05 \x01(\x0b22.google.shopping.merchant.accounts.v1beta.RequiredH\x01\x88\x01\x01:\xb9\x01\xeaA\xb5\x01\n7merchantapi.googleapis.com/TermsOfServiceAgreementState\x12=accounts/{account}/termsOfServiceAgreementStates/{identifier}*\x1dtermsOfServiceAgreementStates2\x1ctermsOfServiceAgreementStateB\x0b\n\t_acceptedB\x0b\n\t_required"\xcf\x01\n\x08Accepted\x12H\n\x10terms_of_service\x18\x01 \x01(\tB.\xfaA+\n)merchantapi.googleapis.com/TermsOfService\x12<\n\x0baccepted_by\x18\x02 \x01(\tB\'\xfaA$\n"merchantapi.googleapis.com/Account\x12+\n\x0bvalid_until\x18\x03 \x01(\x0b2\x11.google.type.DateH\x00\x88\x01\x01B\x0e\n\x0c_valid_until"j\n\x08Required\x12H\n\x10terms_of_service\x18\x01 \x01(\tB.\xfaA+\n)merchantapi.googleapis.com/TermsOfService\x12\x14\n\x0ctos_file_uri\x18\x02 \x01(\t"w\n&GetTermsOfServiceAgreementStateRequest\x12M\n\x04name\x18\x01 \x01(\tB?\xe0A\x02\xfaA9\n7merchantapi.googleapis.com/TermsOfServiceAgreementState"\x8c\x01\n9RetrieveForApplicationTermsOfServiceAgreementStateRequest\x12O\n\x06parent\x18\x01 \x01(\tB?\xe0A\x02\xfaA9\x127merchantapi.googleapis.com/TermsOfServiceAgreementState2\xcf\x05\n#TermsOfServiceAgreementStateService\x12\x8e\x02\n\x1fGetTermsOfServiceAgreementState\x12P.google.shopping.merchant.accounts.v1beta.GetTermsOfServiceAgreementStateRequest\x1aF.google.shopping.merchant.accounts.v1beta.TermsOfServiceAgreementState"Q\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/accounts/v1beta/{name=accounts/*/termsOfServiceAgreementStates/*}\x12\xcd\x02\n2RetrieveForApplicationTermsOfServiceAgreementState\x12c.google.shopping.merchant.accounts.v1beta.RetrieveForApplicationTermsOfServiceAgreementStateRequest\x1aF.google.shopping.merchant.accounts.v1beta.TermsOfServiceAgreementState"j\xdaA\x06parent\x82\xd3\xe4\x93\x02[\x12Y/accounts/v1beta/{parent=accounts/*}/termsOfServiceAgreementStates:retrieveForApplication\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xa3\x01\n,com.google.shopping.merchant.accounts.v1betaB!TermsOfServiceAgreementStateProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1beta.termsofserviceagreementstate_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.shopping.merchant.accounts.v1betaB!TermsOfServiceAgreementStateProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspb'
    _globals['_TERMSOFSERVICEAGREEMENTSTATE'].fields_by_name['name']._loaded_options = None
    _globals['_TERMSOFSERVICEAGREEMENTSTATE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_TERMSOFSERVICEAGREEMENTSTATE']._loaded_options = None
    _globals['_TERMSOFSERVICEAGREEMENTSTATE']._serialized_options = b'\xeaA\xb5\x01\n7merchantapi.googleapis.com/TermsOfServiceAgreementState\x12=accounts/{account}/termsOfServiceAgreementStates/{identifier}*\x1dtermsOfServiceAgreementStates2\x1ctermsOfServiceAgreementState'
    _globals['_ACCEPTED'].fields_by_name['terms_of_service']._loaded_options = None
    _globals['_ACCEPTED'].fields_by_name['terms_of_service']._serialized_options = b'\xfaA+\n)merchantapi.googleapis.com/TermsOfService'
    _globals['_ACCEPTED'].fields_by_name['accepted_by']._loaded_options = None
    _globals['_ACCEPTED'].fields_by_name['accepted_by']._serialized_options = b'\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_REQUIRED'].fields_by_name['terms_of_service']._loaded_options = None
    _globals['_REQUIRED'].fields_by_name['terms_of_service']._serialized_options = b'\xfaA+\n)merchantapi.googleapis.com/TermsOfService'
    _globals['_GETTERMSOFSERVICEAGREEMENTSTATEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTERMSOFSERVICEAGREEMENTSTATEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA9\n7merchantapi.googleapis.com/TermsOfServiceAgreementState'
    _globals['_RETRIEVEFORAPPLICATIONTERMSOFSERVICEAGREEMENTSTATEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_RETRIEVEFORAPPLICATIONTERMSOFSERVICEAGREEMENTSTATEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA9\x127merchantapi.googleapis.com/TermsOfServiceAgreementState'
    _globals['_TERMSOFSERVICEAGREEMENTSTATESERVICE']._loaded_options = None
    _globals['_TERMSOFSERVICEAGREEMENTSTATESERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_TERMSOFSERVICEAGREEMENTSTATESERVICE'].methods_by_name['GetTermsOfServiceAgreementState']._loaded_options = None
    _globals['_TERMSOFSERVICEAGREEMENTSTATESERVICE'].methods_by_name['GetTermsOfServiceAgreementState']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/accounts/v1beta/{name=accounts/*/termsOfServiceAgreementStates/*}'
    _globals['_TERMSOFSERVICEAGREEMENTSTATESERVICE'].methods_by_name['RetrieveForApplicationTermsOfServiceAgreementState']._loaded_options = None
    _globals['_TERMSOFSERVICEAGREEMENTSTATESERVICE'].methods_by_name['RetrieveForApplicationTermsOfServiceAgreementState']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02[\x12Y/accounts/v1beta/{parent=accounts/*}/termsOfServiceAgreementStates:retrieveForApplication'
    _globals['_TERMSOFSERVICEAGREEMENTSTATE']._serialized_start = 328
    _globals['_TERMSOFSERVICEAGREEMENTSTATE']._serialized_end = 855
    _globals['_ACCEPTED']._serialized_start = 858
    _globals['_ACCEPTED']._serialized_end = 1065
    _globals['_REQUIRED']._serialized_start = 1067
    _globals['_REQUIRED']._serialized_end = 1173
    _globals['_GETTERMSOFSERVICEAGREEMENTSTATEREQUEST']._serialized_start = 1175
    _globals['_GETTERMSOFSERVICEAGREEMENTSTATEREQUEST']._serialized_end = 1294
    _globals['_RETRIEVEFORAPPLICATIONTERMSOFSERVICEAGREEMENTSTATEREQUEST']._serialized_start = 1297
    _globals['_RETRIEVEFORAPPLICATIONTERMSOFSERVICEAGREEMENTSTATEREQUEST']._serialized_end = 1437
    _globals['_TERMSOFSERVICEAGREEMENTSTATESERVICE']._serialized_start = 1440
    _globals['_TERMSOFSERVICEAGREEMENTSTATESERVICE']._serialized_end = 2159