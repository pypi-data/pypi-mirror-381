"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ai/generativelanguage/v1beta2/text_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ai.generativelanguage.v1beta2 import citation_pb2 as google_dot_ai_dot_generativelanguage_dot_v1beta2_dot_citation__pb2
from .....google.ai.generativelanguage.v1beta2 import safety_pb2 as google_dot_ai_dot_generativelanguage_dot_v1beta2_dot_safety__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/ai/generativelanguage/v1beta2/text_service.proto\x12$google.ai.generativelanguage.v1beta2\x1a3google/ai/generativelanguage/v1beta2/citation.proto\x1a1google/ai/generativelanguage/v1beta2/safety.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xd0\x03\n\x13GenerateTextRequest\x12>\n\x05model\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'generativelanguage.googleapis.com/Model\x12E\n\x06prompt\x18\x02 \x01(\x0b20.google.ai.generativelanguage.v1beta2.TextPromptB\x03\xe0A\x02\x12\x18\n\x0btemperature\x18\x03 \x01(\x02H\x00\x88\x01\x01\x12\x1c\n\x0fcandidate_count\x18\x04 \x01(\x05H\x01\x88\x01\x01\x12\x1e\n\x11max_output_tokens\x18\x05 \x01(\x05H\x02\x88\x01\x01\x12\x12\n\x05top_p\x18\x06 \x01(\x02H\x03\x88\x01\x01\x12\x12\n\x05top_k\x18\x07 \x01(\x05H\x04\x88\x01\x01\x12L\n\x0fsafety_settings\x18\x08 \x03(\x0b23.google.ai.generativelanguage.v1beta2.SafetySetting\x12\x16\n\x0estop_sequences\x18\t \x03(\tB\x0e\n\x0c_temperatureB\x12\n\x10_candidate_countB\x14\n\x12_max_output_tokensB\x08\n\x06_top_pB\x08\n\x06_top_k"\xf5\x01\n\x14GenerateTextResponse\x12H\n\ncandidates\x18\x01 \x03(\x0b24.google.ai.generativelanguage.v1beta2.TextCompletion\x12D\n\x07filters\x18\x03 \x03(\x0b23.google.ai.generativelanguage.v1beta2.ContentFilter\x12M\n\x0fsafety_feedback\x18\x04 \x03(\x0b24.google.ai.generativelanguage.v1beta2.SafetyFeedback"\x1f\n\nTextPrompt\x12\x11\n\x04text\x18\x01 \x01(\tB\x03\xe0A\x02"\xe4\x01\n\x0eTextCompletion\x12\x13\n\x06output\x18\x01 \x01(\tB\x03\xe0A\x03\x12J\n\x0esafety_ratings\x18\x02 \x03(\x0b22.google.ai.generativelanguage.v1beta2.SafetyRating\x12[\n\x11citation_metadata\x18\x03 \x01(\x0b26.google.ai.generativelanguage.v1beta2.CitationMetadataB\x03\xe0A\x03H\x00\x88\x01\x01B\x14\n\x12_citation_metadata"e\n\x10EmbedTextRequest\x12>\n\x05model\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'generativelanguage.googleapis.com/Model\x12\x11\n\x04text\x18\x02 \x01(\tB\x03\xe0A\x02"o\n\x11EmbedTextResponse\x12L\n\tembedding\x18\x01 \x01(\x0b2/.google.ai.generativelanguage.v1beta2.EmbeddingB\x03\xe0A\x03H\x00\x88\x01\x01B\x0c\n\n_embedding"\x1a\n\tEmbedding\x12\r\n\x05value\x18\x01 \x03(\x022\xf3\x03\n\x0bTextService\x12\x81\x02\n\x0cGenerateText\x129.google.ai.generativelanguage.v1beta2.GenerateTextRequest\x1a:.google.ai.generativelanguage.v1beta2.GenerateTextResponse"z\xdaAFmodel,prompt,temperature,candidate_count,max_output_tokens,top_p,top_k\x82\xd3\xe4\x93\x02+"&/v1beta2/{model=models/*}:generateText:\x01*\x12\xb9\x01\n\tEmbedText\x126.google.ai.generativelanguage.v1beta2.EmbedTextRequest\x1a7.google.ai.generativelanguage.v1beta2.EmbedTextResponse";\xdaA\nmodel,text\x82\xd3\xe4\x93\x02("#/v1beta2/{model=models/*}:embedText:\x01*\x1a$\xcaA!generativelanguage.googleapis.comB\x9e\x01\n(com.google.ai.generativelanguage.v1beta2B\x10TextServiceProtoP\x01Z^cloud.google.com/go/ai/generativelanguage/apiv1beta2/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1beta2.text_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ai.generativelanguage.v1beta2B\x10TextServiceProtoP\x01Z^cloud.google.com/go/ai/generativelanguage/apiv1beta2/generativelanguagepb;generativelanguagepb'
    _globals['_GENERATETEXTREQUEST'].fields_by_name['model']._loaded_options = None
    _globals['_GENERATETEXTREQUEST'].fields_by_name['model']._serialized_options = b"\xe0A\x02\xfaA)\n'generativelanguage.googleapis.com/Model"
    _globals['_GENERATETEXTREQUEST'].fields_by_name['prompt']._loaded_options = None
    _globals['_GENERATETEXTREQUEST'].fields_by_name['prompt']._serialized_options = b'\xe0A\x02'
    _globals['_TEXTPROMPT'].fields_by_name['text']._loaded_options = None
    _globals['_TEXTPROMPT'].fields_by_name['text']._serialized_options = b'\xe0A\x02'
    _globals['_TEXTCOMPLETION'].fields_by_name['output']._loaded_options = None
    _globals['_TEXTCOMPLETION'].fields_by_name['output']._serialized_options = b'\xe0A\x03'
    _globals['_TEXTCOMPLETION'].fields_by_name['citation_metadata']._loaded_options = None
    _globals['_TEXTCOMPLETION'].fields_by_name['citation_metadata']._serialized_options = b'\xe0A\x03'
    _globals['_EMBEDTEXTREQUEST'].fields_by_name['model']._loaded_options = None
    _globals['_EMBEDTEXTREQUEST'].fields_by_name['model']._serialized_options = b"\xe0A\x02\xfaA)\n'generativelanguage.googleapis.com/Model"
    _globals['_EMBEDTEXTREQUEST'].fields_by_name['text']._loaded_options = None
    _globals['_EMBEDTEXTREQUEST'].fields_by_name['text']._serialized_options = b'\xe0A\x02'
    _globals['_EMBEDTEXTRESPONSE'].fields_by_name['embedding']._loaded_options = None
    _globals['_EMBEDTEXTRESPONSE'].fields_by_name['embedding']._serialized_options = b'\xe0A\x03'
    _globals['_TEXTSERVICE']._loaded_options = None
    _globals['_TEXTSERVICE']._serialized_options = b'\xcaA!generativelanguage.googleapis.com'
    _globals['_TEXTSERVICE'].methods_by_name['GenerateText']._loaded_options = None
    _globals['_TEXTSERVICE'].methods_by_name['GenerateText']._serialized_options = b'\xdaAFmodel,prompt,temperature,candidate_count,max_output_tokens,top_p,top_k\x82\xd3\xe4\x93\x02+"&/v1beta2/{model=models/*}:generateText:\x01*'
    _globals['_TEXTSERVICE'].methods_by_name['EmbedText']._loaded_options = None
    _globals['_TEXTSERVICE'].methods_by_name['EmbedText']._serialized_options = b'\xdaA\nmodel,text\x82\xd3\xe4\x93\x02("#/v1beta2/{model=models/*}:embedText:\x01*'
    _globals['_GENERATETEXTREQUEST']._serialized_start = 317
    _globals['_GENERATETEXTREQUEST']._serialized_end = 781
    _globals['_GENERATETEXTRESPONSE']._serialized_start = 784
    _globals['_GENERATETEXTRESPONSE']._serialized_end = 1029
    _globals['_TEXTPROMPT']._serialized_start = 1031
    _globals['_TEXTPROMPT']._serialized_end = 1062
    _globals['_TEXTCOMPLETION']._serialized_start = 1065
    _globals['_TEXTCOMPLETION']._serialized_end = 1293
    _globals['_EMBEDTEXTREQUEST']._serialized_start = 1295
    _globals['_EMBEDTEXTREQUEST']._serialized_end = 1396
    _globals['_EMBEDTEXTRESPONSE']._serialized_start = 1398
    _globals['_EMBEDTEXTRESPONSE']._serialized_end = 1509
    _globals['_EMBEDDING']._serialized_start = 1511
    _globals['_EMBEDDING']._serialized_end = 1537
    _globals['_TEXTSERVICE']._serialized_start = 1540
    _globals['_TEXTSERVICE']._serialized_end = 2039