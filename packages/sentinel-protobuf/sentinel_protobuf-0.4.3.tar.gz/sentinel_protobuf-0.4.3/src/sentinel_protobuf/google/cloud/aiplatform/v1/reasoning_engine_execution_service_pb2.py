"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/reasoning_engine_execution_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/cloud/aiplatform/v1/reasoning_engine_execution_service.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/httpbody.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto"\xa6\x01\n\x1bQueryReasoningEngineRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine\x12+\n\x05input\x18\x02 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x12\x19\n\x0cclass_method\x18\x03 \x01(\tB\x03\xe0A\x01"F\n\x1cQueryReasoningEngineResponse\x12&\n\x06output\x18\x01 \x01(\x0b2\x16.google.protobuf.Value"\xac\x01\n!StreamQueryReasoningEngineRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine\x12+\n\x05input\x18\x02 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x12\x19\n\x0cclass_method\x18\x03 \x01(\tB\x03\xe0A\x012\x86\x04\n\x1fReasoningEngineExecutionService\x12\xd0\x01\n\x14QueryReasoningEngine\x127.google.cloud.aiplatform.v1.QueryReasoningEngineRequest\x1a8.google.cloud.aiplatform.v1.QueryReasoningEngineResponse"E\x82\xd3\xe4\x93\x02?":/v1/{name=projects/*/locations/*/reasoningEngines/*}:query:\x01*\x12\xc0\x01\n\x1aStreamQueryReasoningEngine\x12=.google.cloud.aiplatform.v1.StreamQueryReasoningEngineRequest\x1a\x14.google.api.HttpBody"K\x82\xd3\xe4\x93\x02E"@/v1/{name=projects/*/locations/*/reasoningEngines/*}:streamQuery:\x01*0\x01\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe2\x01\n\x1ecom.google.cloud.aiplatform.v1B$ReasoningEngineExecutionServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.reasoning_engine_execution_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B$ReasoningEngineExecutionServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_QUERYREASONINGENGINEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_QUERYREASONINGENGINEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine'
    _globals['_QUERYREASONINGENGINEREQUEST'].fields_by_name['input']._loaded_options = None
    _globals['_QUERYREASONINGENGINEREQUEST'].fields_by_name['input']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYREASONINGENGINEREQUEST'].fields_by_name['class_method']._loaded_options = None
    _globals['_QUERYREASONINGENGINEREQUEST'].fields_by_name['class_method']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMQUERYREASONINGENGINEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STREAMQUERYREASONINGENGINEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine'
    _globals['_STREAMQUERYREASONINGENGINEREQUEST'].fields_by_name['input']._loaded_options = None
    _globals['_STREAMQUERYREASONINGENGINEREQUEST'].fields_by_name['input']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMQUERYREASONINGENGINEREQUEST'].fields_by_name['class_method']._loaded_options = None
    _globals['_STREAMQUERYREASONINGENGINEREQUEST'].fields_by_name['class_method']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINEEXECUTIONSERVICE']._loaded_options = None
    _globals['_REASONINGENGINEEXECUTIONSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_REASONINGENGINEEXECUTIONSERVICE'].methods_by_name['QueryReasoningEngine']._loaded_options = None
    _globals['_REASONINGENGINEEXECUTIONSERVICE'].methods_by_name['QueryReasoningEngine']._serialized_options = b'\x82\xd3\xe4\x93\x02?":/v1/{name=projects/*/locations/*/reasoningEngines/*}:query:\x01*'
    _globals['_REASONINGENGINEEXECUTIONSERVICE'].methods_by_name['StreamQueryReasoningEngine']._loaded_options = None
    _globals['_REASONINGENGINEEXECUTIONSERVICE'].methods_by_name['StreamQueryReasoningEngine']._serialized_options = b'\x82\xd3\xe4\x93\x02E"@/v1/{name=projects/*/locations/*/reasoningEngines/*}:streamQuery:\x01*'
    _globals['_QUERYREASONINGENGINEREQUEST']._serialized_start = 272
    _globals['_QUERYREASONINGENGINEREQUEST']._serialized_end = 438
    _globals['_QUERYREASONINGENGINERESPONSE']._serialized_start = 440
    _globals['_QUERYREASONINGENGINERESPONSE']._serialized_end = 510
    _globals['_STREAMQUERYREASONINGENGINEREQUEST']._serialized_start = 513
    _globals['_STREAMQUERYREASONINGENGINEREQUEST']._serialized_end = 685
    _globals['_REASONINGENGINEEXECUTIONSERVICE']._serialized_start = 688
    _globals['_REASONINGENGINEEXECUTIONSERVICE']._serialized_end = 1206