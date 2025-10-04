"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/bigquery/v2/external_data_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.bigquery.v2 import decimal_target_types_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_decimal__target__types__pb2
from .....google.cloud.bigquery.v2 import file_set_specification_type_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_file__set__specification__type__pb2
from .....google.cloud.bigquery.v2 import hive_partitioning_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_hive__partitioning__pb2
from .....google.cloud.bigquery.v2 import json_extension_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_json__extension__pb2
from .....google.cloud.bigquery.v2 import map_target_type_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_map__target__type__pb2
from .....google.cloud.bigquery.v2 import table_schema_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_table__schema__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/bigquery/v2/external_data_config.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a3google/cloud/bigquery/v2/decimal_target_types.proto\x1a:google/cloud/bigquery/v2/file_set_specification_type.proto\x1a0google/cloud/bigquery/v2/hive_partitioning.proto\x1a-google/cloud/bigquery/v2/json_extension.proto\x1a.google/cloud/bigquery/v2/map_target_type.proto\x1a+google/cloud/bigquery/v2/table_schema.proto\x1a\x1egoogle/protobuf/wrappers.proto"N\n\x0bAvroOptions\x12?\n\x16use_avro_logical_types\x18\x01 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01"\xd0\x01\n\x0eParquetOptions\x127\n\x0eenum_as_string\x18\x01 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12>\n\x15enable_list_inference\x18\x02 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12E\n\x0fmap_target_type\x18\x03 \x01(\x0e2\'.google.cloud.bigquery.v2.MapTargetTypeB\x03\xe0A\x01"\xed\x03\n\nCsvOptions\x12\x1c\n\x0ffield_delimiter\x18\x01 \x01(\tB\x03\xe0A\x01\x12;\n\x11skip_leading_rows\x18\x02 \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x01\x120\n\x05quote\x18\x03 \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01\x12>\n\x15allow_quoted_newlines\x18\x04 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12:\n\x11allow_jagged_rows\x18\x05 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12\x15\n\x08encoding\x18\x06 \x01(\tB\x03\xe0A\x01\x12J\n!preserve_ascii_control_characters\x18\x07 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x126\n\x0bnull_marker\x18\x08 \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01\x12\x19\n\x0cnull_markers\x18\t \x03(\tB\x03\xe0A\x01\x12 \n\x13source_column_match\x18\n \x01(\tB\x03\xe0A\x01"$\n\x0bJsonOptions\x12\x15\n\x08encoding\x18\x01 \x01(\tB\x03\xe0A\x01"\xfe\x01\n\x0eBigtableColumn\x126\n\x11qualifier_encoded\x18\x01 \x01(\x0b2\x1b.google.protobuf.BytesValue\x126\n\x10qualifier_string\x18\x02 \x01(\x0b2\x1c.google.protobuf.StringValue\x12\x17\n\nfield_name\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04type\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08encoding\x18\x05 \x01(\tB\x03\xe0A\x01\x129\n\x10only_read_latest\x18\x06 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01"\xce\x01\n\x14BigtableColumnFamily\x12\x11\n\tfamily_id\x18\x01 \x01(\t\x12\x11\n\x04type\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08encoding\x18\x03 \x01(\tB\x03\xe0A\x01\x12>\n\x07columns\x18\x04 \x03(\x0b2(.google.cloud.bigquery.v2.BigtableColumnB\x03\xe0A\x01\x129\n\x10only_read_latest\x18\x05 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01"\xb5\x02\n\x0fBigtableOptions\x12L\n\x0fcolumn_families\x18\x01 \x03(\x0b2..google.cloud.bigquery.v2.BigtableColumnFamilyB\x03\xe0A\x01\x12K\n"ignore_unspecified_column_families\x18\x02 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12>\n\x15read_rowkey_as_string\x18\x03 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12G\n\x1eoutput_column_families_as_json\x18\x04 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01"f\n\x13GoogleSheetsOptions\x12;\n\x11skip_leading_rows\x18\x01 \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x01\x12\x12\n\x05range\x18\x02 \x01(\tB\x03\xe0A\x01"\xaf\x0e\n\x19ExternalDataConfiguration\x12\x13\n\x0bsource_uris\x18\x01 \x03(\t\x12J\n\x12file_set_spec_type\x18\x19 \x01(\x0e2).google.cloud.bigquery.v2.FileSetSpecTypeB\x03\xe0A\x01\x12:\n\x06schema\x18\x02 \x01(\x0b2%.google.cloud.bigquery.v2.TableSchemaB\x03\xe0A\x01\x12\x15\n\rsource_format\x18\x03 \x01(\t\x129\n\x0fmax_bad_records\x18\x04 \x01(\x0b2\x1b.google.protobuf.Int32ValueB\x03\xe0A\x01\x12.\n\nautodetect\x18\x05 \x01(\x0b2\x1a.google.protobuf.BoolValue\x12>\n\x15ignore_unknown_values\x18\x06 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12\x18\n\x0bcompression\x18\x07 \x01(\tB\x03\xe0A\x01\x12>\n\x0bcsv_options\x18\x08 \x01(\x0b2$.google.cloud.bigquery.v2.CsvOptionsB\x03\xe0A\x01\x12@\n\x0cjson_options\x18\x1a \x01(\x0b2%.google.cloud.bigquery.v2.JsonOptionsB\x03\xe0A\x01\x12H\n\x10bigtable_options\x18\t \x01(\x0b2).google.cloud.bigquery.v2.BigtableOptionsB\x03\xe0A\x01\x12Q\n\x15google_sheets_options\x18\n \x01(\x0b2-.google.cloud.bigquery.v2.GoogleSheetsOptionsB\x03\xe0A\x01\x12Y\n\x19hive_partitioning_options\x18\r \x01(\x0b21.google.cloud.bigquery.v2.HivePartitioningOptionsB\x03\xe0A\x01\x12\x1a\n\rconnection_id\x18\x0e \x01(\tB\x03\xe0A\x01\x12I\n\x14decimal_target_types\x18\x10 \x03(\x0e2+.google.cloud.bigquery.v2.DecimalTargetType\x12@\n\x0cavro_options\x18\x11 \x01(\x0b2%.google.cloud.bigquery.v2.AvroOptionsB\x03\xe0A\x01\x12D\n\x0ejson_extension\x18\x12 \x01(\x0e2\'.google.cloud.bigquery.v2.JsonExtensionB\x03\xe0A\x01\x12F\n\x0fparquet_options\x18\x13 \x01(\x0b2(.google.cloud.bigquery.v2.ParquetOptionsB\x03\xe0A\x01\x12e\n\x0fobject_metadata\x18\x16 \x01(\x0e2B.google.cloud.bigquery.v2.ExternalDataConfiguration.ObjectMetadataB\x03\xe0A\x01H\x00\x88\x01\x01\x12D\n\x19reference_file_schema_uri\x18\x17 \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01\x12g\n\x13metadata_cache_mode\x18\x18 \x01(\x0e2E.google.cloud.bigquery.v2.ExternalDataConfiguration.MetadataCacheModeB\x03\xe0A\x01\x12\x1b\n\ttime_zone\x18\x1b \x01(\tB\x03\xe0A\x01H\x01\x88\x01\x01\x12\x1d\n\x0bdate_format\x18\x1c \x01(\tB\x03\xe0A\x01H\x02\x88\x01\x01\x12!\n\x0fdatetime_format\x18\x1d \x01(\tB\x03\xe0A\x01H\x03\x88\x01\x01\x12\x1d\n\x0btime_format\x18\x1e \x01(\tB\x03\xe0A\x01H\x04\x88\x01\x01\x12"\n\x10timestamp_format\x18\x1f \x01(\tB\x03\xe0A\x01H\x05\x88\x01\x01\x12"\n\x1atimestamp_target_precision\x18  \x03(\x05"L\n\x0eObjectMetadata\x12\x1f\n\x1bOBJECT_METADATA_UNSPECIFIED\x10\x00\x12\r\n\tDIRECTORY\x10\x01\x12\n\n\x06SIMPLE\x10\x02"S\n\x11MetadataCacheMode\x12#\n\x1fMETADATA_CACHE_MODE_UNSPECIFIED\x10\x00\x12\r\n\tAUTOMATIC\x10\x01\x12\n\n\x06MANUAL\x10\x02B\x12\n\x10_object_metadataB\x0c\n\n_time_zoneB\x0e\n\x0c_date_formatB\x12\n\x10_datetime_formatB\x0e\n\x0c_time_formatB\x13\n\x11_timestamp_formatBt\n\x1ccom.google.cloud.bigquery.v2B\x17ExternalDataConfigProtoZ;cloud.google.com/go/bigquery/v2/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.external_data_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x17ExternalDataConfigProtoZ;cloud.google.com/go/bigquery/v2/apiv2/bigquerypb;bigquerypb'
    _globals['_AVROOPTIONS'].fields_by_name['use_avro_logical_types']._loaded_options = None
    _globals['_AVROOPTIONS'].fields_by_name['use_avro_logical_types']._serialized_options = b'\xe0A\x01'
    _globals['_PARQUETOPTIONS'].fields_by_name['enum_as_string']._loaded_options = None
    _globals['_PARQUETOPTIONS'].fields_by_name['enum_as_string']._serialized_options = b'\xe0A\x01'
    _globals['_PARQUETOPTIONS'].fields_by_name['enable_list_inference']._loaded_options = None
    _globals['_PARQUETOPTIONS'].fields_by_name['enable_list_inference']._serialized_options = b'\xe0A\x01'
    _globals['_PARQUETOPTIONS'].fields_by_name['map_target_type']._loaded_options = None
    _globals['_PARQUETOPTIONS'].fields_by_name['map_target_type']._serialized_options = b'\xe0A\x01'
    _globals['_CSVOPTIONS'].fields_by_name['field_delimiter']._loaded_options = None
    _globals['_CSVOPTIONS'].fields_by_name['field_delimiter']._serialized_options = b'\xe0A\x01'
    _globals['_CSVOPTIONS'].fields_by_name['skip_leading_rows']._loaded_options = None
    _globals['_CSVOPTIONS'].fields_by_name['skip_leading_rows']._serialized_options = b'\xe0A\x01'
    _globals['_CSVOPTIONS'].fields_by_name['quote']._loaded_options = None
    _globals['_CSVOPTIONS'].fields_by_name['quote']._serialized_options = b'\xe0A\x01'
    _globals['_CSVOPTIONS'].fields_by_name['allow_quoted_newlines']._loaded_options = None
    _globals['_CSVOPTIONS'].fields_by_name['allow_quoted_newlines']._serialized_options = b'\xe0A\x01'
    _globals['_CSVOPTIONS'].fields_by_name['allow_jagged_rows']._loaded_options = None
    _globals['_CSVOPTIONS'].fields_by_name['allow_jagged_rows']._serialized_options = b'\xe0A\x01'
    _globals['_CSVOPTIONS'].fields_by_name['encoding']._loaded_options = None
    _globals['_CSVOPTIONS'].fields_by_name['encoding']._serialized_options = b'\xe0A\x01'
    _globals['_CSVOPTIONS'].fields_by_name['preserve_ascii_control_characters']._loaded_options = None
    _globals['_CSVOPTIONS'].fields_by_name['preserve_ascii_control_characters']._serialized_options = b'\xe0A\x01'
    _globals['_CSVOPTIONS'].fields_by_name['null_marker']._loaded_options = None
    _globals['_CSVOPTIONS'].fields_by_name['null_marker']._serialized_options = b'\xe0A\x01'
    _globals['_CSVOPTIONS'].fields_by_name['null_markers']._loaded_options = None
    _globals['_CSVOPTIONS'].fields_by_name['null_markers']._serialized_options = b'\xe0A\x01'
    _globals['_CSVOPTIONS'].fields_by_name['source_column_match']._loaded_options = None
    _globals['_CSVOPTIONS'].fields_by_name['source_column_match']._serialized_options = b'\xe0A\x01'
    _globals['_JSONOPTIONS'].fields_by_name['encoding']._loaded_options = None
    _globals['_JSONOPTIONS'].fields_by_name['encoding']._serialized_options = b'\xe0A\x01'
    _globals['_BIGTABLECOLUMN'].fields_by_name['field_name']._loaded_options = None
    _globals['_BIGTABLECOLUMN'].fields_by_name['field_name']._serialized_options = b'\xe0A\x01'
    _globals['_BIGTABLECOLUMN'].fields_by_name['type']._loaded_options = None
    _globals['_BIGTABLECOLUMN'].fields_by_name['type']._serialized_options = b'\xe0A\x01'
    _globals['_BIGTABLECOLUMN'].fields_by_name['encoding']._loaded_options = None
    _globals['_BIGTABLECOLUMN'].fields_by_name['encoding']._serialized_options = b'\xe0A\x01'
    _globals['_BIGTABLECOLUMN'].fields_by_name['only_read_latest']._loaded_options = None
    _globals['_BIGTABLECOLUMN'].fields_by_name['only_read_latest']._serialized_options = b'\xe0A\x01'
    _globals['_BIGTABLECOLUMNFAMILY'].fields_by_name['type']._loaded_options = None
    _globals['_BIGTABLECOLUMNFAMILY'].fields_by_name['type']._serialized_options = b'\xe0A\x01'
    _globals['_BIGTABLECOLUMNFAMILY'].fields_by_name['encoding']._loaded_options = None
    _globals['_BIGTABLECOLUMNFAMILY'].fields_by_name['encoding']._serialized_options = b'\xe0A\x01'
    _globals['_BIGTABLECOLUMNFAMILY'].fields_by_name['columns']._loaded_options = None
    _globals['_BIGTABLECOLUMNFAMILY'].fields_by_name['columns']._serialized_options = b'\xe0A\x01'
    _globals['_BIGTABLECOLUMNFAMILY'].fields_by_name['only_read_latest']._loaded_options = None
    _globals['_BIGTABLECOLUMNFAMILY'].fields_by_name['only_read_latest']._serialized_options = b'\xe0A\x01'
    _globals['_BIGTABLEOPTIONS'].fields_by_name['column_families']._loaded_options = None
    _globals['_BIGTABLEOPTIONS'].fields_by_name['column_families']._serialized_options = b'\xe0A\x01'
    _globals['_BIGTABLEOPTIONS'].fields_by_name['ignore_unspecified_column_families']._loaded_options = None
    _globals['_BIGTABLEOPTIONS'].fields_by_name['ignore_unspecified_column_families']._serialized_options = b'\xe0A\x01'
    _globals['_BIGTABLEOPTIONS'].fields_by_name['read_rowkey_as_string']._loaded_options = None
    _globals['_BIGTABLEOPTIONS'].fields_by_name['read_rowkey_as_string']._serialized_options = b'\xe0A\x01'
    _globals['_BIGTABLEOPTIONS'].fields_by_name['output_column_families_as_json']._loaded_options = None
    _globals['_BIGTABLEOPTIONS'].fields_by_name['output_column_families_as_json']._serialized_options = b'\xe0A\x01'
    _globals['_GOOGLESHEETSOPTIONS'].fields_by_name['skip_leading_rows']._loaded_options = None
    _globals['_GOOGLESHEETSOPTIONS'].fields_by_name['skip_leading_rows']._serialized_options = b'\xe0A\x01'
    _globals['_GOOGLESHEETSOPTIONS'].fields_by_name['range']._loaded_options = None
    _globals['_GOOGLESHEETSOPTIONS'].fields_by_name['range']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['file_set_spec_type']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['file_set_spec_type']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['schema']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['schema']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['max_bad_records']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['max_bad_records']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['ignore_unknown_values']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['ignore_unknown_values']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['compression']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['compression']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['csv_options']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['csv_options']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['json_options']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['json_options']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['bigtable_options']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['bigtable_options']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['google_sheets_options']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['google_sheets_options']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['hive_partitioning_options']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['hive_partitioning_options']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['connection_id']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['connection_id']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['avro_options']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['avro_options']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['json_extension']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['json_extension']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['parquet_options']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['parquet_options']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['object_metadata']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['object_metadata']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['reference_file_schema_uri']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['reference_file_schema_uri']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['metadata_cache_mode']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['metadata_cache_mode']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['time_zone']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['date_format']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['date_format']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['datetime_format']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['datetime_format']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['time_format']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['time_format']._serialized_options = b'\xe0A\x01'
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['timestamp_format']._loaded_options = None
    _globals['_EXTERNALDATACONFIGURATION'].fields_by_name['timestamp_format']._serialized_options = b'\xe0A\x01'
    _globals['_AVROOPTIONS']._serialized_start = 449
    _globals['_AVROOPTIONS']._serialized_end = 527
    _globals['_PARQUETOPTIONS']._serialized_start = 530
    _globals['_PARQUETOPTIONS']._serialized_end = 738
    _globals['_CSVOPTIONS']._serialized_start = 741
    _globals['_CSVOPTIONS']._serialized_end = 1234
    _globals['_JSONOPTIONS']._serialized_start = 1236
    _globals['_JSONOPTIONS']._serialized_end = 1272
    _globals['_BIGTABLECOLUMN']._serialized_start = 1275
    _globals['_BIGTABLECOLUMN']._serialized_end = 1529
    _globals['_BIGTABLECOLUMNFAMILY']._serialized_start = 1532
    _globals['_BIGTABLECOLUMNFAMILY']._serialized_end = 1738
    _globals['_BIGTABLEOPTIONS']._serialized_start = 1741
    _globals['_BIGTABLEOPTIONS']._serialized_end = 2050
    _globals['_GOOGLESHEETSOPTIONS']._serialized_start = 2052
    _globals['_GOOGLESHEETSOPTIONS']._serialized_end = 2154
    _globals['_EXTERNALDATACONFIGURATION']._serialized_start = 2157
    _globals['_EXTERNALDATACONFIGURATION']._serialized_end = 3996
    _globals['_EXTERNALDATACONFIGURATION_OBJECTMETADATA']._serialized_start = 3728
    _globals['_EXTERNALDATACONFIGURATION_OBJECTMETADATA']._serialized_end = 3804
    _globals['_EXTERNALDATACONFIGURATION_METADATACACHEMODE']._serialized_start = 3806
    _globals['_EXTERNALDATACONFIGURATION_METADATACACHEMODE']._serialized_end = 3889