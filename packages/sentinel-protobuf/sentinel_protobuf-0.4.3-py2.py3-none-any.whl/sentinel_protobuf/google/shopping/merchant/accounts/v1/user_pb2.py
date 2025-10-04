"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1/user.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.shopping.merchant.accounts.v1 import accessright_pb2 as google_dot_shopping_dot_merchant_dot_accounts_dot_v1_dot_accessright__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/shopping/merchant/accounts/v1/user.proto\x12$google.shopping.merchant.accounts.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a6google/shopping/merchant/accounts/v1/accessright.proto"\xbe\x02\n\x04User\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12D\n\x05state\x18\x02 \x01(\x0e20.google.shopping.merchant.accounts.v1.User.StateB\x03\xe0A\x03\x12M\n\raccess_rights\x18\x04 \x03(\x0e21.google.shopping.merchant.accounts.v1.AccessRightB\x03\xe0A\x02"9\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0c\n\x08VERIFIED\x10\x02:S\xeaAP\n\x1fmerchantapi.googleapis.com/User\x12 accounts/{account}/users/{email}*\x05users2\x04user"G\n\x0eGetUserRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fmerchantapi.googleapis.com/User"\xa4\x01\n\x11CreateUserRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12\x14\n\x07user_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12=\n\x04user\x18\x03 \x01(\x0b2*.google.shopping.merchant.accounts.v1.UserB\x03\xe0A\x01"J\n\x11DeleteUserRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fmerchantapi.googleapis.com/User"\x88\x01\n\x11UpdateUserRequest\x12=\n\x04user\x18\x01 \x01(\x0b2*.google.shopping.merchant.accounts.v1.UserB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\x7f\n\x10ListUsersRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"g\n\x11ListUsersResponse\x129\n\x05users\x18\x01 \x03(\x0b2*.google.shopping.merchant.accounts.v1.User\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xcc\x07\n\x0bUserService\x12\xa2\x01\n\x07GetUser\x124.google.shopping.merchant.accounts.v1.GetUserRequest\x1a*.google.shopping.merchant.accounts.v1.User"5\xdaA\x04name\x82\xd3\xe4\x93\x02(\x12&/accounts/v1/{name=accounts/*/users/*}\x12\xbd\x01\n\nCreateUser\x127.google.shopping.merchant.accounts.v1.CreateUserRequest\x1a*.google.shopping.merchant.accounts.v1.User"J\xdaA\x13parent,user,user_id\x82\xd3\xe4\x93\x02."&/accounts/v1/{parent=accounts/*}/users:\x04user\x12\x94\x01\n\nDeleteUser\x127.google.shopping.merchant.accounts.v1.DeleteUserRequest\x1a\x16.google.protobuf.Empty"5\xdaA\x04name\x82\xd3\xe4\x93\x02(*&/accounts/v1/{name=accounts/*/users/*}\x12\xbf\x01\n\nUpdateUser\x127.google.shopping.merchant.accounts.v1.UpdateUserRequest\x1a*.google.shopping.merchant.accounts.v1.User"L\xdaA\x10user,update_mask\x82\xd3\xe4\x93\x0232+/accounts/v1/{user.name=accounts/*/users/*}:\x04user\x12\xb5\x01\n\tListUsers\x126.google.shopping.merchant.accounts.v1.ListUsersRequest\x1a7.google.shopping.merchant.accounts.v1.ListUsersResponse"7\xdaA\x06parent\x82\xd3\xe4\x93\x02(\x12&/accounts/v1/{parent=accounts/*}/users\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xfc\x01\n(com.google.shopping.merchant.accounts.v1B\tUserProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1.user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.shopping.merchant.accounts.v1B\tUserProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1'
    _globals['_USER'].fields_by_name['name']._loaded_options = None
    _globals['_USER'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_USER'].fields_by_name['state']._loaded_options = None
    _globals['_USER'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_USER'].fields_by_name['access_rights']._loaded_options = None
    _globals['_USER'].fields_by_name['access_rights']._serialized_options = b'\xe0A\x02'
    _globals['_USER']._loaded_options = None
    _globals['_USER']._serialized_options = b'\xeaAP\n\x1fmerchantapi.googleapis.com/User\x12 accounts/{account}/users/{email}*\x05users2\x04user'
    _globals['_GETUSERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETUSERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fmerchantapi.googleapis.com/User'
    _globals['_CREATEUSERREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEUSERREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_CREATEUSERREQUEST'].fields_by_name['user_id']._loaded_options = None
    _globals['_CREATEUSERREQUEST'].fields_by_name['user_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEUSERREQUEST'].fields_by_name['user']._loaded_options = None
    _globals['_CREATEUSERREQUEST'].fields_by_name['user']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEUSERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEUSERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fmerchantapi.googleapis.com/User'
    _globals['_UPDATEUSERREQUEST'].fields_by_name['user']._loaded_options = None
    _globals['_UPDATEUSERREQUEST'].fields_by_name['user']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEUSERREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEUSERREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_LISTUSERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTUSERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_LISTUSERSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTUSERSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTUSERSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTUSERSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_USERSERVICE']._loaded_options = None
    _globals['_USERSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_USERSERVICE'].methods_by_name['GetUser']._loaded_options = None
    _globals['_USERSERVICE'].methods_by_name['GetUser']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02(\x12&/accounts/v1/{name=accounts/*/users/*}'
    _globals['_USERSERVICE'].methods_by_name['CreateUser']._loaded_options = None
    _globals['_USERSERVICE'].methods_by_name['CreateUser']._serialized_options = b'\xdaA\x13parent,user,user_id\x82\xd3\xe4\x93\x02."&/accounts/v1/{parent=accounts/*}/users:\x04user'
    _globals['_USERSERVICE'].methods_by_name['DeleteUser']._loaded_options = None
    _globals['_USERSERVICE'].methods_by_name['DeleteUser']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02(*&/accounts/v1/{name=accounts/*/users/*}'
    _globals['_USERSERVICE'].methods_by_name['UpdateUser']._loaded_options = None
    _globals['_USERSERVICE'].methods_by_name['UpdateUser']._serialized_options = b'\xdaA\x10user,update_mask\x82\xd3\xe4\x93\x0232+/accounts/v1/{user.name=accounts/*/users/*}:\x04user'
    _globals['_USERSERVICE'].methods_by_name['ListUsers']._loaded_options = None
    _globals['_USERSERVICE'].methods_by_name['ListUsers']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02(\x12&/accounts/v1/{parent=accounts/*}/users'
    _globals['_USER']._serialized_start = 324
    _globals['_USER']._serialized_end = 642
    _globals['_USER_STATE']._serialized_start = 500
    _globals['_USER_STATE']._serialized_end = 557
    _globals['_GETUSERREQUEST']._serialized_start = 644
    _globals['_GETUSERREQUEST']._serialized_end = 715
    _globals['_CREATEUSERREQUEST']._serialized_start = 718
    _globals['_CREATEUSERREQUEST']._serialized_end = 882
    _globals['_DELETEUSERREQUEST']._serialized_start = 884
    _globals['_DELETEUSERREQUEST']._serialized_end = 958
    _globals['_UPDATEUSERREQUEST']._serialized_start = 961
    _globals['_UPDATEUSERREQUEST']._serialized_end = 1097
    _globals['_LISTUSERSREQUEST']._serialized_start = 1099
    _globals['_LISTUSERSREQUEST']._serialized_end = 1226
    _globals['_LISTUSERSRESPONSE']._serialized_start = 1228
    _globals['_LISTUSERSRESPONSE']._serialized_end = 1331
    _globals['_USERSERVICE']._serialized_start = 1334
    _globals['_USERSERVICE']._serialized_end = 2306