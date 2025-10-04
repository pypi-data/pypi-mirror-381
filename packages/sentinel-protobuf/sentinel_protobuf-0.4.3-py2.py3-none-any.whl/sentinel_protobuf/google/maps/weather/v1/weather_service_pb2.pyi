from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.maps.weather.v1 import air_pressure_pb2 as _air_pressure_pb2
from google.maps.weather.v1 import forecast_day_pb2 as _forecast_day_pb2
from google.maps.weather.v1 import forecast_hour_pb2 as _forecast_hour_pb2
from google.maps.weather.v1 import history_hour_pb2 as _history_hour_pb2
from google.maps.weather.v1 import precipitation_pb2 as _precipitation_pb2
from google.maps.weather.v1 import public_alerts_pb2 as _public_alerts_pb2
from google.maps.weather.v1 import temperature_pb2 as _temperature_pb2
from google.maps.weather.v1 import units_system_pb2 as _units_system_pb2
from google.maps.weather.v1 import visibility_pb2 as _visibility_pb2
from google.maps.weather.v1 import weather_condition_pb2 as _weather_condition_pb2
from google.maps.weather.v1 import wind_pb2 as _wind_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import datetime_pb2 as _datetime_pb2
from google.type import latlng_pb2 as _latlng_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LookupCurrentConditionsRequest(_message.Message):
    __slots__ = ('location', 'units_system', 'language_code')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    UNITS_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    location: _latlng_pb2.LatLng
    units_system: _units_system_pb2.UnitsSystem
    language_code: str

    def __init__(self, location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., units_system: _Optional[_Union[_units_system_pb2.UnitsSystem, str]]=..., language_code: _Optional[str]=...) -> None:
        ...

class LookupCurrentConditionsResponse(_message.Message):
    __slots__ = ('current_time', 'time_zone', 'is_daytime', 'weather_condition', 'temperature', 'feels_like_temperature', 'dew_point', 'heat_index', 'wind_chill', 'relative_humidity', 'uv_index', 'precipitation', 'thunderstorm_probability', 'air_pressure', 'wind', 'visibility', 'cloud_cover', 'current_conditions_history')

    class CurrentConditionsHistory(_message.Message):
        __slots__ = ('temperature_change', 'max_temperature', 'min_temperature', 'snow_qpf', 'qpf')
        TEMPERATURE_CHANGE_FIELD_NUMBER: _ClassVar[int]
        MAX_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
        MIN_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
        SNOW_QPF_FIELD_NUMBER: _ClassVar[int]
        QPF_FIELD_NUMBER: _ClassVar[int]
        temperature_change: _temperature_pb2.Temperature
        max_temperature: _temperature_pb2.Temperature
        min_temperature: _temperature_pb2.Temperature
        snow_qpf: _precipitation_pb2.QuantitativePrecipitationForecast
        qpf: _precipitation_pb2.QuantitativePrecipitationForecast

        def __init__(self, temperature_change: _Optional[_Union[_temperature_pb2.Temperature, _Mapping]]=..., max_temperature: _Optional[_Union[_temperature_pb2.Temperature, _Mapping]]=..., min_temperature: _Optional[_Union[_temperature_pb2.Temperature, _Mapping]]=..., snow_qpf: _Optional[_Union[_precipitation_pb2.QuantitativePrecipitationForecast, _Mapping]]=..., qpf: _Optional[_Union[_precipitation_pb2.QuantitativePrecipitationForecast, _Mapping]]=...) -> None:
            ...
    CURRENT_TIME_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    IS_DAYTIME_FIELD_NUMBER: _ClassVar[int]
    WEATHER_CONDITION_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    FEELS_LIKE_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    DEW_POINT_FIELD_NUMBER: _ClassVar[int]
    HEAT_INDEX_FIELD_NUMBER: _ClassVar[int]
    WIND_CHILL_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    UV_INDEX_FIELD_NUMBER: _ClassVar[int]
    PRECIPITATION_FIELD_NUMBER: _ClassVar[int]
    THUNDERSTORM_PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    AIR_PRESSURE_FIELD_NUMBER: _ClassVar[int]
    WIND_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    CLOUD_COVER_FIELD_NUMBER: _ClassVar[int]
    CURRENT_CONDITIONS_HISTORY_FIELD_NUMBER: _ClassVar[int]
    current_time: _timestamp_pb2.Timestamp
    time_zone: _datetime_pb2.TimeZone
    is_daytime: bool
    weather_condition: _weather_condition_pb2.WeatherCondition
    temperature: _temperature_pb2.Temperature
    feels_like_temperature: _temperature_pb2.Temperature
    dew_point: _temperature_pb2.Temperature
    heat_index: _temperature_pb2.Temperature
    wind_chill: _temperature_pb2.Temperature
    relative_humidity: int
    uv_index: int
    precipitation: _precipitation_pb2.Precipitation
    thunderstorm_probability: int
    air_pressure: _air_pressure_pb2.AirPressure
    wind: _wind_pb2.Wind
    visibility: _visibility_pb2.Visibility
    cloud_cover: int
    current_conditions_history: LookupCurrentConditionsResponse.CurrentConditionsHistory

    def __init__(self, current_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., time_zone: _Optional[_Union[_datetime_pb2.TimeZone, _Mapping]]=..., is_daytime: bool=..., weather_condition: _Optional[_Union[_weather_condition_pb2.WeatherCondition, _Mapping]]=..., temperature: _Optional[_Union[_temperature_pb2.Temperature, _Mapping]]=..., feels_like_temperature: _Optional[_Union[_temperature_pb2.Temperature, _Mapping]]=..., dew_point: _Optional[_Union[_temperature_pb2.Temperature, _Mapping]]=..., heat_index: _Optional[_Union[_temperature_pb2.Temperature, _Mapping]]=..., wind_chill: _Optional[_Union[_temperature_pb2.Temperature, _Mapping]]=..., relative_humidity: _Optional[int]=..., uv_index: _Optional[int]=..., precipitation: _Optional[_Union[_precipitation_pb2.Precipitation, _Mapping]]=..., thunderstorm_probability: _Optional[int]=..., air_pressure: _Optional[_Union[_air_pressure_pb2.AirPressure, _Mapping]]=..., wind: _Optional[_Union[_wind_pb2.Wind, _Mapping]]=..., visibility: _Optional[_Union[_visibility_pb2.Visibility, _Mapping]]=..., cloud_cover: _Optional[int]=..., current_conditions_history: _Optional[_Union[LookupCurrentConditionsResponse.CurrentConditionsHistory, _Mapping]]=...) -> None:
        ...

