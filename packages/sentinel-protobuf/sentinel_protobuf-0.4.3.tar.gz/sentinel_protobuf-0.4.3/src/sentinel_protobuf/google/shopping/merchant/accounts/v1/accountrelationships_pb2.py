"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1/accountrelationships.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/shopping/merchant/accounts/v1/accountrelationships.proto\x12$google.shopping.merchant.accounts.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xa7\x02\n\x13AccountRelationship\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1a\n\x08provider\x18\x02 \x01(\tB\x03\xe0A\x05H\x00\x88\x01\x01\x12"\n\x15provider_display_name\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10account_id_alias\x18\x04 \x01(\tB\x03\xe0A\x01:\x90\x01\xeaA\x8c\x01\n.merchantapi.googleapis.com/AccountRelationship\x12/accounts/{account}/relationships/{relationship}*\x14accountRelationships2\x13accountRelationshipB\x0b\n\t_provider"e\n\x1dGetAccountRelationshipRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.merchantapi.googleapis.com/AccountRelationship"\xb6\x01\n UpdateAccountRelationshipRequest\x12\\\n\x14account_relationship\x18\x01 \x01(\x0b29.google.shopping.merchant.accounts.v1.AccountRelationshipB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\x8e\x01\n\x1fListAccountRelationshipsRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x04 \x01(\x05B\x03\xe0A\x01"\x95\x01\n ListAccountRelationshipsResponse\x12X\n\x15account_relationships\x18\x01 \x03(\x0b29.google.shopping.merchant.accounts.v1.AccountRelationship\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xd5\x06\n\x1bAccountRelationshipsService\x12\xd7\x01\n\x16GetAccountRelationship\x12C.google.shopping.merchant.accounts.v1.GetAccountRelationshipRequest\x1a9.google.shopping.merchant.accounts.v1.AccountRelationship"=\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./accounts/v1/{name=accounts/*/relationships/*}\x12\xa5\x02\n\x19UpdateAccountRelationship\x12F.google.shopping.merchant.accounts.v1.UpdateAccountRelationshipRequest\x1a9.google.shopping.merchant.accounts.v1.AccountRelationship"\x84\x01\xdaA account_relationship,update_mask\x82\xd3\xe4\x93\x02[2C/accounts/v1/{account_relationship.name=accounts/*/relationships/*}:\x14account_relationship\x12\xea\x01\n\x18ListAccountRelationships\x12E.google.shopping.merchant.accounts.v1.ListAccountRelationshipsRequest\x1aF.google.shopping.merchant.accounts.v1.ListAccountRelationshipsResponse"?\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./accounts/v1/{parent=accounts/*}/relationships\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x8c\x02\n(com.google.shopping.merchant.accounts.v1B\x19AccountRelationshipsProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1.accountrelationships_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.shopping.merchant.accounts.v1B\x19AccountRelationshipsProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1'
    _globals['_ACCOUNTRELATIONSHIP'].fields_by_name['name']._loaded_options = None
    _globals['_ACCOUNTRELATIONSHIP'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ACCOUNTRELATIONSHIP'].fields_by_name['provider']._loaded_options = None
    _globals['_ACCOUNTRELATIONSHIP'].fields_by_name['provider']._serialized_options = b'\xe0A\x05'
    _globals['_ACCOUNTRELATIONSHIP'].fields_by_name['provider_display_name']._loaded_options = None
    _globals['_ACCOUNTRELATIONSHIP'].fields_by_name['provider_display_name']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTRELATIONSHIP'].fields_by_name['account_id_alias']._loaded_options = None
    _globals['_ACCOUNTRELATIONSHIP'].fields_by_name['account_id_alias']._serialized_options = b'\xe0A\x01'
    _globals['_ACCOUNTRELATIONSHIP']._loaded_options = None
    _globals['_ACCOUNTRELATIONSHIP']._serialized_options = b'\xeaA\x8c\x01\n.merchantapi.googleapis.com/AccountRelationship\x12/accounts/{account}/relationships/{relationship}*\x14accountRelationships2\x13accountRelationship'
    _globals['_GETACCOUNTRELATIONSHIPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETACCOUNTRELATIONSHIPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.merchantapi.googleapis.com/AccountRelationship'
    _globals['_UPDATEACCOUNTRELATIONSHIPREQUEST'].fields_by_name['account_relationship']._loaded_options = None
    _globals['_UPDATEACCOUNTRELATIONSHIPREQUEST'].fields_by_name['account_relationship']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEACCOUNTRELATIONSHIPREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEACCOUNTRELATIONSHIPREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCOUNTRELATIONSHIPSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTACCOUNTRELATIONSHIPSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_LISTACCOUNTRELATIONSHIPSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTACCOUNTRELATIONSHIPSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTACCOUNTRELATIONSHIPSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTACCOUNTRELATIONSHIPSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_ACCOUNTRELATIONSHIPSSERVICE']._loaded_options = None
    _globals['_ACCOUNTRELATIONSHIPSSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_ACCOUNTRELATIONSHIPSSERVICE'].methods_by_name['GetAccountRelationship']._loaded_options = None
    _globals['_ACCOUNTRELATIONSHIPSSERVICE'].methods_by_name['GetAccountRelationship']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./accounts/v1/{name=accounts/*/relationships/*}'
    _globals['_ACCOUNTRELATIONSHIPSSERVICE'].methods_by_name['UpdateAccountRelationship']._loaded_options = None
    _globals['_ACCOUNTRELATIONSHIPSSERVICE'].methods_by_name['UpdateAccountRelationship']._serialized_options = b'\xdaA account_relationship,update_mask\x82\xd3\xe4\x93\x02[2C/accounts/v1/{account_relationship.name=accounts/*/relationships/*}:\x14account_relationship'
    _globals['_ACCOUNTRELATIONSHIPSSERVICE'].methods_by_name['ListAccountRelationships']._loaded_options = None
    _globals['_ACCOUNTRELATIONSHIPSSERVICE'].methods_by_name['ListAccountRelationships']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./accounts/v1/{parent=accounts/*}/relationships'
    _globals['_ACCOUNTRELATIONSHIP']._serialized_start = 255
    _globals['_ACCOUNTRELATIONSHIP']._serialized_end = 550
    _globals['_GETACCOUNTRELATIONSHIPREQUEST']._serialized_start = 552
    _globals['_GETACCOUNTRELATIONSHIPREQUEST']._serialized_end = 653
    _globals['_UPDATEACCOUNTRELATIONSHIPREQUEST']._serialized_start = 656
    _globals['_UPDATEACCOUNTRELATIONSHIPREQUEST']._serialized_end = 838
    _globals['_LISTACCOUNTRELATIONSHIPSREQUEST']._serialized_start = 841
    _globals['_LISTACCOUNTRELATIONSHIPSREQUEST']._serialized_end = 983
    _globals['_LISTACCOUNTRELATIONSHIPSRESPONSE']._serialized_start = 986
    _globals['_LISTACCOUNTRELATIONSHIPSRESPONSE']._serialized_end = 1135
    _globals['_ACCOUNTRELATIONSHIPSSERVICE']._serialized_start = 1138
    _globals['_ACCOUNTRELATIONSHIPSSERVICE']._serialized_end = 1991