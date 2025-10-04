"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/bigquery/v2/data_format_options.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/bigquery/v2/data_format_options.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto"\x8c\x02\n\x11DataFormatOptions\x12 \n\x13use_int64_timestamp\x18\x01 \x01(\x08B\x03\xe0A\x01\x12g\n\x17timestamp_output_format\x18\x03 \x01(\x0e2A.google.cloud.bigquery.v2.DataFormatOptions.TimestampOutputFormatB\x03\xe0A\x01"l\n\x15TimestampOutputFormat\x12\'\n#TIMESTAMP_OUTPUT_FORMAT_UNSPECIFIED\x10\x00\x12\x0b\n\x07FLOAT64\x10\x01\x12\t\n\x05INT64\x10\x02\x12\x12\n\x0eISO8601_STRING\x10\x03Bs\n\x1ccom.google.cloud.bigquery.v2B\x16DataFormatOptionsProtoZ;cloud.google.com/go/bigquery/v2/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.data_format_options_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x16DataFormatOptionsProtoZ;cloud.google.com/go/bigquery/v2/apiv2/bigquerypb;bigquerypb'
    _globals['_DATAFORMATOPTIONS'].fields_by_name['use_int64_timestamp']._loaded_options = None
    _globals['_DATAFORMATOPTIONS'].fields_by_name['use_int64_timestamp']._serialized_options = b'\xe0A\x01'
    _globals['_DATAFORMATOPTIONS'].fields_by_name['timestamp_output_format']._loaded_options = None
    _globals['_DATAFORMATOPTIONS'].fields_by_name['timestamp_output_format']._serialized_options = b'\xe0A\x01'
    _globals['_DATAFORMATOPTIONS']._serialized_start = 114
    _globals['_DATAFORMATOPTIONS']._serialized_end = 382
    _globals['_DATAFORMATOPTIONS_TIMESTAMPOUTPUTFORMAT']._serialized_start = 274
    _globals['_DATAFORMATOPTIONS_TIMESTAMPOUTPUTFORMAT']._serialized_end = 382