class LookupForecastHoursRequest(_message.Message):
    __slots__ = ('location', 'hours', 'units_system', 'language_code', 'page_size', 'page_token')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    UNITS_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    location: _latlng_pb2.LatLng
    hours: int
    units_system: _units_system_pb2.UnitsSystem
    language_code: str
    page_size: int
    page_token: str

    def __init__(self, location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., hours: _Optional[int]=..., units_system: _Optional[_Union[_units_system_pb2.UnitsSystem, str]]=..., language_code: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class LookupForecastHoursResponse(_message.Message):
    __slots__ = ('forecast_hours', 'time_zone', 'next_page_token')
    FORECAST_HOURS_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    forecast_hours: _containers.RepeatedCompositeFieldContainer[_forecast_hour_pb2.ForecastHour]
    time_zone: _datetime_pb2.TimeZone
    next_page_token: str

    def __init__(self, forecast_hours: _Optional[_Iterable[_Union[_forecast_hour_pb2.ForecastHour, _Mapping]]]=..., time_zone: _Optional[_Union[_datetime_pb2.TimeZone, _Mapping]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class LookupForecastDaysRequest(_message.Message):
    __slots__ = ('location', 'days', 'units_system', 'language_code', 'page_size', 'page_token')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    UNITS_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    location: _latlng_pb2.LatLng
    days: int
    units_system: _units_system_pb2.UnitsSystem
    language_code: str
    page_size: int
    page_token: str

    def __init__(self, location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., days: _Optional[int]=..., units_system: _Optional[_Union[_units_system_pb2.UnitsSystem, str]]=..., language_code: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class LookupForecastDaysResponse(_message.Message):
    __slots__ = ('forecast_days', 'time_zone', 'next_page_token')
    FORECAST_DAYS_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    forecast_days: _containers.RepeatedCompositeFieldContainer[_forecast_day_pb2.ForecastDay]
    time_zone: _datetime_pb2.TimeZone
    next_page_token: str

    def __init__(self, forecast_days: _Optional[_Iterable[_Union[_forecast_day_pb2.ForecastDay, _Mapping]]]=..., time_zone: _Optional[_Union[_datetime_pb2.TimeZone, _Mapping]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class LookupHistoryHoursRequest(_message.Message):
    __slots__ = ('location', 'hours', 'units_system', 'language_code', 'page_size', 'page_token')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    HOURS_FIELD_NUMBER: _ClassVar[int]
    UNITS_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    location: _latlng_pb2.LatLng
    hours: int
    units_system: _units_system_pb2.UnitsSystem
    language_code: str
    page_size: int
    page_token: str

    def __init__(self, location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., hours: _Optional[int]=..., units_system: _Optional[_Union[_units_system_pb2.UnitsSystem, str]]=..., language_code: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class LookupHistoryHoursResponse(_message.Message):
    __slots__ = ('history_hours', 'time_zone', 'next_page_token')
    HISTORY_HOURS_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    history_hours: _containers.RepeatedCompositeFieldContainer[_history_hour_pb2.HistoryHour]
    time_zone: _datetime_pb2.TimeZone
    next_page_token: str

    def __init__(self, history_hours: _Optional[_Iterable[_Union[_history_hour_pb2.HistoryHour, _Mapping]]]=..., time_zone: _Optional[_Union[_datetime_pb2.TimeZone, _Mapping]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class LookupPublicAlertsRequest(_message.Message):
    __slots__ = ('location', 'language_code', 'page_size', 'page_token')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    location: _latlng_pb2.LatLng
    language_code: str
    page_size: int
    page_token: str

    def __init__(self, location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]]=..., language_code: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class LookupPublicAlertsResponse(_message.Message):
    __slots__ = ('weather_alerts', 'region_code', 'next_page_token')
    WEATHER_ALERTS_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    weather_alerts: _containers.RepeatedCompositeFieldContainer[_public_alerts_pb2.PublicAlerts]
    region_code: str
    next_page_token: str

    def __init__(self, weather_alerts: _Optional[_Iterable[_Union[_public_alerts_pb2.PublicAlerts, _Mapping]]]=..., region_code: _Optional[str]=..., next_page_token: _Optional[str]=...) -> None:
        ...