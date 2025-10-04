"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/model.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import deployed_model_ref_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_deployed__model__ref__pb2
from .....google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1beta1 import env_var_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_env__var__pb2
from .....google.cloud.aiplatform.v1beta1 import explanation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_explanation__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/aiplatform/v1beta1/model.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a8google/cloud/aiplatform/v1beta1/deployed_model_ref.proto\x1a5google/cloud/aiplatform/v1beta1/encryption_spec.proto\x1a-google/cloud/aiplatform/v1beta1/env_var.proto\x1a1google/cloud/aiplatform/v1beta1/explanation.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x81\x14\n\x05Model\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1a\n\nversion_id\x18\x1c \x01(\tB\x06\xe0A\x05\xe0A\x03\x12\x17\n\x0fversion_aliases\x18\x1d \x03(\t\x12<\n\x13version_create_time\x18\x1f \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12<\n\x13version_update_time\x18  \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12\x1b\n\x13version_description\x18\x1e \x01(\t\x12\x1d\n\x15default_checkpoint_id\x185 \x01(\t\x12J\n\x10predict_schemata\x18\x04 \x01(\x0b20.google.cloud.aiplatform.v1beta1.PredictSchemata\x12 \n\x13metadata_schema_uri\x18\x05 \x01(\tB\x03\xe0A\x05\x12-\n\x08metadata\x18\x06 \x01(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x05\x12Z\n\x18supported_export_formats\x18\x14 \x03(\x0b23.google.cloud.aiplatform.v1beta1.Model.ExportFormatB\x03\xe0A\x03\x12M\n\x11training_pipeline\x18\x07 \x01(\tB2\xe0A\x03\xfaA,\n*aiplatform.googleapis.com/TrainingPipeline\x12P\n\x0econtainer_spec\x18\t \x01(\x0b23.google.cloud.aiplatform.v1beta1.ModelContainerSpecB\x03\xe0A\x04\x12\x19\n\x0cartifact_uri\x18\x1a \x01(\tB\x03\xe0A\x05\x12q\n$supported_deployment_resources_types\x18\n \x03(\x0e2>.google.cloud.aiplatform.v1beta1.Model.DeploymentResourcesTypeB\x03\xe0A\x03\x12,\n\x1fsupported_input_storage_formats\x18\x0b \x03(\tB\x03\xe0A\x03\x12-\n supported_output_storage_formats\x18\x0c \x03(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x0e \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12O\n\x0fdeployed_models\x18\x0f \x03(\x0b21.google.cloud.aiplatform.v1beta1.DeployedModelRefB\x03\xe0A\x03\x12J\n\x10explanation_spec\x18\x17 \x01(\x0b20.google.cloud.aiplatform.v1beta1.ExplanationSpec\x12\x0c\n\x04etag\x18\x10 \x01(\t\x12B\n\x06labels\x18\x11 \x03(\x0b22.google.cloud.aiplatform.v1beta1.Model.LabelsEntry\x12H\n\x0fencryption_spec\x18\x18 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.EncryptionSpec\x12P\n\x11model_source_info\x18& \x01(\x0b20.google.cloud.aiplatform.v1beta1.ModelSourceInfoB\x03\xe0A\x03\x12Z\n\x13original_model_info\x18" \x01(\x0b28.google.cloud.aiplatform.v1beta1.Model.OriginalModelInfoB\x03\xe0A\x03\x12\x1e\n\x11metadata_artifact\x18, \x01(\tB\x03\xe0A\x03\x12V\n\x11base_model_source\x182 \x01(\x0b26.google.cloud.aiplatform.v1beta1.Model.BaseModelSourceB\x03\xe0A\x01\x12\x1a\n\rsatisfies_pzs\x183 \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x184 \x01(\x08B\x03\xe0A\x03\x12H\n\x0bcheckpoints\x189 \x03(\x0b2+.google.cloud.aiplatform.v1beta1.CheckpointB\x06\xe0A\x03\xe0A\x01\x1a\xda\x01\n\x0cExportFormat\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x03\x12g\n\x13exportable_contents\x18\x02 \x03(\x0e2E.google.cloud.aiplatform.v1beta1.Model.ExportFormat.ExportableContentB\x03\xe0A\x03"P\n\x11ExportableContent\x12"\n\x1eEXPORTABLE_CONTENT_UNSPECIFIED\x10\x00\x12\x0c\n\x08ARTIFACT\x10\x01\x12\t\n\x05IMAGE\x10\x02\x1aK\n\x11OriginalModelInfo\x126\n\x05model\x18\x01 \x01(\tB\'\xe0A\x03\xfaA!\n\x1faiplatform.googleapis.com/Model\x1a\xb4\x01\n\x0fBaseModelSource\x12Q\n\x13model_garden_source\x18\x01 \x01(\x0b22.google.cloud.aiplatform.v1beta1.ModelGardenSourceH\x00\x12D\n\x0cgenie_source\x18\x02 \x01(\x0b2,.google.cloud.aiplatform.v1beta1.GenieSourceH\x00B\x08\n\x06source\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x8c\x01\n\x17DeploymentResourcesType\x12)\n%DEPLOYMENT_RESOURCES_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13DEDICATED_RESOURCES\x10\x01\x12\x17\n\x13AUTOMATIC_RESOURCES\x10\x02\x12\x14\n\x10SHARED_RESOURCES\x10\x03:\\\xeaAY\n\x1faiplatform.googleapis.com/Model\x126projects/{project}/locations/{location}/models/{model}"(\n\x13LargeModelReference\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"n\n\x11ModelGardenSource\x12\x1e\n\x11public_model_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\nversion_id\x18\x03 \x01(\tB\x03\xe0A\x01\x12 \n\x13skip_hf_model_cache\x18\x04 \x01(\x08B\x03\xe0A\x01"*\n\x0bGenieSource\x12\x1b\n\x0ebase_model_uri\x18\x01 \x01(\tB\x03\xe0A\x02"{\n\x0fPredictSchemata\x12 \n\x13instance_schema_uri\x18\x01 \x01(\tB\x03\xe0A\x05\x12"\n\x15parameters_schema_uri\x18\x02 \x01(\tB\x03\xe0A\x05\x12"\n\x15prediction_schema_uri\x18\x03 \x01(\tB\x03\xe0A\x05"\x93\x05\n\x12ModelContainerSpec\x12\x19\n\timage_uri\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12\x14\n\x07command\x18\x02 \x03(\tB\x03\xe0A\x05\x12\x11\n\x04args\x18\x03 \x03(\tB\x03\xe0A\x05\x129\n\x03env\x18\x04 \x03(\x0b2\'.google.cloud.aiplatform.v1beta1.EnvVarB\x03\xe0A\x05\x129\n\x05ports\x18\x05 \x03(\x0b2%.google.cloud.aiplatform.v1beta1.PortB\x03\xe0A\x05\x12\x1a\n\rpredict_route\x18\x06 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0chealth_route\x18\x07 \x01(\tB\x03\xe0A\x05\x12 \n\x13invoke_route_prefix\x18\x0f \x01(\tB\x03\xe0A\x05\x12>\n\ngrpc_ports\x18\t \x03(\x0b2%.google.cloud.aiplatform.v1beta1.PortB\x03\xe0A\x05\x12:\n\x12deployment_timeout\x18\n \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x05\x12"\n\x15shared_memory_size_mb\x18\x0b \x01(\x03B\x03\xe0A\x05\x12B\n\rstartup_probe\x18\x0c \x01(\x0b2&.google.cloud.aiplatform.v1beta1.ProbeB\x03\xe0A\x05\x12A\n\x0chealth_probe\x18\r \x01(\x0b2&.google.cloud.aiplatform.v1beta1.ProbeB\x03\xe0A\x05\x12C\n\x0eliveness_probe\x18\x0e \x01(\x0b2&.google.cloud.aiplatform.v1beta1.ProbeB\x03\xe0A\x05"\x1e\n\x04Port\x12\x16\n\x0econtainer_port\x18\x03 \x01(\x05"\x98\x02\n\x0fModelSourceInfo\x12U\n\x0bsource_type\x18\x01 \x01(\x0e2@.google.cloud.aiplatform.v1beta1.ModelSourceInfo.ModelSourceType\x12\x0c\n\x04copy\x18\x02 \x01(\x08"\x9f\x01\n\x0fModelSourceType\x12!\n\x1dMODEL_SOURCE_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06AUTOML\x10\x01\x12\n\n\x06CUSTOM\x10\x02\x12\x08\n\x04BQML\x10\x03\x12\x10\n\x0cMODEL_GARDEN\x10\x04\x12\t\n\x05GENIE\x10\x05\x12\x19\n\x15CUSTOM_TEXT_EMBEDDING\x10\x06\x12\x0f\n\x0bMARKETPLACE\x10\x07"\xf4\x05\n\x05Probe\x12A\n\x04exec\x18\x01 \x01(\x0b21.google.cloud.aiplatform.v1beta1.Probe.ExecActionH\x00\x12H\n\x08http_get\x18\x04 \x01(\x0b24.google.cloud.aiplatform.v1beta1.Probe.HttpGetActionH\x00\x12A\n\x04grpc\x18\x05 \x01(\x0b21.google.cloud.aiplatform.v1beta1.Probe.GrpcActionH\x00\x12L\n\ntcp_socket\x18\x06 \x01(\x0b26.google.cloud.aiplatform.v1beta1.Probe.TcpSocketActionH\x00\x12\x16\n\x0eperiod_seconds\x18\x02 \x01(\x05\x12\x17\n\x0ftimeout_seconds\x18\x03 \x01(\x05\x12\x19\n\x11failure_threshold\x18\x07 \x01(\x05\x12\x19\n\x11success_threshold\x18\x08 \x01(\x05\x12\x1d\n\x15initial_delay_seconds\x18\t \x01(\x05\x1a\x1d\n\nExecAction\x12\x0f\n\x07command\x18\x01 \x03(\t\x1a\x92\x01\n\rHttpGetAction\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x0c\n\x04host\x18\x03 \x01(\t\x12\x0e\n\x06scheme\x18\x04 \x01(\t\x12G\n\x0chttp_headers\x18\x05 \x03(\x0b21.google.cloud.aiplatform.v1beta1.Probe.HttpHeader\x1a+\n\nGrpcAction\x12\x0c\n\x04port\x18\x01 \x01(\x05\x12\x0f\n\x07service\x18\x02 \x01(\t\x1a-\n\x0fTcpSocketAction\x12\x0c\n\x04port\x18\x01 \x01(\x05\x12\x0c\n\x04host\x18\x02 \x01(\t\x1a)\n\nHttpHeader\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\tB\x0c\n\nprobe_type"@\n\nCheckpoint\x12\x15\n\rcheckpoint_id\x18\x01 \x01(\t\x12\r\n\x05epoch\x18\x02 \x01(\x03\x12\x0c\n\x04step\x18\x03 \x01(\x03B\xe1\x01\n#com.google.cloud.aiplatform.v1beta1B\nModelProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\nModelProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_MODEL_EXPORTFORMAT'].fields_by_name['id']._loaded_options = None
    _globals['_MODEL_EXPORTFORMAT'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL_EXPORTFORMAT'].fields_by_name['exportable_contents']._loaded_options = None
    _globals['_MODEL_EXPORTFORMAT'].fields_by_name['exportable_contents']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL_ORIGINALMODELINFO'].fields_by_name['model']._loaded_options = None
    _globals['_MODEL_ORIGINALMODELINFO'].fields_by_name['model']._serialized_options = b'\xe0A\x03\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_MODEL_LABELSENTRY']._loaded_options = None
    _globals['_MODEL_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_MODEL'].fields_by_name['version_id']._loaded_options = None
    _globals['_MODEL'].fields_by_name['version_id']._serialized_options = b'\xe0A\x05\xe0A\x03'
    _globals['_MODEL'].fields_by_name['version_create_time']._loaded_options = None
    _globals['_MODEL'].fields_by_name['version_create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['version_update_time']._loaded_options = None
    _globals['_MODEL'].fields_by_name['version_update_time']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['display_name']._loaded_options = None
    _globals['_MODEL'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_MODEL'].fields_by_name['metadata_schema_uri']._loaded_options = None
    _globals['_MODEL'].fields_by_name['metadata_schema_uri']._serialized_options = b'\xe0A\x05'
    _globals['_MODEL'].fields_by_name['metadata']._loaded_options = None
    _globals['_MODEL'].fields_by_name['metadata']._serialized_options = b'\xe0A\x05'
    _globals['_MODEL'].fields_by_name['supported_export_formats']._loaded_options = None
    _globals['_MODEL'].fields_by_name['supported_export_formats']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['training_pipeline']._loaded_options = None
    _globals['_MODEL'].fields_by_name['training_pipeline']._serialized_options = b'\xe0A\x03\xfaA,\n*aiplatform.googleapis.com/TrainingPipeline'
    _globals['_MODEL'].fields_by_name['container_spec']._loaded_options = None
    _globals['_MODEL'].fields_by_name['container_spec']._serialized_options = b'\xe0A\x04'
    _globals['_MODEL'].fields_by_name['artifact_uri']._loaded_options = None
    _globals['_MODEL'].fields_by_name['artifact_uri']._serialized_options = b'\xe0A\x05'
    _globals['_MODEL'].fields_by_name['supported_deployment_resources_types']._loaded_options = None
    _globals['_MODEL'].fields_by_name['supported_deployment_resources_types']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['supported_input_storage_formats']._loaded_options = None
    _globals['_MODEL'].fields_by_name['supported_input_storage_formats']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['supported_output_storage_formats']._loaded_options = None
    _globals['_MODEL'].fields_by_name['supported_output_storage_formats']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['create_time']._loaded_options = None
    _globals['_MODEL'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['update_time']._loaded_options = None
    _globals['_MODEL'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['deployed_models']._loaded_options = None
    _globals['_MODEL'].fields_by_name['deployed_models']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['model_source_info']._loaded_options = None
    _globals['_MODEL'].fields_by_name['model_source_info']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['original_model_info']._loaded_options = None
    _globals['_MODEL'].fields_by_name['original_model_info']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['metadata_artifact']._loaded_options = None
    _globals['_MODEL'].fields_by_name['metadata_artifact']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['base_model_source']._loaded_options = None
    _globals['_MODEL'].fields_by_name['base_model_source']._serialized_options = b'\xe0A\x01'
    _globals['_MODEL'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_MODEL'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_MODEL'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['checkpoints']._loaded_options = None
    _globals['_MODEL'].fields_by_name['checkpoints']._serialized_options = b'\xe0A\x03\xe0A\x01'
    _globals['_MODEL']._loaded_options = None
    _globals['_MODEL']._serialized_options = b'\xeaAY\n\x1faiplatform.googleapis.com/Model\x126projects/{project}/locations/{location}/models/{model}'
    _globals['_LARGEMODELREFERENCE'].fields_by_name['name']._loaded_options = None
    _globals['_LARGEMODELREFERENCE'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_MODELGARDENSOURCE'].fields_by_name['public_model_name']._loaded_options = None
    _globals['_MODELGARDENSOURCE'].fields_by_name['public_model_name']._serialized_options = b'\xe0A\x02'
    _globals['_MODELGARDENSOURCE'].fields_by_name['version_id']._loaded_options = None
    _globals['_MODELGARDENSOURCE'].fields_by_name['version_id']._serialized_options = b'\xe0A\x01'
    _globals['_MODELGARDENSOURCE'].fields_by_name['skip_hf_model_cache']._loaded_options = None
    _globals['_MODELGARDENSOURCE'].fields_by_name['skip_hf_model_cache']._serialized_options = b'\xe0A\x01'
    _globals['_GENIESOURCE'].fields_by_name['base_model_uri']._loaded_options = None
    _globals['_GENIESOURCE'].fields_by_name['base_model_uri']._serialized_options = b'\xe0A\x02'
    _globals['_PREDICTSCHEMATA'].fields_by_name['instance_schema_uri']._loaded_options = None
    _globals['_PREDICTSCHEMATA'].fields_by_name['instance_schema_uri']._serialized_options = b'\xe0A\x05'
    _globals['_PREDICTSCHEMATA'].fields_by_name['parameters_schema_uri']._loaded_options = None
    _globals['_PREDICTSCHEMATA'].fields_by_name['parameters_schema_uri']._serialized_options = b'\xe0A\x05'
    _globals['_PREDICTSCHEMATA'].fields_by_name['prediction_schema_uri']._loaded_options = None
    _globals['_PREDICTSCHEMATA'].fields_by_name['prediction_schema_uri']._serialized_options = b'\xe0A\x05'
    _globals['_MODELCONTAINERSPEC'].fields_by_name['image_uri']._loaded_options = None
    _globals['_MODELCONTAINERSPEC'].fields_by_name['image_uri']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_MODELCONTAINERSPEC'].fields_by_name['command']._loaded_options = None
    _globals['_MODELCONTAINERSPEC'].fields_by_name['command']._serialized_options = b'\xe0A\x05'
    _globals['_MODELCONTAINERSPEC'].fields_by_name['args']._loaded_options = None
    _globals['_MODELCONTAINERSPEC'].fields_by_name['args']._serialized_options = b'\xe0A\x05'
    _globals['_MODELCONTAINERSPEC'].fields_by_name['env']._loaded_options = None
    _globals['_MODELCONTAINERSPEC'].fields_by_name['env']._serialized_options = b'\xe0A\x05'
    _globals['_MODELCONTAINERSPEC'].fields_by_name['ports']._loaded_options = None
    _globals['_MODELCONTAINERSPEC'].fields_by_name['ports']._serialized_options = b'\xe0A\x05'
    _globals['_MODELCONTAINERSPEC'].fields_by_name['predict_route']._loaded_options = None
    _globals['_MODELCONTAINERSPEC'].fields_by_name['predict_route']._serialized_options = b'\xe0A\x05'
    _globals['_MODELCONTAINERSPEC'].fields_by_name['health_route']._loaded_options = None
    _globals['_MODELCONTAINERSPEC'].fields_by_name['health_route']._serialized_options = b'\xe0A\x05'
    _globals['_MODELCONTAINERSPEC'].fields_by_name['invoke_route_prefix']._loaded_options = None
    _globals['_MODELCONTAINERSPEC'].fields_by_name['invoke_route_prefix']._serialized_options = b'\xe0A\x05'
    _globals['_MODELCONTAINERSPEC'].fields_by_name['grpc_ports']._loaded_options = None
    _globals['_MODELCONTAINERSPEC'].fields_by_name['grpc_ports']._serialized_options = b'\xe0A\x05'
    _globals['_MODELCONTAINERSPEC'].fields_by_name['deployment_timeout']._loaded_options = None
    _globals['_MODELCONTAINERSPEC'].fields_by_name['deployment_timeout']._serialized_options = b'\xe0A\x05'
    _globals['_MODELCONTAINERSPEC'].fields_by_name['shared_memory_size_mb']._loaded_options = None
    _globals['_MODELCONTAINERSPEC'].fields_by_name['shared_memory_size_mb']._serialized_options = b'\xe0A\x05'
    _globals['_MODELCONTAINERSPEC'].fields_by_name['startup_probe']._loaded_options = None
    _globals['_MODELCONTAINERSPEC'].fields_by_name['startup_probe']._serialized_options = b'\xe0A\x05'
    _globals['_MODELCONTAINERSPEC'].fields_by_name['health_probe']._loaded_options = None
    _globals['_MODELCONTAINERSPEC'].fields_by_name['health_probe']._serialized_options = b'\xe0A\x05'
    _globals['_MODELCONTAINERSPEC'].fields_by_name['liveness_probe']._loaded_options = None
    _globals['_MODELCONTAINERSPEC'].fields_by_name['liveness_probe']._serialized_options = b'\xe0A\x05'
    _globals['_MODEL']._serialized_start = 447
    _globals['_MODEL']._serialized_end = 3008
    _globals['_MODEL_EXPORTFORMAT']._serialized_start = 2246
    _globals['_MODEL_EXPORTFORMAT']._serialized_end = 2464
    _globals['_MODEL_EXPORTFORMAT_EXPORTABLECONTENT']._serialized_start = 2384
    _globals['_MODEL_EXPORTFORMAT_EXPORTABLECONTENT']._serialized_end = 2464
    _globals['_MODEL_ORIGINALMODELINFO']._serialized_start = 2466
    _globals['_MODEL_ORIGINALMODELINFO']._serialized_end = 2541
    _globals['_MODEL_BASEMODELSOURCE']._serialized_start = 2544
    _globals['_MODEL_BASEMODELSOURCE']._serialized_end = 2724
    _globals['_MODEL_LABELSENTRY']._serialized_start = 2726
    _globals['_MODEL_LABELSENTRY']._serialized_end = 2771
    _globals['_MODEL_DEPLOYMENTRESOURCESTYPE']._serialized_start = 2774
    _globals['_MODEL_DEPLOYMENTRESOURCESTYPE']._serialized_end = 2914
    _globals['_LARGEMODELREFERENCE']._serialized_start = 3010
    _globals['_LARGEMODELREFERENCE']._serialized_end = 3050
    _globals['_MODELGARDENSOURCE']._serialized_start = 3052
    _globals['_MODELGARDENSOURCE']._serialized_end = 3162
    _globals['_GENIESOURCE']._serialized_start = 3164
    _globals['_GENIESOURCE']._serialized_end = 3206
    _globals['_PREDICTSCHEMATA']._serialized_start = 3208
    _globals['_PREDICTSCHEMATA']._serialized_end = 3331
    _globals['_MODELCONTAINERSPEC']._serialized_start = 3334
    _globals['_MODELCONTAINERSPEC']._serialized_end = 3993
    _globals['_PORT']._serialized_start = 3995
    _globals['_PORT']._serialized_end = 4025
    _globals['_MODELSOURCEINFO']._serialized_start = 4028
    _globals['_MODELSOURCEINFO']._serialized_end = 4308
    _globals['_MODELSOURCEINFO_MODELSOURCETYPE']._serialized_start = 4149
    _globals['_MODELSOURCEINFO_MODELSOURCETYPE']._serialized_end = 4308
    _globals['_PROBE']._serialized_start = 4311
    _globals['_PROBE']._serialized_end = 5067
    _globals['_PROBE_EXECACTION']._serialized_start = 4740
    _globals['_PROBE_EXECACTION']._serialized_end = 4769
    _globals['_PROBE_HTTPGETACTION']._serialized_start = 4772
    _globals['_PROBE_HTTPGETACTION']._serialized_end = 4918
    _globals['_PROBE_GRPCACTION']._serialized_start = 4920
    _globals['_PROBE_GRPCACTION']._serialized_end = 4963
    _globals['_PROBE_TCPSOCKETACTION']._serialized_start = 4965
    _globals['_PROBE_TCPSOCKETACTION']._serialized_end = 5010
    _globals['_PROBE_HTTPHEADER']._serialized_start = 5012
    _globals['_PROBE_HTTPHEADER']._serialized_end = 5053
    _globals['_CHECKPOINT']._serialized_start = 5069
    _globals['_CHECKPOINT']._serialized_end = 5133