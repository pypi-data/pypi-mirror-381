"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/universalledger/v1/types.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.universalledger.v1 import common_pb2 as google_dot_cloud_dot_universalledger_dot_v1_dot_common__pb2
from .....google.cloud.universalledger.v1 import status_event_pb2 as google_dot_cloud_dot_universalledger_dot_v1_dot_status__event__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/universalledger/v1/types.proto\x12\x1fgoogle.cloud.universalledger.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a,google/cloud/universalledger/v1/common.proto\x1a2google/cloud/universalledger/v1/status_event.proto\x1a\x19google/protobuf/any.proto"\xeb\x02\n\x11ClientTransaction\x12(\n\x03app\x18\x05 \x01(\x0b2\x14.google.protobuf.AnyB\x03\xe0A\x01H\x00\x12+\n\x0boperational\x18\x06 \x01(\x0b2\x14.google.protobuf.AnyH\x00\x12B\n\x05chain\x18\x08 \x01(\x0b21.google.cloud.universalledger.v1.TransactionChainH\x00\x12<\n\x06source\x18\x01 \x01(\x0b2\'.google.cloud.universalledger.v1.EntityB\x03\xe0A\x02\x12A\n\x0bsignatories\x18\x02 \x03(\x0b2\'.google.cloud.universalledger.v1.EntityB\x03\xe0A\x01\x12\x1c\n\x0fsequence_number\x18\x03 \x01(\x03B\x03\xe0A\x02\x12\x14\n\x0cchained_unit\x18\x07 \x01(\x08B\x06\n\x04kind"}\n\x11SignedTransaction\x12*\n\x1dserialized_client_transaction\x18\x01 \x01(\x0cB\x03\xe0A\x02\x12\x1d\n\x10sender_signature\x18\x03 \x01(\x0cB\x03\xe0A\x02\x12\x1d\n\x10other_signatures\x18\x04 \x03(\x0cB\x03\xe0A\x01"!\n\x10TransactionChain\x12\r\n\x05units\x18\x01 \x03(\x0c"G\n\nMerkleTree\x12\x1a\n\rroot_hash_hex\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10num_transactions\x18\x02 \x01(\x03B\x03\xe0A\x03"\x97\x02\n\x10RoundCertificate\x12\x15\n\x08round_id\x18\x01 \x01(\x03B\x03\xe0A\x03\x12\x19\n\x0cvalidator_id\x18\x02 \x01(\tB\x03\xe0A\x03\x12%\n\x18round_state_checksum_hex\x18\x03 \x01(\tB\x03\xe0A\x03\x12%\n\x18round_delta_checksum_hex\x18\x04 \x01(\tB\x03\xe0A\x03\x12E\n\x0bmerkle_tree\x18\x06 \x01(\x0b2+.google.cloud.universalledger.v1.MerkleTreeB\x03\xe0A\x03\x12!\n\x14validator_signatures\x18\x05 \x03(\x0cB\x03\xe0A\x01\x12\x19\n\x0cis_finalized\x18\x07 \x01(\x08B\x03\xe0A\x03"i\n\x11TransactionEffect\x12\x10\n\x03key\x18\x01 \x01(\x0cB\x03\xe0A\x03\x12\x14\n\x07old_val\x18\x02 \x01(\x0cB\x03\xe0A\x03\x12\x14\n\x07new_val\x18\x03 \x01(\x0cB\x03\xe0A\x03\x12\x16\n\tdelta_val\x18\x04 \x01(\x03B\x03\xe0A\x03"<\n\x11TransactionStatus\x12\x11\n\x04code\x18\x01 \x01(\x05B\x03\xe0A\x03\x12\x14\n\x07message\x18\x02 \x01(\x0cB\x03\xe0A\x03"\xa2\x01\n\x12TransactionEffects\x12B\n\x06status\x18\x01 \x01(\x0b22.google.cloud.universalledger.v1.TransactionStatus\x12H\n\x07effects\x18\x02 \x03(\x0b22.google.cloud.universalledger.v1.TransactionEffectB\x03\xe0A\x03"\xb8\x01\n\x10TransactionEvent\x12\x11\n\x04type\x18\x01 \x01(\tB\x03\xe0A\x03\x12Y\n\nattributes\x18\x02 \x03(\x0b2@.google.cloud.universalledger.v1.TransactionEvent.EventAttributeB\x03\xe0A\x03\x1a6\n\x0eEventAttribute\x12\x10\n\x03key\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x12\n\x05value\x18\x02 \x01(\tB\x03\xe0A\x03"\xd2\x02\n\x16TransactionCertificate\x12#\n\x16transaction_digest_hex\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x15\n\x08round_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12U\n\x13transaction_effects\x18\x03 \x01(\x0b23.google.cloud.universalledger.v1.TransactionEffectsB\x03\xe0A\x03\x12F\n\x06events\x18\x06 \x03(\x0b21.google.cloud.universalledger.v1.TransactionEventB\x03\xe0A\x03\x123\n&transaction_effects_state_checksum_hex\x18\x04 \x01(\tB\x03\xe0A\x03\x12(\n certification_results_digest_hex\x18\x05 \x01(\t"\xea\x02\n\x10ProofOfInclusion\x12X\n\x17transaction_certificate\x18\x01 \x01(\x0b27.google.cloud.universalledger.v1.TransactionCertificate\x12L\n\x11round_certificate\x18\x02 \x01(\x0b21.google.cloud.universalledger.v1.RoundCertificate\x12a\n\x12path_to_round_root\x18\x03 \x03(\x0b2@.google.cloud.universalledger.v1.ProofOfInclusion.MerkleTreeNodeB\x03\xe0A\x03\x1aK\n\x0eMerkleTreeNode\x12\x1b\n\x13left_child_hash_hex\x18\x01 \x01(\t\x12\x1c\n\x14right_child_hash_hex\x18\x02 \x01(\t"\xd9\x02\n\x12TransactionAttempt\x12Z\n\x06status\x18\x01 \x01(\x0e2E.google.cloud.universalledger.v1.TransactionAttempt.TransactionStatusB\x03\xe0A\x03\x12M\n\x12proof_of_inclusion\x18\x02 \x01(\x0b21.google.cloud.universalledger.v1.ProofOfInclusion\x12C\n\rstatus_events\x18\x03 \x03(\x0b2,.google.cloud.universalledger.v1.StatusEvent"S\n\x11TransactionStatus\x12"\n\x1eTRANSACTION_STATUS_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\r\n\tFINALIZED\x10\x02B\xeb\x01\n#com.google.cloud.universalledger.v1B\nTypesProtoP\x01ZMcloud.google.com/go/universalledger/apiv1/universalledgerpb;universalledgerpb\xaa\x02\x1fGoogle.Cloud.UniversalLedger.V1\xca\x02\x1fGoogle\\Cloud\\UniversalLedger\\V1\xea\x02"Google::Cloud::UniversalLedger::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.universalledger.v1.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.universalledger.v1B\nTypesProtoP\x01ZMcloud.google.com/go/universalledger/apiv1/universalledgerpb;universalledgerpb\xaa\x02\x1fGoogle.Cloud.UniversalLedger.V1\xca\x02\x1fGoogle\\Cloud\\UniversalLedger\\V1\xea\x02"Google::Cloud::UniversalLedger::V1'
    _globals['_CLIENTTRANSACTION'].fields_by_name['app']._loaded_options = None
    _globals['_CLIENTTRANSACTION'].fields_by_name['app']._serialized_options = b'\xe0A\x01'
    _globals['_CLIENTTRANSACTION'].fields_by_name['source']._loaded_options = None
    _globals['_CLIENTTRANSACTION'].fields_by_name['source']._serialized_options = b'\xe0A\x02'
    _globals['_CLIENTTRANSACTION'].fields_by_name['signatories']._loaded_options = None
    _globals['_CLIENTTRANSACTION'].fields_by_name['signatories']._serialized_options = b'\xe0A\x01'
    _globals['_CLIENTTRANSACTION'].fields_by_name['sequence_number']._loaded_options = None
    _globals['_CLIENTTRANSACTION'].fields_by_name['sequence_number']._serialized_options = b'\xe0A\x02'
    _globals['_SIGNEDTRANSACTION'].fields_by_name['serialized_client_transaction']._loaded_options = None
    _globals['_SIGNEDTRANSACTION'].fields_by_name['serialized_client_transaction']._serialized_options = b'\xe0A\x02'
    _globals['_SIGNEDTRANSACTION'].fields_by_name['sender_signature']._loaded_options = None
    _globals['_SIGNEDTRANSACTION'].fields_by_name['sender_signature']._serialized_options = b'\xe0A\x02'
    _globals['_SIGNEDTRANSACTION'].fields_by_name['other_signatures']._loaded_options = None
    _globals['_SIGNEDTRANSACTION'].fields_by_name['other_signatures']._serialized_options = b'\xe0A\x01'
    _globals['_MERKLETREE'].fields_by_name['root_hash_hex']._loaded_options = None
    _globals['_MERKLETREE'].fields_by_name['root_hash_hex']._serialized_options = b'\xe0A\x03'
    _globals['_MERKLETREE'].fields_by_name['num_transactions']._loaded_options = None
    _globals['_MERKLETREE'].fields_by_name['num_transactions']._serialized_options = b'\xe0A\x03'
    _globals['_ROUNDCERTIFICATE'].fields_by_name['round_id']._loaded_options = None
    _globals['_ROUNDCERTIFICATE'].fields_by_name['round_id']._serialized_options = b'\xe0A\x03'
    _globals['_ROUNDCERTIFICATE'].fields_by_name['validator_id']._loaded_options = None
    _globals['_ROUNDCERTIFICATE'].fields_by_name['validator_id']._serialized_options = b'\xe0A\x03'
    _globals['_ROUNDCERTIFICATE'].fields_by_name['round_state_checksum_hex']._loaded_options = None
    _globals['_ROUNDCERTIFICATE'].fields_by_name['round_state_checksum_hex']._serialized_options = b'\xe0A\x03'
    _globals['_ROUNDCERTIFICATE'].fields_by_name['round_delta_checksum_hex']._loaded_options = None
    _globals['_ROUNDCERTIFICATE'].fields_by_name['round_delta_checksum_hex']._serialized_options = b'\xe0A\x03'
    _globals['_ROUNDCERTIFICATE'].fields_by_name['merkle_tree']._loaded_options = None
    _globals['_ROUNDCERTIFICATE'].fields_by_name['merkle_tree']._serialized_options = b'\xe0A\x03'
    _globals['_ROUNDCERTIFICATE'].fields_by_name['validator_signatures']._loaded_options = None
    _globals['_ROUNDCERTIFICATE'].fields_by_name['validator_signatures']._serialized_options = b'\xe0A\x01'
    _globals['_ROUNDCERTIFICATE'].fields_by_name['is_finalized']._loaded_options = None
    _globals['_ROUNDCERTIFICATE'].fields_by_name['is_finalized']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSACTIONEFFECT'].fields_by_name['key']._loaded_options = None
    _globals['_TRANSACTIONEFFECT'].fields_by_name['key']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSACTIONEFFECT'].fields_by_name['old_val']._loaded_options = None
    _globals['_TRANSACTIONEFFECT'].fields_by_name['old_val']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSACTIONEFFECT'].fields_by_name['new_val']._loaded_options = None
    _globals['_TRANSACTIONEFFECT'].fields_by_name['new_val']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSACTIONEFFECT'].fields_by_name['delta_val']._loaded_options = None
    _globals['_TRANSACTIONEFFECT'].fields_by_name['delta_val']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSACTIONSTATUS'].fields_by_name['code']._loaded_options = None
    _globals['_TRANSACTIONSTATUS'].fields_by_name['code']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSACTIONSTATUS'].fields_by_name['message']._loaded_options = None
    _globals['_TRANSACTIONSTATUS'].fields_by_name['message']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSACTIONEFFECTS'].fields_by_name['effects']._loaded_options = None
    _globals['_TRANSACTIONEFFECTS'].fields_by_name['effects']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSACTIONEVENT_EVENTATTRIBUTE'].fields_by_name['key']._loaded_options = None
    _globals['_TRANSACTIONEVENT_EVENTATTRIBUTE'].fields_by_name['key']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSACTIONEVENT_EVENTATTRIBUTE'].fields_by_name['value']._loaded_options = None
    _globals['_TRANSACTIONEVENT_EVENTATTRIBUTE'].fields_by_name['value']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSACTIONEVENT'].fields_by_name['type']._loaded_options = None
    _globals['_TRANSACTIONEVENT'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSACTIONEVENT'].fields_by_name['attributes']._loaded_options = None
    _globals['_TRANSACTIONEVENT'].fields_by_name['attributes']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSACTIONCERTIFICATE'].fields_by_name['transaction_digest_hex']._loaded_options = None
    _globals['_TRANSACTIONCERTIFICATE'].fields_by_name['transaction_digest_hex']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSACTIONCERTIFICATE'].fields_by_name['round_id']._loaded_options = None
    _globals['_TRANSACTIONCERTIFICATE'].fields_by_name['round_id']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSACTIONCERTIFICATE'].fields_by_name['transaction_effects']._loaded_options = None
    _globals['_TRANSACTIONCERTIFICATE'].fields_by_name['transaction_effects']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSACTIONCERTIFICATE'].fields_by_name['events']._loaded_options = None
    _globals['_TRANSACTIONCERTIFICATE'].fields_by_name['events']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSACTIONCERTIFICATE'].fields_by_name['transaction_effects_state_checksum_hex']._loaded_options = None
    _globals['_TRANSACTIONCERTIFICATE'].fields_by_name['transaction_effects_state_checksum_hex']._serialized_options = b'\xe0A\x03'
    _globals['_PROOFOFINCLUSION'].fields_by_name['path_to_round_root']._loaded_options = None
    _globals['_PROOFOFINCLUSION'].fields_by_name['path_to_round_root']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSACTIONATTEMPT'].fields_by_name['status']._loaded_options = None
    _globals['_TRANSACTIONATTEMPT'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_CLIENTTRANSACTION']._serialized_start = 239
    _globals['_CLIENTTRANSACTION']._serialized_end = 602
    _globals['_SIGNEDTRANSACTION']._serialized_start = 604
    _globals['_SIGNEDTRANSACTION']._serialized_end = 729
    _globals['_TRANSACTIONCHAIN']._serialized_start = 731
    _globals['_TRANSACTIONCHAIN']._serialized_end = 764
    _globals['_MERKLETREE']._serialized_start = 766
    _globals['_MERKLETREE']._serialized_end = 837
    _globals['_ROUNDCERTIFICATE']._serialized_start = 840
    _globals['_ROUNDCERTIFICATE']._serialized_end = 1119
    _globals['_TRANSACTIONEFFECT']._serialized_start = 1121
    _globals['_TRANSACTIONEFFECT']._serialized_end = 1226
    _globals['_TRANSACTIONSTATUS']._serialized_start = 1228
    _globals['_TRANSACTIONSTATUS']._serialized_end = 1288
    _globals['_TRANSACTIONEFFECTS']._serialized_start = 1291
    _globals['_TRANSACTIONEFFECTS']._serialized_end = 1453
    _globals['_TRANSACTIONEVENT']._serialized_start = 1456
    _globals['_TRANSACTIONEVENT']._serialized_end = 1640
    _globals['_TRANSACTIONEVENT_EVENTATTRIBUTE']._serialized_start = 1586
    _globals['_TRANSACTIONEVENT_EVENTATTRIBUTE']._serialized_end = 1640
    _globals['_TRANSACTIONCERTIFICATE']._serialized_start = 1643
    _globals['_TRANSACTIONCERTIFICATE']._serialized_end = 1981
    _globals['_PROOFOFINCLUSION']._serialized_start = 1984
    _globals['_PROOFOFINCLUSION']._serialized_end = 2346
    _globals['_PROOFOFINCLUSION_MERKLETREENODE']._serialized_start = 2271
    _globals['_PROOFOFINCLUSION_MERKLETREENODE']._serialized_end = 2346
    _globals['_TRANSACTIONATTEMPT']._serialized_start = 2349
    _globals['_TRANSACTIONATTEMPT']._serialized_end = 2694
    _globals['_TRANSACTIONATTEMPT_TRANSACTIONSTATUS']._serialized_start = 2611
    _globals['_TRANSACTIONATTEMPT_TRANSACTIONSTATUS']._serialized_end = 2694