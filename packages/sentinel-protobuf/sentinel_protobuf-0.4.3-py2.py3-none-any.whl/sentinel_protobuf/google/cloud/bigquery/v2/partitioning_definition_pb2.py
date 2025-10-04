"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/bigquery/v2/partitioning_definition.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/bigquery/v2/partitioning_definition.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto"f\n\x16PartitioningDefinition\x12L\n\x12partitioned_column\x18\x01 \x03(\x0b2+.google.cloud.bigquery.v2.PartitionedColumnB\x03\xe0A\x01"6\n\x11PartitionedColumn\x12\x17\n\x05field\x18\x01 \x01(\tB\x03\xe0A\x02H\x00\x88\x01\x01B\x08\n\x06_fieldBz\n\x1ccom.google.cloud.bigquery.v2B\x1bPartitioningDefinitionProtoP\x01Z;cloud.google.com/go/bigquery/v2/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.partitioning_definition_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x1bPartitioningDefinitionProtoP\x01Z;cloud.google.com/go/bigquery/v2/apiv2/bigquerypb;bigquerypb'
    _globals['_PARTITIONINGDEFINITION'].fields_by_name['partitioned_column']._loaded_options = None
    _globals['_PARTITIONINGDEFINITION'].fields_by_name['partitioned_column']._serialized_options = b'\xe0A\x01'
    _globals['_PARTITIONEDCOLUMN'].fields_by_name['field']._loaded_options = None
    _globals['_PARTITIONEDCOLUMN'].fields_by_name['field']._serialized_options = b'\xe0A\x02'
    _globals['_PARTITIONINGDEFINITION']._serialized_start = 117
    _globals['_PARTITIONINGDEFINITION']._serialized_end = 219
    _globals['_PARTITIONEDCOLUMN']._serialized_start = 221
    _globals['_PARTITIONEDCOLUMN']._serialized_end = 275