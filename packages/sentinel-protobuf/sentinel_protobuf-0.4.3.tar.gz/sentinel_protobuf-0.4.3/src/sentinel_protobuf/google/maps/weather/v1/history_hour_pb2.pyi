from google.maps.weather.v1 import air_pressure_pb2 as _air_pressure_pb2
from google.maps.weather.v1 import ice_pb2 as _ice_pb2
from google.maps.weather.v1 import precipitation_pb2 as _precipitation_pb2
from google.maps.weather.v1 import temperature_pb2 as _temperature_pb2
from google.maps.weather.v1 import visibility_pb2 as _visibility_pb2
from google.maps.weather.v1 import weather_condition_pb2 as _weather_condition_pb2
from google.maps.weather.v1 import wind_pb2 as _wind_pb2
from google.type import datetime_pb2 as _datetime_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class HistoryHour(_message.Message):
    __slots__ = ('interval', 'display_date_time', 'is_daytime', 'weather_condition', 'temperature', 'feels_like_temperature', 'dew_point', 'heat_index', 'wind_chill', 'wet_bulb_temperature', 'relative_humidity', 'uv_index', 'precipitation', 'thunderstorm_probability', 'air_pressure', 'wind', 'visibility', 'cloud_cover', 'ice_thickness')
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_DAYTIME_FIELD_NUMBER: _ClassVar[int]
    WEATHER_CONDITION_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    FEELS_LIKE_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    DEW_POINT_FIELD_NUMBER: _ClassVar[int]
    HEAT_INDEX_FIELD_NUMBER: _ClassVar[int]
    WIND_CHILL_FIELD_NUMBER: _ClassVar[int]
    WET_BULB_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    UV_INDEX_FIELD_NUMBER: _ClassVar[int]
    PRECIPITATION_FIELD_NUMBER: _ClassVar[int]
    THUNDERSTORM_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    AIR_PRESSURE_FIELD_NUMBER: _ClassVar[int]
    WIND_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    CLOUD_COVER_FIELD_NUMBER: _ClassVar[int]
    ICE_THICKNESS_FIELD_NUMBER: _ClassVar[int]
    interval: _interval_pb2.Interval
    display_date_time: _datetime_pb2.DateTime
    is_daytime: bool
    weather_condition: _weather_condition_pb2.WeatherCondition
    temperature: _temperature_pb2.Temperature
    feels_like_temperature: _temperature_pb2.Temperature
    dew_point: _temperature_pb2.Temperature
    heat_index: _temperature_pb2.Temperature
    wind_chill: _temperature_pb2.Temperature
    wet_bulb_temperature: _temperature_pb2.Temperature
    relative_humidity: int
    uv_index: int
    precipitation: _precipitation_pb2.Precipitation
    thunderstorm_probability: int
    air_pressure: _air_pressure_pb2.AirPressure
    wind: _wind_pb2.Wind
    visibility: _visibility_pb2.Visibility
    cloud_cover: int
    ice_thickness: _ice_pb2.IceThickness

    def __init__(self, interval: _Optional[_Union[_interval_pb2.Interval, _Mapping]]=..., display_date_time: _Optional[_Union[_datetime_pb2.DateTime, _Mapping]]=..., is_daytime: bool=..., weather_condition: _Optional[_Union[_weather_condition_pb2.WeatherCondition, _Mapping]]=..., temperature: _Optional[_Union[_temperature_pb2.Temperature, _Mapping]]=..., feels_like_temperature: _Optional[_Union[_temperature_pb2.Temperature, _Mapping]]=..., dew_point: _Optional[_Union[_temperature_pb2.Temperature, _Mapping]]=..., heat_index: _Optional[_Union[_temperature_pb2.Temperature, _Mapping]]=..., wind_chill: _Optional[_Union[_temperature_pb2.Temperature, _Mapping]]=..., wet_bulb_temperature: _Optional[_Union[_temperature_pb2.Temperature, _Mapping]]=..., relative_humidity: _Optional[int]=..., uv_index: _Optional[int]=..., precipitation: _Optional[_Union[_precipitation_pb2.Precipitation, _Mapping]]=..., thunderstorm_probability: _Optional[int]=..., air_pressure: _Optional[_Union[_air_pressure_pb2.AirPressure, _Mapping]]=..., wind: _Optional[_Union[_wind_pb2.Wind, _Mapping]]=..., visibility: _Optional[_Union[_visibility_pb2.Visibility, _Mapping]]=..., cloud_cover: _Optional[int]=..., ice_thickness: _Optional[_Union[_ice_pb2.IceThickness, _Mapping]]=...) -> None:
        ...