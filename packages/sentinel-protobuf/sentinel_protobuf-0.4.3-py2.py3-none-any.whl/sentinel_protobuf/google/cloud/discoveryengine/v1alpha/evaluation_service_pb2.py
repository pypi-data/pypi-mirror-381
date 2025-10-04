"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1alpha/evaluation_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1alpha import evaluation_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_evaluation__pb2
from .....google.cloud.discoveryengine.v1alpha import sample_query_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_sample__query__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/discoveryengine/v1alpha/evaluation_service.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/discoveryengine/v1alpha/evaluation.proto\x1a7google/cloud/discoveryengine/v1alpha/sample_query.proto\x1a#google/longrunning/operations.proto"W\n\x14GetEvaluationRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/Evaluation"\x80\x01\n\x16ListEvaluationsRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'discoveryengine.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"y\n\x17ListEvaluationsResponse\x12E\n\x0bevaluations\x18\x01 \x03(\x0b20.google.cloud.discoveryengine.v1alpha.Evaluation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xa5\x01\n\x17CreateEvaluationRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'discoveryengine.googleapis.com/Location\x12I\n\nevaluation\x18\x02 \x01(\x0b20.google.cloud.discoveryengine.v1alpha.EvaluationB\x03\xe0A\x02"\x1a\n\x18CreateEvaluationMetadata"\x8c\x01\n\x1cListEvaluationResultsRequest\x12E\n\nevaluation\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/Evaluation\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\xe1\x02\n\x1dListEvaluationResultsResponse\x12p\n\x12evaluation_results\x18\x01 \x03(\x0b2T.google.cloud.discoveryengine.v1alpha.ListEvaluationResultsResponse.EvaluationResult\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x1a\xb4\x01\n\x10EvaluationResult\x12L\n\x0csample_query\x18\x01 \x01(\x0b21.google.cloud.discoveryengine.v1alpha.SampleQueryB\x03\xe0A\x03\x12R\n\x0fquality_metrics\x18\x02 \x01(\x0b24.google.cloud.discoveryengine.v1alpha.QualityMetricsB\x03\xe0A\x032\xc9\x08\n\x11EvaluationService\x12\xc2\x01\n\rGetEvaluation\x12:.google.cloud.discoveryengine.v1alpha.GetEvaluationRequest\x1a0.google.cloud.discoveryengine.v1alpha.Evaluation"C\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v1alpha/{name=projects/*/locations/*/evaluations/*}\x12\xd5\x01\n\x0fListEvaluations\x12<.google.cloud.discoveryengine.v1alpha.ListEvaluationsRequest\x1a=.google.cloud.discoveryengine.v1alpha.ListEvaluationsResponse"E\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v1alpha/{parent=projects/*/locations/*}/evaluations\x12\xc2\x02\n\x10CreateEvaluation\x12=.google.cloud.discoveryengine.v1alpha.CreateEvaluationRequest\x1a\x1d.google.longrunning.Operation"\xcf\x01\xcaAp\n/google.cloud.discoveryengine.v1alpha.Evaluation\x12=google.cloud.discoveryengine.v1alpha.CreateEvaluationMetadata\xdaA\x11parent,evaluation\x82\xd3\xe4\x93\x02B"4/v1alpha/{parent=projects/*/locations/*}/evaluations:\nevaluation\x12\xfd\x01\n\x15ListEvaluationResults\x12B.google.cloud.discoveryengine.v1alpha.ListEvaluationResultsRequest\x1aC.google.cloud.discoveryengine.v1alpha.ListEvaluationResultsResponse"[\xdaA\nevaluation\x82\xd3\xe4\x93\x02H\x12F/v1alpha/{evaluation=projects/*/locations/*/evaluations/*}:listResults\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa2\x02\n(com.google.cloud.discoveryengine.v1alphaB\x16EvaluationServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.evaluation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x16EvaluationServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_GETEVALUATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETEVALUATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/Evaluation'
    _globals['_LISTEVALUATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTEVALUATIONSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\n'discoveryengine.googleapis.com/Location"
    _globals['_CREATEEVALUATIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEEVALUATIONREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\n'discoveryengine.googleapis.com/Location"
    _globals['_CREATEEVALUATIONREQUEST'].fields_by_name['evaluation']._loaded_options = None
    _globals['_CREATEEVALUATIONREQUEST'].fields_by_name['evaluation']._serialized_options = b'\xe0A\x02'
    _globals['_LISTEVALUATIONRESULTSREQUEST'].fields_by_name['evaluation']._loaded_options = None
    _globals['_LISTEVALUATIONRESULTSREQUEST'].fields_by_name['evaluation']._serialized_options = b'\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/Evaluation'
    _globals['_LISTEVALUATIONRESULTSRESPONSE_EVALUATIONRESULT'].fields_by_name['sample_query']._loaded_options = None
    _globals['_LISTEVALUATIONRESULTSRESPONSE_EVALUATIONRESULT'].fields_by_name['sample_query']._serialized_options = b'\xe0A\x03'
    _globals['_LISTEVALUATIONRESULTSRESPONSE_EVALUATIONRESULT'].fields_by_name['quality_metrics']._loaded_options = None
    _globals['_LISTEVALUATIONRESULTSRESPONSE_EVALUATIONRESULT'].fields_by_name['quality_metrics']._serialized_options = b'\xe0A\x03'
    _globals['_EVALUATIONSERVICE']._loaded_options = None
    _globals['_EVALUATIONSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_EVALUATIONSERVICE'].methods_by_name['GetEvaluation']._loaded_options = None
    _globals['_EVALUATIONSERVICE'].methods_by_name['GetEvaluation']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v1alpha/{name=projects/*/locations/*/evaluations/*}'
    _globals['_EVALUATIONSERVICE'].methods_by_name['ListEvaluations']._loaded_options = None
    _globals['_EVALUATIONSERVICE'].methods_by_name['ListEvaluations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v1alpha/{parent=projects/*/locations/*}/evaluations'
    _globals['_EVALUATIONSERVICE'].methods_by_name['CreateEvaluation']._loaded_options = None
    _globals['_EVALUATIONSERVICE'].methods_by_name['CreateEvaluation']._serialized_options = b'\xcaAp\n/google.cloud.discoveryengine.v1alpha.Evaluation\x12=google.cloud.discoveryengine.v1alpha.CreateEvaluationMetadata\xdaA\x11parent,evaluation\x82\xd3\xe4\x93\x02B"4/v1alpha/{parent=projects/*/locations/*}/evaluations:\nevaluation'
    _globals['_EVALUATIONSERVICE'].methods_by_name['ListEvaluationResults']._loaded_options = None
    _globals['_EVALUATIONSERVICE'].methods_by_name['ListEvaluationResults']._serialized_options = b'\xdaA\nevaluation\x82\xd3\xe4\x93\x02H\x12F/v1alpha/{evaluation=projects/*/locations/*/evaluations/*}:listResults'
    _globals['_GETEVALUATIONREQUEST']._serialized_start = 367
    _globals['_GETEVALUATIONREQUEST']._serialized_end = 454
    _globals['_LISTEVALUATIONSREQUEST']._serialized_start = 457
    _globals['_LISTEVALUATIONSREQUEST']._serialized_end = 585
    _globals['_LISTEVALUATIONSRESPONSE']._serialized_start = 587
    _globals['_LISTEVALUATIONSRESPONSE']._serialized_end = 708
    _globals['_CREATEEVALUATIONREQUEST']._serialized_start = 711
    _globals['_CREATEEVALUATIONREQUEST']._serialized_end = 876
    _globals['_CREATEEVALUATIONMETADATA']._serialized_start = 878
    _globals['_CREATEEVALUATIONMETADATA']._serialized_end = 904
    _globals['_LISTEVALUATIONRESULTSREQUEST']._serialized_start = 907
    _globals['_LISTEVALUATIONRESULTSREQUEST']._serialized_end = 1047
    _globals['_LISTEVALUATIONRESULTSRESPONSE']._serialized_start = 1050
    _globals['_LISTEVALUATIONRESULTSRESPONSE']._serialized_end = 1403
    _globals['_LISTEVALUATIONRESULTSRESPONSE_EVALUATIONRESULT']._serialized_start = 1223
    _globals['_LISTEVALUATIONRESULTSRESPONSE_EVALUATIONRESULT']._serialized_end = 1403
    _globals['_EVALUATIONSERVICE']._serialized_start = 1406
    _globals['_EVALUATIONSERVICE']._serialized_end = 2503