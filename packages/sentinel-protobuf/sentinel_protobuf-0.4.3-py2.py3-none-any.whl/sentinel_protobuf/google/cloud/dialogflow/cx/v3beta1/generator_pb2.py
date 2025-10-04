"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/dialogflow/cx/v3beta1/generator.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import generative_settings_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_generative__settings__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/dialogflow/cx/v3beta1/generator.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a<google/cloud/dialogflow/cx/v3beta1/generative_settings.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xc8\x05\n\tGenerator\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12D\n\x0bprompt_text\x18\x03 \x01(\x0b2*.google.cloud.dialogflow.cx.v3beta1.PhraseB\x03\xe0A\x02\x12T\n\x0cplaceholders\x18\x05 \x03(\x0b29.google.cloud.dialogflow.cx.v3beta1.Generator.PlaceholderB\x03\xe0A\x01\x12P\n\x12llm_model_settings\x18\t \x01(\x0b24.google.cloud.dialogflow.cx.v3beta1.LlmModelSettings\x12U\n\x0fmodel_parameter\x18\x08 \x01(\x0b2<.google.cloud.dialogflow.cx.v3beta1.Generator.ModelParameter\x1a\'\n\x0bPlaceholder\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a\xaa\x01\n\x0eModelParameter\x12\x18\n\x0btemperature\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x1d\n\x10max_decode_steps\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x12\n\x05top_p\x18\x03 \x01(\x02H\x02\x88\x01\x01\x12\x12\n\x05top_k\x18\x04 \x01(\x05H\x03\x88\x01\x01B\x0e\n\x0c_temperatureB\x13\n\x11_max_decode_stepsB\x08\n\x06_top_pB\x08\n\x06_top_k:w\xeaAt\n#dialogflow.googleapis.com/Generator\x12Mprojects/{project}/locations/{location}/agents/{agent}/generators/{generator}"\x1b\n\x06Phrase\x12\x11\n\x04text\x18\x01 \x01(\tB\x03\xe0A\x02"\x92\x01\n\x15ListGeneratorsRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#dialogflow.googleapis.com/Generator\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"t\n\x16ListGeneratorsResponse\x12A\n\ngenerators\x18\x01 \x03(\x0b2-.google.cloud.dialogflow.cx.v3beta1.Generator\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"g\n\x13GetGeneratorRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#dialogflow.googleapis.com/Generator\x12\x15\n\rlanguage_code\x18\x02 \x01(\t"\xb3\x01\n\x16CreateGeneratorRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#dialogflow.googleapis.com/Generator\x12E\n\tgenerator\x18\x02 \x01(\x0b2-.google.cloud.dialogflow.cx.v3beta1.GeneratorB\x03\xe0A\x02\x12\x15\n\rlanguage_code\x18\x03 \x01(\t"\xa7\x01\n\x16UpdateGeneratorRequest\x12E\n\tgenerator\x18\x01 \x01(\x0b2-.google.cloud.dialogflow.cx.v3beta1.GeneratorB\x03\xe0A\x02\x12\x15\n\rlanguage_code\x18\x02 \x01(\t\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"b\n\x16DeleteGeneratorRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#dialogflow.googleapis.com/Generator\x12\r\n\x05force\x18\x02 \x01(\x082\xaf\t\n\nGenerators\x12\xd6\x01\n\x0eListGenerators\x129.google.cloud.dialogflow.cx.v3beta1.ListGeneratorsRequest\x1a:.google.cloud.dialogflow.cx.v3beta1.ListGeneratorsResponse"M\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v3beta1/{parent=projects/*/locations/*/agents/*}/generators\x12\xc3\x01\n\x0cGetGenerator\x127.google.cloud.dialogflow.cx.v3beta1.GetGeneratorRequest\x1a-.google.cloud.dialogflow.cx.v3beta1.Generator"K\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v3beta1/{name=projects/*/locations/*/agents/*/generators/*}\x12\xe0\x01\n\x0fCreateGenerator\x12:.google.cloud.dialogflow.cx.v3beta1.CreateGeneratorRequest\x1a-.google.cloud.dialogflow.cx.v3beta1.Generator"b\xdaA\x10parent,generator\x82\xd3\xe4\x93\x02I"</v3beta1/{parent=projects/*/locations/*/agents/*}/generators:\tgenerator\x12\xef\x01\n\x0fUpdateGenerator\x12:.google.cloud.dialogflow.cx.v3beta1.UpdateGeneratorRequest\x1a-.google.cloud.dialogflow.cx.v3beta1.Generator"q\xdaA\x15generator,update_mask\x82\xd3\xe4\x93\x02S2F/v3beta1/{generator.name=projects/*/locations/*/agents/*/generators/*}:\tgenerator\x12\xb2\x01\n\x0fDeleteGenerator\x12:.google.cloud.dialogflow.cx.v3beta1.DeleteGeneratorRequest\x1a\x16.google.protobuf.Empty"K\xdaA\x04name\x82\xd3\xe4\x93\x02>*</v3beta1/{name=projects/*/locations/*/agents/*/generators/*}\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xc5\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\x0eGeneratorProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.generator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\x0eGeneratorProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1'
    _globals['_GENERATOR'].fields_by_name['display_name']._loaded_options = None
    _globals['_GENERATOR'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATOR'].fields_by_name['prompt_text']._loaded_options = None
    _globals['_GENERATOR'].fields_by_name['prompt_text']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATOR'].fields_by_name['placeholders']._loaded_options = None
    _globals['_GENERATOR'].fields_by_name['placeholders']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATOR']._loaded_options = None
    _globals['_GENERATOR']._serialized_options = b'\xeaAt\n#dialogflow.googleapis.com/Generator\x12Mprojects/{project}/locations/{location}/agents/{agent}/generators/{generator}'
    _globals['_PHRASE'].fields_by_name['text']._loaded_options = None
    _globals['_PHRASE'].fields_by_name['text']._serialized_options = b'\xe0A\x02'
    _globals['_LISTGENERATORSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTGENERATORSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#dialogflow.googleapis.com/Generator'
    _globals['_GETGENERATORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETGENERATORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#dialogflow.googleapis.com/Generator'
    _globals['_CREATEGENERATORREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEGENERATORREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#dialogflow.googleapis.com/Generator'
    _globals['_CREATEGENERATORREQUEST'].fields_by_name['generator']._loaded_options = None
    _globals['_CREATEGENERATORREQUEST'].fields_by_name['generator']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEGENERATORREQUEST'].fields_by_name['generator']._loaded_options = None
    _globals['_UPDATEGENERATORREQUEST'].fields_by_name['generator']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEGENERATORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEGENERATORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#dialogflow.googleapis.com/Generator'
    _globals['_GENERATORS']._loaded_options = None
    _globals['_GENERATORS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_GENERATORS'].methods_by_name['ListGenerators']._loaded_options = None
    _globals['_GENERATORS'].methods_by_name['ListGenerators']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v3beta1/{parent=projects/*/locations/*/agents/*}/generators'
    _globals['_GENERATORS'].methods_by_name['GetGenerator']._loaded_options = None
    _globals['_GENERATORS'].methods_by_name['GetGenerator']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v3beta1/{name=projects/*/locations/*/agents/*/generators/*}'
    _globals['_GENERATORS'].methods_by_name['CreateGenerator']._loaded_options = None
    _globals['_GENERATORS'].methods_by_name['CreateGenerator']._serialized_options = b'\xdaA\x10parent,generator\x82\xd3\xe4\x93\x02I"</v3beta1/{parent=projects/*/locations/*/agents/*}/generators:\tgenerator'
    _globals['_GENERATORS'].methods_by_name['UpdateGenerator']._loaded_options = None
    _globals['_GENERATORS'].methods_by_name['UpdateGenerator']._serialized_options = b'\xdaA\x15generator,update_mask\x82\xd3\xe4\x93\x02S2F/v3beta1/{generator.name=projects/*/locations/*/agents/*/generators/*}:\tgenerator'
    _globals['_GENERATORS'].methods_by_name['DeleteGenerator']._loaded_options = None
    _globals['_GENERATORS'].methods_by_name['DeleteGenerator']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02>*</v3beta1/{name=projects/*/locations/*/agents/*/generators/*}'
    _globals['_GENERATOR']._serialized_start = 331
    _globals['_GENERATOR']._serialized_end = 1043
    _globals['_GENERATOR_PLACEHOLDER']._serialized_start = 710
    _globals['_GENERATOR_PLACEHOLDER']._serialized_end = 749
    _globals['_GENERATOR_MODELPARAMETER']._serialized_start = 752
    _globals['_GENERATOR_MODELPARAMETER']._serialized_end = 922
    _globals['_PHRASE']._serialized_start = 1045
    _globals['_PHRASE']._serialized_end = 1072
    _globals['_LISTGENERATORSREQUEST']._serialized_start = 1075
    _globals['_LISTGENERATORSREQUEST']._serialized_end = 1221
    _globals['_LISTGENERATORSRESPONSE']._serialized_start = 1223
    _globals['_LISTGENERATORSRESPONSE']._serialized_end = 1339
    _globals['_GETGENERATORREQUEST']._serialized_start = 1341
    _globals['_GETGENERATORREQUEST']._serialized_end = 1444
    _globals['_CREATEGENERATORREQUEST']._serialized_start = 1447
    _globals['_CREATEGENERATORREQUEST']._serialized_end = 1626
    _globals['_UPDATEGENERATORREQUEST']._serialized_start = 1629
    _globals['_UPDATEGENERATORREQUEST']._serialized_end = 1796
    _globals['_DELETEGENERATORREQUEST']._serialized_start = 1798
    _globals['_DELETEGENERATORREQUEST']._serialized_end = 1896
    _globals['_GENERATORS']._serialized_start = 1899
    _globals['_GENERATORS']._serialized_end = 3098