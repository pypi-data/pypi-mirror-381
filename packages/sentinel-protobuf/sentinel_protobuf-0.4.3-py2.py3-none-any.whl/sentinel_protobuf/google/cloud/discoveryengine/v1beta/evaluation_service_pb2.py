"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1beta/evaluation_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1beta import evaluation_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_evaluation__pb2
from .....google.cloud.discoveryengine.v1beta import sample_query_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_sample__query__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/discoveryengine/v1beta/evaluation_service.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a4google/cloud/discoveryengine/v1beta/evaluation.proto\x1a6google/cloud/discoveryengine/v1beta/sample_query.proto\x1a#google/longrunning/operations.proto"W\n\x14GetEvaluationRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/Evaluation"\x80\x01\n\x16ListEvaluationsRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'discoveryengine.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"x\n\x17ListEvaluationsResponse\x12D\n\x0bevaluations\x18\x01 \x03(\x0b2/.google.cloud.discoveryengine.v1beta.Evaluation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xa4\x01\n\x17CreateEvaluationRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'discoveryengine.googleapis.com/Location\x12H\n\nevaluation\x18\x02 \x01(\x0b2/.google.cloud.discoveryengine.v1beta.EvaluationB\x03\xe0A\x02"\x1a\n\x18CreateEvaluationMetadata"\x8c\x01\n\x1cListEvaluationResultsRequest\x12E\n\nevaluation\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/Evaluation\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\xde\x02\n\x1dListEvaluationResultsResponse\x12o\n\x12evaluation_results\x18\x01 \x03(\x0b2S.google.cloud.discoveryengine.v1beta.ListEvaluationResultsResponse.EvaluationResult\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x1a\xb2\x01\n\x10EvaluationResult\x12K\n\x0csample_query\x18\x01 \x01(\x0b20.google.cloud.discoveryengine.v1beta.SampleQueryB\x03\xe0A\x03\x12Q\n\x0fquality_metrics\x18\x02 \x01(\x0b23.google.cloud.discoveryengine.v1beta.QualityMetricsB\x03\xe0A\x032\xbc\x08\n\x11EvaluationService\x12\xbf\x01\n\rGetEvaluation\x129.google.cloud.discoveryengine.v1beta.GetEvaluationRequest\x1a/.google.cloud.discoveryengine.v1beta.Evaluation"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1beta/{name=projects/*/locations/*/evaluations/*}\x12\xd2\x01\n\x0fListEvaluations\x12;.google.cloud.discoveryengine.v1beta.ListEvaluationsRequest\x1a<.google.cloud.discoveryengine.v1beta.ListEvaluationsResponse"D\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1beta/{parent=projects/*/locations/*}/evaluations\x12\xbe\x02\n\x10CreateEvaluation\x12<.google.cloud.discoveryengine.v1beta.CreateEvaluationRequest\x1a\x1d.google.longrunning.Operation"\xcc\x01\xcaAn\n.google.cloud.discoveryengine.v1beta.Evaluation\x12<google.cloud.discoveryengine.v1beta.CreateEvaluationMetadata\xdaA\x11parent,evaluation\x82\xd3\xe4\x93\x02A"3/v1beta/{parent=projects/*/locations/*}/evaluations:\nevaluation\x12\xfa\x01\n\x15ListEvaluationResults\x12A.google.cloud.discoveryengine.v1beta.ListEvaluationResultsRequest\x1aB.google.cloud.discoveryengine.v1beta.ListEvaluationResultsResponse"Z\xdaA\nevaluation\x82\xd3\xe4\x93\x02G\x12E/v1beta/{evaluation=projects/*/locations/*/evaluations/*}:listResults\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x9d\x02\n\'com.google.cloud.discoveryengine.v1betaB\x16EvaluationServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.evaluation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x16EvaluationServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
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
    _globals['_EVALUATIONSERVICE'].methods_by_name['GetEvaluation']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1beta/{name=projects/*/locations/*/evaluations/*}'
    _globals['_EVALUATIONSERVICE'].methods_by_name['ListEvaluations']._loaded_options = None
    _globals['_EVALUATIONSERVICE'].methods_by_name['ListEvaluations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1beta/{parent=projects/*/locations/*}/evaluations'
    _globals['_EVALUATIONSERVICE'].methods_by_name['CreateEvaluation']._loaded_options = None
    _globals['_EVALUATIONSERVICE'].methods_by_name['CreateEvaluation']._serialized_options = b'\xcaAn\n.google.cloud.discoveryengine.v1beta.Evaluation\x12<google.cloud.discoveryengine.v1beta.CreateEvaluationMetadata\xdaA\x11parent,evaluation\x82\xd3\xe4\x93\x02A"3/v1beta/{parent=projects/*/locations/*}/evaluations:\nevaluation'
    _globals['_EVALUATIONSERVICE'].methods_by_name['ListEvaluationResults']._loaded_options = None
    _globals['_EVALUATIONSERVICE'].methods_by_name['ListEvaluationResults']._serialized_options = b'\xdaA\nevaluation\x82\xd3\xe4\x93\x02G\x12E/v1beta/{evaluation=projects/*/locations/*/evaluations/*}:listResults'
    _globals['_GETEVALUATIONREQUEST']._serialized_start = 363
    _globals['_GETEVALUATIONREQUEST']._serialized_end = 450
    _globals['_LISTEVALUATIONSREQUEST']._serialized_start = 453
    _globals['_LISTEVALUATIONSREQUEST']._serialized_end = 581
    _globals['_LISTEVALUATIONSRESPONSE']._serialized_start = 583
    _globals['_LISTEVALUATIONSRESPONSE']._serialized_end = 703
    _globals['_CREATEEVALUATIONREQUEST']._serialized_start = 706
    _globals['_CREATEEVALUATIONREQUEST']._serialized_end = 870
    _globals['_CREATEEVALUATIONMETADATA']._serialized_start = 872
    _globals['_CREATEEVALUATIONMETADATA']._serialized_end = 898
    _globals['_LISTEVALUATIONRESULTSREQUEST']._serialized_start = 901
    _globals['_LISTEVALUATIONRESULTSREQUEST']._serialized_end = 1041
    _globals['_LISTEVALUATIONRESULTSRESPONSE']._serialized_start = 1044
    _globals['_LISTEVALUATIONRESULTSRESPONSE']._serialized_end = 1394
    _globals['_LISTEVALUATIONRESULTSRESPONSE_EVALUATIONRESULT']._serialized_start = 1216
    _globals['_LISTEVALUATIONRESULTSRESPONSE_EVALUATIONRESULT']._serialized_end = 1394
    _globals['_EVALUATIONSERVICE']._serialized_start = 1397
    _globals['_EVALUATIONSERVICE']._serialized_end = 2481