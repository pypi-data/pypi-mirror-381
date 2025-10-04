"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/dialogflow/cx/v3/fulfillment.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3 import advanced_settings_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_advanced__settings__pb2
from ......google.cloud.dialogflow.cx.v3 import response_message_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_response__message__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/dialogflow/cx/v3/fulfillment.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/dialogflow/cx/v3/advanced_settings.proto\x1a4google/cloud/dialogflow/cx/v3/response_message.proto\x1a\x1cgoogle/protobuf/struct.proto"\xbf\n\n\x0bFulfillment\x12@\n\x08messages\x18\x01 \x03(\x0b2..google.cloud.dialogflow.cx.v3.ResponseMessage\x127\n\x07webhook\x18\x02 \x01(\tB&\xfaA#\n!dialogflow.googleapis.com/Webhook\x12 \n\x18return_partial_responses\x18\x08 \x01(\x08\x12\x0b\n\x03tag\x18\x03 \x01(\t\x12\\\n\x15set_parameter_actions\x18\x04 \x03(\x0b2=.google.cloud.dialogflow.cx.v3.Fulfillment.SetParameterAction\x12V\n\x11conditional_cases\x18\x05 \x03(\x0b2;.google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases\x12J\n\x11advanced_settings\x18\x07 \x01(\x0b2/.google.cloud.dialogflow.cx.v3.AdvancedSettings\x12"\n\x1aenable_generative_fallback\x18\x0c \x01(\x08\x12P\n\ngenerators\x18\r \x03(\x0b2<.google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings\x1aN\n\x12SetParameterAction\x12\x11\n\tparameter\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x1a\xa3\x03\n\x10ConditionalCases\x12O\n\x05cases\x18\x01 \x03(\x0b2@.google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases.Case\x1a\xbd\x02\n\x04Case\x12\x11\n\tcondition\x18\x01 \x01(\t\x12b\n\x0ccase_content\x18\x02 \x03(\x0b2L.google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCases.Case.CaseContent\x1a\xbd\x01\n\x0bCaseContent\x12A\n\x07message\x18\x01 \x01(\x0b2..google.cloud.dialogflow.cx.v3.ResponseMessageH\x00\x12W\n\x10additional_cases\x18\x02 \x01(\x0b2;.google.cloud.dialogflow.cx.v3.Fulfillment.ConditionalCasesH\x00B\x12\n\x10cases_or_message\x1a\x97\x02\n\x11GeneratorSettings\x12>\n\tgenerator\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#dialogflow.googleapis.com/Generator\x12k\n\x10input_parameters\x18\x02 \x03(\x0b2Q.google.cloud.dialogflow.cx.v3.Fulfillment.GeneratorSettings.InputParametersEntry\x12\x1d\n\x10output_parameter\x18\x03 \x01(\tB\x03\xe0A\x02\x1a6\n\x14InputParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\xb3\x01\n!com.google.cloud.dialogflow.cx.v3B\x10FulfillmentProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3.fulfillment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.dialogflow.cx.v3B\x10FulfillmentProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3'
    _globals['_FULFILLMENT_GENERATORSETTINGS_INPUTPARAMETERSENTRY']._loaded_options = None
    _globals['_FULFILLMENT_GENERATORSETTINGS_INPUTPARAMETERSENTRY']._serialized_options = b'8\x01'
    _globals['_FULFILLMENT_GENERATORSETTINGS'].fields_by_name['generator']._loaded_options = None
    _globals['_FULFILLMENT_GENERATORSETTINGS'].fields_by_name['generator']._serialized_options = b'\xe0A\x02\xfaA%\n#dialogflow.googleapis.com/Generator'
    _globals['_FULFILLMENT_GENERATORSETTINGS'].fields_by_name['output_parameter']._loaded_options = None
    _globals['_FULFILLMENT_GENERATORSETTINGS'].fields_by_name['output_parameter']._serialized_options = b'\xe0A\x02'
    _globals['_FULFILLMENT'].fields_by_name['webhook']._loaded_options = None
    _globals['_FULFILLMENT'].fields_by_name['webhook']._serialized_options = b'\xfaA#\n!dialogflow.googleapis.com/Webhook'
    _globals['_FULFILLMENT']._serialized_start = 282
    _globals['_FULFILLMENT']._serialized_end = 1625
    _globals['_FULFILLMENT_SETPARAMETERACTION']._serialized_start = 843
    _globals['_FULFILLMENT_SETPARAMETERACTION']._serialized_end = 921
    _globals['_FULFILLMENT_CONDITIONALCASES']._serialized_start = 924
    _globals['_FULFILLMENT_CONDITIONALCASES']._serialized_end = 1343
    _globals['_FULFILLMENT_CONDITIONALCASES_CASE']._serialized_start = 1026
    _globals['_FULFILLMENT_CONDITIONALCASES_CASE']._serialized_end = 1343
    _globals['_FULFILLMENT_CONDITIONALCASES_CASE_CASECONTENT']._serialized_start = 1154
    _globals['_FULFILLMENT_CONDITIONALCASES_CASE_CASECONTENT']._serialized_end = 1343
    _globals['_FULFILLMENT_GENERATORSETTINGS']._serialized_start = 1346
    _globals['_FULFILLMENT_GENERATORSETTINGS']._serialized_end = 1625
    _globals['_FULFILLMENT_GENERATORSETTINGS_INPUTPARAMETERSENTRY']._serialized_start = 1571
    _globals['_FULFILLMENT_GENERATORSETTINGS_INPUTPARAMETERSENTRY']._serialized_end = 1625