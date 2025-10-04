"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/dataflow/v1beta3/templates.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.dataflow.v1beta3 import environment_pb2 as google_dot_dataflow_dot_v1beta3_dot_environment__pb2
from ....google.dataflow.v1beta3 import jobs_pb2 as google_dot_dataflow_dot_v1beta3_dot_jobs__pb2
from ....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/dataflow/v1beta3/templates.proto\x12\x17google.dataflow.v1beta3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a)google/dataflow/v1beta3/environment.proto\x1a"google/dataflow/v1beta3/jobs.proto\x1a\x17google/rpc/status.proto"G\n\x1aLaunchFlexTemplateResponse\x12)\n\x03job\x18\x01 \x01(\x0b2\x1c.google.dataflow.v1beta3.Job"\xe3\x02\n\rContainerSpec\x12\r\n\x05image\x18\x01 \x01(\t\x12;\n\x08metadata\x18\x02 \x01(\x0b2).google.dataflow.v1beta3.TemplateMetadata\x122\n\x08sdk_info\x18\x03 \x01(\x0b2 .google.dataflow.v1beta3.SDKInfo\x12T\n\x13default_environment\x18\x04 \x01(\x0b27.google.dataflow.v1beta3.FlexTemplateRuntimeEnvironment\x12+\n#image_repository_username_secret_id\x18\x05 \x01(\t\x12+\n#image_repository_password_secret_id\x18\x06 \x01(\t\x12"\n\x1aimage_repository_cert_path\x18\x07 \x01(\t"\xd2\x05\n\x1bLaunchFlexTemplateParameter\x12\x10\n\x08job_name\x18\x01 \x01(\t\x12@\n\x0econtainer_spec\x18\x04 \x01(\x0b2&.google.dataflow.v1beta3.ContainerSpecH\x00\x12!\n\x17container_spec_gcs_path\x18\x05 \x01(\tH\x00\x12X\n\nparameters\x18\x02 \x03(\x0b2D.google.dataflow.v1beta3.LaunchFlexTemplateParameter.ParametersEntry\x12_\n\x0elaunch_options\x18\x06 \x03(\x0b2G.google.dataflow.v1beta3.LaunchFlexTemplateParameter.LaunchOptionsEntry\x12L\n\x0benvironment\x18\x07 \x01(\x0b27.google.dataflow.v1beta3.FlexTemplateRuntimeEnvironment\x12\x0e\n\x06update\x18\x08 \x01(\x08\x12p\n\x17transform_name_mappings\x18\t \x03(\x0b2O.google.dataflow.v1beta3.LaunchFlexTemplateParameter.TransformNameMappingsEntry\x1a1\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a4\n\x12LaunchOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a<\n\x1aTransformNameMappingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\n\n\x08template"\x9d\x08\n\x1eFlexTemplateRuntimeEnvironment\x12\x13\n\x0bnum_workers\x18\x01 \x01(\x05\x12\x13\n\x0bmax_workers\x18\x02 \x01(\x05\x12\x0c\n\x04zone\x18\x03 \x01(\t\x12\x1d\n\x15service_account_email\x18\x04 \x01(\t\x12\x15\n\rtemp_location\x18\x05 \x01(\t\x12\x14\n\x0cmachine_type\x18\x06 \x01(\t\x12\x1e\n\x16additional_experiments\x18\x07 \x03(\t\x12\x0f\n\x07network\x18\x08 \x01(\t\x12\x12\n\nsubnetwork\x18\t \x01(\t\x12q\n\x16additional_user_labels\x18\n \x03(\x0b2Q.google.dataflow.v1beta3.FlexTemplateRuntimeEnvironment.AdditionalUserLabelsEntry\x12\x14\n\x0ckms_key_name\x18\x0b \x01(\t\x12O\n\x10ip_configuration\x18\x0c \x01(\x0e25.google.dataflow.v1beta3.WorkerIPAddressConfiguration\x12\x15\n\rworker_region\x18\r \x01(\t\x12\x13\n\x0bworker_zone\x18\x0e \x01(\t\x12\x1f\n\x17enable_streaming_engine\x18\x0f \x01(\x08\x12H\n\x0bflexrs_goal\x18\x10 \x01(\x0e23.google.dataflow.v1beta3.FlexResourceSchedulingGoal\x12\x18\n\x10staging_location\x18\x11 \x01(\t\x12\x1b\n\x13sdk_container_image\x18\x12 \x01(\t\x12\x14\n\x0cdisk_size_gb\x18\x14 \x01(\x05\x12L\n\x15autoscaling_algorithm\x18\x15 \x01(\x0e2-.google.dataflow.v1beta3.AutoscalingAlgorithm\x12\x18\n\x10dump_heap_on_oom\x18\x16 \x01(\x08\x12#\n\x1bsave_heap_dumps_to_gcs_path\x18\x17 \x01(\t\x12\x1d\n\x15launcher_machine_type\x18\x18 \x01(\t\x12.\n&enable_launcher_vm_serial_port_logging\x18\x19 \x01(\x08\x12H\n\x0estreaming_mode\x18\x1a \x01(\x0e2&.google.dataflow.v1beta3.StreamingModeB\x03\xe0A\x01H\x00\x88\x01\x01\x1a;\n\x19AdditionalUserLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x11\n\x0f_streaming_mode"\xa8\x01\n\x19LaunchFlexTemplateRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12N\n\x10launch_parameter\x18\x02 \x01(\x0b24.google.dataflow.v1beta3.LaunchFlexTemplateParameter\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08"\xcc\x05\n\x12RuntimeEnvironment\x12\x13\n\x0bnum_workers\x18\x0b \x01(\x05\x12\x13\n\x0bmax_workers\x18\x01 \x01(\x05\x12\x0c\n\x04zone\x18\x02 \x01(\t\x12\x1d\n\x15service_account_email\x18\x03 \x01(\t\x12\x15\n\rtemp_location\x18\x04 \x01(\t\x12"\n\x1abypass_temp_dir_validation\x18\x05 \x01(\x08\x12\x14\n\x0cmachine_type\x18\x06 \x01(\t\x12\x1e\n\x16additional_experiments\x18\x07 \x03(\t\x12\x0f\n\x07network\x18\x08 \x01(\t\x12\x12\n\nsubnetwork\x18\t \x01(\t\x12e\n\x16additional_user_labels\x18\n \x03(\x0b2E.google.dataflow.v1beta3.RuntimeEnvironment.AdditionalUserLabelsEntry\x12\x14\n\x0ckms_key_name\x18\x0c \x01(\t\x12O\n\x10ip_configuration\x18\x0e \x01(\x0e25.google.dataflow.v1beta3.WorkerIPAddressConfiguration\x12\x15\n\rworker_region\x18\x0f \x01(\t\x12\x13\n\x0bworker_zone\x18\x10 \x01(\t\x12\x1f\n\x17enable_streaming_engine\x18\x11 \x01(\x08\x12\x14\n\x0cdisk_size_gb\x18\x12 \x01(\x05\x12H\n\x0estreaming_mode\x18\x13 \x01(\x0e2&.google.dataflow.v1beta3.StreamingModeB\x03\xe0A\x01H\x00\x88\x01\x01\x1a;\n\x19AdditionalUserLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x11\n\x0f_streaming_mode"_\n\x1bParameterMetadataEnumOption\x12\x12\n\x05value\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05label\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x01"\xf3\x03\n\x11ParameterMetadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x11\n\thelp_text\x18\x03 \x01(\t\x12\x13\n\x0bis_optional\x18\x04 \x01(\x08\x12\x0f\n\x07regexes\x18\x05 \x03(\t\x12:\n\nparam_type\x18\x06 \x01(\x0e2&.google.dataflow.v1beta3.ParameterType\x12W\n\x0fcustom_metadata\x18\x07 \x03(\x0b2>.google.dataflow.v1beta3.ParameterMetadata.CustomMetadataEntry\x12\x12\n\ngroup_name\x18\x08 \x01(\t\x12\x13\n\x0bparent_name\x18\t \x01(\t\x12\x1d\n\x15parent_trigger_values\x18\n \x03(\t\x12J\n\x0cenum_options\x18\x0b \x03(\x0b24.google.dataflow.v1beta3.ParameterMetadataEnumOption\x12\x15\n\rdefault_value\x18\x0c \x01(\t\x12\x11\n\thidden_ui\x18\r \x01(\x08\x1a5\n\x13CustomMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xe7\x01\n\x10TemplateMetadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12>\n\nparameters\x18\x03 \x03(\x0b2*.google.dataflow.v1beta3.ParameterMetadata\x12\x11\n\tstreaming\x18\x05 \x01(\x08\x12\x1e\n\x16supports_at_least_once\x18\x06 \x01(\x08\x12\x1d\n\x15supports_exactly_once\x18\x07 \x01(\x08\x12\x1e\n\x16default_streaming_mode\x18\x08 \x01(\t"\x8e\x01\n\x07SDKInfo\x12;\n\x08language\x18\x01 \x01(\x0e2).google.dataflow.v1beta3.SDKInfo.Language\x12\x0f\n\x07version\x18\x02 \x01(\t"5\n\x08Language\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04JAVA\x10\x01\x12\n\n\x06PYTHON\x10\x02\x12\x06\n\x02GO\x10\x03"\x85\x01\n\x0fRuntimeMetadata\x122\n\x08sdk_info\x18\x01 \x01(\x0b2 .google.dataflow.v1beta3.SDKInfo\x12>\n\nparameters\x18\x02 \x03(\x0b2*.google.dataflow.v1beta3.ParameterMetadata"\xc6\x02\n\x1cCreateJobFromTemplateRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x10\n\x08job_name\x18\x04 \x01(\t\x12\x12\n\x08gcs_path\x18\x02 \x01(\tH\x00\x12Y\n\nparameters\x18\x03 \x03(\x0b2E.google.dataflow.v1beta3.CreateJobFromTemplateRequest.ParametersEntry\x12@\n\x0benvironment\x18\x05 \x01(\x0b2+.google.dataflow.v1beta3.RuntimeEnvironment\x12\x10\n\x08location\x18\x06 \x01(\t\x1a1\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\n\n\x08template"\xc5\x01\n\x12GetTemplateRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x12\n\x08gcs_path\x18\x02 \x01(\tH\x00\x12F\n\x04view\x18\x03 \x01(\x0e28.google.dataflow.v1beta3.GetTemplateRequest.TemplateView\x12\x10\n\x08location\x18\x04 \x01(\t"!\n\x0cTemplateView\x12\x11\n\rMETADATA_ONLY\x10\x00B\n\n\x08template"\xbf\x02\n\x13GetTemplateResponse\x12"\n\x06status\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x12;\n\x08metadata\x18\x02 \x01(\x0b2).google.dataflow.v1beta3.TemplateMetadata\x12P\n\rtemplate_type\x18\x03 \x01(\x0e29.google.dataflow.v1beta3.GetTemplateResponse.TemplateType\x12B\n\x10runtime_metadata\x18\x04 \x01(\x0b2(.google.dataflow.v1beta3.RuntimeMetadata"1\n\x0cTemplateType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06LEGACY\x10\x01\x12\x08\n\x04FLEX\x10\x02"\xb2\x03\n\x18LaunchTemplateParameters\x12\x10\n\x08job_name\x18\x01 \x01(\t\x12U\n\nparameters\x18\x02 \x03(\x0b2A.google.dataflow.v1beta3.LaunchTemplateParameters.ParametersEntry\x12@\n\x0benvironment\x18\x03 \x01(\x0b2+.google.dataflow.v1beta3.RuntimeEnvironment\x12\x0e\n\x06update\x18\x04 \x01(\x08\x12k\n\x16transform_name_mapping\x18\x05 \x03(\x0b2K.google.dataflow.v1beta3.LaunchTemplateParameters.TransformNameMappingEntry\x1a1\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a;\n\x19TransformNameMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x94\x02\n\x15LaunchTemplateRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x15\n\rvalidate_only\x18\x02 \x01(\x08\x12\x12\n\x08gcs_path\x18\x03 \x01(\tH\x00\x12P\n\x10dynamic_template\x18\x06 \x01(\x0b24.google.dataflow.v1beta3.DynamicTemplateLaunchParamsH\x00\x12L\n\x11launch_parameters\x18\x04 \x01(\x0b21.google.dataflow.v1beta3.LaunchTemplateParameters\x12\x10\n\x08location\x18\x05 \x01(\tB\n\n\x08template"C\n\x16LaunchTemplateResponse\x12)\n\x03job\x18\x01 \x01(\x0b2\x1c.google.dataflow.v1beta3.Job"\xbe\x01\n\x19InvalidTemplateParameters\x12c\n\x14parameter_violations\x18\x01 \x03(\x0b2E.google.dataflow.v1beta3.InvalidTemplateParameters.ParameterViolation\x1a<\n\x12ParameterViolation\x12\x11\n\tparameter\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t"I\n\x1bDynamicTemplateLaunchParams\x12\x10\n\x08gcs_path\x18\x01 \x01(\t\x12\x18\n\x10staging_location\x18\x02 \x01(\t*\xbd\x03\n\rParameterType\x12\x0b\n\x07DEFAULT\x10\x00\x12\x08\n\x04TEXT\x10\x01\x12\x13\n\x0fGCS_READ_BUCKET\x10\x02\x12\x14\n\x10GCS_WRITE_BUCKET\x10\x03\x12\x11\n\rGCS_READ_FILE\x10\x04\x12\x12\n\x0eGCS_WRITE_FILE\x10\x05\x12\x13\n\x0fGCS_READ_FOLDER\x10\x06\x12\x14\n\x10GCS_WRITE_FOLDER\x10\x07\x12\x10\n\x0cPUBSUB_TOPIC\x10\x08\x12\x17\n\x13PUBSUB_SUBSCRIPTION\x10\t\x12\x12\n\x0eBIGQUERY_TABLE\x10\n\x12\x17\n\x13JAVASCRIPT_UDF_FILE\x10\x0b\x12\x13\n\x0fSERVICE_ACCOUNT\x10\x0c\x12\x10\n\x0cMACHINE_TYPE\x10\r\x12\x10\n\x0cKMS_KEY_NAME\x10\x0e\x12\x11\n\rWORKER_REGION\x10\x0f\x12\x0f\n\x0bWORKER_ZONE\x10\x10\x12\x0b\n\x07BOOLEAN\x10\x11\x12\x08\n\x04ENUM\x10\x12\x12\n\n\x06NUMBER\x10\x13\x12\x13\n\x0bKAFKA_TOPIC\x10\x14\x1a\x02\x08\x01\x12\x14\n\x10KAFKA_READ_TOPIC\x10\x15\x12\x15\n\x11KAFKA_WRITE_TOPIC\x10\x162\xe0\x06\n\x10TemplatesService\x12\xdf\x01\n\x15CreateJobFromTemplate\x125.google.dataflow.v1beta3.CreateJobFromTemplateRequest\x1a\x1c.google.dataflow.v1beta3.Job"q\x82\xd3\xe4\x93\x02k":/v1b3/projects/{project_id}/locations/{location}/templates:\x01*Z*"%/v1b3/projects/{project_id}/templates:\x01*\x12\x94\x02\n\x0eLaunchTemplate\x12..google.dataflow.v1beta3.LaunchTemplateRequest\x1a/.google.dataflow.v1beta3.LaunchTemplateResponse"\xa0\x01\x82\xd3\xe4\x93\x02\x99\x01"A/v1b3/projects/{project_id}/locations/{location}/templates:launch:\x11launch_parametersZA",/v1b3/projects/{project_id}/templates:launch:\x11launch_parameters\x12\xdd\x01\n\x0bGetTemplate\x12+.google.dataflow.v1beta3.GetTemplateRequest\x1a,.google.dataflow.v1beta3.GetTemplateResponse"s\x82\xd3\xe4\x93\x02m\x12>/v1b3/projects/{project_id}/locations/{location}/templates:getZ+\x12)/v1b3/projects/{project_id}/templates:get\x1as\xcaA\x17dataflow.googleapis.com\xd2AVhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/compute2\xdd\x02\n\x14FlexTemplatesService\x12\xcf\x01\n\x12LaunchFlexTemplate\x122.google.dataflow.v1beta3.LaunchFlexTemplateRequest\x1a3.google.dataflow.v1beta3.LaunchFlexTemplateResponse"P\x82\xd3\xe4\x93\x02J"E/v1b3/projects/{project_id}/locations/{location}/flexTemplates:launch:\x01*\x1as\xcaA\x17dataflow.googleapis.com\xd2AVhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/computeB\xd1\x01\n\x1bcom.google.dataflow.v1beta3B\x0eTemplatesProtoP\x01Z=cloud.google.com/go/dataflow/apiv1beta3/dataflowpb;dataflowpb\xaa\x02\x1dGoogle.Cloud.Dataflow.V1Beta3\xca\x02\x1dGoogle\\Cloud\\Dataflow\\V1beta3\xea\x02 Google::Cloud::Dataflow::V1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.dataflow.v1beta3.templates_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.dataflow.v1beta3B\x0eTemplatesProtoP\x01Z=cloud.google.com/go/dataflow/apiv1beta3/dataflowpb;dataflowpb\xaa\x02\x1dGoogle.Cloud.Dataflow.V1Beta3\xca\x02\x1dGoogle\\Cloud\\Dataflow\\V1beta3\xea\x02 Google::Cloud::Dataflow::V1beta3'
    _globals['_PARAMETERTYPE'].values_by_name['KAFKA_TOPIC']._loaded_options = None
    _globals['_PARAMETERTYPE'].values_by_name['KAFKA_TOPIC']._serialized_options = b'\x08\x01'
    _globals['_LAUNCHFLEXTEMPLATEPARAMETER_PARAMETERSENTRY']._loaded_options = None
    _globals['_LAUNCHFLEXTEMPLATEPARAMETER_PARAMETERSENTRY']._serialized_options = b'8\x01'
    _globals['_LAUNCHFLEXTEMPLATEPARAMETER_LAUNCHOPTIONSENTRY']._loaded_options = None
    _globals['_LAUNCHFLEXTEMPLATEPARAMETER_LAUNCHOPTIONSENTRY']._serialized_options = b'8\x01'
    _globals['_LAUNCHFLEXTEMPLATEPARAMETER_TRANSFORMNAMEMAPPINGSENTRY']._loaded_options = None
    _globals['_LAUNCHFLEXTEMPLATEPARAMETER_TRANSFORMNAMEMAPPINGSENTRY']._serialized_options = b'8\x01'
    _globals['_FLEXTEMPLATERUNTIMEENVIRONMENT_ADDITIONALUSERLABELSENTRY']._loaded_options = None
    _globals['_FLEXTEMPLATERUNTIMEENVIRONMENT_ADDITIONALUSERLABELSENTRY']._serialized_options = b'8\x01'
    _globals['_FLEXTEMPLATERUNTIMEENVIRONMENT'].fields_by_name['streaming_mode']._loaded_options = None
    _globals['_FLEXTEMPLATERUNTIMEENVIRONMENT'].fields_by_name['streaming_mode']._serialized_options = b'\xe0A\x01'
    _globals['_RUNTIMEENVIRONMENT_ADDITIONALUSERLABELSENTRY']._loaded_options = None
    _globals['_RUNTIMEENVIRONMENT_ADDITIONALUSERLABELSENTRY']._serialized_options = b'8\x01'
    _globals['_RUNTIMEENVIRONMENT'].fields_by_name['streaming_mode']._loaded_options = None
    _globals['_RUNTIMEENVIRONMENT'].fields_by_name['streaming_mode']._serialized_options = b'\xe0A\x01'
    _globals['_PARAMETERMETADATAENUMOPTION'].fields_by_name['value']._loaded_options = None
    _globals['_PARAMETERMETADATAENUMOPTION'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_PARAMETERMETADATAENUMOPTION'].fields_by_name['label']._loaded_options = None
    _globals['_PARAMETERMETADATAENUMOPTION'].fields_by_name['label']._serialized_options = b'\xe0A\x01'
    _globals['_PARAMETERMETADATAENUMOPTION'].fields_by_name['description']._loaded_options = None
    _globals['_PARAMETERMETADATAENUMOPTION'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_PARAMETERMETADATA_CUSTOMMETADATAENTRY']._loaded_options = None
    _globals['_PARAMETERMETADATA_CUSTOMMETADATAENTRY']._serialized_options = b'8\x01'
    _globals['_CREATEJOBFROMTEMPLATEREQUEST_PARAMETERSENTRY']._loaded_options = None
    _globals['_CREATEJOBFROMTEMPLATEREQUEST_PARAMETERSENTRY']._serialized_options = b'8\x01'
    _globals['_LAUNCHTEMPLATEPARAMETERS_PARAMETERSENTRY']._loaded_options = None
    _globals['_LAUNCHTEMPLATEPARAMETERS_PARAMETERSENTRY']._serialized_options = b'8\x01'
    _globals['_LAUNCHTEMPLATEPARAMETERS_TRANSFORMNAMEMAPPINGENTRY']._loaded_options = None
    _globals['_LAUNCHTEMPLATEPARAMETERS_TRANSFORMNAMEMAPPINGENTRY']._serialized_options = b'8\x01'
    _globals['_TEMPLATESSERVICE']._loaded_options = None
    _globals['_TEMPLATESSERVICE']._serialized_options = b'\xcaA\x17dataflow.googleapis.com\xd2AVhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/compute'
    _globals['_TEMPLATESSERVICE'].methods_by_name['CreateJobFromTemplate']._loaded_options = None
    _globals['_TEMPLATESSERVICE'].methods_by_name['CreateJobFromTemplate']._serialized_options = b'\x82\xd3\xe4\x93\x02k":/v1b3/projects/{project_id}/locations/{location}/templates:\x01*Z*"%/v1b3/projects/{project_id}/templates:\x01*'
    _globals['_TEMPLATESSERVICE'].methods_by_name['LaunchTemplate']._loaded_options = None
    _globals['_TEMPLATESSERVICE'].methods_by_name['LaunchTemplate']._serialized_options = b'\x82\xd3\xe4\x93\x02\x99\x01"A/v1b3/projects/{project_id}/locations/{location}/templates:launch:\x11launch_parametersZA",/v1b3/projects/{project_id}/templates:launch:\x11launch_parameters'
    _globals['_TEMPLATESSERVICE'].methods_by_name['GetTemplate']._loaded_options = None
    _globals['_TEMPLATESSERVICE'].methods_by_name['GetTemplate']._serialized_options = b'\x82\xd3\xe4\x93\x02m\x12>/v1b3/projects/{project_id}/locations/{location}/templates:getZ+\x12)/v1b3/projects/{project_id}/templates:get'
    _globals['_FLEXTEMPLATESSERVICE']._loaded_options = None
    _globals['_FLEXTEMPLATESSERVICE']._serialized_options = b'\xcaA\x17dataflow.googleapis.com\xd2AVhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/compute'
    _globals['_FLEXTEMPLATESSERVICE'].methods_by_name['LaunchFlexTemplate']._loaded_options = None
    _globals['_FLEXTEMPLATESSERVICE'].methods_by_name['LaunchFlexTemplate']._serialized_options = b'\x82\xd3\xe4\x93\x02J"E/v1b3/projects/{project_id}/locations/{location}/flexTemplates:launch:\x01*'
    _globals['_PARAMETERTYPE']._serialized_start = 6381
    _globals['_PARAMETERTYPE']._serialized_end = 6826
    _globals['_LAUNCHFLEXTEMPLATERESPONSE']._serialized_start = 260
    _globals['_LAUNCHFLEXTEMPLATERESPONSE']._serialized_end = 331
    _globals['_CONTAINERSPEC']._serialized_start = 334
    _globals['_CONTAINERSPEC']._serialized_end = 689
    _globals['_LAUNCHFLEXTEMPLATEPARAMETER']._serialized_start = 692
    _globals['_LAUNCHFLEXTEMPLATEPARAMETER']._serialized_end = 1414
    _globals['_LAUNCHFLEXTEMPLATEPARAMETER_PARAMETERSENTRY']._serialized_start = 1237
    _globals['_LAUNCHFLEXTEMPLATEPARAMETER_PARAMETERSENTRY']._serialized_end = 1286
    _globals['_LAUNCHFLEXTEMPLATEPARAMETER_LAUNCHOPTIONSENTRY']._serialized_start = 1288
    _globals['_LAUNCHFLEXTEMPLATEPARAMETER_LAUNCHOPTIONSENTRY']._serialized_end = 1340
    _globals['_LAUNCHFLEXTEMPLATEPARAMETER_TRANSFORMNAMEMAPPINGSENTRY']._serialized_start = 1342
    _globals['_LAUNCHFLEXTEMPLATEPARAMETER_TRANSFORMNAMEMAPPINGSENTRY']._serialized_end = 1402
    _globals['_FLEXTEMPLATERUNTIMEENVIRONMENT']._serialized_start = 1417
    _globals['_FLEXTEMPLATERUNTIMEENVIRONMENT']._serialized_end = 2470
    _globals['_FLEXTEMPLATERUNTIMEENVIRONMENT_ADDITIONALUSERLABELSENTRY']._serialized_start = 2392
    _globals['_FLEXTEMPLATERUNTIMEENVIRONMENT_ADDITIONALUSERLABELSENTRY']._serialized_end = 2451
    _globals['_LAUNCHFLEXTEMPLATEREQUEST']._serialized_start = 2473
    _globals['_LAUNCHFLEXTEMPLATEREQUEST']._serialized_end = 2641
    _globals['_RUNTIMEENVIRONMENT']._serialized_start = 2644
    _globals['_RUNTIMEENVIRONMENT']._serialized_end = 3360
    _globals['_RUNTIMEENVIRONMENT_ADDITIONALUSERLABELSENTRY']._serialized_start = 2392
    _globals['_RUNTIMEENVIRONMENT_ADDITIONALUSERLABELSENTRY']._serialized_end = 2451
    _globals['_PARAMETERMETADATAENUMOPTION']._serialized_start = 3362
    _globals['_PARAMETERMETADATAENUMOPTION']._serialized_end = 3457
    _globals['_PARAMETERMETADATA']._serialized_start = 3460
    _globals['_PARAMETERMETADATA']._serialized_end = 3959
    _globals['_PARAMETERMETADATA_CUSTOMMETADATAENTRY']._serialized_start = 3906
    _globals['_PARAMETERMETADATA_CUSTOMMETADATAENTRY']._serialized_end = 3959
    _globals['_TEMPLATEMETADATA']._serialized_start = 3962
    _globals['_TEMPLATEMETADATA']._serialized_end = 4193
    _globals['_SDKINFO']._serialized_start = 4196
    _globals['_SDKINFO']._serialized_end = 4338
    _globals['_SDKINFO_LANGUAGE']._serialized_start = 4285
    _globals['_SDKINFO_LANGUAGE']._serialized_end = 4338
    _globals['_RUNTIMEMETADATA']._serialized_start = 4341
    _globals['_RUNTIMEMETADATA']._serialized_end = 4474
    _globals['_CREATEJOBFROMTEMPLATEREQUEST']._serialized_start = 4477
    _globals['_CREATEJOBFROMTEMPLATEREQUEST']._serialized_end = 4803
    _globals['_CREATEJOBFROMTEMPLATEREQUEST_PARAMETERSENTRY']._serialized_start = 1237
    _globals['_CREATEJOBFROMTEMPLATEREQUEST_PARAMETERSENTRY']._serialized_end = 1286
    _globals['_GETTEMPLATEREQUEST']._serialized_start = 4806
    _globals['_GETTEMPLATEREQUEST']._serialized_end = 5003
    _globals['_GETTEMPLATEREQUEST_TEMPLATEVIEW']._serialized_start = 4958
    _globals['_GETTEMPLATEREQUEST_TEMPLATEVIEW']._serialized_end = 4991
    _globals['_GETTEMPLATERESPONSE']._serialized_start = 5006
    _globals['_GETTEMPLATERESPONSE']._serialized_end = 5325
    _globals['_GETTEMPLATERESPONSE_TEMPLATETYPE']._serialized_start = 5276
    _globals['_GETTEMPLATERESPONSE_TEMPLATETYPE']._serialized_end = 5325
    _globals['_LAUNCHTEMPLATEPARAMETERS']._serialized_start = 5328
    _globals['_LAUNCHTEMPLATEPARAMETERS']._serialized_end = 5762
    _globals['_LAUNCHTEMPLATEPARAMETERS_PARAMETERSENTRY']._serialized_start = 1237
    _globals['_LAUNCHTEMPLATEPARAMETERS_PARAMETERSENTRY']._serialized_end = 1286
    _globals['_LAUNCHTEMPLATEPARAMETERS_TRANSFORMNAMEMAPPINGENTRY']._serialized_start = 5703
    _globals['_LAUNCHTEMPLATEPARAMETERS_TRANSFORMNAMEMAPPINGENTRY']._serialized_end = 5762
    _globals['_LAUNCHTEMPLATEREQUEST']._serialized_start = 5765
    _globals['_LAUNCHTEMPLATEREQUEST']._serialized_end = 6041
    _globals['_LAUNCHTEMPLATERESPONSE']._serialized_start = 6043
    _globals['_LAUNCHTEMPLATERESPONSE']._serialized_end = 6110
    _globals['_INVALIDTEMPLATEPARAMETERS']._serialized_start = 6113
    _globals['_INVALIDTEMPLATEPARAMETERS']._serialized_end = 6303
    _globals['_INVALIDTEMPLATEPARAMETERS_PARAMETERVIOLATION']._serialized_start = 6243
    _globals['_INVALIDTEMPLATEPARAMETERS_PARAMETERVIOLATION']._serialized_end = 6303
    _globals['_DYNAMICTEMPLATELAUNCHPARAMS']._serialized_start = 6305
    _globals['_DYNAMICTEMPLATELAUNCHPARAMS']._serialized_end = 6378
    _globals['_TEMPLATESSERVICE']._serialized_start = 6829
    _globals['_TEMPLATESSERVICE']._serialized_end = 7693
    _globals['_FLEXTEMPLATESSERVICE']._serialized_start = 7696
    _globals['_FLEXTEMPLATESSERVICE']._serialized_end = 8045