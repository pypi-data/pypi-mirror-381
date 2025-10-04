"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ai/generativelanguage/v1/model_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ai.generativelanguage.v1 import model_pb2 as google_dot_ai_dot_generativelanguage_dot_v1_dot_model__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/ai/generativelanguage/v1/model_service.proto\x12\x1fgoogle.ai.generativelanguage.v1\x1a+google/ai/generativelanguage/v1/model.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"P\n\x0fGetModelRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'generativelanguage.googleapis.com/Model":\n\x11ListModelsRequest\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"e\n\x12ListModelsResponse\x126\n\x06models\x18\x01 \x03(\x0b2&.google.ai.generativelanguage.v1.Model\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xe2\x02\n\x0cModelService\x12\x88\x01\n\x08GetModel\x120.google.ai.generativelanguage.v1.GetModelRequest\x1a&.google.ai.generativelanguage.v1.Model""\xdaA\x04name\x82\xd3\xe4\x93\x02\x15\x12\x13/v1/{name=models/*}\x12\xa0\x01\n\nListModels\x122.google.ai.generativelanguage.v1.ListModelsRequest\x1a3.google.ai.generativelanguage.v1.ListModelsResponse")\xdaA\x14page_size,page_token\x82\xd3\xe4\x93\x02\x0c\x12\n/v1/models\x1a$\xcaA!generativelanguage.googleapis.comB\x95\x01\n#com.google.ai.generativelanguage.v1B\x11ModelServiceProtoP\x01ZYcloud.google.com/go/ai/generativelanguage/apiv1/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1.model_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ai.generativelanguage.v1B\x11ModelServiceProtoP\x01ZYcloud.google.com/go/ai/generativelanguage/apiv1/generativelanguagepb;generativelanguagepb'
    _globals['_GETMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMODELREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'generativelanguage.googleapis.com/Model"
    _globals['_MODELSERVICE']._loaded_options = None
    _globals['_MODELSERVICE']._serialized_options = b'\xcaA!generativelanguage.googleapis.com'
    _globals['_MODELSERVICE'].methods_by_name['GetModel']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['GetModel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x15\x12\x13/v1/{name=models/*}'
    _globals['_MODELSERVICE'].methods_by_name['ListModels']._loaded_options = None
    _globals['_MODELSERVICE'].methods_by_name['ListModels']._serialized_options = b'\xdaA\x14page_size,page_token\x82\xd3\xe4\x93\x02\x0c\x12\n/v1/models'
    _globals['_GETMODELREQUEST']._serialized_start = 248
    _globals['_GETMODELREQUEST']._serialized_end = 328
    _globals['_LISTMODELSREQUEST']._serialized_start = 330
    _globals['_LISTMODELSREQUEST']._serialized_end = 388
    _globals['_LISTMODELSRESPONSE']._serialized_start = 390
    _globals['_LISTMODELSRESPONSE']._serialized_end = 491
    _globals['_MODELSERVICE']._serialized_start = 494
    _globals['_MODELSERVICE']._serialized_end = 848