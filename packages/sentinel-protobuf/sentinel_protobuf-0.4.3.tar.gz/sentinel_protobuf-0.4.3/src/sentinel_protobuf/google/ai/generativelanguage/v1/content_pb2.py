"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ai/generativelanguage/v1/content.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/ai/generativelanguage/v1/content.proto\x12\x1fgoogle.ai.generativelanguage.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/protobuf/duration.proto"R\n\x07Content\x124\n\x05parts\x18\x01 \x03(\x0b2%.google.ai.generativelanguage.v1.Part\x12\x11\n\x04role\x18\x02 \x01(\tB\x03\xe0A\x01"\xb7\x01\n\x04Part\x12\x0e\n\x04text\x18\x02 \x01(\tH\x00\x12<\n\x0binline_data\x18\x03 \x01(\x0b2%.google.ai.generativelanguage.v1.BlobH\x00\x12M\n\x0evideo_metadata\x18\x0e \x01(\x0b2..google.ai.generativelanguage.v1.VideoMetadataB\x03\xe0A\x01H\x01B\x06\n\x04dataB\n\n\x08metadata"\'\n\x04Blob\x12\x11\n\tmime_type\x18\x01 \x01(\t\x12\x0c\n\x04data\x18\x02 \x01(\x0c"\x8b\x01\n\rVideoMetadata\x124\n\x0cstart_offset\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x122\n\nend_offset\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x12\x10\n\x03fps\x18\x03 \x01(\x01B\x03\xe0A\x01"f\n\x12ModalityTokenCount\x12;\n\x08modality\x18\x01 \x01(\x0e2).google.ai.generativelanguage.v1.Modality\x12\x13\n\x0btoken_count\x18\x02 \x01(\x05*]\n\x08Modality\x12\x18\n\x14MODALITY_UNSPECIFIED\x10\x00\x12\x08\n\x04TEXT\x10\x01\x12\t\n\x05IMAGE\x10\x02\x12\t\n\x05VIDEO\x10\x03\x12\t\n\x05AUDIO\x10\x04\x12\x0c\n\x08DOCUMENT\x10\x05B\x90\x01\n#com.google.ai.generativelanguage.v1B\x0cContentProtoP\x01ZYcloud.google.com/go/ai/generativelanguage/apiv1/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1.content_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ai.generativelanguage.v1B\x0cContentProtoP\x01ZYcloud.google.com/go/ai/generativelanguage/apiv1/generativelanguagepb;generativelanguagepb'
    _globals['_CONTENT'].fields_by_name['role']._loaded_options = None
    _globals['_CONTENT'].fields_by_name['role']._serialized_options = b'\xe0A\x01'
    _globals['_PART'].fields_by_name['video_metadata']._loaded_options = None
    _globals['_PART'].fields_by_name['video_metadata']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOMETADATA'].fields_by_name['start_offset']._loaded_options = None
    _globals['_VIDEOMETADATA'].fields_by_name['start_offset']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOMETADATA'].fields_by_name['end_offset']._loaded_options = None
    _globals['_VIDEOMETADATA'].fields_by_name['end_offset']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOMETADATA'].fields_by_name['fps']._loaded_options = None
    _globals['_VIDEOMETADATA'].fields_by_name['fps']._serialized_options = b'\xe0A\x01'
    _globals['_MODALITY']._serialized_start = 704
    _globals['_MODALITY']._serialized_end = 797
    _globals['_CONTENT']._serialized_start = 147
    _globals['_CONTENT']._serialized_end = 229
    _globals['_PART']._serialized_start = 232
    _globals['_PART']._serialized_end = 415
    _globals['_BLOB']._serialized_start = 417
    _globals['_BLOB']._serialized_end = 456
    _globals['_VIDEOMETADATA']._serialized_start = 459
    _globals['_VIDEOMETADATA']._serialized_end = 598
    _globals['_MODALITYTOKENCOUNT']._serialized_start = 600
    _globals['_MODALITYTOKENCOUNT']._serialized_end = 702