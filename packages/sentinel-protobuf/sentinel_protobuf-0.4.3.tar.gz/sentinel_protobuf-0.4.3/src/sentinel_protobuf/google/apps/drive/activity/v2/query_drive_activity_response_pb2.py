"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/apps/drive/activity/v2/query_drive_activity_response.proto')
_sym_db = _symbol_database.Default()
from ......google.apps.drive.activity.v2 import action_pb2 as google_dot_apps_dot_drive_dot_activity_dot_v2_dot_action__pb2
from ......google.apps.drive.activity.v2 import actor_pb2 as google_dot_apps_dot_drive_dot_activity_dot_v2_dot_actor__pb2
from ......google.apps.drive.activity.v2 import common_pb2 as google_dot_apps_dot_drive_dot_activity_dot_v2_dot_common__pb2
from ......google.apps.drive.activity.v2 import target_pb2 as google_dot_apps_dot_drive_dot_activity_dot_v2_dot_target__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/apps/drive/activity/v2/query_drive_activity_response.proto\x12\x1dgoogle.apps.drive.activity.v2\x1a*google/apps/drive/activity/v2/action.proto\x1a)google/apps/drive/activity/v2/actor.proto\x1a*google/apps/drive/activity/v2/common.proto\x1a*google/apps/drive/activity/v2/target.proto\x1a\x1fgoogle/protobuf/timestamp.proto"w\n\x1aQueryDriveActivityResponse\x12@\n\nactivities\x18\x01 \x03(\x0b2,.google.apps.drive.activity.v2.DriveActivity\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xfa\x02\n\rDriveActivity\x12J\n\x15primary_action_detail\x18\x02 \x01(\x0b2+.google.apps.drive.activity.v2.ActionDetail\x124\n\x06actors\x18\x03 \x03(\x0b2$.google.apps.drive.activity.v2.Actor\x126\n\x07actions\x18\x04 \x03(\x0b2%.google.apps.drive.activity.v2.Action\x126\n\x07targets\x18\x05 \x03(\x0b2%.google.apps.drive.activity.v2.Target\x12/\n\ttimestamp\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x12>\n\ntime_range\x18\x07 \x01(\x0b2(.google.apps.drive.activity.v2.TimeRangeH\x00B\x06\n\x04timeB\xd4\x01\n!com.google.apps.drive.activity.v2B\x1fQueryDriveActivityResponseProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/activity/v2;activity\xa2\x02\x04GADA\xaa\x02\x1dGoogle.Apps.Drive.Activity.V2\xca\x02\x1dGoogle\\Apps\\Drive\\Activity\\V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.drive.activity.v2.query_drive_activity_response_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.apps.drive.activity.v2B\x1fQueryDriveActivityResponseProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/activity/v2;activity\xa2\x02\x04GADA\xaa\x02\x1dGoogle.Apps.Drive.Activity.V2\xca\x02\x1dGoogle\\Apps\\Drive\\Activity\\V2'
    _globals['_QUERYDRIVEACTIVITYRESPONSE']._serialized_start = 308
    _globals['_QUERYDRIVEACTIVITYRESPONSE']._serialized_end = 427
    _globals['_DRIVEACTIVITY']._serialized_start = 430
    _globals['_DRIVEACTIVITY']._serialized_end = 808