"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/bigquery/v2/table.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.bigquery.v2 import biglake_config_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_biglake__config__pb2
from .....google.cloud.bigquery.v2 import clustering_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_clustering__pb2
from .....google.cloud.bigquery.v2 import encryption_config_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_encryption__config__pb2
from .....google.cloud.bigquery.v2 import error_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_error__pb2
from .....google.cloud.bigquery.v2 import external_catalog_table_options_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_external__catalog__table__options__pb2
from .....google.cloud.bigquery.v2 import external_data_config_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_external__data__config__pb2
from .....google.cloud.bigquery.v2 import managed_table_type_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_managed__table__type__pb2
from .....google.cloud.bigquery.v2 import partitioning_definition_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_partitioning__definition__pb2
from .....google.cloud.bigquery.v2 import privacy_policy_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_privacy__policy__pb2
from .....google.cloud.bigquery.v2 import range_partitioning_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_range__partitioning__pb2
from .....google.cloud.bigquery.v2 import restriction_config_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_restriction__config__pb2
from .....google.cloud.bigquery.v2 import table_constraints_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_table__constraints__pb2
from .....google.cloud.bigquery.v2 import table_reference_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_table__reference__pb2
from .....google.cloud.bigquery.v2 import table_schema_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_table__schema__pb2
from .....google.cloud.bigquery.v2 import time_partitioning_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_time__partitioning__pb2
from .....google.cloud.bigquery.v2 import udf_resource_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_udf__resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/cloud/bigquery/v2/table.proto\x12\x18google.cloud.bigquery.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a-google/cloud/bigquery/v2/biglake_config.proto\x1a)google/cloud/bigquery/v2/clustering.proto\x1a0google/cloud/bigquery/v2/encryption_config.proto\x1a$google/cloud/bigquery/v2/error.proto\x1a=google/cloud/bigquery/v2/external_catalog_table_options.proto\x1a3google/cloud/bigquery/v2/external_data_config.proto\x1a1google/cloud/bigquery/v2/managed_table_type.proto\x1a6google/cloud/bigquery/v2/partitioning_definition.proto\x1a-google/cloud/bigquery/v2/privacy_policy.proto\x1a1google/cloud/bigquery/v2/range_partitioning.proto\x1a1google/cloud/bigquery/v2/restriction_config.proto\x1a0google/cloud/bigquery/v2/table_constraints.proto\x1a.google/cloud/bigquery/v2/table_reference.proto\x1a+google/cloud/bigquery/v2/table_schema.proto\x1a0google/cloud/bigquery/v2/time_partitioning.proto\x1a+google/cloud/bigquery/v2/udf_resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xf5\x03\n\x14TableReplicationInfo\x12C\n\x0csource_table\x18\x01 \x01(\x0b2(.google.cloud.bigquery.v2.TableReferenceB\x03\xe0A\x02\x12$\n\x17replication_interval_ms\x18\x02 \x01(\x03B\x03\xe0A\x01\x123\n#replicated_source_last_refresh_time\x18\x03 \x01(\x03B\x06\xe0A\x03\xe0A\x01\x12d\n\x12replication_status\x18\x04 \x01(\x0e2@.google.cloud.bigquery.v2.TableReplicationInfo.ReplicationStatusB\x06\xe0A\x03\xe0A\x01\x12G\n\x11replication_error\x18\x05 \x01(\x0b2$.google.cloud.bigquery.v2.ErrorProtoB\x06\xe0A\x03\xe0A\x01"\x8d\x01\n\x11ReplicationStatus\x12"\n\x1eREPLICATION_STATUS_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x12\n\x0eSOURCE_DELETED\x10\x02\x12\x15\n\x11PERMISSION_DENIED\x10\x03\x12\x1d\n\x19UNSUPPORTED_CONFIGURATION\x10\x04"\xf4\x02\n\x0eViewDefinition\x12\x12\n\x05query\x18\x01 \x01(\tB\x03\xe0A\x02\x12^\n\x1fuser_defined_function_resources\x18\x02 \x03(\x0b25.google.cloud.bigquery.v2.UserDefinedFunctionResource\x122\n\x0euse_legacy_sql\x18\x03 \x01(\x0b2\x1a.google.protobuf.BoolValue\x12!\n\x19use_explicit_column_names\x18\x04 \x01(\x08\x12D\n\x0eprivacy_policy\x18\x05 \x01(\x0b2\'.google.cloud.bigquery.v2.PrivacyPolicyB\x03\xe0A\x01\x12Q\n\x13foreign_definitions\x18\x06 \x03(\x0b2/.google.cloud.bigquery.v2.ForeignViewDefinitionB\x03\xe0A\x01"A\n\x15ForeignViewDefinition\x12\x12\n\x05query\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07dialect\x18\x07 \x01(\tB\x03\xe0A\x01"\x94\x02\n\x1aMaterializedViewDefinition\x12\x12\n\x05query\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1e\n\x11last_refresh_time\x18\x02 \x01(\x03B\x03\xe0A\x03\x127\n\x0eenable_refresh\x18\x03 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12>\n\x13refresh_interval_ms\x18\x04 \x01(\x0b2\x1c.google.protobuf.UInt64ValueB\x03\xe0A\x01\x12I\n allow_non_incremental_definition\x18\x06 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01"\x9c\x01\n\x16MaterializedViewStatus\x12:\n\x11refresh_watermark\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12F\n\x13last_refresh_status\x18\x02 \x01(\x0b2$.google.cloud.bigquery.v2.ErrorProtoB\x03\xe0A\x03"\x99\x01\n\x12SnapshotDefinition\x12K\n\x14base_table_reference\x18\x01 \x01(\x0b2(.google.cloud.bigquery.v2.TableReferenceB\x03\xe0A\x02\x126\n\rsnapshot_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02"\x93\x01\n\x0fCloneDefinition\x12K\n\x14base_table_reference\x18\x01 \x01(\x0b2(.google.cloud.bigquery.v2.TableReferenceB\x03\xe0A\x02\x123\n\nclone_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02"l\n\x0fStreamingbuffer\x12\x1c\n\x0festimated_bytes\x18\x01 \x01(\x04B\x03\xe0A\x03\x12\x1b\n\x0eestimated_rows\x18\x02 \x01(\x04B\x03\xe0A\x03\x12\x1e\n\x11oldest_entry_time\x18\x03 \x01(\x06B\x03\xe0A\x03"\x99\x1a\n\x05Table\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x11\n\x04etag\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x0f\n\x02id\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x16\n\tself_link\x18\x04 \x01(\tB\x03\xe0A\x03\x12F\n\x0ftable_reference\x18\x05 \x01(\x0b2(.google.cloud.bigquery.v2.TableReferenceB\x03\xe0A\x02\x128\n\rfriendly_name\x18\x06 \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01\x126\n\x0bdescription\x18\x07 \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01\x12;\n\x06labels\x18\x08 \x03(\x0b2+.google.cloud.bigquery.v2.Table.LabelsEntry\x12:\n\x06schema\x18\t \x01(\x0b2%.google.cloud.bigquery.v2.TableSchemaB\x03\xe0A\x01\x12E\n\x11time_partitioning\x18\n \x01(\x0b2*.google.cloud.bigquery.v2.TimePartitioning\x12G\n\x12range_partitioning\x18\x1b \x01(\x0b2+.google.cloud.bigquery.v2.RangePartitioning\x128\n\nclustering\x18\x17 \x01(\x0b2$.google.cloud.bigquery.v2.Clustering\x12A\n\x18require_partition_filter\x18\x1c \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12X\n\x14partition_definition\x183 \x01(\x0b20.google.cloud.bigquery.v2.PartitioningDefinitionB\x03\xe0A\x01H\x00\x88\x01\x01\x123\n\tnum_bytes\x18\x0b \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x03\x12<\n\x12num_physical_bytes\x18\x1a \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x03\x12=\n\x13num_long_term_bytes\x18\x0c \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x03\x123\n\x08num_rows\x18\r \x01(\x0b2\x1c.google.protobuf.UInt64ValueB\x03\xe0A\x03\x12\x1a\n\rcreation_time\x18\x0e \x01(\x03B\x03\xe0A\x03\x129\n\x0fexpiration_time\x18\x0f \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x01\x12\x1f\n\x12last_modified_time\x18\x10 \x01(\x06B\x03\xe0A\x03\x12\x11\n\x04type\x18\x11 \x01(\tB\x03\xe0A\x03\x12;\n\x04view\x18\x12 \x01(\x0b2(.google.cloud.bigquery.v2.ViewDefinitionB\x03\xe0A\x01\x12T\n\x11materialized_view\x18\x19 \x01(\x0b24.google.cloud.bigquery.v2.MaterializedViewDefinitionB\x03\xe0A\x01\x12W\n\x18materialized_view_status\x18* \x01(\x0b20.google.cloud.bigquery.v2.MaterializedViewStatusB\x03\xe0A\x03\x12]\n\x1bexternal_data_configuration\x18\x13 \x01(\x0b23.google.cloud.bigquery.v2.ExternalDataConfigurationB\x03\xe0A\x01\x12R\n\x15biglake_configuration\x18- \x01(\x0b2..google.cloud.bigquery.v2.BigLakeConfigurationB\x03\xe0A\x01\x12K\n\x12managed_table_type\x187 \x01(\x0e2*.google.cloud.bigquery.v2.ManagedTableTypeB\x03\xe0A\x01\x12\x15\n\x08location\x18\x14 \x01(\tB\x03\xe0A\x03\x12H\n\x10streaming_buffer\x18\x15 \x01(\x0b2).google.cloud.bigquery.v2.StreamingbufferB\x03\xe0A\x03\x12S\n\x18encryption_configuration\x18\x16 \x01(\x0b21.google.cloud.bigquery.v2.EncryptionConfiguration\x12N\n\x13snapshot_definition\x18\x1d \x01(\x0b2,.google.cloud.bigquery.v2.SnapshotDefinitionB\x03\xe0A\x03\x12<\n\x11default_collation\x18\x1e \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01\x12[\n\x15default_rounding_mode\x18, \x01(\x0e27.google.cloud.bigquery.v2.TableFieldSchema.RoundingModeB\x03\xe0A\x01\x12H\n\x10clone_definition\x18\x1f \x01(\x0b2).google.cloud.bigquery.v2.CloneDefinitionB\x03\xe0A\x03\x12H\n\x1enum_time_travel_physical_bytes\x18! \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x03\x12A\n\x17num_total_logical_bytes\x18" \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x03\x12B\n\x18num_active_logical_bytes\x18# \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x03\x12E\n\x1bnum_long_term_logical_bytes\x18$ \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x03\x12D\n\x1anum_current_physical_bytes\x185 \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x03\x12B\n\x18num_total_physical_bytes\x18% \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x03\x12C\n\x19num_active_physical_bytes\x18& \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x03\x12F\n\x1cnum_long_term_physical_bytes\x18\' \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x03\x128\n\x0enum_partitions\x18( \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x03\x12\x1a\n\rmax_staleness\x18) \x01(\tB\x03\xe0A\x01\x12I\n\x0crestrictions\x18. \x01(\x0b2+.google.cloud.bigquery.v2.RestrictionConfigB\x06\xe0A\x01\xe0A\x03\x12J\n\x11table_constraints\x18/ \x01(\x0b2*.google.cloud.bigquery.v2.TableConstraintsB\x03\xe0A\x01\x12M\n\rresource_tags\x180 \x03(\x0b21.google.cloud.bigquery.v2.Table.ResourceTagsEntryB\x03\xe0A\x01\x12S\n\x16table_replication_info\x181 \x01(\x0b2..google.cloud.bigquery.v2.TableReplicationInfoB\x03\xe0A\x01\x12B\n\x08replicas\x182 \x03(\x0b2(.google.cloud.bigquery.v2.TableReferenceB\x06\xe0A\x01\xe0A\x03\x12b\n\x1eexternal_catalog_table_options\x186 \x01(\x0b25.google.cloud.bigquery.v2.ExternalCatalogTableOptionsB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a3\n\x11ResourceTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x17\n\x15_partition_definition"\xa5\x02\n\x0fGetTableRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x17\n\x0fselected_fields\x18\x04 \x01(\t\x12N\n\x04view\x18\x05 \x01(\x0e2;.google.cloud.bigquery.v2.GetTableRequest.TableMetadataViewB\x03\xe0A\x01"`\n\x11TableMetadataView\x12#\n\x1fTABLE_METADATA_VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x11\n\rSTORAGE_STATS\x10\x02\x12\x08\n\x04FULL\x10\x03"{\n\x12InsertTableRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x123\n\x05table\x18\x04 \x01(\x0b2\x1f.google.cloud.bigquery.v2.TableB\x03\xe0A\x02"\xb9\x01\n\x19UpdateOrPatchTableRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x03 \x01(\tB\x03\xe0A\x02\x123\n\x05table\x18\x04 \x01(\x0b2\x1f.google.cloud.bigquery.v2.TableB\x03\xe0A\x02\x12\x1e\n\x11autodetect_schema\x18\x05 \x01(\x08B\x03\xe0A\x01"]\n\x12DeleteTableRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x03 \x01(\tB\x03\xe0A\x02"\x8c\x01\n\x11ListTablesRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x121\n\x0bmax_results\x18\x03 \x01(\x0b2\x1c.google.protobuf.UInt32Value\x12\x12\n\npage_token\x18\x04 \x01(\t"\x85\x01\n\x0eListFormatView\x122\n\x0euse_legacy_sql\x18\x01 \x01(\x0b2\x1a.google.protobuf.BoolValue\x12?\n\x0eprivacy_policy\x18\x02 \x01(\x0b2\'.google.cloud.bigquery.v2.PrivacyPolicy"\xa1\x05\n\x0fListFormatTable\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12A\n\x0ftable_reference\x18\x03 \x01(\x0b2(.google.cloud.bigquery.v2.TableReference\x123\n\rfriendly_name\x18\x04 \x01(\x0b2\x1c.google.protobuf.StringValue\x12\x0c\n\x04type\x18\x05 \x01(\t\x12E\n\x11time_partitioning\x18\x06 \x01(\x0b2*.google.cloud.bigquery.v2.TimePartitioning\x12G\n\x12range_partitioning\x18\x0c \x01(\x0b2+.google.cloud.bigquery.v2.RangePartitioning\x128\n\nclustering\x18\x0b \x01(\x0b2$.google.cloud.bigquery.v2.Clustering\x12E\n\x06labels\x18\x07 \x03(\x0b25.google.cloud.bigquery.v2.ListFormatTable.LabelsEntry\x126\n\x04view\x18\x08 \x01(\x0b2(.google.cloud.bigquery.v2.ListFormatView\x12\x1a\n\rcreation_time\x18\t \x01(\x03B\x03\xe0A\x03\x12\x17\n\x0fexpiration_time\x18\n \x01(\x03\x12A\n\x18require_partition_filter\x18\x0e \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xad\x01\n\tTableList\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x0c\n\x04etag\x18\x02 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\x129\n\x06tables\x18\x04 \x03(\x0b2).google.cloud.bigquery.v2.ListFormatTable\x120\n\x0btotal_items\x18\x05 \x01(\x0b2\x1b.google.protobuf.Int32Value2\x90\n\n\x0cTableService\x12\xb0\x01\n\x08GetTable\x12).google.cloud.bigquery.v2.GetTableRequest\x1a\x1f.google.cloud.bigquery.v2.Table"X\x82\xd3\xe4\x93\x02R\x12P/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}\x12\xb0\x01\n\x0bInsertTable\x12,.google.cloud.bigquery.v2.InsertTableRequest\x1a\x1f.google.cloud.bigquery.v2.Table"R\x82\xd3\xe4\x93\x02L"C/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables:\x05table\x12\xc3\x01\n\nPatchTable\x123.google.cloud.bigquery.v2.UpdateOrPatchTableRequest\x1a\x1f.google.cloud.bigquery.v2.Table"_\x82\xd3\xe4\x93\x02Y2P/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}:\x05table\x12\xc4\x01\n\x0bUpdateTable\x123.google.cloud.bigquery.v2.UpdateOrPatchTableRequest\x1a\x1f.google.cloud.bigquery.v2.Table"_\x82\xd3\xe4\x93\x02Y\x1aP/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}:\x05table\x12\xad\x01\n\x0bDeleteTable\x12,.google.cloud.bigquery.v2.DeleteTableRequest\x1a\x16.google.protobuf.Empty"X\x82\xd3\xe4\x93\x02R*P/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}\x12\xab\x01\n\nListTables\x12+.google.cloud.bigquery.v2.ListTablesRequest\x1a#.google.cloud.bigquery.v2.TableList"K\x82\xd3\xe4\x93\x02E\x12C/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables\x1a\xae\x01\xcaA\x17bigquery.googleapis.com\xd2A\x90\x01https://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-onlyBg\n\x1ccom.google.cloud.bigquery.v2B\nTableProtoZ;cloud.google.com/go/bigquery/v2/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.table_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\nTableProtoZ;cloud.google.com/go/bigquery/v2/apiv2/bigquerypb;bigquerypb'
    _globals['_TABLEREPLICATIONINFO'].fields_by_name['source_table']._loaded_options = None
    _globals['_TABLEREPLICATIONINFO'].fields_by_name['source_table']._serialized_options = b'\xe0A\x02'
    _globals['_TABLEREPLICATIONINFO'].fields_by_name['replication_interval_ms']._loaded_options = None
    _globals['_TABLEREPLICATIONINFO'].fields_by_name['replication_interval_ms']._serialized_options = b'\xe0A\x01'
    _globals['_TABLEREPLICATIONINFO'].fields_by_name['replicated_source_last_refresh_time']._loaded_options = None
    _globals['_TABLEREPLICATIONINFO'].fields_by_name['replicated_source_last_refresh_time']._serialized_options = b'\xe0A\x03\xe0A\x01'
    _globals['_TABLEREPLICATIONINFO'].fields_by_name['replication_status']._loaded_options = None
    _globals['_TABLEREPLICATIONINFO'].fields_by_name['replication_status']._serialized_options = b'\xe0A\x03\xe0A\x01'
    _globals['_TABLEREPLICATIONINFO'].fields_by_name['replication_error']._loaded_options = None
    _globals['_TABLEREPLICATIONINFO'].fields_by_name['replication_error']._serialized_options = b'\xe0A\x03\xe0A\x01'
    _globals['_VIEWDEFINITION'].fields_by_name['query']._loaded_options = None
    _globals['_VIEWDEFINITION'].fields_by_name['query']._serialized_options = b'\xe0A\x02'
    _globals['_VIEWDEFINITION'].fields_by_name['privacy_policy']._loaded_options = None
    _globals['_VIEWDEFINITION'].fields_by_name['privacy_policy']._serialized_options = b'\xe0A\x01'
    _globals['_VIEWDEFINITION'].fields_by_name['foreign_definitions']._loaded_options = None
    _globals['_VIEWDEFINITION'].fields_by_name['foreign_definitions']._serialized_options = b'\xe0A\x01'
    _globals['_FOREIGNVIEWDEFINITION'].fields_by_name['query']._loaded_options = None
    _globals['_FOREIGNVIEWDEFINITION'].fields_by_name['query']._serialized_options = b'\xe0A\x02'
    _globals['_FOREIGNVIEWDEFINITION'].fields_by_name['dialect']._loaded_options = None
    _globals['_FOREIGNVIEWDEFINITION'].fields_by_name['dialect']._serialized_options = b'\xe0A\x01'
    _globals['_MATERIALIZEDVIEWDEFINITION'].fields_by_name['query']._loaded_options = None
    _globals['_MATERIALIZEDVIEWDEFINITION'].fields_by_name['query']._serialized_options = b'\xe0A\x02'
    _globals['_MATERIALIZEDVIEWDEFINITION'].fields_by_name['last_refresh_time']._loaded_options = None
    _globals['_MATERIALIZEDVIEWDEFINITION'].fields_by_name['last_refresh_time']._serialized_options = b'\xe0A\x03'
    _globals['_MATERIALIZEDVIEWDEFINITION'].fields_by_name['enable_refresh']._loaded_options = None
    _globals['_MATERIALIZEDVIEWDEFINITION'].fields_by_name['enable_refresh']._serialized_options = b'\xe0A\x01'
    _globals['_MATERIALIZEDVIEWDEFINITION'].fields_by_name['refresh_interval_ms']._loaded_options = None
    _globals['_MATERIALIZEDVIEWDEFINITION'].fields_by_name['refresh_interval_ms']._serialized_options = b'\xe0A\x01'
    _globals['_MATERIALIZEDVIEWDEFINITION'].fields_by_name['allow_non_incremental_definition']._loaded_options = None
    _globals['_MATERIALIZEDVIEWDEFINITION'].fields_by_name['allow_non_incremental_definition']._serialized_options = b'\xe0A\x01'
    _globals['_MATERIALIZEDVIEWSTATUS'].fields_by_name['refresh_watermark']._loaded_options = None
    _globals['_MATERIALIZEDVIEWSTATUS'].fields_by_name['refresh_watermark']._serialized_options = b'\xe0A\x03'
    _globals['_MATERIALIZEDVIEWSTATUS'].fields_by_name['last_refresh_status']._loaded_options = None
    _globals['_MATERIALIZEDVIEWSTATUS'].fields_by_name['last_refresh_status']._serialized_options = b'\xe0A\x03'
    _globals['_SNAPSHOTDEFINITION'].fields_by_name['base_table_reference']._loaded_options = None
    _globals['_SNAPSHOTDEFINITION'].fields_by_name['base_table_reference']._serialized_options = b'\xe0A\x02'
    _globals['_SNAPSHOTDEFINITION'].fields_by_name['snapshot_time']._loaded_options = None
    _globals['_SNAPSHOTDEFINITION'].fields_by_name['snapshot_time']._serialized_options = b'\xe0A\x02'
    _globals['_CLONEDEFINITION'].fields_by_name['base_table_reference']._loaded_options = None
    _globals['_CLONEDEFINITION'].fields_by_name['base_table_reference']._serialized_options = b'\xe0A\x02'
    _globals['_CLONEDEFINITION'].fields_by_name['clone_time']._loaded_options = None
    _globals['_CLONEDEFINITION'].fields_by_name['clone_time']._serialized_options = b'\xe0A\x02'
    _globals['_STREAMINGBUFFER'].fields_by_name['estimated_bytes']._loaded_options = None
    _globals['_STREAMINGBUFFER'].fields_by_name['estimated_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_STREAMINGBUFFER'].fields_by_name['estimated_rows']._loaded_options = None
    _globals['_STREAMINGBUFFER'].fields_by_name['estimated_rows']._serialized_options = b'\xe0A\x03'
    _globals['_STREAMINGBUFFER'].fields_by_name['oldest_entry_time']._loaded_options = None
    _globals['_STREAMINGBUFFER'].fields_by_name['oldest_entry_time']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE_LABELSENTRY']._loaded_options = None
    _globals['_TABLE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_TABLE_RESOURCETAGSENTRY']._loaded_options = None
    _globals['_TABLE_RESOURCETAGSENTRY']._serialized_options = b'8\x01'
    _globals['_TABLE'].fields_by_name['etag']._loaded_options = None
    _globals['_TABLE'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['id']._loaded_options = None
    _globals['_TABLE'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['self_link']._loaded_options = None
    _globals['_TABLE'].fields_by_name['self_link']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['table_reference']._loaded_options = None
    _globals['_TABLE'].fields_by_name['table_reference']._serialized_options = b'\xe0A\x02'
    _globals['_TABLE'].fields_by_name['friendly_name']._loaded_options = None
    _globals['_TABLE'].fields_by_name['friendly_name']._serialized_options = b'\xe0A\x01'
    _globals['_TABLE'].fields_by_name['description']._loaded_options = None
    _globals['_TABLE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_TABLE'].fields_by_name['schema']._loaded_options = None
    _globals['_TABLE'].fields_by_name['schema']._serialized_options = b'\xe0A\x01'
    _globals['_TABLE'].fields_by_name['require_partition_filter']._loaded_options = None
    _globals['_TABLE'].fields_by_name['require_partition_filter']._serialized_options = b'\xe0A\x01'
    _globals['_TABLE'].fields_by_name['partition_definition']._loaded_options = None
    _globals['_TABLE'].fields_by_name['partition_definition']._serialized_options = b'\xe0A\x01'
    _globals['_TABLE'].fields_by_name['num_bytes']._loaded_options = None
    _globals['_TABLE'].fields_by_name['num_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['num_physical_bytes']._loaded_options = None
    _globals['_TABLE'].fields_by_name['num_physical_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['num_long_term_bytes']._loaded_options = None
    _globals['_TABLE'].fields_by_name['num_long_term_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['num_rows']._loaded_options = None
    _globals['_TABLE'].fields_by_name['num_rows']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['creation_time']._loaded_options = None
    _globals['_TABLE'].fields_by_name['creation_time']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['expiration_time']._loaded_options = None
    _globals['_TABLE'].fields_by_name['expiration_time']._serialized_options = b'\xe0A\x01'
    _globals['_TABLE'].fields_by_name['last_modified_time']._loaded_options = None
    _globals['_TABLE'].fields_by_name['last_modified_time']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['type']._loaded_options = None
    _globals['_TABLE'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['view']._loaded_options = None
    _globals['_TABLE'].fields_by_name['view']._serialized_options = b'\xe0A\x01'
    _globals['_TABLE'].fields_by_name['materialized_view']._loaded_options = None
    _globals['_TABLE'].fields_by_name['materialized_view']._serialized_options = b'\xe0A\x01'
    _globals['_TABLE'].fields_by_name['materialized_view_status']._loaded_options = None
    _globals['_TABLE'].fields_by_name['materialized_view_status']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['external_data_configuration']._loaded_options = None
    _globals['_TABLE'].fields_by_name['external_data_configuration']._serialized_options = b'\xe0A\x01'
    _globals['_TABLE'].fields_by_name['biglake_configuration']._loaded_options = None
    _globals['_TABLE'].fields_by_name['biglake_configuration']._serialized_options = b'\xe0A\x01'
    _globals['_TABLE'].fields_by_name['managed_table_type']._loaded_options = None
    _globals['_TABLE'].fields_by_name['managed_table_type']._serialized_options = b'\xe0A\x01'
    _globals['_TABLE'].fields_by_name['location']._loaded_options = None
    _globals['_TABLE'].fields_by_name['location']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['streaming_buffer']._loaded_options = None
    _globals['_TABLE'].fields_by_name['streaming_buffer']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['snapshot_definition']._loaded_options = None
    _globals['_TABLE'].fields_by_name['snapshot_definition']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['default_collation']._loaded_options = None
    _globals['_TABLE'].fields_by_name['default_collation']._serialized_options = b'\xe0A\x01'
    _globals['_TABLE'].fields_by_name['default_rounding_mode']._loaded_options = None
    _globals['_TABLE'].fields_by_name['default_rounding_mode']._serialized_options = b'\xe0A\x01'
    _globals['_TABLE'].fields_by_name['clone_definition']._loaded_options = None
    _globals['_TABLE'].fields_by_name['clone_definition']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['num_time_travel_physical_bytes']._loaded_options = None
    _globals['_TABLE'].fields_by_name['num_time_travel_physical_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['num_total_logical_bytes']._loaded_options = None
    _globals['_TABLE'].fields_by_name['num_total_logical_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['num_active_logical_bytes']._loaded_options = None
    _globals['_TABLE'].fields_by_name['num_active_logical_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['num_long_term_logical_bytes']._loaded_options = None
    _globals['_TABLE'].fields_by_name['num_long_term_logical_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['num_current_physical_bytes']._loaded_options = None
    _globals['_TABLE'].fields_by_name['num_current_physical_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['num_total_physical_bytes']._loaded_options = None
    _globals['_TABLE'].fields_by_name['num_total_physical_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['num_active_physical_bytes']._loaded_options = None
    _globals['_TABLE'].fields_by_name['num_active_physical_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['num_long_term_physical_bytes']._loaded_options = None
    _globals['_TABLE'].fields_by_name['num_long_term_physical_bytes']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['num_partitions']._loaded_options = None
    _globals['_TABLE'].fields_by_name['num_partitions']._serialized_options = b'\xe0A\x03'
    _globals['_TABLE'].fields_by_name['max_staleness']._loaded_options = None
    _globals['_TABLE'].fields_by_name['max_staleness']._serialized_options = b'\xe0A\x01'
    _globals['_TABLE'].fields_by_name['restrictions']._loaded_options = None
    _globals['_TABLE'].fields_by_name['restrictions']._serialized_options = b'\xe0A\x01\xe0A\x03'
    _globals['_TABLE'].fields_by_name['table_constraints']._loaded_options = None
    _globals['_TABLE'].fields_by_name['table_constraints']._serialized_options = b'\xe0A\x01'
    _globals['_TABLE'].fields_by_name['resource_tags']._loaded_options = None
    _globals['_TABLE'].fields_by_name['resource_tags']._serialized_options = b'\xe0A\x01'
    _globals['_TABLE'].fields_by_name['table_replication_info']._loaded_options = None
    _globals['_TABLE'].fields_by_name['table_replication_info']._serialized_options = b'\xe0A\x01'
    _globals['_TABLE'].fields_by_name['replicas']._loaded_options = None
    _globals['_TABLE'].fields_by_name['replicas']._serialized_options = b'\xe0A\x01\xe0A\x03'
    _globals['_TABLE'].fields_by_name['external_catalog_table_options']._loaded_options = None
    _globals['_TABLE'].fields_by_name['external_catalog_table_options']._serialized_options = b'\xe0A\x01'
    _globals['_GETTABLEREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_GETTABLEREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETTABLEREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_GETTABLEREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETTABLEREQUEST'].fields_by_name['table_id']._loaded_options = None
    _globals['_GETTABLEREQUEST'].fields_by_name['table_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETTABLEREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_GETTABLEREQUEST'].fields_by_name['view']._serialized_options = b'\xe0A\x01'
    _globals['_INSERTTABLEREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_INSERTTABLEREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_INSERTTABLEREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_INSERTTABLEREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_INSERTTABLEREQUEST'].fields_by_name['table']._loaded_options = None
    _globals['_INSERTTABLEREQUEST'].fields_by_name['table']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEORPATCHTABLEREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_UPDATEORPATCHTABLEREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEORPATCHTABLEREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_UPDATEORPATCHTABLEREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEORPATCHTABLEREQUEST'].fields_by_name['table_id']._loaded_options = None
    _globals['_UPDATEORPATCHTABLEREQUEST'].fields_by_name['table_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEORPATCHTABLEREQUEST'].fields_by_name['table']._loaded_options = None
    _globals['_UPDATEORPATCHTABLEREQUEST'].fields_by_name['table']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEORPATCHTABLEREQUEST'].fields_by_name['autodetect_schema']._loaded_options = None
    _globals['_UPDATEORPATCHTABLEREQUEST'].fields_by_name['autodetect_schema']._serialized_options = b'\xe0A\x01'
    _globals['_DELETETABLEREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_DELETETABLEREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETABLEREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_DELETETABLEREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETABLEREQUEST'].fields_by_name['table_id']._loaded_options = None
    _globals['_DELETETABLEREQUEST'].fields_by_name['table_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTTABLESREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_LISTTABLESREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTTABLESREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_LISTTABLESREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTFORMATTABLE_LABELSENTRY']._loaded_options = None
    _globals['_LISTFORMATTABLE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_LISTFORMATTABLE'].fields_by_name['creation_time']._loaded_options = None
    _globals['_LISTFORMATTABLE'].fields_by_name['creation_time']._serialized_options = b'\xe0A\x03'
    _globals['_LISTFORMATTABLE'].fields_by_name['require_partition_filter']._loaded_options = None
    _globals['_LISTFORMATTABLE'].fields_by_name['require_partition_filter']._serialized_options = b'\xe0A\x01'
    _globals['_TABLESERVICE']._loaded_options = None
    _globals['_TABLESERVICE']._serialized_options = b'\xcaA\x17bigquery.googleapis.com\xd2A\x90\x01https://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_TABLESERVICE'].methods_by_name['GetTable']._loaded_options = None
    _globals['_TABLESERVICE'].methods_by_name['GetTable']._serialized_options = b'\x82\xd3\xe4\x93\x02R\x12P/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}'
    _globals['_TABLESERVICE'].methods_by_name['InsertTable']._loaded_options = None
    _globals['_TABLESERVICE'].methods_by_name['InsertTable']._serialized_options = b'\x82\xd3\xe4\x93\x02L"C/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables:\x05table'
    _globals['_TABLESERVICE'].methods_by_name['PatchTable']._loaded_options = None
    _globals['_TABLESERVICE'].methods_by_name['PatchTable']._serialized_options = b'\x82\xd3\xe4\x93\x02Y2P/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}:\x05table'
    _globals['_TABLESERVICE'].methods_by_name['UpdateTable']._loaded_options = None
    _globals['_TABLESERVICE'].methods_by_name['UpdateTable']._serialized_options = b'\x82\xd3\xe4\x93\x02Y\x1aP/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}:\x05table'
    _globals['_TABLESERVICE'].methods_by_name['DeleteTable']._loaded_options = None
    _globals['_TABLESERVICE'].methods_by_name['DeleteTable']._serialized_options = b'\x82\xd3\xe4\x93\x02R*P/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}'
    _globals['_TABLESERVICE'].methods_by_name['ListTables']._loaded_options = None
    _globals['_TABLESERVICE'].methods_by_name['ListTables']._serialized_options = b'\x82\xd3\xe4\x93\x02E\x12C/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables'
    _globals['_TABLEREPLICATIONINFO']._serialized_start = 1037
    _globals['_TABLEREPLICATIONINFO']._serialized_end = 1538
    _globals['_TABLEREPLICATIONINFO_REPLICATIONSTATUS']._serialized_start = 1397
    _globals['_TABLEREPLICATIONINFO_REPLICATIONSTATUS']._serialized_end = 1538
    _globals['_VIEWDEFINITION']._serialized_start = 1541
    _globals['_VIEWDEFINITION']._serialized_end = 1913
    _globals['_FOREIGNVIEWDEFINITION']._serialized_start = 1915
    _globals['_FOREIGNVIEWDEFINITION']._serialized_end = 1980
    _globals['_MATERIALIZEDVIEWDEFINITION']._serialized_start = 1983
    _globals['_MATERIALIZEDVIEWDEFINITION']._serialized_end = 2259
    _globals['_MATERIALIZEDVIEWSTATUS']._serialized_start = 2262
    _globals['_MATERIALIZEDVIEWSTATUS']._serialized_end = 2418
    _globals['_SNAPSHOTDEFINITION']._serialized_start = 2421
    _globals['_SNAPSHOTDEFINITION']._serialized_end = 2574
    _globals['_CLONEDEFINITION']._serialized_start = 2577
    _globals['_CLONEDEFINITION']._serialized_end = 2724
    _globals['_STREAMINGBUFFER']._serialized_start = 2726
    _globals['_STREAMINGBUFFER']._serialized_end = 2834
    _globals['_TABLE']._serialized_start = 2837
    _globals['_TABLE']._serialized_end = 6190
    _globals['_TABLE_LABELSENTRY']._serialized_start = 6067
    _globals['_TABLE_LABELSENTRY']._serialized_end = 6112
    _globals['_TABLE_RESOURCETAGSENTRY']._serialized_start = 6114
    _globals['_TABLE_RESOURCETAGSENTRY']._serialized_end = 6165
    _globals['_GETTABLEREQUEST']._serialized_start = 6193
    _globals['_GETTABLEREQUEST']._serialized_end = 6486
    _globals['_GETTABLEREQUEST_TABLEMETADATAVIEW']._serialized_start = 6390
    _globals['_GETTABLEREQUEST_TABLEMETADATAVIEW']._serialized_end = 6486
    _globals['_INSERTTABLEREQUEST']._serialized_start = 6488
    _globals['_INSERTTABLEREQUEST']._serialized_end = 6611
    _globals['_UPDATEORPATCHTABLEREQUEST']._serialized_start = 6614
    _globals['_UPDATEORPATCHTABLEREQUEST']._serialized_end = 6799
    _globals['_DELETETABLEREQUEST']._serialized_start = 6801
    _globals['_DELETETABLEREQUEST']._serialized_end = 6894
    _globals['_LISTTABLESREQUEST']._serialized_start = 6897
    _globals['_LISTTABLESREQUEST']._serialized_end = 7037
    _globals['_LISTFORMATVIEW']._serialized_start = 7040
    _globals['_LISTFORMATVIEW']._serialized_end = 7173
    _globals['_LISTFORMATTABLE']._serialized_start = 7176
    _globals['_LISTFORMATTABLE']._serialized_end = 7849
    _globals['_LISTFORMATTABLE_LABELSENTRY']._serialized_start = 6067
    _globals['_LISTFORMATTABLE_LABELSENTRY']._serialized_end = 6112
    _globals['_TABLELIST']._serialized_start = 7852
    _globals['_TABLELIST']._serialized_end = 8025
    _globals['_TABLESERVICE']._serialized_start = 8028
    _globals['_TABLESERVICE']._serialized_end = 9324