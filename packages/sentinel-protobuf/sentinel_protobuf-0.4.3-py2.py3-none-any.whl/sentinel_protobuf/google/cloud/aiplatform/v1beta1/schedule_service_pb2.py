"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/schedule_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.cloud.aiplatform.v1beta1 import schedule_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_schedule__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/aiplatform/v1beta1/schedule_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a.google/cloud/aiplatform/v1beta1/schedule.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x94\x01\n\x15CreateScheduleRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12@\n\x08schedule\x18\x02 \x01(\x0b2).google.cloud.aiplatform.v1beta1.ScheduleB\x03\xe0A\x02"N\n\x12GetScheduleRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Schedule"\x9a\x01\n\x14ListSchedulesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"n\n\x15ListSchedulesResponse\x12<\n\tschedules\x18\x01 \x03(\x0b2).google.cloud.aiplatform.v1beta1.Schedule\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"Q\n\x15DeleteScheduleRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Schedule"P\n\x14PauseScheduleRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Schedule"h\n\x15ResumeScheduleRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Schedule\x12\x15\n\x08catch_up\x18\x02 \x01(\x08B\x03\xe0A\x01"\x8f\x01\n\x15UpdateScheduleRequest\x12@\n\x08schedule\x18\x01 \x01(\x0b2).google.cloud.aiplatform.v1beta1.ScheduleB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x022\xd0\x0b\n\x0fScheduleService\x12\xcb\x01\n\x0eCreateSchedule\x126.google.cloud.aiplatform.v1beta1.CreateScheduleRequest\x1a).google.cloud.aiplatform.v1beta1.Schedule"V\xdaA\x0fparent,schedule\x82\xd3\xe4\x93\x02>"2/v1beta1/{parent=projects/*/locations/*}/schedules:\x08schedule\x12\xdd\x01\n\x0eDeleteSchedule\x126.google.cloud.aiplatform.v1beta1.DeleteScheduleRequest\x1a\x1d.google.longrunning.Operation"t\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1beta1/{name=projects/*/locations/*/schedules/*}\x12\xb0\x01\n\x0bGetSchedule\x123.google.cloud.aiplatform.v1beta1.GetScheduleRequest\x1a).google.cloud.aiplatform.v1beta1.Schedule"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1beta1/{name=projects/*/locations/*/schedules/*}\x12\xc3\x01\n\rListSchedules\x125.google.cloud.aiplatform.v1beta1.ListSchedulesRequest\x1a6.google.cloud.aiplatform.v1beta1.ListSchedulesResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1beta1/{parent=projects/*/locations/*}/schedules\x12\xaa\x01\n\rPauseSchedule\x125.google.cloud.aiplatform.v1beta1.PauseScheduleRequest\x1a\x16.google.protobuf.Empty"J\xdaA\x04name\x82\xd3\xe4\x93\x02="8/v1beta1/{name=projects/*/locations/*/schedules/*}:pause:\x01*\x12\xbd\x01\n\x0eResumeSchedule\x126.google.cloud.aiplatform.v1beta1.ResumeScheduleRequest\x1a\x16.google.protobuf.Empty"[\xdaA\x04name\xdaA\rname,catch_up\x82\xd3\xe4\x93\x02>"9/v1beta1/{name=projects/*/locations/*/schedules/*}:resume:\x01*\x12\xd9\x01\n\x0eUpdateSchedule\x126.google.cloud.aiplatform.v1beta1.UpdateScheduleRequest\x1a).google.cloud.aiplatform.v1beta1.Schedule"d\xdaA\x14schedule,update_mask\x82\xd3\xe4\x93\x02G2;/v1beta1/{schedule.name=projects/*/locations/*/schedules/*}:\x08schedule\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xeb\x01\n#com.google.cloud.aiplatform.v1beta1B\x14ScheduleServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.schedule_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x14ScheduleServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CREATESCHEDULEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESCHEDULEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATESCHEDULEREQUEST'].fields_by_name['schedule']._loaded_options = None
    _globals['_CREATESCHEDULEREQUEST'].fields_by_name['schedule']._serialized_options = b'\xe0A\x02'
    _globals['_GETSCHEDULEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSCHEDULEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Schedule'
    _globals['_LISTSCHEDULESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSCHEDULESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_DELETESCHEDULEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESCHEDULEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Schedule'
    _globals['_PAUSESCHEDULEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_PAUSESCHEDULEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Schedule'
    _globals['_RESUMESCHEDULEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESUMESCHEDULEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Schedule'
    _globals['_RESUMESCHEDULEREQUEST'].fields_by_name['catch_up']._loaded_options = None
    _globals['_RESUMESCHEDULEREQUEST'].fields_by_name['catch_up']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATESCHEDULEREQUEST'].fields_by_name['schedule']._loaded_options = None
    _globals['_UPDATESCHEDULEREQUEST'].fields_by_name['schedule']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESCHEDULEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESCHEDULEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_SCHEDULESERVICE']._loaded_options = None
    _globals['_SCHEDULESERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SCHEDULESERVICE'].methods_by_name['CreateSchedule']._loaded_options = None
    _globals['_SCHEDULESERVICE'].methods_by_name['CreateSchedule']._serialized_options = b'\xdaA\x0fparent,schedule\x82\xd3\xe4\x93\x02>"2/v1beta1/{parent=projects/*/locations/*}/schedules:\x08schedule'
    _globals['_SCHEDULESERVICE'].methods_by_name['DeleteSchedule']._loaded_options = None
    _globals['_SCHEDULESERVICE'].methods_by_name['DeleteSchedule']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1beta1/{name=projects/*/locations/*/schedules/*}'
    _globals['_SCHEDULESERVICE'].methods_by_name['GetSchedule']._loaded_options = None
    _globals['_SCHEDULESERVICE'].methods_by_name['GetSchedule']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1beta1/{name=projects/*/locations/*/schedules/*}'
    _globals['_SCHEDULESERVICE'].methods_by_name['ListSchedules']._loaded_options = None
    _globals['_SCHEDULESERVICE'].methods_by_name['ListSchedules']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1beta1/{parent=projects/*/locations/*}/schedules'
    _globals['_SCHEDULESERVICE'].methods_by_name['PauseSchedule']._loaded_options = None
    _globals['_SCHEDULESERVICE'].methods_by_name['PauseSchedule']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02="8/v1beta1/{name=projects/*/locations/*/schedules/*}:pause:\x01*'
    _globals['_SCHEDULESERVICE'].methods_by_name['ResumeSchedule']._loaded_options = None
    _globals['_SCHEDULESERVICE'].methods_by_name['ResumeSchedule']._serialized_options = b'\xdaA\x04name\xdaA\rname,catch_up\x82\xd3\xe4\x93\x02>"9/v1beta1/{name=projects/*/locations/*/schedules/*}:resume:\x01*'
    _globals['_SCHEDULESERVICE'].methods_by_name['UpdateSchedule']._loaded_options = None
    _globals['_SCHEDULESERVICE'].methods_by_name['UpdateSchedule']._serialized_options = b'\xdaA\x14schedule,update_mask\x82\xd3\xe4\x93\x02G2;/v1beta1/{schedule.name=projects/*/locations/*/schedules/*}:\x08schedule'
    _globals['_CREATESCHEDULEREQUEST']._serialized_start = 404
    _globals['_CREATESCHEDULEREQUEST']._serialized_end = 552
    _globals['_GETSCHEDULEREQUEST']._serialized_start = 554
    _globals['_GETSCHEDULEREQUEST']._serialized_end = 632
    _globals['_LISTSCHEDULESREQUEST']._serialized_start = 635
    _globals['_LISTSCHEDULESREQUEST']._serialized_end = 789
    _globals['_LISTSCHEDULESRESPONSE']._serialized_start = 791
    _globals['_LISTSCHEDULESRESPONSE']._serialized_end = 901
    _globals['_DELETESCHEDULEREQUEST']._serialized_start = 903
    _globals['_DELETESCHEDULEREQUEST']._serialized_end = 984
    _globals['_PAUSESCHEDULEREQUEST']._serialized_start = 986
    _globals['_PAUSESCHEDULEREQUEST']._serialized_end = 1066
    _globals['_RESUMESCHEDULEREQUEST']._serialized_start = 1068
    _globals['_RESUMESCHEDULEREQUEST']._serialized_end = 1172
    _globals['_UPDATESCHEDULEREQUEST']._serialized_start = 1175
    _globals['_UPDATESCHEDULEREQUEST']._serialized_end = 1318
    _globals['_SCHEDULESERVICE']._serialized_start = 1321
    _globals['_SCHEDULESERVICE']._serialized_end = 2809