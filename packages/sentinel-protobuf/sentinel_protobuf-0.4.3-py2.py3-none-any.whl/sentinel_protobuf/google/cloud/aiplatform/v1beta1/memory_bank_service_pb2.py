"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/memory_bank_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import content_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_content__pb2
from .....google.cloud.aiplatform.v1beta1 import memory_bank_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_memory__bank__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/aiplatform/v1beta1/memory_bank_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/aiplatform/v1beta1/content.proto\x1a1google/cloud/aiplatform/v1beta1/memory_bank.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x96\x01\n\x13CreateMemoryRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine\x12<\n\x06memory\x18\x02 \x01(\x0b2\'.google.cloud.aiplatform.v1beta1.MemoryB\x03\xe0A\x02"t\n\x1dCreateMemoryOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"J\n\x10GetMemoryRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n aiplatform.googleapis.com/Memory"\x89\x01\n\x13UpdateMemoryRequest\x12<\n\x06memory\x18\x01 \x01(\x0b2\'.google.cloud.aiplatform.v1beta1.MemoryB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"t\n\x1dUpdateMemoryOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"\x9e\x01\n\x13ListMemoriesRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01"j\n\x14ListMemoriesResponse\x129\n\x08memories\x18\x01 \x03(\x0b2\'.google.cloud.aiplatform.v1beta1.Memory\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"M\n\x13DeleteMemoryRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n aiplatform.googleapis.com/Memory"t\n\x1dDeleteMemoryOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"\xa0\t\n\x17GenerateMemoriesRequest\x12m\n\x15vertex_session_source\x18\x02 \x01(\x0b2L.google.cloud.aiplatform.v1beta1.GenerateMemoriesRequest.VertexSessionSourceH\x00\x12o\n\x16direct_contents_source\x18\x03 \x01(\x0b2M.google.cloud.aiplatform.v1beta1.GenerateMemoriesRequest.DirectContentsSourceH\x00\x12o\n\x16direct_memories_source\x18\t \x01(\x0b2M.google.cloud.aiplatform.v1beta1.GenerateMemoriesRequest.DirectMemoriesSourceH\x00\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine\x12"\n\x15disable_consolidation\x18\x04 \x01(\x08B\x03\xe0A\x01\x12W\n\x05scope\x18\x08 \x03(\x0b2C.google.cloud.aiplatform.v1beta1.GenerateMemoriesRequest.ScopeEntryB\x03\xe0A\x01\x1a\xb9\x01\n\x13VertexSessionSource\x12:\n\x07session\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Session\x123\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x121\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x1a\xc9\x01\n\x14DirectContentsSource\x12h\n\x06events\x18\x01 \x03(\x0b2S.google.cloud.aiplatform.v1beta1.GenerateMemoriesRequest.DirectContentsSource.EventB\x03\xe0A\x02\x1aG\n\x05Event\x12>\n\x07content\x18\x01 \x01(\x0b2(.google.cloud.aiplatform.v1beta1.ContentB\x03\xe0A\x02\x1a\xb3\x01\n\x14DirectMemoriesSource\x12x\n\x0fdirect_memories\x18\x01 \x03(\x0b2Z.google.cloud.aiplatform.v1beta1.GenerateMemoriesRequest.DirectMemoriesSource.DirectMemoryB\x03\xe0A\x02\x1a!\n\x0cDirectMemory\x12\x11\n\x04fact\x18\x01 \x01(\tB\x03\xe0A\x02\x1a,\n\nScopeEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x08\n\x06source"\xf9\x02\n\x18GenerateMemoriesResponse\x12e\n\x12generated_memories\x18\x01 \x03(\x0b2I.google.cloud.aiplatform.v1beta1.GenerateMemoriesResponse.GeneratedMemory\x1a\xf5\x01\n\x0fGeneratedMemory\x127\n\x06memory\x18\x01 \x01(\x0b2\'.google.cloud.aiplatform.v1beta1.Memory\x12`\n\x06action\x18\x02 \x01(\x0e2P.google.cloud.aiplatform.v1beta1.GenerateMemoriesResponse.GeneratedMemory.Action"G\n\x06Action\x12\x16\n\x12ACTION_UNSPECIFIED\x10\x00\x12\x0b\n\x07CREATED\x10\x01\x12\x0b\n\x07UPDATED\x10\x02\x12\x0b\n\x07DELETED\x10\x03"x\n!GenerateMemoriesOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"\xf2\x04\n\x17RetrieveMemoriesRequest\x12s\n\x18similarity_search_params\x18\x06 \x01(\x0b2O.google.cloud.aiplatform.v1beta1.RetrieveMemoriesRequest.SimilaritySearchParamsH\x00\x12q\n\x17simple_retrieval_params\x18\x07 \x01(\x0b2N.google.cloud.aiplatform.v1beta1.RetrieveMemoriesRequest.SimpleRetrievalParamsH\x00\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine\x12W\n\x05scope\x18\x08 \x03(\x0b2C.google.cloud.aiplatform.v1beta1.RetrieveMemoriesRequest.ScopeEntryB\x03\xe0A\x02\x1aG\n\x16SimilaritySearchParams\x12\x19\n\x0csearch_query\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05top_k\x18\x02 \x01(\x05B\x03\xe0A\x01\x1aH\n\x15SimpleRetrievalParams\x12\x16\n\tpage_size\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01\x1a,\n\nScopeEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x12\n\x10retrieval_params"\xf8\x01\n\x18RetrieveMemoriesResponse\x12e\n\x12retrieved_memories\x18\x01 \x03(\x0b2I.google.cloud.aiplatform.v1beta1.RetrieveMemoriesResponse.RetrievedMemory\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x1a\\\n\x0fRetrievedMemory\x127\n\x06memory\x18\x01 \x01(\x0b2\'.google.cloud.aiplatform.v1beta1.Memory\x12\x10\n\x08distance\x18\x02 \x01(\x012\xe1\x10\n\x11MemoryBankService\x12\x9e\x02\n\x0cCreateMemory\x124.google.cloud.aiplatform.v1beta1.CreateMemoryRequest\x1a\x1d.google.longrunning.Operation"\xb8\x01\xcaA\'\n\x06Memory\x12\x1dCreateMemoryOperationMetadata\x82\xd3\xe4\x93\x02\x87\x01"D/v1beta1/{parent=projects/*/locations/*/reasoningEngines/*}/memories:\x06memoryZ7"-/v1beta1/{parent=reasoningEngines/*}/memories:\x06memory\x12\xee\x01\n\tGetMemory\x121.google.cloud.aiplatform.v1beta1.GetMemoryRequest\x1a\'.google.cloud.aiplatform.v1beta1.Memory"\x84\x01\xdaA\x04name\x82\xd3\xe4\x93\x02w\x12D/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/memories/*}Z/\x12-/v1beta1/{name=reasoningEngines/*/memories/*}\x12\xc1\x02\n\x0cUpdateMemory\x124.google.cloud.aiplatform.v1beta1.UpdateMemoryRequest\x1a\x1d.google.longrunning.Operation"\xdb\x01\xcaA\'\n\x06Memory\x12\x1dUpdateMemoryOperationMetadata\xdaA\x12memory,update_mask\x82\xd3\xe4\x93\x02\x95\x012K/v1beta1/{memory.name=projects/*/locations/*/reasoningEngines/*/memories/*}:\x06memoryZ>24/v1beta1/{memory.name=reasoningEngines/*/memories/*}:\x06memory\x12\x84\x02\n\x0cListMemories\x124.google.cloud.aiplatform.v1beta1.ListMemoriesRequest\x1a5.google.cloud.aiplatform.v1beta1.ListMemoriesResponse"\x86\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02w\x12D/v1beta1/{parent=projects/*/locations/*/reasoningEngines/*}/memoriesZ/\x12-/v1beta1/{parent=reasoningEngines/*}/memories\x12\xa3\x02\n\x0cDeleteMemory\x124.google.cloud.aiplatform.v1beta1.DeleteMemoryRequest\x1a\x1d.google.longrunning.Operation"\xbd\x01\xcaA6\n\x15google.protobuf.Empty\x12\x1dDeleteMemoryOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02w*D/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/memories/*}Z/*-/v1beta1/{name=reasoningEngines/*/memories/*}\x12\xcd\x02\n\x10GenerateMemories\x128.google.cloud.aiplatform.v1beta1.GenerateMemoriesRequest\x1a\x1d.google.longrunning.Operation"\xdf\x01\xcaA=\n\x18GenerateMemoriesResponse\x12!GenerateMemoriesOperationMetadata\xdaA\x06parent\x82\xd3\xe4\x93\x02\x8f\x01"M/v1beta1/{parent=projects/*/locations/*/reasoningEngines/*}/memories:generate:\x01*Z;"6/v1beta1/{parent=reasoningEngines/*}/memories:generate:\x01*\x12\xa9\x02\n\x10RetrieveMemories\x128.google.cloud.aiplatform.v1beta1.RetrieveMemoriesRequest\x1a9.google.cloud.aiplatform.v1beta1.RetrieveMemoriesResponse"\x9f\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\x8f\x01"M/v1beta1/{parent=projects/*/locations/*/reasoningEngines/*}/memories:retrieve:\x01*Z;"6/v1beta1/{parent=reasoningEngines/*}/memories:retrieve:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xed\x01\n#com.google.cloud.aiplatform.v1beta1B\x16MemoryBankServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.memory_bank_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x16MemoryBankServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CREATEMEMORYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEMEMORYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine'
    _globals['_CREATEMEMORYREQUEST'].fields_by_name['memory']._loaded_options = None
    _globals['_CREATEMEMORYREQUEST'].fields_by_name['memory']._serialized_options = b'\xe0A\x02'
    _globals['_GETMEMORYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMEMORYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n aiplatform.googleapis.com/Memory'
    _globals['_UPDATEMEMORYREQUEST'].fields_by_name['memory']._loaded_options = None
    _globals['_UPDATEMEMORYREQUEST'].fields_by_name['memory']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEMEMORYREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEMEMORYREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMEMORIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMEMORIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine'
    _globals['_LISTMEMORIESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTMEMORIESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMEMORIESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTMEMORIESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMEMORIESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTMEMORIESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEMEMORYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEMEMORYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n aiplatform.googleapis.com/Memory'
    _globals['_GENERATEMEMORIESREQUEST_VERTEXSESSIONSOURCE'].fields_by_name['session']._loaded_options = None
    _globals['_GENERATEMEMORIESREQUEST_VERTEXSESSIONSOURCE'].fields_by_name['session']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Session'
    _globals['_GENERATEMEMORIESREQUEST_VERTEXSESSIONSOURCE'].fields_by_name['start_time']._loaded_options = None
    _globals['_GENERATEMEMORIESREQUEST_VERTEXSESSIONSOURCE'].fields_by_name['start_time']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEMEMORIESREQUEST_VERTEXSESSIONSOURCE'].fields_by_name['end_time']._loaded_options = None
    _globals['_GENERATEMEMORIESREQUEST_VERTEXSESSIONSOURCE'].fields_by_name['end_time']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEMEMORIESREQUEST_DIRECTCONTENTSSOURCE_EVENT'].fields_by_name['content']._loaded_options = None
    _globals['_GENERATEMEMORIESREQUEST_DIRECTCONTENTSSOURCE_EVENT'].fields_by_name['content']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEMEMORIESREQUEST_DIRECTCONTENTSSOURCE'].fields_by_name['events']._loaded_options = None
    _globals['_GENERATEMEMORIESREQUEST_DIRECTCONTENTSSOURCE'].fields_by_name['events']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEMEMORIESREQUEST_DIRECTMEMORIESSOURCE_DIRECTMEMORY'].fields_by_name['fact']._loaded_options = None
    _globals['_GENERATEMEMORIESREQUEST_DIRECTMEMORIESSOURCE_DIRECTMEMORY'].fields_by_name['fact']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEMEMORIESREQUEST_DIRECTMEMORIESSOURCE'].fields_by_name['direct_memories']._loaded_options = None
    _globals['_GENERATEMEMORIESREQUEST_DIRECTMEMORIESSOURCE'].fields_by_name['direct_memories']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEMEMORIESREQUEST_SCOPEENTRY']._loaded_options = None
    _globals['_GENERATEMEMORIESREQUEST_SCOPEENTRY']._serialized_options = b'8\x01'
    _globals['_GENERATEMEMORIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_GENERATEMEMORIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine'
    _globals['_GENERATEMEMORIESREQUEST'].fields_by_name['disable_consolidation']._loaded_options = None
    _globals['_GENERATEMEMORIESREQUEST'].fields_by_name['disable_consolidation']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEMEMORIESREQUEST'].fields_by_name['scope']._loaded_options = None
    _globals['_GENERATEMEMORIESREQUEST'].fields_by_name['scope']._serialized_options = b'\xe0A\x01'
    _globals['_RETRIEVEMEMORIESREQUEST_SIMILARITYSEARCHPARAMS'].fields_by_name['search_query']._loaded_options = None
    _globals['_RETRIEVEMEMORIESREQUEST_SIMILARITYSEARCHPARAMS'].fields_by_name['search_query']._serialized_options = b'\xe0A\x02'
    _globals['_RETRIEVEMEMORIESREQUEST_SIMILARITYSEARCHPARAMS'].fields_by_name['top_k']._loaded_options = None
    _globals['_RETRIEVEMEMORIESREQUEST_SIMILARITYSEARCHPARAMS'].fields_by_name['top_k']._serialized_options = b'\xe0A\x01'
    _globals['_RETRIEVEMEMORIESREQUEST_SIMPLERETRIEVALPARAMS'].fields_by_name['page_size']._loaded_options = None
    _globals['_RETRIEVEMEMORIESREQUEST_SIMPLERETRIEVALPARAMS'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_RETRIEVEMEMORIESREQUEST_SIMPLERETRIEVALPARAMS'].fields_by_name['page_token']._loaded_options = None
    _globals['_RETRIEVEMEMORIESREQUEST_SIMPLERETRIEVALPARAMS'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_RETRIEVEMEMORIESREQUEST_SCOPEENTRY']._loaded_options = None
    _globals['_RETRIEVEMEMORIESREQUEST_SCOPEENTRY']._serialized_options = b'8\x01'
    _globals['_RETRIEVEMEMORIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_RETRIEVEMEMORIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine'
    _globals['_RETRIEVEMEMORIESREQUEST'].fields_by_name['scope']._loaded_options = None
    _globals['_RETRIEVEMEMORIESREQUEST'].fields_by_name['scope']._serialized_options = b'\xe0A\x02'
    _globals['_MEMORYBANKSERVICE']._loaded_options = None
    _globals['_MEMORYBANKSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_MEMORYBANKSERVICE'].methods_by_name['CreateMemory']._loaded_options = None
    _globals['_MEMORYBANKSERVICE'].methods_by_name['CreateMemory']._serialized_options = b'\xcaA\'\n\x06Memory\x12\x1dCreateMemoryOperationMetadata\x82\xd3\xe4\x93\x02\x87\x01"D/v1beta1/{parent=projects/*/locations/*/reasoningEngines/*}/memories:\x06memoryZ7"-/v1beta1/{parent=reasoningEngines/*}/memories:\x06memory'
    _globals['_MEMORYBANKSERVICE'].methods_by_name['GetMemory']._loaded_options = None
    _globals['_MEMORYBANKSERVICE'].methods_by_name['GetMemory']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02w\x12D/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/memories/*}Z/\x12-/v1beta1/{name=reasoningEngines/*/memories/*}'
    _globals['_MEMORYBANKSERVICE'].methods_by_name['UpdateMemory']._loaded_options = None
    _globals['_MEMORYBANKSERVICE'].methods_by_name['UpdateMemory']._serialized_options = b"\xcaA'\n\x06Memory\x12\x1dUpdateMemoryOperationMetadata\xdaA\x12memory,update_mask\x82\xd3\xe4\x93\x02\x95\x012K/v1beta1/{memory.name=projects/*/locations/*/reasoningEngines/*/memories/*}:\x06memoryZ>24/v1beta1/{memory.name=reasoningEngines/*/memories/*}:\x06memory"
    _globals['_MEMORYBANKSERVICE'].methods_by_name['ListMemories']._loaded_options = None
    _globals['_MEMORYBANKSERVICE'].methods_by_name['ListMemories']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02w\x12D/v1beta1/{parent=projects/*/locations/*/reasoningEngines/*}/memoriesZ/\x12-/v1beta1/{parent=reasoningEngines/*}/memories'
    _globals['_MEMORYBANKSERVICE'].methods_by_name['DeleteMemory']._loaded_options = None
    _globals['_MEMORYBANKSERVICE'].methods_by_name['DeleteMemory']._serialized_options = b'\xcaA6\n\x15google.protobuf.Empty\x12\x1dDeleteMemoryOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02w*D/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/memories/*}Z/*-/v1beta1/{name=reasoningEngines/*/memories/*}'
    _globals['_MEMORYBANKSERVICE'].methods_by_name['GenerateMemories']._loaded_options = None
    _globals['_MEMORYBANKSERVICE'].methods_by_name['GenerateMemories']._serialized_options = b'\xcaA=\n\x18GenerateMemoriesResponse\x12!GenerateMemoriesOperationMetadata\xdaA\x06parent\x82\xd3\xe4\x93\x02\x8f\x01"M/v1beta1/{parent=projects/*/locations/*/reasoningEngines/*}/memories:generate:\x01*Z;"6/v1beta1/{parent=reasoningEngines/*}/memories:generate:\x01*'
    _globals['_MEMORYBANKSERVICE'].methods_by_name['RetrieveMemories']._loaded_options = None
    _globals['_MEMORYBANKSERVICE'].methods_by_name['RetrieveMemories']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x8f\x01"M/v1beta1/{parent=projects/*/locations/*/reasoningEngines/*}/memories:retrieve:\x01*Z;"6/v1beta1/{parent=reasoningEngines/*}/memories:retrieve:\x01*'
    _globals['_CREATEMEMORYREQUEST']._serialized_start = 490
    _globals['_CREATEMEMORYREQUEST']._serialized_end = 640
    _globals['_CREATEMEMORYOPERATIONMETADATA']._serialized_start = 642
    _globals['_CREATEMEMORYOPERATIONMETADATA']._serialized_end = 758
    _globals['_GETMEMORYREQUEST']._serialized_start = 760
    _globals['_GETMEMORYREQUEST']._serialized_end = 834
    _globals['_UPDATEMEMORYREQUEST']._serialized_start = 837
    _globals['_UPDATEMEMORYREQUEST']._serialized_end = 974
    _globals['_UPDATEMEMORYOPERATIONMETADATA']._serialized_start = 976
    _globals['_UPDATEMEMORYOPERATIONMETADATA']._serialized_end = 1092
    _globals['_LISTMEMORIESREQUEST']._serialized_start = 1095
    _globals['_LISTMEMORIESREQUEST']._serialized_end = 1253
    _globals['_LISTMEMORIESRESPONSE']._serialized_start = 1255
    _globals['_LISTMEMORIESRESPONSE']._serialized_end = 1361
    _globals['_DELETEMEMORYREQUEST']._serialized_start = 1363
    _globals['_DELETEMEMORYREQUEST']._serialized_end = 1440
    _globals['_DELETEMEMORYOPERATIONMETADATA']._serialized_start = 1442
    _globals['_DELETEMEMORYOPERATIONMETADATA']._serialized_end = 1558
    _globals['_GENERATEMEMORIESREQUEST']._serialized_start = 1561
    _globals['_GENERATEMEMORIESREQUEST']._serialized_end = 2745
    _globals['_GENERATEMEMORIESREQUEST_VERTEXSESSIONSOURCE']._serialized_start = 2118
    _globals['_GENERATEMEMORIESREQUEST_VERTEXSESSIONSOURCE']._serialized_end = 2303
    _globals['_GENERATEMEMORIESREQUEST_DIRECTCONTENTSSOURCE']._serialized_start = 2306
    _globals['_GENERATEMEMORIESREQUEST_DIRECTCONTENTSSOURCE']._serialized_end = 2507
    _globals['_GENERATEMEMORIESREQUEST_DIRECTCONTENTSSOURCE_EVENT']._serialized_start = 2436
    _globals['_GENERATEMEMORIESREQUEST_DIRECTCONTENTSSOURCE_EVENT']._serialized_end = 2507
    _globals['_GENERATEMEMORIESREQUEST_DIRECTMEMORIESSOURCE']._serialized_start = 2510
    _globals['_GENERATEMEMORIESREQUEST_DIRECTMEMORIESSOURCE']._serialized_end = 2689
    _globals['_GENERATEMEMORIESREQUEST_DIRECTMEMORIESSOURCE_DIRECTMEMORY']._serialized_start = 2656
    _globals['_GENERATEMEMORIESREQUEST_DIRECTMEMORIESSOURCE_DIRECTMEMORY']._serialized_end = 2689
    _globals['_GENERATEMEMORIESREQUEST_SCOPEENTRY']._serialized_start = 2691
    _globals['_GENERATEMEMORIESREQUEST_SCOPEENTRY']._serialized_end = 2735
    _globals['_GENERATEMEMORIESRESPONSE']._serialized_start = 2748
    _globals['_GENERATEMEMORIESRESPONSE']._serialized_end = 3125
    _globals['_GENERATEMEMORIESRESPONSE_GENERATEDMEMORY']._serialized_start = 2880
    _globals['_GENERATEMEMORIESRESPONSE_GENERATEDMEMORY']._serialized_end = 3125
    _globals['_GENERATEMEMORIESRESPONSE_GENERATEDMEMORY_ACTION']._serialized_start = 3054
    _globals['_GENERATEMEMORIESRESPONSE_GENERATEDMEMORY_ACTION']._serialized_end = 3125
    _globals['_GENERATEMEMORIESOPERATIONMETADATA']._serialized_start = 3127
    _globals['_GENERATEMEMORIESOPERATIONMETADATA']._serialized_end = 3247
    _globals['_RETRIEVEMEMORIESREQUEST']._serialized_start = 3250
    _globals['_RETRIEVEMEMORIESREQUEST']._serialized_end = 3876
    _globals['_RETRIEVEMEMORIESREQUEST_SIMILARITYSEARCHPARAMS']._serialized_start = 3665
    _globals['_RETRIEVEMEMORIESREQUEST_SIMILARITYSEARCHPARAMS']._serialized_end = 3736
    _globals['_RETRIEVEMEMORIESREQUEST_SIMPLERETRIEVALPARAMS']._serialized_start = 3738
    _globals['_RETRIEVEMEMORIESREQUEST_SIMPLERETRIEVALPARAMS']._serialized_end = 3810
    _globals['_RETRIEVEMEMORIESREQUEST_SCOPEENTRY']._serialized_start = 2691
    _globals['_RETRIEVEMEMORIESREQUEST_SCOPEENTRY']._serialized_end = 2735
    _globals['_RETRIEVEMEMORIESRESPONSE']._serialized_start = 3879
    _globals['_RETRIEVEMEMORIESRESPONSE']._serialized_end = 4127
    _globals['_RETRIEVEMEMORIESRESPONSE_RETRIEVEDMEMORY']._serialized_start = 4035
    _globals['_RETRIEVEMEMORIESRESPONSE_RETRIEVEDMEMORY']._serialized_end = 4127
    _globals['_MEMORYBANKSERVICE']._serialized_start = 4130
    _globals['_MEMORYBANKSERVICE']._serialized_end = 6275