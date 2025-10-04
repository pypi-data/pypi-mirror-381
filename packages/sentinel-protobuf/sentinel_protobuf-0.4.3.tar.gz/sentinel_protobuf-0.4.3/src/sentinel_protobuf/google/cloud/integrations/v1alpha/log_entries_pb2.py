"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/integrations/v1alpha/log_entries.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.integrations.v1alpha import cloud_logging_details_pb2 as google_dot_cloud_dot_integrations_dot_v1alpha_dot_cloud__logging__details__pb2
from .....google.cloud.integrations.v1alpha import event_parameter_pb2 as google_dot_cloud_dot_integrations_dot_v1alpha_dot_event__parameter__pb2
from .....google.cloud.integrations.v1alpha import integration_state_pb2 as google_dot_cloud_dot_integrations_dot_v1alpha_dot_integration__state__pb2
from .....google.cloud.integrations.v1alpha import task_config_pb2 as google_dot_cloud_dot_integrations_dot_v1alpha_dot_task__config__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/integrations/v1alpha/log_entries.proto\x12!google.cloud.integrations.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a=google/cloud/integrations/v1alpha/cloud_logging_details.proto\x1a7google/cloud/integrations/v1alpha/event_parameter.proto\x1a9google/cloud/integrations/v1alpha/integration_state.proto\x1a3google/cloud/integrations/v1alpha/task_config.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x95\r\n\rExecutionInfo\x12\x13\n\x0bintegration\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x04 \x01(\t\x12\x12\n\ntrigger_id\x18\x05 \x01(\t\x12[\n\x0erequest_params\x18\x06 \x03(\x0b2C.google.cloud.integrations.v1alpha.ExecutionInfo.RequestParamsEntry\x12]\n\x0fresponse_params\x18\x07 \x03(\x0b2D.google.cloud.integrations.v1alpha.ExecutionInfo.ResponseParamsEntry\x12>\n\x06errors\x18\n \x03(\x0b2..google.cloud.integrations.v1alpha.ErrorDetail\x12C\n\x0ctask_configs\x18\r \x03(\x0b2-.google.cloud.integrations.v1alpha.TaskConfig\x12"\n\x1aintegration_version_number\x18\x0e \x01(\t\x12\x14\n\x0cexecution_id\x18\x0f \x01(\t\x12[\n\x19integration_version_state\x18\x10 \x01(\x0e23.google.cloud.integrations.v1alpha.IntegrationStateB\x03\xe0A\x03\x12#\n\x1benable_database_persistence\x18\x11 \x01(\x08\x12U\n\x15cloud_logging_details\x18\x12 \x01(\x0b26.google.cloud.integrations.v1alpha.CloudLoggingDetails\x12e\n\x1dintegration_execution_details\x18\x13 \x01(\x0b2>.google.cloud.integrations.v1alpha.IntegrationExecutionDetails\x12H\n\x0eexecution_type\x18\x14 \x01(\x0e20.google.cloud.integrations.v1alpha.ExecutionType\x12Z\n\x10execution_method\x18\x15 \x01(\x0e2@.google.cloud.integrations.v1alpha.ExecutionInfo.ExecutionMethod\x12#\n\x1bintegration_snapshot_number\x18\x16 \x01(\x03\x12P\n\x0breplay_info\x18\x17 \x01(\x0b2;.google.cloud.integrations.v1alpha.ExecutionInfo.ReplayInfo\x1a\xbb\x02\n\nReplayInfo\x12"\n\x1aoriginal_execution_info_id\x18\x01 \x01(\t\x12#\n\x1breplayed_execution_info_ids\x18\x02 \x03(\t\x12\x15\n\rreplay_reason\x18\x03 \x01(\t\x12`\n\x0breplay_mode\x18\x04 \x01(\x0e2F.google.cloud.integrations.v1alpha.ExecutionInfo.ReplayInfo.ReplayModeB\x03\xe0A\x01"k\n\nReplayMode\x12\x1b\n\x17REPLAY_MODE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aREPLAY_MODE_FROM_BEGINNING\x10\x01\x12 \n\x1cREPLAY_MODE_POINT_OF_FAILURE\x10\x02\x1ag\n\x12RequestParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12@\n\x05value\x18\x02 \x01(\x0b21.google.cloud.integrations.v1alpha.EventParameter:\x028\x01\x1ah\n\x13ResponseParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12@\n\x05value\x18\x02 \x01(\x0b21.google.cloud.integrations.v1alpha.EventParameter:\x028\x01"^\n\x0fExecutionMethod\x12 \n\x1cEXECUTION_METHOD_UNSPECIFIED\x10\x00\x12\x08\n\x04POST\x10\x01\x12\x0c\n\x08SCHEDULE\x10\x02\x12\x11\n\rPOST_TO_QUEUE\x10\x03"\x82\x05\n\x1bIntegrationExecutionDetails\x12\x82\x01\n\x1bintegration_execution_state\x18\x01 \x01(\x0e2X.google.cloud.integrations.v1alpha.IntegrationExecutionDetails.IntegrationExecutionStateB\x03\xe0A\x03\x12g\n\x1eintegration_execution_snapshot\x18\x02 \x03(\x0b2?.google.cloud.integrations.v1alpha.IntegrationExecutionSnapshot\x12P\n\x17execution_attempt_stats\x18\x03 \x03(\x0b2/.google.cloud.integrations.v1alpha.AttemptStats\x127\n\x13next_execution_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x1f\n\x17execution_retries_count\x18\x05 \x01(\x05\x12\x15\n\rcancel_reason\x18\x06 \x01(\t"\xb1\x01\n\x19IntegrationExecutionState\x12+\n\'INTEGRATION_EXECUTION_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ON_HOLD\x10\x01\x12\x0e\n\nIN_PROCESS\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\r\n\tCANCELLED\x10\x05\x12\x11\n\rRETRY_ON_HOLD\x10\x06\x12\r\n\tSUSPENDED\x10\x07"\x89\x07\n\x1cIntegrationExecutionSnapshot\x12\x1e\n\x16checkpoint_task_number\x18\x01 \x01(\t\x121\n\rsnapshot_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x95\x01\n\'integration_execution_snapshot_metadata\x18\x03 \x01(\x0b2d.google.cloud.integrations.v1alpha.IntegrationExecutionSnapshot.IntegrationExecutionSnapshotMetadata\x12W\n\x16task_execution_details\x18\x04 \x03(\x0b27.google.cloud.integrations.v1alpha.TaskExecutionDetails\x12M\n\x11condition_results\x18\x05 \x03(\x0b22.google.cloud.integrations.v1alpha.ConditionResult\x12n\n\x10execution_params\x18\x06 \x03(\x0b2T.google.cloud.integrations.v1alpha.IntegrationExecutionSnapshot.ExecutionParamsEntry\x1a\xfa\x01\n$IntegrationExecutionSnapshotMetadata\x12\x13\n\x0btask_number\x18\x01 \x01(\t\x12\x0c\n\x04task\x18\x02 \x01(\t\x12)\n!integration_execution_attempt_num\x18\x03 \x01(\x05\x12\x18\n\x10task_attempt_num\x18\x04 \x01(\x05\x12\x12\n\ntask_label\x18\x05 \x01(\t\x12\x1d\n\x15ancestor_task_numbers\x18\x06 \x03(\t\x12"\n\x1aancestor_iteration_numbers\x18\x07 \x03(\t\x12\x13\n\x0bintegration\x18\x08 \x01(\t\x1ai\n\x14ExecutionParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12@\n\x05value\x18\x02 \x01(\x0b21.google.cloud.integrations.v1alpha.EventParameter:\x028\x01"\xe7\x03\n\x14TaskExecutionDetails\x12\x13\n\x0btask_number\x18\x01 \x01(\t\x12h\n\x14task_execution_state\x18\x02 \x01(\x0e2J.google.cloud.integrations.v1alpha.TaskExecutionDetails.TaskExecutionState\x12K\n\x12task_attempt_stats\x18\x03 \x03(\x0b2/.google.cloud.integrations.v1alpha.AttemptStats"\x82\x02\n\x12TaskExecutionState\x12$\n TASK_EXECUTION_STATE_UNSPECIFIED\x10\x00\x12\x15\n\x11PENDING_EXECUTION\x10\x01\x12\x0e\n\nIN_PROCESS\x10\x02\x12\x0b\n\x07SUCCEED\x10\x03\x12\n\n\x06FAILED\x10\x04\x12\t\n\x05FATAL\x10\x05\x12\x11\n\rRETRY_ON_HOLD\x10\x06\x12\x0b\n\x07SKIPPED\x10\x07\x12\r\n\tCANCELLED\x10\x08\x12\x14\n\x10PENDING_ROLLBACK\x10\t\x12\x17\n\x13ROLLBACK_IN_PROCESS\x10\n\x12\x0e\n\nROLLEDBACK\x10\x0b\x12\r\n\tSUSPENDED\x10\x0c"l\n\x0cAttemptStats\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"9\n\x0bErrorDetail\x12\x15\n\rerror_message\x18\x01 \x01(\t\x12\x13\n\x0btask_number\x18\x02 \x01(\x05"X\n\x0fConditionResult\x12\x1b\n\x13current_task_number\x18\x01 \x01(\t\x12\x18\n\x10next_task_number\x18\x02 \x01(\t\x12\x0e\n\x06result\x18\x03 \x01(\x08*W\n\rExecutionType\x12\x1e\n\x1aEXECUTION_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13INTEGRATION_VERSION\x10\x01\x12\r\n\tTEST_CASE\x10\x02B\xa9\x01\n%com.google.cloud.integrations.v1alphaB\x0fLogEntriesProtoP\x01ZIcloud.google.com/go/integrations/apiv1alpha/integrationspb;integrationspb\xaa\x02!Google.Cloud.Integrations.V1Alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.integrations.v1alpha.log_entries_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.integrations.v1alphaB\x0fLogEntriesProtoP\x01ZIcloud.google.com/go/integrations/apiv1alpha/integrationspb;integrationspb\xaa\x02!Google.Cloud.Integrations.V1Alpha'
    _globals['_EXECUTIONINFO_REPLAYINFO'].fields_by_name['replay_mode']._loaded_options = None
    _globals['_EXECUTIONINFO_REPLAYINFO'].fields_by_name['replay_mode']._serialized_options = b'\xe0A\x01'
    _globals['_EXECUTIONINFO_REQUESTPARAMSENTRY']._loaded_options = None
    _globals['_EXECUTIONINFO_REQUESTPARAMSENTRY']._serialized_options = b'8\x01'
    _globals['_EXECUTIONINFO_RESPONSEPARAMSENTRY']._loaded_options = None
    _globals['_EXECUTIONINFO_RESPONSEPARAMSENTRY']._serialized_options = b'8\x01'
    _globals['_EXECUTIONINFO'].fields_by_name['integration_version_state']._loaded_options = None
    _globals['_EXECUTIONINFO'].fields_by_name['integration_version_state']._serialized_options = b'\xe0A\x03'
    _globals['_INTEGRATIONEXECUTIONDETAILS'].fields_by_name['integration_execution_state']._loaded_options = None
    _globals['_INTEGRATIONEXECUTIONDETAILS'].fields_by_name['integration_execution_state']._serialized_options = b'\xe0A\x03'
    _globals['_INTEGRATIONEXECUTIONSNAPSHOT_EXECUTIONPARAMSENTRY']._loaded_options = None
    _globals['_INTEGRATIONEXECUTIONSNAPSHOT_EXECUTIONPARAMSENTRY']._serialized_options = b'8\x01'
    _globals['_EXECUTIONTYPE']._serialized_start = 4378
    _globals['_EXECUTIONTYPE']._serialized_end = 4465
    _globals['_EXECUTIONINFO']._serialized_start = 389
    _globals['_EXECUTIONINFO']._serialized_end = 2074
    _globals['_EXECUTIONINFO_REPLAYINFO']._serialized_start = 1452
    _globals['_EXECUTIONINFO_REPLAYINFO']._serialized_end = 1767
    _globals['_EXECUTIONINFO_REPLAYINFO_REPLAYMODE']._serialized_start = 1660
    _globals['_EXECUTIONINFO_REPLAYINFO_REPLAYMODE']._serialized_end = 1767
    _globals['_EXECUTIONINFO_REQUESTPARAMSENTRY']._serialized_start = 1769
    _globals['_EXECUTIONINFO_REQUESTPARAMSENTRY']._serialized_end = 1872
    _globals['_EXECUTIONINFO_RESPONSEPARAMSENTRY']._serialized_start = 1874
    _globals['_EXECUTIONINFO_RESPONSEPARAMSENTRY']._serialized_end = 1978
    _globals['_EXECUTIONINFO_EXECUTIONMETHOD']._serialized_start = 1980
    _globals['_EXECUTIONINFO_EXECUTIONMETHOD']._serialized_end = 2074
    _globals['_INTEGRATIONEXECUTIONDETAILS']._serialized_start = 2077
    _globals['_INTEGRATIONEXECUTIONDETAILS']._serialized_end = 2719
    _globals['_INTEGRATIONEXECUTIONDETAILS_INTEGRATIONEXECUTIONSTATE']._serialized_start = 2542
    _globals['_INTEGRATIONEXECUTIONDETAILS_INTEGRATIONEXECUTIONSTATE']._serialized_end = 2719
    _globals['_INTEGRATIONEXECUTIONSNAPSHOT']._serialized_start = 2722
    _globals['_INTEGRATIONEXECUTIONSNAPSHOT']._serialized_end = 3627
    _globals['_INTEGRATIONEXECUTIONSNAPSHOT_INTEGRATIONEXECUTIONSNAPSHOTMETADATA']._serialized_start = 3270
    _globals['_INTEGRATIONEXECUTIONSNAPSHOT_INTEGRATIONEXECUTIONSNAPSHOTMETADATA']._serialized_end = 3520
    _globals['_INTEGRATIONEXECUTIONSNAPSHOT_EXECUTIONPARAMSENTRY']._serialized_start = 3522
    _globals['_INTEGRATIONEXECUTIONSNAPSHOT_EXECUTIONPARAMSENTRY']._serialized_end = 3627
    _globals['_TASKEXECUTIONDETAILS']._serialized_start = 3630
    _globals['_TASKEXECUTIONDETAILS']._serialized_end = 4117
    _globals['_TASKEXECUTIONDETAILS_TASKEXECUTIONSTATE']._serialized_start = 3859
    _globals['_TASKEXECUTIONDETAILS_TASKEXECUTIONSTATE']._serialized_end = 4117
    _globals['_ATTEMPTSTATS']._serialized_start = 4119
    _globals['_ATTEMPTSTATS']._serialized_end = 4227
    _globals['_ERRORDETAIL']._serialized_start = 4229
    _globals['_ERRORDETAIL']._serialized_end = 4286
    _globals['_CONDITIONRESULT']._serialized_start = 4288
    _globals['_CONDITIONRESULT']._serialized_end = 4376