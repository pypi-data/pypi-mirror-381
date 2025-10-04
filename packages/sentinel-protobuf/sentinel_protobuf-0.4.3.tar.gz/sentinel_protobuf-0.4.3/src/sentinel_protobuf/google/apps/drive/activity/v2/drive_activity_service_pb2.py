"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/apps/drive/activity/v2/drive_activity_service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.apps.drive.activity.v2 import query_drive_activity_request_pb2 as google_dot_apps_dot_drive_dot_activity_dot_v2_dot_query__drive__activity__request__pb2
from ......google.apps.drive.activity.v2 import query_drive_activity_response_pb2 as google_dot_apps_dot_drive_dot_activity_dot_v2_dot_query__drive__activity__response__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/apps/drive/activity/v2/drive_activity_service.proto\x12\x1dgoogle.apps.drive.activity.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a@google/apps/drive/activity/v2/query_drive_activity_request.proto\x1aAgoogle/apps/drive/activity/v2/query_drive_activity_response.proto2\xcc\x02\n\x14DriveActivityService\x12\xa8\x01\n\x12QueryDriveActivity\x128.google.apps.drive.activity.v2.QueryDriveActivityRequest\x1a9.google.apps.drive.activity.v2.QueryDriveActivityResponse"\x1d\x82\xd3\xe4\x93\x02\x17"\x12/v2/activity:query:\x01*\x1a\x88\x01\xcaA\x1cdriveactivity.googleapis.com\xd2Afhttps://www.googleapis.com/auth/drive.activity,https://www.googleapis.com/auth/drive.activity.readonlyB\xce\x01\n!com.google.apps.drive.activity.v2B\x19DriveActivityServiceProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/activity/v2;activity\xa2\x02\x04GADA\xaa\x02\x1dGoogle.Apps.Drive.Activity.V2\xca\x02\x1dGoogle\\Apps\\Drive\\Activity\\V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.drive.activity.v2.drive_activity_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.apps.drive.activity.v2B\x19DriveActivityServiceProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/activity/v2;activity\xa2\x02\x04GADA\xaa\x02\x1dGoogle.Apps.Drive.Activity.V2\xca\x02\x1dGoogle\\Apps\\Drive\\Activity\\V2'
    _globals['_DRIVEACTIVITYSERVICE']._loaded_options = None
    _globals['_DRIVEACTIVITYSERVICE']._serialized_options = b'\xcaA\x1cdriveactivity.googleapis.com\xd2Afhttps://www.googleapis.com/auth/drive.activity,https://www.googleapis.com/auth/drive.activity.readonly'
    _globals['_DRIVEACTIVITYSERVICE'].methods_by_name['QueryDriveActivity']._loaded_options = None
    _globals['_DRIVEACTIVITYSERVICE'].methods_by_name['QueryDriveActivity']._serialized_options = b'\x82\xd3\xe4\x93\x02\x17"\x12/v2/activity:query:\x01*'
    _globals['_DRIVEACTIVITYSERVICE']._serialized_start = 282
    _globals['_DRIVEACTIVITYSERVICE']._serialized_end = 614