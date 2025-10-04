from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesLeadSurveyAnswerEnum(_message.Message):
    __slots__ = ()

    class SurveyAnswer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocalServicesLeadSurveyAnswerEnum.SurveyAnswer]
        UNKNOWN: _ClassVar[LocalServicesLeadSurveyAnswerEnum.SurveyAnswer]
        VERY_SATISFIED: _ClassVar[LocalServicesLeadSurveyAnswerEnum.SurveyAnswer]
        SATISFIED: _ClassVar[LocalServicesLeadSurveyAnswerEnum.SurveyAnswer]
        NEUTRAL: _ClassVar[LocalServicesLeadSurveyAnswerEnum.SurveyAnswer]
        DISSATISFIED: _ClassVar[LocalServicesLeadSurveyAnswerEnum.SurveyAnswer]
        VERY_DISSATISFIED: _ClassVar[LocalServicesLeadSurveyAnswerEnum.SurveyAnswer]
    UNSPECIFIED: LocalServicesLeadSurveyAnswerEnum.SurveyAnswer
    UNKNOWN: LocalServicesLeadSurveyAnswerEnum.SurveyAnswer
    VERY_SATISFIED: LocalServicesLeadSurveyAnswerEnum.SurveyAnswer
    SATISFIED: LocalServicesLeadSurveyAnswerEnum.SurveyAnswer
    NEUTRAL: LocalServicesLeadSurveyAnswerEnum.SurveyAnswer
    DISSATISFIED: LocalServicesLeadSurveyAnswerEnum.SurveyAnswer
    VERY_DISSATISFIED: LocalServicesLeadSurveyAnswerEnum.SurveyAnswer

    def __init__(self) -> None:
        ...