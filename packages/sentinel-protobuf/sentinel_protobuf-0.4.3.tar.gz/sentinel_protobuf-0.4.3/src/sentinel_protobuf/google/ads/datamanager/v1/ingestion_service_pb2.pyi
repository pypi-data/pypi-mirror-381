from google.ads.datamanager.v1 import audience_pb2 as _audience_pb2
from google.ads.datamanager.v1 import consent_pb2 as _consent_pb2
from google.ads.datamanager.v1 import destination_pb2 as _destination_pb2
from google.ads.datamanager.v1 import encryption_info_pb2 as _encryption_info_pb2
from google.ads.datamanager.v1 import event_pb2 as _event_pb2
from google.ads.datamanager.v1 import terms_of_service_pb2 as _terms_of_service_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Encoding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENCODING_UNSPECIFIED: _ClassVar[Encoding]
    HEX: _ClassVar[Encoding]
    BASE64: _ClassVar[Encoding]
ENCODING_UNSPECIFIED: Encoding
HEX: Encoding
BASE64: Encoding

class IngestAudienceMembersRequest(_message.Message):
    __slots__ = ('destinations', 'audience_members', 'consent', 'validate_only', 'encoding', 'encryption_info', 'terms_of_service')
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    CONSENT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_INFO_FIELD_NUMBER: _ClassVar[int]
    TERMS_OF_SERVICE_FIELD_NUMBER: _ClassVar[int]
    destinations: _containers.RepeatedCompositeFieldContainer[_destination_pb2.Destination]
    audience_members: _containers.RepeatedCompositeFieldContainer[_audience_pb2.AudienceMember]
    consent: _consent_pb2.Consent
    validate_only: bool
    encoding: Encoding
    encryption_info: _encryption_info_pb2.EncryptionInfo
    terms_of_service: _terms_of_service_pb2.TermsOfService

    def __init__(self, destinations: _Optional[_Iterable[_Union[_destination_pb2.Destination, _Mapping]]]=..., audience_members: _Optional[_Iterable[_Union[_audience_pb2.AudienceMember, _Mapping]]]=..., consent: _Optional[_Union[_consent_pb2.Consent, _Mapping]]=..., validate_only: bool=..., encoding: _Optional[_Union[Encoding, str]]=..., encryption_info: _Optional[_Union[_encryption_info_pb2.EncryptionInfo, _Mapping]]=..., terms_of_service: _Optional[_Union[_terms_of_service_pb2.TermsOfService, _Mapping]]=...) -> None:
        ...

class IngestAudienceMembersResponse(_message.Message):
    __slots__ = ('request_id',)
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    request_id: str

    def __init__(self, request_id: _Optional[str]=...) -> None:
        ...

class RemoveAudienceMembersRequest(_message.Message):
    __slots__ = ('destinations', 'audience_members', 'validate_only', 'encoding', 'encryption_info')
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_INFO_FIELD_NUMBER: _ClassVar[int]
    destinations: _containers.RepeatedCompositeFieldContainer[_destination_pb2.Destination]
    audience_members: _containers.RepeatedCompositeFieldContainer[_audience_pb2.AudienceMember]
    validate_only: bool
    encoding: Encoding
    encryption_info: _encryption_info_pb2.EncryptionInfo

    def __init__(self, destinations: _Optional[_Iterable[_Union[_destination_pb2.Destination, _Mapping]]]=..., audience_members: _Optional[_Iterable[_Union[_audience_pb2.AudienceMember, _Mapping]]]=..., validate_only: bool=..., encoding: _Optional[_Union[Encoding, str]]=..., encryption_info: _Optional[_Union[_encryption_info_pb2.EncryptionInfo, _Mapping]]=...) -> None:
        ...

class RemoveAudienceMembersResponse(_message.Message):
    __slots__ = ('request_id',)
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    request_id: str

    def __init__(self, request_id: _Optional[str]=...) -> None:
        ...

class IngestEventsRequest(_message.Message):
    __slots__ = ('destinations', 'events', 'consent', 'validate_only', 'encoding', 'encryption_info')
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    CONSENT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_INFO_FIELD_NUMBER: _ClassVar[int]
    destinations: _containers.RepeatedCompositeFieldContainer[_destination_pb2.Destination]
    events: _containers.RepeatedCompositeFieldContainer[_event_pb2.Event]
    consent: _consent_pb2.Consent
    validate_only: bool
    encoding: Encoding
    encryption_info: _encryption_info_pb2.EncryptionInfo

    def __init__(self, destinations: _Optional[_Iterable[_Union[_destination_pb2.Destination, _Mapping]]]=..., events: _Optional[_Iterable[_Union[_event_pb2.Event, _Mapping]]]=..., consent: _Optional[_Union[_consent_pb2.Consent, _Mapping]]=..., validate_only: bool=..., encoding: _Optional[_Union[Encoding, str]]=..., encryption_info: _Optional[_Union[_encryption_info_pb2.EncryptionInfo, _Mapping]]=...) -> None:
        ...

class IngestEventsResponse(_message.Message):
    __slots__ = ('request_id',)
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    request_id: str

    def __init__(self, request_id: _Optional[str]=...) -> None:
        ...