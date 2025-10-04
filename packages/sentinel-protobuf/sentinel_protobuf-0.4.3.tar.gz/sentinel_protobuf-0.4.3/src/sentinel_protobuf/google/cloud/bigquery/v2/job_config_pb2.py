"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/bigquery/v2/job_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.bigquery.v2 import clustering_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_clustering__pb2
from .....google.cloud.bigquery.v2 import dataset_reference_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_dataset__reference__pb2
from .....google.cloud.bigquery.v2 import decimal_target_types_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_decimal__target__types__pb2
from .....google.cloud.bigquery.v2 import encryption_config_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_encryption__config__pb2
from .....google.cloud.bigquery.v2 import external_data_config_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_external__data__config__pb2
from .....google.cloud.bigquery.v2 import file_set_specification_type_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_file__set__specification__type__pb2
from .....google.cloud.bigquery.v2 import hive_partitioning_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_hive__partitioning__pb2
from .....google.cloud.bigquery.v2 import json_extension_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_json__extension__pb2
from .....google.cloud.bigquery.v2 import model_reference_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_model__reference__pb2
from .....google.cloud.bigquery.v2 import query_parameter_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_query__parameter__pb2
from .....google.cloud.bigquery.v2 import range_partitioning_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_range__partitioning__pb2
from .....google.cloud.bigquery.v2 import system_variable_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_system__variable__pb2
from .....google.cloud.bigquery.v2 import table_reference_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_table__reference__pb2
from .....google.cloud.bigquery.v2 import table_schema_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_table__schema__pb2
from .....google.cloud.bigquery.v2 import time_partitioning_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_time__partitioning__pb2
from .....google.cloud.bigquery.v2 import udf_resource_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_udf__resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/bigquery/v2/job_config.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/bigquery/v2/clustering.proto\x1a0google/cloud/bigquery/v2/dataset_reference.proto\x1a3google/cloud/bigquery/v2/decimal_target_types.proto\x1a0google/cloud/bigquery/v2/encryption_config.proto\x1a3google/cloud/bigquery/v2/external_data_config.proto\x1a:google/cloud/bigquery/v2/file_set_specification_type.proto\x1a0google/cloud/bigquery/v2/hive_partitioning.proto\x1a-google/cloud/bigquery/v2/json_extension.proto\x1a.google/cloud/bigquery/v2/model_reference.proto\x1a.google/cloud/bigquery/v2/query_parameter.proto\x1a1google/cloud/bigquery/v2/range_partitioning.proto\x1a.google/cloud/bigquery/v2/system_variable.proto\x1a.google/cloud/bigquery/v2/table_reference.proto\x1a+google/cloud/bigquery/v2/table_schema.proto\x1a0google/cloud/bigquery/v2/time_partitioning.proto\x1a+google/cloud/bigquery/v2/udf_resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x94\x02\n\x1aDestinationTableProperties\x128\n\rfriendly_name\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01\x126\n\x0bdescription\x18\x02 \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01\x12U\n\x06labels\x18\x03 \x03(\x0b2@.google.cloud.bigquery.v2.DestinationTableProperties.LabelsEntryB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"0\n\x12ConnectionProperty\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t"\xc2\r\n\x15JobConfigurationQuery\x12\r\n\x05query\x18\x01 \x01(\t\x12H\n\x11destination_table\x18\x02 \x01(\x0b2(.google.cloud.bigquery.v2.TableReferenceB\x03\xe0A\x01\x12\x88\x01\n\x1aexternal_table_definitions\x18\x17 \x03(\x0b2M.google.cloud.bigquery.v2.JobConfigurationQuery.ExternalTableDefinitionsEntryB\x03\xe0A\x01R\x10tableDefinitions\x12^\n\x1fuser_defined_function_resources\x18\x04 \x03(\x0b25.google.cloud.bigquery.v2.UserDefinedFunctionResource\x12\x1f\n\x12create_disposition\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x1e\n\x11write_disposition\x18\x06 \x01(\tB\x03\xe0A\x01\x12H\n\x0fdefault_dataset\x18\x07 \x01(\x0b2*.google.cloud.bigquery.v2.DatasetReferenceB\x03\xe0A\x01\x12\x15\n\x08priority\x18\x08 \x01(\tB\x03\xe0A\x01\x12<\n\x13allow_large_results\x18\n \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x128\n\x0fuse_query_cache\x18\x0b \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x128\n\x0fflatten_results\x18\x0c \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x129\n\x14maximum_bytes_billed\x18\x0e \x01(\x0b2\x1b.google.protobuf.Int64Value\x127\n\x0euse_legacy_sql\x18\x0f \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12\x16\n\x0eparameter_mode\x18\x10 \x01(\t\x12B\n\x10query_parameters\x18\x11 \x03(\x0b2(.google.cloud.bigquery.v2.QueryParameter\x12M\n\x10system_variables\x18# \x01(\x0b2).google.cloud.bigquery.v2.SystemVariablesB\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1d\n\x15schema_update_options\x18\x12 \x03(\t\x12E\n\x11time_partitioning\x18\x13 \x01(\x0b2*.google.cloud.bigquery.v2.TimePartitioning\x12G\n\x12range_partitioning\x18\x16 \x01(\x0b2+.google.cloud.bigquery.v2.RangePartitioning\x128\n\nclustering\x18\x14 \x01(\x0b2$.google.cloud.bigquery.v2.Clustering\x12_\n$destination_encryption_configuration\x18\x15 \x01(\x0b21.google.cloud.bigquery.v2.EncryptionConfiguration\x12?\n\x0escript_options\x18\x18 \x01(\x0b2\'.google.cloud.bigquery.v2.ScriptOptions\x12K\n\x15connection_properties\x18! \x03(\x0b2,.google.cloud.bigquery.v2.ConnectionProperty\x122\n\x0ecreate_session\x18" \x01(\x0b2\x1a.google.protobuf.BoolValue\x123\n\ncontinuous\x18$ \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12&\n\x19write_incremental_results\x18% \x01(\x08B\x03\xe0A\x01\x1at\n\x1dExternalTableDefinitionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12B\n\x05value\x18\x02 \x01(\x0b23.google.cloud.bigquery.v2.ExternalDataConfiguration:\x028\x01B\x13\n\x11_system_variables"\xc5\x02\n\rScriptOptions\x129\n\x14statement_timeout_ms\x18\x01 \x01(\x0b2\x1b.google.protobuf.Int64Value\x12:\n\x15statement_byte_budget\x18\x02 \x01(\x0b2\x1b.google.protobuf.Int64Value\x12\\\n\x14key_result_statement\x18\x04 \x01(\x0e2>.google.cloud.bigquery.v2.ScriptOptions.KeyResultStatementKind"_\n\x16KeyResultStatementKind\x12)\n%KEY_RESULT_STATEMENT_KIND_UNSPECIFIED\x10\x00\x12\x08\n\x04LAST\x10\x01\x12\x10\n\x0cFIRST_SELECT\x10\x02"\xb3\x15\n\x14JobConfigurationLoad\x12\x13\n\x0bsource_uris\x18\x01 \x03(\t\x12J\n\x12file_set_spec_type\x181 \x01(\x0e2).google.cloud.bigquery.v2.FileSetSpecTypeB\x03\xe0A\x01\x12:\n\x06schema\x18\x02 \x01(\x0b2%.google.cloud.bigquery.v2.TableSchemaB\x03\xe0A\x01\x12C\n\x11destination_table\x18\x03 \x01(\x0b2(.google.cloud.bigquery.v2.TableReference\x12_\n\x1cdestination_table_properties\x18\x04 \x01(\x0b24.google.cloud.bigquery.v2.DestinationTablePropertiesB\x03\xe0A\x01\x12\x1f\n\x12create_disposition\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x1e\n\x11write_disposition\x18\x06 \x01(\tB\x03\xe0A\x01\x126\n\x0bnull_marker\x18\x07 \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01\x12\x1c\n\x0ffield_delimiter\x18\x08 \x01(\tB\x03\xe0A\x01\x12;\n\x11skip_leading_rows\x18\t \x01(\x0b2\x1b.google.protobuf.Int32ValueB\x03\xe0A\x01\x12\x15\n\x08encoding\x18\n \x01(\tB\x03\xe0A\x01\x120\n\x05quote\x18\x0b \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01\x129\n\x0fmax_bad_records\x18\x0c \x01(\x0b2\x1b.google.protobuf.Int32ValueB\x03\xe0A\x01\x129\n\x15allow_quoted_newlines\x18\x0f \x01(\x0b2\x1a.google.protobuf.BoolValue\x12\x1a\n\rsource_format\x18\x10 \x01(\tB\x03\xe0A\x01\x12:\n\x11allow_jagged_rows\x18\x11 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12>\n\x15ignore_unknown_values\x18\x12 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12\x19\n\x11projection_fields\x18\x13 \x03(\t\x123\n\nautodetect\x18\x14 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12\x1d\n\x15schema_update_options\x18\x15 \x03(\t\x12E\n\x11time_partitioning\x18\x16 \x01(\x0b2*.google.cloud.bigquery.v2.TimePartitioning\x12G\n\x12range_partitioning\x18\x1a \x01(\x0b2+.google.cloud.bigquery.v2.RangePartitioning\x128\n\nclustering\x18\x17 \x01(\x0b2$.google.cloud.bigquery.v2.Clustering\x12_\n$destination_encryption_configuration\x18\x18 \x01(\x0b21.google.cloud.bigquery.v2.EncryptionConfiguration\x12?\n\x16use_avro_logical_types\x18\x19 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12D\n\x19reference_file_schema_uri\x18- \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01\x12Y\n\x19hive_partitioning_options\x18% \x01(\x0b21.google.cloud.bigquery.v2.HivePartitioningOptionsB\x03\xe0A\x01\x12I\n\x14decimal_target_types\x18\' \x03(\x0e2+.google.cloud.bigquery.v2.DecimalTargetType\x12D\n\x0ejson_extension\x18) \x01(\x0e2\'.google.cloud.bigquery.v2.JsonExtensionB\x03\xe0A\x01\x12F\n\x0fparquet_options\x18* \x01(\x0b2(.google.cloud.bigquery.v2.ParquetOptionsB\x03\xe0A\x01\x12J\n!preserve_ascii_control_characters\x18, \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12P\n\x15connection_properties\x18. \x03(\x0b2,.google.cloud.bigquery.v2.ConnectionPropertyB\x03\xe0A\x01\x127\n\x0ecreate_session\x18/ \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12m\n\x19column_name_character_map\x182 \x01(\x0e2E.google.cloud.bigquery.v2.JobConfigurationLoad.ColumnNameCharacterMapB\x03\xe0A\x01\x128\n\x0fcopy_files_only\x183 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x124\n\ttime_zone\x184 \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01\x12\x19\n\x0cnull_markers\x185 \x03(\tB\x03\xe0A\x01\x12\x1d\n\x0bdate_format\x186 \x01(\tB\x03\xe0A\x01H\x00\x88\x01\x01\x12!\n\x0fdatetime_format\x187 \x01(\tB\x03\xe0A\x01H\x01\x88\x01\x01\x12\x1d\n\x0btime_format\x188 \x01(\tB\x03\xe0A\x01H\x02\x88\x01\x01\x12"\n\x10timestamp_format\x189 \x01(\tB\x03\xe0A\x01H\x03\x88\x01\x01\x12b\n\x13source_column_match\x18: \x01(\x0e2@.google.cloud.bigquery.v2.JobConfigurationLoad.SourceColumnMatchB\x03\xe0A\x01\x12"\n\x1atimestamp_target_precision\x18; \x03(\x05"_\n\x16ColumnNameCharacterMap\x12)\n%COLUMN_NAME_CHARACTER_MAP_UNSPECIFIED\x10\x00\x12\n\n\x06STRICT\x10\x01\x12\x06\n\x02V1\x10\x02\x12\x06\n\x02V2\x10\x03"P\n\x11SourceColumnMatch\x12#\n\x1fSOURCE_COLUMN_MATCH_UNSPECIFIED\x10\x00\x12\x0c\n\x08POSITION\x10\x01\x12\x08\n\x04NAME\x10\x02B\x0e\n\x0c_date_formatB\x12\n\x10_datetime_formatB\x0e\n\x0c_time_formatB\x13\n\x11_timestamp_format"\x8a\x05\n\x19JobConfigurationTableCopy\x12>\n\x0csource_table\x18\x01 \x01(\x0b2(.google.cloud.bigquery.v2.TableReference\x12?\n\rsource_tables\x18\x02 \x03(\x0b2(.google.cloud.bigquery.v2.TableReference\x12C\n\x11destination_table\x18\x03 \x01(\x0b2(.google.cloud.bigquery.v2.TableReference\x12\x1f\n\x12create_disposition\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x1e\n\x11write_disposition\x18\x05 \x01(\tB\x03\xe0A\x01\x12_\n$destination_encryption_configuration\x18\x06 \x01(\x0b21.google.cloud.bigquery.v2.EncryptionConfiguration\x12^\n\x0eoperation_type\x18\x08 \x01(\x0e2A.google.cloud.bigquery.v2.JobConfigurationTableCopy.OperationTypeB\x03\xe0A\x01\x12D\n\x1bdestination_expiration_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01"_\n\rOperationType\x12\x1e\n\x1aOPERATION_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04COPY\x10\x01\x12\x0c\n\x08SNAPSHOT\x10\x02\x12\x0b\n\x07RESTORE\x10\x03\x12\t\n\x05CLONE\x10\x04"\xbe\x04\n\x17JobConfigurationExtract\x12@\n\x0csource_table\x18\x01 \x01(\x0b2(.google.cloud.bigquery.v2.TableReferenceH\x00\x12@\n\x0csource_model\x18\t \x01(\x0b2(.google.cloud.bigquery.v2.ModelReferenceH\x00\x12\x18\n\x10destination_uris\x18\x03 \x03(\t\x125\n\x0cprint_header\x18\x04 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12\x1c\n\x0ffield_delimiter\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x1f\n\x12destination_format\x18\x06 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bcompression\x18\x07 \x01(\tB\x03\xe0A\x01\x12:\n\x16use_avro_logical_types\x18\r \x01(\x0b2\x1a.google.protobuf.BoolValue\x12i\n\x15model_extract_options\x18\x0e \x01(\x0b2E.google.cloud.bigquery.v2.JobConfigurationExtract.ModelExtractOptionsB\x03\xe0A\x01\x1aD\n\x13ModelExtractOptions\x12-\n\x08trial_id\x18\x01 \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x08\n\x06source"\x99\x05\n\x10JobConfiguration\x12\x10\n\x08job_type\x18\x08 \x01(\t\x12>\n\x05query\x18\x01 \x01(\x0b2/.google.cloud.bigquery.v2.JobConfigurationQuery\x12<\n\x04load\x18\x02 \x01(\x0b2..google.cloud.bigquery.v2.JobConfigurationLoad\x12A\n\x04copy\x18\x03 \x01(\x0b23.google.cloud.bigquery.v2.JobConfigurationTableCopy\x12B\n\x07extract\x18\x04 \x01(\x0b21.google.cloud.bigquery.v2.JobConfigurationExtract\x120\n\x07dry_run\x18\x05 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x128\n\x0ejob_timeout_ms\x18\x06 \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x01\x12\x1b\n\tmax_slots\x18\x0c \x01(\x05B\x03\xe0A\x01H\x00\x88\x01\x01\x12F\n\x06labels\x18\x07 \x03(\x0b26.google.cloud.bigquery.v2.JobConfiguration.LabelsEntry\x12P\n\x0breservation\x18\x0b \x01(\tB6\xe0A\x01\xfaA0\n.bigqueryreservation.googleapis.com/ReservationH\x01\x88\x01\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x0c\n\n_max_slotsB\x0e\n\x0c_reservationBk\n\x1ccom.google.cloud.bigquery.v2B\x0eJobConfigProtoZ;cloud.google.com/go/bigquery/v2/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.job_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x0eJobConfigProtoZ;cloud.google.com/go/bigquery/v2/apiv2/bigquerypb;bigquerypb'
    _globals['_DESTINATIONTABLEPROPERTIES_LABELSENTRY']._loaded_options = None
    _globals['_DESTINATIONTABLEPROPERTIES_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_DESTINATIONTABLEPROPERTIES'].fields_by_name['friendly_name']._loaded_options = None
    _globals['_DESTINATIONTABLEPROPERTIES'].fields_by_name['friendly_name']._serialized_options = b'\xe0A\x01'
    _globals['_DESTINATIONTABLEPROPERTIES'].fields_by_name['description']._loaded_options = None
    _globals['_DESTINATIONTABLEPROPERTIES'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_DESTINATIONTABLEPROPERTIES'].fields_by_name['labels']._loaded_options = None
    _globals['_DESTINATIONTABLEPROPERTIES'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONQUERY_EXTERNALTABLEDEFINITIONSENTRY']._loaded_options = None
    _globals['_JOBCONFIGURATIONQUERY_EXTERNALTABLEDEFINITIONSENTRY']._serialized_options = b'8\x01'
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['destination_table']._loaded_options = None
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['destination_table']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['external_table_definitions']._loaded_options = None
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['external_table_definitions']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['create_disposition']._loaded_options = None
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['create_disposition']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['write_disposition']._loaded_options = None
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['write_disposition']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['default_dataset']._loaded_options = None
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['default_dataset']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['priority']._loaded_options = None
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['priority']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['allow_large_results']._loaded_options = None
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['allow_large_results']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['use_query_cache']._loaded_options = None
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['use_query_cache']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['flatten_results']._loaded_options = None
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['flatten_results']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['use_legacy_sql']._loaded_options = None
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['use_legacy_sql']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['system_variables']._loaded_options = None
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['system_variables']._serialized_options = b'\xe0A\x03'
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['continuous']._loaded_options = None
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['continuous']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['write_incremental_results']._loaded_options = None
    _globals['_JOBCONFIGURATIONQUERY'].fields_by_name['write_incremental_results']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['file_set_spec_type']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['file_set_spec_type']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['schema']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['schema']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['destination_table_properties']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['destination_table_properties']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['create_disposition']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['create_disposition']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['write_disposition']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['write_disposition']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['null_marker']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['null_marker']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['field_delimiter']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['field_delimiter']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['skip_leading_rows']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['skip_leading_rows']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['encoding']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['encoding']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['quote']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['quote']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['max_bad_records']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['max_bad_records']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['source_format']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['source_format']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['allow_jagged_rows']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['allow_jagged_rows']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['ignore_unknown_values']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['ignore_unknown_values']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['autodetect']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['autodetect']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['use_avro_logical_types']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['use_avro_logical_types']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['reference_file_schema_uri']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['reference_file_schema_uri']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['hive_partitioning_options']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['hive_partitioning_options']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['json_extension']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['json_extension']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['parquet_options']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['parquet_options']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['preserve_ascii_control_characters']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['preserve_ascii_control_characters']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['connection_properties']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['connection_properties']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['create_session']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['create_session']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['column_name_character_map']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['column_name_character_map']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['copy_files_only']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['copy_files_only']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['time_zone']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['null_markers']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['null_markers']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['date_format']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['date_format']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['datetime_format']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['datetime_format']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['time_format']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['time_format']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['timestamp_format']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['timestamp_format']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['source_column_match']._loaded_options = None
    _globals['_JOBCONFIGURATIONLOAD'].fields_by_name['source_column_match']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONTABLECOPY'].fields_by_name['create_disposition']._loaded_options = None
    _globals['_JOBCONFIGURATIONTABLECOPY'].fields_by_name['create_disposition']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONTABLECOPY'].fields_by_name['write_disposition']._loaded_options = None
    _globals['_JOBCONFIGURATIONTABLECOPY'].fields_by_name['write_disposition']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONTABLECOPY'].fields_by_name['operation_type']._loaded_options = None
    _globals['_JOBCONFIGURATIONTABLECOPY'].fields_by_name['operation_type']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONTABLECOPY'].fields_by_name['destination_expiration_time']._loaded_options = None
    _globals['_JOBCONFIGURATIONTABLECOPY'].fields_by_name['destination_expiration_time']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONEXTRACT'].fields_by_name['print_header']._loaded_options = None
    _globals['_JOBCONFIGURATIONEXTRACT'].fields_by_name['print_header']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONEXTRACT'].fields_by_name['field_delimiter']._loaded_options = None
    _globals['_JOBCONFIGURATIONEXTRACT'].fields_by_name['field_delimiter']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONEXTRACT'].fields_by_name['destination_format']._loaded_options = None
    _globals['_JOBCONFIGURATIONEXTRACT'].fields_by_name['destination_format']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONEXTRACT'].fields_by_name['compression']._loaded_options = None
    _globals['_JOBCONFIGURATIONEXTRACT'].fields_by_name['compression']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATIONEXTRACT'].fields_by_name['model_extract_options']._loaded_options = None
    _globals['_JOBCONFIGURATIONEXTRACT'].fields_by_name['model_extract_options']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATION_LABELSENTRY']._loaded_options = None
    _globals['_JOBCONFIGURATION_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_JOBCONFIGURATION'].fields_by_name['dry_run']._loaded_options = None
    _globals['_JOBCONFIGURATION'].fields_by_name['dry_run']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATION'].fields_by_name['job_timeout_ms']._loaded_options = None
    _globals['_JOBCONFIGURATION'].fields_by_name['job_timeout_ms']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATION'].fields_by_name['max_slots']._loaded_options = None
    _globals['_JOBCONFIGURATION'].fields_by_name['max_slots']._serialized_options = b'\xe0A\x01'
    _globals['_JOBCONFIGURATION'].fields_by_name['reservation']._loaded_options = None
    _globals['_JOBCONFIGURATION'].fields_by_name['reservation']._serialized_options = b'\xe0A\x01\xfaA0\n.bigqueryreservation.googleapis.com/Reservation'
    _globals['_DESTINATIONTABLEPROPERTIES']._serialized_start = 986
    _globals['_DESTINATIONTABLEPROPERTIES']._serialized_end = 1262
    _globals['_DESTINATIONTABLEPROPERTIES_LABELSENTRY']._serialized_start = 1217
    _globals['_DESTINATIONTABLEPROPERTIES_LABELSENTRY']._serialized_end = 1262
    _globals['_CONNECTIONPROPERTY']._serialized_start = 1264
    _globals['_CONNECTIONPROPERTY']._serialized_end = 1312
    _globals['_JOBCONFIGURATIONQUERY']._serialized_start = 1315
    _globals['_JOBCONFIGURATIONQUERY']._serialized_end = 3045
    _globals['_JOBCONFIGURATIONQUERY_EXTERNALTABLEDEFINITIONSENTRY']._serialized_start = 2908
    _globals['_JOBCONFIGURATIONQUERY_EXTERNALTABLEDEFINITIONSENTRY']._serialized_end = 3024
    _globals['_SCRIPTOPTIONS']._serialized_start = 3048
    _globals['_SCRIPTOPTIONS']._serialized_end = 3373
    _globals['_SCRIPTOPTIONS_KEYRESULTSTATEMENTKIND']._serialized_start = 3278
    _globals['_SCRIPTOPTIONS_KEYRESULTSTATEMENTKIND']._serialized_end = 3373
    _globals['_JOBCONFIGURATIONLOAD']._serialized_start = 3376
    _globals['_JOBCONFIGURATIONLOAD']._serialized_end = 6115
    _globals['_JOBCONFIGURATIONLOAD_COLUMNNAMECHARACTERMAP']._serialized_start = 5865
    _globals['_JOBCONFIGURATIONLOAD_COLUMNNAMECHARACTERMAP']._serialized_end = 5960
    _globals['_JOBCONFIGURATIONLOAD_SOURCECOLUMNMATCH']._serialized_start = 5962
    _globals['_JOBCONFIGURATIONLOAD_SOURCECOLUMNMATCH']._serialized_end = 6042
    _globals['_JOBCONFIGURATIONTABLECOPY']._serialized_start = 6118
    _globals['_JOBCONFIGURATIONTABLECOPY']._serialized_end = 6768
    _globals['_JOBCONFIGURATIONTABLECOPY_OPERATIONTYPE']._serialized_start = 6673
    _globals['_JOBCONFIGURATIONTABLECOPY_OPERATIONTYPE']._serialized_end = 6768
    _globals['_JOBCONFIGURATIONEXTRACT']._serialized_start = 6771
    _globals['_JOBCONFIGURATIONEXTRACT']._serialized_end = 7345
    _globals['_JOBCONFIGURATIONEXTRACT_MODELEXTRACTOPTIONS']._serialized_start = 7267
    _globals['_JOBCONFIGURATIONEXTRACT_MODELEXTRACTOPTIONS']._serialized_end = 7335
    _globals['_JOBCONFIGURATION']._serialized_start = 7348
    _globals['_JOBCONFIGURATION']._serialized_end = 8013
    _globals['_JOBCONFIGURATION_LABELSENTRY']._serialized_start = 1217
    _globals['_JOBCONFIGURATION_LABELSENTRY']._serialized_end = 1262