"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1beta/import_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1beta import completion_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_completion__pb2
from .....google.cloud.discoveryengine.v1beta import document_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_document__pb2
from .....google.cloud.discoveryengine.v1beta import sample_query_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_sample__query__pb2
from .....google.cloud.discoveryengine.v1beta import user_event_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_user__event__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from .....google.type import date_pb2 as google_dot_type_dot_date__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/discoveryengine/v1beta/import_config.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a4google/cloud/discoveryengine/v1beta/completion.proto\x1a2google/cloud/discoveryengine/v1beta/document.proto\x1a6google/cloud/discoveryengine/v1beta/sample_query.proto\x1a4google/cloud/discoveryengine/v1beta/user_event.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x16google/type/date.proto"9\n\tGcsSource\x12\x17\n\ninput_uris\x18\x01 \x03(\tB\x03\xe0A\x02\x12\x13\n\x0bdata_schema\x18\x02 \x01(\t"\xbc\x01\n\x0eBigQuerySource\x12+\n\x0epartition_date\x18\x05 \x01(\x0b2\x11.google.type.DateH\x00\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x17\n\x0fgcs_staging_dir\x18\x04 \x01(\t\x12\x13\n\x0bdata_schema\x18\x06 \x01(\tB\x0b\n\tpartition"\x89\x01\n\rSpannerSource\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x18\n\x0binstance_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdatabase_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x19\n\x11enable_data_boost\x18\x05 \x01(\x08"\xa9\x07\n\x0fBigtableOptions\x12\x16\n\x0ekey_field_name\x18\x01 \x01(\t\x12T\n\x08families\x18\x02 \x03(\x0b2B.google.cloud.discoveryengine.v1beta.BigtableOptions.FamiliesEntry\x1a\x9a\x02\n\x14BigtableColumnFamily\x12\x12\n\nfield_name\x18\x01 \x01(\t\x12O\n\x08encoding\x18\x02 \x01(\x0e2=.google.cloud.discoveryengine.v1beta.BigtableOptions.Encoding\x12G\n\x04type\x18\x03 \x01(\x0e29.google.cloud.discoveryengine.v1beta.BigtableOptions.Type\x12T\n\x07columns\x18\x04 \x03(\x0b2C.google.cloud.discoveryengine.v1beta.BigtableOptions.BigtableColumn\x1a\xd6\x01\n\x0eBigtableColumn\x12\x16\n\tqualifier\x18\x01 \x01(\x0cB\x03\xe0A\x02\x12\x12\n\nfield_name\x18\x02 \x01(\t\x12O\n\x08encoding\x18\x03 \x01(\x0e2=.google.cloud.discoveryengine.v1beta.BigtableOptions.Encoding\x12G\n\x04type\x18\x04 \x01(\x0e29.google.cloud.discoveryengine.v1beta.BigtableOptions.Type\x1az\n\rFamiliesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12X\n\x05value\x18\x02 \x01(\x0b2I.google.cloud.discoveryengine.v1beta.BigtableOptions.BigtableColumnFamily:\x028\x01"z\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06STRING\x10\x01\x12\n\n\x06NUMBER\x10\x02\x12\x0b\n\x07INTEGER\x10\x03\x12\x0f\n\x0bVAR_INTEGER\x10\x04\x12\x0f\n\x0bBIG_NUMERIC\x10\x05\x12\x0b\n\x07BOOLEAN\x10\x06\x12\x08\n\x04JSON\x10\x07":\n\x08Encoding\x12\x18\n\x14ENCODING_UNSPECIFIED\x10\x00\x12\x08\n\x04TEXT\x10\x01\x12\n\n\x06BINARY\x10\x02"\xaa\x01\n\x0eBigtableSource\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x18\n\x0binstance_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12S\n\x10bigtable_options\x18\x04 \x01(\x0b24.google.cloud.discoveryengine.v1beta.BigtableOptionsB\x03\xe0A\x02"\x83\x01\n\x0fFhirStoreSource\x12?\n\nfhir_store\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#healthcare.googleapis.com/FhirStore\x12\x17\n\x0fgcs_staging_dir\x18\x02 \x01(\t\x12\x16\n\x0eresource_types\x18\x03 \x03(\t"\x99\x01\n\x0eCloudSqlSource\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x18\n\x0binstance_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdatabase_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x17\n\x0fgcs_staging_dir\x18\x05 \x01(\t\x12\x0f\n\x07offload\x18\x06 \x01(\x08"\xa0\x01\n\rAlloyDbSource\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x18\n\x0blocation_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x17\n\ncluster_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdatabase_id\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x05 \x01(\tB\x03\xe0A\x02\x12\x17\n\x0fgcs_staging_dir\x18\x06 \x01(\t"t\n\x0fFirestoreSource\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x18\n\x0bdatabase_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rcollection_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x17\n\x0fgcs_staging_dir\x18\x04 \x01(\t"8\n\x11ImportErrorConfig\x12\x14\n\ngcs_prefix\x18\x01 \x01(\tH\x00B\r\n\x0bdestination"\x87\x04\n\x17ImportUserEventsRequest\x12b\n\rinline_source\x18\x02 \x01(\x0b2I.google.cloud.discoveryengine.v1beta.ImportUserEventsRequest.InlineSourceH\x00\x12D\n\ngcs_source\x18\x03 \x01(\x0b2..google.cloud.discoveryengine.v1beta.GcsSourceH\x00\x12N\n\x0fbigquery_source\x18\x04 \x01(\x0b23.google.cloud.discoveryengine.v1beta.BigQuerySourceH\x00\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x12L\n\x0cerror_config\x18\x05 \x01(\x0b26.google.cloud.discoveryengine.v1beta.ImportErrorConfig\x1aX\n\x0cInlineSource\x12H\n\x0buser_events\x18\x01 \x03(\x0b2..google.cloud.discoveryengine.v1beta.UserEventB\x03\xe0A\x02B\x08\n\x06source"\xcf\x01\n\x18ImportUserEventsResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12L\n\x0cerror_config\x18\x02 \x01(\x0b26.google.cloud.discoveryengine.v1beta.ImportErrorConfig\x12\x1b\n\x13joined_events_count\x18\x03 \x01(\x03\x12\x1d\n\x15unjoined_events_count\x18\x04 \x01(\x03"\xaa\x01\n\x18ImportUserEventsMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rsuccess_count\x18\x03 \x01(\x03\x12\x15\n\rfailure_count\x18\x04 \x01(\x03"\xbe\x01\n\x17ImportDocumentsMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rsuccess_count\x18\x03 \x01(\x03\x12\x15\n\rfailure_count\x18\x04 \x01(\x03\x12\x13\n\x0btotal_count\x18\x05 \x01(\x03"\x83\n\n\x16ImportDocumentsRequest\x12a\n\rinline_source\x18\x02 \x01(\x0b2H.google.cloud.discoveryengine.v1beta.ImportDocumentsRequest.InlineSourceH\x00\x12D\n\ngcs_source\x18\x03 \x01(\x0b2..google.cloud.discoveryengine.v1beta.GcsSourceH\x00\x12N\n\x0fbigquery_source\x18\x04 \x01(\x0b23.google.cloud.discoveryengine.v1beta.BigQuerySourceH\x00\x12Q\n\x11fhir_store_source\x18\n \x01(\x0b24.google.cloud.discoveryengine.v1beta.FhirStoreSourceH\x00\x12L\n\x0espanner_source\x18\x0b \x01(\x0b22.google.cloud.discoveryengine.v1beta.SpannerSourceH\x00\x12O\n\x10cloud_sql_source\x18\x0c \x01(\x0b23.google.cloud.discoveryengine.v1beta.CloudSqlSourceH\x00\x12P\n\x10firestore_source\x18\r \x01(\x0b24.google.cloud.discoveryengine.v1beta.FirestoreSourceH\x00\x12M\n\x0falloy_db_source\x18\x0e \x01(\x0b22.google.cloud.discoveryengine.v1beta.AlloyDbSourceH\x00\x12N\n\x0fbigtable_source\x18\x0f \x01(\x0b23.google.cloud.discoveryengine.v1beta.BigtableSourceH\x00\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Branch\x12L\n\x0cerror_config\x18\x05 \x01(\x0b26.google.cloud.discoveryengine.v1beta.ImportErrorConfig\x12k\n\x13reconciliation_mode\x18\x06 \x01(\x0e2N.google.cloud.discoveryengine.v1beta.ImportDocumentsRequest.ReconciliationMode\x12/\n\x0bupdate_mask\x18\x07 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12\x19\n\x11auto_generate_ids\x18\x08 \x01(\x08\x12\x10\n\x08id_field\x18\t \x01(\t\x1aU\n\x0cInlineSource\x12E\n\tdocuments\x18\x01 \x03(\x0b2-.google.cloud.discoveryengine.v1beta.DocumentB\x03\xe0A\x02"T\n\x12ReconciliationMode\x12#\n\x1fRECONCILIATION_MODE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bINCREMENTAL\x10\x01\x12\x08\n\x04FULL\x10\x02B\x08\n\x06source"\x92\x01\n\x17ImportDocumentsResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12L\n\x0cerror_config\x18\x02 \x01(\x0b26.google.cloud.discoveryengine.v1beta.ImportErrorConfig"\x91\x03\n&ImportSuggestionDenyListEntriesRequest\x12q\n\rinline_source\x18\x02 \x01(\x0b2X.google.cloud.discoveryengine.v1beta.ImportSuggestionDenyListEntriesRequest.InlineSourceH\x00\x12D\n\ngcs_source\x18\x03 \x01(\x0b2..google.cloud.discoveryengine.v1beta.GcsSourceH\x00\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x1ab\n\x0cInlineSource\x12R\n\x07entries\x18\x01 \x03(\x0b2<.google.cloud.discoveryengine.v1beta.SuggestionDenyListEntryB\x03\xe0A\x02B\x08\n\x06source"\x92\x01\n\'ImportSuggestionDenyListEntriesResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12\x1e\n\x16imported_entries_count\x18\x02 \x01(\x03\x12\x1c\n\x14failed_entries_count\x18\x03 \x01(\x03"\x8b\x01\n\'ImportSuggestionDenyListEntriesMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xa8\x04\n"ImportCompletionSuggestionsRequest\x12m\n\rinline_source\x18\x02 \x01(\x0b2T.google.cloud.discoveryengine.v1beta.ImportCompletionSuggestionsRequest.InlineSourceH\x00\x12D\n\ngcs_source\x18\x03 \x01(\x0b2..google.cloud.discoveryengine.v1beta.GcsSourceH\x00\x12N\n\x0fbigquery_source\x18\x04 \x01(\x0b23.google.cloud.discoveryengine.v1beta.BigQuerySourceH\x00\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x12L\n\x0cerror_config\x18\x05 \x01(\x0b26.google.cloud.discoveryengine.v1beta.ImportErrorConfig\x1ac\n\x0cInlineSource\x12S\n\x0bsuggestions\x18\x01 \x03(\x0b29.google.cloud.discoveryengine.v1beta.CompletionSuggestionB\x03\xe0A\x02B\x08\n\x06source"\x9e\x01\n#ImportCompletionSuggestionsResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12L\n\x0cerror_config\x18\x02 \x01(\x0b26.google.cloud.discoveryengine.v1beta.ImportErrorConfig"\xb5\x01\n#ImportCompletionSuggestionsMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rsuccess_count\x18\x03 \x01(\x03\x12\x15\n\rfailure_count\x18\x04 \x01(\x03"\x97\x04\n\x1aImportSampleQueriesRequest\x12e\n\rinline_source\x18\x02 \x01(\x0b2L.google.cloud.discoveryengine.v1beta.ImportSampleQueriesRequest.InlineSourceH\x00\x12D\n\ngcs_source\x18\x03 \x01(\x0b2..google.cloud.discoveryengine.v1beta.GcsSourceH\x00\x12N\n\x0fbigquery_source\x18\x04 \x01(\x0b23.google.cloud.discoveryengine.v1beta.BigQuerySourceH\x00\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-discoveryengine.googleapis.com/SampleQuerySet\x12L\n\x0cerror_config\x18\x05 \x01(\x0b26.google.cloud.discoveryengine.v1beta.ImportErrorConfig\x1a]\n\x0cInlineSource\x12M\n\x0esample_queries\x18\x01 \x03(\x0b20.google.cloud.discoveryengine.v1beta.SampleQueryB\x03\xe0A\x02B\x08\n\x06source"\x96\x01\n\x1bImportSampleQueriesResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12L\n\x0cerror_config\x18\x02 \x01(\x0b26.google.cloud.discoveryengine.v1beta.ImportErrorConfig"\xc2\x01\n\x1bImportSampleQueriesMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rsuccess_count\x18\x03 \x01(\x03\x12\x15\n\rfailure_count\x18\x04 \x01(\x03\x12\x13\n\x0btotal_count\x18\x05 \x01(\x03B\x98\x02\n\'com.google.cloud.discoveryengine.v1betaB\x11ImportConfigProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.import_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x11ImportConfigProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
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
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESREQUEST_INLINESOURCE'].fields_by_name['entries']._loaded_options = None
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESREQUEST_INLINESOURCE'].fields_by_name['entries']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_IMPORTCOMPLETIONSUGGESTIONSREQUEST_INLINESOURCE'].fields_by_name['suggestions']._loaded_options = None
    _globals['_IMPORTCOMPLETIONSUGGESTIONSREQUEST_INLINESOURCE'].fields_by_name['suggestions']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTCOMPLETIONSUGGESTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTCOMPLETIONSUGGESTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_IMPORTSAMPLEQUERIESREQUEST_INLINESOURCE'].fields_by_name['sample_queries']._loaded_options = None
    _globals['_IMPORTSAMPLEQUERIESREQUEST_INLINESOURCE'].fields_by_name['sample_queries']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTSAMPLEQUERIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTSAMPLEQUERIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\n-discoveryengine.googleapis.com/SampleQuerySet'
    _globals['_GCSSOURCE']._serialized_start = 488
    _globals['_GCSSOURCE']._serialized_end = 545
    _globals['_BIGQUERYSOURCE']._serialized_start = 548
    _globals['_BIGQUERYSOURCE']._serialized_end = 736
    _globals['_SPANNERSOURCE']._serialized_start = 739
    _globals['_SPANNERSOURCE']._serialized_end = 876
    _globals['_BIGTABLEOPTIONS']._serialized_start = 879
    _globals['_BIGTABLEOPTIONS']._serialized_end = 1816
    _globals['_BIGTABLEOPTIONS_BIGTABLECOLUMNFAMILY']._serialized_start = 1009
    _globals['_BIGTABLEOPTIONS_BIGTABLECOLUMNFAMILY']._serialized_end = 1291
    _globals['_BIGTABLEOPTIONS_BIGTABLECOLUMN']._serialized_start = 1294
    _globals['_BIGTABLEOPTIONS_BIGTABLECOLUMN']._serialized_end = 1508
    _globals['_BIGTABLEOPTIONS_FAMILIESENTRY']._serialized_start = 1510
    _globals['_BIGTABLEOPTIONS_FAMILIESENTRY']._serialized_end = 1632
    _globals['_BIGTABLEOPTIONS_TYPE']._serialized_start = 1634
    _globals['_BIGTABLEOPTIONS_TYPE']._serialized_end = 1756
    _globals['_BIGTABLEOPTIONS_ENCODING']._serialized_start = 1758
    _globals['_BIGTABLEOPTIONS_ENCODING']._serialized_end = 1816
    _globals['_BIGTABLESOURCE']._serialized_start = 1819
    _globals['_BIGTABLESOURCE']._serialized_end = 1989
    _globals['_FHIRSTORESOURCE']._serialized_start = 1992
    _globals['_FHIRSTORESOURCE']._serialized_end = 2123
    _globals['_CLOUDSQLSOURCE']._serialized_start = 2126
    _globals['_CLOUDSQLSOURCE']._serialized_end = 2279
    _globals['_ALLOYDBSOURCE']._serialized_start = 2282
    _globals['_ALLOYDBSOURCE']._serialized_end = 2442
    _globals['_FIRESTORESOURCE']._serialized_start = 2444
    _globals['_FIRESTORESOURCE']._serialized_end = 2560
    _globals['_IMPORTERRORCONFIG']._serialized_start = 2562
    _globals['_IMPORTERRORCONFIG']._serialized_end = 2618
    _globals['_IMPORTUSEREVENTSREQUEST']._serialized_start = 2621
    _globals['_IMPORTUSEREVENTSREQUEST']._serialized_end = 3140
    _globals['_IMPORTUSEREVENTSREQUEST_INLINESOURCE']._serialized_start = 3042
    _globals['_IMPORTUSEREVENTSREQUEST_INLINESOURCE']._serialized_end = 3130
    _globals['_IMPORTUSEREVENTSRESPONSE']._serialized_start = 3143
    _globals['_IMPORTUSEREVENTSRESPONSE']._serialized_end = 3350
    _globals['_IMPORTUSEREVENTSMETADATA']._serialized_start = 3353
    _globals['_IMPORTUSEREVENTSMETADATA']._serialized_end = 3523
    _globals['_IMPORTDOCUMENTSMETADATA']._serialized_start = 3526
    _globals['_IMPORTDOCUMENTSMETADATA']._serialized_end = 3716
    _globals['_IMPORTDOCUMENTSREQUEST']._serialized_start = 3719
    _globals['_IMPORTDOCUMENTSREQUEST']._serialized_end = 5002
    _globals['_IMPORTDOCUMENTSREQUEST_INLINESOURCE']._serialized_start = 4821
    _globals['_IMPORTDOCUMENTSREQUEST_INLINESOURCE']._serialized_end = 4906
    _globals['_IMPORTDOCUMENTSREQUEST_RECONCILIATIONMODE']._serialized_start = 4908
    _globals['_IMPORTDOCUMENTSREQUEST_RECONCILIATIONMODE']._serialized_end = 4992
    _globals['_IMPORTDOCUMENTSRESPONSE']._serialized_start = 5005
    _globals['_IMPORTDOCUMENTSRESPONSE']._serialized_end = 5151
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESREQUEST']._serialized_start = 5154
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESREQUEST']._serialized_end = 5555
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESREQUEST_INLINESOURCE']._serialized_start = 5447
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESREQUEST_INLINESOURCE']._serialized_end = 5545
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESRESPONSE']._serialized_start = 5558
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESRESPONSE']._serialized_end = 5704
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESMETADATA']._serialized_start = 5707
    _globals['_IMPORTSUGGESTIONDENYLISTENTRIESMETADATA']._serialized_end = 5846
    _globals['_IMPORTCOMPLETIONSUGGESTIONSREQUEST']._serialized_start = 5849
    _globals['_IMPORTCOMPLETIONSUGGESTIONSREQUEST']._serialized_end = 6401
    _globals['_IMPORTCOMPLETIONSUGGESTIONSREQUEST_INLINESOURCE']._serialized_start = 6292
    _globals['_IMPORTCOMPLETIONSUGGESTIONSREQUEST_INLINESOURCE']._serialized_end = 6391
    _globals['_IMPORTCOMPLETIONSUGGESTIONSRESPONSE']._serialized_start = 6404
    _globals['_IMPORTCOMPLETIONSUGGESTIONSRESPONSE']._serialized_end = 6562
    _globals['_IMPORTCOMPLETIONSUGGESTIONSMETADATA']._serialized_start = 6565
    _globals['_IMPORTCOMPLETIONSUGGESTIONSMETADATA']._serialized_end = 6746
    _globals['_IMPORTSAMPLEQUERIESREQUEST']._serialized_start = 6749
    _globals['_IMPORTSAMPLEQUERIESREQUEST']._serialized_end = 7284
    _globals['_IMPORTSAMPLEQUERIESREQUEST_INLINESOURCE']._serialized_start = 7181
    _globals['_IMPORTSAMPLEQUERIESREQUEST_INLINESOURCE']._serialized_end = 7274
    _globals['_IMPORTSAMPLEQUERIESRESPONSE']._serialized_start = 7287
    _globals['_IMPORTSAMPLEQUERIESRESPONSE']._serialized_end = 7437
    _globals['_IMPORTSAMPLEQUERIESMETADATA']._serialized_start = 7440
    _globals['_IMPORTSAMPLEQUERIESMETADATA']._serialized_end = 7634