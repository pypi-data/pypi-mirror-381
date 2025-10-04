"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/universalledger/v1/universalledger.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.universalledger.v1 import query_pb2 as google_dot_cloud_dot_universalledger_dot_v1_dot_query__pb2
from .....google.cloud.universalledger.v1 import types_pb2 as google_dot_cloud_dot_universalledger_dot_v1_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/universalledger/v1/universalledger.proto\x12\x1fgoogle.cloud.universalledger.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a+google/cloud/universalledger/v1/query.proto\x1a+google/cloud/universalledger/v1/types.proto"\x9e\x01\n\x08Endpoint\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08:\x7f\xeaA|\n\'universalledger.googleapis.com/Endpoint\x12<projects/{project}/locations/{location}/endpoints/{endpoint}*\tendpoints2\x08endpoint"\x88\x01\n\x14ListEndpointsRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\x12\'universalledger.googleapis.com/Endpoint\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"n\n\x15ListEndpointsResponse\x12<\n\tendpoints\x18\x01 \x03(\x0b2).google.cloud.universalledger.v1.Endpoint\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"S\n\x12GetEndpointRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'universalledger.googleapis.com/Endpoint"\\\n\x13QueryAccountRequest\x12\x15\n\x08endpoint\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\naccount_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08round_id\x18\x03 \x01(\x03B\x03\xe0A\x01"Q\n\x14QueryAccountResponse\x129\n\x07account\x18\x01 \x01(\x0b2(.google.cloud.universalledger.v1.Account"]\n\x18SubmitTransactionRequest\x12\x15\n\x08endpoint\x18\x01 \x01(\tB\x03\xe0A\x02\x12*\n\x1dserialized_signed_transaction\x18\x02 \x01(\x0cB\x03\xe0A\x02";\n\x19SubmitTransactionResponse\x12\x1e\n\x16transaction_digest_hex\x18\x01 \x01(\t"t\n#SubmitOperationalTransactionRequest\x12\x15\n\x08endpoint\x18\x01 \x01(\tB\x03\xe0A\x02\x126\n)serialized_signed_operational_transaction\x18\x02 \x01(\x0cB\x03\xe0A\x02"F\n$SubmitOperationalTransactionResponse\x12\x1e\n\x16transaction_digest_hex\x18\x01 \x01(\t"Z\n\x1cQueryTransactionStateRequest\x12\x15\n\x08endpoint\x18\x01 \x01(\tB\x03\xe0A\x02\x12#\n\x16transaction_digest_hex\x18\x02 \x01(\tB\x03\xe0A\x02"r\n\x1dQueryTransactionStateResponse\x12Q\n\x14transaction_attempts\x18\x01 \x03(\x0b23.google.cloud.universalledger.v1.TransactionAttempt2\x81\x0c\n\x0fUniversalLedger\x12\x83\x02\n\x11SubmitTransaction\x129.google.cloud.universalledger.v1.SubmitTransactionRequest\x1a:.google.cloud.universalledger.v1.SubmitTransactionResponse"w\xdaA&endpoint,serialized_signed_transaction\x82\xd3\xe4\x93\x02H"C/v1/{endpoint=projects/*/locations/*/endpoints/*}:submitTransaction:\x01*\x12\xbe\x01\n\rListEndpoints\x125.google.cloud.universalledger.v1.ListEndpointsRequest\x1a6.google.cloud.universalledger.v1.ListEndpointsResponse">\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/endpoints\x12\xab\x01\n\x0bGetEndpoint\x123.google.cloud.universalledger.v1.GetEndpointRequest\x1a).google.cloud.universalledger.v1.Endpoint"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/endpoints/*}\x12\xbc\x02\n\x1cSubmitOperationalTransaction\x12D.google.cloud.universalledger.v1.SubmitOperationalTransactionRequest\x1aE.google.cloud.universalledger.v1.SubmitOperationalTransactionResponse"\x8e\x01\xdaA2endpoint,serialized_signed_operational_transaction\x82\xd3\xe4\x93\x02S"N/v1/{endpoint=projects/*/locations/*/endpoints/*}:submitOperationalTransaction:\x01*\x12\x89\x02\n\x15QueryTransactionState\x12=.google.cloud.universalledger.v1.QueryTransactionStateRequest\x1a>.google.cloud.universalledger.v1.QueryTransactionStateResponse"q\xdaA\x1fendpoint,transaction_digest_hex\x82\xd3\xe4\x93\x02I\x12G/v1/{endpoint=projects/*/locations/*/endpoints/*}:queryTransactionState\x12\xd9\x01\n\x0cQueryAccount\x124.google.cloud.universalledger.v1.QueryAccountRequest\x1a5.google.cloud.universalledger.v1.QueryAccountResponse"\\\xdaA\x13endpoint,account_id\x82\xd3\xe4\x93\x02@\x12>/v1/{endpoint=projects/*/locations/*/endpoints/*}:queryAccount\x1aR\xcaA\x1euniversalledger.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf5\x01\n#com.google.cloud.universalledger.v1B\x14UniversalLedgerProtoP\x01ZMcloud.google.com/go/universalledger/apiv1/universalledgerpb;universalledgerpb\xaa\x02\x1fGoogle.Cloud.UniversalLedger.V1\xca\x02\x1fGoogle\\Cloud\\UniversalLedger\\V1\xea\x02"Google::Cloud::UniversalLedger::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.universalledger.v1.universalledger_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.universalledger.v1B\x14UniversalLedgerProtoP\x01ZMcloud.google.com/go/universalledger/apiv1/universalledgerpb;universalledgerpb\xaa\x02\x1fGoogle.Cloud.UniversalLedger.V1\xca\x02\x1fGoogle\\Cloud\\UniversalLedger\\V1\xea\x02"Google::Cloud::UniversalLedger::V1'
    _globals['_ENDPOINT'].fields_by_name['name']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ENDPOINT']._loaded_options = None
    _globals['_ENDPOINT']._serialized_options = b"\xeaA|\n'universalledger.googleapis.com/Endpoint\x12<projects/{project}/locations/{location}/endpoints/{endpoint}*\tendpoints2\x08endpoint"
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\x12'universalledger.googleapis.com/Endpoint"
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETENDPOINTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENDPOINTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'universalledger.googleapis.com/Endpoint"
    _globals['_QUERYACCOUNTREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_QUERYACCOUNTREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02'
    _globals['_QUERYACCOUNTREQUEST'].fields_by_name['account_id']._loaded_options = None
    _globals['_QUERYACCOUNTREQUEST'].fields_by_name['account_id']._serialized_options = b'\xe0A\x02'
    _globals['_QUERYACCOUNTREQUEST'].fields_by_name['round_id']._loaded_options = None
    _globals['_QUERYACCOUNTREQUEST'].fields_by_name['round_id']._serialized_options = b'\xe0A\x01'
    _globals['_SUBMITTRANSACTIONREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_SUBMITTRANSACTIONREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02'
    _globals['_SUBMITTRANSACTIONREQUEST'].fields_by_name['serialized_signed_transaction']._loaded_options = None
    _globals['_SUBMITTRANSACTIONREQUEST'].fields_by_name['serialized_signed_transaction']._serialized_options = b'\xe0A\x02'
    _globals['_SUBMITOPERATIONALTRANSACTIONREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_SUBMITOPERATIONALTRANSACTIONREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02'
    _globals['_SUBMITOPERATIONALTRANSACTIONREQUEST'].fields_by_name['serialized_signed_operational_transaction']._loaded_options = None
    _globals['_SUBMITOPERATIONALTRANSACTIONREQUEST'].fields_by_name['serialized_signed_operational_transaction']._serialized_options = b'\xe0A\x02'
    _globals['_QUERYTRANSACTIONSTATEREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_QUERYTRANSACTIONSTATEREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02'
    _globals['_QUERYTRANSACTIONSTATEREQUEST'].fields_by_name['transaction_digest_hex']._loaded_options = None
    _globals['_QUERYTRANSACTIONSTATEREQUEST'].fields_by_name['transaction_digest_hex']._serialized_options = b'\xe0A\x02'
    _globals['_UNIVERSALLEDGER']._loaded_options = None
    _globals['_UNIVERSALLEDGER']._serialized_options = b'\xcaA\x1euniversalledger.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_UNIVERSALLEDGER'].methods_by_name['SubmitTransaction']._loaded_options = None
    _globals['_UNIVERSALLEDGER'].methods_by_name['SubmitTransaction']._serialized_options = b'\xdaA&endpoint,serialized_signed_transaction\x82\xd3\xe4\x93\x02H"C/v1/{endpoint=projects/*/locations/*/endpoints/*}:submitTransaction:\x01*'
    _globals['_UNIVERSALLEDGER'].methods_by_name['ListEndpoints']._loaded_options = None
    _globals['_UNIVERSALLEDGER'].methods_by_name['ListEndpoints']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/endpoints'
    _globals['_UNIVERSALLEDGER'].methods_by_name['GetEndpoint']._loaded_options = None
    _globals['_UNIVERSALLEDGER'].methods_by_name['GetEndpoint']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/endpoints/*}'
    _globals['_UNIVERSALLEDGER'].methods_by_name['SubmitOperationalTransaction']._loaded_options = None
    _globals['_UNIVERSALLEDGER'].methods_by_name['SubmitOperationalTransaction']._serialized_options = b'\xdaA2endpoint,serialized_signed_operational_transaction\x82\xd3\xe4\x93\x02S"N/v1/{endpoint=projects/*/locations/*/endpoints/*}:submitOperationalTransaction:\x01*'
    _globals['_UNIVERSALLEDGER'].methods_by_name['QueryTransactionState']._loaded_options = None
    _globals['_UNIVERSALLEDGER'].methods_by_name['QueryTransactionState']._serialized_options = b'\xdaA\x1fendpoint,transaction_digest_hex\x82\xd3\xe4\x93\x02I\x12G/v1/{endpoint=projects/*/locations/*/endpoints/*}:queryTransactionState'
    _globals['_UNIVERSALLEDGER'].methods_by_name['QueryAccount']._loaded_options = None
    _globals['_UNIVERSALLEDGER'].methods_by_name['QueryAccount']._serialized_options = b'\xdaA\x13endpoint,account_id\x82\xd3\xe4\x93\x02@\x12>/v1/{endpoint=projects/*/locations/*/endpoints/*}:queryAccount'
    _globals['_ENDPOINT']._serialized_start = 296
    _globals['_ENDPOINT']._serialized_end = 454
    _globals['_LISTENDPOINTSREQUEST']._serialized_start = 457
    _globals['_LISTENDPOINTSREQUEST']._serialized_end = 593
    _globals['_LISTENDPOINTSRESPONSE']._serialized_start = 595
    _globals['_LISTENDPOINTSRESPONSE']._serialized_end = 705
    _globals['_GETENDPOINTREQUEST']._serialized_start = 707
    _globals['_GETENDPOINTREQUEST']._serialized_end = 790
    _globals['_QUERYACCOUNTREQUEST']._serialized_start = 792
    _globals['_QUERYACCOUNTREQUEST']._serialized_end = 884
    _globals['_QUERYACCOUNTRESPONSE']._serialized_start = 886
    _globals['_QUERYACCOUNTRESPONSE']._serialized_end = 967
    _globals['_SUBMITTRANSACTIONREQUEST']._serialized_start = 969
    _globals['_SUBMITTRANSACTIONREQUEST']._serialized_end = 1062
    _globals['_SUBMITTRANSACTIONRESPONSE']._serialized_start = 1064
    _globals['_SUBMITTRANSACTIONRESPONSE']._serialized_end = 1123
    _globals['_SUBMITOPERATIONALTRANSACTIONREQUEST']._serialized_start = 1125
    _globals['_SUBMITOPERATIONALTRANSACTIONREQUEST']._serialized_end = 1241
    _globals['_SUBMITOPERATIONALTRANSACTIONRESPONSE']._serialized_start = 1243
    _globals['_SUBMITOPERATIONALTRANSACTIONRESPONSE']._serialized_end = 1313
    _globals['_QUERYTRANSACTIONSTATEREQUEST']._serialized_start = 1315
    _globals['_QUERYTRANSACTIONSTATEREQUEST']._serialized_end = 1405
    _globals['_QUERYTRANSACTIONSTATERESPONSE']._serialized_start = 1407
    _globals['_QUERYTRANSACTIONSTATERESPONSE']._serialized_end = 1521
    _globals['_UNIVERSALLEDGER']._serialized_start = 1524
    _globals['_UNIVERSALLEDGER']._serialized_end = 3061