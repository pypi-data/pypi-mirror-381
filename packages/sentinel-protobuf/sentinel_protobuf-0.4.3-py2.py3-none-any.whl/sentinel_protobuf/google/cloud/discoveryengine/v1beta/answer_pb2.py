"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1beta/answer.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/discoveryengine/v1beta/answer.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xad#\n\x06Answer\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12@\n\x05state\x18\x02 \x01(\x0e21.google.cloud.discoveryengine.v1beta.Answer.State\x12\x13\n\x0banswer_text\x18\x03 \x01(\t\x12G\n\tcitations\x18\x04 \x03(\x0b24.google.cloud.discoveryengine.v1beta.Answer.Citation\x12I\n\nreferences\x18\x05 \x03(\x0b25.google.cloud.discoveryengine.v1beta.Answer.Reference\x12\x19\n\x11related_questions\x18\x06 \x03(\t\x12?\n\x05steps\x18\x07 \x03(\x0b20.google.cloud.discoveryengine.v1beta.Answer.Step\x12d\n\x18query_understanding_info\x18\n \x01(\x0b2B.google.cloud.discoveryengine.v1beta.Answer.QueryUnderstandingInfo\x12_\n\x16answer_skipped_reasons\x18\x0b \x03(\x0e2?.google.cloud.discoveryengine.v1beta.Answer.AnswerSkippedReason\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x126\n\rcomplete_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a\x7f\n\x08Citation\x12\x13\n\x0bstart_index\x18\x01 \x01(\x03\x12\x11\n\tend_index\x18\x02 \x01(\x03\x12K\n\x07sources\x18\x03 \x03(\x0b2:.google.cloud.discoveryengine.v1beta.Answer.CitationSource\x1a&\n\x0eCitationSource\x12\x14\n\x0creference_id\x18\x01 \x01(\t\x1a\x96\n\n\tReference\x12t\n\x1aunstructured_document_info\x18\x01 \x01(\x0b2N.google.cloud.discoveryengine.v1beta.Answer.Reference.UnstructuredDocumentInfoH\x00\x12U\n\nchunk_info\x18\x02 \x01(\x0b2?.google.cloud.discoveryengine.v1beta.Answer.Reference.ChunkInfoH\x00\x12p\n\x18structured_document_info\x18\x03 \x01(\x0b2L.google.cloud.discoveryengine.v1beta.Answer.Reference.StructuredDocumentInfoH\x00\x1a\x85\x03\n\x18UnstructuredDocumentInfo\x12>\n\x08document\x18\x01 \x01(\tB,\xfaA)\n\'discoveryengine.googleapis.com/Document\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12s\n\x0echunk_contents\x18\x04 \x03(\x0b2[.google.cloud.discoveryengine.v1beta.Answer.Reference.UnstructuredDocumentInfo.ChunkContent\x12,\n\x0bstruct_data\x18\x05 \x01(\x0b2\x17.google.protobuf.Struct\x1aj\n\x0cChunkContent\x12\x0f\n\x07content\x18\x01 \x01(\t\x12\x17\n\x0fpage_identifier\x18\x02 \x01(\t\x12\x1c\n\x0frelevance_score\x18\x03 \x01(\x02H\x00\x88\x01\x01B\x12\n\x10_relevance_score\x1a\xad\x03\n\tChunkInfo\x128\n\x05chunk\x18\x01 \x01(\tB)\xfaA&\n$discoveryengine.googleapis.com/Chunk\x12\x0f\n\x07content\x18\x02 \x01(\t\x12\x1c\n\x0frelevance_score\x18\x03 \x01(\x02H\x00\x88\x01\x01\x12k\n\x11document_metadata\x18\x04 \x01(\x0b2P.google.cloud.discoveryengine.v1beta.Answer.Reference.ChunkInfo.DocumentMetadata\x1a\xb5\x01\n\x10DocumentMetadata\x12>\n\x08document\x18\x01 \x01(\tB,\xfaA)\n\'discoveryengine.googleapis.com/Document\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x17\n\x0fpage_identifier\x18\x04 \x01(\t\x12,\n\x0bstruct_data\x18\x05 \x01(\x0b2\x17.google.protobuf.StructB\x12\n\x10_relevance_score\x1a\x86\x01\n\x16StructuredDocumentInfo\x12>\n\x08document\x18\x01 \x01(\tB,\xfaA)\n\'discoveryengine.googleapis.com/Document\x12,\n\x0bstruct_data\x18\x02 \x01(\x0b2\x17.google.protobuf.StructB\t\n\x07content\x1a\xd8\x08\n\x04Step\x12E\n\x05state\x18\x01 \x01(\x0e26.google.cloud.discoveryengine.v1beta.Answer.Step.State\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x0f\n\x07thought\x18\x03 \x01(\t\x12H\n\x07actions\x18\x04 \x03(\x0b27.google.cloud.discoveryengine.v1beta.Answer.Step.Action\x1a\xcc\x06\n\x06Action\x12]\n\rsearch_action\x18\x02 \x01(\x0b2D.google.cloud.discoveryengine.v1beta.Answer.Step.Action.SearchActionH\x00\x12X\n\x0bobservation\x18\x03 \x01(\x0b2C.google.cloud.discoveryengine.v1beta.Answer.Step.Action.Observation\x1a\x1d\n\x0cSearchAction\x12\r\n\x05query\x18\x01 \x01(\t\x1a\xdf\x04\n\x0bObservation\x12h\n\x0esearch_results\x18\x02 \x03(\x0b2P.google.cloud.discoveryengine.v1beta.Answer.Step.Action.Observation.SearchResult\x1a\xe5\x03\n\x0cSearchResult\x12\x10\n\x08document\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12r\n\x0csnippet_info\x18\x04 \x03(\x0b2\\.google.cloud.discoveryengine.v1beta.Answer.Step.Action.Observation.SearchResult.SnippetInfo\x12n\n\nchunk_info\x18\x05 \x03(\x0b2Z.google.cloud.discoveryengine.v1beta.Answer.Step.Action.Observation.SearchResult.ChunkInfo\x12,\n\x0bstruct_data\x18\x06 \x01(\x0b2\x17.google.protobuf.Struct\x1a6\n\x0bSnippetInfo\x12\x0f\n\x07snippet\x18\x01 \x01(\t\x12\x16\n\x0esnippet_status\x18\x02 \x01(\t\x1a]\n\tChunkInfo\x12\r\n\x05chunk\x18\x01 \x01(\t\x12\x0f\n\x07content\x18\x02 \x01(\t\x12\x1c\n\x0frelevance_score\x18\x03 \x01(\x02H\x00\x88\x01\x01B\x12\n\x10_relevance_scoreB\x08\n\x06action"J\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\n\n\x06FAILED\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x1a\xc2\x03\n\x16QueryUnderstandingInfo\x12}\n\x19query_classification_info\x18\x01 \x03(\x0b2Z.google.cloud.discoveryengine.v1beta.Answer.QueryUnderstandingInfo.QueryClassificationInfo\x1a\xa8\x02\n\x17QueryClassificationInfo\x12m\n\x04type\x18\x01 \x01(\x0e2_.google.cloud.discoveryengine.v1beta.Answer.QueryUnderstandingInfo.QueryClassificationInfo.Type\x12\x10\n\x08positive\x18\x02 \x01(\x08"\x8b\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11ADVERSARIAL_QUERY\x10\x01\x12\x1c\n\x18NON_ANSWER_SEEKING_QUERY\x10\x02\x12\x17\n\x13JAIL_BREAKING_QUERY\x10\x03\x12\x1f\n\x1bNON_ANSWER_SEEKING_QUERY_V2\x10\x04"J\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\n\n\x06FAILED\x10\x02\x12\r\n\tSUCCEEDED\x10\x03"\xdd\x02\n\x13AnswerSkippedReason\x12%\n!ANSWER_SKIPPED_REASON_UNSPECIFIED\x10\x00\x12\x1d\n\x19ADVERSARIAL_QUERY_IGNORED\x10\x01\x12$\n NON_ANSWER_SEEKING_QUERY_IGNORED\x10\x02\x12\x1f\n\x1bOUT_OF_DOMAIN_QUERY_IGNORED\x10\x03\x12\x1e\n\x1aPOTENTIAL_POLICY_VIOLATION\x10\x04\x12\x17\n\x13NO_RELEVANT_CONTENT\x10\x05\x12\x1f\n\x1bJAIL_BREAKING_QUERY_IGNORED\x10\x06\x12\x1d\n\x19CUSTOMER_POLICY_VIOLATION\x10\x07\x12\'\n#NON_ANSWER_SEEKING_QUERY_IGNORED_V2\x10\x08\x12\x17\n\x13LOW_GROUNDED_ANSWER\x10\t:\x85\x03\xeaA\x81\x03\n%discoveryengine.googleapis.com/Answer\x12cprojects/{project}/locations/{location}/dataStores/{data_store}/sessions/{session}/answers/{answer}\x12|projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/sessions/{session}/answers/{answer}\x12uprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}/answers/{answer}B\x92\x02\n\'com.google.cloud.discoveryengine.v1betaB\x0bAnswerProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.answer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x0bAnswerProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
    _globals['_ANSWER_REFERENCE_UNSTRUCTUREDDOCUMENTINFO'].fields_by_name['document']._loaded_options = None
    _globals['_ANSWER_REFERENCE_UNSTRUCTUREDDOCUMENTINFO'].fields_by_name['document']._serialized_options = b"\xfaA)\n'discoveryengine.googleapis.com/Document"
    _globals['_ANSWER_REFERENCE_CHUNKINFO_DOCUMENTMETADATA'].fields_by_name['document']._loaded_options = None
    _globals['_ANSWER_REFERENCE_CHUNKINFO_DOCUMENTMETADATA'].fields_by_name['document']._serialized_options = b"\xfaA)\n'discoveryengine.googleapis.com/Document"
    _globals['_ANSWER_REFERENCE_CHUNKINFO'].fields_by_name['chunk']._loaded_options = None
    _globals['_ANSWER_REFERENCE_CHUNKINFO'].fields_by_name['chunk']._serialized_options = b'\xfaA&\n$discoveryengine.googleapis.com/Chunk'
    _globals['_ANSWER_REFERENCE_STRUCTUREDDOCUMENTINFO'].fields_by_name['document']._loaded_options = None
    _globals['_ANSWER_REFERENCE_STRUCTUREDDOCUMENTINFO'].fields_by_name['document']._serialized_options = b"\xfaA)\n'discoveryengine.googleapis.com/Document"
    _globals['_ANSWER'].fields_by_name['name']._loaded_options = None
    _globals['_ANSWER'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_ANSWER'].fields_by_name['create_time']._loaded_options = None
    _globals['_ANSWER'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ANSWER'].fields_by_name['complete_time']._loaded_options = None
    _globals['_ANSWER'].fields_by_name['complete_time']._serialized_options = b'\xe0A\x03'
    _globals['_ANSWER']._loaded_options = None
    _globals['_ANSWER']._serialized_options = b'\xeaA\x81\x03\n%discoveryengine.googleapis.com/Answer\x12cprojects/{project}/locations/{location}/dataStores/{data_store}/sessions/{session}/answers/{answer}\x12|projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/sessions/{session}/answers/{answer}\x12uprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}/answers/{answer}'
    _globals['_ANSWER']._serialized_start = 213
    _globals['_ANSWER']._serialized_end = 4738
    _globals['_ANSWER_CITATION']._serialized_start = 878
    _globals['_ANSWER_CITATION']._serialized_end = 1005
    _globals['_ANSWER_CITATIONSOURCE']._serialized_start = 1007
    _globals['_ANSWER_CITATIONSOURCE']._serialized_end = 1045
    _globals['_ANSWER_REFERENCE']._serialized_start = 1048
    _globals['_ANSWER_REFERENCE']._serialized_end = 2350
    _globals['_ANSWER_REFERENCE_UNSTRUCTUREDDOCUMENTINFO']._serialized_start = 1381
    _globals['_ANSWER_REFERENCE_UNSTRUCTUREDDOCUMENTINFO']._serialized_end = 1770
    _globals['_ANSWER_REFERENCE_UNSTRUCTUREDDOCUMENTINFO_CHUNKCONTENT']._serialized_start = 1664
    _globals['_ANSWER_REFERENCE_UNSTRUCTUREDDOCUMENTINFO_CHUNKCONTENT']._serialized_end = 1770
    _globals['_ANSWER_REFERENCE_CHUNKINFO']._serialized_start = 1773
    _globals['_ANSWER_REFERENCE_CHUNKINFO']._serialized_end = 2202
    _globals['_ANSWER_REFERENCE_CHUNKINFO_DOCUMENTMETADATA']._serialized_start = 2001
    _globals['_ANSWER_REFERENCE_CHUNKINFO_DOCUMENTMETADATA']._serialized_end = 2182
    _globals['_ANSWER_REFERENCE_STRUCTUREDDOCUMENTINFO']._serialized_start = 2205
    _globals['_ANSWER_REFERENCE_STRUCTUREDDOCUMENTINFO']._serialized_end = 2339
    _globals['_ANSWER_STEP']._serialized_start = 2353
    _globals['_ANSWER_STEP']._serialized_end = 3465
    _globals['_ANSWER_STEP_ACTION']._serialized_start = 2545
    _globals['_ANSWER_STEP_ACTION']._serialized_end = 3389
    _globals['_ANSWER_STEP_ACTION_SEARCHACTION']._serialized_start = 2740
    _globals['_ANSWER_STEP_ACTION_SEARCHACTION']._serialized_end = 2769
    _globals['_ANSWER_STEP_ACTION_OBSERVATION']._serialized_start = 2772
    _globals['_ANSWER_STEP_ACTION_OBSERVATION']._serialized_end = 3379
    _globals['_ANSWER_STEP_ACTION_OBSERVATION_SEARCHRESULT']._serialized_start = 2894
    _globals['_ANSWER_STEP_ACTION_OBSERVATION_SEARCHRESULT']._serialized_end = 3379
    _globals['_ANSWER_STEP_ACTION_OBSERVATION_SEARCHRESULT_SNIPPETINFO']._serialized_start = 3230
    _globals['_ANSWER_STEP_ACTION_OBSERVATION_SEARCHRESULT_SNIPPETINFO']._serialized_end = 3284
    _globals['_ANSWER_STEP_ACTION_OBSERVATION_SEARCHRESULT_CHUNKINFO']._serialized_start = 3286
    _globals['_ANSWER_STEP_ACTION_OBSERVATION_SEARCHRESULT_CHUNKINFO']._serialized_end = 3379
    _globals['_ANSWER_STEP_STATE']._serialized_start = 3391
    _globals['_ANSWER_STEP_STATE']._serialized_end = 3465
    _globals['_ANSWER_QUERYUNDERSTANDINGINFO']._serialized_start = 3468
    _globals['_ANSWER_QUERYUNDERSTANDINGINFO']._serialized_end = 3918
    _globals['_ANSWER_QUERYUNDERSTANDINGINFO_QUERYCLASSIFICATIONINFO']._serialized_start = 3622
    _globals['_ANSWER_QUERYUNDERSTANDINGINFO_QUERYCLASSIFICATIONINFO']._serialized_end = 3918
    _globals['_ANSWER_QUERYUNDERSTANDINGINFO_QUERYCLASSIFICATIONINFO_TYPE']._serialized_start = 3779
    _globals['_ANSWER_QUERYUNDERSTANDINGINFO_QUERYCLASSIFICATIONINFO_TYPE']._serialized_end = 3918
    _globals['_ANSWER_STATE']._serialized_start = 3391
    _globals['_ANSWER_STATE']._serialized_end = 3465
    _globals['_ANSWER_ANSWERSKIPPEDREASON']._serialized_start = 3997
    _globals['_ANSWER_ANSWERSKIPPEDREASON']._serialized_end = 4346