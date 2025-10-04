"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/endpoint.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1beta1 import explanation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_explanation__pb2
from .....google.cloud.aiplatform.v1beta1 import io_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_io__pb2
from .....google.cloud.aiplatform.v1beta1 import machine_resources_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_machine__resources__pb2
from .....google.cloud.aiplatform.v1beta1 import service_networking_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_service__networking__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/aiplatform/v1beta1/endpoint.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/aiplatform/v1beta1/encryption_spec.proto\x1a1google/cloud/aiplatform/v1beta1/explanation.proto\x1a(google/cloud/aiplatform/v1beta1/io.proto\x1a7google/cloud/aiplatform/v1beta1/machine_resources.proto\x1a8google/cloud/aiplatform/v1beta1/service_networking.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb4\x0c\n\x08Endpoint\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12L\n\x0fdeployed_models\x18\x04 \x03(\x0b2..google.cloud.aiplatform.v1beta1.DeployedModelB\x03\xe0A\x03\x12R\n\rtraffic_split\x18\x05 \x03(\x0b2;.google.cloud.aiplatform.v1beta1.Endpoint.TrafficSplitEntry\x12\x0c\n\x04etag\x18\x06 \x01(\t\x12E\n\x06labels\x18\x07 \x03(\x0b25.google.cloud.aiplatform.v1beta1.Endpoint.LabelsEntry\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12H\n\x0fencryption_spec\x18\n \x01(\x0b2/.google.cloud.aiplatform.v1beta1.EncryptionSpec\x127\n\x07network\x18\r \x01(\tB&\xe0A\x01\xfaA \n\x1ecompute.googleapis.com/Network\x12*\n\x1eenable_private_service_connect\x18\x11 \x01(\x08B\x02\x18\x01\x12i\n\x1eprivate_service_connect_config\x18\x15 \x01(\x0b2<.google.cloud.aiplatform.v1beta1.PrivateServiceConnectConfigB\x03\xe0A\x01\x12g\n\x1fmodel_deployment_monitoring_job\x18\x0e \x01(\tB>\xe0A\x03\xfaA8\n6aiplatform.googleapis.com/ModelDeploymentMonitoringJob\x12u\n\'predict_request_response_logging_config\x18\x12 \x01(\x0b2D.google.cloud.aiplatform.v1beta1.PredictRequestResponseLoggingConfig\x12"\n\x1adedicated_endpoint_enabled\x18\x18 \x01(\x08\x12#\n\x16dedicated_endpoint_dns\x18\x19 \x01(\tB\x03\xe0A\x03\x12Y\n\x18client_connection_config\x18\x17 \x01(\x0b27.google.cloud.aiplatform.v1beta1.ClientConnectionConfig\x12\x1a\n\rsatisfies_pzs\x18\x1b \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x1c \x01(\x08B\x03\xe0A\x03\x12j\n\x1fgen_ai_advanced_features_config\x18\x1d \x01(\x0b2<.google.cloud.aiplatform.v1beta1.GenAiAdvancedFeaturesConfigB\x03\xe0A\x01\x12$\n\x1cprivate_model_server_enabled\x18\x1e \x01(\x08\x1a3\n\x11TrafficSplitEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x028\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\xb5\x01\xeaA\xb1\x01\n"aiplatform.googleapis.com/Endpoint\x12<projects/{project}/locations/{location}/endpoints/{endpoint}\x12Mprojects/{project}/locations/{location}/publishers/{publisher}/models/{model}"\x86\x0b\n\rDeployedModel\x12R\n\x13dedicated_resources\x18\x07 \x01(\x0b23.google.cloud.aiplatform.v1beta1.DedicatedResourcesH\x00\x12R\n\x13automatic_resources\x18\x08 \x01(\x0b23.google.cloud.aiplatform.v1beta1.AutomaticResourcesH\x00\x12Q\n\x10shared_resources\x18\x11 \x01(\tB5\xfaA2\n0aiplatform.googleapis.com/DeploymentResourcePoolH\x00\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x05\x123\n\x05model\x18\x02 \x01(\tB$\xfaA!\n\x1faiplatform.googleapis.com/Model\x12\x1d\n\x10model_version_id\x18\x12 \x01(\tB\x03\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12J\n\x10explanation_spec\x18\t \x01(\x0b20.google.cloud.aiplatform.v1beta1.ExplanationSpec\x12\x1c\n\x14disable_explanations\x18\x13 \x01(\x08\x12\x17\n\x0fservice_account\x18\x0b \x01(\t\x12 \n\x18enable_container_logging\x18\x0c \x01(\x08\x12!\n\x19disable_container_logging\x18\x0f \x01(\x08\x12\x1d\n\x15enable_access_logging\x18\r \x01(\x08\x12Q\n\x11private_endpoints\x18\x0e \x01(\x0b21.google.cloud.aiplatform.v1beta1.PrivateEndpointsB\x03\xe0A\x03\x12Y\n\x18faster_deployment_config\x18\x17 \x01(\x0b27.google.cloud.aiplatform.v1beta1.FasterDeploymentConfig\x12H\n\x0frollout_options\x18\x19 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.RolloutOptions\x12J\n\x06status\x18\x1a \x01(\x0b25.google.cloud.aiplatform.v1beta1.DeployedModel.StatusB\x03\xe0A\x03\x12W\n\rsystem_labels\x18\x1c \x03(\x0b2@.google.cloud.aiplatform.v1beta1.DeployedModel.SystemLabelsEntry\x12\x15\n\rcheckpoint_id\x18\x1d \x01(\t\x12`\n\x19speculative_decoding_spec\x18\x1e \x01(\x0b28.google.cloud.aiplatform.v1beta1.SpeculativeDecodingSpecB\x03\xe0A\x01\x1a\x7f\n\x06Status\x12\x14\n\x07message\x18\x01 \x01(\tB\x03\xe0A\x03\x129\n\x10last_update_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12$\n\x17available_replica_count\x18\x03 \x01(\x05B\x03\xe0A\x03\x1a3\n\x11SystemLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x16\n\x14prediction_resources"\x8f\x01\n\x10PrivateEndpoints\x12\x1d\n\x10predict_http_uri\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10explain_http_uri\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x1c\n\x0fhealth_http_uri\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x1f\n\x12service_attachment\x18\x04 \x01(\tB\x03\xe0A\x03"\xf4\x01\n#PredictRequestResponseLoggingConfig\x12\x0f\n\x07enabled\x18\x01 \x01(\x08\x12\x15\n\rsampling_rate\x18\x02 \x01(\x01\x12R\n\x14bigquery_destination\x18\x03 \x01(\x0b24.google.cloud.aiplatform.v1beta1.BigQueryDestination\x124\n\'request_response_logging_schema_version\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x13enable_otel_logging\x18\x06 \x01(\x08"t\n\x14PublisherModelConfig\x12\\\n\x0elogging_config\x18\x03 \x01(\x0b2D.google.cloud.aiplatform.v1beta1.PredictRequestResponseLoggingConfig"N\n\x16ClientConnectionConfig\x124\n\x11inference_timeout\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration"5\n\x16FasterDeploymentConfig\x12\x1b\n\x13fast_tryout_enabled\x18\x02 \x01(\x08"\xf7\x01\n\x0eRolloutOptions\x12"\n\x18max_unavailable_replicas\x18\x03 \x01(\x05H\x00\x12$\n\x1amax_unavailable_percentage\x18\x04 \x01(\x05H\x00\x12\x1c\n\x12max_surge_replicas\x18\x05 \x01(\x05H\x01\x12\x1e\n\x14max_surge_percentage\x18\x06 \x01(\x05H\x01\x12\x1f\n\x17previous_deployed_model\x18\x01 \x01(\t\x12\x1c\n\x0frevision_number\x18\x02 \x01(\x05B\x03\xe0A\x03B\x11\n\x0fmax_unavailableB\x0b\n\tmax_surge"\x9a\x01\n\x1bGenAiAdvancedFeaturesConfig\x12Z\n\nrag_config\x18\x01 \x01(\x0b2F.google.cloud.aiplatform.v1beta1.GenAiAdvancedFeaturesConfig.RagConfig\x1a\x1f\n\tRagConfig\x12\x12\n\nenable_rag\x18\x01 \x01(\x08"\xa3\x03\n\x17SpeculativeDecodingSpec\x12q\n\x17draft_model_speculation\x18\x02 \x01(\x0b2N.google.cloud.aiplatform.v1beta1.SpeculativeDecodingSpec.DraftModelSpeculationH\x00\x12f\n\x11ngram_speculation\x18\x03 \x01(\x0b2I.google.cloud.aiplatform.v1beta1.SpeculativeDecodingSpec.NgramSpeculationH\x00\x12\x1f\n\x17speculative_token_count\x18\x01 \x01(\x05\x1aU\n\x15DraftModelSpeculation\x12<\n\x0bdraft_model\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model\x1a&\n\x10NgramSpeculation\x12\x12\n\nngram_size\x18\x01 \x01(\x05B\r\n\x0bspeculationB\xe4\x01\n#com.google.cloud.aiplatform.v1beta1B\rEndpointProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.endpoint_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\rEndpointProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_ENDPOINT_TRAFFICSPLITENTRY']._loaded_options = None
    _globals['_ENDPOINT_TRAFFICSPLITENTRY']._serialized_options = b'8\x01'
    _globals['_ENDPOINT_LABELSENTRY']._loaded_options = None
    _globals['_ENDPOINT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ENDPOINT'].fields_by_name['name']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINT'].fields_by_name['display_name']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_ENDPOINT'].fields_by_name['deployed_models']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['deployed_models']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINT'].fields_by_name['create_time']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINT'].fields_by_name['update_time']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINT'].fields_by_name['network']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['network']._serialized_options = b'\xe0A\x01\xfaA \n\x1ecompute.googleapis.com/Network'
    _globals['_ENDPOINT'].fields_by_name['enable_private_service_connect']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['enable_private_service_connect']._serialized_options = b'\x18\x01'
    _globals['_ENDPOINT'].fields_by_name['private_service_connect_config']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['private_service_connect_config']._serialized_options = b'\xe0A\x01'
    _globals['_ENDPOINT'].fields_by_name['model_deployment_monitoring_job']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['model_deployment_monitoring_job']._serialized_options = b'\xe0A\x03\xfaA8\n6aiplatform.googleapis.com/ModelDeploymentMonitoringJob'
    _globals['_ENDPOINT'].fields_by_name['dedicated_endpoint_dns']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['dedicated_endpoint_dns']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINT'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINT'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_ENDPOINT'].fields_by_name['gen_ai_advanced_features_config']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['gen_ai_advanced_features_config']._serialized_options = b'\xe0A\x01'
    _globals['_ENDPOINT']._loaded_options = None
    _globals['_ENDPOINT']._serialized_options = b'\xeaA\xb1\x01\n"aiplatform.googleapis.com/Endpoint\x12<projects/{project}/locations/{location}/endpoints/{endpoint}\x12Mprojects/{project}/locations/{location}/publishers/{publisher}/models/{model}'
    _globals['_DEPLOYEDMODEL_STATUS'].fields_by_name['message']._loaded_options = None
    _globals['_DEPLOYEDMODEL_STATUS'].fields_by_name['message']._serialized_options = b'\xe0A\x03'
    _globals['_DEPLOYEDMODEL_STATUS'].fields_by_name['last_update_time']._loaded_options = None
    _globals['_DEPLOYEDMODEL_STATUS'].fields_by_name['last_update_time']._serialized_options = b'\xe0A\x03'
    _globals['_DEPLOYEDMODEL_STATUS'].fields_by_name['available_replica_count']._loaded_options = None
    _globals['_DEPLOYEDMODEL_STATUS'].fields_by_name['available_replica_count']._serialized_options = b'\xe0A\x03'
    _globals['_DEPLOYEDMODEL_SYSTEMLABELSENTRY']._loaded_options = None
    _globals['_DEPLOYEDMODEL_SYSTEMLABELSENTRY']._serialized_options = b'8\x01'
    _globals['_DEPLOYEDMODEL'].fields_by_name['shared_resources']._loaded_options = None
    _globals['_DEPLOYEDMODEL'].fields_by_name['shared_resources']._serialized_options = b'\xfaA2\n0aiplatform.googleapis.com/DeploymentResourcePool'
    _globals['_DEPLOYEDMODEL'].fields_by_name['id']._loaded_options = None
    _globals['_DEPLOYEDMODEL'].fields_by_name['id']._serialized_options = b'\xe0A\x05'
    _globals['_DEPLOYEDMODEL'].fields_by_name['model']._loaded_options = None
    _globals['_DEPLOYEDMODEL'].fields_by_name['model']._serialized_options = b'\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_DEPLOYEDMODEL'].fields_by_name['model_version_id']._loaded_options = None
    _globals['_DEPLOYEDMODEL'].fields_by_name['model_version_id']._serialized_options = b'\xe0A\x03'
    _globals['_DEPLOYEDMODEL'].fields_by_name['create_time']._loaded_options = None
    _globals['_DEPLOYEDMODEL'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DEPLOYEDMODEL'].fields_by_name['private_endpoints']._loaded_options = None
    _globals['_DEPLOYEDMODEL'].fields_by_name['private_endpoints']._serialized_options = b'\xe0A\x03'
    _globals['_DEPLOYEDMODEL'].fields_by_name['status']._loaded_options = None
    _globals['_DEPLOYEDMODEL'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_DEPLOYEDMODEL'].fields_by_name['speculative_decoding_spec']._loaded_options = None
    _globals['_DEPLOYEDMODEL'].fields_by_name['speculative_decoding_spec']._serialized_options = b'\xe0A\x01'
    _globals['_PRIVATEENDPOINTS'].fields_by_name['predict_http_uri']._loaded_options = None
    _globals['_PRIVATEENDPOINTS'].fields_by_name['predict_http_uri']._serialized_options = b'\xe0A\x03'
    _globals['_PRIVATEENDPOINTS'].fields_by_name['explain_http_uri']._loaded_options = None
    _globals['_PRIVATEENDPOINTS'].fields_by_name['explain_http_uri']._serialized_options = b'\xe0A\x03'
    _globals['_PRIVATEENDPOINTS'].fields_by_name['health_http_uri']._loaded_options = None
    _globals['_PRIVATEENDPOINTS'].fields_by_name['health_http_uri']._serialized_options = b'\xe0A\x03'
    _globals['_PRIVATEENDPOINTS'].fields_by_name['service_attachment']._loaded_options = None
    _globals['_PRIVATEENDPOINTS'].fields_by_name['service_attachment']._serialized_options = b'\xe0A\x03'
    _globals['_PREDICTREQUESTRESPONSELOGGINGCONFIG'].fields_by_name['request_response_logging_schema_version']._loaded_options = None
    _globals['_PREDICTREQUESTRESPONSELOGGINGCONFIG'].fields_by_name['request_response_logging_schema_version']._serialized_options = b'\xe0A\x03'
    _globals['_ROLLOUTOPTIONS'].fields_by_name['revision_number']._loaded_options = None
    _globals['_ROLLOUTOPTIONS'].fields_by_name['revision_number']._serialized_options = b'\xe0A\x03'
    _globals['_SPECULATIVEDECODINGSPEC_DRAFTMODELSPECULATION'].fields_by_name['draft_model']._loaded_options = None
    _globals['_SPECULATIVEDECODINGSPEC_DRAFTMODELSPECULATION'].fields_by_name['draft_model']._serialized_options = b'\xe0A\x02\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_ENDPOINT']._serialized_start = 472
    _globals['_ENDPOINT']._serialized_end = 2060
    _globals['_ENDPOINT_TRAFFICSPLITENTRY']._serialized_start = 1778
    _globals['_ENDPOINT_TRAFFICSPLITENTRY']._serialized_end = 1829
    _globals['_ENDPOINT_LABELSENTRY']._serialized_start = 1831
    _globals['_ENDPOINT_LABELSENTRY']._serialized_end = 1876
    _globals['_DEPLOYEDMODEL']._serialized_start = 2063
    _globals['_DEPLOYEDMODEL']._serialized_end = 3477
    _globals['_DEPLOYEDMODEL_STATUS']._serialized_start = 3273
    _globals['_DEPLOYEDMODEL_STATUS']._serialized_end = 3400
    _globals['_DEPLOYEDMODEL_SYSTEMLABELSENTRY']._serialized_start = 3402
    _globals['_DEPLOYEDMODEL_SYSTEMLABELSENTRY']._serialized_end = 3453
    _globals['_PRIVATEENDPOINTS']._serialized_start = 3480
    _globals['_PRIVATEENDPOINTS']._serialized_end = 3623
    _globals['_PREDICTREQUESTRESPONSELOGGINGCONFIG']._serialized_start = 3626
    _globals['_PREDICTREQUESTRESPONSELOGGINGCONFIG']._serialized_end = 3870
    _globals['_PUBLISHERMODELCONFIG']._serialized_start = 3872
    _globals['_PUBLISHERMODELCONFIG']._serialized_end = 3988
    _globals['_CLIENTCONNECTIONCONFIG']._serialized_start = 3990
    _globals['_CLIENTCONNECTIONCONFIG']._serialized_end = 4068
    _globals['_FASTERDEPLOYMENTCONFIG']._serialized_start = 4070
    _globals['_FASTERDEPLOYMENTCONFIG']._serialized_end = 4123
    _globals['_ROLLOUTOPTIONS']._serialized_start = 4126
    _globals['_ROLLOUTOPTIONS']._serialized_end = 4373
    _globals['_GENAIADVANCEDFEATURESCONFIG']._serialized_start = 4376
    _globals['_GENAIADVANCEDFEATURESCONFIG']._serialized_end = 4530
    _globals['_GENAIADVANCEDFEATURESCONFIG_RAGCONFIG']._serialized_start = 4499
    _globals['_GENAIADVANCEDFEATURESCONFIG_RAGCONFIG']._serialized_end = 4530
    _globals['_SPECULATIVEDECODINGSPEC']._serialized_start = 4533
    _globals['_SPECULATIVEDECODINGSPEC']._serialized_end = 4952
    _globals['_SPECULATIVEDECODINGSPEC_DRAFTMODELSPECULATION']._serialized_start = 4812
    _globals['_SPECULATIVEDECODINGSPEC_DRAFTMODELSPECULATION']._serialized_end = 4897
    _globals['_SPECULATIVEDECODINGSPEC_NGRAMSPECULATION']._serialized_start = 4899
    _globals['_SPECULATIVEDECODINGSPEC_NGRAMSPECULATION']._serialized_end = 4937