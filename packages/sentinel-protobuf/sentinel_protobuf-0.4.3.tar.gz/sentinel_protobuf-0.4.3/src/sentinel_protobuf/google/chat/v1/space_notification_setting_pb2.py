"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/chat/v1/space_notification_setting.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/chat/v1/space_notification_setting.proto\x12\x0egoogle.chat.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xc6\x04\n\x18SpaceNotificationSetting\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12_\n\x14notification_setting\x18\x02 \x01(\x0e2<.google.chat.v1.SpaceNotificationSetting.NotificationSettingH\x00\x88\x01\x01\x12O\n\x0cmute_setting\x18\x03 \x01(\x0e24.google.chat.v1.SpaceNotificationSetting.MuteSettingH\x01\x88\x01\x01"r\n\x13NotificationSetting\x12$\n NOTIFICATION_SETTING_UNSPECIFIED\x10\x00\x12\x07\n\x03ALL\x10\x01\x12\x16\n\x12MAIN_CONVERSATIONS\x10\x02\x12\x0b\n\x07FOR_YOU\x10\x03\x12\x07\n\x03OFF\x10\x04"C\n\x0bMuteSetting\x12\x1c\n\x18MUTE_SETTING_UNSPECIFIED\x10\x00\x12\x0b\n\x07UNMUTED\x10\x01\x12\t\n\x05MUTED\x10\x02:\x81\x01\xeaA~\n,chat.googleapis.com/SpaceNotificationSetting\x124users/{user}/spaces/{space}/spaceNotificationSetting2\x18spaceNotificationSettingB\x17\n\x15_notification_settingB\x0f\n\r_mute_setting"h\n"GetSpaceNotificationSettingRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,chat.googleapis.com/SpaceNotificationSetting"\xb0\x01\n%UpdateSpaceNotificationSettingRequest\x12Q\n\x1aspace_notification_setting\x18\x01 \x01(\x0b2(.google.chat.v1.SpaceNotificationSettingB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02B\xb6\x01\n\x12com.google.chat.v1B\x1dSpaceNotificationSettingProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.chat.v1.space_notification_setting_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x12com.google.chat.v1B\x1dSpaceNotificationSettingProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1'
    _globals['_SPACENOTIFICATIONSETTING'].fields_by_name['name']._loaded_options = None
    _globals['_SPACENOTIFICATIONSETTING'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_SPACENOTIFICATIONSETTING']._loaded_options = None
    _globals['_SPACENOTIFICATIONSETTING']._serialized_options = b'\xeaA~\n,chat.googleapis.com/SpaceNotificationSetting\x124users/{user}/spaces/{space}/spaceNotificationSetting2\x18spaceNotificationSetting'
    _globals['_GETSPACENOTIFICATIONSETTINGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSPACENOTIFICATIONSETTINGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,chat.googleapis.com/SpaceNotificationSetting'
    _globals['_UPDATESPACENOTIFICATIONSETTINGREQUEST'].fields_by_name['space_notification_setting']._loaded_options = None
    _globals['_UPDATESPACENOTIFICATIONSETTINGREQUEST'].fields_by_name['space_notification_setting']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESPACENOTIFICATIONSETTINGREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESPACENOTIFICATIONSETTINGREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_SPACENOTIFICATIONSETTING']._serialized_start = 162
    _globals['_SPACENOTIFICATIONSETTING']._serialized_end = 744
    _globals['_SPACENOTIFICATIONSETTING_NOTIFICATIONSETTING']._serialized_start = 387
    _globals['_SPACENOTIFICATIONSETTING_NOTIFICATIONSETTING']._serialized_end = 501
    _globals['_SPACENOTIFICATIONSETTING_MUTESETTING']._serialized_start = 503
    _globals['_SPACENOTIFICATIONSETTING_MUTESETTING']._serialized_end = 570
    _globals['_GETSPACENOTIFICATIONSETTINGREQUEST']._serialized_start = 746
    _globals['_GETSPACENOTIFICATIONSETTINGREQUEST']._serialized_end = 850
    _globals['_UPDATESPACENOTIFICATIONSETTINGREQUEST']._serialized_start = 853
    _globals['_UPDATESPACENOTIFICATIONSETTINGREQUEST']._serialized_end = 1029