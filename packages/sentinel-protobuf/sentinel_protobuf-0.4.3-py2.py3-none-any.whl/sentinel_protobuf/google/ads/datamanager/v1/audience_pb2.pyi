from google.ads.datamanager.v1 import consent_pb2 as _consent_pb2
from google.ads.datamanager.v1 import user_data_pb2 as _user_data_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AudienceMember(_message.Message):
    __slots__ = ('user_data', 'pair_data', 'mobile_data', 'consent')
    USER_DATA_FIELD_NUMBER: _ClassVar[int]
    PAIR_DATA_FIELD_NUMBER: _ClassVar[int]
    MOBILE_DATA_FIELD_NUMBER: _ClassVar[int]
    CONSENT_FIELD_NUMBER: _ClassVar[int]
    user_data: _user_data_pb2.UserData
    pair_data: PairData
    mobile_data: MobileData
    consent: _consent_pb2.Consent

    def __init__(self, user_data: _Optional[_Union[_user_data_pb2.UserData, _Mapping]]=..., pair_data: _Optional[_Union[PairData, _Mapping]]=..., mobile_data: _Optional[_Union[MobileData, _Mapping]]=..., consent: _Optional[_Union[_consent_pb2.Consent, _Mapping]]=...) -> None:
        ...

class PairData(_message.Message):
    __slots__ = ('pair_ids',)
    PAIR_IDS_FIELD_NUMBER: _ClassVar[int]
    pair_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, pair_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class MobileData(_message.Message):
    __slots__ = ('mobile_ids',)
    MOBILE_IDS_FIELD_NUMBER: _ClassVar[int]
    mobile_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, mobile_ids: _Optional[_Iterable[str]]=...) -> None:
        ...