"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/assist_answer.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/discoveryengine/v1/assist_answer.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x8d\x06\n\x0cAssistAnswer\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12B\n\x05state\x18\x02 \x01(\x0e23.google.cloud.discoveryengine.v1.AssistAnswer.State\x12D\n\x07replies\x18\x03 \x03(\x0b23.google.cloud.discoveryengine.v1.AssistAnswer.Reply\x12a\n\x16assist_skipped_reasons\x18\x05 \x03(\x0e2A.google.cloud.discoveryengine.v1.AssistAnswer.AssistSkippedReason\x1ag\n\x05Reply\x12U\n\x10grounded_content\x18\x01 \x01(\x0b29.google.cloud.discoveryengine.v1.AssistantGroundedContentH\x00B\x07\n\x05reply"W\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\n\n\x06FAILED\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\x0b\n\x07SKIPPED\x10\x04"\x81\x01\n\x13AssistSkippedReason\x12%\n!ASSIST_SKIPPED_REASON_UNSPECIFIED\x10\x00\x12$\n NON_ASSIST_SEEKING_QUERY_IGNORED\x10\x01\x12\x1d\n\x19CUSTOMER_POLICY_VIOLATION\x10\x02:\xb6\x01\xeaA\xb2\x01\n+discoveryengine.googleapis.com/AssistAnswer\x12\x82\x01projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}/assistAnswers/{assist_answer}"\xb1\x06\n\x10AssistantContent\x12\x0e\n\x04text\x18\x02 \x01(\tH\x00\x12M\n\x0binline_data\x18\x03 \x01(\x0b26.google.cloud.discoveryengine.v1.AssistantContent.BlobH\x00\x12F\n\x04file\x18\x04 \x01(\x0b26.google.cloud.discoveryengine.v1.AssistantContent.FileH\x00\x12[\n\x0fexecutable_code\x18\x07 \x01(\x0b2@.google.cloud.discoveryengine.v1.AssistantContent.ExecutableCodeH\x00\x12f\n\x15code_execution_result\x18\x08 \x01(\x0b2E.google.cloud.discoveryengine.v1.AssistantContent.CodeExecutionResultH\x00\x12\x0c\n\x04role\x18\x01 \x01(\t\x12\x14\n\x07thought\x18\x06 \x01(\x08B\x03\xe0A\x01\x1a1\n\x04Blob\x12\x16\n\tmime_type\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04data\x18\x02 \x01(\x0cB\x03\xe0A\x02\x1a4\n\x04File\x12\x16\n\tmime_type\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07file_id\x18\x02 \x01(\tB\x03\xe0A\x02\x1a#\n\x0eExecutableCode\x12\x11\n\x04code\x18\x02 \x01(\tB\x03\xe0A\x02\x1a\xf6\x01\n\x13CodeExecutionResult\x12c\n\x07outcome\x18\x01 \x01(\x0e2M.google.cloud.discoveryengine.v1.AssistantContent.CodeExecutionResult.OutcomeB\x03\xe0A\x02\x12\x13\n\x06output\x18\x02 \x01(\tB\x03\xe0A\x01"e\n\x07Outcome\x12\x17\n\x13OUTCOME_UNSPECIFIED\x10\x00\x12\x0e\n\nOUTCOME_OK\x10\x01\x12\x12\n\x0eOUTCOME_FAILED\x10\x02\x12\x1d\n\x19OUTCOME_DEADLINE_EXCEEDED\x10\x03B\x06\n\x04data"\xdf\x07\n\x18AssistantGroundedContent\x12r\n\x17text_grounding_metadata\x18\x03 \x01(\x0b2O.google.cloud.discoveryengine.v1.AssistantGroundedContent.TextGroundingMetadataH\x00\x12B\n\x07content\x18\x01 \x01(\x0b21.google.cloud.discoveryengine.v1.AssistantContent\x1a\xfe\x05\n\x15TextGroundingMetadata\x12i\n\x08segments\x18\x04 \x03(\x0b2W.google.cloud.discoveryengine.v1.AssistantGroundedContent.TextGroundingMetadata.Segment\x12m\n\nreferences\x18\x02 \x03(\x0b2Y.google.cloud.discoveryengine.v1.AssistantGroundedContent.TextGroundingMetadata.Reference\x1as\n\x07Segment\x12\x13\n\x0bstart_index\x18\x01 \x01(\x03\x12\x11\n\tend_index\x18\x02 \x01(\x03\x12\x19\n\x11reference_indices\x18\x04 \x03(\x05\x12\x17\n\x0fgrounding_score\x18\x05 \x01(\x02\x12\x0c\n\x04text\x18\x06 \x01(\t\x1a\x95\x03\n\tReference\x12\x0f\n\x07content\x18\x01 \x01(\t\x12\x85\x01\n\x11document_metadata\x18\x02 \x01(\x0b2j.google.cloud.discoveryengine.v1.AssistantGroundedContent.TextGroundingMetadata.Reference.DocumentMetadata\x1a\xee\x01\n\x10DocumentMetadata\x12C\n\x08document\x18\x01 \x01(\tB,\xfaA)\n\'discoveryengine.googleapis.com/DocumentH\x00\x88\x01\x01\x12\x10\n\x03uri\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x12\n\x05title\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x1c\n\x0fpage_identifier\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x13\n\x06domain\x18\x05 \x01(\tH\x04\x88\x01\x01B\x0b\n\t_documentB\x06\n\x04_uriB\x08\n\x06_titleB\x12\n\x10_page_identifierB\t\n\x07_domainB\n\n\x08metadataB\x84\x02\n#com.google.cloud.discoveryengine.v1B\x11AssistAnswerProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.assist_answer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x11AssistAnswerProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_ASSISTANSWER'].fields_by_name['name']._loaded_options = None
    _globals['_ASSISTANSWER'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_ASSISTANSWER']._loaded_options = None
    _globals['_ASSISTANSWER']._serialized_options = b'\xeaA\xb2\x01\n+discoveryengine.googleapis.com/AssistAnswer\x12\x82\x01projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}/assistAnswers/{assist_answer}'
    _globals['_ASSISTANTCONTENT_BLOB'].fields_by_name['mime_type']._loaded_options = None
    _globals['_ASSISTANTCONTENT_BLOB'].fields_by_name['mime_type']._serialized_options = b'\xe0A\x02'
    _globals['_ASSISTANTCONTENT_BLOB'].fields_by_name['data']._loaded_options = None
    _globals['_ASSISTANTCONTENT_BLOB'].fields_by_name['data']._serialized_options = b'\xe0A\x02'
    _globals['_ASSISTANTCONTENT_FILE'].fields_by_name['mime_type']._loaded_options = None
    _globals['_ASSISTANTCONTENT_FILE'].fields_by_name['mime_type']._serialized_options = b'\xe0A\x02'
    _globals['_ASSISTANTCONTENT_FILE'].fields_by_name['file_id']._loaded_options = None
    _globals['_ASSISTANTCONTENT_FILE'].fields_by_name['file_id']._serialized_options = b'\xe0A\x02'
    _globals['_ASSISTANTCONTENT_EXECUTABLECODE'].fields_by_name['code']._loaded_options = None
    _globals['_ASSISTANTCONTENT_EXECUTABLECODE'].fields_by_name['code']._serialized_options = b'\xe0A\x02'
    _globals['_ASSISTANTCONTENT_CODEEXECUTIONRESULT'].fields_by_name['outcome']._loaded_options = None
    _globals['_ASSISTANTCONTENT_CODEEXECUTIONRESULT'].fields_by_name['outcome']._serialized_options = b'\xe0A\x02'
    _globals['_ASSISTANTCONTENT_CODEEXECUTIONRESULT'].fields_by_name['output']._loaded_options = None
    _globals['_ASSISTANTCONTENT_CODEEXECUTIONRESULT'].fields_by_name['output']._serialized_options = b'\xe0A\x01'
    _globals['_ASSISTANTCONTENT'].fields_by_name['thought']._loaded_options = None
    _globals['_ASSISTANTCONTENT'].fields_by_name['thought']._serialized_options = b'\xe0A\x01'
    _globals['_ASSISTANTGROUNDEDCONTENT_TEXTGROUNDINGMETADATA_REFERENCE_DOCUMENTMETADATA'].fields_by_name['document']._loaded_options = None
    _globals['_ASSISTANTGROUNDEDCONTENT_TEXTGROUNDINGMETADATA_REFERENCE_DOCUMENTMETADATA'].fields_by_name['document']._serialized_options = b"\xfaA)\n'discoveryengine.googleapis.com/Document"
    _globals['_ASSISTANSWER']._serialized_start = 149
    _globals['_ASSISTANSWER']._serialized_end = 930
    _globals['_ASSISTANSWER_REPLY']._serialized_start = 421
    _globals['_ASSISTANSWER_REPLY']._serialized_end = 524
    _globals['_ASSISTANSWER_STATE']._serialized_start = 526
    _globals['_ASSISTANSWER_STATE']._serialized_end = 613
    _globals['_ASSISTANSWER_ASSISTSKIPPEDREASON']._serialized_start = 616
    _globals['_ASSISTANSWER_ASSISTSKIPPEDREASON']._serialized_end = 745
    _globals['_ASSISTANTCONTENT']._serialized_start = 933
    _globals['_ASSISTANTCONTENT']._serialized_end = 1750
    _globals['_ASSISTANTCONTENT_BLOB']._serialized_start = 1353
    _globals['_ASSISTANTCONTENT_BLOB']._serialized_end = 1402
    _globals['_ASSISTANTCONTENT_FILE']._serialized_start = 1404
    _globals['_ASSISTANTCONTENT_FILE']._serialized_end = 1456
    _globals['_ASSISTANTCONTENT_EXECUTABLECODE']._serialized_start = 1458
    _globals['_ASSISTANTCONTENT_EXECUTABLECODE']._serialized_end = 1493
    _globals['_ASSISTANTCONTENT_CODEEXECUTIONRESULT']._serialized_start = 1496
    _globals['_ASSISTANTCONTENT_CODEEXECUTIONRESULT']._serialized_end = 1742
    _globals['_ASSISTANTCONTENT_CODEEXECUTIONRESULT_OUTCOME']._serialized_start = 1641
    _globals['_ASSISTANTCONTENT_CODEEXECUTIONRESULT_OUTCOME']._serialized_end = 1742
    _globals['_ASSISTANTGROUNDEDCONTENT']._serialized_start = 1753
    _globals['_ASSISTANTGROUNDEDCONTENT']._serialized_end = 2744
    _globals['_ASSISTANTGROUNDEDCONTENT_TEXTGROUNDINGMETADATA']._serialized_start = 1966
    _globals['_ASSISTANTGROUNDEDCONTENT_TEXTGROUNDINGMETADATA']._serialized_end = 2732
    _globals['_ASSISTANTGROUNDEDCONTENT_TEXTGROUNDINGMETADATA_SEGMENT']._serialized_start = 2209
    _globals['_ASSISTANTGROUNDEDCONTENT_TEXTGROUNDINGMETADATA_SEGMENT']._serialized_end = 2324
    _globals['_ASSISTANTGROUNDEDCONTENT_TEXTGROUNDINGMETADATA_REFERENCE']._serialized_start = 2327
    _globals['_ASSISTANTGROUNDEDCONTENT_TEXTGROUNDINGMETADATA_REFERENCE']._serialized_end = 2732
    _globals['_ASSISTANTGROUNDEDCONTENT_TEXTGROUNDINGMETADATA_REFERENCE_DOCUMENTMETADATA']._serialized_start = 2494
    _globals['_ASSISTANTGROUNDEDCONTENT_TEXTGROUNDINGMETADATA_REFERENCE_DOCUMENTMETADATA']._serialized_end = 2732