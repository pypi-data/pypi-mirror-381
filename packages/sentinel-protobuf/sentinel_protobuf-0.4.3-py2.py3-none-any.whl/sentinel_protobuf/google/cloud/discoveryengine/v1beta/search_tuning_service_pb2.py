"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1beta/search_tuning_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1beta import custom_tuning_model_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_custom__tuning__model__pb2
from .....google.cloud.discoveryengine.v1beta import import_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_import__config__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/discoveryengine/v1beta/search_tuning_service.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a=google/cloud/discoveryengine/v1beta/custom_tuning_model.proto\x1a7google/cloud/discoveryengine/v1beta/import_config.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"_\n\x17ListCustomModelsRequest\x12D\n\ndata_store\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore"b\n\x18ListCustomModelsResponse\x12F\n\x06models\x18\x01 \x03(\x0b26.google.cloud.discoveryengine.v1beta.CustomTuningModel"\xca\x03\n\x17TrainCustomModelRequest\x12k\n\x12gcs_training_input\x18\x02 \x01(\x0b2M.google.cloud.discoveryengine.v1beta.TrainCustomModelRequest.GcsTrainingInputH\x00\x12D\n\ndata_store\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x12\x12\n\nmodel_type\x18\x03 \x01(\t\x12L\n\x0cerror_config\x18\x04 \x01(\x0b26.google.cloud.discoveryengine.v1beta.ImportErrorConfig\x12\x10\n\x08model_id\x18\x05 \x01(\t\x1av\n\x10GcsTrainingInput\x12\x18\n\x10corpus_data_path\x18\x01 \x01(\t\x12\x17\n\x0fquery_data_path\x18\x02 \x01(\t\x12\x17\n\x0ftrain_data_path\x18\x03 \x01(\t\x12\x16\n\x0etest_data_path\x18\x04 \x01(\tB\x10\n\x0etraining_input"\xca\x02\n\x18TrainCustomModelResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12L\n\x0cerror_config\x18\x02 \x01(\x0b26.google.cloud.discoveryengine.v1beta.ImportErrorConfig\x12\x14\n\x0cmodel_status\x18\x03 \x01(\t\x12[\n\x07metrics\x18\x04 \x03(\x0b2J.google.cloud.discoveryengine.v1beta.TrainCustomModelResponse.MetricsEntry\x12\x12\n\nmodel_name\x18\x05 \x01(\t\x1a.\n\x0cMetricsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x028\x01"|\n\x18TrainCustomModelMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp2\xae\x05\n\x13SearchTuningService\x12\xd3\x02\n\x10TrainCustomModel\x12<.google.cloud.discoveryengine.v1beta.TrainCustomModelRequest\x1a\x1d.google.longrunning.Operation"\xe1\x01\xcaA|\n<google.cloud.discoveryengine.v1beta.TrainCustomModelResponse\x12<google.cloud.discoveryengine.v1beta.TrainCustomModelMetadata\x82\xd3\xe4\x93\x02\\"W/v1beta/{data_store=projects/*/locations/*/collections/*/dataStores/*}:trainCustomModel:\x01*\x12\xec\x01\n\x10ListCustomModels\x12<.google.cloud.discoveryengine.v1beta.ListCustomModelsRequest\x1a=.google.cloud.discoveryengine.v1beta.ListCustomModelsResponse"[\x82\xd3\xe4\x93\x02U\x12S/v1beta/{data_store=projects/*/locations/*/collections/*/dataStores/*}/customModels\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x9f\x02\n\'com.google.cloud.discoveryengine.v1betaB\x18SearchTuningServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.search_tuning_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x18SearchTuningServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
    _globals['_LISTCUSTOMMODELSREQUEST'].fields_by_name['data_store']._loaded_options = None
    _globals['_LISTCUSTOMMODELSREQUEST'].fields_by_name['data_store']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_TRAINCUSTOMMODELREQUEST'].fields_by_name['data_store']._loaded_options = None
    _globals['_TRAINCUSTOMMODELREQUEST'].fields_by_name['data_store']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_TRAINCUSTOMMODELRESPONSE_METRICSENTRY']._loaded_options = None
    _globals['_TRAINCUSTOMMODELRESPONSE_METRICSENTRY']._serialized_options = b'8\x01'
    _globals['_SEARCHTUNINGSERVICE']._loaded_options = None
    _globals['_SEARCHTUNINGSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SEARCHTUNINGSERVICE'].methods_by_name['TrainCustomModel']._loaded_options = None
    _globals['_SEARCHTUNINGSERVICE'].methods_by_name['TrainCustomModel']._serialized_options = b'\xcaA|\n<google.cloud.discoveryengine.v1beta.TrainCustomModelResponse\x12<google.cloud.discoveryengine.v1beta.TrainCustomModelMetadata\x82\xd3\xe4\x93\x02\\"W/v1beta/{data_store=projects/*/locations/*/collections/*/dataStores/*}:trainCustomModel:\x01*'
    _globals['_SEARCHTUNINGSERVICE'].methods_by_name['ListCustomModels']._loaded_options = None
    _globals['_SEARCHTUNINGSERVICE'].methods_by_name['ListCustomModels']._serialized_options = b'\x82\xd3\xe4\x93\x02U\x12S/v1beta/{data_store=projects/*/locations/*/collections/*/dataStores/*}/customModels'
    _globals['_LISTCUSTOMMODELSREQUEST']._serialized_start = 434
    _globals['_LISTCUSTOMMODELSREQUEST']._serialized_end = 529
    _globals['_LISTCUSTOMMODELSRESPONSE']._serialized_start = 531
    _globals['_LISTCUSTOMMODELSRESPONSE']._serialized_end = 629
    _globals['_TRAINCUSTOMMODELREQUEST']._serialized_start = 632
    _globals['_TRAINCUSTOMMODELREQUEST']._serialized_end = 1090
    _globals['_TRAINCUSTOMMODELREQUEST_GCSTRAININGINPUT']._serialized_start = 954
    _globals['_TRAINCUSTOMMODELREQUEST_GCSTRAININGINPUT']._serialized_end = 1072
    _globals['_TRAINCUSTOMMODELRESPONSE']._serialized_start = 1093
    _globals['_TRAINCUSTOMMODELRESPONSE']._serialized_end = 1423
    _globals['_TRAINCUSTOMMODELRESPONSE_METRICSENTRY']._serialized_start = 1377
    _globals['_TRAINCUSTOMMODELRESPONSE_METRICSENTRY']._serialized_end = 1423
    _globals['_TRAINCUSTOMMODELMETADATA']._serialized_start = 1425
    _globals['_TRAINCUSTOMMODELMETADATA']._serialized_end = 1549
    _globals['_SEARCHTUNINGSERVICE']._serialized_start = 1552
    _globals['_SEARCHTUNINGSERVICE']._serialized_end = 2238