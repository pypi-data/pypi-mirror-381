"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2/safety.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/cloud/retail/v2/safety.proto\x12\x16google.cloud.retail.v2\x1a\x1fgoogle/api/field_behavior.proto"\xd5\x03\n\rSafetySetting\x126\n\x08category\x18\x01 \x01(\x0e2$.google.cloud.retail.v2.HarmCategory\x12K\n\tthreshold\x18\x02 \x01(\x0e28.google.cloud.retail.v2.SafetySetting.HarmBlockThreshold\x12J\n\x06method\x18\x03 \x01(\x0e25.google.cloud.retail.v2.SafetySetting.HarmBlockMethodB\x03\xe0A\x01"\x9d\x01\n\x12HarmBlockThreshold\x12$\n HARM_BLOCK_THRESHOLD_UNSPECIFIED\x10\x00\x12\x17\n\x13BLOCK_LOW_AND_ABOVE\x10\x01\x12\x1a\n\x16BLOCK_MEDIUM_AND_ABOVE\x10\x02\x12\x13\n\x0fBLOCK_ONLY_HIGH\x10\x03\x12\x0e\n\nBLOCK_NONE\x10\x04\x12\x07\n\x03OFF\x10\x05"S\n\x0fHarmBlockMethod\x12!\n\x1dHARM_BLOCK_METHOD_UNSPECIFIED\x10\x00\x12\x0c\n\x08SEVERITY\x10\x01\x12\x0f\n\x0bPROBABILITY\x10\x02*\xd7\x01\n\x0cHarmCategory\x12\x1d\n\x19HARM_CATEGORY_UNSPECIFIED\x10\x00\x12\x1d\n\x19HARM_CATEGORY_HATE_SPEECH\x10\x01\x12#\n\x1fHARM_CATEGORY_DANGEROUS_CONTENT\x10\x02\x12\x1c\n\x18HARM_CATEGORY_HARASSMENT\x10\x03\x12#\n\x1fHARM_CATEGORY_SEXUALLY_EXPLICIT\x10\x04\x12!\n\x1dHARM_CATEGORY_CIVIC_INTEGRITY\x10\x05B\xb6\x01\n\x1acom.google.cloud.retail.v2B\x0bSafetyProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2.safety_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.retail.v2B\x0bSafetyProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2'
    _globals['_SAFETYSETTING'].fields_by_name['method']._loaded_options = None
    _globals['_SAFETYSETTING'].fields_by_name['method']._serialized_options = b'\xe0A\x01'
    _globals['_HARMCATEGORY']._serialized_start = 569
    _globals['_HARMCATEGORY']._serialized_end = 784
    _globals['_SAFETYSETTING']._serialized_start = 97
    _globals['_SAFETYSETTING']._serialized_end = 566
    _globals['_SAFETYSETTING_HARMBLOCKTHRESHOLD']._serialized_start = 324
    _globals['_SAFETYSETTING_HARMBLOCKTHRESHOLD']._serialized_end = 481
    _globals['_SAFETYSETTING_HARMBLOCKMETHOD']._serialized_start = 483
    _globals['_SAFETYSETTING_HARMBLOCKMETHOD']._serialized_end = 566