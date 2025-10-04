"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/datacatalog/v1/datacatalog.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.datacatalog.v1 import bigquery_pb2 as google_dot_cloud_dot_datacatalog_dot_v1_dot_bigquery__pb2
from .....google.cloud.datacatalog.v1 import common_pb2 as google_dot_cloud_dot_datacatalog_dot_v1_dot_common__pb2
from .....google.cloud.datacatalog.v1 import data_source_pb2 as google_dot_cloud_dot_datacatalog_dot_v1_dot_data__source__pb2
from .....google.cloud.datacatalog.v1 import dataplex_spec_pb2 as google_dot_cloud_dot_datacatalog_dot_v1_dot_dataplex__spec__pb2
from .....google.cloud.datacatalog.v1 import gcs_fileset_spec_pb2 as google_dot_cloud_dot_datacatalog_dot_v1_dot_gcs__fileset__spec__pb2
from .....google.cloud.datacatalog.v1 import schema_pb2 as google_dot_cloud_dot_datacatalog_dot_v1_dot_schema__pb2
from .....google.cloud.datacatalog.v1 import search_pb2 as google_dot_cloud_dot_datacatalog_dot_v1_dot_search__pb2
from .....google.cloud.datacatalog.v1 import table_spec_pb2 as google_dot_cloud_dot_datacatalog_dot_v1_dot_table__spec__pb2
from .....google.cloud.datacatalog.v1 import tags_pb2 as google_dot_cloud_dot_datacatalog_dot_v1_dot_tags__pb2
from .....google.cloud.datacatalog.v1 import timestamps_pb2 as google_dot_cloud_dot_datacatalog_dot_v1_dot_timestamps__pb2
from .....google.cloud.datacatalog.v1 import usage_pb2 as google_dot_cloud_dot_datacatalog_dot_v1_dot_usage__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/datacatalog/v1/datacatalog.proto\x12\x1bgoogle.cloud.datacatalog.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/cloud/datacatalog/v1/bigquery.proto\x1a(google/cloud/datacatalog/v1/common.proto\x1a-google/cloud/datacatalog/v1/data_source.proto\x1a/google/cloud/datacatalog/v1/dataplex_spec.proto\x1a2google/cloud/datacatalog/v1/gcs_fileset_spec.proto\x1a(google/cloud/datacatalog/v1/schema.proto\x1a(google/cloud/datacatalog/v1/search.proto\x1a,google/cloud/datacatalog/v1/table_spec.proto\x1a&google/cloud/datacatalog/v1/tags.proto\x1a,google/cloud/datacatalog/v1/timestamps.proto\x1a\'google/cloud/datacatalog/v1/usage.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xa0\x03\n\x14SearchCatalogRequest\x12K\n\x05scope\x18\x06 \x01(\x0b27.google.cloud.datacatalog.v1.SearchCatalogRequest.ScopeB\x03\xe0A\x02\x12\x12\n\x05query\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x10\n\x08order_by\x18\x05 \x01(\t\x12\x19\n\x0cadmin_search\x18\x11 \x01(\x08B\x03\xe0A\x01\x1a\xcd\x01\n\x05Scope\x12\x17\n\x0finclude_org_ids\x18\x02 \x03(\t\x12\x1b\n\x13include_project_ids\x18\x03 \x03(\t\x12#\n\x1binclude_gcp_public_datasets\x18\x07 \x01(\x08\x12!\n\x14restricted_locations\x18\x10 \x03(\tB\x03\xe0A\x01\x12\x19\n\x0cstarred_only\x18\x12 \x01(\x08B\x03\xe0A\x01\x12+\n\x1cinclude_public_tag_templates\x18\x13 \x01(\x08B\x05\x18\x01\xe0A\x01"\x9c\x01\n\x15SearchCatalogResponse\x12A\n\x07results\x18\x01 \x03(\x0b20.google.cloud.datacatalog.v1.SearchCatalogResult\x12\x12\n\ntotal_size\x18\x02 \x01(\x05\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\x12\x13\n\x0bunreachable\x18\x06 \x03(\t"\xb3\x01\n\x17CreateEntryGroupRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%datacatalog.googleapis.com/EntryGroup\x12\x1b\n\x0eentry_group_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12<\n\x0bentry_group\x18\x02 \x01(\x0b2\'.google.cloud.datacatalog.v1.EntryGroup"\x8d\x01\n\x17UpdateEntryGroupRequest\x12A\n\x0bentry_group\x18\x01 \x01(\x0b2\'.google.cloud.datacatalog.v1.EntryGroupB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x82\x01\n\x14GetEntryGroupRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%datacatalog.googleapis.com/EntryGroup\x12-\n\tread_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"j\n\x17DeleteEntryGroupRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%datacatalog.googleapis.com/EntryGroup\x12\x12\n\x05force\x18\x02 \x01(\x08B\x03\xe0A\x01"\x88\x01\n\x16ListEntryGroupsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%datacatalog.googleapis.com/EntryGroup\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"q\n\x17ListEntryGroupsResponse\x12=\n\x0centry_groups\x18\x01 \x03(\x0b2\'.google.cloud.datacatalog.v1.EntryGroup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xa2\x01\n\x12CreateEntryRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%datacatalog.googleapis.com/EntryGroup\x12\x15\n\x08entry_id\x18\x03 \x01(\tB\x03\xe0A\x02\x126\n\x05entry\x18\x02 \x01(\x0b2".google.cloud.datacatalog.v1.EntryB\x03\xe0A\x02"}\n\x12UpdateEntryRequest\x126\n\x05entry\x18\x01 \x01(\x0b2".google.cloud.datacatalog.v1.EntryB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"L\n\x12DeleteEntryRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n datacatalog.googleapis.com/Entry"I\n\x0fGetEntryRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n datacatalog.googleapis.com/Entry"\x99\x01\n\x12LookupEntryRequest\x12\x19\n\x0flinked_resource\x18\x01 \x01(\tH\x00\x12\x16\n\x0csql_resource\x18\x03 \x01(\tH\x00\x12\x1e\n\x14fully_qualified_name\x18\x05 \x01(\tH\x00\x12\x0f\n\x07project\x18\x06 \x01(\t\x12\x10\n\x08location\x18\x07 \x01(\tB\r\n\x0btarget_name"\x81\x11\n\x05Entry\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x03\xe0A\x08\xfaA\'\n%datacatalog.googleapis.com/EntryGroup\x12\x17\n\x0flinked_resource\x18\t \x01(\t\x12\x1c\n\x14fully_qualified_name\x18\x1d \x01(\t\x126\n\x04type\x18\x02 \x01(\x0e2&.google.cloud.datacatalog.v1.EntryTypeH\x00\x12\x1d\n\x13user_specified_type\x18\x10 \x01(\tH\x00\x12O\n\x11integrated_system\x18\x11 \x01(\x0e2-.google.cloud.datacatalog.v1.IntegratedSystemB\x03\xe0A\x03H\x01\x12\x1f\n\x15user_specified_system\x18\x12 \x01(\tH\x01\x12V\n\x18sql_database_system_spec\x18\' \x01(\x0b22.google.cloud.datacatalog.v1.SqlDatabaseSystemSpecH\x02\x12K\n\x12looker_system_spec\x18( \x01(\x0b2-.google.cloud.datacatalog.v1.LookerSystemSpecH\x02\x12Z\n\x1acloud_bigtable_system_spec\x18) \x01(\x0b24.google.cloud.datacatalog.v1.CloudBigtableSystemSpecH\x02\x12G\n\x10gcs_fileset_spec\x18\x06 \x01(\x0b2+.google.cloud.datacatalog.v1.GcsFilesetSpecH\x03\x12R\n\x13bigquery_table_spec\x18\x0c \x01(\x0b2..google.cloud.datacatalog.v1.BigQueryTableSpecB\x03\xe0A\x03H\x03\x12_\n\x1abigquery_date_sharded_spec\x18\x0f \x01(\x0b24.google.cloud.datacatalog.v1.BigQueryDateShardedSpecB\x03\xe0A\x03H\x03\x12M\n\x13database_table_spec\x18\x18 \x01(\x0b2..google.cloud.datacatalog.v1.DatabaseTableSpecH\x04\x12\\\n\x1bdata_source_connection_spec\x18\x1b \x01(\x0b25.google.cloud.datacatalog.v1.DataSourceConnectionSpecH\x04\x12@\n\x0croutine_spec\x18\x1c \x01(\x0b2(.google.cloud.datacatalog.v1.RoutineSpecH\x04\x12@\n\x0cdataset_spec\x18  \x01(\x0b2(.google.cloud.datacatalog.v1.DatasetSpecH\x04\x12@\n\x0cfileset_spec\x18! \x01(\x0b2(.google.cloud.datacatalog.v1.FilesetSpecH\x04\x12@\n\x0cservice_spec\x18* \x01(\x0b2(.google.cloud.datacatalog.v1.ServiceSpecH\x04\x12<\n\nmodel_spec\x18+ \x01(\x0b2&.google.cloud.datacatalog.v1.ModelSpecH\x04\x12X\n\x19feature_online_store_spec\x18- \x01(\x0b23.google.cloud.datacatalog.v1.FeatureOnlineStoreSpecH\x04\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x12F\n\x10business_context\x18% \x01(\x0b2,.google.cloud.datacatalog.v1.BusinessContext\x123\n\x06schema\x18\x05 \x01(\x0b2#.google.cloud.datacatalog.v1.Schema\x12O\n\x18source_system_timestamps\x18\x07 \x01(\x0b2-.google.cloud.datacatalog.v1.SystemTimestamps\x12>\n\x0cusage_signal\x18\r \x01(\x0b2(.google.cloud.datacatalog.v1.UsageSignal\x12>\n\x06labels\x18\x0e \x03(\x0b2..google.cloud.datacatalog.v1.Entry.LabelsEntry\x12A\n\x0bdata_source\x18\x14 \x01(\x0b2\'.google.cloud.datacatalog.v1.DataSourceB\x03\xe0A\x03\x12K\n\x10personal_details\x18\x1a \x01(\x0b2,.google.cloud.datacatalog.v1.PersonalDetailsB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:x\xeaAu\n datacatalog.googleapis.com/Entry\x12Qprojects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}B\x0c\n\nentry_typeB\x08\n\x06systemB\r\n\x0bsystem_specB\x0b\n\ttype_specB\x06\n\x04spec"\xcb\x04\n\x11DatabaseTableSpec\x12F\n\x04type\x18\x01 \x01(\x0e28.google.cloud.datacatalog.v1.DatabaseTableSpec.TableType\x12K\n\x0edataplex_table\x18\x02 \x01(\x0b2..google.cloud.datacatalog.v1.DataplexTableSpecB\x03\xe0A\x03\x12[\n\x12database_view_spec\x18\x03 \x01(\x0b2?.google.cloud.datacatalog.v1.DatabaseTableSpec.DatabaseViewSpec\x1a\x80\x02\n\x10DatabaseViewSpec\x12[\n\tview_type\x18\x01 \x01(\x0e2H.google.cloud.datacatalog.v1.DatabaseTableSpec.DatabaseViewSpec.ViewType\x12\x14\n\nbase_table\x18\x02 \x01(\tH\x00\x12\x13\n\tsql_query\x18\x03 \x01(\tH\x00"O\n\x08ViewType\x12\x19\n\x15VIEW_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rSTANDARD_VIEW\x10\x01\x12\x15\n\x11MATERIALIZED_VIEW\x10\x02B\x13\n\x11source_definition"A\n\tTableType\x12\x1a\n\x16TABLE_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06NATIVE\x10\x01\x12\x0c\n\x08EXTERNAL\x10\x02"Y\n\x0bFilesetSpec\x12J\n\x10dataplex_fileset\x18\x01 \x01(\x0b20.google.cloud.datacatalog.v1.DataplexFilesetSpec"q\n\x18DataSourceConnectionSpec\x12U\n\x18bigquery_connection_spec\x18\x01 \x01(\x0b23.google.cloud.datacatalog.v1.BigQueryConnectionSpec"\xc3\x04\n\x0bRoutineSpec\x12J\n\x0croutine_type\x18\x01 \x01(\x0e24.google.cloud.datacatalog.v1.RoutineSpec.RoutineType\x12\x10\n\x08language\x18\x02 \x01(\t\x12L\n\x11routine_arguments\x18\x03 \x03(\x0b21.google.cloud.datacatalog.v1.RoutineSpec.Argument\x12\x13\n\x0breturn_type\x18\x04 \x01(\t\x12\x17\n\x0fdefinition_body\x18\x05 \x01(\t\x12Q\n\x15bigquery_routine_spec\x18\x06 \x01(\x0b20.google.cloud.datacatalog.v1.BigQueryRoutineSpecH\x00\x1a\xa6\x01\n\x08Argument\x12\x0c\n\x04name\x18\x01 \x01(\t\x12D\n\x04mode\x18\x02 \x01(\x0e26.google.cloud.datacatalog.v1.RoutineSpec.Argument.Mode\x12\x0c\n\x04type\x18\x03 \x01(\t"8\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x06\n\x02IN\x10\x01\x12\x07\n\x03OUT\x10\x02\x12\t\n\x05INOUT\x10\x03"O\n\x0bRoutineType\x12\x1c\n\x18ROUTINE_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fSCALAR_FUNCTION\x10\x01\x12\r\n\tPROCEDURE\x10\x02B\r\n\x0bsystem_spec"k\n\x0bDatasetSpec\x12M\n\x13vertex_dataset_spec\x18\x02 \x01(\x0b2..google.cloud.datacatalog.v1.VertexDatasetSpecH\x00B\r\n\x0bsystem_spec"\\\n\x15SqlDatabaseSystemSpec\x12\x12\n\nsql_engine\x18\x01 \x01(\t\x12\x18\n\x10database_version\x18\x02 \x01(\t\x12\x15\n\rinstance_host\x18\x03 \x01(\t"\xca\x01\n\x10LookerSystemSpec\x12\x1a\n\x12parent_instance_id\x18\x01 \x01(\t\x12$\n\x1cparent_instance_display_name\x18\x02 \x01(\t\x12\x17\n\x0fparent_model_id\x18\x03 \x01(\t\x12!\n\x19parent_model_display_name\x18\x04 \x01(\t\x12\x16\n\x0eparent_view_id\x18\x05 \x01(\t\x12 \n\x18parent_view_display_name\x18\x06 \x01(\t"8\n\x17CloudBigtableSystemSpec\x12\x1d\n\x15instance_display_name\x18\x01 \x01(\t"\xfd\x01\n\x19CloudBigtableInstanceSpec\x12u\n\x1ccloud_bigtable_cluster_specs\x18\x01 \x03(\x0b2O.google.cloud.datacatalog.v1.CloudBigtableInstanceSpec.CloudBigtableClusterSpec\x1ai\n\x18CloudBigtableClusterSpec\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x17\n\x0flinked_resource\x18\x04 \x01(\t"|\n\x0bServiceSpec\x12^\n\x1ccloud_bigtable_instance_spec\x18\x01 \x01(\x0b26.google.cloud.datacatalog.v1.CloudBigtableInstanceSpecH\x00B\r\n\x0bsystem_spec"\xa0\x02\n\x15VertexModelSourceInfo\x12W\n\x0bsource_type\x18\x01 \x01(\x0e2B.google.cloud.datacatalog.v1.VertexModelSourceInfo.ModelSourceType\x12\x0c\n\x04copy\x18\x02 \x01(\x08"\x9f\x01\n\x0fModelSourceType\x12!\n\x1dMODEL_SOURCE_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06AUTOML\x10\x01\x12\n\n\x06CUSTOM\x10\x02\x12\x08\n\x04BQML\x10\x03\x12\x10\n\x0cMODEL_GARDEN\x10\x04\x12\t\n\x05GENIE\x10\x05\x12\x19\n\x15CUSTOM_TEXT_EMBEDDING\x10\x06\x12\x0f\n\x0bMARKETPLACE\x10\x07"\xce\x01\n\x0fVertexModelSpec\x12\x12\n\nversion_id\x18\x01 \x01(\t\x12\x17\n\x0fversion_aliases\x18\x02 \x03(\t\x12\x1b\n\x13version_description\x18\x03 \x01(\t\x12T\n\x18vertex_model_source_info\x18\x04 \x01(\x0b22.google.cloud.datacatalog.v1.VertexModelSourceInfo\x12\x1b\n\x13container_image_uri\x18\x05 \x01(\t"\xe4\x02\n\x11VertexDatasetSpec\x12\x17\n\x0fdata_item_count\x18\x01 \x01(\x03\x12J\n\tdata_type\x18\x02 \x01(\x0e27.google.cloud.datacatalog.v1.VertexDatasetSpec.DataType"\xe9\x01\n\x08DataType\x12\x19\n\x15DATA_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05TABLE\x10\x01\x12\t\n\x05IMAGE\x10\x02\x12\x08\n\x04TEXT\x10\x03\x12\t\n\x05VIDEO\x10\x04\x12\x10\n\x0cCONVERSATION\x10\x05\x12\x0f\n\x0bTIME_SERIES\x10\x06\x12\x0c\n\x08DOCUMENT\x10\x07\x12\x12\n\x0eTEXT_TO_SPEECH\x10\x08\x12\x0f\n\x0bTRANSLATION\x10\t\x12\x10\n\x0cSTORE_VISION\x10\n\x12\x1e\n\x1aENTERPRISE_KNOWLEDGE_GRAPH\x10\x0b\x12\x0f\n\x0bTEXT_PROMPT\x10\x0c"e\n\tModelSpec\x12I\n\x11vertex_model_spec\x18\x01 \x01(\x0b2,.google.cloud.datacatalog.v1.VertexModelSpecH\x00B\r\n\x0bsystem_spec"\xbe\x01\n\x16FeatureOnlineStoreSpec\x12Z\n\x0cstorage_type\x18\x01 \x01(\x0e2?.google.cloud.datacatalog.v1.FeatureOnlineStoreSpec.StorageTypeB\x03\xe0A\x03"H\n\x0bStorageType\x12\x1c\n\x18STORAGE_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08BIGTABLE\x10\x01\x12\r\n\tOPTIMIZED\x10\x02"\x8e\x01\n\x0fBusinessContext\x12B\n\x0eentry_overview\x18\x01 \x01(\x0b2*.google.cloud.datacatalog.v1.EntryOverview\x127\n\x08contacts\x18\x02 \x01(\x0b2%.google.cloud.datacatalog.v1.Contacts"!\n\rEntryOverview\x12\x10\n\x08overview\x18\x01 \x01(\t"v\n\x08Contacts\x12<\n\x06people\x18\x01 \x03(\x0b2,.google.cloud.datacatalog.v1.Contacts.Person\x1a,\n\x06Person\x12\x13\n\x0bdesignation\x18\x01 \x01(\t\x12\r\n\x05email\x18\x02 \x01(\t"\xb4\x02\n\nEntryGroup\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12S\n\x17data_catalog_timestamps\x18\x04 \x01(\x0b2-.google.cloud.datacatalog.v1.SystemTimestampsB\x03\xe0A\x03\x12$\n\x17transferred_to_dataplex\x18\t \x01(\x08B\x03\xe0A\x01:m\xeaAj\n%datacatalog.googleapis.com/EntryGroup\x12Aprojects/{project}/locations/{location}/entryGroups/{entry_group}"\xbd\x01\n\x18CreateTagTemplateRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&datacatalog.googleapis.com/TagTemplate\x12\x1c\n\x0ftag_template_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12C\n\x0ctag_template\x18\x02 \x01(\x0b2(.google.cloud.datacatalog.v1.TagTemplateB\x03\xe0A\x02"U\n\x15GetTagTemplateRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&datacatalog.googleapis.com/TagTemplate"\x90\x01\n\x18UpdateTagTemplateRequest\x12C\n\x0ctag_template\x18\x01 \x01(\x0b2(.google.cloud.datacatalog.v1.TagTemplateB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"l\n\x18DeleteTagTemplateRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&datacatalog.googleapis.com/TagTemplate\x12\x12\n\x05force\x18\x02 \x01(\x08B\x03\xe0A\x02"~\n\x10CreateTagRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1edatacatalog.googleapis.com/Tag\x122\n\x03tag\x18\x02 \x01(\x0b2 .google.cloud.datacatalog.v1.TagB\x03\xe0A\x02"w\n\x10UpdateTagRequest\x122\n\x03tag\x18\x01 \x01(\x0b2 .google.cloud.datacatalog.v1.TagB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"H\n\x10DeleteTagRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1edatacatalog.googleapis.com/Tag"\xd3\x01\n\x1dCreateTagTemplateFieldRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&datacatalog.googleapis.com/TagTemplate\x12"\n\x15tag_template_field_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12N\n\x12tag_template_field\x18\x03 \x01(\x0b2-.google.cloud.datacatalog.v1.TagTemplateFieldB\x03\xe0A\x02"\xe8\x01\n\x1dUpdateTagTemplateFieldRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+datacatalog.googleapis.com/TagTemplateField\x12N\n\x12tag_template_field\x18\x02 \x01(\x0b2-.google.cloud.datacatalog.v1.TagTemplateFieldB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\x8a\x01\n\x1dRenameTagTemplateFieldRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+datacatalog.googleapis.com/TagTemplateField\x12&\n\x19new_tag_template_field_id\x18\x02 \x01(\tB\x03\xe0A\x02"\x9e\x01\n&RenameTagTemplateFieldEnumValueRequest\x12J\n\x04name\x18\x01 \x01(\tB<\xe0A\x02\xfaA6\n4datacatalog.googleapis.com/TagTemplateFieldEnumValue\x12(\n\x1bnew_enum_value_display_name\x18\x02 \x01(\tB\x03\xe0A\x02"v\n\x1dDeleteTagTemplateFieldRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+datacatalog.googleapis.com/TagTemplateField\x12\x12\n\x05force\x18\x02 \x01(\x08B\x03\xe0A\x02"p\n\x0fListTagsRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1edatacatalog.googleapis.com/Tag\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"[\n\x10ListTagsResponse\x12.\n\x04tags\x18\x01 \x03(\x0b2 .google.cloud.datacatalog.v1.Tag\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xe4\x01\n\x14ReconcileTagsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n datacatalog.googleapis.com/Entry\x12D\n\x0ctag_template\x18\x02 \x01(\tB.\xe0A\x02\xfaA(\n&datacatalog.googleapis.com/TagTemplate\x12\x1c\n\x14force_delete_missing\x18\x03 \x01(\x08\x12.\n\x04tags\x18\x04 \x03(\x0b2 .google.cloud.datacatalog.v1.Tag"k\n\x15ReconcileTagsResponse\x12\x1a\n\x12created_tags_count\x18\x01 \x01(\x03\x12\x1a\n\x12updated_tags_count\x18\x02 \x01(\x03\x12\x1a\n\x12deleted_tags_count\x18\x03 \x01(\x03"\x93\x03\n\x15ReconcileTagsMetadata\x12U\n\x05state\x18\x01 \x01(\x0e2F.google.cloud.datacatalog.v1.ReconcileTagsMetadata.ReconciliationState\x12N\n\x06errors\x18\x02 \x03(\x0b2>.google.cloud.datacatalog.v1.ReconcileTagsMetadata.ErrorsEntry\x1aA\n\x0bErrorsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b2\x12.google.rpc.Status:\x028\x01"\x8f\x01\n\x13ReconciliationState\x12$\n RECONCILIATION_STATE_UNSPECIFIED\x10\x00\x12\x19\n\x15RECONCILIATION_QUEUED\x10\x01\x12\x1e\n\x1aRECONCILIATION_IN_PROGRESS\x10\x02\x12\x17\n\x13RECONCILIATION_DONE\x10\x03"\xa9\x01\n\x12ListEntriesRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%datacatalog.googleapis.com/EntryGroup\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12-\n\tread_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask"c\n\x13ListEntriesResponse\x123\n\x07entries\x18\x01 \x03(\x0b2".google.cloud.datacatalog.v1.Entry\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"J\n\x10StarEntryRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n datacatalog.googleapis.com/Entry"\x13\n\x11StarEntryResponse"L\n\x12UnstarEntryRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n datacatalog.googleapis.com/Entry"\x15\n\x13UnstarEntryResponse"\x8a\x01\n\x14ImportEntriesRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 datacatalog.googleapis.com/Entry\x12\x19\n\x0fgcs_bucket_path\x18\x02 \x01(\tH\x00\x12\x13\n\x06job_id\x18\x03 \x01(\tB\x03\xe0A\x01B\x08\n\x06source"\x95\x01\n\x15ImportEntriesResponse\x12#\n\x16upserted_entries_count\x18\x05 \x01(\x03H\x00\x88\x01\x01\x12"\n\x15deleted_entries_count\x18\x06 \x01(\x03H\x01\x88\x01\x01B\x19\n\x17_upserted_entries_countB\x18\n\x16_deleted_entries_count"\x88\x02\n\x15ImportEntriesMetadata\x12M\n\x05state\x18\x01 \x01(\x0e2>.google.cloud.datacatalog.v1.ImportEntriesMetadata.ImportState\x12"\n\x06errors\x18\x02 \x03(\x0b2\x12.google.rpc.Status"|\n\x0bImportState\x12\x1c\n\x18IMPORT_STATE_UNSPECIFIED\x10\x00\x12\x11\n\rIMPORT_QUEUED\x10\x01\x12\x16\n\x12IMPORT_IN_PROGRESS\x10\x02\x12\x0f\n\x0bIMPORT_DONE\x10\x03\x12\x13\n\x0fIMPORT_OBSOLETE\x10\x04"\x9d\x01\n\x1aModifyEntryOverviewRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n datacatalog.googleapis.com/Entry\x12G\n\x0eentry_overview\x18\x02 \x01(\x0b2*.google.cloud.datacatalog.v1.EntryOverviewB\x03\xe0A\x02"\x92\x01\n\x1aModifyEntryContactsRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n datacatalog.googleapis.com/Entry\x12<\n\x08contacts\x18\x02 \x01(\x0b2%.google.cloud.datacatalog.v1.ContactsB\x03\xe0A\x02"\xde\x01\n\x10SetConfigRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12S\n\x16tag_template_migration\x18\x02 \x01(\x0e21.google.cloud.datacatalog.v1.TagTemplateMigrationH\x00\x12Q\n\x15catalog_ui_experience\x18\x03 \x01(\x0e20.google.cloud.datacatalog.v1.CatalogUIExperienceH\x00B\x0f\n\rconfiguration"*\n\x15RetrieveConfigRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"3\n\x1eRetrieveEffectiveConfigRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02"\xbe\x01\n\x12OrganizationConfig\x12K\n\x06config\x18\x01 \x03(\x0b2;.google.cloud.datacatalog.v1.OrganizationConfig.ConfigEntry\x1a[\n\x0bConfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12;\n\x05value\x18\x02 \x01(\x0b2,.google.cloud.datacatalog.v1.MigrationConfig:\x028\x01"\xfa\x01\n\x0fMigrationConfig\x12Q\n\x16tag_template_migration\x18\x01 \x01(\x0e21.google.cloud.datacatalog.v1.TagTemplateMigration\x12O\n\x15catalog_ui_experience\x18\x02 \x01(\x0e20.google.cloud.datacatalog.v1.CatalogUIExperience\x12C\n\x1ftemplate_migration_enabled_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp*\xba\x02\n\tEntryType\x12\x1a\n\x16ENTRY_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05TABLE\x10\x02\x12\t\n\x05MODEL\x10\x05\x12\x0f\n\x0bDATA_STREAM\x10\x03\x12\x0b\n\x07FILESET\x10\x04\x12\x0b\n\x07CLUSTER\x10\x06\x12\x0c\n\x08DATABASE\x10\x07\x12\x1a\n\x16DATA_SOURCE_CONNECTION\x10\x08\x12\x0b\n\x07ROUTINE\x10\t\x12\x08\n\x04LAKE\x10\n\x12\x08\n\x04ZONE\x10\x0b\x12\x0b\n\x07SERVICE\x10\x0e\x12\x13\n\x0fDATABASE_SCHEMA\x10\x0f\x12\r\n\tDASHBOARD\x10\x10\x12\x0b\n\x07EXPLORE\x10\x11\x12\x08\n\x04LOOK\x10\x12\x12\x18\n\x14FEATURE_ONLINE_STORE\x10\x13\x12\x10\n\x0cFEATURE_VIEW\x10\x14\x12\x11\n\rFEATURE_GROUP\x10\x15*\x87\x01\n\x14TagTemplateMigration\x12&\n"TAG_TEMPLATE_MIGRATION_UNSPECIFIED\x10\x00\x12"\n\x1eTAG_TEMPLATE_MIGRATION_ENABLED\x10\x01\x12#\n\x1fTAG_TEMPLATE_MIGRATION_DISABLED\x10\x02*\x83\x01\n\x13CatalogUIExperience\x12%\n!CATALOG_UI_EXPERIENCE_UNSPECIFIED\x10\x00\x12!\n\x1dCATALOG_UI_EXPERIENCE_ENABLED\x10\x01\x12"\n\x1eCATALOG_UI_EXPERIENCE_DISABLED\x10\x022\xd2A\n\x0bDataCatalog\x12\xa6\x01\n\rSearchCatalog\x121.google.cloud.datacatalog.v1.SearchCatalogRequest\x1a2.google.cloud.datacatalog.v1.SearchCatalogResponse".\x88\x02\x01\xdaA\x0bscope,query\x82\xd3\xe4\x93\x02\x17"\x12/v1/catalog:search:\x01*\x12\xde\x01\n\x10CreateEntryGroup\x124.google.cloud.datacatalog.v1.CreateEntryGroupRequest\x1a\'.google.cloud.datacatalog.v1.EntryGroup"k\x88\x02\x01\xdaA!parent,entry_group_id,entry_group\x82\xd3\xe4\x93\x02>"//v1/{parent=projects/*/locations/*}/entryGroups:\x0bentry_group\x12\xbf\x01\n\rGetEntryGroup\x121.google.cloud.datacatalog.v1.GetEntryGroupRequest\x1a\'.google.cloud.datacatalog.v1.EntryGroup"R\x88\x02\x01\xdaA\x04name\xdaA\x0ename,read_mask\x82\xd3\xe4\x93\x021\x12//v1/{name=projects/*/locations/*/entryGroups/*}\x12\xee\x01\n\x10UpdateEntryGroup\x124.google.cloud.datacatalog.v1.UpdateEntryGroupRequest\x1a\'.google.cloud.datacatalog.v1.EntryGroup"{\x88\x02\x01\xdaA\x0bentry_group\xdaA\x17entry_group,update_mask\x82\xd3\xe4\x93\x02J2;/v1/{entry_group.name=projects/*/locations/*/entryGroups/*}:\x0bentry_group\x12\xa3\x01\n\x10DeleteEntryGroup\x124.google.cloud.datacatalog.v1.DeleteEntryGroupRequest\x1a\x16.google.protobuf.Empty"A\x88\x02\x01\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1/{name=projects/*/locations/*/entryGroups/*}\x12\xc1\x01\n\x0fListEntryGroups\x123.google.cloud.datacatalog.v1.ListEntryGroupsRequest\x1a4.google.cloud.datacatalog.v1.ListEntryGroupsResponse"C\x88\x02\x01\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=projects/*/locations/*}/entryGroups\x12\xc7\x01\n\x0bCreateEntry\x12/.google.cloud.datacatalog.v1.CreateEntryRequest\x1a".google.cloud.datacatalog.v1.Entry"c\x88\x02\x01\xdaA\x15parent,entry_id,entry\x82\xd3\xe4\x93\x02B"9/v1/{parent=projects/*/locations/*/entryGroups/*}/entries:\x05entry\x12\xd1\x01\n\x0bUpdateEntry\x12/.google.cloud.datacatalog.v1.UpdateEntryRequest\x1a".google.cloud.datacatalog.v1.Entry"m\x88\x02\x01\xdaA\x05entry\xdaA\x11entry,update_mask\x82\xd3\xe4\x93\x02H2?/v1/{entry.name=projects/*/locations/*/entryGroups/*/entries/*}:\x05entry\x12\xa3\x01\n\x0bDeleteEntry\x12/.google.cloud.datacatalog.v1.DeleteEntryRequest\x1a\x16.google.protobuf.Empty"K\x88\x02\x01\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v1/{name=projects/*/locations/*/entryGroups/*/entries/*}\x12\xa9\x01\n\x08GetEntry\x12,.google.cloud.datacatalog.v1.GetEntryRequest\x1a".google.cloud.datacatalog.v1.Entry"K\x88\x02\x01\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v1/{name=projects/*/locations/*/entryGroups/*/entries/*}\x12\x81\x01\n\x0bLookupEntry\x12/.google.cloud.datacatalog.v1.LookupEntryRequest\x1a".google.cloud.datacatalog.v1.Entry"\x1d\x88\x02\x01\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/entries:lookup\x12\xbf\x01\n\x0bListEntries\x12/.google.cloud.datacatalog.v1.ListEntriesRequest\x1a0.google.cloud.datacatalog.v1.ListEntriesResponse"M\x88\x02\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v1/{parent=projects/*/locations/*/entryGroups/*}/entries\x12\xd7\x01\n\x13ModifyEntryOverview\x127.google.cloud.datacatalog.v1.ModifyEntryOverviewRequest\x1a*.google.cloud.datacatalog.v1.EntryOverview"[\x88\x02\x01\x82\xd3\xe4\x93\x02R"M/v1/{name=projects/*/locations/*/entryGroups/*/entries/*}:modifyEntryOverview:\x01*\x12\xd2\x01\n\x13ModifyEntryContacts\x127.google.cloud.datacatalog.v1.ModifyEntryContactsRequest\x1a%.google.cloud.datacatalog.v1.Contacts"[\x88\x02\x01\x82\xd3\xe4\x93\x02R"M/v1/{name=projects/*/locations/*/entryGroups/*/entries/*}:modifyEntryContacts:\x01*\x12\xe5\x01\n\x11CreateTagTemplate\x125.google.cloud.datacatalog.v1.CreateTagTemplateRequest\x1a(.google.cloud.datacatalog.v1.TagTemplate"o\x88\x02\x01\xdaA#parent,tag_template_id,tag_template\x82\xd3\xe4\x93\x02@"0/v1/{parent=projects/*/locations/*}/tagTemplates:\x0ctag_template\x12\xb2\x01\n\x0eGetTagTemplate\x122.google.cloud.datacatalog.v1.GetTagTemplateRequest\x1a(.google.cloud.datacatalog.v1.TagTemplate"B\x88\x02\x01\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v1/{name=projects/*/locations/*/tagTemplates/*}\x12\xf7\x01\n\x11UpdateTagTemplate\x125.google.cloud.datacatalog.v1.UpdateTagTemplateRequest\x1a(.google.cloud.datacatalog.v1.TagTemplate"\x80\x01\x88\x02\x01\xdaA\x0ctag_template\xdaA\x18tag_template,update_mask\x82\xd3\xe4\x93\x02M2=/v1/{tag_template.name=projects/*/locations/*/tagTemplates/*}:\x0ctag_template\x12\xac\x01\n\x11DeleteTagTemplate\x125.google.cloud.datacatalog.v1.DeleteTagTemplateRequest\x1a\x16.google.protobuf.Empty"H\x88\x02\x01\xdaA\nname,force\x82\xd3\xe4\x93\x022*0/v1/{name=projects/*/locations/*/tagTemplates/*}\x12\x90\x02\n\x16CreateTagTemplateField\x12:.google.cloud.datacatalog.v1.CreateTagTemplateFieldRequest\x1a-.google.cloud.datacatalog.v1.TagTemplateField"\x8a\x01\x88\x02\x01\xdaA/parent,tag_template_field_id,tag_template_field\x82\xd3\xe4\x93\x02O"9/v1/{parent=projects/*/locations/*/tagTemplates/*}/fields:\x12tag_template_field\x12\x9e\x02\n\x16UpdateTagTemplateField\x12:.google.cloud.datacatalog.v1.UpdateTagTemplateFieldRequest\x1a-.google.cloud.datacatalog.v1.TagTemplateField"\x98\x01\x88\x02\x01\xdaA\x17name,tag_template_field\xdaA#name,tag_template_field,update_mask\x82\xd3\xe4\x93\x02O29/v1/{name=projects/*/locations/*/tagTemplates/*/fields/*}:\x12tag_template_field\x12\xf4\x01\n\x16RenameTagTemplateField\x12:.google.cloud.datacatalog.v1.RenameTagTemplateFieldRequest\x1a-.google.cloud.datacatalog.v1.TagTemplateField"o\x88\x02\x01\xdaA\x1ename,new_tag_template_field_id\x82\xd3\xe4\x93\x02E"@/v1/{name=projects/*/locations/*/tagTemplates/*/fields/*}:rename:\x01*\x12\x95\x02\n\x1fRenameTagTemplateFieldEnumValue\x12C.google.cloud.datacatalog.v1.RenameTagTemplateFieldEnumValueRequest\x1a-.google.cloud.datacatalog.v1.TagTemplateField"~\x88\x02\x01\xdaA name,new_enum_value_display_name\x82\xd3\xe4\x93\x02R"M/v1/{name=projects/*/locations/*/tagTemplates/*/fields/*/enumValues/*}:rename:\x01*\x12\xbf\x01\n\x16DeleteTagTemplateField\x12:.google.cloud.datacatalog.v1.DeleteTagTemplateFieldRequest\x1a\x16.google.protobuf.Empty"Q\x88\x02\x01\xdaA\nname,force\x82\xd3\xe4\x93\x02;*9/v1/{name=projects/*/locations/*/tagTemplates/*/fields/*}\x12\xfc\x01\n\tCreateTag\x12-.google.cloud.datacatalog.v1.CreateTagRequest\x1a .google.cloud.datacatalog.v1.Tag"\x9d\x01\x88\x02\x01\xdaA\nparent,tag\x82\xd3\xe4\x93\x02\x86\x01"@/v1/{parent=projects/*/locations/*/entryGroups/*/entries/*}/tags:\x03tagZ="6/v1/{parent=projects/*/locations/*/entryGroups/*}/tags:\x03tag\x12\x8f\x02\n\tUpdateTag\x12-.google.cloud.datacatalog.v1.UpdateTagRequest\x1a .google.cloud.datacatalog.v1.Tag"\xb0\x01\x88\x02\x01\xdaA\x03tag\xdaA\x0ftag,update_mask\x82\xd3\xe4\x93\x02\x8e\x012D/v1/{tag.name=projects/*/locations/*/entryGroups/*/entries/*/tags/*}:\x03tagZA2:/v1/{tag.name=projects/*/locations/*/entryGroups/*/tags/*}:\x03tag\x12\xe1\x01\n\tDeleteTag\x12-.google.cloud.datacatalog.v1.DeleteTagRequest\x1a\x16.google.protobuf.Empty"\x8c\x01\x88\x02\x01\xdaA\x04name\x82\xd3\xe4\x93\x02|*@/v1/{name=projects/*/locations/*/entryGroups/*/entries/*/tags/*}Z8*6/v1/{name=projects/*/locations/*/entryGroups/*/tags/*}\x12\xf8\x01\n\x08ListTags\x12,.google.cloud.datacatalog.v1.ListTagsRequest\x1a-.google.cloud.datacatalog.v1.ListTagsResponse"\x8e\x01\x88\x02\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02|\x12@/v1/{parent=projects/*/locations/*/entryGroups/*/entries/*}/tagsZ8\x126/v1/{parent=projects/*/locations/*/entryGroups/*}/tags\x12\xed\x01\n\rReconcileTags\x121.google.cloud.datacatalog.v1.ReconcileTagsRequest\x1a\x1d.google.longrunning.Operation"\x89\x01\x88\x02\x01\xcaA.\n\x15ReconcileTagsResponse\x12\x15ReconcileTagsMetadata\x82\xd3\xe4\x93\x02O"J/v1/{parent=projects/*/locations/*/entryGroups/*/entries/*}/tags:reconcile:\x01*\x12\xbf\x01\n\tStarEntry\x12-.google.cloud.datacatalog.v1.StarEntryRequest\x1a..google.cloud.datacatalog.v1.StarEntryResponse"S\x88\x02\x01\xdaA\x04name\x82\xd3\xe4\x93\x02C">/v1/{name=projects/*/locations/*/entryGroups/*/entries/*}:star:\x01*\x12\xc7\x01\n\x0bUnstarEntry\x12/.google.cloud.datacatalog.v1.UnstarEntryRequest\x1a0.google.cloud.datacatalog.v1.UnstarEntryResponse"U\x88\x02\x01\xdaA\x04name\x82\xd3\xe4\x93\x02E"@/v1/{name=projects/*/locations/*/entryGroups/*/entries/*}:unstar:\x01*\x12\xf5\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"\xa9\x01\x88\x02\x01\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02\x8d\x01"A/v1/{resource=projects/*/locations/*/tagTemplates/*}:setIamPolicy:\x01*ZE"@/v1/{resource=projects/*/locations/*/entryGroups/*}:setIamPolicy:\x01*\x12\xbf\x02\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"\xf3\x01\x88\x02\x01\xdaA\x08resource\x82\xd3\xe4\x93\x02\xde\x01"A/v1/{resource=projects/*/locations/*/tagTemplates/*}:getIamPolicy:\x01*ZE"@/v1/{resource=projects/*/locations/*/entryGroups/*}:getIamPolicy:\x01*ZO"J/v1/{resource=projects/*/locations/*/entryGroups/*/entries/*}:getIamPolicy:\x01*\x12\xe6\x02\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"\xfa\x01\x88\x02\x01\x82\xd3\xe4\x93\x02\xf0\x01"G/v1/{resource=projects/*/locations/*/tagTemplates/*}:testIamPermissions:\x01*ZK"F/v1/{resource=projects/*/locations/*/entryGroups/*}:testIamPermissions:\x01*ZU"P/v1/{resource=projects/*/locations/*/entryGroups/*/entries/*}:testIamPermissions:\x01*\x12\xe2\x01\n\rImportEntries\x121.google.cloud.datacatalog.v1.ImportEntriesRequest\x1a\x1d.google.longrunning.Operation"\x7f\x88\x02\x01\xcaA.\n\x15ImportEntriesResponse\x12\x15ImportEntriesMetadata\x82\xd3\xe4\x93\x02E"@/v1/{parent=projects/*/locations/*/entryGroups/*}/entries:import:\x01*\x12\xda\x01\n\tSetConfig\x12-.google.cloud.datacatalog.v1.SetConfigRequest\x1a,.google.cloud.datacatalog.v1.MigrationConfig"p\x88\x02\x01\x82\xd3\xe4\x93\x02g"0/v1/{name=organizations/*/locations/*}:setConfig:\x01*Z0"+/v1/{name=projects/*/locations/*}:setConfig:\x01*\x12\xb7\x01\n\x0eRetrieveConfig\x122.google.cloud.datacatalog.v1.RetrieveConfigRequest\x1a/.google.cloud.datacatalog.v1.OrganizationConfig"@\x88\x02\x01\x82\xd3\xe4\x93\x027\x125/v1/{name=organizations/*/locations/*}:retrieveConfig\x12\x8d\x02\n\x17RetrieveEffectiveConfig\x12;.google.cloud.datacatalog.v1.RetrieveEffectiveConfigRequest\x1a,.google.cloud.datacatalog.v1.MigrationConfig"\x86\x01\x88\x02\x01\x82\xd3\xe4\x93\x02}\x12>/v1/{name=organizations/*/locations/*}:retrieveEffectiveConfigZ;\x129/v1/{name=projects/*/locations/*}:retrieveEffectiveConfig\x1aQ\x88\x02\x01\xcaA\x1adatacatalog.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x87\x03\n\x1fcom.google.cloud.datacatalog.v1P\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1\xeaA\xc0\x01\n4datacatalog.googleapis.com/TagTemplateFieldEnumValue\x12\x87\x01projects/{project}/locations/{location}/tagTemplates/{tag_template}/fields/{tag_template_field_id}/enumValues/{enum_value_display_name}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datacatalog.v1.datacatalog_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.datacatalog.v1P\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1\xeaA\xc0\x01\n4datacatalog.googleapis.com/TagTemplateFieldEnumValue\x12\x87\x01projects/{project}/locations/{location}/tagTemplates/{tag_template}/fields/{tag_template_field_id}/enumValues/{enum_value_display_name}'
    _globals['_SEARCHCATALOGREQUEST_SCOPE'].fields_by_name['restricted_locations']._loaded_options = None
    _globals['_SEARCHCATALOGREQUEST_SCOPE'].fields_by_name['restricted_locations']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHCATALOGREQUEST_SCOPE'].fields_by_name['starred_only']._loaded_options = None
    _globals['_SEARCHCATALOGREQUEST_SCOPE'].fields_by_name['starred_only']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHCATALOGREQUEST_SCOPE'].fields_by_name['include_public_tag_templates']._loaded_options = None
    _globals['_SEARCHCATALOGREQUEST_SCOPE'].fields_by_name['include_public_tag_templates']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_SEARCHCATALOGREQUEST'].fields_by_name['scope']._loaded_options = None
    _globals['_SEARCHCATALOGREQUEST'].fields_by_name['scope']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHCATALOGREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_SEARCHCATALOGREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHCATALOGREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_SEARCHCATALOGREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHCATALOGREQUEST'].fields_by_name['admin_search']._loaded_options = None
    _globals['_SEARCHCATALOGREQUEST'].fields_by_name['admin_search']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEENTRYGROUPREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEENTRYGROUPREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%datacatalog.googleapis.com/EntryGroup"
    _globals['_CREATEENTRYGROUPREQUEST'].fields_by_name['entry_group_id']._loaded_options = None
    _globals['_CREATEENTRYGROUPREQUEST'].fields_by_name['entry_group_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEENTRYGROUPREQUEST'].fields_by_name['entry_group']._loaded_options = None
    _globals['_UPDATEENTRYGROUPREQUEST'].fields_by_name['entry_group']._serialized_options = b'\xe0A\x02'
    _globals['_GETENTRYGROUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENTRYGROUPREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%datacatalog.googleapis.com/EntryGroup"
    _globals['_DELETEENTRYGROUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEENTRYGROUPREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%datacatalog.googleapis.com/EntryGroup"
    _globals['_DELETEENTRYGROUPREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETEENTRYGROUPREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENTRYGROUPSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENTRYGROUPSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%datacatalog.googleapis.com/EntryGroup"
    _globals['_LISTENTRYGROUPSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTENTRYGROUPSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENTRYGROUPSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTENTRYGROUPSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEENTRYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEENTRYREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%datacatalog.googleapis.com/EntryGroup"
    _globals['_CREATEENTRYREQUEST'].fields_by_name['entry_id']._loaded_options = None
    _globals['_CREATEENTRYREQUEST'].fields_by_name['entry_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEENTRYREQUEST'].fields_by_name['entry']._loaded_options = None
    _globals['_CREATEENTRYREQUEST'].fields_by_name['entry']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEENTRYREQUEST'].fields_by_name['entry']._loaded_options = None
    _globals['_UPDATEENTRYREQUEST'].fields_by_name['entry']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEENTRYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEENTRYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n datacatalog.googleapis.com/Entry'
    _globals['_GETENTRYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENTRYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n datacatalog.googleapis.com/Entry'
    _globals['_ENTRY_LABELSENTRY']._loaded_options = None
    _globals['_ENTRY_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ENTRY'].fields_by_name['name']._loaded_options = None
    _globals['_ENTRY'].fields_by_name['name']._serialized_options = b"\xe0A\x03\xe0A\x08\xfaA'\n%datacatalog.googleapis.com/EntryGroup"
    _globals['_ENTRY'].fields_by_name['integrated_system']._loaded_options = None
    _globals['_ENTRY'].fields_by_name['integrated_system']._serialized_options = b'\xe0A\x03'
    _globals['_ENTRY'].fields_by_name['bigquery_table_spec']._loaded_options = None
    _globals['_ENTRY'].fields_by_name['bigquery_table_spec']._serialized_options = b'\xe0A\x03'
    _globals['_ENTRY'].fields_by_name['bigquery_date_sharded_spec']._loaded_options = None
    _globals['_ENTRY'].fields_by_name['bigquery_date_sharded_spec']._serialized_options = b'\xe0A\x03'
    _globals['_ENTRY'].fields_by_name['data_source']._loaded_options = None
    _globals['_ENTRY'].fields_by_name['data_source']._serialized_options = b'\xe0A\x03'
    _globals['_ENTRY'].fields_by_name['personal_details']._loaded_options = None
    _globals['_ENTRY'].fields_by_name['personal_details']._serialized_options = b'\xe0A\x03'
    _globals['_ENTRY']._loaded_options = None
    _globals['_ENTRY']._serialized_options = b'\xeaAu\n datacatalog.googleapis.com/Entry\x12Qprojects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}'
    _globals['_DATABASETABLESPEC'].fields_by_name['dataplex_table']._loaded_options = None
    _globals['_DATABASETABLESPEC'].fields_by_name['dataplex_table']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREONLINESTORESPEC'].fields_by_name['storage_type']._loaded_options = None
    _globals['_FEATUREONLINESTORESPEC'].fields_by_name['storage_type']._serialized_options = b'\xe0A\x03'
    _globals['_ENTRYGROUP'].fields_by_name['name']._loaded_options = None
    _globals['_ENTRYGROUP'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ENTRYGROUP'].fields_by_name['data_catalog_timestamps']._loaded_options = None
    _globals['_ENTRYGROUP'].fields_by_name['data_catalog_timestamps']._serialized_options = b'\xe0A\x03'
    _globals['_ENTRYGROUP'].fields_by_name['transferred_to_dataplex']._loaded_options = None
    _globals['_ENTRYGROUP'].fields_by_name['transferred_to_dataplex']._serialized_options = b'\xe0A\x01'
    _globals['_ENTRYGROUP']._loaded_options = None
    _globals['_ENTRYGROUP']._serialized_options = b'\xeaAj\n%datacatalog.googleapis.com/EntryGroup\x12Aprojects/{project}/locations/{location}/entryGroups/{entry_group}'
    _globals['_CREATETAGTEMPLATEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETAGTEMPLATEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&datacatalog.googleapis.com/TagTemplate'
    _globals['_CREATETAGTEMPLATEREQUEST'].fields_by_name['tag_template_id']._loaded_options = None
    _globals['_CREATETAGTEMPLATEREQUEST'].fields_by_name['tag_template_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETAGTEMPLATEREQUEST'].fields_by_name['tag_template']._loaded_options = None
    _globals['_CREATETAGTEMPLATEREQUEST'].fields_by_name['tag_template']._serialized_options = b'\xe0A\x02'
    _globals['_GETTAGTEMPLATEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTAGTEMPLATEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&datacatalog.googleapis.com/TagTemplate'
    _globals['_UPDATETAGTEMPLATEREQUEST'].fields_by_name['tag_template']._loaded_options = None
    _globals['_UPDATETAGTEMPLATEREQUEST'].fields_by_name['tag_template']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETAGTEMPLATEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETAGTEMPLATEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&datacatalog.googleapis.com/TagTemplate'
    _globals['_DELETETAGTEMPLATEREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETETAGTEMPLATEREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETAGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETAGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1edatacatalog.googleapis.com/Tag'
    _globals['_CREATETAGREQUEST'].fields_by_name['tag']._loaded_options = None
    _globals['_CREATETAGREQUEST'].fields_by_name['tag']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETAGREQUEST'].fields_by_name['tag']._loaded_options = None
    _globals['_UPDATETAGREQUEST'].fields_by_name['tag']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETAGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETAGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \x12\x1edatacatalog.googleapis.com/Tag'
    _globals['_CREATETAGTEMPLATEFIELDREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETAGTEMPLATEFIELDREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\n&datacatalog.googleapis.com/TagTemplate'
    _globals['_CREATETAGTEMPLATEFIELDREQUEST'].fields_by_name['tag_template_field_id']._loaded_options = None
    _globals['_CREATETAGTEMPLATEFIELDREQUEST'].fields_by_name['tag_template_field_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETAGTEMPLATEFIELDREQUEST'].fields_by_name['tag_template_field']._loaded_options = None
    _globals['_CREATETAGTEMPLATEFIELDREQUEST'].fields_by_name['tag_template_field']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETAGTEMPLATEFIELDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATETAGTEMPLATEFIELDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+datacatalog.googleapis.com/TagTemplateField'
    _globals['_UPDATETAGTEMPLATEFIELDREQUEST'].fields_by_name['tag_template_field']._loaded_options = None
    _globals['_UPDATETAGTEMPLATEFIELDREQUEST'].fields_by_name['tag_template_field']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETAGTEMPLATEFIELDREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATETAGTEMPLATEFIELDREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_RENAMETAGTEMPLATEFIELDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RENAMETAGTEMPLATEFIELDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+datacatalog.googleapis.com/TagTemplateField'
    _globals['_RENAMETAGTEMPLATEFIELDREQUEST'].fields_by_name['new_tag_template_field_id']._loaded_options = None
    _globals['_RENAMETAGTEMPLATEFIELDREQUEST'].fields_by_name['new_tag_template_field_id']._serialized_options = b'\xe0A\x02'
    _globals['_RENAMETAGTEMPLATEFIELDENUMVALUEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RENAMETAGTEMPLATEFIELDENUMVALUEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA6\n4datacatalog.googleapis.com/TagTemplateFieldEnumValue'
    _globals['_RENAMETAGTEMPLATEFIELDENUMVALUEREQUEST'].fields_by_name['new_enum_value_display_name']._loaded_options = None
    _globals['_RENAMETAGTEMPLATEFIELDENUMVALUEREQUEST'].fields_by_name['new_enum_value_display_name']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETAGTEMPLATEFIELDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETAGTEMPLATEFIELDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+datacatalog.googleapis.com/TagTemplateField'
    _globals['_DELETETAGTEMPLATEFIELDREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETETAGTEMPLATEFIELDREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x02'
    _globals['_LISTTAGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTAGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1edatacatalog.googleapis.com/Tag'
    _globals['_RECONCILETAGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_RECONCILETAGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n datacatalog.googleapis.com/Entry'
    _globals['_RECONCILETAGSREQUEST'].fields_by_name['tag_template']._loaded_options = None
    _globals['_RECONCILETAGSREQUEST'].fields_by_name['tag_template']._serialized_options = b'\xe0A\x02\xfaA(\n&datacatalog.googleapis.com/TagTemplate'
    _globals['_RECONCILETAGSMETADATA_ERRORSENTRY']._loaded_options = None
    _globals['_RECONCILETAGSMETADATA_ERRORSENTRY']._serialized_options = b'8\x01'
    _globals['_LISTENTRIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENTRIESREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%datacatalog.googleapis.com/EntryGroup"
    _globals['_STARENTRYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STARENTRYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n datacatalog.googleapis.com/Entry'
    _globals['_UNSTARENTRYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UNSTARENTRYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n datacatalog.googleapis.com/Entry'
    _globals['_IMPORTENTRIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTENTRIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 datacatalog.googleapis.com/Entry'
    _globals['_IMPORTENTRIESREQUEST'].fields_by_name['job_id']._loaded_options = None
    _globals['_IMPORTENTRIESREQUEST'].fields_by_name['job_id']._serialized_options = b'\xe0A\x01'
    _globals['_MODIFYENTRYOVERVIEWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_MODIFYENTRYOVERVIEWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n datacatalog.googleapis.com/Entry'
    _globals['_MODIFYENTRYOVERVIEWREQUEST'].fields_by_name['entry_overview']._loaded_options = None
    _globals['_MODIFYENTRYOVERVIEWREQUEST'].fields_by_name['entry_overview']._serialized_options = b'\xe0A\x02'
    _globals['_MODIFYENTRYCONTACTSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_MODIFYENTRYCONTACTSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n datacatalog.googleapis.com/Entry'
    _globals['_MODIFYENTRYCONTACTSREQUEST'].fields_by_name['contacts']._loaded_options = None
    _globals['_MODIFYENTRYCONTACTSREQUEST'].fields_by_name['contacts']._serialized_options = b'\xe0A\x02'
    _globals['_SETCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_SETCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_RETRIEVECONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RETRIEVECONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_RETRIEVEEFFECTIVECONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RETRIEVEEFFECTIVECONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_ORGANIZATIONCONFIG_CONFIGENTRY']._loaded_options = None
    _globals['_ORGANIZATIONCONFIG_CONFIGENTRY']._serialized_options = b'8\x01'
    _globals['_DATACATALOG']._loaded_options = None
    _globals['_DATACATALOG']._serialized_options = b'\x88\x02\x01\xcaA\x1adatacatalog.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DATACATALOG'].methods_by_name['SearchCatalog']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['SearchCatalog']._serialized_options = b'\x88\x02\x01\xdaA\x0bscope,query\x82\xd3\xe4\x93\x02\x17"\x12/v1/catalog:search:\x01*'
    _globals['_DATACATALOG'].methods_by_name['CreateEntryGroup']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['CreateEntryGroup']._serialized_options = b'\x88\x02\x01\xdaA!parent,entry_group_id,entry_group\x82\xd3\xe4\x93\x02>"//v1/{parent=projects/*/locations/*}/entryGroups:\x0bentry_group'
    _globals['_DATACATALOG'].methods_by_name['GetEntryGroup']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['GetEntryGroup']._serialized_options = b'\x88\x02\x01\xdaA\x04name\xdaA\x0ename,read_mask\x82\xd3\xe4\x93\x021\x12//v1/{name=projects/*/locations/*/entryGroups/*}'
    _globals['_DATACATALOG'].methods_by_name['UpdateEntryGroup']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['UpdateEntryGroup']._serialized_options = b'\x88\x02\x01\xdaA\x0bentry_group\xdaA\x17entry_group,update_mask\x82\xd3\xe4\x93\x02J2;/v1/{entry_group.name=projects/*/locations/*/entryGroups/*}:\x0bentry_group'
    _globals['_DATACATALOG'].methods_by_name['DeleteEntryGroup']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['DeleteEntryGroup']._serialized_options = b'\x88\x02\x01\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1/{name=projects/*/locations/*/entryGroups/*}'
    _globals['_DATACATALOG'].methods_by_name['ListEntryGroups']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['ListEntryGroups']._serialized_options = b'\x88\x02\x01\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=projects/*/locations/*}/entryGroups'
    _globals['_DATACATALOG'].methods_by_name['CreateEntry']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['CreateEntry']._serialized_options = b'\x88\x02\x01\xdaA\x15parent,entry_id,entry\x82\xd3\xe4\x93\x02B"9/v1/{parent=projects/*/locations/*/entryGroups/*}/entries:\x05entry'
    _globals['_DATACATALOG'].methods_by_name['UpdateEntry']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['UpdateEntry']._serialized_options = b'\x88\x02\x01\xdaA\x05entry\xdaA\x11entry,update_mask\x82\xd3\xe4\x93\x02H2?/v1/{entry.name=projects/*/locations/*/entryGroups/*/entries/*}:\x05entry'
    _globals['_DATACATALOG'].methods_by_name['DeleteEntry']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['DeleteEntry']._serialized_options = b'\x88\x02\x01\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v1/{name=projects/*/locations/*/entryGroups/*/entries/*}'
    _globals['_DATACATALOG'].methods_by_name['GetEntry']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['GetEntry']._serialized_options = b'\x88\x02\x01\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v1/{name=projects/*/locations/*/entryGroups/*/entries/*}'
    _globals['_DATACATALOG'].methods_by_name['LookupEntry']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['LookupEntry']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/entries:lookup'
    _globals['_DATACATALOG'].methods_by_name['ListEntries']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['ListEntries']._serialized_options = b'\x88\x02\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v1/{parent=projects/*/locations/*/entryGroups/*}/entries'
    _globals['_DATACATALOG'].methods_by_name['ModifyEntryOverview']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['ModifyEntryOverview']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x02R"M/v1/{name=projects/*/locations/*/entryGroups/*/entries/*}:modifyEntryOverview:\x01*'
    _globals['_DATACATALOG'].methods_by_name['ModifyEntryContacts']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['ModifyEntryContacts']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x02R"M/v1/{name=projects/*/locations/*/entryGroups/*/entries/*}:modifyEntryContacts:\x01*'
    _globals['_DATACATALOG'].methods_by_name['CreateTagTemplate']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['CreateTagTemplate']._serialized_options = b'\x88\x02\x01\xdaA#parent,tag_template_id,tag_template\x82\xd3\xe4\x93\x02@"0/v1/{parent=projects/*/locations/*}/tagTemplates:\x0ctag_template'
    _globals['_DATACATALOG'].methods_by_name['GetTagTemplate']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['GetTagTemplate']._serialized_options = b'\x88\x02\x01\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v1/{name=projects/*/locations/*/tagTemplates/*}'
    _globals['_DATACATALOG'].methods_by_name['UpdateTagTemplate']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['UpdateTagTemplate']._serialized_options = b'\x88\x02\x01\xdaA\x0ctag_template\xdaA\x18tag_template,update_mask\x82\xd3\xe4\x93\x02M2=/v1/{tag_template.name=projects/*/locations/*/tagTemplates/*}:\x0ctag_template'
    _globals['_DATACATALOG'].methods_by_name['DeleteTagTemplate']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['DeleteTagTemplate']._serialized_options = b'\x88\x02\x01\xdaA\nname,force\x82\xd3\xe4\x93\x022*0/v1/{name=projects/*/locations/*/tagTemplates/*}'
    _globals['_DATACATALOG'].methods_by_name['CreateTagTemplateField']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['CreateTagTemplateField']._serialized_options = b'\x88\x02\x01\xdaA/parent,tag_template_field_id,tag_template_field\x82\xd3\xe4\x93\x02O"9/v1/{parent=projects/*/locations/*/tagTemplates/*}/fields:\x12tag_template_field'
    _globals['_DATACATALOG'].methods_by_name['UpdateTagTemplateField']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['UpdateTagTemplateField']._serialized_options = b'\x88\x02\x01\xdaA\x17name,tag_template_field\xdaA#name,tag_template_field,update_mask\x82\xd3\xe4\x93\x02O29/v1/{name=projects/*/locations/*/tagTemplates/*/fields/*}:\x12tag_template_field'
    _globals['_DATACATALOG'].methods_by_name['RenameTagTemplateField']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['RenameTagTemplateField']._serialized_options = b'\x88\x02\x01\xdaA\x1ename,new_tag_template_field_id\x82\xd3\xe4\x93\x02E"@/v1/{name=projects/*/locations/*/tagTemplates/*/fields/*}:rename:\x01*'
    _globals['_DATACATALOG'].methods_by_name['RenameTagTemplateFieldEnumValue']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['RenameTagTemplateFieldEnumValue']._serialized_options = b'\x88\x02\x01\xdaA name,new_enum_value_display_name\x82\xd3\xe4\x93\x02R"M/v1/{name=projects/*/locations/*/tagTemplates/*/fields/*/enumValues/*}:rename:\x01*'
    _globals['_DATACATALOG'].methods_by_name['DeleteTagTemplateField']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['DeleteTagTemplateField']._serialized_options = b'\x88\x02\x01\xdaA\nname,force\x82\xd3\xe4\x93\x02;*9/v1/{name=projects/*/locations/*/tagTemplates/*/fields/*}'
    _globals['_DATACATALOG'].methods_by_name['CreateTag']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['CreateTag']._serialized_options = b'\x88\x02\x01\xdaA\nparent,tag\x82\xd3\xe4\x93\x02\x86\x01"@/v1/{parent=projects/*/locations/*/entryGroups/*/entries/*}/tags:\x03tagZ="6/v1/{parent=projects/*/locations/*/entryGroups/*}/tags:\x03tag'
    _globals['_DATACATALOG'].methods_by_name['UpdateTag']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['UpdateTag']._serialized_options = b'\x88\x02\x01\xdaA\x03tag\xdaA\x0ftag,update_mask\x82\xd3\xe4\x93\x02\x8e\x012D/v1/{tag.name=projects/*/locations/*/entryGroups/*/entries/*/tags/*}:\x03tagZA2:/v1/{tag.name=projects/*/locations/*/entryGroups/*/tags/*}:\x03tag'
    _globals['_DATACATALOG'].methods_by_name['DeleteTag']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['DeleteTag']._serialized_options = b'\x88\x02\x01\xdaA\x04name\x82\xd3\xe4\x93\x02|*@/v1/{name=projects/*/locations/*/entryGroups/*/entries/*/tags/*}Z8*6/v1/{name=projects/*/locations/*/entryGroups/*/tags/*}'
    _globals['_DATACATALOG'].methods_by_name['ListTags']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['ListTags']._serialized_options = b'\x88\x02\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02|\x12@/v1/{parent=projects/*/locations/*/entryGroups/*/entries/*}/tagsZ8\x126/v1/{parent=projects/*/locations/*/entryGroups/*}/tags'
    _globals['_DATACATALOG'].methods_by_name['ReconcileTags']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['ReconcileTags']._serialized_options = b'\x88\x02\x01\xcaA.\n\x15ReconcileTagsResponse\x12\x15ReconcileTagsMetadata\x82\xd3\xe4\x93\x02O"J/v1/{parent=projects/*/locations/*/entryGroups/*/entries/*}/tags:reconcile:\x01*'
    _globals['_DATACATALOG'].methods_by_name['StarEntry']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['StarEntry']._serialized_options = b'\x88\x02\x01\xdaA\x04name\x82\xd3\xe4\x93\x02C">/v1/{name=projects/*/locations/*/entryGroups/*/entries/*}:star:\x01*'
    _globals['_DATACATALOG'].methods_by_name['UnstarEntry']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['UnstarEntry']._serialized_options = b'\x88\x02\x01\xdaA\x04name\x82\xd3\xe4\x93\x02E"@/v1/{name=projects/*/locations/*/entryGroups/*/entries/*}:unstar:\x01*'
    _globals['_DATACATALOG'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['SetIamPolicy']._serialized_options = b'\x88\x02\x01\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02\x8d\x01"A/v1/{resource=projects/*/locations/*/tagTemplates/*}:setIamPolicy:\x01*ZE"@/v1/{resource=projects/*/locations/*/entryGroups/*}:setIamPolicy:\x01*'
    _globals['_DATACATALOG'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['GetIamPolicy']._serialized_options = b'\x88\x02\x01\xdaA\x08resource\x82\xd3\xe4\x93\x02\xde\x01"A/v1/{resource=projects/*/locations/*/tagTemplates/*}:getIamPolicy:\x01*ZE"@/v1/{resource=projects/*/locations/*/entryGroups/*}:getIamPolicy:\x01*ZO"J/v1/{resource=projects/*/locations/*/entryGroups/*/entries/*}:getIamPolicy:\x01*'
    _globals['_DATACATALOG'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['TestIamPermissions']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x02\xf0\x01"G/v1/{resource=projects/*/locations/*/tagTemplates/*}:testIamPermissions:\x01*ZK"F/v1/{resource=projects/*/locations/*/entryGroups/*}:testIamPermissions:\x01*ZU"P/v1/{resource=projects/*/locations/*/entryGroups/*/entries/*}:testIamPermissions:\x01*'
    _globals['_DATACATALOG'].methods_by_name['ImportEntries']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['ImportEntries']._serialized_options = b'\x88\x02\x01\xcaA.\n\x15ImportEntriesResponse\x12\x15ImportEntriesMetadata\x82\xd3\xe4\x93\x02E"@/v1/{parent=projects/*/locations/*/entryGroups/*}/entries:import:\x01*'
    _globals['_DATACATALOG'].methods_by_name['SetConfig']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['SetConfig']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x02g"0/v1/{name=organizations/*/locations/*}:setConfig:\x01*Z0"+/v1/{name=projects/*/locations/*}:setConfig:\x01*'
    _globals['_DATACATALOG'].methods_by_name['RetrieveConfig']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['RetrieveConfig']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x027\x125/v1/{name=organizations/*/locations/*}:retrieveConfig'
    _globals['_DATACATALOG'].methods_by_name['RetrieveEffectiveConfig']._loaded_options = None
    _globals['_DATACATALOG'].methods_by_name['RetrieveEffectiveConfig']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x02}\x12>/v1/{name=organizations/*/locations/*}:retrieveEffectiveConfigZ;\x129/v1/{name=projects/*/locations/*}:retrieveEffectiveConfig'
    _globals['_ENTRYTYPE']._serialized_start = 13866
    _globals['_ENTRYTYPE']._serialized_end = 14180
    _globals['_TAGTEMPLATEMIGRATION']._serialized_start = 14183
    _globals['_TAGTEMPLATEMIGRATION']._serialized_end = 14318
    _globals['_CATALOGUIEXPERIENCE']._serialized_start = 14321
    _globals['_CATALOGUIEXPERIENCE']._serialized_end = 14452
    _globals['_SEARCHCATALOGREQUEST']._serialized_start = 903
    _globals['_SEARCHCATALOGREQUEST']._serialized_end = 1319
    _globals['_SEARCHCATALOGREQUEST_SCOPE']._serialized_start = 1114
    _globals['_SEARCHCATALOGREQUEST_SCOPE']._serialized_end = 1319
    _globals['_SEARCHCATALOGRESPONSE']._serialized_start = 1322
    _globals['_SEARCHCATALOGRESPONSE']._serialized_end = 1478
    _globals['_CREATEENTRYGROUPREQUEST']._serialized_start = 1481
    _globals['_CREATEENTRYGROUPREQUEST']._serialized_end = 1660
    _globals['_UPDATEENTRYGROUPREQUEST']._serialized_start = 1663
    _globals['_UPDATEENTRYGROUPREQUEST']._serialized_end = 1804
    _globals['_GETENTRYGROUPREQUEST']._serialized_start = 1807
    _globals['_GETENTRYGROUPREQUEST']._serialized_end = 1937
    _globals['_DELETEENTRYGROUPREQUEST']._serialized_start = 1939
    _globals['_DELETEENTRYGROUPREQUEST']._serialized_end = 2045
    _globals['_LISTENTRYGROUPSREQUEST']._serialized_start = 2048
    _globals['_LISTENTRYGROUPSREQUEST']._serialized_end = 2184
    _globals['_LISTENTRYGROUPSRESPONSE']._serialized_start = 2186
    _globals['_LISTENTRYGROUPSRESPONSE']._serialized_end = 2299
    _globals['_CREATEENTRYREQUEST']._serialized_start = 2302
    _globals['_CREATEENTRYREQUEST']._serialized_end = 2464
    _globals['_UPDATEENTRYREQUEST']._serialized_start = 2466
    _globals['_UPDATEENTRYREQUEST']._serialized_end = 2591
    _globals['_DELETEENTRYREQUEST']._serialized_start = 2593
    _globals['_DELETEENTRYREQUEST']._serialized_end = 2669
    _globals['_GETENTRYREQUEST']._serialized_start = 2671
    _globals['_GETENTRYREQUEST']._serialized_end = 2744
    _globals['_LOOKUPENTRYREQUEST']._serialized_start = 2747
    _globals['_LOOKUPENTRYREQUEST']._serialized_end = 2900
    _globals['_ENTRY']._serialized_start = 2903
    _globals['_ENTRY']._serialized_end = 5080
    _globals['_ENTRY_LABELSENTRY']._serialized_start = 4853
    _globals['_ENTRY_LABELSENTRY']._serialized_end = 4898
    _globals['_DATABASETABLESPEC']._serialized_start = 5083
    _globals['_DATABASETABLESPEC']._serialized_end = 5670
    _globals['_DATABASETABLESPEC_DATABASEVIEWSPEC']._serialized_start = 5347
    _globals['_DATABASETABLESPEC_DATABASEVIEWSPEC']._serialized_end = 5603
    _globals['_DATABASETABLESPEC_DATABASEVIEWSPEC_VIEWTYPE']._serialized_start = 5503
    _globals['_DATABASETABLESPEC_DATABASEVIEWSPEC_VIEWTYPE']._serialized_end = 5582
    _globals['_DATABASETABLESPEC_TABLETYPE']._serialized_start = 5605
    _globals['_DATABASETABLESPEC_TABLETYPE']._serialized_end = 5670
    _globals['_FILESETSPEC']._serialized_start = 5672
    _globals['_FILESETSPEC']._serialized_end = 5761
    _globals['_DATASOURCECONNECTIONSPEC']._serialized_start = 5763
    _globals['_DATASOURCECONNECTIONSPEC']._serialized_end = 5876
    _globals['_ROUTINESPEC']._serialized_start = 5879
    _globals['_ROUTINESPEC']._serialized_end = 6458
    _globals['_ROUTINESPEC_ARGUMENT']._serialized_start = 6196
    _globals['_ROUTINESPEC_ARGUMENT']._serialized_end = 6362
    _globals['_ROUTINESPEC_ARGUMENT_MODE']._serialized_start = 6306
    _globals['_ROUTINESPEC_ARGUMENT_MODE']._serialized_end = 6362
    _globals['_ROUTINESPEC_ROUTINETYPE']._serialized_start = 6364
    _globals['_ROUTINESPEC_ROUTINETYPE']._serialized_end = 6443
    _globals['_DATASETSPEC']._serialized_start = 6460
    _globals['_DATASETSPEC']._serialized_end = 6567
    _globals['_SQLDATABASESYSTEMSPEC']._serialized_start = 6569
    _globals['_SQLDATABASESYSTEMSPEC']._serialized_end = 6661
    _globals['_LOOKERSYSTEMSPEC']._serialized_start = 6664
    _globals['_LOOKERSYSTEMSPEC']._serialized_end = 6866
    _globals['_CLOUDBIGTABLESYSTEMSPEC']._serialized_start = 6868
    _globals['_CLOUDBIGTABLESYSTEMSPEC']._serialized_end = 6924
    _globals['_CLOUDBIGTABLEINSTANCESPEC']._serialized_start = 6927
    _globals['_CLOUDBIGTABLEINSTANCESPEC']._serialized_end = 7180
    _globals['_CLOUDBIGTABLEINSTANCESPEC_CLOUDBIGTABLECLUSTERSPEC']._serialized_start = 7075
    _globals['_CLOUDBIGTABLEINSTANCESPEC_CLOUDBIGTABLECLUSTERSPEC']._serialized_end = 7180
    _globals['_SERVICESPEC']._serialized_start = 7182
    _globals['_SERVICESPEC']._serialized_end = 7306
    _globals['_VERTEXMODELSOURCEINFO']._serialized_start = 7309
    _globals['_VERTEXMODELSOURCEINFO']._serialized_end = 7597
    _globals['_VERTEXMODELSOURCEINFO_MODELSOURCETYPE']._serialized_start = 7438
    _globals['_VERTEXMODELSOURCEINFO_MODELSOURCETYPE']._serialized_end = 7597
    _globals['_VERTEXMODELSPEC']._serialized_start = 7600
    _globals['_VERTEXMODELSPEC']._serialized_end = 7806
    _globals['_VERTEXDATASETSPEC']._serialized_start = 7809
    _globals['_VERTEXDATASETSPEC']._serialized_end = 8165
    _globals['_VERTEXDATASETSPEC_DATATYPE']._serialized_start = 7932
    _globals['_VERTEXDATASETSPEC_DATATYPE']._serialized_end = 8165
    _globals['_MODELSPEC']._serialized_start = 8167
    _globals['_MODELSPEC']._serialized_end = 8268
    _globals['_FEATUREONLINESTORESPEC']._serialized_start = 8271
    _globals['_FEATUREONLINESTORESPEC']._serialized_end = 8461
    _globals['_FEATUREONLINESTORESPEC_STORAGETYPE']._serialized_start = 8389
    _globals['_FEATUREONLINESTORESPEC_STORAGETYPE']._serialized_end = 8461
    _globals['_BUSINESSCONTEXT']._serialized_start = 8464
    _globals['_BUSINESSCONTEXT']._serialized_end = 8606
    _globals['_ENTRYOVERVIEW']._serialized_start = 8608
    _globals['_ENTRYOVERVIEW']._serialized_end = 8641
    _globals['_CONTACTS']._serialized_start = 8643
    _globals['_CONTACTS']._serialized_end = 8761
    _globals['_CONTACTS_PERSON']._serialized_start = 8717
    _globals['_CONTACTS_PERSON']._serialized_end = 8761
    _globals['_ENTRYGROUP']._serialized_start = 8764
    _globals['_ENTRYGROUP']._serialized_end = 9072
    _globals['_CREATETAGTEMPLATEREQUEST']._serialized_start = 9075
    _globals['_CREATETAGTEMPLATEREQUEST']._serialized_end = 9264
    _globals['_GETTAGTEMPLATEREQUEST']._serialized_start = 9266
    _globals['_GETTAGTEMPLATEREQUEST']._serialized_end = 9351
    _globals['_UPDATETAGTEMPLATEREQUEST']._serialized_start = 9354
    _globals['_UPDATETAGTEMPLATEREQUEST']._serialized_end = 9498
    _globals['_DELETETAGTEMPLATEREQUEST']._serialized_start = 9500
    _globals['_DELETETAGTEMPLATEREQUEST']._serialized_end = 9608
    _globals['_CREATETAGREQUEST']._serialized_start = 9610
    _globals['_CREATETAGREQUEST']._serialized_end = 9736
    _globals['_UPDATETAGREQUEST']._serialized_start = 9738
    _globals['_UPDATETAGREQUEST']._serialized_end = 9857
    _globals['_DELETETAGREQUEST']._serialized_start = 9859
    _globals['_DELETETAGREQUEST']._serialized_end = 9931
    _globals['_CREATETAGTEMPLATEFIELDREQUEST']._serialized_start = 9934
    _globals['_CREATETAGTEMPLATEFIELDREQUEST']._serialized_end = 10145
    _globals['_UPDATETAGTEMPLATEFIELDREQUEST']._serialized_start = 10148
    _globals['_UPDATETAGTEMPLATEFIELDREQUEST']._serialized_end = 10380
    _globals['_RENAMETAGTEMPLATEFIELDREQUEST']._serialized_start = 10383
    _globals['_RENAMETAGTEMPLATEFIELDREQUEST']._serialized_end = 10521
    _globals['_RENAMETAGTEMPLATEFIELDENUMVALUEREQUEST']._serialized_start = 10524
    _globals['_RENAMETAGTEMPLATEFIELDENUMVALUEREQUEST']._serialized_end = 10682
    _globals['_DELETETAGTEMPLATEFIELDREQUEST']._serialized_start = 10684
    _globals['_DELETETAGTEMPLATEFIELDREQUEST']._serialized_end = 10802
    _globals['_LISTTAGSREQUEST']._serialized_start = 10804
    _globals['_LISTTAGSREQUEST']._serialized_end = 10916
    _globals['_LISTTAGSRESPONSE']._serialized_start = 10918
    _globals['_LISTTAGSRESPONSE']._serialized_end = 11009
    _globals['_RECONCILETAGSREQUEST']._serialized_start = 11012
    _globals['_RECONCILETAGSREQUEST']._serialized_end = 11240
    _globals['_RECONCILETAGSRESPONSE']._serialized_start = 11242
    _globals['_RECONCILETAGSRESPONSE']._serialized_end = 11349
    _globals['_RECONCILETAGSMETADATA']._serialized_start = 11352
    _globals['_RECONCILETAGSMETADATA']._serialized_end = 11755
    _globals['_RECONCILETAGSMETADATA_ERRORSENTRY']._serialized_start = 11544
    _globals['_RECONCILETAGSMETADATA_ERRORSENTRY']._serialized_end = 11609
    _globals['_RECONCILETAGSMETADATA_RECONCILIATIONSTATE']._serialized_start = 11612
    _globals['_RECONCILETAGSMETADATA_RECONCILIATIONSTATE']._serialized_end = 11755
    _globals['_LISTENTRIESREQUEST']._serialized_start = 11758
    _globals['_LISTENTRIESREQUEST']._serialized_end = 11927
    _globals['_LISTENTRIESRESPONSE']._serialized_start = 11929
    _globals['_LISTENTRIESRESPONSE']._serialized_end = 12028
    _globals['_STARENTRYREQUEST']._serialized_start = 12030
    _globals['_STARENTRYREQUEST']._serialized_end = 12104
    _globals['_STARENTRYRESPONSE']._serialized_start = 12106
    _globals['_STARENTRYRESPONSE']._serialized_end = 12125
    _globals['_UNSTARENTRYREQUEST']._serialized_start = 12127
    _globals['_UNSTARENTRYREQUEST']._serialized_end = 12203
    _globals['_UNSTARENTRYRESPONSE']._serialized_start = 12205
    _globals['_UNSTARENTRYRESPONSE']._serialized_end = 12226
    _globals['_IMPORTENTRIESREQUEST']._serialized_start = 12229
    _globals['_IMPORTENTRIESREQUEST']._serialized_end = 12367
    _globals['_IMPORTENTRIESRESPONSE']._serialized_start = 12370
    _globals['_IMPORTENTRIESRESPONSE']._serialized_end = 12519
    _globals['_IMPORTENTRIESMETADATA']._serialized_start = 12522
    _globals['_IMPORTENTRIESMETADATA']._serialized_end = 12786
    _globals['_IMPORTENTRIESMETADATA_IMPORTSTATE']._serialized_start = 12662
    _globals['_IMPORTENTRIESMETADATA_IMPORTSTATE']._serialized_end = 12786
    _globals['_MODIFYENTRYOVERVIEWREQUEST']._serialized_start = 12789
    _globals['_MODIFYENTRYOVERVIEWREQUEST']._serialized_end = 12946
    _globals['_MODIFYENTRYCONTACTSREQUEST']._serialized_start = 12949
    _globals['_MODIFYENTRYCONTACTSREQUEST']._serialized_end = 13095
    _globals['_SETCONFIGREQUEST']._serialized_start = 13098
    _globals['_SETCONFIGREQUEST']._serialized_end = 13320
    _globals['_RETRIEVECONFIGREQUEST']._serialized_start = 13322
    _globals['_RETRIEVECONFIGREQUEST']._serialized_end = 13364
    _globals['_RETRIEVEEFFECTIVECONFIGREQUEST']._serialized_start = 13366
    _globals['_RETRIEVEEFFECTIVECONFIGREQUEST']._serialized_end = 13417
    _globals['_ORGANIZATIONCONFIG']._serialized_start = 13420
    _globals['_ORGANIZATIONCONFIG']._serialized_end = 13610
    _globals['_ORGANIZATIONCONFIG_CONFIGENTRY']._serialized_start = 13519
    _globals['_ORGANIZATIONCONFIG_CONFIGENTRY']._serialized_end = 13610
    _globals['_MIGRATIONCONFIG']._serialized_start = 13613
    _globals['_MIGRATIONCONFIG']._serialized_end = 13863
    _globals['_DATACATALOG']._serialized_start = 14455
    _globals['_DATACATALOG']._serialized_end = 22857