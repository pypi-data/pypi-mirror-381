"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/saasplatform/saasservicemgmt/v1beta1/rollouts_resources.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.saasplatform.saasservicemgmt.v1beta1 import common_pb2 as google_dot_cloud_dot_saasplatform_dot_saasservicemgmt_dot_v1beta1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nJgoogle/cloud/saasplatform/saasservicemgmt/v1beta1/rollouts_resources.proto\x121google.cloud.saasplatform.saasservicemgmt.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a>google/cloud/saasplatform/saasservicemgmt/v1beta1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd1\r\n\x07Rollout\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12B\n\x07release\x18\x03 \x01(\tB1\xe0A\x01\xe0A\x05\xfaA(\n&saasservicemgmt.googleapis.com/Release\x126\n\nstart_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x06\xe0A\x01\xe0A\x03\x124\n\x08end_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x06\xe0A\x01\xe0A\x03\x12[\n\x05state\x18\n \x01(\x0e2G.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout.RolloutStateB\x03\xe0A\x03\x12\x1a\n\rstate_message\x18\x0b \x01(\tB\x03\xe0A\x03\x12A\n\x15state_transition_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x06\xe0A\x01\xe0A\x03\x12G\n\x0croot_rollout\x18\x10 \x01(\tB1\xe0A\x03\xe0A\x01\xfaA(\n&saasservicemgmt.googleapis.com/Rollout\x12I\n\x0eparent_rollout\x18\x11 \x01(\tB1\xe0A\x03\xe0A\x01\xfaA(\n&saasservicemgmt.googleapis.com/Rollout\x12+\n\x1erollout_orchestration_strategy\x18\x13 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bunit_filter\x18\x15 \x01(\tB\x03\xe0A\x01\x12K\n\x0crollout_kind\x18\x16 \x01(\tB5\xe0A\x01\xe0A\x05\xfaA,\n*saasservicemgmt.googleapis.com/RolloutKind\x12V\n\x05stats\x18\x18 \x01(\x0b2?.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutStatsB\x06\xe0A\x03\xe0A\x01\x12W\n\x07control\x18\x19 \x01(\x0b2A.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutControlB\x03\xe0A\x01\x12\\\n\x06labels\x18\xa1Q \x03(\x0b2F.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout.LabelsEntryB\x03\xe0A\x01\x12f\n\x0bannotations\x18\xa2Q \x03(\x0b2K.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout.AnnotationsEntryB\x03\xe0A\x01\x12\x19\n\x03uid\x18\xd9O \x01(\tB\x0b\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12\x12\n\x04etag\x18\xdaO \x01(\tB\x03\xe0A\x03\x125\n\x0bcreate_time\x18\xbfP \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x125\n\x0bupdate_time\x18\xc0P \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xa6\x02\n\x0cRolloutState\x12\x1d\n\x19ROLLOUT_STATE_UNSPECIFIED\x10\x00\x12\x19\n\x15ROLLOUT_STATE_RUNNING\x10\x01\x12\x18\n\x14ROLLOUT_STATE_PAUSED\x10\x02\x12\x1b\n\x17ROLLOUT_STATE_SUCCEEDED\x10\x03\x12\x18\n\x14ROLLOUT_STATE_FAILED\x10\x04\x12\x1b\n\x17ROLLOUT_STATE_CANCELLED\x10\x05\x12\x19\n\x15ROLLOUT_STATE_WAITING\x10\x06\x12\x1c\n\x18ROLLOUT_STATE_CANCELLING\x10\x07\x12\x1a\n\x16ROLLOUT_STATE_RESUMING\x10\x08\x12\x19\n\x15ROLLOUT_STATE_PAUSING\x10\t:}\xeaAz\n&saasservicemgmt.googleapis.com/Rollout\x12=projects/{project}/locations/{location}/rollouts/{rollout_id}*\x08rollouts2\x07rollout"\x95\t\n\x0bRolloutKind\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12E\n\tunit_kind\x18\x02 \x01(\tB2\xe0A\x02\xe0A\x05\xfaA)\n\'saasservicemgmt.googleapis.com/UnitKind\x12+\n\x1erollout_orchestration_strategy\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bunit_filter\x18\x05 \x01(\tB\x03\xe0A\x01\x12}\n\x19update_unit_kind_strategy\x18\x06 \x01(\x0e2U.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind.UpdateUnitKindStrategyB\x03\xe0A\x01\x12^\n\x0cerror_budget\x18\x07 \x01(\x0b2>.google.cloud.saasplatform.saasservicemgmt.v1beta1.ErrorBudgetB\x03\xe0A\x01H\x00\x88\x01\x01\x12`\n\x06labels\x18\xa1Q \x03(\x0b2J.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind.LabelsEntryB\x03\xe0A\x01\x12j\n\x0bannotations\x18\xa2Q \x03(\x0b2O.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind.AnnotationsEntryB\x03\xe0A\x01\x12\x19\n\x03uid\x18\xd9O \x01(\tB\x0b\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12\x12\n\x04etag\x18\xdaO \x01(\tB\x03\xe0A\x03\x125\n\x0bcreate_time\x18\xbfP \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x125\n\x0bupdate_time\x18\xc0P \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x90\x01\n\x16UpdateUnitKindStrategy\x12)\n%UPDATE_UNIT_KIND_STRATEGY_UNSPECIFIED\x10\x00\x12&\n"UPDATE_UNIT_KIND_STRATEGY_ON_START\x10\x01\x12#\n\x1fUPDATE_UNIT_KIND_STRATEGY_NEVER\x10\x02:\x93\x01\xeaA\x8f\x01\n*saasservicemgmt.googleapis.com/RolloutKind\x12Fprojects/{project}/locations/{location}/rolloutKinds/{rollout_kind_id}*\x0crolloutKinds2\x0brolloutKindB\x0f\n\r_error_budget"J\n\x0bErrorBudget\x12\x1a\n\rallowed_count\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x1f\n\x12allowed_percentage\x18\x02 \x01(\x05B\x03\xe0A\x01"n\n\x0cRolloutStats\x12^\n\x13operations_by_state\x18\x02 \x03(\x0b2<.google.cloud.saasplatform.saasservicemgmt.v1beta1.AggregateB\x03\xe0A\x03"\xad\x02\n\x0eRolloutControl\x12s\n\nrun_params\x18\x02 \x01(\x0b2X.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutControl.RunRolloutActionParamsB\x03\xe0A\x01H\x00\x12U\n\x06action\x18\x01 \x01(\x0e2@.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutActionB\x03\xe0A\x02\x1a>\n\x16RunRolloutActionParams\x12$\n\x17retry_failed_operations\x18\x01 \x01(\x08B\x03\xe0A\x02B\x0f\n\raction_params*|\n\rRolloutAction\x12\x1e\n\x1aROLLOUT_ACTION_UNSPECIFIED\x10\x00\x12\x16\n\x12ROLLOUT_ACTION_RUN\x10\x01\x12\x18\n\x14ROLLOUT_ACTION_PAUSE\x10\x02\x12\x19\n\x15ROLLOUT_ACTION_CANCEL\x10\x03B\xd6\x02\n5com.google.cloud.saasplatform.saasservicemgmt.v1beta1B\x1aSaasRolloutsResourcesProtoP\x01Z_cloud.google.com/go/saasplatform/saasservicemgmt/apiv1beta1/saasservicemgmtpb;saasservicemgmtpb\xaa\x021Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1\xca\x021Google\\Cloud\\SaasPlatform\\SaasServiceMgmt\\V1beta1\xea\x025Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.saasplatform.saasservicemgmt.v1beta1.rollouts_resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n5com.google.cloud.saasplatform.saasservicemgmt.v1beta1B\x1aSaasRolloutsResourcesProtoP\x01Z_cloud.google.com/go/saasplatform/saasservicemgmt/apiv1beta1/saasservicemgmtpb;saasservicemgmtpb\xaa\x021Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1\xca\x021Google\\Cloud\\SaasPlatform\\SaasServiceMgmt\\V1beta1\xea\x025Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1'
    _globals['_ROLLOUT_LABELSENTRY']._loaded_options = None
    _globals['_ROLLOUT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ROLLOUT_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_ROLLOUT_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_ROLLOUT'].fields_by_name['name']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ROLLOUT'].fields_by_name['release']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['release']._serialized_options = b'\xe0A\x01\xe0A\x05\xfaA(\n&saasservicemgmt.googleapis.com/Release'
    _globals['_ROLLOUT'].fields_by_name['start_time']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['start_time']._serialized_options = b'\xe0A\x01\xe0A\x03'
    _globals['_ROLLOUT'].fields_by_name['end_time']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['end_time']._serialized_options = b'\xe0A\x01\xe0A\x03'
    _globals['_ROLLOUT'].fields_by_name['state']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_ROLLOUT'].fields_by_name['state_message']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['state_message']._serialized_options = b'\xe0A\x03'
    _globals['_ROLLOUT'].fields_by_name['state_transition_time']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['state_transition_time']._serialized_options = b'\xe0A\x01\xe0A\x03'
    _globals['_ROLLOUT'].fields_by_name['root_rollout']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['root_rollout']._serialized_options = b'\xe0A\x03\xe0A\x01\xfaA(\n&saasservicemgmt.googleapis.com/Rollout'
    _globals['_ROLLOUT'].fields_by_name['parent_rollout']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['parent_rollout']._serialized_options = b'\xe0A\x03\xe0A\x01\xfaA(\n&saasservicemgmt.googleapis.com/Rollout'
    _globals['_ROLLOUT'].fields_by_name['rollout_orchestration_strategy']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['rollout_orchestration_strategy']._serialized_options = b'\xe0A\x01'
    _globals['_ROLLOUT'].fields_by_name['unit_filter']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['unit_filter']._serialized_options = b'\xe0A\x01'
    _globals['_ROLLOUT'].fields_by_name['rollout_kind']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['rollout_kind']._serialized_options = b'\xe0A\x01\xe0A\x05\xfaA,\n*saasservicemgmt.googleapis.com/RolloutKind'
    _globals['_ROLLOUT'].fields_by_name['stats']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['stats']._serialized_options = b'\xe0A\x03\xe0A\x01'
    _globals['_ROLLOUT'].fields_by_name['control']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['control']._serialized_options = b'\xe0A\x01'
    _globals['_ROLLOUT'].fields_by_name['labels']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_ROLLOUT'].fields_by_name['annotations']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['annotations']._serialized_options = b'\xe0A\x01'
    _globals['_ROLLOUT'].fields_by_name['uid']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['uid']._serialized_options = b'\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_ROLLOUT'].fields_by_name['etag']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_ROLLOUT'].fields_by_name['create_time']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ROLLOUT'].fields_by_name['update_time']._loaded_options = None
    _globals['_ROLLOUT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ROLLOUT']._loaded_options = None
    _globals['_ROLLOUT']._serialized_options = b'\xeaAz\n&saasservicemgmt.googleapis.com/Rollout\x12=projects/{project}/locations/{location}/rollouts/{rollout_id}*\x08rollouts2\x07rollout'
    _globals['_ROLLOUTKIND_LABELSENTRY']._loaded_options = None
    _globals['_ROLLOUTKIND_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ROLLOUTKIND_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_ROLLOUTKIND_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_ROLLOUTKIND'].fields_by_name['name']._loaded_options = None
    _globals['_ROLLOUTKIND'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ROLLOUTKIND'].fields_by_name['unit_kind']._loaded_options = None
    _globals['_ROLLOUTKIND'].fields_by_name['unit_kind']._serialized_options = b"\xe0A\x02\xe0A\x05\xfaA)\n'saasservicemgmt.googleapis.com/UnitKind"
    _globals['_ROLLOUTKIND'].fields_by_name['rollout_orchestration_strategy']._loaded_options = None
    _globals['_ROLLOUTKIND'].fields_by_name['rollout_orchestration_strategy']._serialized_options = b'\xe0A\x01'
    _globals['_ROLLOUTKIND'].fields_by_name['unit_filter']._loaded_options = None
    _globals['_ROLLOUTKIND'].fields_by_name['unit_filter']._serialized_options = b'\xe0A\x01'
    _globals['_ROLLOUTKIND'].fields_by_name['update_unit_kind_strategy']._loaded_options = None
    _globals['_ROLLOUTKIND'].fields_by_name['update_unit_kind_strategy']._serialized_options = b'\xe0A\x01'
    _globals['_ROLLOUTKIND'].fields_by_name['error_budget']._loaded_options = None
    _globals['_ROLLOUTKIND'].fields_by_name['error_budget']._serialized_options = b'\xe0A\x01'
    _globals['_ROLLOUTKIND'].fields_by_name['labels']._loaded_options = None
    _globals['_ROLLOUTKIND'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_ROLLOUTKIND'].fields_by_name['annotations']._loaded_options = None
    _globals['_ROLLOUTKIND'].fields_by_name['annotations']._serialized_options = b'\xe0A\x01'
    _globals['_ROLLOUTKIND'].fields_by_name['uid']._loaded_options = None
    _globals['_ROLLOUTKIND'].fields_by_name['uid']._serialized_options = b'\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_ROLLOUTKIND'].fields_by_name['etag']._loaded_options = None
    _globals['_ROLLOUTKIND'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_ROLLOUTKIND'].fields_by_name['create_time']._loaded_options = None
    _globals['_ROLLOUTKIND'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ROLLOUTKIND'].fields_by_name['update_time']._loaded_options = None
    _globals['_ROLLOUTKIND'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ROLLOUTKIND']._loaded_options = None
    _globals['_ROLLOUTKIND']._serialized_options = b'\xeaA\x8f\x01\n*saasservicemgmt.googleapis.com/RolloutKind\x12Fprojects/{project}/locations/{location}/rolloutKinds/{rollout_kind_id}*\x0crolloutKinds2\x0brolloutKind'
    _globals['_ERRORBUDGET'].fields_by_name['allowed_count']._loaded_options = None
    _globals['_ERRORBUDGET'].fields_by_name['allowed_count']._serialized_options = b'\xe0A\x01'
    _globals['_ERRORBUDGET'].fields_by_name['allowed_percentage']._loaded_options = None
    _globals['_ERRORBUDGET'].fields_by_name['allowed_percentage']._serialized_options = b'\xe0A\x01'
    _globals['_ROLLOUTSTATS'].fields_by_name['operations_by_state']._loaded_options = None
    _globals['_ROLLOUTSTATS'].fields_by_name['operations_by_state']._serialized_options = b'\xe0A\x03'
    _globals['_ROLLOUTCONTROL_RUNROLLOUTACTIONPARAMS'].fields_by_name['retry_failed_operations']._loaded_options = None
    _globals['_ROLLOUTCONTROL_RUNROLLOUTACTIONPARAMS'].fields_by_name['retry_failed_operations']._serialized_options = b'\xe0A\x02'
    _globals['_ROLLOUTCONTROL'].fields_by_name['run_params']._loaded_options = None
    _globals['_ROLLOUTCONTROL'].fields_by_name['run_params']._serialized_options = b'\xe0A\x01'
    _globals['_ROLLOUTCONTROL'].fields_by_name['action']._loaded_options = None
    _globals['_ROLLOUTCONTROL'].fields_by_name['action']._serialized_options = b'\xe0A\x02'
    _globals['_ROLLOUTACTION']._serialized_start = 3731
    _globals['_ROLLOUTACTION']._serialized_end = 3855
    _globals['_ROLLOUT']._serialized_start = 316
    _globals['_ROLLOUT']._serialized_end = 2061
    _globals['_ROLLOUT_LABELSENTRY']._serialized_start = 1540
    _globals['_ROLLOUT_LABELSENTRY']._serialized_end = 1585
    _globals['_ROLLOUT_ANNOTATIONSENTRY']._serialized_start = 1587
    _globals['_ROLLOUT_ANNOTATIONSENTRY']._serialized_end = 1637
    _globals['_ROLLOUT_ROLLOUTSTATE']._serialized_start = 1640
    _globals['_ROLLOUT_ROLLOUTSTATE']._serialized_end = 1934
    _globals['_ROLLOUTKIND']._serialized_start = 2064
    _globals['_ROLLOUTKIND']._serialized_end = 3237
    _globals['_ROLLOUTKIND_LABELSENTRY']._serialized_start = 1540
    _globals['_ROLLOUTKIND_LABELSENTRY']._serialized_end = 1585
    _globals['_ROLLOUTKIND_ANNOTATIONSENTRY']._serialized_start = 1587
    _globals['_ROLLOUTKIND_ANNOTATIONSENTRY']._serialized_end = 1637
    _globals['_ROLLOUTKIND_UPDATEUNITKINDSTRATEGY']._serialized_start = 2926
    _globals['_ROLLOUTKIND_UPDATEUNITKINDSTRATEGY']._serialized_end = 3070
    _globals['_ERRORBUDGET']._serialized_start = 3239
    _globals['_ERRORBUDGET']._serialized_end = 3313
    _globals['_ROLLOUTSTATS']._serialized_start = 3315
    _globals['_ROLLOUTSTATS']._serialized_end = 3425
    _globals['_ROLLOUTCONTROL']._serialized_start = 3428
    _globals['_ROLLOUTCONTROL']._serialized_end = 3729
    _globals['_ROLLOUTCONTROL_RUNROLLOUTACTIONPARAMS']._serialized_start = 3650
    _globals['_ROLLOUTCONTROL_RUNROLLOUTACTIONPARAMS']._serialized_end = 3712