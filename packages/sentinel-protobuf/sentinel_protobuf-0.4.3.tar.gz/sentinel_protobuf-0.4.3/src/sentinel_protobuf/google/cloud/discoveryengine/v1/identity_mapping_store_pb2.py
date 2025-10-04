"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/identity_mapping_store.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import cmek_config_service_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_cmek__config__service__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/discoveryengine/v1/identity_mapping_store.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a9google/cloud/discoveryengine/v1/cmek_config_service.proto"\x9f\x02\n\x14IdentityMappingStore\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0ckms_key_name\x18\x03 \x01(\tB\x03\xe0A\x04\x12E\n\x0bcmek_config\x18\x04 \x01(\x0b2+.google.cloud.discoveryengine.v1.CmekConfigB\x03\xe0A\x03:\x91\x01\xeaA\x8d\x01\n3discoveryengine.googleapis.com/IdentityMappingStore\x12Vprojects/{project}/locations/{location}/identityMappingStores/{identity_mapping_store}"u\n\x14IdentityMappingEntry\x12\x11\n\x07user_id\x18\x02 \x01(\tH\x00\x12\x12\n\x08group_id\x18\x03 \x01(\tH\x00\x12\x1e\n\x11external_identity\x18\x01 \x01(\tB\x03\xe0A\x02B\x16\n\x14identity_provider_idB\x8c\x02\n#com.google.cloud.discoveryengine.v1B\x19IdentityMappingStoreProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.identity_mapping_store_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x19IdentityMappingStoreProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_IDENTITYMAPPINGSTORE'].fields_by_name['name']._loaded_options = None
    _globals['_IDENTITYMAPPINGSTORE'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_IDENTITYMAPPINGSTORE'].fields_by_name['kms_key_name']._loaded_options = None
    _globals['_IDENTITYMAPPINGSTORE'].fields_by_name['kms_key_name']._serialized_options = b'\xe0A\x04'
    _globals['_IDENTITYMAPPINGSTORE'].fields_by_name['cmek_config']._loaded_options = None
    _globals['_IDENTITYMAPPINGSTORE'].fields_by_name['cmek_config']._serialized_options = b'\xe0A\x03'
    _globals['_IDENTITYMAPPINGSTORE']._loaded_options = None
    _globals['_IDENTITYMAPPINGSTORE']._serialized_options = b'\xeaA\x8d\x01\n3discoveryengine.googleapis.com/IdentityMappingStore\x12Vprojects/{project}/locations/{location}/identityMappingStores/{identity_mapping_store}'
    _globals['_IDENTITYMAPPINGENTRY'].fields_by_name['external_identity']._loaded_options = None
    _globals['_IDENTITYMAPPINGENTRY'].fields_by_name['external_identity']._serialized_options = b'\xe0A\x02'
    _globals['_IDENTITYMAPPINGSTORE']._serialized_start = 217
    _globals['_IDENTITYMAPPINGSTORE']._serialized_end = 504
    _globals['_IDENTITYMAPPINGENTRY']._serialized_start = 506
    _globals['_IDENTITYMAPPINGENTRY']._serialized_end = 623