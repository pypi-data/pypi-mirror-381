"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1beta/gbpaccounts.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/shopping/merchant/accounts/v1beta/gbpaccounts.proto\x12(google.shopping.merchant.accounts.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto"\xe2\x02\n\nGbpAccount\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x16\n\x0egbp_account_id\x18\x02 \x01(\t\x12G\n\x04type\x18\x03 \x01(\x0e29.google.shopping.merchant.accounts.v1beta.GbpAccount.Type\x12\x18\n\x10gbp_account_name\x18\x05 \x01(\t\x12\x15\n\rlisting_count\x18\x06 \x01(\x03"<\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04USER\x10\x01\x12\x14\n\x10BUSINESS_ACCOUNT\x10\x02:q\xeaAn\n%merchantapi.googleapis.com/GbpAccount\x12,accounts/{account}/gbpAccounts/{gbp_account}*\x0bgbpAccounts2\ngbpAccount"\x85\x01\n\x16ListGbpAccountsRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"~\n\x17ListGbpAccountsResponse\x12J\n\x0cgbp_accounts\x18\x01 \x03(\x0b24.google.shopping.merchant.accounts.v1beta.GbpAccount\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"k\n\x15LinkGbpAccountRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12\x16\n\tgbp_email\x18\x02 \x01(\tB\x03\xe0A\x02"B\n\x16LinkGbpAccountResponse\x12(\n\x08response\x18\x01 \x01(\x0b2\x16.google.protobuf.Empty2\xa4\x04\n\x12GbpAccountsService\x12\xd9\x01\n\x0fListGbpAccounts\x12@.google.shopping.merchant.accounts.v1beta.ListGbpAccountsRequest\x1aA.google.shopping.merchant.accounts.v1beta.ListGbpAccountsResponse"A\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/accounts/v1beta/{parent=accounts/*}/gbpAccounts\x12\xe8\x01\n\x0eLinkGbpAccount\x12?.google.shopping.merchant.accounts.v1beta.LinkGbpAccountRequest\x1a@.google.shopping.merchant.accounts.v1beta.LinkGbpAccountResponse"S\xdaA\x06parent\x82\xd3\xe4\x93\x02D"?/accounts/v1beta/{parent=accounts/*}/gbpAccounts:linkGbpAccount:\x01*\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x92\x01\n,com.google.shopping.merchant.accounts.v1betaB\x10GbpAccountsProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1beta.gbpaccounts_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.shopping.merchant.accounts.v1betaB\x10GbpAccountsProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspb'
    _globals['_GBPACCOUNT'].fields_by_name['name']._loaded_options = None
    _globals['_GBPACCOUNT'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_GBPACCOUNT']._loaded_options = None
    _globals['_GBPACCOUNT']._serialized_options = b'\xeaAn\n%merchantapi.googleapis.com/GbpAccount\x12,accounts/{account}/gbpAccounts/{gbp_account}*\x0bgbpAccounts2\ngbpAccount'
    _globals['_LISTGBPACCOUNTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTGBPACCOUNTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_LISTGBPACCOUNTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTGBPACCOUNTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTGBPACCOUNTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTGBPACCOUNTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LINKGBPACCOUNTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LINKGBPACCOUNTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_LINKGBPACCOUNTREQUEST'].fields_by_name['gbp_email']._loaded_options = None
    _globals['_LINKGBPACCOUNTREQUEST'].fields_by_name['gbp_email']._serialized_options = b'\xe0A\x02'
    _globals['_GBPACCOUNTSSERVICE']._loaded_options = None
    _globals['_GBPACCOUNTSSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_GBPACCOUNTSSERVICE'].methods_by_name['ListGbpAccounts']._loaded_options = None
    _globals['_GBPACCOUNTSSERVICE'].methods_by_name['ListGbpAccounts']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/accounts/v1beta/{parent=accounts/*}/gbpAccounts'
    _globals['_GBPACCOUNTSSERVICE'].methods_by_name['LinkGbpAccount']._loaded_options = None
    _globals['_GBPACCOUNTSSERVICE'].methods_by_name['LinkGbpAccount']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02D"?/accounts/v1beta/{parent=accounts/*}/gbpAccounts:linkGbpAccount:\x01*'
    _globals['_GBPACCOUNT']._serialized_start = 249
    _globals['_GBPACCOUNT']._serialized_end = 603
    _globals['_GBPACCOUNT_TYPE']._serialized_start = 428
    _globals['_GBPACCOUNT_TYPE']._serialized_end = 488
    _globals['_LISTGBPACCOUNTSREQUEST']._serialized_start = 606
    _globals['_LISTGBPACCOUNTSREQUEST']._serialized_end = 739
    _globals['_LISTGBPACCOUNTSRESPONSE']._serialized_start = 741
    _globals['_LISTGBPACCOUNTSRESPONSE']._serialized_end = 867
    _globals['_LINKGBPACCOUNTREQUEST']._serialized_start = 869
    _globals['_LINKGBPACCOUNTREQUEST']._serialized_end = 976
    _globals['_LINKGBPACCOUNTRESPONSE']._serialized_start = 978
    _globals['_LINKGBPACCOUNTRESPONSE']._serialized_end = 1044
    _globals['_GBPACCOUNTSSERVICE']._serialized_start = 1047
    _globals['_GBPACCOUNTSSERVICE']._serialized_end = 1595