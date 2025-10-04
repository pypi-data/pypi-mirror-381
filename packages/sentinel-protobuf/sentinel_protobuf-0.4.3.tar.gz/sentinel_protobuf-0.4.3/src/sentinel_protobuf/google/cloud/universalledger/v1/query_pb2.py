"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/universalledger/v1/query.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.universalledger.v1 import accounts_pb2 as google_dot_cloud_dot_universalledger_dot_v1_dot_accounts__pb2
from .....google.cloud.universalledger.v1 import common_pb2 as google_dot_cloud_dot_universalledger_dot_v1_dot_common__pb2
from .....google.cloud.universalledger.v1 import transactions_pb2 as google_dot_cloud_dot_universalledger_dot_v1_dot_transactions__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/universalledger/v1/query.proto\x12\x1fgoogle.cloud.universalledger.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a.google/cloud/universalledger/v1/accounts.proto\x1a,google/cloud/universalledger/v1/common.proto\x1a2google/cloud/universalledger/v1/transactions.proto"\xff\x05\n\x07Account\x12I\n\x0cuser_details\x18\x06 \x01(\x0b2,.google.cloud.universalledger.v1.UserDetailsB\x03\xe0A\x03H\x00\x12^\n\x17account_manager_details\x18\x04 \x01(\x0b26.google.cloud.universalledger.v1.AccountManagerDetailsB\x03\xe0A\x03H\x00\x12Z\n\x15token_manager_details\x18\x05 \x01(\x0b24.google.cloud.universalledger.v1.TokenManagerDetailsB\x03\xe0A\x03H\x00\x12Q\n\x10contract_details\x18\x0b \x01(\x0b20.google.cloud.universalledger.v1.ContractDetailsB\x03\xe0A\x03H\x00\x12[\n\x15clearinghouse_details\x18\n \x01(\x0b25.google.cloud.universalledger.v1.ClearingHouseDetailsB\x03\xe0A\x03H\x00\x12b\n\x19currency_operator_details\x18\x07 \x01(\x0b28.google.cloud.universalledger.v1.CurrencyOperatorDetailsB\x03\xe0A\x03H\x00\x12b\n\x19platform_operator_details\x18\x08 \x01(\x0b28.google.cloud.universalledger.v1.PlatformOperatorDetailsB\x03\xe0A\x03H\x00\x12\x1c\n\x0fsequence_number\x18\x01 \x01(\x03B\x03\xe0A\x03\x12\x17\n\npublic_key\x18\x02 \x01(\x0cB\x03\xe0A\x03\x12\x15\n\x08round_id\x18\x03 \x01(\x03B\x03\xe0A\x03\x12\x14\n\x07comment\x18\t \x01(\tB\x03\xe0A\x03B\x11\n\x0faccount_details"w\n\x15AccountManagerDetails\x12C\n\rtoken_manager\x18\x01 \x01(\x0b2\'.google.cloud.universalledger.v1.EntityB\x03\xe0A\x03\x12\x19\n\x0cnum_accounts\x18\x02 \x01(\x05B\x03\xe0A\x03"\xae\x01\n\x13TokenManagerDetails\x12K\n\x0eissuance_limit\x18\x01 \x01(\x0b2..google.cloud.universalledger.v1.CurrencyValueB\x03\xe0A\x03\x12J\n\rissued_tokens\x18\x02 \x01(\x0b2..google.cloud.universalledger.v1.CurrencyValueB\x03\xe0A\x03"\xa4\x04\n\x0bUserDetails\x12E\n\x0faccount_manager\x18\x01 \x01(\x0b2\'.google.cloud.universalledger.v1.EntityB\x03\xe0A\x03\x12C\n\rtoken_manager\x18\x02 \x01(\x0b2\'.google.cloud.universalledger.v1.EntityB\x03\xe0A\x03\x129\n\x05roles\x18\x03 \x03(\x0e2%.google.cloud.universalledger.v1.RoleB\x03\xe0A\x03\x12K\n\x0eaccount_status\x18\x04 \x01(\x0e2..google.cloud.universalledger.v1.AccountStatusB\x03\xe0A\x03\x12D\n\x07balance\x18\x05 \x01(\x0b2..google.cloud.universalledger.v1.CurrencyValueB\x03\xe0A\x03\x12\\\n\x0eaccount_fields\x18\x06 \x03(\x0b2?.google.cloud.universalledger.v1.UserDetails.AccountFieldsEntryB\x03\xe0A\x03\x1a]\n\x12AccountFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x126\n\x05value\x18\x02 \x01(\x0b2\'.google.cloud.universalledger.v1.Fields:\x028\x01"\x9a\x02\n\x17CurrencyOperatorDetails\x12\x15\n\x08currency\x18\x01 \x01(\tB\x03\xe0A\x03\x12K\n\x0eaccount_status\x18\x02 \x01(\x0e2..google.cloud.universalledger.v1.AccountStatusB\x03\xe0A\x03\x12H\n\x12previous_entity_id\x18\x03 \x01(\x0b2\'.google.cloud.universalledger.v1.EntityB\x03\xe0A\x03\x12Q\n\x1bplatform_operator_entity_id\x18\x04 \x01(\x0b2\'.google.cloud.universalledger.v1.EntityB\x03\xe0A\x03"\xb0\x01\n\x17PlatformOperatorDetails\x12K\n\x0eaccount_status\x18\x01 \x01(\x0e2..google.cloud.universalledger.v1.AccountStatusB\x03\xe0A\x03\x12H\n\x12previous_entity_id\x18\x02 \x01(\x0b2\'.google.cloud.universalledger.v1.EntityB\x03\xe0A\x03"\xfb\x01\n\x14ClearingHouseDetails\x12K\n\x0eaccount_status\x18\x01 \x01(\x0e2..google.cloud.universalledger.v1.AccountStatusB\x03\xe0A\x03\x12G\n\x08balances\x18\x02 \x03(\x0b20.google.cloud.universalledger.v1.BalanceToSettleB\x03\xe0A\x03\x12M\n\x0fsettlement_mode\x18\x03 \x01(\x0e2/.google.cloud.universalledger.v1.SettlementModeB\x03\xe0A\x03"\xa8\x01\n\x0fContractDetails\x12;\n\x05owner\x18\x01 \x01(\x0b2\'.google.cloud.universalledger.v1.EntityB\x03\xe0A\x03\x12\x11\n\x04code\x18\x02 \x01(\x0cB\x03\xe0A\x03\x12E\n\x0fcontract_fields\x18\x03 \x01(\x0b2\'.google.cloud.universalledger.v1.FieldsB\x03\xe0A\x03"\xe4\x01\n\x0fBalanceToSettle\x12C\n\rbalance_payer\x18\x01 \x01(\x0b2\'.google.cloud.universalledger.v1.EntityB\x03\xe0A\x03\x12F\n\x10balance_receiver\x18\x02 \x01(\x0b2\'.google.cloud.universalledger.v1.EntityB\x03\xe0A\x03\x12D\n\x07balance\x18\x03 \x01(\x0b2..google.cloud.universalledger.v1.CurrencyValueB\x03\xe0A\x03"\xa9\x01\n\x06Fields\x12H\n\x06fields\x18\x01 \x03(\x0b23.google.cloud.universalledger.v1.Fields.FieldsEntryB\x03\xe0A\x03\x1aU\n\x0bFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x125\n\x05value\x18\x02 \x01(\x0b2&.google.cloud.universalledger.v1.Value:\x028\x01B\xeb\x01\n#com.google.cloud.universalledger.v1B\nQueryProtoP\x01ZMcloud.google.com/go/universalledger/apiv1/universalledgerpb;universalledgerpb\xaa\x02\x1fGoogle.Cloud.UniversalLedger.V1\xca\x02\x1fGoogle\\Cloud\\UniversalLedger\\V1\xea\x02"Google::Cloud::UniversalLedger::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.universalledger.v1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.universalledger.v1B\nQueryProtoP\x01ZMcloud.google.com/go/universalledger/apiv1/universalledgerpb;universalledgerpb\xaa\x02\x1fGoogle.Cloud.UniversalLedger.V1\xca\x02\x1fGoogle\\Cloud\\UniversalLedger\\V1\xea\x02"Google::Cloud::UniversalLedger::V1'
    _globals['_ACCOUNT'].fields_by_name['user_details']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['user_details']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNT'].fields_by_name['account_manager_details']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['account_manager_details']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNT'].fields_by_name['token_manager_details']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['token_manager_details']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNT'].fields_by_name['contract_details']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['contract_details']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNT'].fields_by_name['clearinghouse_details']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['clearinghouse_details']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNT'].fields_by_name['currency_operator_details']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['currency_operator_details']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNT'].fields_by_name['platform_operator_details']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['platform_operator_details']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNT'].fields_by_name['sequence_number']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['sequence_number']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNT'].fields_by_name['public_key']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['public_key']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNT'].fields_by_name['round_id']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['round_id']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNT'].fields_by_name['comment']._loaded_options = None
    _globals['_ACCOUNT'].fields_by_name['comment']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTMANAGERDETAILS'].fields_by_name['token_manager']._loaded_options = None
    _globals['_ACCOUNTMANAGERDETAILS'].fields_by_name['token_manager']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTMANAGERDETAILS'].fields_by_name['num_accounts']._loaded_options = None
    _globals['_ACCOUNTMANAGERDETAILS'].fields_by_name['num_accounts']._serialized_options = b'\xe0A\x03'
    _globals['_TOKENMANAGERDETAILS'].fields_by_name['issuance_limit']._loaded_options = None
    _globals['_TOKENMANAGERDETAILS'].fields_by_name['issuance_limit']._serialized_options = b'\xe0A\x03'
    _globals['_TOKENMANAGERDETAILS'].fields_by_name['issued_tokens']._loaded_options = None
    _globals['_TOKENMANAGERDETAILS'].fields_by_name['issued_tokens']._serialized_options = b'\xe0A\x03'
    _globals['_USERDETAILS_ACCOUNTFIELDSENTRY']._loaded_options = None
    _globals['_USERDETAILS_ACCOUNTFIELDSENTRY']._serialized_options = b'8\x01'
    _globals['_USERDETAILS'].fields_by_name['account_manager']._loaded_options = None
    _globals['_USERDETAILS'].fields_by_name['account_manager']._serialized_options = b'\xe0A\x03'
    _globals['_USERDETAILS'].fields_by_name['token_manager']._loaded_options = None
    _globals['_USERDETAILS'].fields_by_name['token_manager']._serialized_options = b'\xe0A\x03'
    _globals['_USERDETAILS'].fields_by_name['roles']._loaded_options = None
    _globals['_USERDETAILS'].fields_by_name['roles']._serialized_options = b'\xe0A\x03'
    _globals['_USERDETAILS'].fields_by_name['account_status']._loaded_options = None
    _globals['_USERDETAILS'].fields_by_name['account_status']._serialized_options = b'\xe0A\x03'
    _globals['_USERDETAILS'].fields_by_name['balance']._loaded_options = None
    _globals['_USERDETAILS'].fields_by_name['balance']._serialized_options = b'\xe0A\x03'
    _globals['_USERDETAILS'].fields_by_name['account_fields']._loaded_options = None
    _globals['_USERDETAILS'].fields_by_name['account_fields']._serialized_options = b'\xe0A\x03'
    _globals['_CURRENCYOPERATORDETAILS'].fields_by_name['currency']._loaded_options = None
    _globals['_CURRENCYOPERATORDETAILS'].fields_by_name['currency']._serialized_options = b'\xe0A\x03'
    _globals['_CURRENCYOPERATORDETAILS'].fields_by_name['account_status']._loaded_options = None
    _globals['_CURRENCYOPERATORDETAILS'].fields_by_name['account_status']._serialized_options = b'\xe0A\x03'
    _globals['_CURRENCYOPERATORDETAILS'].fields_by_name['previous_entity_id']._loaded_options = None
    _globals['_CURRENCYOPERATORDETAILS'].fields_by_name['previous_entity_id']._serialized_options = b'\xe0A\x03'
    _globals['_CURRENCYOPERATORDETAILS'].fields_by_name['platform_operator_entity_id']._loaded_options = None
    _globals['_CURRENCYOPERATORDETAILS'].fields_by_name['platform_operator_entity_id']._serialized_options = b'\xe0A\x03'
    _globals['_PLATFORMOPERATORDETAILS'].fields_by_name['account_status']._loaded_options = None
    _globals['_PLATFORMOPERATORDETAILS'].fields_by_name['account_status']._serialized_options = b'\xe0A\x03'
    _globals['_PLATFORMOPERATORDETAILS'].fields_by_name['previous_entity_id']._loaded_options = None
    _globals['_PLATFORMOPERATORDETAILS'].fields_by_name['previous_entity_id']._serialized_options = b'\xe0A\x03'
    _globals['_CLEARINGHOUSEDETAILS'].fields_by_name['account_status']._loaded_options = None
    _globals['_CLEARINGHOUSEDETAILS'].fields_by_name['account_status']._serialized_options = b'\xe0A\x03'
    _globals['_CLEARINGHOUSEDETAILS'].fields_by_name['balances']._loaded_options = None
    _globals['_CLEARINGHOUSEDETAILS'].fields_by_name['balances']._serialized_options = b'\xe0A\x03'
    _globals['_CLEARINGHOUSEDETAILS'].fields_by_name['settlement_mode']._loaded_options = None
    _globals['_CLEARINGHOUSEDETAILS'].fields_by_name['settlement_mode']._serialized_options = b'\xe0A\x03'
    _globals['_CONTRACTDETAILS'].fields_by_name['owner']._loaded_options = None
    _globals['_CONTRACTDETAILS'].fields_by_name['owner']._serialized_options = b'\xe0A\x03'
    _globals['_CONTRACTDETAILS'].fields_by_name['code']._loaded_options = None
    _globals['_CONTRACTDETAILS'].fields_by_name['code']._serialized_options = b'\xe0A\x03'
    _globals['_CONTRACTDETAILS'].fields_by_name['contract_fields']._loaded_options = None
    _globals['_CONTRACTDETAILS'].fields_by_name['contract_fields']._serialized_options = b'\xe0A\x03'
    _globals['_BALANCETOSETTLE'].fields_by_name['balance_payer']._loaded_options = None
    _globals['_BALANCETOSETTLE'].fields_by_name['balance_payer']._serialized_options = b'\xe0A\x03'
    _globals['_BALANCETOSETTLE'].fields_by_name['balance_receiver']._loaded_options = None
    _globals['_BALANCETOSETTLE'].fields_by_name['balance_receiver']._serialized_options = b'\xe0A\x03'
    _globals['_BALANCETOSETTLE'].fields_by_name['balance']._loaded_options = None
    _globals['_BALANCETOSETTLE'].fields_by_name['balance']._serialized_options = b'\xe0A\x03'
    _globals['_FIELDS_FIELDSENTRY']._loaded_options = None
    _globals['_FIELDS_FIELDSENTRY']._serialized_options = b'8\x01'
    _globals['_FIELDS'].fields_by_name['fields']._loaded_options = None
    _globals['_FIELDS'].fields_by_name['fields']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNT']._serialized_start = 260
    _globals['_ACCOUNT']._serialized_end = 1027
    _globals['_ACCOUNTMANAGERDETAILS']._serialized_start = 1029
    _globals['_ACCOUNTMANAGERDETAILS']._serialized_end = 1148
    _globals['_TOKENMANAGERDETAILS']._serialized_start = 1151
    _globals['_TOKENMANAGERDETAILS']._serialized_end = 1325
    _globals['_USERDETAILS']._serialized_start = 1328
    _globals['_USERDETAILS']._serialized_end = 1876
    _globals['_USERDETAILS_ACCOUNTFIELDSENTRY']._serialized_start = 1783
    _globals['_USERDETAILS_ACCOUNTFIELDSENTRY']._serialized_end = 1876
    _globals['_CURRENCYOPERATORDETAILS']._serialized_start = 1879
    _globals['_CURRENCYOPERATORDETAILS']._serialized_end = 2161
    _globals['_PLATFORMOPERATORDETAILS']._serialized_start = 2164
    _globals['_PLATFORMOPERATORDETAILS']._serialized_end = 2340
    _globals['_CLEARINGHOUSEDETAILS']._serialized_start = 2343
    _globals['_CLEARINGHOUSEDETAILS']._serialized_end = 2594
    _globals['_CONTRACTDETAILS']._serialized_start = 2597
    _globals['_CONTRACTDETAILS']._serialized_end = 2765
    _globals['_BALANCETOSETTLE']._serialized_start = 2768
    _globals['_BALANCETOSETTLE']._serialized_end = 2996
    _globals['_FIELDS']._serialized_start = 2999
    _globals['_FIELDS']._serialized_end = 3168
    _globals['_FIELDS_FIELDSENTRY']._serialized_start = 3083
    _globals['_FIELDS_FIELDSENTRY']._serialized_end = 3168