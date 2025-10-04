"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ai/generativelanguage/v1beta2/model_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ai.generativelanguage.v1beta2 import model_pb2 as google_dot_ai_dot_generativelanguage_dot_v1beta2_dot_model__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ai/generativelanguage/v1beta2/model_service.proto\x12$google.ai.generativelanguage.v1beta2\x1a0google/ai/generativelanguage/v1beta2/model.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"P\n\x0fGetModelRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'generativelanguage.googleapis.com/Model":\n\x11ListModelsRequest\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"j\n\x12ListModelsResponse\x12;\n\x06models\x18\x01 \x03(\x0b2+.google.ai.generativelanguage.v1beta2.Model\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x80\x03\n\x0cModelService\x12\x97\x01\n\x08GetModel\x125.google.ai.generativelanguage.v1beta2.GetModelRequest\x1a+.google.ai.generativelanguage.v1beta2.Model"\'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1a\x12\x18/v1beta2/{name=models/*}\x12\xaf\x01\n\nListModels\x127.google.ai.generativelanguage.v1beta2.ListModelsRequest\x1a8.google.ai.generativelanguage.v1beta2.ListModelsResponse".\xdaA\x14page_size,page_token\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1beta2/models\x1a$\xcaA!generativelanguage.googleapis.comB\x9f\x01\n(com.google.ai.generativelanguage.v1beta2B\x11ModelServiceProtoP\x01Z^cloud.google.com/go/ai/generativelanguage/apiv1beta2/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1beta2.model_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ai.generativelanguage.v1beta2B\x11ModelServiceProtoP\x01Z^cloud.google.com/go/ai/generativelanguage/apiv1beta2/generativelanguagepb;generativelanguagepb'
    _globals['_GETMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMODELREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'generativelanguage.googleapis.com/Model"
    _globals['_MODELSERVICE']._loaded_options = None
    _globals['_MODELSERVICE']._serialized_options = b'\xcaA!generativelanguage.googleapis.com'
    _globals['_MODELSERVICE'].methods_by_name['GetModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['GetModel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1a\x12\x18/v1beta2/{name=models/*}'
    _globals['_MODELSERVICE'].methods_by_name['ListModels']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ListModels']._serialized_options = b'\xdaA\x14page_size,page_token\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1beta2/models'
    _globals['_GETMODELREQUEST']._serialized_start = 263
    _globals['_GETMODELREQUEST']._serialized_end = 343
    _globals['_LISTMODELSREQUEST']._serialized_start = 345
    _globals['_LISTMODELSREQUEST']._serialized_end = 403
    _globals['_LISTMODELSRESPONSE']._serialized_start = 405
    _globals['_LISTMODELSRESPONSE']._serialized_end = 511
    _globals['_MODELSERVICE']._serialized_start = 514
    _globals['_MODELSERVICE']._serialized_end = 898