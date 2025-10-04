"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/prediction_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import content_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_content__pb2
from .....google.cloud.aiplatform.v1 import explanation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_explanation__pb2
from .....google.cloud.aiplatform.v1 import tool_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_tool__pb2
from .....google.cloud.aiplatform.v1 import types_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_types__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/aiplatform/v1/prediction_service.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/httpbody.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/aiplatform/v1/content.proto\x1a,google/cloud/aiplatform/v1/explanation.proto\x1a%google/cloud/aiplatform/v1/tool.proto\x1a&google/cloud/aiplatform/v1/types.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xaa\x01\n\x0ePredictRequest\x12<\n\x08endpoint\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint\x12.\n\tinstances\x18\x02 \x03(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x02\x12*\n\nparameters\x18\x03 \x01(\x0b2\x16.google.protobuf.Value"\x80\x02\n\x0fPredictResponse\x12+\n\x0bpredictions\x18\x01 \x03(\x0b2\x16.google.protobuf.Value\x12\x19\n\x11deployed_model_id\x18\x02 \x01(\t\x126\n\x05model\x18\x03 \x01(\tB\'\xe0A\x03\xfaA!\n\x1faiplatform.googleapis.com/Model\x12\x1d\n\x10model_version_id\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x1f\n\x12model_display_name\x18\x04 \x01(\tB\x03\xe0A\x03\x12-\n\x08metadata\x18\x06 \x01(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x03"z\n\x11RawPredictRequest\x12<\n\x08endpoint\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint\x12\'\n\thttp_body\x18\x02 \x01(\x0b2\x14.google.api.HttpBody"\x80\x01\n\x17StreamRawPredictRequest\x12<\n\x08endpoint\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint\x12\'\n\thttp_body\x18\x02 \x01(\x0b2\x14.google.api.HttpBody"\xc0\x01\n\x14DirectPredictRequest\x12<\n\x08endpoint\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint\x122\n\x06inputs\x18\x02 \x03(\x0b2".google.cloud.aiplatform.v1.Tensor\x126\n\nparameters\x18\x03 \x01(\x0b2".google.cloud.aiplatform.v1.Tensor"\x84\x01\n\x15DirectPredictResponse\x123\n\x07outputs\x18\x01 \x03(\x0b2".google.cloud.aiplatform.v1.Tensor\x126\n\nparameters\x18\x02 \x01(\x0b2".google.cloud.aiplatform.v1.Tensor"{\n\x17DirectRawPredictRequest\x12<\n\x08endpoint\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint\x12\x13\n\x0bmethod_name\x18\x02 \x01(\t\x12\r\n\x05input\x18\x03 \x01(\x0c"*\n\x18DirectRawPredictResponse\x12\x0e\n\x06output\x18\x01 \x01(\x0c"\xd0\x01\n\x1aStreamDirectPredictRequest\x12<\n\x08endpoint\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint\x127\n\x06inputs\x18\x02 \x03(\x0b2".google.cloud.aiplatform.v1.TensorB\x03\xe0A\x01\x12;\n\nparameters\x18\x03 \x01(\x0b2".google.cloud.aiplatform.v1.TensorB\x03\xe0A\x01"\x8a\x01\n\x1bStreamDirectPredictResponse\x123\n\x07outputs\x18\x01 \x03(\x0b2".google.cloud.aiplatform.v1.Tensor\x126\n\nparameters\x18\x02 \x01(\x0b2".google.cloud.aiplatform.v1.Tensor"\x8b\x01\n\x1dStreamDirectRawPredictRequest\x12<\n\x08endpoint\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint\x12\x18\n\x0bmethod_name\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x12\n\x05input\x18\x03 \x01(\x0cB\x03\xe0A\x01"0\n\x1eStreamDirectRawPredictResponse\x12\x0e\n\x06output\x18\x01 \x01(\x0c"\xc3\x01\n\x17StreamingPredictRequest\x12<\n\x08endpoint\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint\x122\n\x06inputs\x18\x02 \x03(\x0b2".google.cloud.aiplatform.v1.Tensor\x126\n\nparameters\x18\x03 \x01(\x0b2".google.cloud.aiplatform.v1.Tensor"\x87\x01\n\x18StreamingPredictResponse\x123\n\x07outputs\x18\x01 \x03(\x0b2".google.cloud.aiplatform.v1.Tensor\x126\n\nparameters\x18\x02 \x01(\x0b2".google.cloud.aiplatform.v1.Tensor"~\n\x1aStreamingRawPredictRequest\x12<\n\x08endpoint\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint\x12\x13\n\x0bmethod_name\x18\x02 \x01(\t\x12\r\n\x05input\x18\x03 \x01(\x0c"-\n\x1bStreamingRawPredictResponse\x12\x0e\n\x06output\x18\x01 \x01(\x0c"\x9d\x02\n\x0eExplainRequest\x12<\n\x08endpoint\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint\x12.\n\tinstances\x18\x02 \x03(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x02\x12*\n\nparameters\x18\x04 \x01(\x0b2\x16.google.protobuf.Value\x12V\n\x19explanation_spec_override\x18\x05 \x01(\x0b23.google.cloud.aiplatform.v1.ExplanationSpecOverride\x12\x19\n\x11deployed_model_id\x18\x03 \x01(\t"\x98\x01\n\x0fExplainResponse\x12=\n\x0cexplanations\x18\x01 \x03(\x0b2\'.google.cloud.aiplatform.v1.Explanation\x12\x19\n\x11deployed_model_id\x18\x02 \x01(\t\x12+\n\x0bpredictions\x18\x03 \x03(\x0b2\x16.google.protobuf.Value"\xd3\x03\n\x12CountTokensRequest\x12<\n\x08endpoint\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint\x12\x12\n\x05model\x18\x03 \x01(\tB\x03\xe0A\x01\x12.\n\tinstances\x18\x02 \x03(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x01\x12:\n\x08contents\x18\x04 \x03(\x0b2#.google.cloud.aiplatform.v1.ContentB\x03\xe0A\x01\x12I\n\x12system_instruction\x18\x05 \x01(\x0b2#.google.cloud.aiplatform.v1.ContentB\x03\xe0A\x01H\x00\x88\x01\x01\x124\n\x05tools\x18\x06 \x03(\x0b2 .google.cloud.aiplatform.v1.ToolB\x03\xe0A\x01\x12Q\n\x11generation_config\x18\x07 \x01(\x0b2,.google.cloud.aiplatform.v1.GenerationConfigB\x03\xe0A\x01H\x01\x88\x01\x01B\x15\n\x13_system_instructionB\x14\n\x12_generation_config"\xa2\x01\n\x13CountTokensResponse\x12\x14\n\x0ctotal_tokens\x18\x01 \x01(\x05\x12!\n\x19total_billable_characters\x18\x02 \x01(\x05\x12R\n\x15prompt_tokens_details\x18\x03 \x03(\x0b2..google.cloud.aiplatform.v1.ModalityTokenCountB\x03\xe0A\x03"\xf5\x05\n\x16GenerateContentRequest\x12\x12\n\x05model\x18\x05 \x01(\tB\x03\xe0A\x02\x12:\n\x08contents\x18\x02 \x03(\x0b2#.google.cloud.aiplatform.v1.ContentB\x03\xe0A\x02\x12I\n\x12system_instruction\x18\x08 \x01(\x0b2#.google.cloud.aiplatform.v1.ContentB\x03\xe0A\x01H\x00\x88\x01\x01\x12G\n\x0ecached_content\x18\t \x01(\tB/\xe0A\x01\xfaA)\n\'aiplatform.googleapis.com/CachedContent\x124\n\x05tools\x18\x06 \x03(\x0b2 .google.cloud.aiplatform.v1.ToolB\x03\xe0A\x01\x12@\n\x0btool_config\x18\x07 \x01(\x0b2&.google.cloud.aiplatform.v1.ToolConfigB\x03\xe0A\x01\x12S\n\x06labels\x18\n \x03(\x0b2>.google.cloud.aiplatform.v1.GenerateContentRequest.LabelsEntryB\x03\xe0A\x01\x12G\n\x0fsafety_settings\x18\x03 \x03(\x0b2).google.cloud.aiplatform.v1.SafetySettingB\x03\xe0A\x01\x12M\n\x12model_armor_config\x18\x0b \x01(\x0b2,.google.cloud.aiplatform.v1.ModelArmorConfigB\x03\xe0A\x01\x12L\n\x11generation_config\x18\x04 \x01(\x0b2,.google.cloud.aiplatform.v1.GenerationConfigB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x15\n\x13_system_instruction"\xa0\t\n\x17GenerateContentResponse\x12>\n\ncandidates\x18\x02 \x03(\x0b2%.google.cloud.aiplatform.v1.CandidateB\x03\xe0A\x03\x12\x1a\n\rmodel_version\x18\x0b \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x0bresponse_id\x18\r \x01(\tB\x03\xe0A\x03\x12`\n\x0fprompt_feedback\x18\x03 \x01(\x0b2B.google.cloud.aiplatform.v1.GenerateContentResponse.PromptFeedbackB\x03\xe0A\x03\x12Y\n\x0eusage_metadata\x18\x04 \x01(\x0b2A.google.cloud.aiplatform.v1.GenerateContentResponse.UsageMetadata\x1a\xe7\x02\n\x0ePromptFeedback\x12k\n\x0cblock_reason\x18\x01 \x01(\x0e2P.google.cloud.aiplatform.v1.GenerateContentResponse.PromptFeedback.BlockedReasonB\x03\xe0A\x03\x12E\n\x0esafety_ratings\x18\x02 \x03(\x0b2(.google.cloud.aiplatform.v1.SafetyRatingB\x03\xe0A\x03\x12!\n\x14block_reason_message\x18\x03 \x01(\tB\x03\xe0A\x03"~\n\rBlockedReason\x12\x1e\n\x1aBLOCKED_REASON_UNSPECIFIED\x10\x00\x12\n\n\x06SAFETY\x10\x01\x12\t\n\x05OTHER\x10\x02\x12\r\n\tBLOCKLIST\x10\x03\x12\x16\n\x12PROHIBITED_CONTENT\x10\x04\x12\x0f\n\x0bMODEL_ARMOR\x10\x05\x1a\xb1\x03\n\rUsageMetadata\x12\x1a\n\x12prompt_token_count\x18\x01 \x01(\x05\x12\x1e\n\x16candidates_token_count\x18\x02 \x01(\x05\x12!\n\x14thoughts_token_count\x18\x0e \x01(\x05B\x03\xe0A\x03\x12\x19\n\x11total_token_count\x18\x03 \x01(\x05\x12\'\n\x1acached_content_token_count\x18\x05 \x01(\x05B\x03\xe0A\x03\x12R\n\x15prompt_tokens_details\x18\t \x03(\x0b2..google.cloud.aiplatform.v1.ModalityTokenCountB\x03\xe0A\x03\x12Q\n\x14cache_tokens_details\x18\n \x03(\x0b2..google.cloud.aiplatform.v1.ModalityTokenCountB\x03\xe0A\x03\x12V\n\x19candidates_tokens_details\x18\x0b \x03(\x0b2..google.cloud.aiplatform.v1.ModalityTokenCountB\x03\xe0A\x032\xf2\x19\n\x11PredictionService\x12\x94\x02\n\x07Predict\x12*.google.cloud.aiplatform.v1.PredictRequest\x1a+.google.cloud.aiplatform.v1.PredictResponse"\xaf\x01\xdaA\x1dendpoint,instances,parameters\x82\xd3\xe4\x93\x02\x88\x01"9/v1/{endpoint=projects/*/locations/*/endpoints/*}:predict:\x01*ZH"C/v1/{endpoint=projects/*/locations/*/publishers/*/models/*}:predict:\x01*\x12\xfe\x01\n\nRawPredict\x12-.google.cloud.aiplatform.v1.RawPredictRequest\x1a\x14.google.api.HttpBody"\xaa\x01\xdaA\x12endpoint,http_body\x82\xd3\xe4\x93\x02\x8e\x01"</v1/{endpoint=projects/*/locations/*/endpoints/*}:rawPredict:\x01*ZK"F/v1/{endpoint=projects/*/locations/*/publishers/*/models/*}:rawPredict:\x01*\x12\x98\x02\n\x10StreamRawPredict\x123.google.cloud.aiplatform.v1.StreamRawPredictRequest\x1a\x14.google.api.HttpBody"\xb6\x01\xdaA\x12endpoint,http_body\x82\xd3\xe4\x93\x02\x9a\x01"B/v1/{endpoint=projects/*/locations/*/endpoints/*}:streamRawPredict:\x01*ZQ"L/v1/{endpoint=projects/*/locations/*/publishers/*/models/*}:streamRawPredict:\x01*0\x01\x12\xc0\x01\n\rDirectPredict\x120.google.cloud.aiplatform.v1.DirectPredictRequest\x1a1.google.cloud.aiplatform.v1.DirectPredictResponse"J\x82\xd3\xe4\x93\x02D"?/v1/{endpoint=projects/*/locations/*/endpoints/*}:directPredict:\x01*\x12\xcc\x01\n\x10DirectRawPredict\x123.google.cloud.aiplatform.v1.DirectRawPredictRequest\x1a4.google.cloud.aiplatform.v1.DirectRawPredictResponse"M\x82\xd3\xe4\x93\x02G"B/v1/{endpoint=projects/*/locations/*/endpoints/*}:directRawPredict:\x01*\x12\x8c\x01\n\x13StreamDirectPredict\x126.google.cloud.aiplatform.v1.StreamDirectPredictRequest\x1a7.google.cloud.aiplatform.v1.StreamDirectPredictResponse"\x00(\x010\x01\x12\x95\x01\n\x16StreamDirectRawPredict\x129.google.cloud.aiplatform.v1.StreamDirectRawPredictRequest\x1a:.google.cloud.aiplatform.v1.StreamDirectRawPredictResponse"\x00(\x010\x01\x12\x83\x01\n\x10StreamingPredict\x123.google.cloud.aiplatform.v1.StreamingPredictRequest\x1a4.google.cloud.aiplatform.v1.StreamingPredictResponse"\x00(\x010\x01\x12\xb5\x02\n\x16ServerStreamingPredict\x123.google.cloud.aiplatform.v1.StreamingPredictRequest\x1a4.google.cloud.aiplatform.v1.StreamingPredictResponse"\xad\x01\x82\xd3\xe4\x93\x02\xa6\x01"H/v1/{endpoint=projects/*/locations/*/endpoints/*}:serverStreamingPredict:\x01*ZW"R/v1/{endpoint=projects/*/locations/*/publishers/*/models/*}:serverStreamingPredict:\x01*0\x01\x12\x8c\x01\n\x13StreamingRawPredict\x126.google.cloud.aiplatform.v1.StreamingRawPredictRequest\x1a7.google.cloud.aiplatform.v1.StreamingRawPredictResponse"\x00(\x010\x01\x12\xda\x01\n\x07Explain\x12*.google.cloud.aiplatform.v1.ExplainRequest\x1a+.google.cloud.aiplatform.v1.ExplainResponse"v\xdaA/endpoint,instances,parameters,deployed_model_id\x82\xd3\xe4\x93\x02>"9/v1/{endpoint=projects/*/locations/*/endpoints/*}:explain:\x01*\x12\x8d\x03\n\x0fGenerateContent\x122.google.cloud.aiplatform.v1.GenerateContentRequest\x1a3.google.cloud.aiplatform.v1.GenerateContentResponse"\x90\x02\xdaA\x0emodel,contents\x82\xd3\xe4\x93\x02\xf8\x01">/v1/{model=projects/*/locations/*/endpoints/*}:generateContent:\x01*ZM"H/v1/{model=projects/*/locations/*/publishers/*/models/*}:generateContent:\x01*Z,"\'/v1/{model=endpoints/*}:generateContent:\x01*Z6"1/v1/{model=publishers/*/models/*}:generateContent:\x01*\x12\xad\x03\n\x15StreamGenerateContent\x122.google.cloud.aiplatform.v1.GenerateContentRequest\x1a3.google.cloud.aiplatform.v1.GenerateContentResponse"\xa8\x02\xdaA\x0emodel,contents\x82\xd3\xe4\x93\x02\x90\x02"D/v1/{model=projects/*/locations/*/endpoints/*}:streamGenerateContent:\x01*ZS"N/v1/{model=projects/*/locations/*/publishers/*/models/*}:streamGenerateContent:\x01*Z2"-/v1/{model=endpoints/*}:streamGenerateContent:\x01*Z<"7/v1/{model=publishers/*/models/*}:streamGenerateContent:\x01*0\x01\x1a\x86\x01\xcaA\x19aiplatform.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-onlyB\xd4\x01\n\x1ecom.google.cloud.aiplatform.v1B\x16PredictionServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.prediction_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x16PredictionServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_PREDICTREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_PREDICTREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_PREDICTREQUEST'].fields_by_name['instances']._loaded_options = None
    _globals['_PREDICTREQUEST'].fields_by_name['instances']._serialized_options = b'\xe0A\x02'
    _globals['_PREDICTRESPONSE'].fields_by_name['model']._loaded_options = None
    _globals['_PREDICTRESPONSE'].fields_by_name['model']._serialized_options = b'\xe0A\x03\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_PREDICTRESPONSE'].fields_by_name['model_version_id']._loaded_options = None
    _globals['_PREDICTRESPONSE'].fields_by_name['model_version_id']._serialized_options = b'\xe0A\x03'
    _globals['_PREDICTRESPONSE'].fields_by_name['model_display_name']._loaded_options = None
    _globals['_PREDICTRESPONSE'].fields_by_name['model_display_name']._serialized_options = b'\xe0A\x03'
    _globals['_PREDICTRESPONSE'].fields_by_name['metadata']._loaded_options = None
    _globals['_PREDICTRESPONSE'].fields_by_name['metadata']._serialized_options = b'\xe0A\x03'
    _globals['_RAWPREDICTREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_RAWPREDICTREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_STREAMRAWPREDICTREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_STREAMRAWPREDICTREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_DIRECTPREDICTREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_DIRECTPREDICTREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_DIRECTRAWPREDICTREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_DIRECTRAWPREDICTREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_STREAMDIRECTPREDICTREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_STREAMDIRECTPREDICTREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_STREAMDIRECTPREDICTREQUEST'].fields_by_name['inputs']._loaded_options = None
    _globals['_STREAMDIRECTPREDICTREQUEST'].fields_by_name['inputs']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMDIRECTPREDICTREQUEST'].fields_by_name['parameters']._loaded_options = None
    _globals['_STREAMDIRECTPREDICTREQUEST'].fields_by_name['parameters']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMDIRECTRAWPREDICTREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_STREAMDIRECTRAWPREDICTREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_STREAMDIRECTRAWPREDICTREQUEST'].fields_by_name['method_name']._loaded_options = None
    _globals['_STREAMDIRECTRAWPREDICTREQUEST'].fields_by_name['method_name']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMDIRECTRAWPREDICTREQUEST'].fields_by_name['input']._loaded_options = None
    _globals['_STREAMDIRECTRAWPREDICTREQUEST'].fields_by_name['input']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMINGPREDICTREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_STREAMINGPREDICTREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_STREAMINGRAWPREDICTREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_STREAMINGRAWPREDICTREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_EXPLAINREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_EXPLAINREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_EXPLAINREQUEST'].fields_by_name['instances']._loaded_options = None
    _globals['_EXPLAINREQUEST'].fields_by_name['instances']._serialized_options = b'\xe0A\x02'
    _globals['_COUNTTOKENSREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_COUNTTOKENSREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_COUNTTOKENSREQUEST'].fields_by_name['model']._loaded_options = None
    _globals['_COUNTTOKENSREQUEST'].fields_by_name['model']._serialized_options = b'\xe0A\x01'
    _globals['_COUNTTOKENSREQUEST'].fields_by_name['instances']._loaded_options = None
    _globals['_COUNTTOKENSREQUEST'].fields_by_name['instances']._serialized_options = b'\xe0A\x01'
    _globals['_COUNTTOKENSREQUEST'].fields_by_name['contents']._loaded_options = None
    _globals['_COUNTTOKENSREQUEST'].fields_by_name['contents']._serialized_options = b'\xe0A\x01'
    _globals['_COUNTTOKENSREQUEST'].fields_by_name['system_instruction']._loaded_options = None
    _globals['_COUNTTOKENSREQUEST'].fields_by_name['system_instruction']._serialized_options = b'\xe0A\x01'
    _globals['_COUNTTOKENSREQUEST'].fields_by_name['tools']._loaded_options = None
    _globals['_COUNTTOKENSREQUEST'].fields_by_name['tools']._serialized_options = b'\xe0A\x01'
    _globals['_COUNTTOKENSREQUEST'].fields_by_name['generation_config']._loaded_options = None
    _globals['_COUNTTOKENSREQUEST'].fields_by_name['generation_config']._serialized_options = b'\xe0A\x01'
    _globals['_COUNTTOKENSRESPONSE'].fields_by_name['prompt_tokens_details']._loaded_options = None
    _globals['_COUNTTOKENSRESPONSE'].fields_by_name['prompt_tokens_details']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATECONTENTREQUEST_LABELSENTRY']._loaded_options = None
    _globals['_GENERATECONTENTREQUEST_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_GENERATECONTENTREQUEST'].fields_by_name['model']._loaded_options = None
    _globals['_GENERATECONTENTREQUEST'].fields_by_name['model']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATECONTENTREQUEST'].fields_by_name['contents']._loaded_options = None
    _globals['_GENERATECONTENTREQUEST'].fields_by_name['contents']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATECONTENTREQUEST'].fields_by_name['system_instruction']._loaded_options = None
    _globals['_GENERATECONTENTREQUEST'].fields_by_name['system_instruction']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECONTENTREQUEST'].fields_by_name['cached_content']._loaded_options = None
    _globals['_GENERATECONTENTREQUEST'].fields_by_name['cached_content']._serialized_options = b"\xe0A\x01\xfaA)\n'aiplatform.googleapis.com/CachedContent"
    _globals['_GENERATECONTENTREQUEST'].fields_by_name['tools']._loaded_options = None
    _globals['_GENERATECONTENTREQUEST'].fields_by_name['tools']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECONTENTREQUEST'].fields_by_name['tool_config']._loaded_options = None
    _globals['_GENERATECONTENTREQUEST'].fields_by_name['tool_config']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECONTENTREQUEST'].fields_by_name['labels']._loaded_options = None
    _globals['_GENERATECONTENTREQUEST'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECONTENTREQUEST'].fields_by_name['safety_settings']._loaded_options = None
    _globals['_GENERATECONTENTREQUEST'].fields_by_name['safety_settings']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECONTENTREQUEST'].fields_by_name['model_armor_config']._loaded_options = None
    _globals['_GENERATECONTENTREQUEST'].fields_by_name['model_armor_config']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECONTENTREQUEST'].fields_by_name['generation_config']._loaded_options = None
    _globals['_GENERATECONTENTREQUEST'].fields_by_name['generation_config']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECONTENTRESPONSE_PROMPTFEEDBACK'].fields_by_name['block_reason']._loaded_options = None
    _globals['_GENERATECONTENTRESPONSE_PROMPTFEEDBACK'].fields_by_name['block_reason']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATECONTENTRESPONSE_PROMPTFEEDBACK'].fields_by_name['safety_ratings']._loaded_options = None
    _globals['_GENERATECONTENTRESPONSE_PROMPTFEEDBACK'].fields_by_name['safety_ratings']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATECONTENTRESPONSE_PROMPTFEEDBACK'].fields_by_name['block_reason_message']._loaded_options = None
    _globals['_GENERATECONTENTRESPONSE_PROMPTFEEDBACK'].fields_by_name['block_reason_message']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATECONTENTRESPONSE_USAGEMETADATA'].fields_by_name['thoughts_token_count']._loaded_options = None
    _globals['_GENERATECONTENTRESPONSE_USAGEMETADATA'].fields_by_name['thoughts_token_count']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATECONTENTRESPONSE_USAGEMETADATA'].fields_by_name['cached_content_token_count']._loaded_options = None
    _globals['_GENERATECONTENTRESPONSE_USAGEMETADATA'].fields_by_name['cached_content_token_count']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATECONTENTRESPONSE_USAGEMETADATA'].fields_by_name['prompt_tokens_details']._loaded_options = None
    _globals['_GENERATECONTENTRESPONSE_USAGEMETADATA'].fields_by_name['prompt_tokens_details']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATECONTENTRESPONSE_USAGEMETADATA'].fields_by_name['cache_tokens_details']._loaded_options = None
    _globals['_GENERATECONTENTRESPONSE_USAGEMETADATA'].fields_by_name['cache_tokens_details']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATECONTENTRESPONSE_USAGEMETADATA'].fields_by_name['candidates_tokens_details']._loaded_options = None
    _globals['_GENERATECONTENTRESPONSE_USAGEMETADATA'].fields_by_name['candidates_tokens_details']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATECONTENTRESPONSE'].fields_by_name['candidates']._loaded_options = None
    _globals['_GENERATECONTENTRESPONSE'].fields_by_name['candidates']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATECONTENTRESPONSE'].fields_by_name['model_version']._loaded_options = None
    _globals['_GENERATECONTENTRESPONSE'].fields_by_name['model_version']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATECONTENTRESPONSE'].fields_by_name['create_time']._loaded_options = None
    _globals['_GENERATECONTENTRESPONSE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATECONTENTRESPONSE'].fields_by_name['response_id']._loaded_options = None
    _globals['_GENERATECONTENTRESPONSE'].fields_by_name['response_id']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATECONTENTRESPONSE'].fields_by_name['prompt_feedback']._loaded_options = None
    _globals['_GENERATECONTENTRESPONSE'].fields_by_name['prompt_feedback']._serialized_options = b'\xe0A\x03'
    _globals['_PREDICTIONSERVICE']._loaded_options = None
    _globals['_PREDICTIONSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2Aghttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_PREDICTIONSERVICE'].methods_by_name['Predict']._loaded_options = None
    _globals['_PREDICTIONSERVICE'].methods_by_name['Predict']._serialized_options = b'\xdaA\x1dendpoint,instances,parameters\x82\xd3\xe4\x93\x02\x88\x01"9/v1/{endpoint=projects/*/locations/*/endpoints/*}:predict:\x01*ZH"C/v1/{endpoint=projects/*/locations/*/publishers/*/models/*}:predict:\x01*'
    _globals['_PREDICTIONSERVICE'].methods_by_name['RawPredict']._loaded_options = None
    _globals['_PREDICTIONSERVICE'].methods_by_name['RawPredict']._serialized_options = b'\xdaA\x12endpoint,http_body\x82\xd3\xe4\x93\x02\x8e\x01"</v1/{endpoint=projects/*/locations/*/endpoints/*}:rawPredict:\x01*ZK"F/v1/{endpoint=projects/*/locations/*/publishers/*/models/*}:rawPredict:\x01*'
    _globals['_PREDICTIONSERVICE'].methods_by_name['StreamRawPredict']._loaded_options = None
    _globals['_PREDICTIONSERVICE'].methods_by_name['StreamRawPredict']._serialized_options = b'\xdaA\x12endpoint,http_body\x82\xd3\xe4\x93\x02\x9a\x01"B/v1/{endpoint=projects/*/locations/*/endpoints/*}:streamRawPredict:\x01*ZQ"L/v1/{endpoint=projects/*/locations/*/publishers/*/models/*}:streamRawPredict:\x01*'
    _globals['_PREDICTIONSERVICE'].methods_by_name['DirectPredict']._loaded_options = None
    _globals['_PREDICTIONSERVICE'].methods_by_name['DirectPredict']._serialized_options = b'\x82\xd3\xe4\x93\x02D"?/v1/{endpoint=projects/*/locations/*/endpoints/*}:directPredict:\x01*'
    _globals['_PREDICTIONSERVICE'].methods_by_name['DirectRawPredict']._loaded_options = None
    _globals['_PREDICTIONSERVICE'].methods_by_name['DirectRawPredict']._serialized_options = b'\x82\xd3\xe4\x93\x02G"B/v1/{endpoint=projects/*/locations/*/endpoints/*}:directRawPredict:\x01*'
    _globals['_PREDICTIONSERVICE'].methods_by_name['ServerStreamingPredict']._loaded_options = None
    _globals['_PREDICTIONSERVICE'].methods_by_name['ServerStreamingPredict']._serialized_options = b'\x82\xd3\xe4\x93\x02\xa6\x01"H/v1/{endpoint=projects/*/locations/*/endpoints/*}:serverStreamingPredict:\x01*ZW"R/v1/{endpoint=projects/*/locations/*/publishers/*/models/*}:serverStreamingPredict:\x01*'
    _globals['_PREDICTIONSERVICE'].methods_by_name['Explain']._loaded_options = None
    _globals['_PREDICTIONSERVICE'].methods_by_name['Explain']._serialized_options = b'\xdaA/endpoint,instances,parameters,deployed_model_id\x82\xd3\xe4\x93\x02>"9/v1/{endpoint=projects/*/locations/*/endpoints/*}:explain:\x01*'
    _globals['_PREDICTIONSERVICE'].methods_by_name['GenerateContent']._loaded_options = None
    _globals['_PREDICTIONSERVICE'].methods_by_name['GenerateContent']._serialized_options = b'\xdaA\x0emodel,contents\x82\xd3\xe4\x93\x02\xf8\x01">/v1/{model=projects/*/locations/*/endpoints/*}:generateContent:\x01*ZM"H/v1/{model=projects/*/locations/*/publishers/*/models/*}:generateContent:\x01*Z,"\'/v1/{model=endpoints/*}:generateContent:\x01*Z6"1/v1/{model=publishers/*/models/*}:generateContent:\x01*'
    _globals['_PREDICTIONSERVICE'].methods_by_name['StreamGenerateContent']._loaded_options = None
    _globals['_PREDICTIONSERVICE'].methods_by_name['StreamGenerateContent']._serialized_options = b'\xdaA\x0emodel,contents\x82\xd3\xe4\x93\x02\x90\x02"D/v1/{model=projects/*/locations/*/endpoints/*}:streamGenerateContent:\x01*ZS"N/v1/{model=projects/*/locations/*/publishers/*/models/*}:streamGenerateContent:\x01*Z2"-/v1/{model=endpoints/*}:streamGenerateContent:\x01*Z<"7/v1/{model=publishers/*/models/*}:streamGenerateContent:\x01*'
    _globals['_PREDICTREQUEST']._serialized_start = 456
    _globals['_PREDICTREQUEST']._serialized_end = 626
    _globals['_PREDICTRESPONSE']._serialized_start = 629
    _globals['_PREDICTRESPONSE']._serialized_end = 885
    _globals['_RAWPREDICTREQUEST']._serialized_start = 887
    _globals['_RAWPREDICTREQUEST']._serialized_end = 1009
    _globals['_STREAMRAWPREDICTREQUEST']._serialized_start = 1012
    _globals['_STREAMRAWPREDICTREQUEST']._serialized_end = 1140
    _globals['_DIRECTPREDICTREQUEST']._serialized_start = 1143
    _globals['_DIRECTPREDICTREQUEST']._serialized_end = 1335
    _globals['_DIRECTPREDICTRESPONSE']._serialized_start = 1338
    _globals['_DIRECTPREDICTRESPONSE']._serialized_end = 1470
    _globals['_DIRECTRAWPREDICTREQUEST']._serialized_start = 1472
    _globals['_DIRECTRAWPREDICTREQUEST']._serialized_end = 1595
    _globals['_DIRECTRAWPREDICTRESPONSE']._serialized_start = 1597
    _globals['_DIRECTRAWPREDICTRESPONSE']._serialized_end = 1639
    _globals['_STREAMDIRECTPREDICTREQUEST']._serialized_start = 1642
    _globals['_STREAMDIRECTPREDICTREQUEST']._serialized_end = 1850
    _globals['_STREAMDIRECTPREDICTRESPONSE']._serialized_start = 1853
    _globals['_STREAMDIRECTPREDICTRESPONSE']._serialized_end = 1991
    _globals['_STREAMDIRECTRAWPREDICTREQUEST']._serialized_start = 1994
    _globals['_STREAMDIRECTRAWPREDICTREQUEST']._serialized_end = 2133
    _globals['_STREAMDIRECTRAWPREDICTRESPONSE']._serialized_start = 2135
    _globals['_STREAMDIRECTRAWPREDICTRESPONSE']._serialized_end = 2183
    _globals['_STREAMINGPREDICTREQUEST']._serialized_start = 2186
    _globals['_STREAMINGPREDICTREQUEST']._serialized_end = 2381
    _globals['_STREAMINGPREDICTRESPONSE']._serialized_start = 2384
    _globals['_STREAMINGPREDICTRESPONSE']._serialized_end = 2519
    _globals['_STREAMINGRAWPREDICTREQUEST']._serialized_start = 2521
    _globals['_STREAMINGRAWPREDICTREQUEST']._serialized_end = 2647
    _globals['_STREAMINGRAWPREDICTRESPONSE']._serialized_start = 2649
    _globals['_STREAMINGRAWPREDICTRESPONSE']._serialized_end = 2694
    _globals['_EXPLAINREQUEST']._serialized_start = 2697
    _globals['_EXPLAINREQUEST']._serialized_end = 2982
    _globals['_EXPLAINRESPONSE']._serialized_start = 2985
    _globals['_EXPLAINRESPONSE']._serialized_end = 3137
    _globals['_COUNTTOKENSREQUEST']._serialized_start = 3140
    _globals['_COUNTTOKENSREQUEST']._serialized_end = 3607
    _globals['_COUNTTOKENSRESPONSE']._serialized_start = 3610
    _globals['_COUNTTOKENSRESPONSE']._serialized_end = 3772
    _globals['_GENERATECONTENTREQUEST']._serialized_start = 3775
    _globals['_GENERATECONTENTREQUEST']._serialized_end = 4532
    _globals['_GENERATECONTENTREQUEST_LABELSENTRY']._serialized_start = 4464
    _globals['_GENERATECONTENTREQUEST_LABELSENTRY']._serialized_end = 4509
    _globals['_GENERATECONTENTRESPONSE']._serialized_start = 4535
    _globals['_GENERATECONTENTRESPONSE']._serialized_end = 5719
    _globals['_GENERATECONTENTRESPONSE_PROMPTFEEDBACK']._serialized_start = 4924
    _globals['_GENERATECONTENTRESPONSE_PROMPTFEEDBACK']._serialized_end = 5283
    _globals['_GENERATECONTENTRESPONSE_PROMPTFEEDBACK_BLOCKEDREASON']._serialized_start = 5157
    _globals['_GENERATECONTENTRESPONSE_PROMPTFEEDBACK_BLOCKEDREASON']._serialized_end = 5283
    _globals['_GENERATECONTENTRESPONSE_USAGEMETADATA']._serialized_start = 5286
    _globals['_GENERATECONTENTRESPONSE_USAGEMETADATA']._serialized_end = 5719
    _globals['_PREDICTIONSERVICE']._serialized_start = 5722
    _globals['_PREDICTIONSERVICE']._serialized_end = 9036