"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ai/generativelanguage/v1beta/citation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/ai/generativelanguage/v1beta/citation.proto\x12#google.ai.generativelanguage.v1beta\x1a\x1fgoogle/api/field_behavior.proto"a\n\x10CitationMetadata\x12M\n\x10citation_sources\x18\x01 \x03(\x0b23.google.ai.generativelanguage.v1beta.CitationSource"\xb0\x01\n\x0eCitationSource\x12\x1d\n\x0bstart_index\x18\x01 \x01(\x05B\x03\xe0A\x01H\x00\x88\x01\x01\x12\x1b\n\tend_index\x18\x02 \x01(\x05B\x03\xe0A\x01H\x01\x88\x01\x01\x12\x15\n\x03uri\x18\x03 \x01(\tB\x03\xe0A\x01H\x02\x88\x01\x01\x12\x19\n\x07license\x18\x04 \x01(\tB\x03\xe0A\x01H\x03\x88\x01\x01B\x0e\n\x0c_start_indexB\x0c\n\n_end_indexB\x06\n\x04_uriB\n\n\x08_licenseB\x99\x01\n\'com.google.ai.generativelanguage.v1betaB\rCitationProtoP\x01Z]cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1beta.citation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.ai.generativelanguage.v1betaB\rCitationProtoP\x01Z]cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb;generativelanguagepb"
    _globals['_CITATIONSOURCE'].fields_by_name['start_index']._loaded_options = None
    _globals['_CITATIONSOURCE'].fields_by_name['start_index']._serialized_options = b'\xe0A\x01'
    _globals['_CITATIONSOURCE'].fields_by_name['end_index']._loaded_options = None
    _globals['_CITATIONSOURCE'].fields_by_name['end_index']._serialized_options = b'\xe0A\x01'
    _globals['_CITATIONSOURCE'].fields_by_name['uri']._loaded_options = None
    _globals['_CITATIONSOURCE'].fields_by_name['uri']._serialized_options = b'\xe0A\x01'
    _globals['_CITATIONSOURCE'].fields_by_name['license']._loaded_options = None
    _globals['_CITATIONSOURCE'].fields_by_name['license']._serialized_options = b'\xe0A\x01'
    _globals['_CITATIONMETADATA']._serialized_start = 124
    _globals['_CITATIONMETADATA']._serialized_end = 221
    _globals['_CITATIONSOURCE']._serialized_start = 224
    _globals['_CITATIONSOURCE']._serialized_end = 400