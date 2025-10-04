"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/bigquery/datatransfer/v1/transfer.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/bigquery/datatransfer/v1/transfer.proto\x12%google.cloud.bigquery.datatransfer.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto"0\n\x10EmailPreferences\x12\x1c\n\x14enable_failure_email\x18\x01 \x01(\x08"\x90\x01\n\x0fScheduleOptions\x12\x1f\n\x17disable_auto_scheduling\x18\x03 \x01(\x08\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xa7\x02\n\x11ScheduleOptionsV2\x12W\n\x13time_based_schedule\x18\x01 \x01(\x0b28.google.cloud.bigquery.datatransfer.v1.TimeBasedScheduleH\x00\x12P\n\x0fmanual_schedule\x18\x02 \x01(\x0b25.google.cloud.bigquery.datatransfer.v1.ManualScheduleH\x00\x12[\n\x15event_driven_schedule\x18\x03 \x01(\x0b2:.google.cloud.bigquery.datatransfer.v1.EventDrivenScheduleH\x00B\n\n\x08schedule"\x83\x01\n\x11TimeBasedSchedule\x12\x10\n\x08schedule\x18\x01 \x01(\t\x12.\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x10\n\x0eManualSchedule"2\n\x13EventDrivenSchedule\x12\x1b\n\x13pubsub_subscription\x18\x01 \x01(\t"(\n\x08UserInfo\x12\x12\n\x05email\x18\x01 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_email"\x9b\t\n\x0eTransferConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12 \n\x16destination_dataset_id\x18\x02 \x01(\tH\x00\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12\x16\n\x0edata_source_id\x18\x05 \x01(\t\x12\'\n\x06params\x18\t \x01(\x0b2\x17.google.protobuf.Struct\x12\x10\n\x08schedule\x18\x07 \x01(\t\x12P\n\x10schedule_options\x18\x18 \x01(\x0b26.google.cloud.bigquery.datatransfer.v1.ScheduleOptions\x12U\n\x13schedule_options_v2\x18\x1f \x01(\x0b28.google.cloud.bigquery.datatransfer.v1.ScheduleOptionsV2\x12 \n\x18data_refresh_window_days\x18\x0c \x01(\x05\x12\x10\n\x08disabled\x18\r \x01(\x08\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x126\n\rnext_run_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12H\n\x05state\x18\n \x01(\x0e24.google.cloud.bigquery.datatransfer.v1.TransferStateB\x03\xe0A\x03\x12\x0f\n\x07user_id\x18\x0b \x01(\x03\x12\x1b\n\x0edataset_region\x18\x0e \x01(\tB\x03\xe0A\x03\x12!\n\x19notification_pubsub_topic\x18\x0f \x01(\t\x12R\n\x11email_preferences\x18\x12 \x01(\x0b27.google.cloud.bigquery.datatransfer.v1.EmailPreferences\x12M\n\nowner_info\x18\x1b \x01(\x0b2/.google.cloud.bigquery.datatransfer.v1.UserInfoB\x03\xe0A\x03H\x01\x88\x01\x01\x12`\n\x18encryption_configuration\x18\x1c \x01(\x0b2>.google.cloud.bigquery.datatransfer.v1.EncryptionConfiguration\x12&\n\x05error\x18  \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03:\xb9\x01\xeaA\xb5\x01\n2bigquerydatatransfer.googleapis.com/TransferConfig\x124projects/{project}/transferConfigs/{transfer_config}\x12Iprojects/{project}/locations/{location}/transferConfigs/{transfer_config}B\r\n\x0bdestinationB\r\n\x0b_owner_info"M\n\x17EncryptionConfiguration\x122\n\x0ckms_key_name\x18\x01 \x01(\x0b2\x1c.google.protobuf.StringValue"\xff\x06\n\x0bTransferRun\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x121\n\rschedule_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08run_time\x18\n \x01(\x0b2\x1a.google.protobuf.Timestamp\x12(\n\x0cerror_status\x18\x15 \x01(\x0b2\x12.google.rpc.Status\x123\n\nstart_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12,\n\x06params\x18\t \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x03\x12%\n\x16destination_dataset_id\x18\x02 \x01(\tB\x03\xe0A\x03H\x00\x12\x1b\n\x0edata_source_id\x18\x07 \x01(\tB\x03\xe0A\x03\x12C\n\x05state\x18\x08 \x01(\x0e24.google.cloud.bigquery.datatransfer.v1.TransferState\x12\x0f\n\x07user_id\x18\x0b \x01(\x03\x12\x15\n\x08schedule\x18\x0c \x01(\tB\x03\xe0A\x03\x12&\n\x19notification_pubsub_topic\x18\x17 \x01(\tB\x03\xe0A\x03\x12W\n\x11email_preferences\x18\x19 \x01(\x0b27.google.cloud.bigquery.datatransfer.v1.EmailPreferencesB\x03\xe0A\x03:\xc4\x01\xeaA\xc0\x01\n\'bigquerydatatransfer.googleapis.com/Run\x12?projects/{project}/transferConfigs/{transfer_config}/runs/{run}\x12Tprojects/{project}/locations/{location}/transferConfigs/{transfer_config}/runs/{run}B\r\n\x0bdestination"\x8a\x02\n\x0fTransferMessage\x120\n\x0cmessage_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12X\n\x08severity\x18\x02 \x01(\x0e2F.google.cloud.bigquery.datatransfer.v1.TransferMessage.MessageSeverity\x12\x14\n\x0cmessage_text\x18\x03 \x01(\t"U\n\x0fMessageSeverity\x12 \n\x1cMESSAGE_SEVERITY_UNSPECIFIED\x10\x00\x12\x08\n\x04INFO\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05ERROR\x10\x03*K\n\x0cTransferType\x12\x1d\n\x19TRANSFER_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05BATCH\x10\x01\x12\r\n\tSTREAMING\x10\x02\x1a\x02\x18\x01*s\n\rTransferState\x12\x1e\n\x1aTRANSFER_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\r\n\tSUCCEEDED\x10\x04\x12\n\n\x06FAILED\x10\x05\x12\r\n\tCANCELLED\x10\x06B\x8f\x02\n)com.google.cloud.bigquery.datatransfer.v1B\rTransferProtoP\x01ZMcloud.google.com/go/bigquery/datatransfer/apiv1/datatransferpb;datatransferpb\xa2\x02\x05GCBDT\xaa\x02%Google.Cloud.BigQuery.DataTransfer.V1\xca\x02%Google\\Cloud\\BigQuery\\DataTransfer\\V1\xea\x02)Google::Cloud::Bigquery::DataTransfer::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.datatransfer.v1.transfer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.bigquery.datatransfer.v1B\rTransferProtoP\x01ZMcloud.google.com/go/bigquery/datatransfer/apiv1/datatransferpb;datatransferpb\xa2\x02\x05GCBDT\xaa\x02%Google.Cloud.BigQuery.DataTransfer.V1\xca\x02%Google\\Cloud\\BigQuery\\DataTransfer\\V1\xea\x02)Google::Cloud::Bigquery::DataTransfer::V1'
    _globals['_TRANSFERTYPE']._loaded_options = None
    _globals['_TRANSFERTYPE']._serialized_options = b'\x18\x01'
    _globals['_TRANSFERCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_TRANSFERCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_TRANSFERCONFIG'].fields_by_name['update_time']._loaded_options = None
    _globals['_TRANSFERCONFIG'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFERCONFIG'].fields_by_name['next_run_time']._loaded_options = None
    _globals['_TRANSFERCONFIG'].fields_by_name['next_run_time']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFERCONFIG'].fields_by_name['state']._loaded_options = None
    _globals['_TRANSFERCONFIG'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFERCONFIG'].fields_by_name['dataset_region']._loaded_options = None
    _globals['_TRANSFERCONFIG'].fields_by_name['dataset_region']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFERCONFIG'].fields_by_name['owner_info']._loaded_options = None
    _globals['_TRANSFERCONFIG'].fields_by_name['owner_info']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFERCONFIG'].fields_by_name['error']._loaded_options = None
    _globals['_TRANSFERCONFIG'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFERCONFIG']._loaded_options = None
    _globals['_TRANSFERCONFIG']._serialized_options = b'\xeaA\xb5\x01\n2bigquerydatatransfer.googleapis.com/TransferConfig\x124projects/{project}/transferConfigs/{transfer_config}\x12Iprojects/{project}/locations/{location}/transferConfigs/{transfer_config}'
    _globals['_TRANSFERRUN'].fields_by_name['name']._loaded_options = None
    _globals['_TRANSFERRUN'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_TRANSFERRUN'].fields_by_name['start_time']._loaded_options = None
    _globals['_TRANSFERRUN'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFERRUN'].fields_by_name['end_time']._loaded_options = None
    _globals['_TRANSFERRUN'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFERRUN'].fields_by_name['update_time']._loaded_options = None
    _globals['_TRANSFERRUN'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFERRUN'].fields_by_name['params']._loaded_options = None
    _globals['_TRANSFERRUN'].fields_by_name['params']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFERRUN'].fields_by_name['destination_dataset_id']._loaded_options = None
    _globals['_TRANSFERRUN'].fields_by_name['destination_dataset_id']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFERRUN'].fields_by_name['data_source_id']._loaded_options = None
    _globals['_TRANSFERRUN'].fields_by_name['data_source_id']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFERRUN'].fields_by_name['schedule']._loaded_options = None
    _globals['_TRANSFERRUN'].fields_by_name['schedule']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFERRUN'].fields_by_name['notification_pubsub_topic']._loaded_options = None
    _globals['_TRANSFERRUN'].fields_by_name['notification_pubsub_topic']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFERRUN'].fields_by_name['email_preferences']._loaded_options = None
    _globals['_TRANSFERRUN'].fields_by_name['email_preferences']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFERRUN']._loaded_options = None
    _globals['_TRANSFERRUN']._serialized_options = b"\xeaA\xc0\x01\n'bigquerydatatransfer.googleapis.com/Run\x12?projects/{project}/transferConfigs/{transfer_config}/runs/{run}\x12Tprojects/{project}/locations/{location}/transferConfigs/{transfer_config}/runs/{run}"
    _globals['_TRANSFERTYPE']._serialized_start = 3444
    _globals['_TRANSFERTYPE']._serialized_end = 3519
    _globals['_TRANSFERSTATE']._serialized_start = 3521
    _globals['_TRANSFERSTATE']._serialized_end = 3636
    _globals['_EMAILPREFERENCES']._serialized_start = 275
    _globals['_EMAILPREFERENCES']._serialized_end = 323
    _globals['_SCHEDULEOPTIONS']._serialized_start = 326
    _globals['_SCHEDULEOPTIONS']._serialized_end = 470
    _globals['_SCHEDULEOPTIONSV2']._serialized_start = 473
    _globals['_SCHEDULEOPTIONSV2']._serialized_end = 768
    _globals['_TIMEBASEDSCHEDULE']._serialized_start = 771
    _globals['_TIMEBASEDSCHEDULE']._serialized_end = 902
    _globals['_MANUALSCHEDULE']._serialized_start = 904
    _globals['_MANUALSCHEDULE']._serialized_end = 920
    _globals['_EVENTDRIVENSCHEDULE']._serialized_start = 922
    _globals['_EVENTDRIVENSCHEDULE']._serialized_end = 972
    _globals['_USERINFO']._serialized_start = 974
    _globals['_USERINFO']._serialized_end = 1014
    _globals['_TRANSFERCONFIG']._serialized_start = 1017
    _globals['_TRANSFERCONFIG']._serialized_end = 2196
    _globals['_ENCRYPTIONCONFIGURATION']._serialized_start = 2198
    _globals['_ENCRYPTIONCONFIGURATION']._serialized_end = 2275
    _globals['_TRANSFERRUN']._serialized_start = 2278
    _globals['_TRANSFERRUN']._serialized_end = 3173
    _globals['_TRANSFERMESSAGE']._serialized_start = 3176
    _globals['_TRANSFERMESSAGE']._serialized_end = 3442
    _globals['_TRANSFERMESSAGE_MESSAGESEVERITY']._serialized_start = 3357
    _globals['_TRANSFERMESSAGE_MESSAGESEVERITY']._serialized_end = 3442