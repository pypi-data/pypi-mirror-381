"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1/customerservice.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.type import phone_number_pb2 as google_dot_type_dot_phone__number__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/shopping/merchant/accounts/v1/customerservice.proto\x12$google.shopping.merchant.accounts.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/type/phone_number.proto"\x90\x01\n\x0fCustomerService\x12\x15\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x01H\x00\x88\x01\x01\x12\x17\n\x05email\x18\x02 \x01(\tB\x03\xe0A\x01H\x01\x88\x01\x01\x121\n\x05phone\x18\x03 \x01(\x0b2\x18.google.type.PhoneNumberB\x03\xe0A\x01H\x02\x88\x01\x01B\x06\n\x04_uriB\x08\n\x06_emailB\x08\n\x06_phoneB\x87\x02\n(com.google.shopping.merchant.accounts.v1B\x14CustomerServiceProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1.customerservice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.shopping.merchant.accounts.v1B\x14CustomerServiceProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1'
    _globals['_CUSTOMERSERVICE'].fields_by_name['uri']._loaded_options = None
    _globals['_CUSTOMERSERVICE'].fields_by_name['uri']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMERSERVICE'].fields_by_name['email']._loaded_options = None
    _globals['_CUSTOMERSERVICE'].fields_by_name['email']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMERSERVICE'].fields_by_name['phone']._loaded_options = None
    _globals['_CUSTOMERSERVICE'].fields_by_name['phone']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMERSERVICE']._serialized_start = 166
    _globals['_CUSTOMERSERVICE']._serialized_end = 310