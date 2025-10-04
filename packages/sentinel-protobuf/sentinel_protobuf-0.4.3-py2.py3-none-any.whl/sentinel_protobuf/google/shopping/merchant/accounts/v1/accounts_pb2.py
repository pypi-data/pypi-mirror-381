"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1/accounts.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.shopping.merchant.accounts.v1 import accountservices_pb2 as google_dot_shopping_dot_merchant_dot_accounts_dot_v1_dot_accountservices__pb2
from ......google.shopping.merchant.accounts.v1 import user_pb2 as google_dot_shopping_dot_merchant_dot_accounts_dot_v1_dot_user__pb2
from ......google.type import datetime_pb2 as google_dot_type_dot_datetime__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/shopping/merchant/accounts/v1/accounts.proto\x12$google.shopping.merchant.accounts.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a:google/shopping/merchant/accounts/v1/accountservices.proto\x1a/google/shopping/merchant/accounts/v1/user.proto\x1a\x1agoogle/type/datetime.proto"\xb9\x02\n\x07Account\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x17\n\naccount_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x19\n\x0caccount_name\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x1f\n\radult_content\x18\x04 \x01(\x08B\x03\xe0A\x01H\x00\x88\x01\x01\x12\x19\n\x0ctest_account\x18\x05 \x01(\x08B\x03\xe0A\x03\x12-\n\ttime_zone\x18\x06 \x01(\x0b2\x15.google.type.TimeZoneB\x03\xe0A\x02\x12\x1a\n\rlanguage_code\x18\x07 \x01(\tB\x03\xe0A\x02:N\xeaAK\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}*\x08accounts2\x07accountB\x10\n\x0e_adult_content"M\n\x11GetAccountRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account"\xc2\x04\n CreateAndConfigureAccountRequest\x12C\n\x07account\x18\x01 \x01(\x0b2-.google.shopping.merchant.accounts.v1.AccountB\x03\xe0A\x02\x12a\n\x04user\x18\x03 \x03(\x0b2N.google.shopping.merchant.accounts.v1.CreateAndConfigureAccountRequest.AddUserB\x03\xe0A\x01\x12n\n\x07service\x18\x04 \x03(\x0b2X.google.shopping.merchant.accounts.v1.CreateAndConfigureAccountRequest.AddAccountServiceB\x03\xe0A\x02\x1a^\n\x07AddUser\x12\x14\n\x07user_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12=\n\x04user\x18\x02 \x01(\x0b2*.google.shopping.merchant.accounts.v1.UserB\x03\xe0A\x01\x1a\xa5\x01\n\x11AddAccountService\x12W\n\x13account_aggregation\x18g \x01(\x0b28.google.shopping.merchant.accounts.v1.AccountAggregationH\x00\x12\x1a\n\x08provider\x18\x01 \x01(\tB\x03\xe0A\x02H\x01\x88\x01\x01B\x0e\n\x0cservice_typeB\x0b\n\t_provider"d\n\x14DeleteAccountRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12\x12\n\x05force\x18\x02 \x01(\x08B\x03\xe0A\x01"\x91\x01\n\x14UpdateAccountRequest\x12C\n\x07account\x18\x01 \x01(\x0b2-.google.shopping.merchant.accounts.v1.AccountB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"[\n\x13ListAccountsRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x03 \x01(\tB\x03\xe0A\x01"p\n\x14ListAccountsResponse\x12?\n\x08accounts\x18\x01 \x03(\x0b2-.google.shopping.merchant.accounts.v1.Account\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x87\x01\n\x16ListSubAccountsRequest\x12<\n\x08provider\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"s\n\x17ListSubAccountsResponse\x12?\n\x08accounts\x18\x01 \x03(\x0b2-.google.shopping.merchant.accounts.v1.Account\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xaa\t\n\x0fAccountsService\x12\xa3\x01\n\nGetAccount\x127.google.shopping.merchant.accounts.v1.GetAccountRequest\x1a-.google.shopping.merchant.accounts.v1.Account"-\xdaA\x04name\x82\xd3\xe4\x93\x02 \x12\x1e/accounts/v1/{name=accounts/*}\x12\xc7\x01\n\x19CreateAndConfigureAccount\x12F.google.shopping.merchant.accounts.v1.CreateAndConfigureAccountRequest\x1a-.google.shopping.merchant.accounts.v1.Account"3\x82\xd3\xe4\x93\x02-"(/accounts/v1/accounts:createAndConfigure:\x01*\x12\x92\x01\n\rDeleteAccount\x12:.google.shopping.merchant.accounts.v1.DeleteAccountRequest\x1a\x16.google.protobuf.Empty"-\xdaA\x04name\x82\xd3\xe4\x93\x02 *\x1e/accounts/v1/{name=accounts/*}\x12\xc9\x01\n\rUpdateAccount\x12:.google.shopping.merchant.accounts.v1.UpdateAccountRequest\x1a-.google.shopping.merchant.accounts.v1.Account"M\xdaA\x13account,update_mask\x82\xd3\xe4\x93\x0212&/accounts/v1/{account.name=accounts/*}:\x07account\x12\xa4\x01\n\x0cListAccounts\x129.google.shopping.merchant.accounts.v1.ListAccountsRequest\x1a:.google.shopping.merchant.accounts.v1.ListAccountsResponse"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/accounts/v1/accounts\x12\xd5\x01\n\x0fListSubAccounts\x12<.google.shopping.merchant.accounts.v1.ListSubAccountsRequest\x1a=.google.shopping.merchant.accounts.v1.ListSubAccountsResponse"E\xdaA\x08provider\x82\xd3\xe4\x93\x024\x122/accounts/v1/{provider=accounts/*}:listSubaccounts\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x80\x02\n(com.google.shopping.merchant.accounts.v1B\rAccountsProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1.accounts_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.shopping.merchant.accounts.v1B\rAccountsProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1'
    _globals['_ACCOUNT'].fields_by_name['name']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ACCOUNT'].fields_by_name['account_id']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['account_id']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNT'].fields_by_name['account_name']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['account_name']._serialized_options = b'\xe0A\x02'
    _globals['_ACCOUNT'].fields_by_name['adult_content']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['adult_content']._serialized_options = b'\xe0A\x01'
    _globals['_ACCOUNT'].fields_by_name['test_account']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['test_account']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNT'].fields_by_name['time_zone']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x02'
    _globals['_ACCOUNT'].fields_by_name['language_code']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['language_code']._serialized_options = b'\xe0A\x02'
    _globals['_ACCOUNT']._loaded_options = None
    _globals['_ACCOUNT']._serialized_options = b'\xeaAK\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}*\x08accounts2\x07account'
    _globals['_GETACCOUNTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETACCOUNTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST_ADDUSER'].fields_by_name['user_id']._loaded_options = None
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST_ADDUSER'].fields_by_name['user_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST_ADDUSER'].fields_by_name['user']._loaded_options = None
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST_ADDUSER'].fields_by_name['user']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST_ADDACCOUNTSERVICE'].fields_by_name['provider']._loaded_options = None
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST_ADDACCOUNTSERVICE'].fields_by_name['provider']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST'].fields_by_name['account']._loaded_options = None
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST'].fields_by_name['account']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST'].fields_by_name['user']._loaded_options = None
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST'].fields_by_name['user']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST'].fields_by_name['service']._loaded_options = None
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST'].fields_by_name['service']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEACCOUNTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEACCOUNTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_DELETEACCOUNTREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETEACCOUNTREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEACCOUNTREQUEST'].fields_by_name['account']._loaded_options = None
    _globals['_UPDATEACCOUNTREQUEST'].fields_by_name['account']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEACCOUNTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEACCOUNTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCOUNTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTACCOUNTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCOUNTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTACCOUNTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCOUNTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTACCOUNTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSUBACCOUNTSREQUEST'].fields_by_name['provider']._loaded_options = None
    _globals['_LISTSUBACCOUNTSREQUEST'].fields_by_name['provider']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_LISTSUBACCOUNTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTSUBACCOUNTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSUBACCOUNTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTSUBACCOUNTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_ACCOUNTSSERVICE']._loaded_options = None
    _globals['_ACCOUNTSSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_ACCOUNTSSERVICE'].methods_by_name['GetAccount']._loaded_options = None
    _globals['_ACCOUNTSSERVICE'].methods_by_name['GetAccount']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02 \x12\x1e/accounts/v1/{name=accounts/*}'
    _globals['_ACCOUNTSSERVICE'].methods_by_name['CreateAndConfigureAccount']._loaded_options = None
    _globals['_ACCOUNTSSERVICE'].methods_by_name['CreateAndConfigureAccount']._serialized_options = b'\x82\xd3\xe4\x93\x02-"(/accounts/v1/accounts:createAndConfigure:\x01*'
    _globals['_ACCOUNTSSERVICE'].methods_by_name['DeleteAccount']._loaded_options = None
    _globals['_ACCOUNTSSERVICE'].methods_by_name['DeleteAccount']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02 *\x1e/accounts/v1/{name=accounts/*}'
    _globals['_ACCOUNTSSERVICE'].methods_by_name['UpdateAccount']._loaded_options = None
    _globals['_ACCOUNTSSERVICE'].methods_by_name['UpdateAccount']._serialized_options = b'\xdaA\x13account,update_mask\x82\xd3\xe4\x93\x0212&/accounts/v1/{account.name=accounts/*}:\x07account'
    _globals['_ACCOUNTSSERVICE'].methods_by_name['ListAccounts']._loaded_options = None
    _globals['_ACCOUNTSSERVICE'].methods_by_name['ListAccounts']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17\x12\x15/accounts/v1/accounts'
    _globals['_ACCOUNTSSERVICE'].methods_by_name['ListSubAccounts']._loaded_options = None
    _globals['_ACCOUNTSSERVICE'].methods_by_name['ListSubAccounts']._serialized_options = b'\xdaA\x08provider\x82\xd3\xe4\x93\x024\x122/accounts/v1/{provider=accounts/*}:listSubaccounts'
    _globals['_ACCOUNT']._serialized_start = 409
    _globals['_ACCOUNT']._serialized_end = 722
    _globals['_GETACCOUNTREQUEST']._serialized_start = 724
    _globals['_GETACCOUNTREQUEST']._serialized_end = 801
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST']._serialized_start = 804
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST']._serialized_end = 1382
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST_ADDUSER']._serialized_start = 1120
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST_ADDUSER']._serialized_end = 1214
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST_ADDACCOUNTSERVICE']._serialized_start = 1217
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST_ADDACCOUNTSERVICE']._serialized_end = 1382
    _globals['_DELETEACCOUNTREQUEST']._serialized_start = 1384
    _globals['_DELETEACCOUNTREQUEST']._serialized_end = 1484
    _globals['_UPDATEACCOUNTREQUEST']._serialized_start = 1487
    _globals['_UPDATEACCOUNTREQUEST']._serialized_end = 1632
    _globals['_LISTACCOUNTSREQUEST']._serialized_start = 1634
    _globals['_LISTACCOUNTSREQUEST']._serialized_end = 1725
    _globals['_LISTACCOUNTSRESPONSE']._serialized_start = 1727
    _globals['_LISTACCOUNTSRESPONSE']._serialized_end = 1839
    _globals['_LISTSUBACCOUNTSREQUEST']._serialized_start = 1842
    _globals['_LISTSUBACCOUNTSREQUEST']._serialized_end = 1977
    _globals['_LISTSUBACCOUNTSRESPONSE']._serialized_start = 1979
    _globals['_LISTSUBACCOUNTSRESPONSE']._serialized_end = 2094
    _globals['_ACCOUNTSSERVICE']._serialized_start = 2097
    _globals['_ACCOUNTSSERVICE']._serialized_end = 3291