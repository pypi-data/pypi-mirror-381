"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ai/generativelanguage/v1beta2/model.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/ai/generativelanguage/v1beta2/model.proto\x12$google.ai.generativelanguage.v1beta2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xf8\x02\n\x05Model\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rbase_model_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07version\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x14\n\x0cdisplay_name\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t\x12\x19\n\x11input_token_limit\x18\x06 \x01(\x05\x12\x1a\n\x12output_token_limit\x18\x07 \x01(\x05\x12$\n\x1csupported_generation_methods\x18\x08 \x03(\t\x12\x18\n\x0btemperature\x18\t \x01(\x02H\x00\x88\x01\x01\x12\x12\n\x05top_p\x18\n \x01(\x02H\x01\x88\x01\x01\x12\x12\n\x05top_k\x18\x0b \x01(\x05H\x02\x88\x01\x01:<\xeaA9\n\'generativelanguage.googleapis.com/Model\x12\x0emodels/{model}B\x0e\n\x0c_temperatureB\x08\n\x06_top_pB\x08\n\x06_top_kB\x98\x01\n(com.google.ai.generativelanguage.v1beta2B\nModelProtoP\x01Z^cloud.google.com/go/ai/generativelanguage/apiv1beta2/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1beta2.model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ai.generativelanguage.v1beta2B\nModelProtoP\x01Z^cloud.google.com/go/ai/generativelanguage/apiv1beta2/generativelanguagepb;generativelanguagepb'
    _globals['_MODEL'].fields_by_name['name']._loaded_options = None
    _globals['_MODEL'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_MODEL'].fields_by_name['base_model_id']._loaded_options = None
    _globals['_MODEL'].fields_by_name['base_model_id']._serialized_options = b'\xe0A\x02'
    _globals['_MODEL'].fields_by_name['version']._loaded_options = None
    _globals['_MODEL'].fields_by_name['version']._serialized_options = b'\xe0A\x02'
    _globals['_MODEL']._loaded_options = None
    _globals['_MODEL']._serialized_options = b"\xeaA9\n'generativelanguage.googleapis.com/Model\x12\x0emodels/{model}"
    _globals['_MODEL']._serialized_start = 151
    _globals['_MODEL']._serialized_end = 527