"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/bigquery/v2/table_schema.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/bigquery/v2/table_schema.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x94\x01\n\x0bTableSchema\x12:\n\x06fields\x18\x01 \x03(\x0b2*.google.cloud.bigquery.v2.TableFieldSchema\x12I\n\x11foreign_type_info\x18\x03 \x01(\x0b2).google.cloud.bigquery.v2.ForeignTypeInfoB\x03\xe0A\x01"\x96\x01\n\x0fForeignTypeInfo\x12N\n\x0btype_system\x18\x01 \x01(\x0e24.google.cloud.bigquery.v2.ForeignTypeInfo.TypeSystemB\x03\xe0A\x02"3\n\nTypeSystem\x12\x1b\n\x17TYPE_SYSTEM_UNSPECIFIED\x10\x00\x12\x08\n\x04HIVE\x10\x01".\n\x10DataPolicyOption\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01B\x07\n\x05_name"\xe2\x07\n\x10TableFieldSchema\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04type\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04mode\x18\x03 \x01(\tB\x03\xe0A\x01\x12?\n\x06fields\x18\x04 \x03(\x0b2*.google.cloud.bigquery.v2.TableFieldSchemaB\x03\xe0A\x01\x126\n\x0bdescription\x18\x06 \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01\x12R\n\x0bpolicy_tags\x18\t \x01(\x0b28.google.cloud.bigquery.v2.TableFieldSchema.PolicyTagListB\x03\xe0A\x01\x12F\n\rdata_policies\x18\x15 \x03(\x0b2*.google.cloud.bigquery.v2.DataPolicyOptionB\x03\xe0A\x01\x12\x17\n\nmax_length\x18\n \x01(\x03B\x03\xe0A\x01\x12\x16\n\tprecision\x18\x0b \x01(\x03B\x03\xe0A\x01\x12\x12\n\x05scale\x18\x0c \x01(\x03B\x03\xe0A\x01\x12=\n\x13timestamp_precision\x18\x1b \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x01\x12S\n\rrounding_mode\x18\x0f \x01(\x0e27.google.cloud.bigquery.v2.TableFieldSchema.RoundingModeB\x03\xe0A\x01\x124\n\tcollation\x18\r \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01\x12C\n\x18default_value_expression\x18\x0e \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01\x12\\\n\x12range_element_type\x18\x12 \x01(\x0b2;.google.cloud.bigquery.v2.TableFieldSchema.FieldElementTypeB\x03\xe0A\x01\x12$\n\x17foreign_type_definition\x18\x17 \x01(\tB\x03\xe0A\x01\x1a\x1e\n\rPolicyTagList\x12\r\n\x05names\x18\x01 \x03(\t\x1a%\n\x10FieldElementType\x12\x11\n\x04type\x18\x01 \x01(\tB\x03\xe0A\x02"a\n\x0cRoundingMode\x12\x1d\n\x19ROUNDING_MODE_UNSPECIFIED\x10\x00\x12\x1d\n\x19ROUND_HALF_AWAY_FROM_ZERO\x10\x01\x12\x13\n\x0fROUND_HALF_EVEN\x10\x02Bm\n\x1ccom.google.cloud.bigquery.v2B\x10TableSchemaProtoZ;cloud.google.com/go/bigquery/v2/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.table_schema_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x10TableSchemaProtoZ;cloud.google.com/go/bigquery/v2/apiv2/bigquerypb;bigquerypb'
    _globals['_TABLESCHEMA'].fields_by_name['foreign_type_info']._loaded_options = None
    _globals['_TABLESCHEMA'].fields_by_name['foreign_type_info']._serialized_options = b'\xe0A\x01'
    _globals['_FOREIGNTYPEINFO'].fields_by_name['type_system']._loaded_options = None
    _globals['_FOREIGNTYPEINFO'].fields_by_name['type_system']._serialized_options = b'\xe0A\x02'
    _globals['_TABLEFIELDSCHEMA_FIELDELEMENTTYPE'].fields_by_name['type']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA_FIELDELEMENTTYPE'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['name']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['type']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['mode']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['mode']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['fields']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['fields']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['description']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['policy_tags']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['policy_tags']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['data_policies']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['data_policies']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['max_length']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['max_length']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['precision']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['precision']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['scale']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['scale']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['timestamp_precision']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['timestamp_precision']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['rounding_mode']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['rounding_mode']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['collation']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['collation']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['default_value_expression']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['default_value_expression']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['range_element_type']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['range_element_type']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['foreign_type_definition']._loaded_options = None
    _globals['_TABLEFIELDSCHEMA'].fields_by_name['foreign_type_definition']._serialized_options = b'\xe0A\x01'
    _globals['_TABLESCHEMA']._serialized_start = 139
    _globals['_TABLESCHEMA']._serialized_end = 287
    _globals['_FOREIGNTYPEINFO']._serialized_start = 290
    _globals['_FOREIGNTYPEINFO']._serialized_end = 440
    _globals['_FOREIGNTYPEINFO_TYPESYSTEM']._serialized_start = 389
    _globals['_FOREIGNTYPEINFO_TYPESYSTEM']._serialized_end = 440
    _globals['_DATAPOLICYOPTION']._serialized_start = 442
    _globals['_DATAPOLICYOPTION']._serialized_end = 488
    _globals['_TABLEFIELDSCHEMA']._serialized_start = 491
    _globals['_TABLEFIELDSCHEMA']._serialized_end = 1485
    _globals['_TABLEFIELDSCHEMA_POLICYTAGLIST']._serialized_start = 1317
    _globals['_TABLEFIELDSCHEMA_POLICYTAGLIST']._serialized_end = 1347
    _globals['_TABLEFIELDSCHEMA_FIELDELEMENTTYPE']._serialized_start = 1349
    _globals['_TABLEFIELDSCHEMA_FIELDELEMENTTYPE']._serialized_end = 1386
    _globals['_TABLEFIELDSCHEMA_ROUNDINGMODE']._serialized_start = 1388
    _globals['_TABLEFIELDSCHEMA_ROUNDINGMODE']._serialized_end = 1485