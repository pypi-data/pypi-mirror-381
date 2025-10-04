"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/dataplex/v1/logs.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dataplex.v1 import datascans_common_pb2 as google_dot_cloud_dot_dataplex_dot_v1_dot_datascans__common__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/cloud/dataplex/v1/logs.proto\x12\x18google.cloud.dataplex.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/dataplex/v1/datascans_common.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x9d\x0c\n\x0eDiscoveryEvent\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0f\n\x07lake_id\x18\x02 \x01(\t\x12\x0f\n\x07zone_id\x18\x03 \x01(\t\x12\x10\n\x08asset_id\x18\x04 \x01(\t\x12\x15\n\rdata_location\x18\x05 \x01(\t\x12\x13\n\x0bdatascan_id\x18\x06 \x01(\t\x12@\n\x04type\x18\n \x01(\x0e22.google.cloud.dataplex.v1.DiscoveryEvent.EventType\x12H\n\x06config\x18\x14 \x01(\x0b26.google.cloud.dataplex.v1.DiscoveryEvent.ConfigDetailsH\x00\x12H\n\x06entity\x18\x15 \x01(\x0b26.google.cloud.dataplex.v1.DiscoveryEvent.EntityDetailsH\x00\x12N\n\tpartition\x18\x16 \x01(\x0b29.google.cloud.dataplex.v1.DiscoveryEvent.PartitionDetailsH\x00\x12H\n\x06action\x18\x17 \x01(\x0b26.google.cloud.dataplex.v1.DiscoveryEvent.ActionDetailsH\x00\x12F\n\x05table\x18\x18 \x01(\x0b25.google.cloud.dataplex.v1.DiscoveryEvent.TableDetailsH\x00\x1a\x9e\x01\n\rConfigDetails\x12Z\n\nparameters\x18\x01 \x03(\x0b2F.google.cloud.dataplex.v1.DiscoveryEvent.ConfigDetails.ParametersEntry\x1a1\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1ab\n\rEntityDetails\x12\x0e\n\x06entity\x18\x01 \x01(\t\x12A\n\x04type\x18\x02 \x01(\x0e23.google.cloud.dataplex.v1.DiscoveryEvent.EntityType\x1a_\n\x0cTableDetails\x12\r\n\x05table\x18\x01 \x01(\t\x12@\n\x04type\x18\x02 \x01(\x0e22.google.cloud.dataplex.v1.DiscoveryEvent.TableType\x1a\x98\x01\n\x10PartitionDetails\x12\x11\n\tpartition\x18\x01 \x01(\t\x12\x0e\n\x06entity\x18\x02 \x01(\t\x12A\n\x04type\x18\x03 \x01(\x0e23.google.cloud.dataplex.v1.DiscoveryEvent.EntityType\x12\x1e\n\x16sampled_data_locations\x18\x04 \x03(\t\x1a,\n\rActionDetails\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05issue\x18\x02 \x01(\t"\x82\x02\n\tEventType\x12\x1a\n\x16EVENT_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06CONFIG\x10\x01\x12\x12\n\x0eENTITY_CREATED\x10\x02\x12\x12\n\x0eENTITY_UPDATED\x10\x03\x12\x12\n\x0eENTITY_DELETED\x10\x04\x12\x15\n\x11PARTITION_CREATED\x10\x05\x12\x15\n\x11PARTITION_UPDATED\x10\x06\x12\x15\n\x11PARTITION_DELETED\x10\x07\x12\x13\n\x0fTABLE_PUBLISHED\x10\n\x12\x11\n\rTABLE_UPDATED\x10\x0b\x12\x11\n\rTABLE_IGNORED\x10\x0c\x12\x11\n\rTABLE_DELETED\x10\r"A\n\nEntityType\x12\x1b\n\x17ENTITY_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05TABLE\x10\x01\x12\x0b\n\x07FILESET\x10\x02"`\n\tTableType\x12\x1a\n\x16TABLE_TYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0eEXTERNAL_TABLE\x10\x01\x12\x11\n\rBIGLAKE_TABLE\x10\x02\x12\x10\n\x0cOBJECT_TABLE\x10\x03B\t\n\x07details"\xc5\x05\n\x08JobEvent\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x12.\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x127\n\x05state\x18\x05 \x01(\x0e2(.google.cloud.dataplex.v1.JobEvent.State\x12\x0f\n\x07retries\x18\x06 \x01(\x05\x125\n\x04type\x18\x07 \x01(\x0e2\'.google.cloud.dataplex.v1.JobEvent.Type\x12;\n\x07service\x18\x08 \x01(\x0e2*.google.cloud.dataplex.v1.JobEvent.Service\x12\x13\n\x0bservice_job\x18\t \x01(\t\x12N\n\x11execution_trigger\x18\x0b \x01(\x0e23.google.cloud.dataplex.v1.JobEvent.ExecutionTrigger"5\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05SPARK\x10\x01\x12\x0c\n\x08NOTEBOOK\x10\x02"U\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\n\n\x06FAILED\x10\x02\x12\r\n\tCANCELLED\x10\x03\x12\x0b\n\x07ABORTED\x10\x04"0\n\x07Service\x12\x17\n\x13SERVICE_UNSPECIFIED\x10\x00\x12\x0c\n\x08DATAPROC\x10\x01"W\n\x10ExecutionTrigger\x12!\n\x1dEXECUTION_TRIGGER_UNSPECIFIED\x10\x00\x12\x0f\n\x0bTASK_CONFIG\x10\x01\x12\x0f\n\x0bRUN_REQUEST\x10\x02"\xbd\x05\n\x0cSessionEvent\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x12\n\nsession_id\x18\x03 \x01(\t\x12>\n\x04type\x18\x04 \x01(\x0e20.google.cloud.dataplex.v1.SessionEvent.EventType\x12C\n\x05query\x18\x05 \x01(\x0b22.google.cloud.dataplex.v1.SessionEvent.QueryDetailH\x00\x12\x17\n\x0fevent_succeeded\x18\x06 \x01(\x08\x12\x1c\n\x14fast_startup_enabled\x18\x07 \x01(\x08\x126\n\x13unassigned_duration\x18\x08 \x01(\x0b2\x19.google.protobuf.Duration\x1a\xa3\x02\n\x0bQueryDetail\x12\x10\n\x08query_id\x18\x01 \x01(\t\x12\x12\n\nquery_text\x18\x02 \x01(\t\x12I\n\x06engine\x18\x03 \x01(\x0e29.google.cloud.dataplex.v1.SessionEvent.QueryDetail.Engine\x12+\n\x08duration\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x12\x19\n\x11result_size_bytes\x18\x05 \x01(\x03\x12\x1c\n\x14data_processed_bytes\x18\x06 \x01(\x03"=\n\x06Engine\x12\x16\n\x12ENGINE_UNSPECIFIED\x10\x00\x12\r\n\tSPARK_SQL\x10\x01\x12\x0c\n\x08BIGQUERY\x10\x02"S\n\tEventType\x12\x1a\n\x16EVENT_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05START\x10\x01\x12\x08\n\x04STOP\x10\x02\x12\t\n\x05QUERY\x10\x03\x12\n\n\x06CREATE\x10\x04B\x08\n\x06detail"\xba\x07\n\x0fGovernanceEvent\x12\x0f\n\x07message\x18\x01 \x01(\t\x12G\n\nevent_type\x18\x02 \x01(\x0e23.google.cloud.dataplex.v1.GovernanceEvent.EventType\x12E\n\x06entity\x18\x03 \x01(\x0b20.google.cloud.dataplex.v1.GovernanceEvent.EntityH\x00\x88\x01\x01\x1a\xd2\x01\n\x06Entity\x123\n\x06entity\x18\x01 \x01(\tB#\xfaA \n\x1edataplex.googleapis.com/Entity\x12P\n\x0bentity_type\x18\x02 \x01(\x0e2;.google.cloud.dataplex.v1.GovernanceEvent.Entity.EntityType"A\n\nEntityType\x12\x1b\n\x17ENTITY_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05TABLE\x10\x01\x12\x0b\n\x07FILESET\x10\x02"\xa5\x04\n\tEventType\x12\x1a\n\x16EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aRESOURCE_IAM_POLICY_UPDATE\x10\x01\x12\x19\n\x15BIGQUERY_TABLE_CREATE\x10\x02\x12\x19\n\x15BIGQUERY_TABLE_UPDATE\x10\x03\x12\x19\n\x15BIGQUERY_TABLE_DELETE\x10\x04\x12\x1e\n\x1aBIGQUERY_CONNECTION_CREATE\x10\x05\x12\x1e\n\x1aBIGQUERY_CONNECTION_UPDATE\x10\x06\x12\x1e\n\x1aBIGQUERY_CONNECTION_DELETE\x10\x07\x12\x1c\n\x18BIGQUERY_TAXONOMY_CREATE\x10\n\x12\x1e\n\x1aBIGQUERY_POLICY_TAG_CREATE\x10\x0b\x12\x1e\n\x1aBIGQUERY_POLICY_TAG_DELETE\x10\x0c\x12&\n"BIGQUERY_POLICY_TAG_SET_IAM_POLICY\x10\r\x12\x18\n\x14ACCESS_POLICY_UPDATE\x10\x0e\x12%\n!GOVERNANCE_RULE_MATCHED_RESOURCES\x10\x0f\x12(\n$GOVERNANCE_RULE_SEARCH_LIMIT_EXCEEDS\x10\x10\x12\x1a\n\x16GOVERNANCE_RULE_ERRORS\x10\x11\x12\x1e\n\x1aGOVERNANCE_RULE_PROCESSING\x10\x12B\t\n\x07_entity"\xe5\x13\n\rDataScanEvent\x12\x13\n\x0bdata_source\x18\x01 \x01(\t\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x12/\n\x0bcreate_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.Timestamp\x12.\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12>\n\x04type\x18\x05 \x01(\x0e20.google.cloud.dataplex.v1.DataScanEvent.ScanType\x12<\n\x05state\x18\x06 \x01(\x0e2-.google.cloud.dataplex.v1.DataScanEvent.State\x12\x0f\n\x07message\x18\x07 \x01(\t\x12\x14\n\x0cspec_version\x18\x08 \x01(\t\x12@\n\x07trigger\x18\t \x01(\x0e2/.google.cloud.dataplex.v1.DataScanEvent.Trigger\x12<\n\x05scope\x18\n \x01(\x0e2-.google.cloud.dataplex.v1.DataScanEvent.Scope\x12Q\n\x0cdata_profile\x18e \x01(\x0b29.google.cloud.dataplex.v1.DataScanEvent.DataProfileResultH\x00\x12Q\n\x0cdata_quality\x18f \x01(\x0b29.google.cloud.dataplex.v1.DataScanEvent.DataQualityResultH\x00\x12b\n\x14data_profile_configs\x18\xc9\x01 \x01(\x0b2A.google.cloud.dataplex.v1.DataScanEvent.DataProfileAppliedConfigsH\x01\x12b\n\x14data_quality_configs\x18\xca\x01 \x01(\x0b2A.google.cloud.dataplex.v1.DataScanEvent.DataQualityAppliedConfigsH\x01\x12_\n\x18post_scan_actions_result\x18\x0b \x01(\x0b2=.google.cloud.dataplex.v1.DataScanEvent.PostScanActionsResult\x12\\\n\x19catalog_publishing_status\x18\r \x01(\x0b29.google.cloud.dataplex.v1.DataScanCatalogPublishingStatus\x1a&\n\x11DataProfileResult\x12\x11\n\trow_count\x18\x01 \x01(\x03\x1a\x9c\x04\n\x11DataQualityResult\x12\x11\n\trow_count\x18\x01 \x01(\x03\x12\x0e\n\x06passed\x18\x02 \x01(\x08\x12h\n\x10dimension_passed\x18\x03 \x03(\x0b2N.google.cloud.dataplex.v1.DataScanEvent.DataQualityResult.DimensionPassedEntry\x12\r\n\x05score\x18\x04 \x01(\x02\x12f\n\x0fdimension_score\x18\x05 \x03(\x0b2M.google.cloud.dataplex.v1.DataScanEvent.DataQualityResult.DimensionScoreEntry\x12`\n\x0ccolumn_score\x18\x06 \x03(\x0b2J.google.cloud.dataplex.v1.DataScanEvent.DataQualityResult.ColumnScoreEntry\x1a6\n\x14DimensionPassedEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x028\x01\x1a5\n\x13DimensionScoreEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x028\x01\x1a2\n\x10ColumnScoreEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x028\x01\x1ap\n\x19DataProfileAppliedConfigs\x12\x18\n\x10sampling_percent\x18\x01 \x01(\x02\x12\x1a\n\x12row_filter_applied\x18\x02 \x01(\x08\x12\x1d\n\x15column_filter_applied\x18\x03 \x01(\x08\x1aQ\n\x19DataQualityAppliedConfigs\x12\x18\n\x10sampling_percent\x18\x01 \x01(\x02\x12\x1a\n\x12row_filter_applied\x18\x02 \x01(\x08\x1a\xe6\x02\n\x15PostScanActionsResult\x12r\n\x16bigquery_export_result\x18\x01 \x01(\x0b2R.google.cloud.dataplex.v1.DataScanEvent.PostScanActionsResult.BigQueryExportResult\x1a\xd8\x01\n\x14BigQueryExportResult\x12g\n\x05state\x18\x01 \x01(\x0e2X.google.cloud.dataplex.v1.DataScanEvent.PostScanActionsResult.BigQueryExportResult.State\x12\x0f\n\x07message\x18\x02 \x01(\t"F\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\n\n\x06FAILED\x10\x02\x12\x0b\n\x07SKIPPED\x10\x03"]\n\x08ScanType\x12\x19\n\x15SCAN_TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cDATA_PROFILE\x10\x01\x12\x10\n\x0cDATA_QUALITY\x10\x02\x12\x12\n\x0eDATA_DISCOVERY\x10\x04"b\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07STARTED\x10\x01\x12\r\n\tSUCCEEDED\x10\x02\x12\n\n\x06FAILED\x10\x03\x12\r\n\tCANCELLED\x10\x04\x12\x0b\n\x07CREATED\x10\x05"?\n\x07Trigger\x12\x17\n\x13TRIGGER_UNSPECIFIED\x10\x00\x12\r\n\tON_DEMAND\x10\x01\x12\x0c\n\x08SCHEDULE\x10\x02"9\n\x05Scope\x12\x15\n\x11SCOPE_UNSPECIFIED\x10\x00\x12\x08\n\x04FULL\x10\x01\x12\x0f\n\x0bINCREMENTAL\x10\x02B\x08\n\x06resultB\x10\n\x0eappliedConfigs"\x99\x07\n\x19DataQualityScanRuleResult\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x13\n\x0bdata_source\x18\x02 \x01(\t\x12\x0e\n\x06column\x18\x03 \x01(\t\x12\x11\n\trule_name\x18\x04 \x01(\t\x12O\n\trule_type\x18\x05 \x01(\x0e2<.google.cloud.dataplex.v1.DataQualityScanRuleResult.RuleType\x12Z\n\x0eevalution_type\x18\x06 \x01(\x0e2B.google.cloud.dataplex.v1.DataQualityScanRuleResult.EvaluationType\x12\x16\n\x0erule_dimension\x18\x07 \x01(\t\x12\x19\n\x11threshold_percent\x18\x08 \x01(\x01\x12J\n\x06result\x18\t \x01(\x0e2:.google.cloud.dataplex.v1.DataQualityScanRuleResult.Result\x12\x1b\n\x13evaluated_row_count\x18\n \x01(\x03\x12\x18\n\x10passed_row_count\x18\x0b \x01(\x03\x12\x16\n\x0enull_row_count\x18\x0c \x01(\x03\x12\x1b\n\x13assertion_row_count\x18\r \x01(\x03"\x92\x02\n\x08RuleType\x12\x19\n\x15RULE_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14NON_NULL_EXPECTATION\x10\x01\x12\x15\n\x11RANGE_EXPECTATION\x10\x02\x12\x15\n\x11REGEX_EXPECTATION\x10\x03\x12\x1d\n\x19ROW_CONDITION_EXPECTATION\x10\x04\x12\x13\n\x0fSET_EXPECTATION\x10\x05\x12\x1f\n\x1bSTATISTIC_RANGE_EXPECTATION\x10\x06\x12\x1f\n\x1bTABLE_CONDITION_EXPECTATION\x10\x07\x12\x1a\n\x16UNIQUENESS_EXPECTATION\x10\x08\x12\x11\n\rSQL_ASSERTION\x10\t"M\n\x0eEvaluationType\x12\x1f\n\x1bEVALUATION_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PER_ROW\x10\x01\x12\r\n\tAGGREGATE\x10\x02"8\n\x06Result\x12\x16\n\x12RESULT_UNSPECIFIED\x10\x00\x12\n\n\x06PASSED\x10\x01\x12\n\n\x06FAILED\x10\x02"\x9a\x03\n\x15BusinessGlossaryEvent\x12\x0f\n\x07message\x18\x01 \x01(\t\x12M\n\nevent_type\x18\x02 \x01(\x0e29.google.cloud.dataplex.v1.BusinessGlossaryEvent.EventType\x12\x10\n\x08resource\x18\x03 \x01(\t"\x8e\x02\n\tEventType\x12\x1a\n\x16EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fGLOSSARY_CREATE\x10\x01\x12\x13\n\x0fGLOSSARY_UPDATE\x10\x02\x12\x13\n\x0fGLOSSARY_DELETE\x10\x03\x12\x1c\n\x18GLOSSARY_CATEGORY_CREATE\x10\x04\x12\x1c\n\x18GLOSSARY_CATEGORY_UPDATE\x10\x05\x12\x1c\n\x18GLOSSARY_CATEGORY_DELETE\x10\x06\x12\x18\n\x14GLOSSARY_TERM_CREATE\x10\x07\x12\x18\n\x14GLOSSARY_TERM_UPDATE\x10\x08\x12\x18\n\x14GLOSSARY_TERM_DELETE\x10\t"\xd2\x01\n\x0eEntryLinkEvent\x12\x0f\n\x07message\x18\x01 \x01(\t\x12F\n\nevent_type\x18\x02 \x01(\x0e22.google.cloud.dataplex.v1.EntryLinkEvent.EventType\x12\x10\n\x08resource\x18\x03 \x01(\t"U\n\tEventType\x12\x1a\n\x16EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11ENTRY_LINK_CREATE\x10\x01\x12\x15\n\x11ENTRY_LINK_DELETE\x10\x02Be\n\x1ccom.google.cloud.dataplex.v1B\tLogsProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataplex.v1.logs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.dataplex.v1B\tLogsProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpb'
    _globals['_DISCOVERYEVENT_CONFIGDETAILS_PARAMETERSENTRY']._loaded_options = None
    _globals['_DISCOVERYEVENT_CONFIGDETAILS_PARAMETERSENTRY']._serialized_options = b'8\x01'
    _globals['_GOVERNANCEEVENT_ENTITY'].fields_by_name['entity']._loaded_options = None
    _globals['_GOVERNANCEEVENT_ENTITY'].fields_by_name['entity']._serialized_options = b'\xfaA \n\x1edataplex.googleapis.com/Entity'
    _globals['_DATASCANEVENT_DATAQUALITYRESULT_DIMENSIONPASSEDENTRY']._loaded_options = None
    _globals['_DATASCANEVENT_DATAQUALITYRESULT_DIMENSIONPASSEDENTRY']._serialized_options = b'8\x01'
    _globals['_DATASCANEVENT_DATAQUALITYRESULT_DIMENSIONSCOREENTRY']._loaded_options = None
    _globals['_DATASCANEVENT_DATAQUALITYRESULT_DIMENSIONSCOREENTRY']._serialized_options = b'8\x01'
    _globals['_DATASCANEVENT_DATAQUALITYRESULT_COLUMNSCOREENTRY']._loaded_options = None
    _globals['_DATASCANEVENT_DATAQUALITYRESULT_COLUMNSCOREENTRY']._serialized_options = b'8\x01'
    _globals['_DISCOVERYEVENT']._serialized_start = 240
    _globals['_DISCOVERYEVENT']._serialized_end = 1805
    _globals['_DISCOVERYEVENT_CONFIGDETAILS']._serialized_start = 812
    _globals['_DISCOVERYEVENT_CONFIGDETAILS']._serialized_end = 970
    _globals['_DISCOVERYEVENT_CONFIGDETAILS_PARAMETERSENTRY']._serialized_start = 921
    _globals['_DISCOVERYEVENT_CONFIGDETAILS_PARAMETERSENTRY']._serialized_end = 970
    _globals['_DISCOVERYEVENT_ENTITYDETAILS']._serialized_start = 972
    _globals['_DISCOVERYEVENT_ENTITYDETAILS']._serialized_end = 1070
    _globals['_DISCOVERYEVENT_TABLEDETAILS']._serialized_start = 1072
    _globals['_DISCOVERYEVENT_TABLEDETAILS']._serialized_end = 1167
    _globals['_DISCOVERYEVENT_PARTITIONDETAILS']._serialized_start = 1170
    _globals['_DISCOVERYEVENT_PARTITIONDETAILS']._serialized_end = 1322
    _globals['_DISCOVERYEVENT_ACTIONDETAILS']._serialized_start = 1324
    _globals['_DISCOVERYEVENT_ACTIONDETAILS']._serialized_end = 1368
    _globals['_DISCOVERYEVENT_EVENTTYPE']._serialized_start = 1371
    _globals['_DISCOVERYEVENT_EVENTTYPE']._serialized_end = 1629
    _globals['_DISCOVERYEVENT_ENTITYTYPE']._serialized_start = 1631
    _globals['_DISCOVERYEVENT_ENTITYTYPE']._serialized_end = 1696
    _globals['_DISCOVERYEVENT_TABLETYPE']._serialized_start = 1698
    _globals['_DISCOVERYEVENT_TABLETYPE']._serialized_end = 1794
    _globals['_JOBEVENT']._serialized_start = 1808
    _globals['_JOBEVENT']._serialized_end = 2517
    _globals['_JOBEVENT_TYPE']._serialized_start = 2238
    _globals['_JOBEVENT_TYPE']._serialized_end = 2291
    _globals['_JOBEVENT_STATE']._serialized_start = 2293
    _globals['_JOBEVENT_STATE']._serialized_end = 2378
    _globals['_JOBEVENT_SERVICE']._serialized_start = 2380
    _globals['_JOBEVENT_SERVICE']._serialized_end = 2428
    _globals['_JOBEVENT_EXECUTIONTRIGGER']._serialized_start = 2430
    _globals['_JOBEVENT_EXECUTIONTRIGGER']._serialized_end = 2517
    _globals['_SESSIONEVENT']._serialized_start = 2520
    _globals['_SESSIONEVENT']._serialized_end = 3221
    _globals['_SESSIONEVENT_QUERYDETAIL']._serialized_start = 2835
    _globals['_SESSIONEVENT_QUERYDETAIL']._serialized_end = 3126
    _globals['_SESSIONEVENT_QUERYDETAIL_ENGINE']._serialized_start = 3065
    _globals['_SESSIONEVENT_QUERYDETAIL_ENGINE']._serialized_end = 3126
    _globals['_SESSIONEVENT_EVENTTYPE']._serialized_start = 3128
    _globals['_SESSIONEVENT_EVENTTYPE']._serialized_end = 3211
    _globals['_GOVERNANCEEVENT']._serialized_start = 3224
    _globals['_GOVERNANCEEVENT']._serialized_end = 4178
    _globals['_GOVERNANCEEVENT_ENTITY']._serialized_start = 3405
    _globals['_GOVERNANCEEVENT_ENTITY']._serialized_end = 3615
    _globals['_GOVERNANCEEVENT_ENTITY_ENTITYTYPE']._serialized_start = 1631
    _globals['_GOVERNANCEEVENT_ENTITY_ENTITYTYPE']._serialized_end = 1696
    _globals['_GOVERNANCEEVENT_EVENTTYPE']._serialized_start = 3618
    _globals['_GOVERNANCEEVENT_EVENTTYPE']._serialized_end = 4167
    _globals['_DATASCANEVENT']._serialized_start = 4181
    _globals['_DATASCANEVENT']._serialized_end = 6714
    _globals['_DATASCANEVENT_DATAPROFILERESULT']._serialized_start = 5228
    _globals['_DATASCANEVENT_DATAPROFILERESULT']._serialized_end = 5266
    _globals['_DATASCANEVENT_DATAQUALITYRESULT']._serialized_start = 5269
    _globals['_DATASCANEVENT_DATAQUALITYRESULT']._serialized_end = 5809
    _globals['_DATASCANEVENT_DATAQUALITYRESULT_DIMENSIONPASSEDENTRY']._serialized_start = 5648
    _globals['_DATASCANEVENT_DATAQUALITYRESULT_DIMENSIONPASSEDENTRY']._serialized_end = 5702
    _globals['_DATASCANEVENT_DATAQUALITYRESULT_DIMENSIONSCOREENTRY']._serialized_start = 5704
    _globals['_DATASCANEVENT_DATAQUALITYRESULT_DIMENSIONSCOREENTRY']._serialized_end = 5757
    _globals['_DATASCANEVENT_DATAQUALITYRESULT_COLUMNSCOREENTRY']._serialized_start = 5759
    _globals['_DATASCANEVENT_DATAQUALITYRESULT_COLUMNSCOREENTRY']._serialized_end = 5809
    _globals['_DATASCANEVENT_DATAPROFILEAPPLIEDCONFIGS']._serialized_start = 5811
    _globals['_DATASCANEVENT_DATAPROFILEAPPLIEDCONFIGS']._serialized_end = 5923
    _globals['_DATASCANEVENT_DATAQUALITYAPPLIEDCONFIGS']._serialized_start = 5925
    _globals['_DATASCANEVENT_DATAQUALITYAPPLIEDCONFIGS']._serialized_end = 6006
    _globals['_DATASCANEVENT_POSTSCANACTIONSRESULT']._serialized_start = 6009
    _globals['_DATASCANEVENT_POSTSCANACTIONSRESULT']._serialized_end = 6367
    _globals['_DATASCANEVENT_POSTSCANACTIONSRESULT_BIGQUERYEXPORTRESULT']._serialized_start = 6151
    _globals['_DATASCANEVENT_POSTSCANACTIONSRESULT_BIGQUERYEXPORTRESULT']._serialized_end = 6367
    _globals['_DATASCANEVENT_POSTSCANACTIONSRESULT_BIGQUERYEXPORTRESULT_STATE']._serialized_start = 6297
    _globals['_DATASCANEVENT_POSTSCANACTIONSRESULT_BIGQUERYEXPORTRESULT_STATE']._serialized_end = 6367
    _globals['_DATASCANEVENT_SCANTYPE']._serialized_start = 6369
    _globals['_DATASCANEVENT_SCANTYPE']._serialized_end = 6462
    _globals['_DATASCANEVENT_STATE']._serialized_start = 6464
    _globals['_DATASCANEVENT_STATE']._serialized_end = 6562
    _globals['_DATASCANEVENT_TRIGGER']._serialized_start = 6564
    _globals['_DATASCANEVENT_TRIGGER']._serialized_end = 6627
    _globals['_DATASCANEVENT_SCOPE']._serialized_start = 6629
    _globals['_DATASCANEVENT_SCOPE']._serialized_end = 6686
    _globals['_DATAQUALITYSCANRULERESULT']._serialized_start = 6717
    _globals['_DATAQUALITYSCANRULERESULT']._serialized_end = 7638
    _globals['_DATAQUALITYSCANRULERESULT_RULETYPE']._serialized_start = 7227
    _globals['_DATAQUALITYSCANRULERESULT_RULETYPE']._serialized_end = 7501
    _globals['_DATAQUALITYSCANRULERESULT_EVALUATIONTYPE']._serialized_start = 7503
    _globals['_DATAQUALITYSCANRULERESULT_EVALUATIONTYPE']._serialized_end = 7580
    _globals['_DATAQUALITYSCANRULERESULT_RESULT']._serialized_start = 7582
    _globals['_DATAQUALITYSCANRULERESULT_RESULT']._serialized_end = 7638
    _globals['_BUSINESSGLOSSARYEVENT']._serialized_start = 7641
    _globals['_BUSINESSGLOSSARYEVENT']._serialized_end = 8051
    _globals['_BUSINESSGLOSSARYEVENT_EVENTTYPE']._serialized_start = 7781
    _globals['_BUSINESSGLOSSARYEVENT_EVENTTYPE']._serialized_end = 8051
    _globals['_ENTRYLINKEVENT']._serialized_start = 8054
    _globals['_ENTRYLINKEVENT']._serialized_end = 8264
    _globals['_ENTRYLINKEVENT_EVENTTYPE']._serialized_start = 8179
    _globals['_ENTRYLINKEVENT_EVENTTYPE']._serialized_end = 8264