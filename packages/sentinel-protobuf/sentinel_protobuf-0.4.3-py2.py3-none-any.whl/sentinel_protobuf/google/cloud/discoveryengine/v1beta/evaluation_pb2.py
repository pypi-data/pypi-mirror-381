"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1beta/evaluation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1beta import search_service_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_search__service__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/discoveryengine/v1beta/evaluation.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a8google/cloud/discoveryengine/v1beta/search_service.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xe3\x07\n\nEvaluation\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\\\n\x0fevaluation_spec\x18\x02 \x01(\x0b2>.google.cloud.discoveryengine.v1beta.Evaluation.EvaluationSpecB\x03\xe0A\x02\x12Q\n\x0fquality_metrics\x18\x03 \x01(\x0b23.google.cloud.discoveryengine.v1beta.QualityMetricsB\x03\xe0A\x03\x12I\n\x05state\x18\x04 \x01(\x0e25.google.cloud.discoveryengine.v1beta.Evaluation.StateB\x03\xe0A\x03\x12&\n\x05error\x18\x05 \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12.\n\rerror_samples\x18\x08 \x03(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x1a\xbd\x02\n\x0eEvaluationSpec\x12Q\n\x0esearch_request\x18\x02 \x01(\x0b22.google.cloud.discoveryengine.v1beta.SearchRequestB\x03\xe0A\x02H\x00\x12h\n\x0equery_set_spec\x18\x01 \x01(\x0b2K.google.cloud.discoveryengine.v1beta.Evaluation.EvaluationSpec.QuerySetSpecB\x03\xe0A\x02\x1a_\n\x0cQuerySetSpec\x12O\n\x10sample_query_set\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-discoveryengine.googleapis.com/SampleQuerySetB\r\n\x0bsearch_spec"S\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\n\n\x06FAILED\x10\x04:p\xeaAm\n)discoveryengine.googleapis.com/Evaluation\x12@projects/{project}/locations/{location}/evaluations/{evaluation}"\x86\x04\n\x0eQualityMetrics\x12S\n\ndoc_recall\x18\x01 \x01(\x0b2?.google.cloud.discoveryengine.v1beta.QualityMetrics.TopkMetrics\x12V\n\rdoc_precision\x18\x02 \x01(\x0b2?.google.cloud.discoveryengine.v1beta.QualityMetrics.TopkMetrics\x12Q\n\x08doc_ndcg\x18\x03 \x01(\x0b2?.google.cloud.discoveryengine.v1beta.QualityMetrics.TopkMetrics\x12T\n\x0bpage_recall\x18\x04 \x01(\x0b2?.google.cloud.discoveryengine.v1beta.QualityMetrics.TopkMetrics\x12R\n\tpage_ndcg\x18\x05 \x01(\x0b2?.google.cloud.discoveryengine.v1beta.QualityMetrics.TopkMetrics\x1aJ\n\x0bTopkMetrics\x12\r\n\x05top_1\x18\x01 \x01(\x01\x12\r\n\x05top_3\x18\x02 \x01(\x01\x12\r\n\x05top_5\x18\x03 \x01(\x01\x12\x0e\n\x06top_10\x18\x04 \x01(\x01B\x96\x02\n\'com.google.cloud.discoveryengine.v1betaB\x0fEvaluationProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.evaluation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x0fEvaluationProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
    _globals['_EVALUATION_EVALUATIONSPEC_QUERYSETSPEC'].fields_by_name['sample_query_set']._loaded_options = None
    _globals['_EVALUATION_EVALUATIONSPEC_QUERYSETSPEC'].fields_by_name['sample_query_set']._serialized_options = b'\xe0A\x02\xfaA/\n-discoveryengine.googleapis.com/SampleQuerySet'
    _globals['_EVALUATION_EVALUATIONSPEC'].fields_by_name['search_request']._loaded_options = None
    _globals['_EVALUATION_EVALUATIONSPEC'].fields_by_name['search_request']._serialized_options = b'\xe0A\x02'
    _globals['_EVALUATION_EVALUATIONSPEC'].fields_by_name['query_set_spec']._loaded_options = None
    _globals['_EVALUATION_EVALUATIONSPEC'].fields_by_name['query_set_spec']._serialized_options = b'\xe0A\x02'
    _globals['_EVALUATION'].fields_by_name['name']._loaded_options = None
    _globals['_EVALUATION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_EVALUATION'].fields_by_name['evaluation_spec']._loaded_options = None
    _globals['_EVALUATION'].fields_by_name['evaluation_spec']._serialized_options = b'\xe0A\x02'
    _globals['_EVALUATION'].fields_by_name['quality_metrics']._loaded_options = None
    _globals['_EVALUATION'].fields_by_name['quality_metrics']._serialized_options = b'\xe0A\x03'
    _globals['_EVALUATION'].fields_by_name['state']._loaded_options = None
    _globals['_EVALUATION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_EVALUATION'].fields_by_name['error']._loaded_options = None
    _globals['_EVALUATION'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_EVALUATION'].fields_by_name['create_time']._loaded_options = None
    _globals['_EVALUATION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_EVALUATION'].fields_by_name['end_time']._loaded_options = None
    _globals['_EVALUATION'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_EVALUATION'].fields_by_name['error_samples']._loaded_options = None
    _globals['_EVALUATION'].fields_by_name['error_samples']._serialized_options = b'\xe0A\x03'
    _globals['_EVALUATION']._loaded_options = None
    _globals['_EVALUATION']._serialized_options = b'\xeaAm\n)discoveryengine.googleapis.com/Evaluation\x12@projects/{project}/locations/{location}/evaluations/{evaluation}'
    _globals['_EVALUATION']._serialized_start = 270
    _globals['_EVALUATION']._serialized_end = 1265
    _globals['_EVALUATION_EVALUATIONSPEC']._serialized_start = 749
    _globals['_EVALUATION_EVALUATIONSPEC']._serialized_end = 1066
    _globals['_EVALUATION_EVALUATIONSPEC_QUERYSETSPEC']._serialized_start = 956
    _globals['_EVALUATION_EVALUATIONSPEC_QUERYSETSPEC']._serialized_end = 1051
    _globals['_EVALUATION_STATE']._serialized_start = 1068
    _globals['_EVALUATION_STATE']._serialized_end = 1151
    _globals['_QUALITYMETRICS']._serialized_start = 1268
    _globals['_QUALITYMETRICS']._serialized_end = 1786
    _globals['_QUALITYMETRICS_TOPKMETRICS']._serialized_start = 1712
    _globals['_QUALITYMETRICS_TOPKMETRICS']._serialized_end = 1786