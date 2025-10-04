from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PrecipitationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRECIPITATION_TYPE_UNSPECIFIED: _ClassVar[PrecipitationType]
    NONE: _ClassVar[PrecipitationType]
    SNOW: _ClassVar[PrecipitationType]
    RAIN: _ClassVar[PrecipitationType]
    LIGHT_RAIN: _ClassVar[PrecipitationType]
    HEAVY_RAIN: _ClassVar[PrecipitationType]
    RAIN_AND_SNOW: _ClassVar[PrecipitationType]
    SLEET: _ClassVar[PrecipitationType]
    FREEZING_RAIN: _ClassVar[PrecipitationType]
PRECIPITATION_TYPE_UNSPECIFIED: PrecipitationType
NONE: PrecipitationType
SNOW: PrecipitationType
RAIN: PrecipitationType
LIGHT_RAIN: PrecipitationType
HEAVY_RAIN: PrecipitationType
RAIN_AND_SNOW: PrecipitationType
SLEET: PrecipitationType
FREEZING_RAIN: PrecipitationType

class Precipitation(_message.Message):
    __slots__ = ('probability', 'snow_qpf', 'qpf')
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    SNOW_QPF_FIELD_NUMBER: _ClassVar[int]
    QPF_FIELD_NUMBER: _ClassVar[int]
    probability: PrecipitationProbability
    snow_qpf: QuantitativePrecipitationForecast
    qpf: QuantitativePrecipitationForecast

    def __init__(self, probability: _Optional[_Union[PrecipitationProbability, _Mapping]]=..., snow_qpf: _Optional[_Union[QuantitativePrecipitationForecast, _Mapping]]=..., qpf: _Optional[_Union[QuantitativePrecipitationForecast, _Mapping]]=...) -> None:
        ...

class PrecipitationProbability(_message.Message):
    __slots__ = ('percent', 'type')
    PERCENT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    percent: int
    type: PrecipitationType

    def __init__(self, percent: _Optional[int]=..., type: _Optional[_Union[PrecipitationType, str]]=...) -> None:
        ...

class QuantitativePrecipitationForecast(_message.Message):
    __slots__ = ('quantity', 'unit')

    class Unit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNIT_UNSPECIFIED: _ClassVar[QuantitativePrecipitationForecast.Unit]
        MILLIMETERS: _ClassVar[QuantitativePrecipitationForecast.Unit]
        INCHES: _ClassVar[QuantitativePrecipitationForecast.Unit]
    UNIT_UNSPECIFIED: QuantitativePrecipitationForecast.Unit
    MILLIMETERS: QuantitativePrecipitationForecast.Unit
    INCHES: QuantitativePrecipitationForecast.Unit
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    quantity: float
    unit: QuantitativePrecipitationForecast.Unit

    def __init__(self, quantity: _Optional[float]=..., unit: _Optional[_Union[QuantitativePrecipitationForecast.Unit, str]]=...) -> None:
        ...