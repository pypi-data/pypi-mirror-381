"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1/businessinfo.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.shopping.merchant.accounts.v1 import customerservice_pb2 as google_dot_shopping_dot_merchant_dot_accounts_dot_v1_dot_customerservice__pb2
from ......google.shopping.merchant.accounts.v1 import phoneverificationstate_pb2 as google_dot_shopping_dot_merchant_dot_accounts_dot_v1_dot_phoneverificationstate__pb2
from ......google.type import phone_number_pb2 as google_dot_type_dot_phone__number__pb2
from ......google.type import postal_address_pb2 as google_dot_type_dot_postal__address__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/shopping/merchant/accounts/v1/businessinfo.proto\x12$google.shopping.merchant.accounts.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a:google/shopping/merchant/accounts/v1/customerservice.proto\x1aAgoogle/shopping/merchant/accounts/v1/phoneverificationstate.proto\x1a\x1egoogle/type/phone_number.proto\x1a google/type/postal_address.proto"\xe3\x04\n\x0cBusinessInfo\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x125\n\x07address\x18\x02 \x01(\x0b2\x1a.google.type.PostalAddressB\x03\xe0A\x01H\x00\x88\x01\x01\x121\n\x05phone\x18\x03 \x01(\x0b2\x18.google.type.PhoneNumberB\x03\xe0A\x03H\x01\x88\x01\x01\x12h\n\x18phone_verification_state\x18\x04 \x01(\x0e2<.google.shopping.merchant.accounts.v1.PhoneVerificationStateB\x03\xe0A\x03H\x02\x88\x01\x01\x12Y\n\x10customer_service\x18\x05 \x01(\x0b25.google.shopping.merchant.accounts.v1.CustomerServiceB\x03\xe0A\x01H\x03\x88\x01\x01\x125\n#korean_business_registration_number\x18\x06 \x01(\tB\x03\xe0A\x01H\x04\x88\x01\x01:j\xeaAg\n\'merchantapi.googleapis.com/BusinessInfo\x12\x1faccounts/{account}/businessInfo*\rbusinessInfos2\x0cbusinessInfoB\n\n\x08_addressB\x08\n\x06_phoneB\x1b\n\x19_phone_verification_stateB\x13\n\x11_customer_serviceB&\n$_korean_business_registration_number"W\n\x16GetBusinessInfoRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'merchantapi.googleapis.com/BusinessInfo"\xa1\x01\n\x19UpdateBusinessInfoRequest\x12N\n\rbusiness_info\x18\x01 \x01(\x0b22.google.shopping.merchant.accounts.v1.BusinessInfoB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x012\x9a\x04\n\x13BusinessInfoService\x12\xbf\x01\n\x0fGetBusinessInfo\x12<.google.shopping.merchant.accounts.v1.GetBusinessInfoRequest\x1a2.google.shopping.merchant.accounts.v1.BusinessInfo":\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/accounts/v1/{name=accounts/*/businessInfo}\x12\xf7\x01\n\x12UpdateBusinessInfo\x12?.google.shopping.merchant.accounts.v1.UpdateBusinessInfoRequest\x1a2.google.shopping.merchant.accounts.v1.BusinessInfo"l\xdaA\x19business_info,update_mask\x82\xd3\xe4\x93\x02J29/accounts/v1/{business_info.name=accounts/*/businessInfo}:\rbusiness_info\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x84\x02\n(com.google.shopping.merchant.accounts.v1B\x11BusinessInfoProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1.businessinfo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.shopping.merchant.accounts.v1B\x11BusinessInfoProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1'
    _globals['_BUSINESSINFO'].fields_by_name['name']._loaded_options = None
    _globals['_BUSINESSINFO'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_BUSINESSINFO'].fields_by_name['address']._loaded_options = None
    _globals['_BUSINESSINFO'].fields_by_name['address']._serialized_options = b'\xe0A\x01'
    _globals['_BUSINESSINFO'].fields_by_name['phone']._loaded_options = None
    _globals['_BUSINESSINFO'].fields_by_name['phone']._serialized_options = b'\xe0A\x03'
    _globals['_BUSINESSINFO'].fields_by_name['phone_verification_state']._loaded_options = None
    _globals['_BUSINESSINFO'].fields_by_name['phone_verification_state']._serialized_options = b'\xe0A\x03'
    _globals['_BUSINESSINFO'].fields_by_name['customer_service']._loaded_options = None
    _globals['_BUSINESSINFO'].fields_by_name['customer_service']._serialized_options = b'\xe0A\x01'
    _globals['_BUSINESSINFO'].fields_by_name['korean_business_registration_number']._loaded_options = None
    _globals['_BUSINESSINFO'].fields_by_name['korean_business_registration_number']._serialized_options = b'\xe0A\x01'
    _globals['_BUSINESSINFO']._loaded_options = None
    _globals['_BUSINESSINFO']._serialized_options = b"\xeaAg\n'merchantapi.googleapis.com/BusinessInfo\x12\x1faccounts/{account}/businessInfo*\rbusinessInfos2\x0cbusinessInfo"
    _globals['_GETBUSINESSINFOREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETBUSINESSINFOREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'merchantapi.googleapis.com/BusinessInfo"
    _globals['_UPDATEBUSINESSINFOREQUEST'].fields_by_name['business_info']._loaded_options = None
    _globals['_UPDATEBUSINESSINFOREQUEST'].fields_by_name['business_info']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEBUSINESSINFOREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEBUSINESSINFOREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_BUSINESSINFOSERVICE']._loaded_options = None
    _globals['_BUSINESSINFOSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_BUSINESSINFOSERVICE'].methods_by_name['GetBusinessInfo']._loaded_options = None
    _globals['_BUSINESSINFOSERVICE'].methods_by_name['GetBusinessInfo']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/accounts/v1/{name=accounts/*/businessInfo}'
    _globals['_BUSINESSINFOSERVICE'].methods_by_name['UpdateBusinessInfo']._loaded_options = None
    _globals['_BUSINESSINFOSERVICE'].methods_by_name['UpdateBusinessInfo']._serialized_options = b'\xdaA\x19business_info,update_mask\x82\xd3\xe4\x93\x02J29/accounts/v1/{business_info.name=accounts/*/businessInfo}:\rbusiness_info'
    _globals['_BUSINESSINFO']._serialized_start = 440
    _globals['_BUSINESSINFO']._serialized_end = 1051
    _globals['_GETBUSINESSINFOREQUEST']._serialized_start = 1053
    _globals['_GETBUSINESSINFOREQUEST']._serialized_end = 1140
    _globals['_UPDATEBUSINESSINFOREQUEST']._serialized_start = 1143
    _globals['_UPDATEBUSINESSINFOREQUEST']._serialized_end = 1304
    _globals['_BUSINESSINFOSERVICE']._serialized_start = 1307
    _globals['_BUSINESSINFOSERVICE']._serialized_end = 1845