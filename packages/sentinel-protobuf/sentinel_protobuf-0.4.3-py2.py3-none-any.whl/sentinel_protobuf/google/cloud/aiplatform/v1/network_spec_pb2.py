"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/network_spec.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/aiplatform/v1/network_spec.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x19google/api/resource.proto"\x9f\x01\n\x0bNetworkSpec\x12\x1e\n\x16enable_internet_access\x18\x01 \x01(\x08\x124\n\x07network\x18\x02 \x01(\tB#\xfaA \n\x1ecompute.googleapis.com/Network\x12:\n\nsubnetwork\x18\x03 \x01(\tB&\xfaA#\n!compute.googleapis.com/SubnetworkB\xb2\x02\n\x1ecom.google.cloud.aiplatform.v1B\x10NetworkSpecProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1\xeaAa\n!compute.googleapis.com/Subnetwork\x12<projects/{project}/regions/{region}/subnetworks/{subnetwork}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.network_spec_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x10NetworkSpecProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1\xeaAa\n!compute.googleapis.com/Subnetwork\x12<projects/{project}/regions/{region}/subnetworks/{subnetwork}'
    _globals['_NETWORKSPEC'].fields_by_name['network']._loaded_options = None
    _globals['_NETWORKSPEC'].fields_by_name['network']._serialized_options = b'\xfaA \n\x1ecompute.googleapis.com/Network'
    _globals['_NETWORKSPEC'].fields_by_name['subnetwork']._loaded_options = None
    _globals['_NETWORKSPEC'].fields_by_name['subnetwork']._serialized_options = b'\xfaA#\n!compute.googleapis.com/Subnetwork'
    _globals['_NETWORKSPEC']._serialized_start = 105
    _globals['_NETWORKSPEC']._serialized_end = 264