"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ai/generativelanguage/v1beta/discuss_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ai.generativelanguage.v1beta import citation_pb2 as google_dot_ai_dot_generativelanguage_dot_v1beta_dot_citation__pb2
from .....google.ai.generativelanguage.v1beta import safety_pb2 as google_dot_ai_dot_generativelanguage_dot_v1beta_dot_safety__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/ai/generativelanguage/v1beta/discuss_service.proto\x12#google.ai.generativelanguage.v1beta\x1a2google/ai/generativelanguage/v1beta/citation.proto\x1a0google/ai/generativelanguage/v1beta/safety.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xcd\x02\n\x16GenerateMessageRequest\x12>\n\x05model\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'generativelanguage.googleapis.com/Model\x12G\n\x06prompt\x18\x02 \x01(\x0b22.google.ai.generativelanguage.v1beta.MessagePromptB\x03\xe0A\x02\x12\x1d\n\x0btemperature\x18\x03 \x01(\x02B\x03\xe0A\x01H\x00\x88\x01\x01\x12!\n\x0fcandidate_count\x18\x04 \x01(\x05B\x03\xe0A\x01H\x01\x88\x01\x01\x12\x17\n\x05top_p\x18\x05 \x01(\x02B\x03\xe0A\x01H\x02\x88\x01\x01\x12\x17\n\x05top_k\x18\x06 \x01(\x05B\x03\xe0A\x01H\x03\x88\x01\x01B\x0e\n\x0c_temperatureB\x12\n\x10_candidate_countB\x08\n\x06_top_pB\x08\n\x06_top_k"\xe0\x01\n\x17GenerateMessageResponse\x12@\n\ncandidates\x18\x01 \x03(\x0b2,.google.ai.generativelanguage.v1beta.Message\x12>\n\x08messages\x18\x02 \x03(\x0b2,.google.ai.generativelanguage.v1beta.Message\x12C\n\x07filters\x18\x03 \x03(\x0b22.google.ai.generativelanguage.v1beta.ContentFilter"\xa6\x01\n\x07Message\x12\x13\n\x06author\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x14\n\x07content\x18\x02 \x01(\tB\x03\xe0A\x02\x12Z\n\x11citation_metadata\x18\x03 \x01(\x0b25.google.ai.generativelanguage.v1beta.CitationMetadataB\x03\xe0A\x03H\x00\x88\x01\x01B\x14\n\x12_citation_metadata"\xaf\x01\n\rMessagePrompt\x12\x14\n\x07context\x18\x01 \x01(\tB\x03\xe0A\x01\x12C\n\x08examples\x18\x02 \x03(\x0b2,.google.ai.generativelanguage.v1beta.ExampleB\x03\xe0A\x01\x12C\n\x08messages\x18\x03 \x03(\x0b2,.google.ai.generativelanguage.v1beta.MessageB\x03\xe0A\x02"\x8e\x01\n\x07Example\x12@\n\x05input\x18\x01 \x01(\x0b2,.google.ai.generativelanguage.v1beta.MessageB\x03\xe0A\x02\x12A\n\x06output\x18\x02 \x01(\x0b2,.google.ai.generativelanguage.v1beta.MessageB\x03\xe0A\x02"\xa4\x01\n\x19CountMessageTokensRequest\x12>\n\x05model\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'generativelanguage.googleapis.com/Model\x12G\n\x06prompt\x18\x02 \x01(\x0b22.google.ai.generativelanguage.v1beta.MessagePromptB\x03\xe0A\x02"1\n\x1aCountMessageTokensResponse\x12\x13\n\x0btoken_count\x18\x01 \x01(\x052\x90\x04\n\x0eDiscussService\x12\xf8\x01\n\x0fGenerateMessage\x12;.google.ai.generativelanguage.v1beta.GenerateMessageRequest\x1a<.google.ai.generativelanguage.v1beta.GenerateMessageResponse"j\xdaA4model,prompt,temperature,candidate_count,top_p,top_k\x82\xd3\xe4\x93\x02-"(/v1beta/{model=models/*}:generateMessage:\x01*\x12\xdc\x01\n\x12CountMessageTokens\x12>.google.ai.generativelanguage.v1beta.CountMessageTokensRequest\x1a?.google.ai.generativelanguage.v1beta.CountMessageTokensResponse"E\xdaA\x0cmodel,prompt\x82\xd3\xe4\x93\x020"+/v1beta/{model=models/*}:countMessageTokens:\x01*\x1a$\xcaA!generativelanguage.googleapis.comB\x9f\x01\n\'com.google.ai.generativelanguage.v1betaB\x13DiscussServiceProtoP\x01Z]cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1beta.discuss_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.ai.generativelanguage.v1betaB\x13DiscussServiceProtoP\x01Z]cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb;generativelanguagepb"
    _globals['_GENERATEMESSAGEREQUEST'].fields_by_name['model']._loaded_options = None
    _globals['_GENERATEMESSAGEREQUEST'].fields_by_name['model']._serialized_options = b"\xe0A\x02\xfaA)\n'generativelanguage.googleapis.com/Model"
    _globals['_GENERATEMESSAGEREQUEST'].fields_by_name['prompt']._loaded_options = None
    _globals['_GENERATEMESSAGEREQUEST'].fields_by_name['prompt']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEMESSAGEREQUEST'].fields_by_name['temperature']._loaded_options = None
    _globals['_GENERATEMESSAGEREQUEST'].fields_by_name['temperature']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEMESSAGEREQUEST'].fields_by_name['candidate_count']._loaded_options = None
    _globals['_GENERATEMESSAGEREQUEST'].fields_by_name['candidate_count']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEMESSAGEREQUEST'].fields_by_name['top_p']._loaded_options = None
    _globals['_GENERATEMESSAGEREQUEST'].fields_by_name['top_p']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEMESSAGEREQUEST'].fields_by_name['top_k']._loaded_options = None
    _globals['_GENERATEMESSAGEREQUEST'].fields_by_name['top_k']._serialized_options = b'\xe0A\x01'
    _globals['_MESSAGE'].fields_by_name['author']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['author']._serialized_options = b'\xe0A\x01'
    _globals['_MESSAGE'].fields_by_name['content']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['content']._serialized_options = b'\xe0A\x02'
    _globals['_MESSAGE'].fields_by_name['citation_metadata']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['citation_metadata']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGEPROMPT'].fields_by_name['context']._loaded_options = None
    _globals['_MESSAGEPROMPT'].fields_by_name['context']._serialized_options = b'\xe0A\x01'
    _globals['_MESSAGEPROMPT'].fields_by_name['examples']._loaded_options = None
    _globals['_MESSAGEPROMPT'].fields_by_name['examples']._serialized_options = b'\xe0A\x01'
    _globals['_MESSAGEPROMPT'].fields_by_name['messages']._loaded_options = None
    _globals['_MESSAGEPROMPT'].fields_by_name['messages']._serialized_options = b'\xe0A\x02'
    _globals['_EXAMPLE'].fields_by_name['input']._loaded_options = None
    _globals['_EXAMPLE'].fields_by_name['input']._serialized_options = b'\xe0A\x02'
    _globals['_EXAMPLE'].fields_by_name['output']._loaded_options = None
    _globals['_EXAMPLE'].fields_by_name['output']._serialized_options = b'\xe0A\x02'
    _globals['_COUNTMESSAGETOKENSREQUEST'].fields_by_name['model']._loaded_options = None
    _globals['_COUNTMESSAGETOKENSREQUEST'].fields_by_name['model']._serialized_options = b"\xe0A\x02\xfaA)\n'generativelanguage.googleapis.com/Model"
    _globals['_COUNTMESSAGETOKENSREQUEST'].fields_by_name['prompt']._loaded_options = None
    _globals['_COUNTMESSAGETOKENSREQUEST'].fields_by_name['prompt']._serialized_options = b'\xe0A\x02'
    _globals['_DISCUSSSERVICE']._loaded_options = None
    _globals['_DISCUSSSERVICE']._serialized_options = b'\xcaA!generativelanguage.googleapis.com'
    _globals['_DISCUSSSERVICE'].methods_by_name['GenerateMessage']._loaded_options = None
    _globals['_DISCUSSSERVICE'].methods_by_name['GenerateMessage']._serialized_options = b'\xdaA4model,prompt,temperature,candidate_count,top_p,top_k\x82\xd3\xe4\x93\x02-"(/v1beta/{model=models/*}:generateMessage:\x01*'
    _globals['_DISCUSSSERVICE'].methods_by_name['CountMessageTokens']._loaded_options = None
    _globals['_DISCUSSSERVICE'].methods_by_name['CountMessageTokens']._serialized_options = b'\xdaA\x0cmodel,prompt\x82\xd3\xe4\x93\x020"+/v1beta/{model=models/*}:countMessageTokens:\x01*'
    _globals['_GENERATEMESSAGEREQUEST']._serialized_start = 316
    _globals['_GENERATEMESSAGEREQUEST']._serialized_end = 649
    _globals['_GENERATEMESSAGERESPONSE']._serialized_start = 652
    _globals['_GENERATEMESSAGERESPONSE']._serialized_end = 876
    _globals['_MESSAGE']._serialized_start = 879
    _globals['_MESSAGE']._serialized_end = 1045
    _globals['_MESSAGEPROMPT']._serialized_start = 1048
    _globals['_MESSAGEPROMPT']._serialized_end = 1223
    _globals['_EXAMPLE']._serialized_start = 1226
    _globals['_EXAMPLE']._serialized_end = 1368
    _globals['_COUNTMESSAGETOKENSREQUEST']._serialized_start = 1371
    _globals['_COUNTMESSAGETOKENSREQUEST']._serialized_end = 1535
    _globals['_COUNTMESSAGETOKENSRESPONSE']._serialized_start = 1537
    _globals['_COUNTMESSAGETOKENSRESPONSE']._serialized_end = 1586
    _globals['_DISCUSSSERVICE']._serialized_start = 1589
    _globals['_DISCUSSSERVICE']._serialized_end = 2117