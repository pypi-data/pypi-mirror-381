from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MoonPhase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MOON_PHASE_UNSPECIFIED: _ClassVar[MoonPhase]
    NEW_MOON: _ClassVar[MoonPhase]
    WAXING_CRESCENT: _ClassVar[MoonPhase]
    FIRST_QUARTER: _ClassVar[MoonPhase]
    WAXING_GIBBOUS: _ClassVar[MoonPhase]
    FULL_MOON: _ClassVar[MoonPhase]
    WANING_GIBBOUS: _ClassVar[MoonPhase]
    LAST_QUARTER: _ClassVar[MoonPhase]
    WANING_CRESCENT: _ClassVar[MoonPhase]
MOON_PHASE_UNSPECIFIED: MoonPhase
NEW_MOON: MoonPhase
WAXING_CRESCENT: MoonPhase
FIRST_QUARTER: MoonPhase
WAXING_GIBBOUS: MoonPhase
FULL_MOON: MoonPhase
WANING_GIBBOUS: MoonPhase
LAST_QUARTER: MoonPhase
WANING_CRESCENT: MoonPhase

class SunEvents(_message.Message):
    __slots__ = ('sunrise_time', 'sunset_time')
    SUNRISE_TIME_FIELD_NUMBER: _ClassVar[int]
    SUNSET_TIME_FIELD_NUMBER: _ClassVar[int]
    sunrise_time: _timestamp_pb2.Timestamp
    sunset_time: _timestamp_pb2.Timestamp

    def __init__(self, sunrise_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., sunset_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class MoonEvents(_message.Message):
    __slots__ = ('moonrise_times', 'moonset_times', 'moon_phase')
    MOONRISE_TIMES_FIELD_NUMBER: _ClassVar[int]
    MOONSET_TIMES_FIELD_NUMBER: _ClassVar[int]
    MOON_PHASE_FIELD_NUMBER: _ClassVar[int]
    moonrise_times: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    moonset_times: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    moon_phase: MoonPhase

    def __init__(self, moonrise_times: _Optional[_Iterable[_Union[_timestamp_pb2.Timestamp, _Mapping]]]=..., moonset_times: _Optional[_Iterable[_Union[_timestamp_pb2.Timestamp, _Mapping]]]=..., moon_phase: _Optional[_Union[MoonPhase, str]]=...) -> None:
        ...