"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ai/generativelanguage/v1alpha/retriever.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/ai/generativelanguage/v1alpha/retriever.proto\x12$google.ai.generativelanguage.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf7\x01\n\x06Corpus\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x08\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:P\xeaAM\n(generativelanguage.googleapis.com/Corpus\x12\x10corpora/{corpus}*\x07corpora2\x06corpus"\xe8\x02\n\x08Document\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x08\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x01\x12R\n\x0fcustom_metadata\x18\x03 \x03(\x0b24.google.ai.generativelanguage.v1alpha.CustomMetadataB\x03\xe0A\x01\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:k\xeaAh\n*generativelanguage.googleapis.com/Document\x12%corpora/{corpus}/documents/{document}*\tdocuments2\x08document"\x1c\n\nStringList\x12\x0e\n\x06values\x18\x01 \x03(\t"\xab\x01\n\x0eCustomMetadata\x12\x16\n\x0cstring_value\x18\x02 \x01(\tH\x00\x12M\n\x11string_list_value\x18\x06 \x01(\x0b20.google.ai.generativelanguage.v1alpha.StringListH\x00\x12\x17\n\rnumeric_value\x18\x07 \x01(\x02H\x00\x12\x10\n\x03key\x18\x01 \x01(\tB\x03\xe0A\x02B\x07\n\x05value"l\n\x0eMetadataFilter\x12\x10\n\x03key\x18\x01 \x01(\tB\x03\xe0A\x02\x12H\n\nconditions\x18\x02 \x03(\x0b2/.google.ai.generativelanguage.v1alpha.ConditionB\x03\xe0A\x02"\xae\x02\n\tCondition\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x12\x17\n\rnumeric_value\x18\x06 \x01(\x02H\x00\x12P\n\toperation\x18\x05 \x01(\x0e28.google.ai.generativelanguage.v1alpha.Condition.OperatorB\x03\xe0A\x02"\x94\x01\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\x08\n\x04LESS\x10\x01\x12\x0e\n\nLESS_EQUAL\x10\x02\x12\t\n\x05EQUAL\x10\x03\x12\x11\n\rGREATER_EQUAL\x10\x04\x12\x0b\n\x07GREATER\x10\x05\x12\r\n\tNOT_EQUAL\x10\x06\x12\x0c\n\x08INCLUDES\x10\x07\x12\x0c\n\x08EXCLUDES\x10\x08B\x07\n\x05value"\xbd\x04\n\x05Chunk\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x08\xe0A\x05\x12B\n\x04data\x18\x02 \x01(\x0b2/.google.ai.generativelanguage.v1alpha.ChunkDataB\x03\xe0A\x02\x12R\n\x0fcustom_metadata\x18\x03 \x03(\x0b24.google.ai.generativelanguage.v1alpha.CustomMetadataB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12E\n\x05state\x18\x06 \x01(\x0e21.google.ai.generativelanguage.v1alpha.Chunk.StateB\x03\xe0A\x03"`\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x1c\n\x18STATE_PENDING_PROCESSING\x10\x01\x12\x10\n\x0cSTATE_ACTIVE\x10\x02\x12\x10\n\x0cSTATE_FAILED\x10\n:q\xeaAn\n\'generativelanguage.googleapis.com/Chunk\x124corpora/{corpus}/documents/{document}/chunks/{chunk}*\x06chunks2\x05chunk"+\n\tChunkData\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00B\x06\n\x04dataB\x9c\x01\n(com.google.ai.generativelanguage.v1alphaB\x0eRetrieverProtoP\x01Z^cloud.google.com/go/ai/generativelanguage/apiv1alpha/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1alpha.retriever_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ai.generativelanguage.v1alphaB\x0eRetrieverProtoP\x01Z^cloud.google.com/go/ai/generativelanguage/apiv1alpha/generativelanguagepb;generativelanguagepb'
    _globals['_CORPUS'].fields_by_name['name']._loaded_options = None
    _globals['_CORPUS'].fields_by_name['name']._serialized_options = b'\xe0A\x08\xe0A\x05'
    _globals['_CORPUS'].fields_by_name['display_name']._loaded_options = None
    _globals['_CORPUS'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_CORPUS'].fields_by_name['create_time']._loaded_options = None
    _globals['_CORPUS'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CORPUS'].fields_by_name['update_time']._loaded_options = None
    _globals['_CORPUS'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CORPUS']._loaded_options = None
    _globals['_CORPUS']._serialized_options = b'\xeaAM\n(generativelanguage.googleapis.com/Corpus\x12\x10corpora/{corpus}*\x07corpora2\x06corpus'
    _globals['_DOCUMENT'].fields_by_name['name']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['name']._serialized_options = b'\xe0A\x08\xe0A\x05'
    _globals['_DOCUMENT'].fields_by_name['display_name']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_DOCUMENT'].fields_by_name['custom_metadata']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['custom_metadata']._serialized_options = b'\xe0A\x01'
    _globals['_DOCUMENT'].fields_by_name['update_time']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_DOCUMENT'].fields_by_name['create_time']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DOCUMENT']._loaded_options = None
    _globals['_DOCUMENT']._serialized_options = b'\xeaAh\n*generativelanguage.googleapis.com/Document\x12%corpora/{corpus}/documents/{document}*\tdocuments2\x08document'
    _globals['_CUSTOMMETADATA'].fields_by_name['key']._loaded_options = None
    _globals['_CUSTOMMETADATA'].fields_by_name['key']._serialized_options = b'\xe0A\x02'
    _globals['_METADATAFILTER'].fields_by_name['key']._loaded_options = None
    _globals['_METADATAFILTER'].fields_by_name['key']._serialized_options = b'\xe0A\x02'
    _globals['_METADATAFILTER'].fields_by_name['conditions']._loaded_options = None
    _globals['_METADATAFILTER'].fields_by_name['conditions']._serialized_options = b'\xe0A\x02'
    _globals['_CONDITION'].fields_by_name['operation']._loaded_options = None
    _globals['_CONDITION'].fields_by_name['operation']._serialized_options = b'\xe0A\x02'
    _globals['_CHUNK'].fields_by_name['name']._loaded_options = None
    _globals['_CHUNK'].fields_by_name['name']._serialized_options = b'\xe0A\x08\xe0A\x05'
    _globals['_CHUNK'].fields_by_name['data']._loaded_options = None
    _globals['_CHUNK'].fields_by_name['data']._serialized_options = b'\xe0A\x02'
    _globals['_CHUNK'].fields_by_name['custom_metadata']._loaded_options = None
    _globals['_CHUNK'].fields_by_name['custom_metadata']._serialized_options = b'\xe0A\x01'
    _globals['_CHUNK'].fields_by_name['create_time']._loaded_options = None
    _globals['_CHUNK'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CHUNK'].fields_by_name['update_time']._loaded_options = None
    _globals['_CHUNK'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CHUNK'].fields_by_name['state']._loaded_options = None
    _globals['_CHUNK'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_CHUNK']._loaded_options = None
    _globals['_CHUNK']._serialized_options = b"\xeaAn\n'generativelanguage.googleapis.com/Chunk\x124corpora/{corpus}/documents/{document}/chunks/{chunk}*\x06chunks2\x05chunk"
    _globals['_CORPUS']._serialized_start = 188
    _globals['_CORPUS']._serialized_end = 435
    _globals['_DOCUMENT']._serialized_start = 438
    _globals['_DOCUMENT']._serialized_end = 798
    _globals['_STRINGLIST']._serialized_start = 800
    _globals['_STRINGLIST']._serialized_end = 828
    _globals['_CUSTOMMETADATA']._serialized_start = 831
    _globals['_CUSTOMMETADATA']._serialized_end = 1002
    _globals['_METADATAFILTER']._serialized_start = 1004
    _globals['_METADATAFILTER']._serialized_end = 1112
    _globals['_CONDITION']._serialized_start = 1115
    _globals['_CONDITION']._serialized_end = 1417
    _globals['_CONDITION_OPERATOR']._serialized_start = 1260
    _globals['_CONDITION_OPERATOR']._serialized_end = 1408
    _globals['_CHUNK']._serialized_start = 1420
    _globals['_CHUNK']._serialized_end = 1993
    _globals['_CHUNK_STATE']._serialized_start = 1782
    _globals['_CHUNK_STATE']._serialized_end = 1878
    _globals['_CHUNKDATA']._serialized_start = 1995
    _globals['_CHUNKDATA']._serialized_end = 2038