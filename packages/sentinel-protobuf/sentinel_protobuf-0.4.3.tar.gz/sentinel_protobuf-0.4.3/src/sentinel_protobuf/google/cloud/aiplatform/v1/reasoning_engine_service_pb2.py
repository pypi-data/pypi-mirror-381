"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/reasoning_engine_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_operation__pb2
from .....google.cloud.aiplatform.v1 import reasoning_engine_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_reasoning__engine__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/aiplatform/v1/reasoning_engine_service.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/cloud/aiplatform/v1/operation.proto\x1a1google/cloud/aiplatform/v1/reasoning_engine.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xa5\x01\n\x1cCreateReasoningEngineRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12J\n\x10reasoning_engine\x18\x02 \x01(\x0b2+.google.cloud.aiplatform.v1.ReasoningEngineB\x03\xe0A\x02"x\n&CreateReasoningEngineOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata"\\\n\x19GetReasoningEngineRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine"\xa0\x01\n\x1cUpdateReasoningEngineRequest\x12J\n\x10reasoning_engine\x18\x01 \x01(\x0b2+.google.cloud.aiplatform.v1.ReasoningEngineB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"x\n&UpdateReasoningEngineOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata"\x9e\x01\n\x1bListReasoningEnginesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01"\x7f\n\x1cListReasoningEnginesResponse\x12F\n\x11reasoning_engines\x18\x01 \x03(\x0b2+.google.cloud.aiplatform.v1.ReasoningEngine\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"s\n\x1cDeleteReasoningEngineRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine\x12\x12\n\x05force\x18\x02 \x01(\x08B\x03\xe0A\x012\xaf\n\n\x16ReasoningEngineService\x12\x97\x02\n\x15CreateReasoningEngine\x128.google.cloud.aiplatform.v1.CreateReasoningEngineRequest\x1a\x1d.google.longrunning.Operation"\xa4\x01\xcaA9\n\x0fReasoningEngine\x12&CreateReasoningEngineOperationMetadata\xdaA\x17parent,reasoning_engine\x82\xd3\xe4\x93\x02H"4/v1/{parent=projects/*/locations/*}/reasoningEngines:\x10reasoning_engine\x12\xbd\x01\n\x12GetReasoningEngine\x125.google.cloud.aiplatform.v1.GetReasoningEngineRequest\x1a+.google.cloud.aiplatform.v1.ReasoningEngine"C\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v1/{name=projects/*/locations/*/reasoningEngines/*}\x12\xd0\x01\n\x14ListReasoningEngines\x127.google.cloud.aiplatform.v1.ListReasoningEnginesRequest\x1a8.google.cloud.aiplatform.v1.ListReasoningEnginesResponse"E\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v1/{parent=projects/*/locations/*}/reasoningEngines\x12\xad\x02\n\x15UpdateReasoningEngine\x128.google.cloud.aiplatform.v1.UpdateReasoningEngineRequest\x1a\x1d.google.longrunning.Operation"\xba\x01\xcaA9\n\x0fReasoningEngine\x12&UpdateReasoningEngineOperationMetadata\xdaA\x1creasoning_engine,update_mask\x82\xd3\xe4\x93\x02Y2E/v1/{reasoning_engine.name=projects/*/locations/*/reasoningEngines/*}:\x10reasoning_engine\x12\xe8\x01\n\x15DeleteReasoningEngine\x128.google.cloud.aiplatform.v1.DeleteReasoningEngineRequest\x1a\x1d.google.longrunning.Operation"v\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x026*4/v1/{name=projects/*/locations/*/reasoningEngines/*}\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd9\x01\n\x1ecom.google.cloud.aiplatform.v1B\x1bReasoningEngineServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.reasoning_engine_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x1bReasoningEngineServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_CREATEREASONINGENGINEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEREASONINGENGINEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEREASONINGENGINEREQUEST'].fields_by_name['reasoning_engine']._loaded_options = None
    _globals['_CREATEREASONINGENGINEREQUEST'].fields_by_name['reasoning_engine']._serialized_options = b'\xe0A\x02'
    _globals['_GETREASONINGENGINEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETREASONINGENGINEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine'
    _globals['_UPDATEREASONINGENGINEREQUEST'].fields_by_name['reasoning_engine']._loaded_options = None
    _globals['_UPDATEREASONINGENGINEREQUEST'].fields_by_name['reasoning_engine']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEREASONINGENGINEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEREASONINGENGINEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_LISTREASONINGENGINESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTREASONINGENGINESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTREASONINGENGINESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTREASONINGENGINESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTREASONINGENGINESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTREASONINGENGINESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTREASONINGENGINESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTREASONINGENGINESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEREASONINGENGINEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEREASONINGENGINEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine'
    _globals['_DELETEREASONINGENGINEREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETEREASONINGENGINEREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x01'
    _globals['_REASONINGENGINESERVICE']._loaded_options = None
    _globals['_REASONINGENGINESERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_REASONINGENGINESERVICE'].methods_by_name['CreateReasoningEngine']._loaded_options = None
    _globals['_REASONINGENGINESERVICE'].methods_by_name['CreateReasoningEngine']._serialized_options = b'\xcaA9\n\x0fReasoningEngine\x12&CreateReasoningEngineOperationMetadata\xdaA\x17parent,reasoning_engine\x82\xd3\xe4\x93\x02H"4/v1/{parent=projects/*/locations/*}/reasoningEngines:\x10reasoning_engine'
    _globals['_REASONINGENGINESERVICE'].methods_by_name['GetReasoningEngine']._loaded_options = None
    _globals['_REASONINGENGINESERVICE'].methods_by_name['GetReasoningEngine']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v1/{name=projects/*/locations/*/reasoningEngines/*}'
    _globals['_REASONINGENGINESERVICE'].methods_by_name['ListReasoningEngines']._loaded_options = None
    _globals['_REASONINGENGINESERVICE'].methods_by_name['ListReasoningEngines']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v1/{parent=projects/*/locations/*}/reasoningEngines'
    _globals['_REASONINGENGINESERVICE'].methods_by_name['UpdateReasoningEngine']._loaded_options = None
    _globals['_REASONINGENGINESERVICE'].methods_by_name['UpdateReasoningEngine']._serialized_options = b'\xcaA9\n\x0fReasoningEngine\x12&UpdateReasoningEngineOperationMetadata\xdaA\x1creasoning_engine,update_mask\x82\xd3\xe4\x93\x02Y2E/v1/{reasoning_engine.name=projects/*/locations/*/reasoningEngines/*}:\x10reasoning_engine'
    _globals['_REASONINGENGINESERVICE'].methods_by_name['DeleteReasoningEngine']._loaded_options = None
    _globals['_REASONINGENGINESERVICE'].methods_by_name['DeleteReasoningEngine']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x026*4/v1/{name=projects/*/locations/*/reasoningEngines/*}'
    _globals['_CREATEREASONINGENGINEREQUEST']._serialized_start = 400
    _globals['_CREATEREASONINGENGINEREQUEST']._serialized_end = 565
    _globals['_CREATEREASONINGENGINEOPERATIONMETADATA']._serialized_start = 567
    _globals['_CREATEREASONINGENGINEOPERATIONMETADATA']._serialized_end = 687
    _globals['_GETREASONINGENGINEREQUEST']._serialized_start = 689
    _globals['_GETREASONINGENGINEREQUEST']._serialized_end = 781
    _globals['_UPDATEREASONINGENGINEREQUEST']._serialized_start = 784
    _globals['_UPDATEREASONINGENGINEREQUEST']._serialized_end = 944
    _globals['_UPDATEREASONINGENGINEOPERATIONMETADATA']._serialized_start = 946
    _globals['_UPDATEREASONINGENGINEOPERATIONMETADATA']._serialized_end = 1066
    _globals['_LISTREASONINGENGINESREQUEST']._serialized_start = 1069
    _globals['_LISTREASONINGENGINESREQUEST']._serialized_end = 1227
    _globals['_LISTREASONINGENGINESRESPONSE']._serialized_start = 1229
    _globals['_LISTREASONINGENGINESRESPONSE']._serialized_end = 1356
    _globals['_DELETEREASONINGENGINEREQUEST']._serialized_start = 1358
    _globals['_DELETEREASONINGENGINEREQUEST']._serialized_end = 1473
    _globals['_REASONINGENGINESERVICE']._serialized_start = 1476
    _globals['_REASONINGENGINESERVICE']._serialized_end = 2803