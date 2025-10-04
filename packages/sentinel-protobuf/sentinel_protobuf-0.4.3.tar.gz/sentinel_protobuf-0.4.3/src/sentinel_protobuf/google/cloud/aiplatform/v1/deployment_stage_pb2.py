"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/deployment_stage.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/aiplatform/v1/deployment_stage.proto\x12\x1agoogle.cloud.aiplatform.v1*\x81\x02\n\x0fDeploymentStage\x12 \n\x1cDEPLOYMENT_STAGE_UNSPECIFIED\x10\x00\x12\x17\n\x13STARTING_DEPLOYMENT\x10\x05\x12\x13\n\x0fPREPARING_MODEL\x10\x06\x12\x1c\n\x18CREATING_SERVING_CLUSTER\x10\x07\x12\x1b\n\x17ADDING_NODES_TO_CLUSTER\x10\x08\x12\x1b\n\x17GETTING_CONTAINER_IMAGE\x10\t\x12\x19\n\x15STARTING_MODEL_SERVER\x10\x03\x12\x10\n\x0cFINISHING_UP\x10\x04\x12\x19\n\x15DEPLOYMENT_TERMINATED\x10\nB\xd2\x01\n\x1ecom.google.cloud.aiplatform.v1B\x14DeploymentStageProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.deployment_stage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x14DeploymentStageProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_DEPLOYMENTSTAGE']._serialized_start = 82
    _globals['_DEPLOYMENTSTAGE']._serialized_end = 339