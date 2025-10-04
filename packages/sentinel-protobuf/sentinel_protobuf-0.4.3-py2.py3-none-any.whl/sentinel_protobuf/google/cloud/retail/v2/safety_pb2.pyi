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

class SafetySetting(_message.Message):
    __slots__ = ('category', 'threshold', 'method')

    class HarmBlockThreshold(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HARM_BLOCK_THRESHOLD_UNSPECIFIED: _ClassVar[SafetySetting.HarmBlockThreshold]
        BLOCK_LOW_AND_ABOVE: _ClassVar[SafetySetting.HarmBlockThreshold]
        BLOCK_MEDIUM_AND_ABOVE: _ClassVar[SafetySetting.HarmBlockThreshold]
        BLOCK_ONLY_HIGH: _ClassVar[SafetySetting.HarmBlockThreshold]
        BLOCK_NONE: _ClassVar[SafetySetting.HarmBlockThreshold]
        OFF: _ClassVar[SafetySetting.HarmBlockThreshold]
    HARM_BLOCK_THRESHOLD_UNSPECIFIED: SafetySetting.HarmBlockThreshold
    BLOCK_LOW_AND_ABOVE: SafetySetting.HarmBlockThreshold
    BLOCK_MEDIUM_AND_ABOVE: SafetySetting.HarmBlockThreshold
    BLOCK_ONLY_HIGH: SafetySetting.HarmBlockThreshold
    BLOCK_NONE: SafetySetting.HarmBlockThreshold
    OFF: SafetySetting.HarmBlockThreshold

    class HarmBlockMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HARM_BLOCK_METHOD_UNSPECIFIED: _ClassVar[SafetySetting.HarmBlockMethod]
        SEVERITY: _ClassVar[SafetySetting.HarmBlockMethod]
        PROBABILITY: _ClassVar[SafetySetting.HarmBlockMethod]
    HARM_BLOCK_METHOD_UNSPECIFIED: SafetySetting.HarmBlockMethod
    SEVERITY: SafetySetting.HarmBlockMethod
    PROBABILITY: SafetySetting.HarmBlockMethod
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    category: HarmCategory
    threshold: SafetySetting.HarmBlockThreshold
    method: SafetySetting.HarmBlockMethod

    def __init__(self, category: _Optional[_Union[HarmCategory, str]]=..., threshold: _Optional[_Union[SafetySetting.HarmBlockThreshold, str]]=..., method: _Optional[_Union[SafetySetting.HarmBlockMethod, str]]=...) -> None:
        ...