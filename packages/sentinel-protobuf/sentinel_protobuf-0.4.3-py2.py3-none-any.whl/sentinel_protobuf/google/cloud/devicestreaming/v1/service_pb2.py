"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/devicestreaming/v1/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.devicestreaming.v1 import adb_service_pb2 as google_dot_cloud_dot_devicestreaming_dot_v1_dot_adb__service__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/devicestreaming/v1/service.proto\x12\x1fgoogle.cloud.devicestreaming.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/devicestreaming/v1/adb_service.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xce\x01\n\x1aCreateDeviceSessionRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12K\n\x0edevice_session\x18\x02 \x01(\x0b2..google.cloud.devicestreaming.v1.DeviceSessionB\x03\xe0A\x02\x12\x1e\n\x11device_session_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xa6\x01\n\x19ListDeviceSessionsRequest\x12C\n\x06parent\x18\x04 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x16\n\tpage_size\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x03 \x01(\tB\x03\xe0A\x01"~\n\x1aListDeviceSessionsResponse\x12G\n\x0fdevice_sessions\x18\x01 \x03(\x0b2..google.cloud.devicestreaming.v1.DeviceSession\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"]\n\x17GetDeviceSessionRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,devicestreaming.googleapis.com/DeviceSession"`\n\x1aCancelDeviceSessionRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,devicestreaming.googleapis.com/DeviceSession"\x9f\x01\n\x1aUpdateDeviceSessionRequest\x12K\n\x0edevice_session\x18\x01 \x01(\x0b2..google.cloud.devicestreaming.v1.DeviceSessionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\xb5\x08\n\rDeviceSession\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x03\x12O\n\x05state\x18\x03 \x01(\x0e2;.google.cloud.devicestreaming.v1.DeviceSession.SessionStateB\x03\xe0A\x03\x12^\n\x0fstate_histories\x18\x0e \x03(\x0b2@.google.cloud.devicestreaming.v1.DeviceSession.SessionStateEventB\x03\xe0A\x03\x12-\n\x03ttl\x18\r \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01H\x00\x126\n\x0bexpire_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01H\x00\x12:\n\x12inactivity_timeout\x18\x07 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12:\n\x11active_start_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12K\n\x0eandroid_device\x18\x0f \x01(\x0b2..google.cloud.devicestreaming.v1.AndroidDeviceB\x03\xe0A\x02\x1a\xbd\x01\n\x11SessionStateEvent\x12W\n\rsession_state\x18\x01 \x01(\x0e2;.google.cloud.devicestreaming.v1.DeviceSession.SessionStateB\x03\xe0A\x03\x123\n\nevent_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1a\n\rstate_message\x18\x03 \x01(\tB\x03\xe0A\x03"\x8c\x01\n\x0cSessionState\x12\x1d\n\x19SESSION_STATE_UNSPECIFIED\x10\x00\x12\r\n\tREQUESTED\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\n\n\x06ACTIVE\x10\x03\x12\x0b\n\x07EXPIRED\x10\x04\x12\x0c\n\x08FINISHED\x10\x05\x12\x0f\n\x0bUNAVAILABLE\x10\x06\x12\t\n\x05ERROR\x10\x07:\x85\x01\xeaA\x81\x01\n,devicestreaming.googleapis.com/DeviceSession\x122projects/{project}/deviceSessions/{device_session}*\x0edeviceSessions2\rdeviceSessionB\x0c\n\nexpiration"~\n\rAndroidDevice\x12\x1d\n\x10android_model_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1f\n\x12android_version_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06locale\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0borientation\x18\x04 \x01(\tB\x03\xe0A\x012\xe0\t\n\x13DirectAccessService\x12\xec\x01\n\x13CreateDeviceSession\x12;.google.cloud.devicestreaming.v1.CreateDeviceSessionRequest\x1a..google.cloud.devicestreaming.v1.DeviceSession"h\xdaA\'parent,device_session,device_session_id\x82\xd3\xe4\x93\x028"&/v1/{parent=projects/*}/deviceSessions:\x0edevice_session\x12\xc6\x01\n\x12ListDeviceSessions\x12:.google.cloud.devicestreaming.v1.ListDeviceSessionsRequest\x1a;.google.cloud.devicestreaming.v1.ListDeviceSessionsResponse"7\xdaA\x06parent\x82\xd3\xe4\x93\x02(\x12&/v1/{parent=projects/*}/deviceSessions\x12\xb3\x01\n\x10GetDeviceSession\x128.google.cloud.devicestreaming.v1.GetDeviceSessionRequest\x1a..google.cloud.devicestreaming.v1.DeviceSession"5\xdaA\x04name\x82\xd3\xe4\x93\x02(\x12&/v1/{name=projects/*/deviceSessions/*}\x12\xa4\x01\n\x13CancelDeviceSession\x12;.google.cloud.devicestreaming.v1.CancelDeviceSessionRequest\x1a\x16.google.protobuf.Empty"8\x82\xd3\xe4\x93\x022"-/v1/{name=projects/*/deviceSessions/*}:cancel:\x01*\x12\xee\x01\n\x13UpdateDeviceSession\x12;.google.cloud.devicestreaming.v1.UpdateDeviceSessionRequest\x1a..google.cloud.devicestreaming.v1.DeviceSession"j\xdaA\x1adevice_session,update_mask\x82\xd3\xe4\x93\x02G25/v1/{device_session.name=projects/*/deviceSessions/*}:\x0edevice_session\x12o\n\nAdbConnect\x12+.google.cloud.devicestreaming.v1.AdbMessage\x1a..google.cloud.devicestreaming.v1.DeviceMessage"\x00(\x010\x01\x1aR\xcaA\x1edevicestreaming.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xed\x01\n#com.google.cloud.devicestreaming.v1B\x0cServiceProtoP\x01ZMcloud.google.com/go/devicestreaming/apiv1/devicestreamingpb;devicestreamingpb\xaa\x02\x1fGoogle.Cloud.DeviceStreaming.V1\xca\x02\x1fGoogle\\Cloud\\DeviceStreaming\\V1\xea\x02"Google::Cloud::DeviceStreaming::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.devicestreaming.v1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.devicestreaming.v1B\x0cServiceProtoP\x01ZMcloud.google.com/go/devicestreaming/apiv1/devicestreamingpb;devicestreamingpb\xaa\x02\x1fGoogle.Cloud.DeviceStreaming.V1\xca\x02\x1fGoogle\\Cloud\\DeviceStreaming\\V1\xea\x02"Google::Cloud::DeviceStreaming::V1'
    _globals['_CREATEDEVICESESSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDEVICESESSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_CREATEDEVICESESSIONREQUEST'].fields_by_name['device_session']._loaded_options = None
    _globals['_CREATEDEVICESESSIONREQUEST'].fields_by_name['device_session']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDEVICESESSIONREQUEST'].fields_by_name['device_session_id']._loaded_options = None
    _globals['_CREATEDEVICESESSIONREQUEST'].fields_by_name['device_session_id']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDEVICESESSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDEVICESESSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_LISTDEVICESESSIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTDEVICESESSIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDEVICESESSIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTDEVICESESSIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDEVICESESSIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTDEVICESESSIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_GETDEVICESESSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDEVICESESSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,devicestreaming.googleapis.com/DeviceSession'
    _globals['_CANCELDEVICESESSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CANCELDEVICESESSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,devicestreaming.googleapis.com/DeviceSession'
    _globals['_UPDATEDEVICESESSIONREQUEST'].fields_by_name['device_session']._loaded_options = None
    _globals['_UPDATEDEVICESESSIONREQUEST'].fields_by_name['device_session']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDEVICESESSIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEDEVICESESSIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_DEVICESESSION_SESSIONSTATEEVENT'].fields_by_name['session_state']._loaded_options = None
    _globals['_DEVICESESSION_SESSIONSTATEEVENT'].fields_by_name['session_state']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICESESSION_SESSIONSTATEEVENT'].fields_by_name['event_time']._loaded_options = None
    _globals['_DEVICESESSION_SESSIONSTATEEVENT'].fields_by_name['event_time']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICESESSION_SESSIONSTATEEVENT'].fields_by_name['state_message']._loaded_options = None
    _globals['_DEVICESESSION_SESSIONSTATEEVENT'].fields_by_name['state_message']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICESESSION'].fields_by_name['name']._loaded_options = None
    _globals['_DEVICESESSION'].fields_by_name['name']._serialized_options = b'\xe0A\x01'
    _globals['_DEVICESESSION'].fields_by_name['display_name']._loaded_options = None
    _globals['_DEVICESESSION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICESESSION'].fields_by_name['state']._loaded_options = None
    _globals['_DEVICESESSION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICESESSION'].fields_by_name['state_histories']._loaded_options = None
    _globals['_DEVICESESSION'].fields_by_name['state_histories']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICESESSION'].fields_by_name['ttl']._loaded_options = None
    _globals['_DEVICESESSION'].fields_by_name['ttl']._serialized_options = b'\xe0A\x01'
    _globals['_DEVICESESSION'].fields_by_name['expire_time']._loaded_options = None
    _globals['_DEVICESESSION'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x01'
    _globals['_DEVICESESSION'].fields_by_name['inactivity_timeout']._loaded_options = None
    _globals['_DEVICESESSION'].fields_by_name['inactivity_timeout']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICESESSION'].fields_by_name['create_time']._loaded_options = None
    _globals['_DEVICESESSION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICESESSION'].fields_by_name['active_start_time']._loaded_options = None
    _globals['_DEVICESESSION'].fields_by_name['active_start_time']._serialized_options = b'\xe0A\x03'
    _globals['_DEVICESESSION'].fields_by_name['android_device']._loaded_options = None
    _globals['_DEVICESESSION'].fields_by_name['android_device']._serialized_options = b'\xe0A\x02'
    _globals['_DEVICESESSION']._loaded_options = None
    _globals['_DEVICESESSION']._serialized_options = b'\xeaA\x81\x01\n,devicestreaming.googleapis.com/DeviceSession\x122projects/{project}/deviceSessions/{device_session}*\x0edeviceSessions2\rdeviceSession'
    _globals['_ANDROIDDEVICE'].fields_by_name['android_model_id']._loaded_options = None
    _globals['_ANDROIDDEVICE'].fields_by_name['android_model_id']._serialized_options = b'\xe0A\x02'
    _globals['_ANDROIDDEVICE'].fields_by_name['android_version_id']._loaded_options = None
    _globals['_ANDROIDDEVICE'].fields_by_name['android_version_id']._serialized_options = b'\xe0A\x02'
    _globals['_ANDROIDDEVICE'].fields_by_name['locale']._loaded_options = None
    _globals['_ANDROIDDEVICE'].fields_by_name['locale']._serialized_options = b'\xe0A\x01'
    _globals['_ANDROIDDEVICE'].fields_by_name['orientation']._loaded_options = None
    _globals['_ANDROIDDEVICE'].fields_by_name['orientation']._serialized_options = b'\xe0A\x01'
    _globals['_DIRECTACCESSSERVICE']._loaded_options = None
    _globals['_DIRECTACCESSSERVICE']._serialized_options = b'\xcaA\x1edevicestreaming.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DIRECTACCESSSERVICE'].methods_by_name['CreateDeviceSession']._loaded_options = None
    _globals['_DIRECTACCESSSERVICE'].methods_by_name['CreateDeviceSession']._serialized_options = b'\xdaA\'parent,device_session,device_session_id\x82\xd3\xe4\x93\x028"&/v1/{parent=projects/*}/deviceSessions:\x0edevice_session'
    _globals['_DIRECTACCESSSERVICE'].methods_by_name['ListDeviceSessions']._loaded_options = None
    _globals['_DIRECTACCESSSERVICE'].methods_by_name['ListDeviceSessions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02(\x12&/v1/{parent=projects/*}/deviceSessions'
    _globals['_DIRECTACCESSSERVICE'].methods_by_name['GetDeviceSession']._loaded_options = None
    _globals['_DIRECTACCESSSERVICE'].methods_by_name['GetDeviceSession']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02(\x12&/v1/{name=projects/*/deviceSessions/*}'
    _globals['_DIRECTACCESSSERVICE'].methods_by_name['CancelDeviceSession']._loaded_options = None
    _globals['_DIRECTACCESSSERVICE'].methods_by_name['CancelDeviceSession']._serialized_options = b'\x82\xd3\xe4\x93\x022"-/v1/{name=projects/*/deviceSessions/*}:cancel:\x01*'
    _globals['_DIRECTACCESSSERVICE'].methods_by_name['UpdateDeviceSession']._loaded_options = None
    _globals['_DIRECTACCESSSERVICE'].methods_by_name['UpdateDeviceSession']._serialized_options = b'\xdaA\x1adevice_session,update_mask\x82\xd3\xe4\x93\x02G25/v1/{device_session.name=projects/*/deviceSessions/*}:\x0edevice_session'
    _globals['_CREATEDEVICESESSIONREQUEST']._serialized_start = 377
    _globals['_CREATEDEVICESESSIONREQUEST']._serialized_end = 583
    _globals['_LISTDEVICESESSIONSREQUEST']._serialized_start = 586
    _globals['_LISTDEVICESESSIONSREQUEST']._serialized_end = 752
    _globals['_LISTDEVICESESSIONSRESPONSE']._serialized_start = 754
    _globals['_LISTDEVICESESSIONSRESPONSE']._serialized_end = 880
    _globals['_GETDEVICESESSIONREQUEST']._serialized_start = 882
    _globals['_GETDEVICESESSIONREQUEST']._serialized_end = 975
    _globals['_CANCELDEVICESESSIONREQUEST']._serialized_start = 977
    _globals['_CANCELDEVICESESSIONREQUEST']._serialized_end = 1073
    _globals['_UPDATEDEVICESESSIONREQUEST']._serialized_start = 1076
    _globals['_UPDATEDEVICESESSIONREQUEST']._serialized_end = 1235
    _globals['_DEVICESESSION']._serialized_start = 1238
    _globals['_DEVICESESSION']._serialized_end = 2315
    _globals['_DEVICESESSION_SESSIONSTATEEVENT']._serialized_start = 1833
    _globals['_DEVICESESSION_SESSIONSTATEEVENT']._serialized_end = 2022
    _globals['_DEVICESESSION_SESSIONSTATE']._serialized_start = 2025
    _globals['_DEVICESESSION_SESSIONSTATE']._serialized_end = 2165
    _globals['_ANDROIDDEVICE']._serialized_start = 2317
    _globals['_ANDROIDDEVICE']._serialized_end = 2443
    _globals['_DIRECTACCESSSERVICE']._serialized_start = 2446
    _globals['_DIRECTACCESSSERVICE']._serialized_end = 3694