"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1alpha/answer.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/discoveryengine/v1alpha/answer.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xdf"\n\x06Answer\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12A\n\x05state\x18\x02 \x01(\x0e22.google.cloud.discoveryengine.v1alpha.Answer.State\x12\x13\n\x0banswer_text\x18\x03 \x01(\t\x12H\n\tcitations\x18\x04 \x03(\x0b25.google.cloud.discoveryengine.v1alpha.Answer.Citation\x12J\n\nreferences\x18\x05 \x03(\x0b26.google.cloud.discoveryengine.v1alpha.Answer.Reference\x12\x19\n\x11related_questions\x18\x06 \x03(\t\x12@\n\x05steps\x18\x07 \x03(\x0b21.google.cloud.discoveryengine.v1alpha.Answer.Step\x12e\n\x18query_understanding_info\x18\n \x01(\x0b2C.google.cloud.discoveryengine.v1alpha.Answer.QueryUnderstandingInfo\x12`\n\x16answer_skipped_reasons\x18\x0b \x03(\x0e2@.google.cloud.discoveryengine.v1alpha.Answer.AnswerSkippedReason\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x126\n\rcomplete_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a\x80\x01\n\x08Citation\x12\x13\n\x0bstart_index\x18\x01 \x01(\x03\x12\x11\n\tend_index\x18\x02 \x01(\x03\x12L\n\x07sources\x18\x03 \x03(\x0b2;.google.cloud.discoveryengine.v1alpha.Answer.CitationSource\x1a&\n\x0eCitationSource\x12\x14\n\x0creference_id\x18\x01 \x01(\t\x1a\x9b\n\n\tReference\x12u\n\x1aunstructured_document_info\x18\x01 \x01(\x0b2O.google.cloud.discoveryengine.v1alpha.Answer.Reference.UnstructuredDocumentInfoH\x00\x12V\n\nchunk_info\x18\x02 \x01(\x0b2@.google.cloud.discoveryengine.v1alpha.Answer.Reference.ChunkInfoH\x00\x12q\n\x18structured_document_info\x18\x03 \x01(\x0b2M.google.cloud.discoveryengine.v1alpha.Answer.Reference.StructuredDocumentInfoH\x00\x1a\x86\x03\n\x18UnstructuredDocumentInfo\x12>\n\x08document\x18\x01 \x01(\tB,\xfaA)\n\'discoveryengine.googleapis.com/Document\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12t\n\x0echunk_contents\x18\x04 \x03(\x0b2\\.google.cloud.discoveryengine.v1alpha.Answer.Reference.UnstructuredDocumentInfo.ChunkContent\x12,\n\x0bstruct_data\x18\x05 \x01(\x0b2\x17.google.protobuf.Struct\x1aj\n\x0cChunkContent\x12\x0f\n\x07content\x18\x01 \x01(\t\x12\x17\n\x0fpage_identifier\x18\x02 \x01(\t\x12\x1c\n\x0frelevance_score\x18\x03 \x01(\x02H\x00\x88\x01\x01B\x12\n\x10_relevance_score\x1a\xae\x03\n\tChunkInfo\x128\n\x05chunk\x18\x01 \x01(\tB)\xfaA&\n$discoveryengine.googleapis.com/Chunk\x12\x0f\n\x07content\x18\x02 \x01(\t\x12\x1c\n\x0frelevance_score\x18\x03 \x01(\x02H\x00\x88\x01\x01\x12l\n\x11document_metadata\x18\x04 \x01(\x0b2Q.google.cloud.discoveryengine.v1alpha.Answer.Reference.ChunkInfo.DocumentMetadata\x1a\xb5\x01\n\x10DocumentMetadata\x12>\n\x08document\x18\x01 \x01(\tB,\xfaA)\n\'discoveryengine.googleapis.com/Document\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x17\n\x0fpage_identifier\x18\x04 \x01(\t\x12,\n\x0bstruct_data\x18\x05 \x01(\x0b2\x17.google.protobuf.StructB\x12\n\x10_relevance_score\x1a\x86\x01\n\x16StructuredDocumentInfo\x12>\n\x08document\x18\x01 \x01(\tB,\xfaA)\n\'discoveryengine.googleapis.com/Document\x12,\n\x0bstruct_data\x18\x02 \x01(\x0b2\x17.google.protobuf.StructB\t\n\x07content\x1a\xdf\x08\n\x04Step\x12F\n\x05state\x18\x01 \x01(\x0e27.google.cloud.discoveryengine.v1alpha.Answer.Step.State\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x0f\n\x07thought\x18\x03 \x01(\t\x12I\n\x07actions\x18\x04 \x03(\x0b28.google.cloud.discoveryengine.v1alpha.Answer.Step.Action\x1a\xd1\x06\n\x06Action\x12^\n\rsearch_action\x18\x02 \x01(\x0b2E.google.cloud.discoveryengine.v1alpha.Answer.Step.Action.SearchActionH\x00\x12Y\n\x0bobservation\x18\x03 \x01(\x0b2D.google.cloud.discoveryengine.v1alpha.Answer.Step.Action.Observation\x1a\x1d\n\x0cSearchAction\x12\r\n\x05query\x18\x01 \x01(\t\x1a\xe2\x04\n\x0bObservation\x12i\n\x0esearch_results\x18\x02 \x03(\x0b2Q.google.cloud.discoveryengine.v1alpha.Answer.Step.Action.Observation.SearchResult\x1a\xe7\x03\n\x0cSearchResult\x12\x10\n\x08document\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12s\n\x0csnippet_info\x18\x04 \x03(\x0b2].google.cloud.discoveryengine.v1alpha.Answer.Step.Action.Observation.SearchResult.SnippetInfo\x12o\n\nchunk_info\x18\x05 \x03(\x0b2[.google.cloud.discoveryengine.v1alpha.Answer.Step.Action.Observation.SearchResult.ChunkInfo\x12,\n\x0bstruct_data\x18\x06 \x01(\x0b2\x17.google.protobuf.Struct\x1a6\n\x0bSnippetInfo\x12\x0f\n\x07snippet\x18\x01 \x01(\t\x12\x16\n\x0esnippet_status\x18\x02 \x01(\t\x1a]\n\tChunkInfo\x12\r\n\x05chunk\x18\x01 \x01(\t\x12\x0f\n\x07content\x18\x02 \x01(\t\x12\x1c\n\x0frelevance_score\x18\x03 \x01(\x02H\x00\x88\x01\x01B\x12\n\x10_relevance_scoreB\x08\n\x06action"J\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\n\n\x06FAILED\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x1a\xa2\x03\n\x16QueryUnderstandingInfo\x12~\n\x19query_classification_info\x18\x01 \x03(\x0b2[.google.cloud.discoveryengine.v1alpha.Answer.QueryUnderstandingInfo.QueryClassificationInfo\x1a\x87\x02\n\x17QueryClassificationInfo\x12n\n\x04type\x18\x01 \x01(\x0e2`.google.cloud.discoveryengine.v1alpha.Answer.QueryUnderstandingInfo.QueryClassificationInfo.Type\x12\x10\n\x08positive\x18\x02 \x01(\x08"j\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11ADVERSARIAL_QUERY\x10\x01\x12\x1c\n\x18NON_ANSWER_SEEKING_QUERY\x10\x02\x12\x17\n\x13JAIL_BREAKING_QUERY\x10\x03"J\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\n\n\x06FAILED\x10\x02\x12\r\n\tSUCCEEDED\x10\x03"\x9b\x02\n\x13AnswerSkippedReason\x12%\n!ANSWER_SKIPPED_REASON_UNSPECIFIED\x10\x00\x12\x1d\n\x19ADVERSARIAL_QUERY_IGNORED\x10\x01\x12$\n NON_ANSWER_SEEKING_QUERY_IGNORED\x10\x02\x12\x1f\n\x1bOUT_OF_DOMAIN_QUERY_IGNORED\x10\x03\x12\x1e\n\x1aPOTENTIAL_POLICY_VIOLATION\x10\x04\x12\x17\n\x13NO_RELEVANT_CONTENT\x10\x05\x12\x1f\n\x1bJAIL_BREAKING_QUERY_IGNORED\x10\x06\x12\x1d\n\x19CUSTOMER_POLICY_VIOLATION\x10\x07:\x85\x03\xeaA\x81\x03\n%discoveryengine.googleapis.com/Answer\x12cprojects/{project}/locations/{location}/dataStores/{data_store}/sessions/{session}/answers/{answer}\x12|projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/sessions/{session}/answers/{answer}\x12uprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}/answers/{answer}B\x97\x02\n(com.google.cloud.discoveryengine.v1alphaB\x0bAnswerProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.answer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x0bAnswerProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
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
    _globals['_ANSWER']._serialized_start = 215
    _globals['_ANSWER']._serialized_end = 4662
    _globals['_ANSWER_CITATION']._serialized_start = 887
    _globals['_ANSWER_CITATION']._serialized_end = 1015
    _globals['_ANSWER_CITATIONSOURCE']._serialized_start = 1017
    _globals['_ANSWER_CITATIONSOURCE']._serialized_end = 1055
    _globals['_ANSWER_REFERENCE']._serialized_start = 1058
    _globals['_ANSWER_REFERENCE']._serialized_end = 2365
    _globals['_ANSWER_REFERENCE_UNSTRUCTUREDDOCUMENTINFO']._serialized_start = 1394
    _globals['_ANSWER_REFERENCE_UNSTRUCTUREDDOCUMENTINFO']._serialized_end = 1784
    _globals['_ANSWER_REFERENCE_UNSTRUCTUREDDOCUMENTINFO_CHUNKCONTENT']._serialized_start = 1678
    _globals['_ANSWER_REFERENCE_UNSTRUCTUREDDOCUMENTINFO_CHUNKCONTENT']._serialized_end = 1784
    _globals['_ANSWER_REFERENCE_CHUNKINFO']._serialized_start = 1787
    _globals['_ANSWER_REFERENCE_CHUNKINFO']._serialized_end = 2217
    _globals['_ANSWER_REFERENCE_CHUNKINFO_DOCUMENTMETADATA']._serialized_start = 2016
    _globals['_ANSWER_REFERENCE_CHUNKINFO_DOCUMENTMETADATA']._serialized_end = 2197
    _globals['_ANSWER_REFERENCE_STRUCTUREDDOCUMENTINFO']._serialized_start = 2220
    _globals['_ANSWER_REFERENCE_STRUCTUREDDOCUMENTINFO']._serialized_end = 2354
    _globals['_ANSWER_STEP']._serialized_start = 2368
    _globals['_ANSWER_STEP']._serialized_end = 3487
    _globals['_ANSWER_STEP_ACTION']._serialized_start = 2562
    _globals['_ANSWER_STEP_ACTION']._serialized_end = 3411
    _globals['_ANSWER_STEP_ACTION_SEARCHACTION']._serialized_start = 2759
    _globals['_ANSWER_STEP_ACTION_SEARCHACTION']._serialized_end = 2788
    _globals['_ANSWER_STEP_ACTION_OBSERVATION']._serialized_start = 2791
    _globals['_ANSWER_STEP_ACTION_OBSERVATION']._serialized_end = 3401
    _globals['_ANSWER_STEP_ACTION_OBSERVATION_SEARCHRESULT']._serialized_start = 2914
    _globals['_ANSWER_STEP_ACTION_OBSERVATION_SEARCHRESULT']._serialized_end = 3401
    _globals['_ANSWER_STEP_ACTION_OBSERVATION_SEARCHRESULT_SNIPPETINFO']._serialized_start = 3252
    _globals['_ANSWER_STEP_ACTION_OBSERVATION_SEARCHRESULT_SNIPPETINFO']._serialized_end = 3306
    _globals['_ANSWER_STEP_ACTION_OBSERVATION_SEARCHRESULT_CHUNKINFO']._serialized_start = 3308
    _globals['_ANSWER_STEP_ACTION_OBSERVATION_SEARCHRESULT_CHUNKINFO']._serialized_end = 3401
    _globals['_ANSWER_STEP_STATE']._serialized_start = 3413
    _globals['_ANSWER_STEP_STATE']._serialized_end = 3487
    _globals['_ANSWER_QUERYUNDERSTANDINGINFO']._serialized_start = 3490
    _globals['_ANSWER_QUERYUNDERSTANDINGINFO']._serialized_end = 3908
    _globals['_ANSWER_QUERYUNDERSTANDINGINFO_QUERYCLASSIFICATIONINFO']._serialized_start = 3645
    _globals['_ANSWER_QUERYUNDERSTANDINGINFO_QUERYCLASSIFICATIONINFO']._serialized_end = 3908
    _globals['_ANSWER_QUERYUNDERSTANDINGINFO_QUERYCLASSIFICATIONINFO_TYPE']._serialized_start = 3802
    _globals['_ANSWER_QUERYUNDERSTANDINGINFO_QUERYCLASSIFICATIONINFO_TYPE']._serialized_end = 3908
    _globals['_ANSWER_STATE']._serialized_start = 3413
    _globals['_ANSWER_STATE']._serialized_end = 3487
    _globals['_ANSWER_ANSWERSKIPPEDREASON']._serialized_start = 3987
    _globals['_ANSWER_ANSWERSKIPPEDREASON']._serialized_end = 4270