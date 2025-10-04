"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/reasoning_engine.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1beta1 import env_var_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_env__var__pb2
from .....google.cloud.aiplatform.v1beta1 import service_networking_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_service__networking__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/aiplatform/v1beta1/reasoning_engine.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/aiplatform/v1beta1/encryption_spec.proto\x1a-google/cloud/aiplatform/v1beta1/env_var.proto\x1a8google/cloud/aiplatform/v1beta1/service_networking.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbf\x08\n\x13ReasoningEngineSpec\x12!\n\x0fservice_account\x18\x01 \x01(\tB\x03\xe0A\x01H\x00\x88\x01\x01\x12[\n\x0cpackage_spec\x18\x02 \x01(\x0b2@.google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.PackageSpecB\x03\xe0A\x01\x12a\n\x0fdeployment_spec\x18\x04 \x01(\x0b2C.google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.DeploymentSpecB\x03\xe0A\x01\x123\n\rclass_methods\x18\x03 \x03(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x12\x1c\n\x0fagent_framework\x18\x05 \x01(\tB\x03\xe0A\x01\x1a\x98\x01\n\x0bPackageSpec\x12"\n\x15pickle_object_gcs_uri\x18\x01 \x01(\tB\x03\xe0A\x01\x12%\n\x18dependency_files_gcs_uri\x18\x02 \x01(\tB\x03\xe0A\x01\x12!\n\x14requirements_gcs_uri\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1b\n\x0epython_version\x18\x04 \x01(\tB\x03\xe0A\x01\x1a\xc2\x04\n\x0eDeploymentSpec\x129\n\x03env\x18\x01 \x03(\x0b2\'.google.cloud.aiplatform.v1beta1.EnvVarB\x03\xe0A\x01\x12F\n\nsecret_env\x18\x02 \x03(\x0b2-.google.cloud.aiplatform.v1beta1.SecretEnvVarB\x03\xe0A\x01\x12V\n\x14psc_interface_config\x18\x04 \x01(\x0b23.google.cloud.aiplatform.v1beta1.PscInterfaceConfigB\x03\xe0A\x01\x12\x1f\n\rmin_instances\x18\x05 \x01(\x05B\x03\xe0A\x01H\x00\x88\x01\x01\x12\x1f\n\rmax_instances\x18\x06 \x01(\x05B\x03\xe0A\x01H\x01\x88\x01\x01\x12u\n\x0fresource_limits\x18\x07 \x03(\x0b2W.google.cloud.aiplatform.v1beta1.ReasoningEngineSpec.DeploymentSpec.ResourceLimitsEntryB\x03\xe0A\x01\x12\'\n\x15container_concurrency\x18\x08 \x01(\x05B\x03\xe0A\x01H\x02\x88\x01\x01\x1a5\n\x13ResourceLimitsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x10\n\x0e_min_instancesB\x10\n\x0e_max_instancesB\x18\n\x16_container_concurrencyB\x12\n\x10_service_account"\xe5\x04\n\x0fReasoningEngine\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x07 \x01(\tB\x03\xe0A\x01\x12G\n\x04spec\x18\x03 \x01(\x0b24.google.cloud.aiplatform.v1beta1.ReasoningEngineSpecB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x06 \x01(\tB\x03\xe0A\x01\x12V\n\x0ccontext_spec\x18\t \x01(\x0b2;.google.cloud.aiplatform.v1beta1.ReasoningEngineContextSpecB\x03\xe0A\x01\x12H\n\x0fencryption_spec\x18\x0b \x01(\x0b2/.google.cloud.aiplatform.v1beta1.EncryptionSpec:\x9f\x01\xeaA\x9b\x01\n)aiplatform.googleapis.com/ReasoningEngine\x12Kprojects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}*\x10reasoningEngines2\x0freasoningEngine"\xec\x08\n\x1aReasoningEngineContextSpec\x12m\n\x12memory_bank_config\x18\x01 \x01(\x0b2L.google.cloud.aiplatform.v1beta1.ReasoningEngineContextSpec.MemoryBankConfigB\x03\xe0A\x01\x1a\xde\x07\n\x10MemoryBankConfig\x12}\n\x11generation_config\x18\x01 \x01(\x0b2].google.cloud.aiplatform.v1beta1.ReasoningEngineContextSpec.MemoryBankConfig.GenerationConfigB\x03\xe0A\x01\x12\x8a\x01\n\x18similarity_search_config\x18\x02 \x01(\x0b2c.google.cloud.aiplatform.v1beta1.ReasoningEngineContextSpec.MemoryBankConfig.SimilaritySearchConfigB\x03\xe0A\x01\x12o\n\nttl_config\x18\x05 \x01(\x0b2V.google.cloud.aiplatform.v1beta1.ReasoningEngineContextSpec.MemoryBankConfig.TtlConfigB\x03\xe0A\x01\x1a\x9e\x03\n\tTtlConfig\x125\n\x0bdefault_ttl\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01H\x00\x12\x8c\x01\n\x13granular_ttl_config\x18\x02 \x01(\x0b2h.google.cloud.aiplatform.v1beta1.ReasoningEngineContextSpec.MemoryBankConfig.TtlConfig.GranularTtlConfigB\x03\xe0A\x01H\x00\x1a\xc3\x01\n\x11GranularTtlConfig\x122\n\ncreate_ttl\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x12<\n\x14generate_created_ttl\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x12<\n\x14generate_updated_ttl\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01B\x05\n\x03ttl\x1aM\n\x10GenerationConfig\x129\n\x05model\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint\x1a]\n\x16SimilaritySearchConfig\x12C\n\x0fembedding_model\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/EndpointB\xeb\x01\n#com.google.cloud.aiplatform.v1beta1B\x14ReasoningEngineProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.reasoning_engine_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x14ReasoningEngineProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_REASONINGENGINESPEC_PACKAGESPEC'].fields_by_name['pickle_object_gcs_uri']._loaded_options = None
    _globals['_REASONINGENGINESPEC_PACKAGESPEC'].fields_by_name['pickle_object_gcs_uri']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESPEC_PACKAGESPEC'].fields_by_name['dependency_files_gcs_uri']._loaded_options = None
    _globals['_REASONINGENGINESPEC_PACKAGESPEC'].fields_by_name['dependency_files_gcs_uri']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESPEC_PACKAGESPEC'].fields_by_name['requirements_gcs_uri']._loaded_options = None
    _globals['_REASONINGENGINESPEC_PACKAGESPEC'].fields_by_name['requirements_gcs_uri']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESPEC_PACKAGESPEC'].fields_by_name['python_version']._loaded_options = None
    _globals['_REASONINGENGINESPEC_PACKAGESPEC'].fields_by_name['python_version']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESPEC_DEPLOYMENTSPEC_RESOURCELIMITSENTRY']._loaded_options = None
    _globals['_REASONINGENGINESPEC_DEPLOYMENTSPEC_RESOURCELIMITSENTRY']._serialized_options = b'8\x01'
    _globals['_REASONINGENGINESPEC_DEPLOYMENTSPEC'].fields_by_name['env']._loaded_options = None
    _globals['_REASONINGENGINESPEC_DEPLOYMENTSPEC'].fields_by_name['env']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESPEC_DEPLOYMENTSPEC'].fields_by_name['secret_env']._loaded_options = None
    _globals['_REASONINGENGINESPEC_DEPLOYMENTSPEC'].fields_by_name['secret_env']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESPEC_DEPLOYMENTSPEC'].fields_by_name['psc_interface_config']._loaded_options = None
    _globals['_REASONINGENGINESPEC_DEPLOYMENTSPEC'].fields_by_name['psc_interface_config']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESPEC_DEPLOYMENTSPEC'].fields_by_name['min_instances']._loaded_options = None
    _globals['_REASONINGENGINESPEC_DEPLOYMENTSPEC'].fields_by_name['min_instances']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESPEC_DEPLOYMENTSPEC'].fields_by_name['max_instances']._loaded_options = None
    _globals['_REASONINGENGINESPEC_DEPLOYMENTSPEC'].fields_by_name['max_instances']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESPEC_DEPLOYMENTSPEC'].fields_by_name['resource_limits']._loaded_options = None
    _globals['_REASONINGENGINESPEC_DEPLOYMENTSPEC'].fields_by_name['resource_limits']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESPEC_DEPLOYMENTSPEC'].fields_by_name['container_concurrency']._loaded_options = None
    _globals['_REASONINGENGINESPEC_DEPLOYMENTSPEC'].fields_by_name['container_concurrency']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESPEC'].fields_by_name['service_account']._loaded_options = None
    _globals['_REASONINGENGINESPEC'].fields_by_name['service_account']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESPEC'].fields_by_name['package_spec']._loaded_options = None
    _globals['_REASONINGENGINESPEC'].fields_by_name['package_spec']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESPEC'].fields_by_name['deployment_spec']._loaded_options = None
    _globals['_REASONINGENGINESPEC'].fields_by_name['deployment_spec']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESPEC'].fields_by_name['class_methods']._loaded_options = None
    _globals['_REASONINGENGINESPEC'].fields_by_name['class_methods']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESPEC'].fields_by_name['agent_framework']._loaded_options = None
    _globals['_REASONINGENGINESPEC'].fields_by_name['agent_framework']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINE'].fields_by_name['name']._loaded_options = None
    _globals['_REASONINGENGINE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_REASONINGENGINE'].fields_by_name['display_name']._loaded_options = None
    _globals['_REASONINGENGINE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_REASONINGENGINE'].fields_by_name['description']._loaded_options = None
    _globals['_REASONINGENGINE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINE'].fields_by_name['spec']._loaded_options = None
    _globals['_REASONINGENGINE'].fields_by_name['spec']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINE'].fields_by_name['create_time']._loaded_options = None
    _globals['_REASONINGENGINE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_REASONINGENGINE'].fields_by_name['update_time']._loaded_options = None
    _globals['_REASONINGENGINE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_REASONINGENGINE'].fields_by_name['etag']._loaded_options = None
    _globals['_REASONINGENGINE'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINE'].fields_by_name['context_spec']._loaded_options = None
    _globals['_REASONINGENGINE'].fields_by_name['context_spec']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINE']._loaded_options = None
    _globals['_REASONINGENGINE']._serialized_options = b'\xeaA\x9b\x01\n)aiplatform.googleapis.com/ReasoningEngine\x12Kprojects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}*\x10reasoningEngines2\x0freasoningEngine'
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_TTLCONFIG_GRANULARTTLCONFIG'].fields_by_name['create_ttl']._loaded_options = None
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_TTLCONFIG_GRANULARTTLCONFIG'].fields_by_name['create_ttl']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_TTLCONFIG_GRANULARTTLCONFIG'].fields_by_name['generate_created_ttl']._loaded_options = None
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_TTLCONFIG_GRANULARTTLCONFIG'].fields_by_name['generate_created_ttl']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_TTLCONFIG_GRANULARTTLCONFIG'].fields_by_name['generate_updated_ttl']._loaded_options = None
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_TTLCONFIG_GRANULARTTLCONFIG'].fields_by_name['generate_updated_ttl']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_TTLCONFIG'].fields_by_name['default_ttl']._loaded_options = None
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_TTLCONFIG'].fields_by_name['default_ttl']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_TTLCONFIG'].fields_by_name['granular_ttl_config']._loaded_options = None
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_TTLCONFIG'].fields_by_name['granular_ttl_config']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_GENERATIONCONFIG'].fields_by_name['model']._loaded_options = None
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_GENERATIONCONFIG'].fields_by_name['model']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_SIMILARITYSEARCHCONFIG'].fields_by_name['embedding_model']._loaded_options = None
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_SIMILARITYSEARCHCONFIG'].fields_by_name['embedding_model']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG'].fields_by_name['generation_config']._loaded_options = None
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG'].fields_by_name['generation_config']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG'].fields_by_name['similarity_search_config']._loaded_options = None
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG'].fields_by_name['similarity_search_config']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG'].fields_by_name['ttl_config']._loaded_options = None
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG'].fields_by_name['ttl_config']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINECONTEXTSPEC'].fields_by_name['memory_bank_config']._loaded_options = None
    _globals['_REASONINGENGINECONTEXTSPEC'].fields_by_name['memory_bank_config']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESPEC']._serialized_start = 407
    _globals['_REASONINGENGINESPEC']._serialized_end = 1494
    _globals['_REASONINGENGINESPEC_PACKAGESPEC']._serialized_start = 741
    _globals['_REASONINGENGINESPEC_PACKAGESPEC']._serialized_end = 893
    _globals['_REASONINGENGINESPEC_DEPLOYMENTSPEC']._serialized_start = 896
    _globals['_REASONINGENGINESPEC_DEPLOYMENTSPEC']._serialized_end = 1474
    _globals['_REASONINGENGINESPEC_DEPLOYMENTSPEC_RESOURCELIMITSENTRY']._serialized_start = 1359
    _globals['_REASONINGENGINESPEC_DEPLOYMENTSPEC_RESOURCELIMITSENTRY']._serialized_end = 1412
    _globals['_REASONINGENGINE']._serialized_start = 1497
    _globals['_REASONINGENGINE']._serialized_end = 2110
    _globals['_REASONINGENGINECONTEXTSPEC']._serialized_start = 2113
    _globals['_REASONINGENGINECONTEXTSPEC']._serialized_end = 3245
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG']._serialized_start = 2255
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG']._serialized_end = 3245
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_TTLCONFIG']._serialized_start = 2657
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_TTLCONFIG']._serialized_end = 3071
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_TTLCONFIG_GRANULARTTLCONFIG']._serialized_start = 2869
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_TTLCONFIG_GRANULARTTLCONFIG']._serialized_end = 3064
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_GENERATIONCONFIG']._serialized_start = 3073
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_GENERATIONCONFIG']._serialized_end = 3150
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_SIMILARITYSEARCHCONFIG']._serialized_start = 3152
    _globals['_REASONINGENGINECONTEXTSPEC_MEMORYBANKCONFIG_SIMILARITYSEARCHCONFIG']._serialized_end = 3245