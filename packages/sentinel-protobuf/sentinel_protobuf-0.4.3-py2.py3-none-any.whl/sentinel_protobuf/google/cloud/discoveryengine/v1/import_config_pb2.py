"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/import_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import completion_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_completion__pb2
from .....google.cloud.discoveryengine.v1 import document_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_document__pb2
from .....google.cloud.discoveryengine.v1 import user_event_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_user__event__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from .....google.type import date_pb2 as google_dot_type_dot_date__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/discoveryengine/v1/import_config.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/discoveryengine/v1/completion.proto\x1a.google/cloud/discoveryengine/v1/document.proto\x1a0google/cloud/discoveryengine/v1/user_event.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x16google/type/date.proto"9\n\tGcsSource\x12\x17\n\ninput_uris\x18\x01 \x03(\tB\x03\xe0A\x02\x12\x13\n\x0bdata_schema\x18\x02 \x01(\t"\xbc\x01\n\x0eBigQuerySource\x12+\n\x0epartition_date\x18\x05 \x01(\x0b2\x11.google.type.DateH\x00\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x17\n\x0fgcs_staging_dir\x18\x04 \x01(\t\x12\x13\n\x0bdata_schema\x18\x06 \x01(\tB\x0b\n\tpartition"\x89\x01\n\rSpannerSource\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x18\n\x0binstance_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdatabase_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x19\n\x11enable_data_boost\x18\x05 \x01(\x08"\x8d\x07\n\x0fBigtableOptions\x12\x16\n\x0ekey_field_name\x18\x01 \x01(\t\x12P\n\x08families\x18\x02 \x03(\x0b2>.google.cloud.discoveryengine.v1.BigtableOptions.FamiliesEntry\x1a\x8e\x02\n\x14BigtableColumnFamily\x12\x12\n\nfield_name\x18\x01 \x01(\t\x12K\n\x08encoding\x18\x02 \x01(\x0e29.google.cloud.discoveryengine.v1.BigtableOptions.Encoding\x12C\n\x04type\x18\x03 \x01(\x0e25.google.cloud.discoveryengine.v1.BigtableOptions.Type\x12P\n\x07columns\x18\x04 \x03(\x0b2?.google.cloud.discoveryengine.v1.BigtableOptions.BigtableColumn\x1a\xce\x01\n\x0eBigtableColumn\x12\x16\n\tqualifier\x18\x01 \x01(\x0cB\x03\xe0A\x02\x12\x12\n\nfield_name\x18\x02 \x01(\t\x12K\n\x08encoding\x18\x03 \x01(\x0e29.google.cloud.discoveryengine.v1.BigtableOptions.Encoding\x12C\n\x04type\x18\x04 \x01(\x0e25.google.cloud.discoveryengine.v1.BigtableOptions.Type\x1av\n\rFamiliesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12T\n\x05value\x18\x02 \x01(\x0b2E.google.cloud.discoveryengine.v1.BigtableOptions.BigtableColumnFamily:\x028\x01"z\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06STRING\x10\x01\x12\n\n\x06NUMBER\x10\x02\x12\x0b\n\x07INTEGER\x10\x03\x12\x0f\n\x0bVAR_INTEGER\x10\x04\x12\x0f\n\x0bBIG_NUMERIC\x10\x05\x12\x0b\n\x07BOOLEAN\x10\x06\x12\x08\n\x04JSON\x10\x07":\n\x08Encoding\x12\x18\n\x14ENCODING_UNSPECIFIED\x10\x00\x12\x08\n\x04TEXT\x10\x01\x12\n\n\x06BINARY\x10\x02"\xa6\x01\n\x0eBigtableSource\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x18\n\x0binstance_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12O\n\x10bigtable_options\x18\x04 \x01(\x0b20.google.cloud.discoveryengine.v1.BigtableOptionsB\x03\xe0A\x02"\xb6\x01\n\x0fFhirStoreSource\x12?\n\nfhir_store\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#healthcare.googleapis.com/FhirStore\x12\x17\n\x0fgcs_staging_dir\x18\x02 \x01(\t\x12\x16\n\x0eresource_types\x18\x03 \x03(\t\x121\n$update_from_latest_predefined_schema\x18\x04 \x01(\x08B\x03\xe0A\x01"\x99\x01\n\x0eCloudSqlSource\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x18\n\x0binstance_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdatabase_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x17\n\x0fgcs_staging_dir\x18\x05 \x01(\t\x12\x0f\n\x07offload\x18\x06 \x01(\x08"\xa0\x01\n\rAlloyDbSource\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x18\n\x0blocation_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x17\n\ncluster_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdatabase_id\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x05 \x01(\tB\x03\xe0A\x02\x12\x17\n\x0fgcs_staging_dir\x18\x06 \x01(\t"t\n\x0fFirestoreSource\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x18\n\x0bdatabase_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rcollection_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x17\n\x0fgcs_staging_dir\x18\x04 \x01(\t"8\n\x11ImportErrorConfig\x12\x14\n\ngcs_prefix\x18\x01 \x01(\tH\x00B\r\n\x0bdestination"\xf3\x03\n\x17ImportUserEventsRequest\x12^\n\rinline_source\x18\x02 \x01(\x0b2E.google.cloud.discoveryengine.v1.ImportUserEventsRequest.InlineSourceH\x00\x12@\n\ngcs_source\x18\x03 \x01(\x0b2*.google.cloud.discoveryengine.v1.GcsSourceH\x00\x12J\n\x0fbigquery_source\x18\x04 \x01(\x0b2/.google.cloud.discoveryengine.v1.BigQuerySourceH\x00\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x12H\n\x0cerror_config\x18\x05 \x01(\x0b22.google.cloud.discoveryengine.v1.ImportErrorConfig\x1aT\n\x0cInlineSource\x12D\n\x0buser_events\x18\x01 \x03(\x0b2*.google.cloud.discoveryengine.v1.UserEventB\x03\xe0A\x02B\x08\n\x06source"\xcb\x01\n\x18ImportUserEventsResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12H\n\x0cerror_config\x18\x02 \x01(\x0b22.google.cloud.discoveryengine.v1.ImportErrorConfig\x12\x1b\n\x13joined_events_count\x18\x03 \x01(\x03\x12\x1d\n\x15unjoined_events_count\x18\x04 \x01(\x03"\xaa\x01\n\x18ImportUserEventsMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rsuccess_count\x18\x03 \x01(\x03\x12\x15\n\rfailure_count\x18\x04 \x01(\x03"\xbe\x01\n\x17ImportDocumentsMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rsuccess_count\x18\x03 \x01(\x03\x12\x15\n\rfailure_count\x18\x04 \x01(\x03\x12\x13\n\x0btotal_count\x18\x05 \x01(\x03"\xf7\t\n\x16ImportDocumentsRequest\x12]\n\rinline_source\x18\x02 \x01(\x0b2D.google.cloud.discoveryengine.v1.ImportDocumentsRequest.InlineSourceH\x00\x12@\n\ngcs_source\x18\x03 \x01(\x0b2*.google.cloud.discoveryengine.v1.GcsSourceH\x00\x12J\n\x0fbigquery_source\x18\x04 \x01(\x0b2/.google.cloud.discoveryengine.v1.BigQuerySourceH\x00\x12M\n\x11fhir_store_source\x18\n \x01(\x0b20.google.cloud.discoveryengine.v1.FhirStoreSourceH\x00\x12H\n\x0espanner_source\x18\x0b \x01(\x0b2..google.cloud.discoveryengine.v1.SpannerSourceH\x00\x12K\n\x10cloud_sql_source\x18\x0c \x01(\x0b2/.google.cloud.discoveryengine.v1.CloudSqlSourceH\x00\x12L\n\x10firestore_source\x18\r \x01(\x0b20.google.cloud.discoveryengine.v1.FirestoreSourceH\x00\x12I\n\x0falloy_db_source\x18\x0e \x01(\x0b2..google.cloud.discoveryengine.v1.AlloyDbSourceH\x00\x12J\n\x0fbigtable_source\x18\x0f \x01(\x0b2/.google.cloud.discoveryengine.v1.BigtableSourceH\x00\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Branch\x12H\n\x0cerror_config\x18\x05 \x01(\x0b22.google.cloud.discoveryengine.v1.ImportErrorConfig\x12g\n\x13reconciliation_mode\x18\x06 \x01(\x0e2J.google.cloud.discoveryengine.v1.ImportDocumentsRequest.ReconciliationMode\x12/\n\x0bupdate_mask\x18\x07 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x19\n\x11auto_generate_ids\x18\x08 \x01(\x08\x12\x10\n\x08id_field\x18\t \x01(\t\x12"\n\x15force_refresh_content\x18\x10 \x01(\x08B\x03\xe0A\x01\x1aQ\n\x0cInlineSource\x12A\n\tdocuments\x18\x01 \x03(\x0b2).google.cloud.discoveryengine.v1.DocumentB\x03\xe0A\x02"T\n\x12ReconciliationMode\x12#\n\x1fRECONCILIATION_MODE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bINCREMENTAL\x10\x01\x12\x08\n\x04FULL\x10\x02B\x08\n\x06source"\x8e\x01\n\x17ImportDocumentsResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12H\n\x0cerror_config\x18\x02 \x01(\x0b22.google.cloud.discoveryengine.v1.ImportErrorConfig"\x85\x03\n&ImportSuggestionDenyListEntriesRequest\x12m\n\rinline_source\x18\x02 \x01(\x0b2T.google.cloud.discoveryengine.v1.ImportSuggestionDenyListEntriesRequest.InlineSourceH\x00\x12@\n\ngcs_source\x18\x03 \x01(\x0b2*.google.cloud.discoveryengine.v1.GcsSourceH\x00\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x1a^\n\x0cInlineSource\x12N\n\x07entries\x18\x01 \x03(\x0b28.google.cloud.discoveryengine.v1.SuggestionDenyListEntryB\x03\xe0A\x02B\x08\n\x06source"\x92\x01\n\'ImportSuggestionDenyListEntriesResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12\x1e\n\x16imported_entries_count\x18\x02 \x01(\x03\x12\x1c\n\x14failed_entries_count\x18\x03 \x01(\x03"\x8b\x01\n\'ImportSuggestionDenyListEntriesMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x94\x04\n"ImportCompletionSuggestionsRequest\x12i\n\rinline_source\x18\x02 \x01(\x0b2P.google.cloud.discoveryengine.v1.ImportCompletionSuggestionsRequest.InlineSourceH\x00\x12@\n\ngcs_source\x18\x03 \x01(\x0b2*.google.cloud.discoveryengine.v1.GcsSourceH\x00\x12J\n\x0fbigquery_source\x18\x04 \x01(\x0b2/.google.cloud.discoveryengine.v1.BigQuerySourceH\x00\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x12H\n\x0cerror_config\x18\x05 \x01(\x0b22.google.cloud.discoveryengine.v1.ImportErrorConfig\x1a_\n\x0cInlineSource\x12O\n\x0bsuggestions\x18\x01 \x03(\x0b25.google.cloud.discoveryengine.v1.CompletionSuggestionB\x03\xe0A\x02B\x08\n\x06source"\x9a\x01\n#ImportCompletionSuggestionsResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12H\n\x0cerror_config\x18\x02 \x01(\x0b22.google.cloud.discoveryengine.v1.ImportErrorConfig"\xb5\x01\n#ImportCompletionSuggestionsMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rsuccess_count\x18\x03 \x01(\x03\x12\x15\n\rfailure_count\x18\x04 \x01(\x03B\x84\x02\n#com.google.cloud.discoveryengine.v1B\x11ImportConfigProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.import_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x11ImportConfigProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_GCSSOURCE'].fields_by_name['input_uris']._loaded_options = None
    _globals['_GCSSOURCE'].fields_by_name['input_uris']._serialized_options = b'\xe0A\x02'
    _globals['_BIGQUERYSOURCE'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_BIGQUERYSOURCE'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_BIGQUERYSOURCE'].fields_by_name['table_id']._loaded_options = None
    _globals['_BIGQUERYSOURCE'].fields_by_name['table_id']._serialized_options = b'\xe0A\x02'
    _globals['_SPANNERSOURCE'].fields_by_name['instance_id']._loaded_options = None
    _globals['_SPANNERSOURCE'].fields_by_name['instance_id']._serialized_options = b'\xe0A\x02'
    _globals['_SPANNERSOURCE'].fields_by_name['database_id']._loaded_options = None
    _globals['_SPANNERSOURCE'].fields_by_name['database_id']._serialized_options = b'\xe0A\x02'
    _globals['_SPANNERSOURCE'].fields_by_name['table_id']._loaded_options = None
    _globals['_SPANNERSOURCE'].fields_by_name['table_id']._serialized_options = b'\xe0A\x02'
    _globals['_BIGTABLEOPTIONS_BIGTABLECOLUMN'].fields_by_name['qualifier']._loaded_options = None
    _globals['_BIGTABLEOPTIONS_BIGTABLECOLUMN'].fields_by_name['qualifier']._serialized_options = b'\xe0A\x02'
    _globals['_BIGTABLEOPTIONS_FAMILIESENTRY']._loaded_options = None
    _globals['_BIGTABLEOPTIONS_FAMILIESENTRY']._serialized_options = b'8\x01'
    _globals['_BIGTABLESOURCE'].fields_by_name['instance_id']._loaded_options = None
    _globals['_BIGTABLESOURCE'].fields_by_name['instance_id']._serialized_options = b'\xe0A\x02'
    _globals['_BIGTABLESOURCE'].fields_by_name['table_id']._loaded_options = None
    _globals['_BIGTABLESOURCE'].fields_by_name['table_id']._serialized_options = b'\xe0A\x02'
    _globals['_BIGTABLESOURCE'].fields_by_name['bigtable_options']._loaded_options = None
    _globals['_BIGTABLESOURCE'].fields_by_name['bigtable_options']._serialized_options = b'\xe0A\x02'
    _globals['_FHIRSTORESOURCE'].fields_by_name['fhir_store']._loaded_options = None
    _globals['_FHIRSTORESOURCE'].fields_by_name['fhir_store']._serialized_options = b'\xe0A\x02\xfaA%\n#healthcare.googleapis.com/FhirStore'
    _globals['_FHIRSTORESOURCE'].fields_by_name['update_from_latest_predefined_schema']._loaded_options = None
    _globals['_FHIRSTORESOURCE'].fields_by_name['update_from_latest_predefined_schema']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDSQLSOURCE'].fields_by_name['instance_id']._loaded_options = None
    _globals['_CLOUDSQLSOURCE'].fields_by_name['instance_id']._serialized_options = b'\xe0A\x02'
    _globals['_CLOUDSQLSOURCE'].fields_by_name['database_id']._loaded_options = None
    _globals['_CLOUDSQLSOURCE'].fields_by_name['database_id']._serialized_options = b'\xe0A\x02'
    _globals['_CLOUDSQLSOURCE'].fields_by_name['table_id']._loaded_options = None
    _globals['_CLOUDSQLSOURCE'].fields_by_name['table_id']._serialized_options = b'\xe0A\x02'
    _globals['_ALLOYDBSOURCE'].fields_by_name['location_id']._loaded_options = None
    _globals['_ALLOYDBSOURCE'].fields_by_name['location_id']._serialized_options = b'\xe0A\x02'
    _globals['_ALLOYDBSOURCE'].fields_by_name['cluster_id']._loaded_options = None
    _globals['_ALLOYDBSOURCE'].fields_by_name['cluster_id']._serialized_options = b'\xe0A\x02'
    _globals['_ALLOYDBSOURCE'].fields_by_name['database_id']._loaded_options = None
    _globals['_ALLOYDBSOURCE'].fields_by_name['database_id']._serialized_options = b'\xe0A\x02'
    _globals['_ALLOYDBSOURCE'].fields_by_name['table_id']._loaded_options = None
    _globals['_ALLOYDBSOURCE'].fields_by_name['table_id']._serialized_options = b'\xe0A\x02'
    _globals['_FIRESTORESOURCE'].fields_by_name['database_id']._loaded_options = None
    _globals['_FIRESTORESOURCE'].fields_by_name['database_id']._serialized_options = b'\xe0A\x02'
    _globals['_FIRESTORESOURCE'].fields_by_name['collection_id']._loaded_options = None
    _globals['_FIRESTORESOURCE'].fields_by_name['collection_id']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTUSEREVENTSREQUEST_INLINESOURCE'].fields_by_name['user_events']._loaded_options = None
    _globals['_IMPORTUSEREVENTSREQUEST_INLINESOURCE'].fields_by_name['user_events']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTUSEREVENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTUSEREVENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_IMPORTDOCUMENTSREQUEST_INLINESOURCE'].fields_by_name['documents']._loaded_options = None
    _globals['_IMPORTDOCUMENTSREQUEST_INLINESOURCE'].fields_by_name['documents']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTDOCUMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTDOCUMENTSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%discoveryengine.googleapis.com/Branch"
    _globals['_IMPORTDOCUMENTSREQUEST'].fields_by_name['force_refresh_content']._loaded_options = None
    _globals['_IMPORTDOCUMENTSREQUEST'].fields_by_name['force_refresh_content']._serialized_options = b'\xe0A\x01'
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESREQUEST_INLINESOURCE'].fields_by_name['entries']._loaded_options = None
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESREQUEST_INLINESOURCE'].fields_by_name['entries']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_IMPORTCOMPLETIONSUGGESTIONSREQUEST_INLINESOURCE'].fields_by_name['suggestions']._loaded_options = None
    _globals['_IMPORTCOMPLETIONSUGGESTIONSREQUEST_INLINESOURCE'].fields_by_name['suggestions']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTCOMPLETIONSUGGESTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTCOMPLETIONSUGGESTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_GCSSOURCE']._serialized_start = 412
    _globals['_GCSSOURCE']._serialized_end = 469
    _globals['_BIGQUERYSOURCE']._serialized_start = 472
    _globals['_BIGQUERYSOURCE']._serialized_end = 660
    _globals['_SPANNERSOURCE']._serialized_start = 663
    _globals['_SPANNERSOURCE']._serialized_end = 800
    _globals['_BIGTABLEOPTIONS']._serialized_start = 803
    _globals['_BIGTABLEOPTIONS']._serialized_end = 1712
    _globals['_BIGTABLEOPTIONS_BIGTABLECOLUMNFAMILY']._serialized_start = 929
    _globals['_BIGTABLEOPTIONS_BIGTABLECOLUMNFAMILY']._serialized_end = 1199
    _globals['_BIGTABLEOPTIONS_BIGTABLECOLUMN']._serialized_start = 1202
    _globals['_BIGTABLEOPTIONS_BIGTABLECOLUMN']._serialized_end = 1408
    _globals['_BIGTABLEOPTIONS_FAMILIESENTRY']._serialized_start = 1410
    _globals['_BIGTABLEOPTIONS_FAMILIESENTRY']._serialized_end = 1528
    _globals['_BIGTABLEOPTIONS_TYPE']._serialized_start = 1530
    _globals['_BIGTABLEOPTIONS_TYPE']._serialized_end = 1652
    _globals['_BIGTABLEOPTIONS_ENCODING']._serialized_start = 1654
    _globals['_BIGTABLEOPTIONS_ENCODING']._serialized_end = 1712
    _globals['_BIGTABLESOURCE']._serialized_start = 1715
    _globals['_BIGTABLESOURCE']._serialized_end = 1881
    _globals['_FHIRSTORESOURCE']._serialized_start = 1884
    _globals['_FHIRSTORESOURCE']._serialized_end = 2066
    _globals['_CLOUDSQLSOURCE']._serialized_start = 2069
    _globals['_CLOUDSQLSOURCE']._serialized_end = 2222
    _globals['_ALLOYDBSOURCE']._serialized_start = 2225
    _globals['_ALLOYDBSOURCE']._serialized_end = 2385
    _globals['_FIRESTORESOURCE']._serialized_start = 2387
    _globals['_FIRESTORESOURCE']._serialized_end = 2503
    _globals['_IMPORTERRORCONFIG']._serialized_start = 2505
    _globals['_IMPORTERRORCONFIG']._serialized_end = 2561
    _globals['_IMPORTUSEREVENTSREQUEST']._serialized_start = 2564
    _globals['_IMPORTUSEREVENTSREQUEST']._serialized_end = 3063
    _globals['_IMPORTUSEREVENTSREQUEST_INLINESOURCE']._serialized_start = 2969
    _globals['_IMPORTUSEREVENTSREQUEST_INLINESOURCE']._serialized_end = 3053
    _globals['_IMPORTUSEREVENTSRESPONSE']._serialized_start = 3066
    _globals['_IMPORTUSEREVENTSRESPONSE']._serialized_end = 3269
    _globals['_IMPORTUSEREVENTSMETADATA']._serialized_start = 3272
    _globals['_IMPORTUSEREVENTSMETADATA']._serialized_end = 3442
    _globals['_IMPORTDOCUMENTSMETADATA']._serialized_start = 3445
    _globals['_IMPORTDOCUMENTSMETADATA']._serialized_end = 3635
    _globals['_IMPORTDOCUMENTSREQUEST']._serialized_start = 3638
    _globals['_IMPORTDOCUMENTSREQUEST']._serialized_end = 4909
    _globals['_IMPORTDOCUMENTSREQUEST_INLINESOURCE']._serialized_start = 4732
    _globals['_IMPORTDOCUMENTSREQUEST_INLINESOURCE']._serialized_end = 4813
    _globals['_IMPORTDOCUMENTSREQUEST_RECONCILIATIONMODE']._serialized_start = 4815
    _globals['_IMPORTDOCUMENTSREQUEST_RECONCILIATIONMODE']._serialized_end = 4899
    _globals['_IMPORTDOCUMENTSRESPONSE']._serialized_start = 4912
    _globals['_IMPORTDOCUMENTSRESPONSE']._serialized_end = 5054
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESREQUEST']._serialized_start = 5057
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESREQUEST']._serialized_end = 5446
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESREQUEST_INLINESOURCE']._serialized_start = 5342
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESREQUEST_INLINESOURCE']._serialized_end = 5436
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESRESPONSE']._serialized_start = 5449
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESRESPONSE']._serialized_end = 5595
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESMETADATA']._serialized_start = 5598
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESMETADATA']._serialized_end = 5737
    _globals['_IMPORTCOMPLETIONSUGGESTIONSREQUEST']._serialized_start = 5740
    _globals['_IMPORTCOMPLETIONSUGGESTIONSREQUEST']._serialized_end = 6272
    _globals['_IMPORTCOMPLETIONSUGGESTIONSREQUEST_INLINESOURCE']._serialized_start = 6167
    _globals['_IMPORTCOMPLETIONSUGGESTIONSREQUEST_INLINESOURCE']._serialized_end = 6262
    _globals['_IMPORTCOMPLETIONSUGGESTIONSRESPONSE']._serialized_start = 6275
    _globals['_IMPORTCOMPLETIONSUGGESTIONSRESPONSE']._serialized_end = 6429
    _globals['_IMPORTCOMPLETIONSUGGESTIONSMETADATA']._serialized_start = 6432
    _globals['_IMPORTCOMPLETIONSUGGESTIONSMETADATA']._serialized_end = 6613