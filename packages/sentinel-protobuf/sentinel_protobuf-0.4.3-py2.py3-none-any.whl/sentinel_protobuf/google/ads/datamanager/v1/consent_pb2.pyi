from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ConsentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONSENT_STATUS_UNSPECIFIED: _ClassVar[ConsentStatus]
    CONSENT_GRANTED: _ClassVar[ConsentStatus]
    CONSENT_DENIED: _ClassVar[ConsentStatus]
CONSENT_STATUS_UNSPECIFIED: ConsentStatus
CONSENT_GRANTED: ConsentStatus
CONSENT_DENIED: ConsentStatus

class Consent(_message.Message):
    __slots__ = ('ad_user_data', 'ad_personalization')
    AD_USER_DATA_FIELD_NUMBER: _ClassVar[int]
    AD_PERSONALIZATION_FIELD_NUMBER: _ClassVar[int]
    ad_user_data: ConsentStatus
    ad_personalization: ConsentStatus

    def __init__(self, ad_user_data: _Optional[_Union[ConsentStatus, str]]=..., ad_personalization: _Optional[_Union[ConsentStatus, str]]=...) -> None:
        ...