from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SpaceNotificationSetting(_message.Message):
    __slots__ = ('name', 'notification_setting', 'mute_setting')

    class NotificationSetting(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOTIFICATION_SETTING_UNSPECIFIED: _ClassVar[SpaceNotificationSetting.NotificationSetting]
        ALL: _ClassVar[SpaceNotificationSetting.NotificationSetting]
        MAIN_CONVERSATIONS: _ClassVar[SpaceNotificationSetting.NotificationSetting]
        FOR_YOU: _ClassVar[SpaceNotificationSetting.NotificationSetting]
        OFF: _ClassVar[SpaceNotificationSetting.NotificationSetting]
    NOTIFICATION_SETTING_UNSPECIFIED: SpaceNotificationSetting.NotificationSetting
    ALL: SpaceNotificationSetting.NotificationSetting
    MAIN_CONVERSATIONS: SpaceNotificationSetting.NotificationSetting
    FOR_YOU: SpaceNotificationSetting.NotificationSetting
    OFF: SpaceNotificationSetting.NotificationSetting

    class MuteSetting(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MUTE_SETTING_UNSPECIFIED: _ClassVar[SpaceNotificationSetting.MuteSetting]
        UNMUTED: _ClassVar[SpaceNotificationSetting.MuteSetting]
        MUTED: _ClassVar[SpaceNotificationSetting.MuteSetting]
    MUTE_SETTING_UNSPECIFIED: SpaceNotificationSetting.MuteSetting
    UNMUTED: SpaceNotificationSetting.MuteSetting
    MUTED: SpaceNotificationSetting.MuteSetting
    NAME_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_SETTING_FIELD_NUMBER: _ClassVar[int]
    MUTE_SETTING_FIELD_NUMBER: _ClassVar[int]
    name: str
    notification_setting: SpaceNotificationSetting.NotificationSetting
    mute_setting: SpaceNotificationSetting.MuteSetting

    def __init__(self, name: _Optional[str]=..., notification_setting: _Optional[_Union[SpaceNotificationSetting.NotificationSetting, str]]=..., mute_setting: _Optional[_Union[SpaceNotificationSetting.MuteSetting, str]]=...) -> None:
        ...

class GetSpaceNotificationSettingRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateSpaceNotificationSettingRequest(_message.Message):
    __slots__ = ('space_notification_setting', 'update_mask')
    SPACE_NOTIFICATION_SETTING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    space_notification_setting: SpaceNotificationSetting
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, space_notification_setting: _Optional[_Union[SpaceNotificationSetting, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...