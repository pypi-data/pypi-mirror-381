from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class HarmCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HARM_CATEGORY_UNSPECIFIED: _ClassVar[HarmCategory]
    HARM_CATEGORY_HATE_SPEECH: _ClassVar[HarmCategory]
    HARM_CATEGORY_DANGEROUS_CONTENT: _ClassVar[HarmCategory]
    HARM_CATEGORY_HARASSMENT: _ClassVar[HarmCategory]
    HARM_CATEGORY_SEXUALLY_EXPLICIT: _ClassVar[HarmCategory]
    HARM_CATEGORY_CIVIC_INTEGRITY: _ClassVar[HarmCategory]
HARM_CATEGORY_UNSPECIFIED: HarmCategory
HARM_CATEGORY_HATE_SPEECH: HarmCategory
HARM_CATEGORY_DANGEROUS_CONTENT: HarmCategory
HARM_CATEGORY_HARASSMENT: HarmCategory
HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmCategory
HARM_CATEGORY_CIVIC_INTEGRITY: HarmCategory

class SafetyRating(_message.Message):
    __slots__ = ('category', 'probability', 'probability_score', 'severity', 'severity_score', 'blocked')

    class HarmProbability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HARM_PROBABILITY_UNSPECIFIED: _ClassVar[SafetyRating.HarmProbability]
        NEGLIGIBLE: _ClassVar[SafetyRating.HarmProbability]
        LOW: _ClassVar[SafetyRating.HarmProbability]
        MEDIUM: _ClassVar[SafetyRating.HarmProbability]
        HIGH: _ClassVar[SafetyRating.HarmProbability]
    HARM_PROBABILITY_UNSPECIFIED: SafetyRating.HarmProbability
    NEGLIGIBLE: SafetyRating.HarmProbability
    LOW: SafetyRating.HarmProbability
    MEDIUM: SafetyRating.HarmProbability
    HIGH: SafetyRating.HarmProbability

    class HarmSeverity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HARM_SEVERITY_UNSPECIFIED: _ClassVar[SafetyRating.HarmSeverity]
        HARM_SEVERITY_NEGLIGIBLE: _ClassVar[SafetyRating.HarmSeverity]
        HARM_SEVERITY_LOW: _ClassVar[SafetyRating.HarmSeverity]
        HARM_SEVERITY_MEDIUM: _ClassVar[SafetyRating.HarmSeverity]
        HARM_SEVERITY_HIGH: _ClassVar[SafetyRating.HarmSeverity]
    HARM_SEVERITY_UNSPECIFIED: SafetyRating.HarmSeverity
    HARM_SEVERITY_NEGLIGIBLE: SafetyRating.HarmSeverity
    HARM_SEVERITY_LOW: SafetyRating.HarmSeverity
    HARM_SEVERITY_MEDIUM: SafetyRating.HarmSeverity
    HARM_SEVERITY_HIGH: SafetyRating.HarmSeverity
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_SCORE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_SCORE_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_FIELD_NUMBER: _ClassVar[int]
    category: HarmCategory
    probability: SafetyRating.HarmProbability
    probability_score: float
    severity: SafetyRating.HarmSeverity
    severity_score: float
    blocked: bool

    def __init__(self, category: _Optional[_Union[HarmCategory, str]]=..., probability: _Optional[_Union[SafetyRating.HarmProbability, str]]=..., probability_score: _Optional[float]=..., severity: _Optional[_Union[SafetyRating.HarmSeverity, str]]=..., severity_score: _Optional[float]=..., blocked: bool=...) -> None:
        ...