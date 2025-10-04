from google.type import localized_text_pb2 as _localized_text_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class WeatherCondition(_message.Message):
    __slots__ = ('icon_base_uri', 'description', 'type')

    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[WeatherCondition.Type]
        CLEAR: _ClassVar[WeatherCondition.Type]
        MOSTLY_CLEAR: _ClassVar[WeatherCondition.Type]
        PARTLY_CLOUDY: _ClassVar[WeatherCondition.Type]
        MOSTLY_CLOUDY: _ClassVar[WeatherCondition.Type]
        CLOUDY: _ClassVar[WeatherCondition.Type]
        WINDY: _ClassVar[WeatherCondition.Type]
        WIND_AND_RAIN: _ClassVar[WeatherCondition.Type]
        LIGHT_RAIN_SHOWERS: _ClassVar[WeatherCondition.Type]
        CHANCE_OF_SHOWERS: _ClassVar[WeatherCondition.Type]
        SCATTERED_SHOWERS: _ClassVar[WeatherCondition.Type]
        RAIN_SHOWERS: _ClassVar[WeatherCondition.Type]
        HEAVY_RAIN_SHOWERS: _ClassVar[WeatherCondition.Type]
        LIGHT_TO_MODERATE_RAIN: _ClassVar[WeatherCondition.Type]
        MODERATE_TO_HEAVY_RAIN: _ClassVar[WeatherCondition.Type]
        RAIN: _ClassVar[WeatherCondition.Type]
        LIGHT_RAIN: _ClassVar[WeatherCondition.Type]
        HEAVY_RAIN: _ClassVar[WeatherCondition.Type]
        RAIN_PERIODICALLY_HEAVY: _ClassVar[WeatherCondition.Type]
        LIGHT_SNOW_SHOWERS: _ClassVar[WeatherCondition.Type]
        CHANCE_OF_SNOW_SHOWERS: _ClassVar[WeatherCondition.Type]
        SCATTERED_SNOW_SHOWERS: _ClassVar[WeatherCondition.Type]
        SNOW_SHOWERS: _ClassVar[WeatherCondition.Type]
        HEAVY_SNOW_SHOWERS: _ClassVar[WeatherCondition.Type]
        LIGHT_TO_MODERATE_SNOW: _ClassVar[WeatherCondition.Type]
        MODERATE_TO_HEAVY_SNOW: _ClassVar[WeatherCondition.Type]
        SNOW: _ClassVar[WeatherCondition.Type]
        LIGHT_SNOW: _ClassVar[WeatherCondition.Type]
        HEAVY_SNOW: _ClassVar[WeatherCondition.Type]
        SNOWSTORM: _ClassVar[WeatherCondition.Type]
        SNOW_PERIODICALLY_HEAVY: _ClassVar[WeatherCondition.Type]
        HEAVY_SNOW_STORM: _ClassVar[WeatherCondition.Type]
        BLOWING_SNOW: _ClassVar[WeatherCondition.Type]
        RAIN_AND_SNOW: _ClassVar[WeatherCondition.Type]
        HAIL: _ClassVar[WeatherCondition.Type]
        HAIL_SHOWERS: _ClassVar[WeatherCondition.Type]
        THUNDERSTORM: _ClassVar[WeatherCondition.Type]
        THUNDERSHOWER: _ClassVar[WeatherCondition.Type]
        LIGHT_THUNDERSTORM_RAIN: _ClassVar[WeatherCondition.Type]
        SCATTERED_THUNDERSTORMS: _ClassVar[WeatherCondition.Type]
        HEAVY_THUNDERSTORM: _ClassVar[WeatherCondition.Type]
    TYPE_UNSPECIFIED: WeatherCondition.Type
    CLEAR: WeatherCondition.Type
    MOSTLY_CLEAR: WeatherCondition.Type
    PARTLY_CLOUDY: WeatherCondition.Type
    MOSTLY_CLOUDY: WeatherCondition.Type
    CLOUDY: WeatherCondition.Type
    WINDY: WeatherCondition.Type
    WIND_AND_RAIN: WeatherCondition.Type
    LIGHT_RAIN_SHOWERS: WeatherCondition.Type
    CHANCE_OF_SHOWERS: WeatherCondition.Type
    SCATTERED_SHOWERS: WeatherCondition.Type
    RAIN_SHOWERS: WeatherCondition.Type
    HEAVY_RAIN_SHOWERS: WeatherCondition.Type
    LIGHT_TO_MODERATE_RAIN: WeatherCondition.Type
    MODERATE_TO_HEAVY_RAIN: WeatherCondition.Type
    RAIN: WeatherCondition.Type
    LIGHT_RAIN: WeatherCondition.Type
    HEAVY_RAIN: WeatherCondition.Type
    RAIN_PERIODICALLY_HEAVY: WeatherCondition.Type
    LIGHT_SNOW_SHOWERS: WeatherCondition.Type
    CHANCE_OF_SNOW_SHOWERS: WeatherCondition.Type
    SCATTERED_SNOW_SHOWERS: WeatherCondition.Type
    SNOW_SHOWERS: WeatherCondition.Type
    HEAVY_SNOW_SHOWERS: WeatherCondition.Type
    LIGHT_TO_MODERATE_SNOW: WeatherCondition.Type
    MODERATE_TO_HEAVY_SNOW: WeatherCondition.Type
    SNOW: WeatherCondition.Type
    LIGHT_SNOW: WeatherCondition.Type
    HEAVY_SNOW: WeatherCondition.Type
    SNOWSTORM: WeatherCondition.Type
    SNOW_PERIODICALLY_HEAVY: WeatherCondition.Type
    HEAVY_SNOW_STORM: WeatherCondition.Type
    BLOWING_SNOW: WeatherCondition.Type
    RAIN_AND_SNOW: WeatherCondition.Type
    HAIL: WeatherCondition.Type
    HAIL_SHOWERS: WeatherCondition.Type
    THUNDERSTORM: WeatherCondition.Type
    THUNDERSHOWER: WeatherCondition.Type
    LIGHT_THUNDERSTORM_RAIN: WeatherCondition.Type
    SCATTERED_THUNDERSTORMS: WeatherCondition.Type
    HEAVY_THUNDERSTORM: WeatherCondition.Type
    ICON_BASE_URI_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    icon_base_uri: str
    description: _localized_text_pb2.LocalizedText
    type: WeatherCondition.Type

    def __init__(self, icon_base_uri: _Optional[str]=..., description: _Optional[_Union[_localized_text_pb2.LocalizedText, _Mapping]]=..., type: _Optional[_Union[WeatherCondition.Type, str]]=...) -> None:
        ...