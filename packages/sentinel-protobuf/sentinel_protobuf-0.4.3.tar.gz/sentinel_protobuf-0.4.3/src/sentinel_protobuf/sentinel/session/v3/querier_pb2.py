"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/session/v3/querier.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....sentinel.session.v3 import params_pb2 as sentinel_dot_session_dot_v3_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!sentinel/session/v3/querier.proto\x12\x13sentinel.session.v3\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a sentinel/session/v3/params.proto"R\n\x14QuerySessionsRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"m\n\x1eQuerySessionsForAccountRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"|\n!QuerySessionsForAllocationRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0f\n\x07address\x18\x02 \x01(\t\x12:\n\npagination\x18\x03 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"j\n\x1bQuerySessionsForNodeRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"m\n#QuerySessionsForSubscriptionRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"!\n\x13QuerySessionRequest\x12\n\n\x02id\x18\x01 \x01(\x04"\x14\n\x12QueryParamsRequest"|\n\x15QuerySessionsResponse\x12&\n\x08sessions\x18\x01 \x03(\x0b2\x14.google.protobuf.Any\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x86\x01\n\x1fQuerySessionsForAccountResponse\x12&\n\x08sessions\x18\x01 \x03(\x0b2\x14.google.protobuf.Any\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x89\x01\n"QuerySessionsForAllocationResponse\x12&\n\x08sessions\x18\x01 \x03(\x0b2\x14.google.protobuf.Any\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x83\x01\n\x1cQuerySessionsForNodeResponse\x12&\n\x08sessions\x18\x01 \x03(\x0b2\x14.google.protobuf.Any\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x8b\x01\n$QuerySessionsForSubscriptionResponse\x12&\n\x08sessions\x18\x01 \x03(\x0b2\x14.google.protobuf.Any\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"=\n\x14QuerySessionResponse\x12%\n\x07session\x18\x01 \x01(\x0b2\x14.google.protobuf.Any"H\n\x13QueryParamsResponse\x121\n\x06params\x18\x01 \x01(\x0b2\x1b.sentinel.session.v3.ParamsB\x04\xc8\xde\x1f\x002\xde\t\n\x0cQueryService\x12\x8d\x01\n\rQuerySessions\x12).sentinel.session.v3.QuerySessionsRequest\x1a*.sentinel.session.v3.QuerySessionsResponse"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/sentinel/session/v3/sessions\x12\xbe\x01\n\x17QuerySessionsForAccount\x123.sentinel.session.v3.QuerySessionsForAccountRequest\x1a4.sentinel.session.v3.QuerySessionsForAccountResponse"8\x82\xd3\xe4\x93\x022\x120/sentinel/session/v3/accounts/{address}/sessions\x12\xb2\x01\n\x14QuerySessionsForNode\x120.sentinel.session.v3.QuerySessionsForNodeRequest\x1a1.sentinel.session.v3.QuerySessionsForNodeResponse"5\x82\xd3\xe4\x93\x02/\x12-/sentinel/session/v3/nodes/{address}/sessions\x12\xcd\x01\n\x1cQuerySessionsForSubscription\x128.sentinel.session.v3.QuerySessionsForSubscriptionRequest\x1a9.sentinel.session.v3.QuerySessionsForSubscriptionResponse"8\x82\xd3\xe4\x93\x022\x120/sentinel/session/v3/subscriptions/{id}/sessions\x12\xdd\x01\n\x1aQuerySessionsForAllocation\x126.sentinel.session.v3.QuerySessionsForAllocationRequest\x1a7.sentinel.session.v3.QuerySessionsForAllocationResponse"N\x82\xd3\xe4\x93\x02H\x12F/sentinel/session/v3/subscriptions/{id}/allocations/{address}/sessions\x12\x8f\x01\n\x0cQuerySession\x12(.sentinel.session.v3.QuerySessionRequest\x1a).sentinel.session.v3.QuerySessionResponse"*\x82\xd3\xe4\x93\x02$\x12"/sentinel/session/v3/sessions/{id}\x12\x85\x01\n\x0bQueryParams\x12\'.sentinel.session.v3.QueryParamsRequest\x1a(.sentinel.session.v3.QueryParamsResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/sentinel/session/v3/paramsBIZ?github.com/sentinel-official/sentinelhub/v12/x/session/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.session.v3.querier_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z?github.com/sentinel-official/sentinelhub/v12/x/session/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSERVICE'].methods_by_name['QuerySessions']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySessions']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f\x12\x1d/sentinel/session/v3/sessions'
    _globals['_QUERYSERVICE'].methods_by_name['QuerySessionsForAccount']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySessionsForAccount']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/sentinel/session/v3/accounts/{address}/sessions'
    _globals['_QUERYSERVICE'].methods_by_name['QuerySessionsForNode']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySessionsForNode']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/sentinel/session/v3/nodes/{address}/sessions'
    _globals['_QUERYSERVICE'].methods_by_name['QuerySessionsForSubscription']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySessionsForSubscription']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/sentinel/session/v3/subscriptions/{id}/sessions'
    _globals['_QUERYSERVICE'].methods_by_name['QuerySessionsForAllocation']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySessionsForAllocation']._serialized_options = b'\x82\xd3\xe4\x93\x02H\x12F/sentinel/session/v3/subscriptions/{id}/allocations/{address}/sessions'
    _globals['_QUERYSERVICE'].methods_by_name['QuerySession']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QuerySession']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/sentinel/session/v3/sessions/{id}'
    _globals['_QUERYSERVICE'].methods_by_name['QueryParams']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryParams']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x12\x1b/sentinel/session/v3/params'
    _globals['_QUERYSESSIONSREQUEST']._serialized_start = 215
    _globals['_QUERYSESSIONSREQUEST']._serialized_end = 297
    _globals['_QUERYSESSIONSFORACCOUNTREQUEST']._serialized_start = 299
    _globals['_QUERYSESSIONSFORACCOUNTREQUEST']._serialized_end = 408
    _globals['_QUERYSESSIONSFORALLOCATIONREQUEST']._serialized_start = 410
    _globals['_QUERYSESSIONSFORALLOCATIONREQUEST']._serialized_end = 534
    _globals['_QUERYSESSIONSFORNODEREQUEST']._serialized_start = 536
    _globals['_QUERYSESSIONSFORNODEREQUEST']._serialized_end = 642
    _globals['_QUERYSESSIONSFORSUBSCRIPTIONREQUEST']._serialized_start = 644
    _globals['_QUERYSESSIONSFORSUBSCRIPTIONREQUEST']._serialized_end = 753
    _globals['_QUERYSESSIONREQUEST']._serialized_start = 755
    _globals['_QUERYSESSIONREQUEST']._serialized_end = 788
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 790
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 810
    _globals['_QUERYSESSIONSRESPONSE']._serialized_start = 812
    _globals['_QUERYSESSIONSRESPONSE']._serialized_end = 936
    _globals['_QUERYSESSIONSFORACCOUNTRESPONSE']._serialized_start = 939
    _globals['_QUERYSESSIONSFORACCOUNTRESPONSE']._serialized_end = 1073
    _globals['_QUERYSESSIONSFORALLOCATIONRESPONSE']._serialized_start = 1076
    _globals['_QUERYSESSIONSFORALLOCATIONRESPONSE']._serialized_end = 1213
    _globals['_QUERYSESSIONSFORNODERESPONSE']._serialized_start = 1216
    _globals['_QUERYSESSIONSFORNODERESPONSE']._serialized_end = 1347
    _globals['_QUERYSESSIONSFORSUBSCRIPTIONRESPONSE']._serialized_start = 1350
    _globals['_QUERYSESSIONSFORSUBSCRIPTIONRESPONSE']._serialized_end = 1489
    _globals['_QUERYSESSIONRESPONSE']._serialized_start = 1491
    _globals['_QUERYSESSIONRESPONSE']._serialized_end = 1552
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 1554
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 1626
    _globals['_QUERYSERVICE']._serialized_start = 1629
    _globals['_QUERYSERVICE']._serialized_end = 2875