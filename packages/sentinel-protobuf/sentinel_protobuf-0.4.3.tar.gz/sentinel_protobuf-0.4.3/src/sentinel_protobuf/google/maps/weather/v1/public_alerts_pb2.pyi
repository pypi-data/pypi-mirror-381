from google.maps.weather.v1 import public_alerts_enums_pb2 as _public_alerts_enums_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import localized_text_pb2 as _localized_text_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataSource(_message.Message):
    __slots__ = ('publisher', 'name', 'authority_uri')
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHORITY_URI_FIELD_NUMBER: _ClassVar[int]
    publisher: _public_alerts_enums_pb2.Publisher
    name: str
    authority_uri: str

    def __init__(self, publisher: _Optional[_Union[_public_alerts_enums_pb2.Publisher, str]]=..., name: _Optional[str]=..., authority_uri: _Optional[str]=...) -> None:
        ...

class SafetyRecommendation(_message.Message):
    __slots__ = ('directive', 'subtext')
    DIRECTIVE_FIELD_NUMBER: _ClassVar[int]
    SUBTEXT_FIELD_NUMBER: _ClassVar[int]
    directive: str
    subtext: str

    def __init__(self, directive: _Optional[str]=..., subtext: _Optional[str]=...) -> None:
        ...

class PublicAlerts(_message.Message):
    __slots__ = ('alert_id', 'alert_title', 'event_type', 'area_name', 'polygon', 'description', 'severity', 'certainty', 'urgency', 'instruction', 'safety_recommendations', 'timezone_offset', 'start_time', 'expiration_time', 'data_source')
    ALERT_ID_FIELD_NUMBER: _ClassVar[int]
    ALERT_TITLE_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    AREA_NAME_FIELD_NUMBER: _ClassVar[int]
    POLYGON_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    CERTAINTY_FIELD_NUMBER: _ClassVar[int]
    URGENCY_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    SAFETY_RECOMMENDATIONS_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    DATA_SOURCE_FIELD_NUMBER: _ClassVar[int]
    alert_id: str
    alert_title: _localized_text_pb2.LocalizedText
    event_type: _public_alerts_enums_pb2.WeatherEventType
    area_name: str
    polygon: str
    description: str
    severity: _public_alerts_enums_pb2.Severity
    certainty: _public_alerts_enums_pb2.Certainty
    urgency: _public_alerts_enums_pb2.Urgency
    instruction: _containers.RepeatedScalarFieldContainer[str]
    safety_recommendations: _containers.RepeatedCompositeFieldContainer[SafetyRecommendation]
    timezone_offset: str
    start_time: _timestamp_pb2.Timestamp
    expiration_time: _timestamp_pb2.Timestamp
    data_source: DataSource

    def __init__(self, alert_id: _Optional[str]=..., alert_title: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]]=..., event_type: _Optional[_Union[_public_alerts_enums_pb2.WeatherEventType, str]]=..., area_name: _Optional[str]=..., polygon: _Optional[str]=..., description: _Optional[str]=..., severity: _Optional[_Union[_public_alerts_enums_pb2.Severity, str]]=..., certainty: _Optional[_Union[_public_alerts_enums_pb2.Certainty, str]]=..., urgency: _Optional[_Union[_public_alerts_enums_pb2.Urgency, str]]=..., instruction: _Optional[_Iterable[str]]=..., safety_recommendations: _Optional[_Iterable[_Union[SafetyRecommendation, _Mapping]]]=..., timezone_offset: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., data_source: _Optional[_Union[DataSource, _Mapping]]=...) -> None:
        ...