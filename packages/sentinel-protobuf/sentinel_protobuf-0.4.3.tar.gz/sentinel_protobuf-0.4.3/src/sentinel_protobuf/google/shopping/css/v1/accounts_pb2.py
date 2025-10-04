"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/css/v1/accounts.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/shopping/css/v1/accounts.proto\x12\x16google.shopping.css.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xc9\x01\n\x18ListChildAccountsRequest\x122\n\x06parent\x18\x01 \x01(\tB"\xe0A\x02\xfaA\x1c\n\x1acss.googleapis.com/Account\x12\x15\n\x08label_id\x18\x02 \x01(\x03H\x00\x88\x01\x01\x12\x16\n\tfull_name\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x16\n\tpage_size\x18\x04 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x05 \x01(\tB\x03\xe0A\x01B\x0b\n\t_label_idB\x0c\n\n_full_name"g\n\x19ListChildAccountsResponse\x121\n\x08accounts\x18\x01 \x03(\x0b2\x1f.google.shopping.css.v1.Account\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x89\x01\n\x11GetAccountRequest\x120\n\x04name\x18\x01 \x01(\tB"\xe0A\x02\xfaA\x1c\n\x1acss.googleapis.com/Account\x127\n\x06parent\x18\x02 \x01(\tB"\xe0A\x01\xfaA\x1c\n\x1acss.googleapis.com/AccountH\x00\x88\x01\x01B\t\n\x07_parent"\xa5\x01\n\x1aUpdateAccountLabelsRequest\x120\n\x04name\x18\x01 \x01(\tB"\xe0A\x02\xfaA\x1c\n\x1acss.googleapis.com/Account\x12\x11\n\tlabel_ids\x18\x02 \x03(\x03\x127\n\x06parent\x18\x03 \x01(\tB"\xe0A\x01\xfaA\x1c\n\x1acss.googleapis.com/AccountH\x00\x88\x01\x01B\t\n\x07_parent"\xbb\x04\n\x07Account\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\tfull_name\x18\x02 \x01(\tB\x06\xe0A\x03\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tH\x00\x88\x01\x01\x12!\n\x0chomepage_uri\x18\x04 \x01(\tB\x06\xe0A\x03\xe0A\x05H\x01\x88\x01\x01\x12\x13\n\x06parent\x18\x05 \x01(\tH\x02\x88\x01\x01\x12\x11\n\tlabel_ids\x18\x06 \x03(\x03\x12\x1b\n\x13automatic_label_ids\x18\x07 \x03(\x03\x12F\n\x0caccount_type\x18\x08 \x01(\x0e2+.google.shopping.css.v1.Account.AccountTypeB\x03\xe0A\x03"\xc6\x01\n\x0bAccountType\x12\x1c\n\x18ACCOUNT_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tCSS_GROUP\x10\x01\x12\x0e\n\nCSS_DOMAIN\x10\x02\x12\x16\n\x12MC_PRIMARY_CSS_MCA\x10\x03\x12\x0e\n\nMC_CSS_MCA\x10\x04\x12\x16\n\x12MC_MARKETPLACE_MCA\x10\x05\x12\x10\n\x0cMC_OTHER_MCA\x10\x06\x12\x11\n\rMC_STANDALONE\x10\x07\x12\x15\n\x11MC_MCA_SUBACCOUNT\x10\x08:F\xeaAC\n\x1acss.googleapis.com/Account\x12\x12accounts/{account}*\x08accounts2\x07accountB\x0f\n\r_display_nameB\x0f\n\r_homepage_uriB\t\n\x07_parent2\xa5\x04\n\x0fAccountsService\x12\xb4\x01\n\x11ListChildAccounts\x120.google.shopping.css.v1.ListChildAccountsRequest\x1a1.google.shopping.css.v1.ListChildAccountsResponse":\xdaA\x06parent\x82\xd3\xe4\x93\x02+\x12)/v1/{parent=accounts/*}:listChildAccounts\x12~\n\nGetAccount\x12).google.shopping.css.v1.GetAccountRequest\x1a\x1f.google.shopping.css.v1.Account"$\xdaA\x04name\x82\xd3\xe4\x93\x02\x17\x12\x15/v1/{name=accounts/*}\x12\x99\x01\n\x0cUpdateLabels\x122.google.shopping.css.v1.UpdateAccountLabelsRequest\x1a\x1f.google.shopping.css.v1.Account"4\xdaA\x04name\x82\xd3\xe4\x93\x02\'""/v1/{name=accounts/*}:updateLabels:\x01*\x1a?\xcaA\x12css.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xaf\x01\n\x1acom.google.shopping.css.v1B\rAccountsProtoP\x01Z2cloud.google.com/go/shopping/css/apiv1/csspb;csspb\xaa\x02\x16Google.Shopping.Css.V1\xca\x02\x16Google\\Shopping\\Css\\V1\xea\x02\x19Google::Shopping::Css::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.css.v1.accounts_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.shopping.css.v1B\rAccountsProtoP\x01Z2cloud.google.com/go/shopping/css/apiv1/csspb;csspb\xaa\x02\x16Google.Shopping.Css.V1\xca\x02\x16Google\\Shopping\\Css\\V1\xea\x02\x19Google::Shopping::Css::V1'
    _globals['_LISTCHILDACCOUNTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCHILDACCOUNTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1c\n\x1acss.googleapis.com/Account'
    _globals['_LISTCHILDACCOUNTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCHILDACCOUNTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCHILDACCOUNTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCHILDACCOUNTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETACCOUNTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETACCOUNTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1c\n\x1acss.googleapis.com/Account'
    _globals['_GETACCOUNTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_GETACCOUNTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x01\xfaA\x1c\n\x1acss.googleapis.com/Account'
    _globals['_UPDATEACCOUNTLABELSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATEACCOUNTLABELSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1c\n\x1acss.googleapis.com/Account'
    _globals['_UPDATEACCOUNTLABELSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_UPDATEACCOUNTLABELSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x01\xfaA\x1c\n\x1acss.googleapis.com/Account'
    _globals['_ACCOUNT'].fields_by_name['full_name']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['full_name']._serialized_options = b'\xe0A\x03\xe0A\x05'
    _globals['_ACCOUNT'].fields_by_name['homepage_uri']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['homepage_uri']._serialized_options = b'\xe0A\x03\xe0A\x05'
    _globals['_ACCOUNT'].fields_by_name['account_type']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['account_type']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNT']._loaded_options = None
    _globals['_ACCOUNT']._serialized_options = b'\xeaAC\n\x1acss.googleapis.com/Account\x12\x12accounts/{account}*\x08accounts2\x07account'
    _globals['_ACCOUNTSSERVICE']._loaded_options = None
    _globals['_ACCOUNTSSERVICE']._serialized_options = b"\xcaA\x12css.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_ACCOUNTSSERVICE'].methods_by_name['ListChildAccounts']._loaded_options = None
    _globals['_ACCOUNTSSERVICE'].methods_by_name['ListChildAccounts']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02+\x12)/v1/{parent=accounts/*}:listChildAccounts'
    _globals['_ACCOUNTSSERVICE'].methods_by_name['GetAccount']._loaded_options = None
    _globals['_ACCOUNTSSERVICE'].methods_by_name['GetAccount']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x17\x12\x15/v1/{name=accounts/*}'
    _globals['_ACCOUNTSSERVICE'].methods_by_name['UpdateLabels']._loaded_options = None
    _globals['_ACCOUNTSSERVICE'].methods_by_name['UpdateLabels']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\'""/v1/{name=accounts/*}:updateLabels:\x01*'
    _globals['_LISTCHILDACCOUNTSREQUEST']._serialized_start = 181
    _globals['_LISTCHILDACCOUNTSREQUEST']._serialized_end = 382
    _globals['_LISTCHILDACCOUNTSRESPONSE']._serialized_start = 384
    _globals['_LISTCHILDACCOUNTSRESPONSE']._serialized_end = 487
    _globals['_GETACCOUNTREQUEST']._serialized_start = 490
    _globals['_GETACCOUNTREQUEST']._serialized_end = 627
    _globals['_UPDATEACCOUNTLABELSREQUEST']._serialized_start = 630
    _globals['_UPDATEACCOUNTLABELSREQUEST']._serialized_end = 795
    _globals['_ACCOUNT']._serialized_start = 798
    _globals['_ACCOUNT']._serialized_end = 1369
    _globals['_ACCOUNT_ACCOUNTTYPE']._serialized_start = 1054
    _globals['_ACCOUNT_ACCOUNTTYPE']._serialized_end = 1252
    _globals['_ACCOUNTSSERVICE']._serialized_start = 1372
    _globals['_ACCOUNTSSERVICE']._serialized_end = 1921