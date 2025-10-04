"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/chunk.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/discoveryengine/v1/chunk.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto"\xff\x0b\n\x05Chunk\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0f\n\x07content\x18\x03 \x01(\t\x12!\n\x0frelevance_score\x18\x08 \x01(\x01B\x03\xe0A\x03H\x00\x88\x01\x01\x12R\n\x11document_metadata\x18\x05 \x01(\x0b27.google.cloud.discoveryengine.v1.Chunk.DocumentMetadata\x129\n\x13derived_struct_data\x18\x04 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x03\x12B\n\tpage_span\x18\x06 \x01(\x0b2/.google.cloud.discoveryengine.v1.Chunk.PageSpan\x12Q\n\x0echunk_metadata\x18\x07 \x01(\x0b24.google.cloud.discoveryengine.v1.Chunk.ChunkMetadataB\x03\xe0A\x03\x12\x16\n\tdata_urls\x18\t \x03(\tB\x03\xe0A\x03\x12 \n\x13annotation_contents\x18\x0b \x03(\tB\x03\xe0A\x03\x12[\n\x13annotation_metadata\x18\x0c \x03(\x0b29.google.cloud.discoveryengine.v1.Chunk.AnnotationMetadataB\x03\xe0A\x03\x1a\\\n\x10DocumentMetadata\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12,\n\x0bstruct_data\x18\x03 \x01(\x0b2\x17.google.protobuf.Struct\x1a0\n\x08PageSpan\x12\x12\n\npage_start\x18\x01 \x01(\x05\x12\x10\n\x08page_end\x18\x02 \x01(\x05\x1a\x8d\x01\n\rChunkMetadata\x12?\n\x0fprevious_chunks\x18\x01 \x03(\x0b2&.google.cloud.discoveryengine.v1.Chunk\x12;\n\x0bnext_chunks\x18\x02 \x03(\x0b2&.google.cloud.discoveryengine.v1.Chunk\x1a|\n\x11StructuredContent\x12Q\n\x0estructure_type\x18\x01 \x01(\x0e24.google.cloud.discoveryengine.v1.Chunk.StructureTypeB\x03\xe0A\x03\x12\x14\n\x07content\x18\x02 \x01(\tB\x03\xe0A\x03\x1a\x86\x01\n\x12AnnotationMetadata\x12Y\n\x12structured_content\x18\x01 \x01(\x0b28.google.cloud.discoveryengine.v1.Chunk.StructuredContentB\x03\xe0A\x03\x12\x15\n\x08image_id\x18\x02 \x01(\tB\x03\xe0A\x03"{\n\rStructureType\x12\x1e\n\x1aSTRUCTURE_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15SHAREHOLDER_STRUCTURE\x10\x01\x12\x17\n\x13SIGNATURE_STRUCTURE\x10\x02\x12\x16\n\x12CHECKBOX_STRUCTURE\x10\x03:\xb2\x02\xeaA\xae\x02\n$discoveryengine.googleapis.com/Chunk\x12uprojects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}/documents/{document}/chunks/{chunk}\x12\x8e\x01projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}/chunks/{chunk}B\x12\n\x10_relevance_scoreB\xfd\x01\n#com.google.cloud.discoveryengine.v1B\nChunkProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.chunk_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\nChunkProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_CHUNK_STRUCTUREDCONTENT'].fields_by_name['structure_type']._loaded_options = None
    _globals['_CHUNK_STRUCTUREDCONTENT'].fields_by_name['structure_type']._serialized_options = b'\xe0A\x03'
    _globals['_CHUNK_STRUCTUREDCONTENT'].fields_by_name['content']._loaded_options = None
    _globals['_CHUNK_STRUCTUREDCONTENT'].fields_by_name['content']._serialized_options = b'\xe0A\x03'
    _globals['_CHUNK_ANNOTATIONMETADATA'].fields_by_name['structured_content']._loaded_options = None
    _globals['_CHUNK_ANNOTATIONMETADATA'].fields_by_name['structured_content']._serialized_options = b'\xe0A\x03'
    _globals['_CHUNK_ANNOTATIONMETADATA'].fields_by_name['image_id']._loaded_options = None
    _globals['_CHUNK_ANNOTATIONMETADATA'].fields_by_name['image_id']._serialized_options = b'\xe0A\x03'
    _globals['_CHUNK'].fields_by_name['relevance_score']._loaded_options = None
    _globals['_CHUNK'].fields_by_name['relevance_score']._serialized_options = b'\xe0A\x03'
    _globals['_CHUNK'].fields_by_name['derived_struct_data']._loaded_options = None
    _globals['_CHUNK'].fields_by_name['derived_struct_data']._serialized_options = b'\xe0A\x03'
    _globals['_CHUNK'].fields_by_name['chunk_metadata']._loaded_options = None
    _globals['_CHUNK'].fields_by_name['chunk_metadata']._serialized_options = b'\xe0A\x03'
    _globals['_CHUNK'].fields_by_name['data_urls']._loaded_options = None
    _globals['_CHUNK'].fields_by_name['data_urls']._serialized_options = b'\xe0A\x03'
    _globals['_CHUNK'].fields_by_name['annotation_contents']._loaded_options = None
    _globals['_CHUNK'].fields_by_name['annotation_contents']._serialized_options = b'\xe0A\x03'
    _globals['_CHUNK'].fields_by_name['annotation_metadata']._loaded_options = None
    _globals['_CHUNK'].fields_by_name['annotation_metadata']._serialized_options = b'\xe0A\x03'
    _globals['_CHUNK']._loaded_options = None
    _globals['_CHUNK']._serialized_options = b'\xeaA\xae\x02\n$discoveryengine.googleapis.com/Chunk\x12uprojects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}/documents/{document}/chunks/{chunk}\x12\x8e\x01projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}/chunks/{chunk}'
    _globals['_CHUNK']._serialized_start = 171
    _globals['_CHUNK']._serialized_end = 1706
    _globals['_CHUNK_DOCUMENTMETADATA']._serialized_start = 703
    _globals['_CHUNK_DOCUMENTMETADATA']._serialized_end = 795
    _globals['_CHUNK_PAGESPAN']._serialized_start = 797
    _globals['_CHUNK_PAGESPAN']._serialized_end = 845
    _globals['_CHUNK_CHUNKMETADATA']._serialized_start = 848
    _globals['_CHUNK_CHUNKMETADATA']._serialized_end = 989
    _globals['_CHUNK_STRUCTUREDCONTENT']._serialized_start = 991
    _globals['_CHUNK_STRUCTUREDCONTENT']._serialized_end = 1115
    _globals['_CHUNK_ANNOTATIONMETADATA']._serialized_start = 1118
    _globals['_CHUNK_ANNOTATIONMETADATA']._serialized_end = 1252
    _globals['_CHUNK_STRUCTURETYPE']._serialized_start = 1254
    _globals['_CHUNK_STRUCTURETYPE']._serialized_end = 1377