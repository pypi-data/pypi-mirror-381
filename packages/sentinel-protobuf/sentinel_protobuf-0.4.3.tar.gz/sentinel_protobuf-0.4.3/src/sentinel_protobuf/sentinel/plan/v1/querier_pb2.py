"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/plan/v1/querier.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....sentinel.node.v1 import node_pb2 as sentinel_dot_node_dot_v1_dot_node__pb2
from ....sentinel.plan.v1 import plan_pb2 as sentinel_dot_plan_dot_v1_dot_plan__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/plan/v1/querier.proto\x12\x10sentinel.plan.v1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bsentinel/node/v1/node.proto\x1a\x1bsentinel/plan/v1/plan.proto\x1a\x1esentinel/types/v1/status.proto"z\n\x11QueryPlansRequest\x12)\n\x06status\x18\x01 \x01(\x0e2\x19.sentinel.types.v1.Status\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x96\x01\n\x1cQueryPlansForProviderRequest\x12\x0f\n\x07address\x18\x01 \x01(\t\x12)\n\x06status\x18\x02 \x01(\x0e2\x19.sentinel.types.v1.Status\x12:\n\npagination\x18\x03 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x1e\n\x10QueryPlanRequest\x12\n\n\x02id\x18\x01 \x01(\x04"b\n\x18QueryNodesForPlanRequest\x12\n\n\x02id\x18\x01 \x01(\x04\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"~\n\x12QueryPlansResponse\x12+\n\x05plans\x18\x01 \x03(\x0b2\x16.sentinel.plan.v1.PlanB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x89\x01\n\x1dQueryPlansForProviderResponse\x12+\n\x05plans\x18\x01 \x03(\x0b2\x16.sentinel.plan.v1.PlanB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"?\n\x11QueryPlanResponse\x12*\n\x04plan\x18\x01 \x01(\x0b2\x16.sentinel.plan.v1.PlanB\x04\xc8\xde\x1f\x00"\x85\x01\n\x19QueryNodesForPlanResponse\x12+\n\x05nodes\x18\x01 \x03(\x0b2\x16.sentinel.node.v1.NodeB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse2\xcf\x04\n\x0cQueryService\x12x\n\nQueryPlans\x12#.sentinel.plan.v1.QueryPlansRequest\x1a$.sentinel.plan.v1.QueryPlansResponse"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/sentinel/plan/v1/plans\x12\xad\x01\n\x15QueryPlansForProvider\x12..sentinel.plan.v1.QueryPlansForProviderRequest\x1a/.sentinel.plan.v1.QueryPlansForProviderResponse"3\x82\xd3\xe4\x93\x02-\x12+/sentinel/plan/v1/providers/{address}/plans\x12z\n\tQueryPlan\x12".sentinel.plan.v1.QueryPlanRequest\x1a#.sentinel.plan.v1.QueryPlanResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/sentinel/plan/v1/plans/{id}\x12\x98\x01\n\x11QueryNodesForPlan\x12*.sentinel.plan.v1.QueryNodesForPlanRequest\x1a+.sentinel.plan.v1.QueryNodesForPlanResponse"*\x82\xd3\xe4\x93\x02$\x12"/sentinel/plan/v1/plans/{id}/nodesBFZ<github.com/sentinel-official/sentinelhub/v12/x/plan/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.plan.v1.querier_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/sentinel-official/sentinelhub/v12/x/plan/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_QUERYPLANSRESPONSE'].fields_by_name['plans']._loaded_options = None
    _globals['_QUERYPLANSRESPONSE'].fields_by_name['plans']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYPLANSFORPROVIDERRESPONSE'].fields_by_name['plans']._loaded_options = None
    _globals['_QUERYPLANSFORPROVIDERRESPONSE'].fields_by_name['plans']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYPLANRESPONSE'].fields_by_name['plan']._loaded_options = None
    _globals['_QUERYPLANRESPONSE'].fields_by_name['plan']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYNODESFORPLANRESPONSE'].fields_by_name['nodes']._loaded_options = None
    _globals['_QUERYNODESFORPLANRESPONSE'].fields_by_name['nodes']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYSERVICE'].methods_by_name['QueryPlans']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryPlans']._serialized_options = b'\x82\xd3\xe4\x93\x02\x19\x12\x17/sentinel/plan/v1/plans'
    _globals['_QUERYSERVICE'].methods_by_name['QueryPlansForProvider']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryPlansForProvider']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/sentinel/plan/v1/providers/{address}/plans'
    _globals['_QUERYSERVICE'].methods_by_name['QueryPlan']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryPlan']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/sentinel/plan/v1/plans/{id}'
    _globals['_QUERYSERVICE'].methods_by_name['QueryNodesForPlan']._loaded_options = None
    _globals['_QUERYSERVICE'].methods_by_name['QueryNodesForPlan']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/sentinel/plan/v1/plans/{id}/nodes'
    _globals['_QUERYPLANSREQUEST']._serialized_start = 238
    _globals['_QUERYPLANSREQUEST']._serialized_end = 360
    _globals['_QUERYPLANSFORPROVIDERREQUEST']._serialized_start = 363
    _globals['_QUERYPLANSFORPROVIDERREQUEST']._serialized_end = 513
    _globals['_QUERYPLANREQUEST']._serialized_start = 515
    _globals['_QUERYPLANREQUEST']._serialized_end = 545
    _globals['_QUERYNODESFORPLANREQUEST']._serialized_start = 547
    _globals['_QUERYNODESFORPLANREQUEST']._serialized_end = 645
    _globals['_QUERYPLANSRESPONSE']._serialized_start = 647
    _globals['_QUERYPLANSRESPONSE']._serialized_end = 773
    _globals['_QUERYPLANSFORPROVIDERRESPONSE']._serialized_start = 776
    _globals['_QUERYPLANSFORPROVIDERRESPONSE']._serialized_end = 913
    _globals['_QUERYPLANRESPONSE']._serialized_start = 915
    _globals['_QUERYPLANRESPONSE']._serialized_end = 978
    _globals['_QUERYNODESFORPLANRESPONSE']._serialized_start = 981
    _globals['_QUERYNODESFORPLANRESPONSE']._serialized_end = 1114
    _globals['_QUERYSERVICE']._serialized_start = 1117
    _globals['_QUERYSERVICE']._serialized_end = 1708