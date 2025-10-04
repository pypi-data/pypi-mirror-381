"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/vertex_rag_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import content_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_content__pb2
from .....google.cloud.aiplatform.v1beta1 import tool_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_tool__pb2
from .....google.cloud.aiplatform.v1beta1 import vertex_rag_data_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_vertex__rag__data__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/aiplatform/v1beta1/vertex_rag_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/aiplatform/v1beta1/content.proto\x1a*google/cloud/aiplatform/v1beta1/tool.proto\x1a5google/cloud/aiplatform/v1beta1/vertex_rag_data.proto"\x9a\x02\n\x08RagQuery\x12\x13\n\x04text\x18\x01 \x01(\tB\x03\xe0A\x01H\x00\x12\x1f\n\x10similarity_top_k\x18\x02 \x01(\x05B\x05\x18\x01\xe0A\x01\x12I\n\x07ranking\x18\x04 \x01(\x0b21.google.cloud.aiplatform.v1beta1.RagQuery.RankingB\x05\x18\x01\xe0A\x01\x12V\n\x14rag_retrieval_config\x18\x06 \x01(\x0b23.google.cloud.aiplatform.v1beta1.RagRetrievalConfigB\x03\xe0A\x01\x1a,\n\x07Ranking\x12\x17\n\x05alpha\x18\x01 \x01(\x02B\x03\xe0A\x01H\x00\x88\x01\x01B\x08\n\x06_alphaB\x07\n\x05query"\xdf\x04\n\x17RetrieveContextsRequest\x12c\n\x10vertex_rag_store\x18\x02 \x01(\x0b2G.google.cloud.aiplatform.v1beta1.RetrieveContextsRequest.VertexRagStoreH\x00\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12=\n\x05query\x18\x03 \x01(\x0b2).google.cloud.aiplatform.v1beta1.RagQueryB\x03\xe0A\x02\x1a\xd5\x02\n\x0eVertexRagStore\x12\x1a\n\x0brag_corpora\x18\x01 \x03(\tB\x05\x18\x01\xe0A\x01\x12o\n\rrag_resources\x18\x03 \x03(\x0b2S.google.cloud.aiplatform.v1beta1.RetrieveContextsRequest.VertexRagStore.RagResourceB\x03\xe0A\x01\x12-\n\x19vector_distance_threshold\x18\x02 \x01(\x01B\x05\x18\x01\xe0A\x01H\x00\x88\x01\x01\x1ai\n\x0bRagResource\x12?\n\nrag_corpus\x18\x01 \x01(\tB+\xe0A\x01\xfaA%\n#aiplatform.googleapis.com/RagCorpus\x12\x19\n\x0crag_file_ids\x18\x02 \x03(\tB\x03\xe0A\x01B\x1c\n\x1a_vector_distance_thresholdB\r\n\x0bdata_source"\xab\x02\n\x0bRagContexts\x12F\n\x08contexts\x18\x01 \x03(\x0b24.google.cloud.aiplatform.v1beta1.RagContexts.Context\x1a\xd3\x01\n\x07Context\x12\x12\n\nsource_uri\x18\x01 \x01(\t\x12\x1b\n\x13source_display_name\x18\x05 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x14\n\x08distance\x18\x03 \x01(\x01B\x02\x18\x01\x12\x1b\n\x0fsparse_distance\x18\x04 \x01(\x01B\x02\x18\x01\x12\x12\n\x05score\x18\x06 \x01(\x01H\x00\x88\x01\x01\x128\n\x05chunk\x18\x07 \x01(\x0b2).google.cloud.aiplatform.v1beta1.RagChunkB\x08\n\x06_score"Z\n\x18RetrieveContextsResponse\x12>\n\x08contexts\x18\x01 \x01(\x0b2,.google.cloud.aiplatform.v1beta1.RagContexts"\xfd\x02\n\x14AugmentPromptRequest\x12P\n\x10vertex_rag_store\x18\x04 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.VertexRagStoreB\x03\xe0A\x01H\x00\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12?\n\x08contents\x18\x02 \x03(\x0b2(.google.cloud.aiplatform.v1beta1.ContentB\x03\xe0A\x01\x12O\n\x05model\x18\x03 \x01(\x0b2;.google.cloud.aiplatform.v1beta1.AugmentPromptRequest.ModelB\x03\xe0A\x01\x1a7\n\x05Model\x12\x12\n\x05model\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rmodel_version\x18\x02 \x01(\tB\x03\xe0A\x01B\r\n\x0bdata_source"\x91\x01\n\x15AugmentPromptResponse\x12B\n\x10augmented_prompt\x18\x01 \x03(\x0b2(.google.cloud.aiplatform.v1beta1.Content\x124\n\x05facts\x18\x02 \x03(\x0b2%.google.cloud.aiplatform.v1beta1.Fact"\xf1\x02\n\x19CorroborateContentRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12C\n\x07content\x18\x02 \x01(\x0b2(.google.cloud.aiplatform.v1beta1.ContentB\x03\xe0A\x01H\x00\x88\x01\x01\x129\n\x05facts\x18\x03 \x03(\x0b2%.google.cloud.aiplatform.v1beta1.FactB\x03\xe0A\x01\x12^\n\nparameters\x18\x04 \x01(\x0b2E.google.cloud.aiplatform.v1beta1.CorroborateContentRequest.ParametersB\x03\xe0A\x01\x1a-\n\nParameters\x12\x1f\n\x12citation_threshold\x18\x01 \x01(\x01B\x03\xe0A\x01B\n\n\x08_content"\x8e\x01\n\x1aCorroborateContentResponse\x12 \n\x13corroboration_score\x18\x01 \x01(\x02H\x00\x88\x01\x01\x126\n\x06claims\x18\x02 \x03(\x0b2&.google.cloud.aiplatform.v1beta1.ClaimB\x16\n\x14_corroboration_score"\x9b\x02\n\x04Fact\x12\x12\n\x05query\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05title\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x10\n\x03uri\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x14\n\x07summary\x18\x04 \x01(\tH\x03\x88\x01\x01\x12 \n\x0fvector_distance\x18\x05 \x01(\x01B\x02\x18\x01H\x04\x88\x01\x01\x12\x12\n\x05score\x18\x06 \x01(\x01H\x05\x88\x01\x01\x12=\n\x05chunk\x18\x07 \x01(\x0b2).google.cloud.aiplatform.v1beta1.RagChunkH\x06\x88\x01\x01B\x08\n\x06_queryB\x08\n\x06_titleB\x06\n\x04_uriB\n\n\x08_summaryB\x12\n\x10_vector_distanceB\x08\n\x06_scoreB\x08\n\x06_chunk"\x8b\x01\n\x05Claim\x12\x18\n\x0bstart_index\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x16\n\tend_index\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x14\n\x0cfact_indexes\x18\x03 \x03(\x05\x12\x12\n\x05score\x18\x04 \x01(\x02H\x02\x88\x01\x01B\x0e\n\x0c_start_indexB\x0c\n\n_end_indexB\x08\n\x06_score2\x93\x06\n\x10VertexRagService\x12\xdc\x01\n\x10RetrieveContexts\x128.google.cloud.aiplatform.v1beta1.RetrieveContextsRequest\x1a9.google.cloud.aiplatform.v1beta1.RetrieveContextsResponse"S\xdaA\x0cparent,query\x82\xd3\xe4\x93\x02>"9/v1beta1/{parent=projects/*/locations/*}:retrieveContexts:\x01*\x12\xe1\x01\n\rAugmentPrompt\x125.google.cloud.aiplatform.v1beta1.AugmentPromptRequest\x1a6.google.cloud.aiplatform.v1beta1.AugmentPromptResponse"a\xdaA\x1dparent,model,vertex_rag_store\x82\xd3\xe4\x93\x02;"6/v1beta1/{parent=projects/*/locations/*}:augmentPrompt:\x01*\x12\xec\x01\n\x12CorroborateContent\x12:.google.cloud.aiplatform.v1beta1.CorroborateContentRequest\x1a;.google.cloud.aiplatform.v1beta1.CorroborateContentResponse"]\xdaA\x14parent,content,facts\x82\xd3\xe4\x93\x02@";/v1beta1/{parent=projects/*/locations/*}:corroborateContent:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xec\x01\n#com.google.cloud.aiplatform.v1beta1B\x15VertexRagServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.vertex_rag_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x15VertexRagServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_RAGQUERY_RANKING'].fields_by_name['alpha']._loaded_options = None
    _globals['_RAGQUERY_RANKING'].fields_by_name['alpha']._serialized_options = b'\xe0A\x01'
    _globals['_RAGQUERY'].fields_by_name['text']._loaded_options = None
    _globals['_RAGQUERY'].fields_by_name['text']._serialized_options = b'\xe0A\x01'
    _globals['_RAGQUERY'].fields_by_name['similarity_top_k']._loaded_options = None
    _globals['_RAGQUERY'].fields_by_name['similarity_top_k']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_RAGQUERY'].fields_by_name['ranking']._loaded_options = None
    _globals['_RAGQUERY'].fields_by_name['ranking']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_RAGQUERY'].fields_by_name['rag_retrieval_config']._loaded_options = None
    _globals['_RAGQUERY'].fields_by_name['rag_retrieval_config']._serialized_options = b'\xe0A\x01'
    _globals['_RETRIEVECONTEXTSREQUEST_VERTEXRAGSTORE_RAGRESOURCE'].fields_by_name['rag_corpus']._loaded_options = None
    _globals['_RETRIEVECONTEXTSREQUEST_VERTEXRAGSTORE_RAGRESOURCE'].fields_by_name['rag_corpus']._serialized_options = b'\xe0A\x01\xfaA%\n#aiplatform.googleapis.com/RagCorpus'
    _globals['_RETRIEVECONTEXTSREQUEST_VERTEXRAGSTORE_RAGRESOURCE'].fields_by_name['rag_file_ids']._loaded_options = None
    _globals['_RETRIEVECONTEXTSREQUEST_VERTEXRAGSTORE_RAGRESOURCE'].fields_by_name['rag_file_ids']._serialized_options = b'\xe0A\x01'
    _globals['_RETRIEVECONTEXTSREQUEST_VERTEXRAGSTORE'].fields_by_name['rag_corpora']._loaded_options = None
    _globals['_RETRIEVECONTEXTSREQUEST_VERTEXRAGSTORE'].fields_by_name['rag_corpora']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_RETRIEVECONTEXTSREQUEST_VERTEXRAGSTORE'].fields_by_name['rag_resources']._loaded_options = None
    _globals['_RETRIEVECONTEXTSREQUEST_VERTEXRAGSTORE'].fields_by_name['rag_resources']._serialized_options = b'\xe0A\x01'
    _globals['_RETRIEVECONTEXTSREQUEST_VERTEXRAGSTORE'].fields_by_name['vector_distance_threshold']._loaded_options = None
    _globals['_RETRIEVECONTEXTSREQUEST_VERTEXRAGSTORE'].fields_by_name['vector_distance_threshold']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_RETRIEVECONTEXTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_RETRIEVECONTEXTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_RETRIEVECONTEXTSREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_RETRIEVECONTEXTSREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x02'
    _globals['_RAGCONTEXTS_CONTEXT'].fields_by_name['distance']._loaded_options = None
    _globals['_RAGCONTEXTS_CONTEXT'].fields_by_name['distance']._serialized_options = b'\x18\x01'
    _globals['_RAGCONTEXTS_CONTEXT'].fields_by_name['sparse_distance']._loaded_options = None
    _globals['_RAGCONTEXTS_CONTEXT'].fields_by_name['sparse_distance']._serialized_options = b'\x18\x01'
    _globals['_AUGMENTPROMPTREQUEST_MODEL'].fields_by_name['model']._loaded_options = None
    _globals['_AUGMENTPROMPTREQUEST_MODEL'].fields_by_name['model']._serialized_options = b'\xe0A\x01'
    _globals['_AUGMENTPROMPTREQUEST_MODEL'].fields_by_name['model_version']._loaded_options = None
    _globals['_AUGMENTPROMPTREQUEST_MODEL'].fields_by_name['model_version']._serialized_options = b'\xe0A\x01'
    _globals['_AUGMENTPROMPTREQUEST'].fields_by_name['vertex_rag_store']._loaded_options = None
    _globals['_AUGMENTPROMPTREQUEST'].fields_by_name['vertex_rag_store']._serialized_options = b'\xe0A\x01'
    _globals['_AUGMENTPROMPTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_AUGMENTPROMPTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_AUGMENTPROMPTREQUEST'].fields_by_name['contents']._loaded_options = None
    _globals['_AUGMENTPROMPTREQUEST'].fields_by_name['contents']._serialized_options = b'\xe0A\x01'
    _globals['_AUGMENTPROMPTREQUEST'].fields_by_name['model']._loaded_options = None
    _globals['_AUGMENTPROMPTREQUEST'].fields_by_name['model']._serialized_options = b'\xe0A\x01'
    _globals['_CORROBORATECONTENTREQUEST_PARAMETERS'].fields_by_name['citation_threshold']._loaded_options = None
    _globals['_CORROBORATECONTENTREQUEST_PARAMETERS'].fields_by_name['citation_threshold']._serialized_options = b'\xe0A\x01'
    _globals['_CORROBORATECONTENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CORROBORATECONTENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CORROBORATECONTENTREQUEST'].fields_by_name['content']._loaded_options = None
    _globals['_CORROBORATECONTENTREQUEST'].fields_by_name['content']._serialized_options = b'\xe0A\x01'
    _globals['_CORROBORATECONTENTREQUEST'].fields_by_name['facts']._loaded_options = None
    _globals['_CORROBORATECONTENTREQUEST'].fields_by_name['facts']._serialized_options = b'\xe0A\x01'
    _globals['_CORROBORATECONTENTREQUEST'].fields_by_name['parameters']._loaded_options = None
    _globals['_CORROBORATECONTENTREQUEST'].fields_by_name['parameters']._serialized_options = b'\xe0A\x01'
    _globals['_FACT'].fields_by_name['vector_distance']._loaded_options = None
    _globals['_FACT'].fields_by_name['vector_distance']._serialized_options = b'\x18\x01'
    _globals['_VERTEXRAGSERVICE']._loaded_options = None
    _globals['_VERTEXRAGSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_VERTEXRAGSERVICE'].methods_by_name['RetrieveContexts']._loaded_options = None
    _globals['_VERTEXRAGSERVICE'].methods_by_name['RetrieveContexts']._serialized_options = b'\xdaA\x0cparent,query\x82\xd3\xe4\x93\x02>"9/v1beta1/{parent=projects/*/locations/*}:retrieveContexts:\x01*'
    _globals['_VERTEXRAGSERVICE'].methods_by_name['AugmentPrompt']._loaded_options = None
    _globals['_VERTEXRAGSERVICE'].methods_by_name['AugmentPrompt']._serialized_options = b'\xdaA\x1dparent,model,vertex_rag_store\x82\xd3\xe4\x93\x02;"6/v1beta1/{parent=projects/*/locations/*}:augmentPrompt:\x01*'
    _globals['_VERTEXRAGSERVICE'].methods_by_name['CorroborateContent']._loaded_options = None
    _globals['_VERTEXRAGSERVICE'].methods_by_name['CorroborateContent']._serialized_options = b'\xdaA\x14parent,content,facts\x82\xd3\xe4\x93\x02@";/v1beta1/{parent=projects/*/locations/*}:corroborateContent:\x01*'
    _globals['_RAGQUERY']._serialized_start = 355
    _globals['_RAGQUERY']._serialized_end = 637
    _globals['_RAGQUERY_RANKING']._serialized_start = 584
    _globals['_RAGQUERY_RANKING']._serialized_end = 628
    _globals['_RETRIEVECONTEXTSREQUEST']._serialized_start = 640
    _globals['_RETRIEVECONTEXTSREQUEST']._serialized_end = 1247
    _globals['_RETRIEVECONTEXTSREQUEST_VERTEXRAGSTORE']._serialized_start = 891
    _globals['_RETRIEVECONTEXTSREQUEST_VERTEXRAGSTORE']._serialized_end = 1232
    _globals['_RETRIEVECONTEXTSREQUEST_VERTEXRAGSTORE_RAGRESOURCE']._serialized_start = 1097
    _globals['_RETRIEVECONTEXTSREQUEST_VERTEXRAGSTORE_RAGRESOURCE']._serialized_end = 1202
    _globals['_RAGCONTEXTS']._serialized_start = 1250
    _globals['_RAGCONTEXTS']._serialized_end = 1549
    _globals['_RAGCONTEXTS_CONTEXT']._serialized_start = 1338
    _globals['_RAGCONTEXTS_CONTEXT']._serialized_end = 1549
    _globals['_RETRIEVECONTEXTSRESPONSE']._serialized_start = 1551
    _globals['_RETRIEVECONTEXTSRESPONSE']._serialized_end = 1641
    _globals['_AUGMENTPROMPTREQUEST']._serialized_start = 1644
    _globals['_AUGMENTPROMPTREQUEST']._serialized_end = 2025
    _globals['_AUGMENTPROMPTREQUEST_MODEL']._serialized_start = 1955
    _globals['_AUGMENTPROMPTREQUEST_MODEL']._serialized_end = 2010
    _globals['_AUGMENTPROMPTRESPONSE']._serialized_start = 2028
    _globals['_AUGMENTPROMPTRESPONSE']._serialized_end = 2173
    _globals['_CORROBORATECONTENTREQUEST']._serialized_start = 2176
    _globals['_CORROBORATECONTENTREQUEST']._serialized_end = 2545
    _globals['_CORROBORATECONTENTREQUEST_PARAMETERS']._serialized_start = 2488
    _globals['_CORROBORATECONTENTREQUEST_PARAMETERS']._serialized_end = 2533
    _globals['_CORROBORATECONTENTRESPONSE']._serialized_start = 2548
    _globals['_CORROBORATECONTENTRESPONSE']._serialized_end = 2690
    _globals['_FACT']._serialized_start = 2693
    _globals['_FACT']._serialized_end = 2976
    _globals['_CLAIM']._serialized_start = 2979
    _globals['_CLAIM']._serialized_end = 3118
    _globals['_VERTEXRAGSERVICE']._serialized_start = 3121
    _globals['_VERTEXRAGSERVICE']._serialized_end = 3908