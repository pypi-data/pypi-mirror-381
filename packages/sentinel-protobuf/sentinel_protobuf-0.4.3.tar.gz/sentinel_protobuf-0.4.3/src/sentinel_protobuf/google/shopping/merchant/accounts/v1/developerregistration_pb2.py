"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1/developerregistration.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/shopping/merchant/accounts/v1/developerregistration.proto\x12$google.shopping.merchant.accounts.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto"\xd1\x01\n\x15DeveloperRegistration\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x14\n\x07gcp_ids\x18\x02 \x03(\tB\x03\xe0A\x03:\x8e\x01\xeaA\x8a\x01\n0merchantapi.googleapis.com/DeveloperRegistration\x12(accounts/{account}/developerRegistration*\x15developerRegistration2\x15developerRegistration"z\n\x12RegisterGcpRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0merchantapi.googleapis.com/DeveloperRegistration\x12\x1c\n\x0fdeveloper_email\x18\x02 \x01(\tB\x03\xe0A\x05"^\n\x14UnregisterGcpRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0merchantapi.googleapis.com/DeveloperRegistration"i\n\x1fGetDeveloperRegistrationRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0merchantapi.googleapis.com/DeveloperRegistration2\xd6\x05\n\x1cDeveloperRegistrationService\x12\xd1\x01\n\x0bRegisterGcp\x128.google.shopping.merchant.accounts.v1.RegisterGcpRequest\x1a;.google.shopping.merchant.accounts.v1.DeveloperRegistration"K\x82\xd3\xe4\x93\x02E"@/accounts/v1/{name=accounts/*/developerRegistration}:registerGcp:\x01*\x12\xe3\x01\n\x18GetDeveloperRegistration\x12E.google.shopping.merchant.accounts.v1.GetDeveloperRegistrationRequest\x1a;.google.shopping.merchant.accounts.v1.DeveloperRegistration"C\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/accounts/v1/{name=accounts/*/developerRegistration}\x12\xb2\x01\n\rUnregisterGcp\x12:.google.shopping.merchant.accounts.v1.UnregisterGcpRequest\x1a\x16.google.protobuf.Empty"M\x82\xd3\xe4\x93\x02G"B/accounts/v1/{name=accounts/*/developerRegistration}:unregisterGcp:\x01*\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x8d\x02\n(com.google.shopping.merchant.accounts.v1B\x1aDeveloperRegistrationProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1.developerregistration_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.shopping.merchant.accounts.v1B\x1aDeveloperRegistrationProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1'
    _globals['_DEVELOPERREGISTRATION'].fields_by_name['name']._loaded_options = None
    _globals['_DEVELOPERREGISTRATION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_DEVELOPERREGISTRATION'].fields_by_name['gcp_ids']._loaded_options = None
    _globals['_DEVELOPERREGISTRATION'].fields_by_name['gcp_ids']._serialized_options = b'\xe0A\x03'
    _globals['_DEVELOPERREGISTRATION']._loaded_options = None
    _globals['_DEVELOPERREGISTRATION']._serialized_options = b'\xeaA\x8a\x01\n0merchantapi.googleapis.com/DeveloperRegistration\x12(accounts/{account}/developerRegistration*\x15developerRegistration2\x15developerRegistration'
    _globals['_REGISTERGCPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_REGISTERGCPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0merchantapi.googleapis.com/DeveloperRegistration'
    _globals['_REGISTERGCPREQUEST'].fields_by_name['developer_email']._loaded_options = None
    _globals['_REGISTERGCPREQUEST'].fields_by_name['developer_email']._serialized_options = b'\xe0A\x05'
    _globals['_UNREGISTERGCPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UNREGISTERGCPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0merchantapi.googleapis.com/DeveloperRegistration'
    _globals['_GETDEVELOPERREGISTRATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDEVELOPERREGISTRATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0merchantapi.googleapis.com/DeveloperRegistration'
    _globals['_DEVELOPERREGISTRATIONSERVICE']._loaded_options = None
    _globals['_DEVELOPERREGISTRATIONSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_DEVELOPERREGISTRATIONSERVICE'].methods_by_name['RegisterGcp']._loaded_options = None
    _globals['_DEVELOPERREGISTRATIONSERVICE'].methods_by_name['RegisterGcp']._serialized_options = b'\x82\xd3\xe4\x93\x02E"@/accounts/v1/{name=accounts/*/developerRegistration}:registerGcp:\x01*'
    _globals['_DEVELOPERREGISTRATIONSERVICE'].methods_by_name['GetDeveloperRegistration']._loaded_options = None
    _globals['_DEVELOPERREGISTRATIONSERVICE'].methods_by_name['GetDeveloperRegistration']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/accounts/v1/{name=accounts/*/developerRegistration}'
    _globals['_DEVELOPERREGISTRATIONSERVICE'].methods_by_name['UnregisterGcp']._loaded_options = None
    _globals['_DEVELOPERREGISTRATIONSERVICE'].methods_by_name['UnregisterGcp']._serialized_options = b'\x82\xd3\xe4\x93\x02G"B/accounts/v1/{name=accounts/*/developerRegistration}:unregisterGcp:\x01*'
    _globals['_DEVELOPERREGISTRATION']._serialized_start = 251
    _globals['_DEVELOPERREGISTRATION']._serialized_end = 460
    _globals['_REGISTERGCPREQUEST']._serialized_start = 462
    _globals['_REGISTERGCPREQUEST']._serialized_end = 584
    _globals['_UNREGISTERGCPREQUEST']._serialized_start = 586
    _globals['_UNREGISTERGCPREQUEST']._serialized_end = 680
    _globals['_GETDEVELOPERREGISTRATIONREQUEST']._serialized_start = 682
    _globals['_GETDEVELOPERREGISTRATIONREQUEST']._serialized_end = 787
    _globals['_DEVELOPERREGISTRATIONSERVICE']._serialized_start = 790
    _globals['_DEVELOPERREGISTRATIONSERVICE']._serialized_end = 1516