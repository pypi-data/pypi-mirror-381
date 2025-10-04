"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1beta/chunk.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/discoveryengine/v1beta/chunk.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto"\xf8\x07\n\x05Chunk\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0f\n\x07content\x18\x03 \x01(\t\x12!\n\x0frelevance_score\x18\x08 \x01(\x01B\x03\xe0A\x03H\x00\x88\x01\x01\x12V\n\x11document_metadata\x18\x05 \x01(\x0b2;.google.cloud.discoveryengine.v1beta.Chunk.DocumentMetadata\x129\n\x13derived_struct_data\x18\x04 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x03\x12F\n\tpage_span\x18\x06 \x01(\x0b23.google.cloud.discoveryengine.v1beta.Chunk.PageSpan\x12U\n\x0echunk_metadata\x18\x07 \x01(\x0b28.google.cloud.discoveryengine.v1beta.Chunk.ChunkMetadataB\x03\xe0A\x03\x1a\\\n\x10DocumentMetadata\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12,\n\x0bstruct_data\x18\x03 \x01(\x0b2\x17.google.protobuf.Struct\x1a0\n\x08PageSpan\x12\x12\n\npage_start\x18\x01 \x01(\x05\x12\x10\n\x08page_end\x18\x02 \x01(\x05\x1a\x95\x01\n\rChunkMetadata\x12C\n\x0fprevious_chunks\x18\x01 \x03(\x0b2*.google.cloud.discoveryengine.v1beta.Chunk\x12?\n\x0bnext_chunks\x18\x02 \x03(\x0b2*.google.cloud.discoveryengine.v1beta.Chunk:\xb2\x02\xeaA\xae\x02\n$discoveryengine.googleapis.com/Chunk\x12uprojects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}/documents/{document}/chunks/{chunk}\x12\x8e\x01projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}/chunks/{chunk}B\x12\n\x10_relevance_scoreB\x91\x02\n\'com.google.cloud.discoveryengine.v1betaB\nChunkProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.chunk_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\nChunkProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
    _globals['_CHUNK'].fields_by_name['relevance_score']._loaded_options = None
    _globals['_CHUNK'].fields_by_name['relevance_score']._serialized_options = b'\xe0A\x03'
    _globals['_CHUNK'].fields_by_name['derived_struct_data']._loaded_options = None
    _globals['_CHUNK'].fields_by_name['derived_struct_data']._serialized_options = b'\xe0A\x03'
    _globals['_CHUNK'].fields_by_name['chunk_metadata']._loaded_options = None
    _globals['_CHUNK'].fields_by_name['chunk_metadata']._serialized_options = b'\xe0A\x03'
    _globals['_CHUNK']._loaded_options = None
    _globals['_CHUNK']._serialized_options = b'\xeaA\xae\x02\n$discoveryengine.googleapis.com/Chunk\x12uprojects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}/documents/{document}/chunks/{chunk}\x12\x8e\x01projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}/chunks/{chunk}'
    _globals['_CHUNK']._serialized_start = 179
    _globals['_CHUNK']._serialized_end = 1195
    _globals['_CHUNK_DOCUMENTMETADATA']._serialized_start = 572
    _globals['_CHUNK_DOCUMENTMETADATA']._serialized_end = 664
    _globals['_CHUNK_PAGESPAN']._serialized_start = 666
    _globals['_CHUNK_PAGESPAN']._serialized_end = 714
    _globals['_CHUNK_CHUNKMETADATA']._serialized_start = 717
    _globals['_CHUNK_CHUNKMETADATA']._serialized_end = 866