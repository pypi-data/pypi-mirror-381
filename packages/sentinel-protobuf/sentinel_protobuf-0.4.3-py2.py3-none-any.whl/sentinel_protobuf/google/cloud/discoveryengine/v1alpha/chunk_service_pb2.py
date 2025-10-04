"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1alpha/chunk_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1alpha import chunk_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_chunk__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/discoveryengine/v1alpha/chunk_service.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/discoveryengine/v1alpha/chunk.proto"M\n\x0fGetChunkRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$discoveryengine.googleapis.com/Chunk"{\n\x11ListChunksRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'discoveryengine.googleapis.com/Document\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"j\n\x12ListChunksResponse\x12;\n\x06chunks\x18\x01 \x03(\x0b2+.google.cloud.discoveryengine.v1alpha.Chunk\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xed\x05\n\x0cChunkService\x12\xb9\x02\n\x08GetChunk\x125.google.cloud.discoveryengine.v1alpha.GetChunkRequest\x1a+.google.cloud.discoveryengine.v1alpha.Chunk"\xc8\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xba\x01\x12S/v1alpha/{name=projects/*/locations/*/dataStores/*/branches/*/documents/*/chunks/*}Zc\x12a/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*/chunks/*}\x12\xcc\x02\n\nListChunks\x127.google.cloud.discoveryengine.v1alpha.ListChunksRequest\x1a8.google.cloud.discoveryengine.v1alpha.ListChunksResponse"\xca\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xba\x01\x12S/v1alpha/{parent=projects/*/locations/*/dataStores/*/branches/*/documents/*}/chunksZc\x12a/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}/chunks\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x9d\x02\n(com.google.cloud.discoveryengine.v1alphaB\x11ChunkServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.chunk_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x11ChunkServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_GETCHUNKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCHUNKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$discoveryengine.googleapis.com/Chunk'
    _globals['_LISTCHUNKSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCHUNKSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\n'discoveryengine.googleapis.com/Document"
    _globals['_CHUNKSERVICE']._loaded_options = None
    _globals['_CHUNKSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CHUNKSERVICE'].methods_by_name['GetChunk']._loaded_options = None
    _globals['_CHUNKSERVICE'].methods_by_name['GetChunk']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xba\x01\x12S/v1alpha/{name=projects/*/locations/*/dataStores/*/branches/*/documents/*/chunks/*}Zc\x12a/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*/chunks/*}'
    _globals['_CHUNKSERVICE'].methods_by_name['ListChunks']._loaded_options = None
    _globals['_CHUNKSERVICE'].methods_by_name['ListChunks']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xba\x01\x12S/v1alpha/{parent=projects/*/locations/*/dataStores/*/branches/*/documents/*}/chunksZc\x12a/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}/chunks'
    _globals['_GETCHUNKREQUEST']._serialized_start = 263
    _globals['_GETCHUNKREQUEST']._serialized_end = 340
    _globals['_LISTCHUNKSREQUEST']._serialized_start = 342
    _globals['_LISTCHUNKSREQUEST']._serialized_end = 465
    _globals['_LISTCHUNKSRESPONSE']._serialized_start = 467
    _globals['_LISTCHUNKSRESPONSE']._serialized_end = 573
    _globals['_CHUNKSERVICE']._serialized_start = 576
    _globals['_CHUNKSERVICE']._serialized_end = 1325