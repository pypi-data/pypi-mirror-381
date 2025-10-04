from google.maps.weather.v1 import celestial_events_pb2 as _celestial_events_pb2
from google.maps.weather.v1 import ice_pb2 as _ice_pb2
from google.maps.weather.v1 import precipitation_pb2 as _precipitation_pb2
from google.maps.weather.v1 import temperature_pb2 as _temperature_pb2
from google.maps.weather.v1 import weather_condition_pb2 as _weather_condition_pb2
from google.maps.weather.v1 import wind_pb2 as _wind_pb2
from google.type import date_pb2 as _date_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ForecastDay(_message.Message):
    __slots__ = ('interval', 'display_date', 'daytime_forecast', 'nighttime_forecast', 'max_temperature', 'min_temperature', 'feels_like_max_temperature', 'feels_like_min_temperature', 'max_heat_index', 'sun_events', 'moon_events')
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_DATE_FIELD_NUMBER: _ClassVar[int]
    DAYTIME_FORECAST_FIELD_NUMBER: _ClassVar[int]
    NIGHTTIME_FORECAST_FIELD_NUMBER: _ClassVar[int]
    MAX_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    MIN_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    FEELS_LIKE_MAX_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    FEELS_LIKE_MIN_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    MAX_HEAT_INDEX_FIELD_NUMBER: _ClassVar[int]
    SUN_EVENTS_FIELD_NUMBER: _ClassVar[int]
    MOON_EVENTS_FIELD_NUMBER: _ClassVar[int]
    interval: _interval_pb2.Interval
    display_date: _date_pb2.Date
    daytime_forecast: ForecastDayPart
    nighttime_forecast: ForecastDayPart
    max_temperature: _temperature_pb2.Temperature
    min_temperature: _temperature_pb2.Temperature
    feels_like_max_temperature: _temperature_pb2.Temperature
    feels_like_min_temperature: _temperature_pb2.Temperature
    max_heat_index: _temperature_pb2.Temperature
    sun_events: _celestial_events_pb2.SunEvents
    moon_events: _celestial_events_pb2.MoonEvents

    def __init__(self, interval: _Optional[_Union[_interval_pb2.Interval, _Mapping]]=..., display_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., daytime_forecast: _Optional[_Union[ForecastDayPart, _Mapping]]=..., nighttime_forecast: _Optional[_Union[ForecastDayPart, _Mapping]]=..., max_temperature: _Optional[_Union[_temperature_pb2.Temperature, _Mapping]]=..., min_temperature: _Optional[_Union[_temperature_pb2.Temperature, _Mapping]]=..., feels_like_max_temperature: _Optional[_Union[_temperature_pb2.Temperature, _Mapping]]=..., feels_like_min_temperature: _Optional[_Union[_temperature_pb2.Temperature, _Mapping]]=..., max_heat_index: _Optional[_Union[_temperature_pb2.Temperature, _Mapping]]=..., sun_events: _Optional[_Union[_celestial_events_pb2.SunEvents, _Mapping]]=..., moon_events: _Optional[_Union[_celestial_events_pb2.MoonEvents, _Mapping]]=...) -> None:
        ...

class ForecastDayPart(_message.Message):
    __slots__ = ('interval', 'weather_condition', 'relative_humidity', 'uv_index', 'precipitation', 'thunderstorm_probability', 'wind', 'cloud_cover', 'ice_thickness')
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    WEATHER_CONDITION_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    UV_INDEX_FIELD_NUMBER: _ClassVar[int]
    PRECIPITATION_FIELD_NUMBER: _ClassVar[int]
    THUNDERSTORM_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    WIND_FIELD_NUMBER: _ClassVar[int]
    CLOUD_COVER_FIELD_NUMBER: _ClassVar[int]
    ICE_THICKNESS_FIELD_NUMBER: _ClassVar[int]
    interval: _interval_pb2.Interval
    weather_condition: _weather_condition_pb2.WeatherCondition
    relative_humidity: int
    uv_index: int
    precipitation: _precipitation_pb2.Precipitation
    thunderstorm_probability: int
    wind: _wind_pb2.Wind
    cloud_cover: int
    ice_thickness: _ice_pb2.IceThickness

    def __init__(self, interval: _Optional[_Union[_interval_pb2.Interval, _Mapping]]=..., weather_condition: _Optional[_Union[_weather_condition_pb2.WeatherCondition, _Mapping]]=..., relative_humidity: _Optional[int]=..., uv_index: _Optional[int]=..., precipitation: _Optional[_Union[_precipitation_pb2.Precipitation, _Mapping]]=..., thunderstorm_probability: _Optional[int]=..., wind: _Optional[_Union[_wind_pb2.Wind, _Mapping]]=..., cloud_cover: _Optional[int]=..., ice_thickness: _Optional[_Union[_ice_pb2.IceThickness, _Mapping]]=...) -> None:
        ...