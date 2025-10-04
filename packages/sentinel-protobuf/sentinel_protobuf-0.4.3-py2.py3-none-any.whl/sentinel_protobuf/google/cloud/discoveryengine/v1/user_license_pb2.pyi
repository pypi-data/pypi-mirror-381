from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UserLicense(_message.Message):
    __slots__ = ('user_principal', 'user_profile', 'license_assignment_state', 'license_config', 'create_time', 'update_time', 'last_login_time')

    class LicenseAssignmentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LICENSE_ASSIGNMENT_STATE_UNSPECIFIED: _ClassVar[UserLicense.LicenseAssignmentState]
        ASSIGNED: _ClassVar[UserLicense.LicenseAssignmentState]
        UNASSIGNED: _ClassVar[UserLicense.LicenseAssignmentState]
        NO_LICENSE: _ClassVar[UserLicense.LicenseAssignmentState]
        NO_LICENSE_ATTEMPTED_LOGIN: _ClassVar[UserLicense.LicenseAssignmentState]
    LICENSE_ASSIGNMENT_STATE_UNSPECIFIED: UserLicense.LicenseAssignmentState
    ASSIGNED: UserLicense.LicenseAssignmentState
    UNASSIGNED: UserLicense.LicenseAssignmentState
    NO_LICENSE: UserLicense.LicenseAssignmentState
    NO_LICENSE_ATTEMPTED_LOGIN: UserLicense.LicenseAssignmentState
    USER_PRINCIPAL_FIELD_NUMBER: _ClassVar[int]
    USER_PROFILE_FIELD_NUMBER: _ClassVar[int]
    LICENSE_ASSIGNMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    LICENSE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_LOGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    user_principal: str
    user_profile: str
    license_assignment_state: UserLicense.LicenseAssignmentState
    license_config: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    last_login_time: _timestamp_pb2.Timestamp

    def __init__(self, user_principal: _Optional[str]=..., user_profile: _Optional[str]=..., license_assignment_state: _Optional[_Union[UserLicense.LicenseAssignmentState, str]]=..., license_config: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_login_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...