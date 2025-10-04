"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1beta/accounts.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.shopping.merchant.accounts.v1beta import accountservices_pb2 as google_dot_shopping_dot_merchant_dot_accounts_dot_v1beta_dot_accountservices__pb2
from ......google.shopping.merchant.accounts.v1beta import user_pb2 as google_dot_shopping_dot_merchant_dot_accounts_dot_v1beta_dot_user__pb2
from ......google.type import datetime_pb2 as google_dot_type_dot_datetime__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/shopping/merchant/accounts/v1beta/accounts.proto\x12(google.shopping.merchant.accounts.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a>google/shopping/merchant/accounts/v1beta/accountservices.proto\x1a3google/shopping/merchant/accounts/v1beta/user.proto\x1a\x1agoogle/type/datetime.proto"\x8a\x02\n\x07Account\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x17\n\naccount_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x19\n\x0caccount_name\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x15\n\radult_content\x18\x04 \x01(\x08\x12\x19\n\x0ctest_account\x18\x05 \x01(\x08B\x03\xe0A\x03\x12-\n\ttime_zone\x18\x06 \x01(\x0b2\x15.google.type.TimeZoneB\x03\xe0A\x02\x12\x1a\n\rlanguage_code\x18\x07 \x01(\tB\x03\xe0A\x02:;\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}"M\n\x11GetAccountRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account"\x9f\x06\n CreateAndConfigureAccountRequest\x12G\n\x07account\x18\x01 \x01(\x0b21.google.shopping.merchant.accounts.v1beta.AccountB\x03\xe0A\x02\x12O\n\x05users\x18\x02 \x03(\x0b2;.google.shopping.merchant.accounts.v1beta.CreateUserRequestB\x03\xe0A\x01\x12\x8a\x01\n\x17accept_terms_of_service\x18\x03 \x01(\x0b2_.google.shopping.merchant.accounts.v1beta.CreateAndConfigureAccountRequest.AcceptTermsOfServiceB\x03\xe0A\x01H\x00\x88\x01\x01\x12r\n\x07service\x18\x04 \x03(\x0b2\\.google.shopping.merchant.accounts.v1beta.CreateAndConfigureAccountRequest.AddAccountServiceB\x03\xe0A\x02\x1aq\n\x14AcceptTermsOfService\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/TermsOfService\x12\x18\n\x0bregion_code\x18\x03 \x01(\tB\x03\xe0A\x02\x1a\xd0\x01\n\x11AddAccountService\x12[\n\x13account_aggregation\x18g \x01(\x0b2<.google.shopping.merchant.accounts.v1beta.AccountAggregationH\x00\x12A\n\x08provider\x18\x01 \x01(\tB*\xe0A\x01\xfaA$\n"merchantapi.googleapis.com/AccountH\x01\x88\x01\x01B\x0e\n\x0cservice_typeB\x0b\n\t_providerB\x1a\n\x18_accept_terms_of_service"d\n\x14DeleteAccountRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12\x12\n\x05force\x18\x02 \x01(\x08B\x03\xe0A\x01"\x95\x01\n\x14UpdateAccountRequest\x12G\n\x07account\x18\x01 \x01(\x0b21.google.shopping.merchant.accounts.v1beta.AccountB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"[\n\x13ListAccountsRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x03 \x01(\tB\x03\xe0A\x01"t\n\x14ListAccountsResponse\x12C\n\x08accounts\x18\x01 \x03(\x0b21.google.shopping.merchant.accounts.v1beta.Account\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x87\x01\n\x16ListSubAccountsRequest\x12<\n\x08provider\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"w\n\x17ListSubAccountsResponse\x12C\n\x08accounts\x18\x01 \x03(\x0b21.google.shopping.merchant.accounts.v1beta.Account\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xee\t\n\x0fAccountsService\x12\xaf\x01\n\nGetAccount\x12;.google.shopping.merchant.accounts.v1beta.GetAccountRequest\x1a1.google.shopping.merchant.accounts.v1beta.Account"1\xdaA\x04name\x82\xd3\xe4\x93\x02$\x12"/accounts/v1beta/{name=accounts/*}\x12\xd3\x01\n\x19CreateAndConfigureAccount\x12J.google.shopping.merchant.accounts.v1beta.CreateAndConfigureAccountRequest\x1a1.google.shopping.merchant.accounts.v1beta.Account"7\x82\xd3\xe4\x93\x021",/accounts/v1beta/accounts:createAndConfigure:\x01*\x12\x9a\x01\n\rDeleteAccount\x12>.google.shopping.merchant.accounts.v1beta.DeleteAccountRequest\x1a\x16.google.protobuf.Empty"1\xdaA\x04name\x82\xd3\xe4\x93\x02$*"/accounts/v1beta/{name=accounts/*}\x12\xd5\x01\n\rUpdateAccount\x12>.google.shopping.merchant.accounts.v1beta.UpdateAccountRequest\x1a1.google.shopping.merchant.accounts.v1beta.Account"Q\xdaA\x13account,update_mask\x82\xd3\xe4\x93\x0252*/accounts/v1beta/{account.name=accounts/*}:\x07account\x12\xb0\x01\n\x0cListAccounts\x12=.google.shopping.merchant.accounts.v1beta.ListAccountsRequest\x1a>.google.shopping.merchant.accounts.v1beta.ListAccountsResponse"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/accounts/v1beta/accounts\x12\xe1\x01\n\x0fListSubAccounts\x12@.google.shopping.merchant.accounts.v1beta.ListSubAccountsRequest\x1aA.google.shopping.merchant.accounts.v1beta.ListSubAccountsResponse"I\xdaA\x08provider\x82\xd3\xe4\x93\x028\x126/accounts/v1beta/{provider=accounts/*}:listSubaccounts\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x8f\x01\n,com.google.shopping.merchant.accounts.v1betaB\rAccountsProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1beta.accounts_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.shopping.merchant.accounts.v1betaB\rAccountsProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspb'
    _globals['_ACCOUNT'].fields_by_name['name']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ACCOUNT'].fields_by_name['account_id']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['account_id']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNT'].fields_by_name['account_name']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['account_name']._serialized_options = b'\xe0A\x02'
    _globals['_ACCOUNT'].fields_by_name['test_account']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['test_account']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNT'].fields_by_name['time_zone']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x02'
    _globals['_ACCOUNT'].fields_by_name['language_code']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['language_code']._serialized_options = b'\xe0A\x02'
    _globals['_ACCOUNT']._loaded_options = None
    _globals['_ACCOUNT']._serialized_options = b'\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}'
    _globals['_GETACCOUNTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETACCOUNTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST_ACCEPTTERMSOFSERVICE'].fields_by_name['name']._loaded_options = None
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST_ACCEPTTERMSOFSERVICE'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/TermsOfService'
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST_ACCEPTTERMSOFSERVICE'].fields_by_name['region_code']._loaded_options = None
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST_ACCEPTTERMSOFSERVICE'].fields_by_name['region_code']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST_ADDACCOUNTSERVICE'].fields_by_name['provider']._loaded_options = None
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST_ADDACCOUNTSERVICE'].fields_by_name['provider']._serialized_options = b'\xe0A\x01\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST'].fields_by_name['account']._loaded_options = None
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST'].fields_by_name['account']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST'].fields_by_name['users']._loaded_options = None
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST'].fields_by_name['users']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST'].fields_by_name['accept_terms_of_service']._loaded_options = None
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST'].fields_by_name['accept_terms_of_service']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST'].fields_by_name['service']._loaded_options = None
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST'].fields_by_name['service']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEACCOUNTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEACCOUNTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_DELETEACCOUNTREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETEACCOUNTREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEACCOUNTREQUEST'].fields_by_name['account']._loaded_options = None
    _globals['_UPDATEACCOUNTREQUEST'].fields_by_name['account']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEACCOUNTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEACCOUNTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
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
    _globals['_ACCOUNTSSERVICE'].methods_by_name['GetAccount']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02$\x12"/accounts/v1beta/{name=accounts/*}'
    _globals['_ACCOUNTSSERVICE'].methods_by_name['CreateAndConfigureAccount']._loaded_options = None
    _globals['_ACCOUNTSSERVICE'].methods_by_name['CreateAndConfigureAccount']._serialized_options = b'\x82\xd3\xe4\x93\x021",/accounts/v1beta/accounts:createAndConfigure:\x01*'
    _globals['_ACCOUNTSSERVICE'].methods_by_name['DeleteAccount']._loaded_options = None
    _globals['_ACCOUNTSSERVICE'].methods_by_name['DeleteAccount']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02$*"/accounts/v1beta/{name=accounts/*}'
    _globals['_ACCOUNTSSERVICE'].methods_by_name['UpdateAccount']._loaded_options = None
    _globals['_ACCOUNTSSERVICE'].methods_by_name['UpdateAccount']._serialized_options = b'\xdaA\x13account,update_mask\x82\xd3\xe4\x93\x0252*/accounts/v1beta/{account.name=accounts/*}:\x07account'
    _globals['_ACCOUNTSSERVICE'].methods_by_name['ListAccounts']._loaded_options = None
    _globals['_ACCOUNTSSERVICE'].methods_by_name['ListAccounts']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b\x12\x19/accounts/v1beta/accounts'
    _globals['_ACCOUNTSSERVICE'].methods_by_name['ListSubAccounts']._loaded_options = None
    _globals['_ACCOUNTSSERVICE'].methods_by_name['ListSubAccounts']._serialized_options = b'\xdaA\x08provider\x82\xd3\xe4\x93\x028\x126/accounts/v1beta/{provider=accounts/*}:listSubaccounts'
    _globals['_ACCOUNT']._serialized_start = 425
    _globals['_ACCOUNT']._serialized_end = 691
    _globals['_GETACCOUNTREQUEST']._serialized_start = 693
    _globals['_GETACCOUNTREQUEST']._serialized_end = 770
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST']._serialized_start = 773
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST']._serialized_end = 1572
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST_ACCEPTTERMSOFSERVICE']._serialized_start = 1220
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST_ACCEPTTERMSOFSERVICE']._serialized_end = 1333
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST_ADDACCOUNTSERVICE']._serialized_start = 1336
    _globals['_CREATEANDCONFIGUREACCOUNTREQUEST_ADDACCOUNTSERVICE']._serialized_end = 1544
    _globals['_DELETEACCOUNTREQUEST']._serialized_start = 1574
    _globals['_DELETEACCOUNTREQUEST']._serialized_end = 1674
    _globals['_UPDATEACCOUNTREQUEST']._serialized_start = 1677
    _globals['_UPDATEACCOUNTREQUEST']._serialized_end = 1826
    _globals['_LISTACCOUNTSREQUEST']._serialized_start = 1828
    _globals['_LISTACCOUNTSREQUEST']._serialized_end = 1919
    _globals['_LISTACCOUNTSRESPONSE']._serialized_start = 1921
    _globals['_LISTACCOUNTSRESPONSE']._serialized_end = 2037
    _globals['_LISTSUBACCOUNTSREQUEST']._serialized_start = 2040
    _globals['_LISTSUBACCOUNTSREQUEST']._serialized_end = 2175
    _globals['_LISTSUBACCOUNTSRESPONSE']._serialized_start = 2177
    _globals['_LISTSUBACCOUNTSRESPONSE']._serialized_end = 2296
    _globals['_ACCOUNTSSERVICE']._serialized_start = 2299
    _globals['_ACCOUNTSSERVICE']._serialized_end = 3561