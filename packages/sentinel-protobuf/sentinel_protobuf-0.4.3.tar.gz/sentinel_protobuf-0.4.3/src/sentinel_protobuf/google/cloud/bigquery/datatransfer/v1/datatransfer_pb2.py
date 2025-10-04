"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/bigquery/datatransfer/v1/datatransfer.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.bigquery.datatransfer.v1 import transfer_pb2 as google_dot_cloud_dot_bigquery_dot_datatransfer_dot_v1_dot_transfer__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/bigquery/datatransfer/v1/datatransfer.proto\x12%google.cloud.bigquery.datatransfer.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a4google/cloud/bigquery/datatransfer/v1/transfer.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x8f\x05\n\x13DataSourceParameter\x12\x10\n\x08param_id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x13\n\x0bdescription\x18\x03 \x01(\t\x12M\n\x04type\x18\x04 \x01(\x0e2?.google.cloud.bigquery.datatransfer.v1.DataSourceParameter.Type\x12\x10\n\x08required\x18\x05 \x01(\x08\x12\x10\n\x08repeated\x18\x06 \x01(\x08\x12\x18\n\x10validation_regex\x18\x07 \x01(\t\x12\x16\n\x0eallowed_values\x18\x08 \x03(\t\x12/\n\tmin_value\x18\t \x01(\x0b2\x1c.google.protobuf.DoubleValue\x12/\n\tmax_value\x18\n \x01(\x0b2\x1c.google.protobuf.DoubleValue\x12J\n\x06fields\x18\x0b \x03(\x0b2:.google.cloud.bigquery.datatransfer.v1.DataSourceParameter\x12\x1e\n\x16validation_description\x18\x0c \x01(\t\x12\x1b\n\x13validation_help_url\x18\r \x01(\t\x12\x11\n\timmutable\x18\x0e \x01(\x08\x12\x0f\n\x07recurse\x18\x0f \x01(\x08\x12\x12\n\ndeprecated\x18\x14 \x01(\x08"s\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06STRING\x10\x01\x12\x0b\n\x07INTEGER\x10\x02\x12\n\n\x06DOUBLE\x10\x03\x12\x0b\n\x07BOOLEAN\x10\x04\x12\n\n\x06RECORD\x10\x05\x12\r\n\tPLUS_PAGE\x10\x06\x12\x08\n\x04LIST\x10\x07"\x9c\t\n\nDataSource\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x16\n\x0edata_source_id\x18\x02 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x12\x11\n\tclient_id\x18\x05 \x01(\t\x12\x0e\n\x06scopes\x18\x06 \x03(\t\x12N\n\rtransfer_type\x18\x07 \x01(\x0e23.google.cloud.bigquery.datatransfer.v1.TransferTypeB\x02\x18\x01\x12\'\n\x1bsupports_multiple_transfers\x18\x08 \x01(\x08B\x02\x18\x01\x12\x1f\n\x17update_deadline_seconds\x18\t \x01(\x05\x12\x18\n\x10default_schedule\x18\n \x01(\t\x12 \n\x18supports_custom_schedule\x18\x0b \x01(\x08\x12N\n\nparameters\x18\x0c \x03(\x0b2:.google.cloud.bigquery.datatransfer.v1.DataSourceParameter\x12\x10\n\x08help_url\x18\r \x01(\t\x12_\n\x12authorization_type\x18\x0e \x01(\x0e2C.google.cloud.bigquery.datatransfer.v1.DataSource.AuthorizationType\x12\\\n\x11data_refresh_type\x18\x0f \x01(\x0e2A.google.cloud.bigquery.datatransfer.v1.DataSource.DataRefreshType\x12(\n default_data_refresh_window_days\x18\x10 \x01(\x05\x12\x1c\n\x14manual_runs_disabled\x18\x11 \x01(\x08\x12<\n\x19minimum_schedule_interval\x18\x12 \x01(\x0b2\x19.google.protobuf.Duration"\x8a\x01\n\x11AuthorizationType\x12"\n\x1eAUTHORIZATION_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12AUTHORIZATION_CODE\x10\x01\x12"\n\x1eGOOGLE_PLUS_AUTHORIZATION_CODE\x10\x02\x12\x15\n\x11FIRST_PARTY_OAUTH\x10\x03"c\n\x0fDataRefreshType\x12!\n\x1dDATA_REFRESH_TYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0eSLIDING_WINDOW\x10\x01\x12\x19\n\x15CUSTOM_SLIDING_WINDOW\x10\x02:\xa5\x01\xeaA\xa1\x01\n.bigquerydatatransfer.googleapis.com/DataSource\x12,projects/{project}/dataSources/{data_source}\x12Aprojects/{project}/locations/{location}/dataSources/{data_source}"\\\n\x14GetDataSourceRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.bigquerydatatransfer.googleapis.com/DataSource"\x87\x01\n\x16ListDataSourcesRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\x12.bigquerydatatransfer.googleapis.com/DataSource\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05"\x80\x01\n\x17ListDataSourcesResponse\x12G\n\x0cdata_sources\x18\x01 \x03(\x0b21.google.cloud.bigquery.datatransfer.v1.DataSource\x12\x1c\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0A\x03"\x92\x02\n\x1bCreateTransferConfigRequest\x12J\n\x06parent\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\x122bigquerydatatransfer.googleapis.com/TransferConfig\x12S\n\x0ftransfer_config\x18\x02 \x01(\x0b25.google.cloud.bigquery.datatransfer.v1.TransferConfigB\x03\xe0A\x02\x12\x1e\n\x12authorization_code\x18\x03 \x01(\tB\x02\x18\x01\x12\x14\n\x0cversion_info\x18\x05 \x01(\t\x12\x1c\n\x14service_account_name\x18\x06 \x01(\t"\xfc\x01\n\x1bUpdateTransferConfigRequest\x12S\n\x0ftransfer_config\x18\x01 \x01(\x0b25.google.cloud.bigquery.datatransfer.v1.TransferConfigB\x03\xe0A\x02\x12\x1e\n\x12authorization_code\x18\x03 \x01(\tB\x02\x18\x01\x124\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12\x14\n\x0cversion_info\x18\x05 \x01(\t\x12\x1c\n\x14service_account_name\x18\x06 \x01(\t"d\n\x18GetTransferConfigRequest\x12H\n\x04name\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2bigquerydatatransfer.googleapis.com/TransferConfig"g\n\x1bDeleteTransferConfigRequest\x12H\n\x04name\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2bigquerydatatransfer.googleapis.com/TransferConfig"V\n\x15GetTransferRunRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'bigquerydatatransfer.googleapis.com/Run"Y\n\x18DeleteTransferRunRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'bigquerydatatransfer.googleapis.com/Run"\xa8\x01\n\x1aListTransferConfigsRequest\x12J\n\x06parent\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\x122bigquerydatatransfer.googleapis.com/TransferConfig\x12\x17\n\x0fdata_source_ids\x18\x02 \x03(\t\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05"\x91\x01\n\x1bListTransferConfigsResponse\x12T\n\x10transfer_configs\x18\x01 \x03(\x0b25.google.cloud.bigquery.datatransfer.v1.TransferConfigB\x03\xe0A\x03\x12\x1c\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0A\x03"\xde\x02\n\x17ListTransferRunsRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\x12\'bigquerydatatransfer.googleapis.com/Run\x12D\n\x06states\x18\x02 \x03(\x0e24.google.cloud.bigquery.datatransfer.v1.TransferState\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12^\n\x0brun_attempt\x18\x05 \x01(\x0e2I.google.cloud.bigquery.datatransfer.v1.ListTransferRunsRequest.RunAttempt"5\n\nRunAttempt\x12\x1b\n\x17RUN_ATTEMPT_UNSPECIFIED\x10\x00\x12\n\n\x06LATEST\x10\x01"\x88\x01\n\x18ListTransferRunsResponse\x12N\n\rtransfer_runs\x18\x01 \x03(\x0b22.google.cloud.bigquery.datatransfer.v1.TransferRunB\x03\xe0A\x03\x12\x1c\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0A\x03"\xe0\x01\n\x17ListTransferLogsRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'bigquerydatatransfer.googleapis.com/Run\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12]\n\rmessage_types\x18\x06 \x03(\x0e2F.google.cloud.bigquery.datatransfer.v1.TransferMessage.MessageSeverity"\x90\x01\n\x18ListTransferLogsResponse\x12V\n\x11transfer_messages\x18\x01 \x03(\x0b26.google.cloud.bigquery.datatransfer.v1.TransferMessageB\x03\xe0A\x03\x12\x1c\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0A\x03"^\n\x16CheckValidCredsRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.bigquerydatatransfer.googleapis.com/DataSource"2\n\x17CheckValidCredsResponse\x12\x17\n\x0fhas_valid_creds\x18\x01 \x01(\x08"\xd1\x01\n\x1bScheduleTransferRunsRequest\x12J\n\x06parent\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2bigquerydatatransfer.googleapis.com/TransferConfig\x123\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02\x121\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02"`\n\x1cScheduleTransferRunsResponse\x12@\n\x04runs\x18\x01 \x03(\x0b22.google.cloud.bigquery.datatransfer.v1.TransferRun"\x8a\x03\n\x1eStartManualTransferRunsRequest\x12J\n\x06parent\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2bigquerydatatransfer.googleapis.com/TransferConfig\x12o\n\x14requested_time_range\x18\x03 \x01(\x0b2O.google.cloud.bigquery.datatransfer.v1.StartManualTransferRunsRequest.TimeRangeH\x00\x128\n\x12requested_run_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x1ai\n\tTimeRange\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x06\n\x04time"c\n\x1fStartManualTransferRunsResponse\x12@\n\x04runs\x18\x01 \x03(\x0b22.google.cloud.bigquery.datatransfer.v1.TransferRun"F\n\x18EnrollDataSourcesRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\x0fdata_source_ids\x18\x02 \x03(\t"H\n\x1aUnenrollDataSourcesRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\x0fdata_source_ids\x18\x02 \x03(\t2\xd5"\n\x13DataTransferService\x12\xe6\x01\n\rGetDataSource\x12;.google.cloud.bigquery.datatransfer.v1.GetDataSourceRequest\x1a1.google.cloud.bigquery.datatransfer.v1.DataSource"e\xdaA\x04name\x82\xd3\xe4\x93\x02X\x12//v1/{name=projects/*/locations/*/dataSources/*}Z%\x12#/v1/{name=projects/*/dataSources/*}\x12\xf9\x01\n\x0fListDataSources\x12=.google.cloud.bigquery.datatransfer.v1.ListDataSourcesRequest\x1a>.google.cloud.bigquery.datatransfer.v1.ListDataSourcesResponse"g\xdaA\x06parent\x82\xd3\xe4\x93\x02X\x12//v1/{parent=projects/*/locations/*}/dataSourcesZ%\x12#/v1/{parent=projects/*}/dataSources\x12\xb6\x02\n\x14CreateTransferConfig\x12B.google.cloud.bigquery.datatransfer.v1.CreateTransferConfigRequest\x1a5.google.cloud.bigquery.datatransfer.v1.TransferConfig"\xa2\x01\xdaA\x16parent,transfer_config\x82\xd3\xe4\x93\x02\x82\x01"3/v1/{parent=projects/*/locations/*}/transferConfigs:\x0ftransfer_configZ:"\'/v1/{parent=projects/*}/transferConfigs:\x0ftransfer_config\x12\xdb\x02\n\x14UpdateTransferConfig\x12B.google.cloud.bigquery.datatransfer.v1.UpdateTransferConfigRequest\x1a5.google.cloud.bigquery.datatransfer.v1.TransferConfig"\xc7\x01\xdaA\x1btransfer_config,update_mask\x82\xd3\xe4\x93\x02\xa2\x012C/v1/{transfer_config.name=projects/*/locations/*/transferConfigs/*}:\x0ftransfer_configZJ27/v1/{transfer_config.name=projects/*/transferConfigs/*}:\x0ftransfer_config\x12\xe1\x01\n\x14DeleteTransferConfig\x12B.google.cloud.bigquery.datatransfer.v1.DeleteTransferConfigRequest\x1a\x16.google.protobuf.Empty"m\xdaA\x04name\x82\xd3\xe4\x93\x02`*3/v1/{name=projects/*/locations/*/transferConfigs/*}Z)*\'/v1/{name=projects/*/transferConfigs/*}\x12\xfa\x01\n\x11GetTransferConfig\x12?.google.cloud.bigquery.datatransfer.v1.GetTransferConfigRequest\x1a5.google.cloud.bigquery.datatransfer.v1.TransferConfig"m\xdaA\x04name\x82\xd3\xe4\x93\x02`\x123/v1/{name=projects/*/locations/*/transferConfigs/*}Z)\x12\'/v1/{name=projects/*/transferConfigs/*}\x12\x8d\x02\n\x13ListTransferConfigs\x12A.google.cloud.bigquery.datatransfer.v1.ListTransferConfigsRequest\x1aB.google.cloud.bigquery.datatransfer.v1.ListTransferConfigsResponse"o\xdaA\x06parent\x82\xd3\xe4\x93\x02`\x123/v1/{parent=projects/*/locations/*}/transferConfigsZ)\x12\'/v1/{parent=projects/*}/transferConfigs\x12\xcd\x02\n\x14ScheduleTransferRuns\x12B.google.cloud.bigquery.datatransfer.v1.ScheduleTransferRunsRequest\x1aC.google.cloud.bigquery.datatransfer.v1.ScheduleTransferRunsResponse"\xab\x01\x88\x02\x01\xdaA\x1aparent,start_time,end_time\x82\xd3\xe4\x93\x02\x84\x01"B/v1/{parent=projects/*/locations/*/transferConfigs/*}:scheduleRuns:\x01*Z;"6/v1/{parent=projects/*/transferConfigs/*}:scheduleRuns:\x01*\x12\xbc\x02\n\x17StartManualTransferRuns\x12E.google.cloud.bigquery.datatransfer.v1.StartManualTransferRunsRequest\x1aF.google.cloud.bigquery.datatransfer.v1.StartManualTransferRunsResponse"\x91\x01\x82\xd3\xe4\x93\x02\x8a\x01"E/v1/{parent=projects/*/locations/*/transferConfigs/*}:startManualRuns:\x01*Z>"9/v1/{parent=projects/*/transferConfigs/*}:startManualRuns:\x01*\x12\xff\x01\n\x0eGetTransferRun\x12<.google.cloud.bigquery.datatransfer.v1.GetTransferRunRequest\x1a2.google.cloud.bigquery.datatransfer.v1.TransferRun"{\xdaA\x04name\x82\xd3\xe4\x93\x02n\x12:/v1/{name=projects/*/locations/*/transferConfigs/*/runs/*}Z0\x12./v1/{name=projects/*/transferConfigs/*/runs/*}\x12\xe9\x01\n\x11DeleteTransferRun\x12?.google.cloud.bigquery.datatransfer.v1.DeleteTransferRunRequest\x1a\x16.google.protobuf.Empty"{\xdaA\x04name\x82\xd3\xe4\x93\x02n*:/v1/{name=projects/*/locations/*/transferConfigs/*/runs/*}Z0*./v1/{name=projects/*/transferConfigs/*/runs/*}\x12\x92\x02\n\x10ListTransferRuns\x12>.google.cloud.bigquery.datatransfer.v1.ListTransferRunsRequest\x1a?.google.cloud.bigquery.datatransfer.v1.ListTransferRunsResponse"}\xdaA\x06parent\x82\xd3\xe4\x93\x02n\x12:/v1/{parent=projects/*/locations/*/transferConfigs/*}/runsZ0\x12./v1/{parent=projects/*/transferConfigs/*}/runs\x12\xb2\x02\n\x10ListTransferLogs\x12>.google.cloud.bigquery.datatransfer.v1.ListTransferLogsRequest\x1a?.google.cloud.bigquery.datatransfer.v1.ListTransferLogsResponse"\x9c\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\x8c\x01\x12I/v1/{parent=projects/*/locations/*/transferConfigs/*/runs/*}/transferLogsZ?\x12=/v1/{parent=projects/*/transferConfigs/*/runs/*}/transferLogs\x12\x9e\x02\n\x0fCheckValidCreds\x12=.google.cloud.bigquery.datatransfer.v1.CheckValidCredsRequest\x1a>.google.cloud.bigquery.datatransfer.v1.CheckValidCredsResponse"\x8b\x01\xdaA\x04name\x82\xd3\xe4\x93\x02~"?/v1/{name=projects/*/locations/*/dataSources/*}:checkValidCreds:\x01*Z8"3/v1/{name=projects/*/dataSources/*}:checkValidCreds:\x01*\x12\xda\x01\n\x11EnrollDataSources\x12?.google.cloud.bigquery.datatransfer.v1.EnrollDataSourcesRequest\x1a\x16.google.protobuf.Empty"l\x82\xd3\xe4\x93\x02f"3/v1/{name=projects/*/locations/*}:enrollDataSources:\x01*Z,"\'/v1/{name=projects/*}:enrollDataSources:\x01*\x12\xb2\x01\n\x13UnenrollDataSources\x12A.google.cloud.bigquery.datatransfer.v1.UnenrollDataSourcesRequest\x1a\x16.google.protobuf.Empty"@\x82\xd3\xe4\x93\x02:"5/v1/{name=projects/*/locations/*}:unenrollDataSources:\x01*\x1aW\xcaA#bigquerydatatransfer.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x8b\x02\n)com.google.cloud.bigquery.datatransfer.v1B\x11DataTransferProtoP\x01ZMcloud.google.com/go/bigquery/datatransfer/apiv1/datatransferpb;datatransferpb\xaa\x02%Google.Cloud.BigQuery.DataTransfer.V1\xca\x02%Google\\Cloud\\BigQuery\\DataTransfer\\V1\xea\x02)Google::Cloud::Bigquery::DataTransfer::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.datatransfer.v1.datatransfer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.bigquery.datatransfer.v1B\x11DataTransferProtoP\x01ZMcloud.google.com/go/bigquery/datatransfer/apiv1/datatransferpb;datatransferpb\xaa\x02%Google.Cloud.BigQuery.DataTransfer.V1\xca\x02%Google\\Cloud\\BigQuery\\DataTransfer\\V1\xea\x02)Google::Cloud::Bigquery::DataTransfer::V1'
    _globals['_DATASOURCE'].fields_by_name['name']._loaded_options = None
    _globals['_DATASOURCE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_DATASOURCE'].fields_by_name['transfer_type']._loaded_options = None
    _globals['_DATASOURCE'].fields_by_name['transfer_type']._serialized_options = b'\x18\x01'
    _globals['_DATASOURCE'].fields_by_name['supports_multiple_transfers']._loaded_options = None
    _globals['_DATASOURCE'].fields_by_name['supports_multiple_transfers']._serialized_options = b'\x18\x01'
    _globals['_DATASOURCE']._loaded_options = None
    _globals['_DATASOURCE']._serialized_options = b'\xeaA\xa1\x01\n.bigquerydatatransfer.googleapis.com/DataSource\x12,projects/{project}/dataSources/{data_source}\x12Aprojects/{project}/locations/{location}/dataSources/{data_source}'
    _globals['_GETDATASOURCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATASOURCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.bigquerydatatransfer.googleapis.com/DataSource'
    _globals['_LISTDATASOURCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATASOURCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\x12.bigquerydatatransfer.googleapis.com/DataSource'
    _globals['_LISTDATASOURCESRESPONSE'].fields_by_name['next_page_token']._loaded_options = None
    _globals['_LISTDATASOURCESRESPONSE'].fields_by_name['next_page_token']._serialized_options = b'\xe0A\x03'
    _globals['_CREATETRANSFERCONFIGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETRANSFERCONFIGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA4\x122bigquerydatatransfer.googleapis.com/TransferConfig'
    _globals['_CREATETRANSFERCONFIGREQUEST'].fields_by_name['transfer_config']._loaded_options = None
    _globals['_CREATETRANSFERCONFIGREQUEST'].fields_by_name['transfer_config']._serialized_options = b'\xe0A\x02'
    _globals['_CREATETRANSFERCONFIGREQUEST'].fields_by_name['authorization_code']._loaded_options = None
    _globals['_CREATETRANSFERCONFIGREQUEST'].fields_by_name['authorization_code']._serialized_options = b'\x18\x01'
    _globals['_UPDATETRANSFERCONFIGREQUEST'].fields_by_name['transfer_config']._loaded_options = None
    _globals['_UPDATETRANSFERCONFIGREQUEST'].fields_by_name['transfer_config']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATETRANSFERCONFIGREQUEST'].fields_by_name['authorization_code']._loaded_options = None
    _globals['_UPDATETRANSFERCONFIGREQUEST'].fields_by_name['authorization_code']._serialized_options = b'\x18\x01'
    _globals['_UPDATETRANSFERCONFIGREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATETRANSFERCONFIGREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_GETTRANSFERCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTRANSFERCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA4\n2bigquerydatatransfer.googleapis.com/TransferConfig'
    _globals['_DELETETRANSFERCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETRANSFERCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA4\n2bigquerydatatransfer.googleapis.com/TransferConfig'
    _globals['_GETTRANSFERRUNREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTRANSFERRUNREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'bigquerydatatransfer.googleapis.com/Run"
    _globals['_DELETETRANSFERRUNREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETRANSFERRUNREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'bigquerydatatransfer.googleapis.com/Run"
    _globals['_LISTTRANSFERCONFIGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTRANSFERCONFIGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA4\x122bigquerydatatransfer.googleapis.com/TransferConfig'
    _globals['_LISTTRANSFERCONFIGSRESPONSE'].fields_by_name['transfer_configs']._loaded_options = None
    _globals['_LISTTRANSFERCONFIGSRESPONSE'].fields_by_name['transfer_configs']._serialized_options = b'\xe0A\x03'
    _globals['_LISTTRANSFERCONFIGSRESPONSE'].fields_by_name['next_page_token']._loaded_options = None
    _globals['_LISTTRANSFERCONFIGSRESPONSE'].fields_by_name['next_page_token']._serialized_options = b'\xe0A\x03'
    _globals['_LISTTRANSFERRUNSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTRANSFERRUNSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\x12'bigquerydatatransfer.googleapis.com/Run"
    _globals['_LISTTRANSFERRUNSRESPONSE'].fields_by_name['transfer_runs']._loaded_options = None
    _globals['_LISTTRANSFERRUNSRESPONSE'].fields_by_name['transfer_runs']._serialized_options = b'\xe0A\x03'
    _globals['_LISTTRANSFERRUNSRESPONSE'].fields_by_name['next_page_token']._loaded_options = None
    _globals['_LISTTRANSFERRUNSRESPONSE'].fields_by_name['next_page_token']._serialized_options = b'\xe0A\x03'
    _globals['_LISTTRANSFERLOGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTRANSFERLOGSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\n'bigquerydatatransfer.googleapis.com/Run"
    _globals['_LISTTRANSFERLOGSRESPONSE'].fields_by_name['transfer_messages']._loaded_options = None
    _globals['_LISTTRANSFERLOGSRESPONSE'].fields_by_name['transfer_messages']._serialized_options = b'\xe0A\x03'
    _globals['_LISTTRANSFERLOGSRESPONSE'].fields_by_name['next_page_token']._loaded_options = None
    _globals['_LISTTRANSFERLOGSRESPONSE'].fields_by_name['next_page_token']._serialized_options = b'\xe0A\x03'
    _globals['_CHECKVALIDCREDSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CHECKVALIDCREDSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.bigquerydatatransfer.googleapis.com/DataSource'
    _globals['_SCHEDULETRANSFERRUNSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_SCHEDULETRANSFERRUNSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA4\n2bigquerydatatransfer.googleapis.com/TransferConfig'
    _globals['_SCHEDULETRANSFERRUNSREQUEST'].fields_by_name['start_time']._loaded_options = None
    _globals['_SCHEDULETRANSFERRUNSREQUEST'].fields_by_name['start_time']._serialized_options = b'\xe0A\x02'
    _globals['_SCHEDULETRANSFERRUNSREQUEST'].fields_by_name['end_time']._loaded_options = None
    _globals['_SCHEDULETRANSFERRUNSREQUEST'].fields_by_name['end_time']._serialized_options = b'\xe0A\x02'
    _globals['_STARTMANUALTRANSFERRUNSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_STARTMANUALTRANSFERRUNSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA4\n2bigquerydatatransfer.googleapis.com/TransferConfig'
    _globals['_ENROLLDATASOURCESREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ENROLLDATASOURCESREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_UNENROLLDATASOURCESREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UNENROLLDATASOURCESREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_DATATRANSFERSERVICE']._loaded_options = None
    _globals['_DATATRANSFERSERVICE']._serialized_options = b'\xcaA#bigquerydatatransfer.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DATATRANSFERSERVICE'].methods_by_name['GetDataSource']._loaded_options = None
    _globals['_DATATRANSFERSERVICE'].methods_by_name['GetDataSource']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02X\x12//v1/{name=projects/*/locations/*/dataSources/*}Z%\x12#/v1/{name=projects/*/dataSources/*}'
    _globals['_DATATRANSFERSERVICE'].methods_by_name['ListDataSources']._loaded_options = None
    _globals['_DATATRANSFERSERVICE'].methods_by_name['ListDataSources']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02X\x12//v1/{parent=projects/*/locations/*}/dataSourcesZ%\x12#/v1/{parent=projects/*}/dataSources'
    _globals['_DATATRANSFERSERVICE'].methods_by_name['CreateTransferConfig']._loaded_options = None
    _globals['_DATATRANSFERSERVICE'].methods_by_name['CreateTransferConfig']._serialized_options = b'\xdaA\x16parent,transfer_config\x82\xd3\xe4\x93\x02\x82\x01"3/v1/{parent=projects/*/locations/*}/transferConfigs:\x0ftransfer_configZ:"\'/v1/{parent=projects/*}/transferConfigs:\x0ftransfer_config'
    _globals['_DATATRANSFERSERVICE'].methods_by_name['UpdateTransferConfig']._loaded_options = None
    _globals['_DATATRANSFERSERVICE'].methods_by_name['UpdateTransferConfig']._serialized_options = b'\xdaA\x1btransfer_config,update_mask\x82\xd3\xe4\x93\x02\xa2\x012C/v1/{transfer_config.name=projects/*/locations/*/transferConfigs/*}:\x0ftransfer_configZJ27/v1/{transfer_config.name=projects/*/transferConfigs/*}:\x0ftransfer_config'
    _globals['_DATATRANSFERSERVICE'].methods_by_name['DeleteTransferConfig']._loaded_options = None
    _globals['_DATATRANSFERSERVICE'].methods_by_name['DeleteTransferConfig']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02`*3/v1/{name=projects/*/locations/*/transferConfigs/*}Z)*'/v1/{name=projects/*/transferConfigs/*}"
    _globals['_DATATRANSFERSERVICE'].methods_by_name['GetTransferConfig']._loaded_options = None
    _globals['_DATATRANSFERSERVICE'].methods_by_name['GetTransferConfig']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02`\x123/v1/{name=projects/*/locations/*/transferConfigs/*}Z)\x12'/v1/{name=projects/*/transferConfigs/*}"
    _globals['_DATATRANSFERSERVICE'].methods_by_name['ListTransferConfigs']._loaded_options = None
    _globals['_DATATRANSFERSERVICE'].methods_by_name['ListTransferConfigs']._serialized_options = b"\xdaA\x06parent\x82\xd3\xe4\x93\x02`\x123/v1/{parent=projects/*/locations/*}/transferConfigsZ)\x12'/v1/{parent=projects/*}/transferConfigs"
    _globals['_DATATRANSFERSERVICE'].methods_by_name['ScheduleTransferRuns']._loaded_options = None
    _globals['_DATATRANSFERSERVICE'].methods_by_name['ScheduleTransferRuns']._serialized_options = b'\x88\x02\x01\xdaA\x1aparent,start_time,end_time\x82\xd3\xe4\x93\x02\x84\x01"B/v1/{parent=projects/*/locations/*/transferConfigs/*}:scheduleRuns:\x01*Z;"6/v1/{parent=projects/*/transferConfigs/*}:scheduleRuns:\x01*'
    _globals['_DATATRANSFERSERVICE'].methods_by_name['StartManualTransferRuns']._loaded_options = None
    _globals['_DATATRANSFERSERVICE'].methods_by_name['StartManualTransferRuns']._serialized_options = b'\x82\xd3\xe4\x93\x02\x8a\x01"E/v1/{parent=projects/*/locations/*/transferConfigs/*}:startManualRuns:\x01*Z>"9/v1/{parent=projects/*/transferConfigs/*}:startManualRuns:\x01*'
    _globals['_DATATRANSFERSERVICE'].methods_by_name['GetTransferRun']._loaded_options = None
    _globals['_DATATRANSFERSERVICE'].methods_by_name['GetTransferRun']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02n\x12:/v1/{name=projects/*/locations/*/transferConfigs/*/runs/*}Z0\x12./v1/{name=projects/*/transferConfigs/*/runs/*}'
    _globals['_DATATRANSFERSERVICE'].methods_by_name['DeleteTransferRun']._loaded_options = None
    _globals['_DATATRANSFERSERVICE'].methods_by_name['DeleteTransferRun']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02n*:/v1/{name=projects/*/locations/*/transferConfigs/*/runs/*}Z0*./v1/{name=projects/*/transferConfigs/*/runs/*}'
    _globals['_DATATRANSFERSERVICE'].methods_by_name['ListTransferRuns']._loaded_options = None
    _globals['_DATATRANSFERSERVICE'].methods_by_name['ListTransferRuns']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02n\x12:/v1/{parent=projects/*/locations/*/transferConfigs/*}/runsZ0\x12./v1/{parent=projects/*/transferConfigs/*}/runs'
    _globals['_DATATRANSFERSERVICE'].methods_by_name['ListTransferLogs']._loaded_options = None
    _globals['_DATATRANSFERSERVICE'].methods_by_name['ListTransferLogs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x8c\x01\x12I/v1/{parent=projects/*/locations/*/transferConfigs/*/runs/*}/transferLogsZ?\x12=/v1/{parent=projects/*/transferConfigs/*/runs/*}/transferLogs'
    _globals['_DATATRANSFERSERVICE'].methods_by_name['CheckValidCreds']._loaded_options = None
    _globals['_DATATRANSFERSERVICE'].methods_by_name['CheckValidCreds']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02~"?/v1/{name=projects/*/locations/*/dataSources/*}:checkValidCreds:\x01*Z8"3/v1/{name=projects/*/dataSources/*}:checkValidCreds:\x01*'
    _globals['_DATATRANSFERSERVICE'].methods_by_name['EnrollDataSources']._loaded_options = None
    _globals['_DATATRANSFERSERVICE'].methods_by_name['EnrollDataSources']._serialized_options = b'\x82\xd3\xe4\x93\x02f"3/v1/{name=projects/*/locations/*}:enrollDataSources:\x01*Z,"\'/v1/{name=projects/*}:enrollDataSources:\x01*'
    _globals['_DATATRANSFERSERVICE'].methods_by_name['UnenrollDataSources']._loaded_options = None
    _globals['_DATATRANSFERSERVICE'].methods_by_name['UnenrollDataSources']._serialized_options = b'\x82\xd3\xe4\x93\x02:"5/v1/{name=projects/*/locations/*}:unenrollDataSources:\x01*'
    _globals['_DATASOURCEPARAMETER']._serialized_start = 429
    _globals['_DATASOURCEPARAMETER']._serialized_end = 1084
    _globals['_DATASOURCEPARAMETER_TYPE']._serialized_start = 969
    _globals['_DATASOURCEPARAMETER_TYPE']._serialized_end = 1084
    _globals['_DATASOURCE']._serialized_start = 1087
    _globals['_DATASOURCE']._serialized_end = 2267
    _globals['_DATASOURCE_AUTHORIZATIONTYPE']._serialized_start = 1860
    _globals['_DATASOURCE_AUTHORIZATIONTYPE']._serialized_end = 1998
    _globals['_DATASOURCE_DATAREFRESHTYPE']._serialized_start = 2000
    _globals['_DATASOURCE_DATAREFRESHTYPE']._serialized_end = 2099
    _globals['_GETDATASOURCEREQUEST']._serialized_start = 2269
    _globals['_GETDATASOURCEREQUEST']._serialized_end = 2361
    _globals['_LISTDATASOURCESREQUEST']._serialized_start = 2364
    _globals['_LISTDATASOURCESREQUEST']._serialized_end = 2499
    _globals['_LISTDATASOURCESRESPONSE']._serialized_start = 2502
    _globals['_LISTDATASOURCESRESPONSE']._serialized_end = 2630
    _globals['_CREATETRANSFERCONFIGREQUEST']._serialized_start = 2633
    _globals['_CREATETRANSFERCONFIGREQUEST']._serialized_end = 2907
    _globals['_UPDATETRANSFERCONFIGREQUEST']._serialized_start = 2910
    _globals['_UPDATETRANSFERCONFIGREQUEST']._serialized_end = 3162
    _globals['_GETTRANSFERCONFIGREQUEST']._serialized_start = 3164
    _globals['_GETTRANSFERCONFIGREQUEST']._serialized_end = 3264
    _globals['_DELETETRANSFERCONFIGREQUEST']._serialized_start = 3266
    _globals['_DELETETRANSFERCONFIGREQUEST']._serialized_end = 3369
    _globals['_GETTRANSFERRUNREQUEST']._serialized_start = 3371
    _globals['_GETTRANSFERRUNREQUEST']._serialized_end = 3457
    _globals['_DELETETRANSFERRUNREQUEST']._serialized_start = 3459
    _globals['_DELETETRANSFERRUNREQUEST']._serialized_end = 3548
    _globals['_LISTTRANSFERCONFIGSREQUEST']._serialized_start = 3551
    _globals['_LISTTRANSFERCONFIGSREQUEST']._serialized_end = 3719
    _globals['_LISTTRANSFERCONFIGSRESPONSE']._serialized_start = 3722
    _globals['_LISTTRANSFERCONFIGSRESPONSE']._serialized_end = 3867
    _globals['_LISTTRANSFERRUNSREQUEST']._serialized_start = 3870
    _globals['_LISTTRANSFERRUNSREQUEST']._serialized_end = 4220
    _globals['_LISTTRANSFERRUNSREQUEST_RUNATTEMPT']._serialized_start = 4167
    _globals['_LISTTRANSFERRUNSREQUEST_RUNATTEMPT']._serialized_end = 4220
    _globals['_LISTTRANSFERRUNSRESPONSE']._serialized_start = 4223
    _globals['_LISTTRANSFERRUNSRESPONSE']._serialized_end = 4359
    _globals['_LISTTRANSFERLOGSREQUEST']._serialized_start = 4362
    _globals['_LISTTRANSFERLOGSREQUEST']._serialized_end = 4586
    _globals['_LISTTRANSFERLOGSRESPONSE']._serialized_start = 4589
    _globals['_LISTTRANSFERLOGSRESPONSE']._serialized_end = 4733
    _globals['_CHECKVALIDCREDSREQUEST']._serialized_start = 4735
    _globals['_CHECKVALIDCREDSREQUEST']._serialized_end = 4829
    _globals['_CHECKVALIDCREDSRESPONSE']._serialized_start = 4831
    _globals['_CHECKVALIDCREDSRESPONSE']._serialized_end = 4881
    _globals['_SCHEDULETRANSFERRUNSREQUEST']._serialized_start = 4884
    _globals['_SCHEDULETRANSFERRUNSREQUEST']._serialized_end = 5093
    _globals['_SCHEDULETRANSFERRUNSRESPONSE']._serialized_start = 5095
    _globals['_SCHEDULETRANSFERRUNSRESPONSE']._serialized_end = 5191
    _globals['_STARTMANUALTRANSFERRUNSREQUEST']._serialized_start = 5194
    _globals['_STARTMANUALTRANSFERRUNSREQUEST']._serialized_end = 5588
    _globals['_STARTMANUALTRANSFERRUNSREQUEST_TIMERANGE']._serialized_start = 5475
    _globals['_STARTMANUALTRANSFERRUNSREQUEST_TIMERANGE']._serialized_end = 5580
    _globals['_STARTMANUALTRANSFERRUNSRESPONSE']._serialized_start = 5590
    _globals['_STARTMANUALTRANSFERRUNSRESPONSE']._serialized_end = 5689
    _globals['_ENROLLDATASOURCESREQUEST']._serialized_start = 5691
    _globals['_ENROLLDATASOURCESREQUEST']._serialized_end = 5761
    _globals['_UNENROLLDATASOURCESREQUEST']._serialized_start = 5763
    _globals['_UNENROLLDATASOURCESREQUEST']._serialized_end = 5835
    _globals['_DATATRANSFERSERVICE']._serialized_start = 5838
    _globals['_DATATRANSFERSERVICE']._serialized_end = 10275