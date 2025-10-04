"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/maps/weather/v1/forecast_hour.proto')
_sym_db = _symbol_database.Default()
from .....google.maps.weather.v1 import air_pressure_pb2 as google_dot_maps_dot_weather_dot_v1_dot_air__pressure__pb2
from .....google.maps.weather.v1 import ice_pb2 as google_dot_maps_dot_weather_dot_v1_dot_ice__pb2
from .....google.maps.weather.v1 import precipitation_pb2 as google_dot_maps_dot_weather_dot_v1_dot_precipitation__pb2
from .....google.maps.weather.v1 import temperature_pb2 as google_dot_maps_dot_weather_dot_v1_dot_temperature__pb2
from .....google.maps.weather.v1 import visibility_pb2 as google_dot_maps_dot_weather_dot_v1_dot_visibility__pb2
from .....google.maps.weather.v1 import weather_condition_pb2 as google_dot_maps_dot_weather_dot_v1_dot_weather__condition__pb2
from .....google.maps.weather.v1 import wind_pb2 as google_dot_maps_dot_weather_dot_v1_dot_wind__pb2
from .....google.type import datetime_pb2 as google_dot_type_dot_datetime__pb2
from .....google.type import interval_pb2 as google_dot_type_dot_interval__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/maps/weather/v1/forecast_hour.proto\x12\x16google.maps.weather.v1\x1a)google/maps/weather/v1/air_pressure.proto\x1a google/maps/weather/v1/ice.proto\x1a*google/maps/weather/v1/precipitation.proto\x1a(google/maps/weather/v1/temperature.proto\x1a\'google/maps/weather/v1/visibility.proto\x1a.google/maps/weather/v1/weather_condition.proto\x1a!google/maps/weather/v1/wind.proto\x1a\x1agoogle/type/datetime.proto\x1a\x1agoogle/type/interval.proto"\xa4\x08\n\x0cForecastHour\x12\'\n\x08interval\x18\x01 \x01(\x0b2\x15.google.type.Interval\x120\n\x11display_date_time\x18\x02 \x01(\x0b2\x15.google.type.DateTime\x12\x17\n\nis_daytime\x18\x03 \x01(\x08H\x00\x88\x01\x01\x12C\n\x11weather_condition\x18\x04 \x01(\x0b2(.google.maps.weather.v1.WeatherCondition\x128\n\x0btemperature\x18\x05 \x01(\x0b2#.google.maps.weather.v1.Temperature\x12C\n\x16feels_like_temperature\x18\x06 \x01(\x0b2#.google.maps.weather.v1.Temperature\x126\n\tdew_point\x18\x07 \x01(\x0b2#.google.maps.weather.v1.Temperature\x127\n\nheat_index\x18\x08 \x01(\x0b2#.google.maps.weather.v1.Temperature\x127\n\nwind_chill\x18\t \x01(\x0b2#.google.maps.weather.v1.Temperature\x12A\n\x14wet_bulb_temperature\x18\n \x01(\x0b2#.google.maps.weather.v1.Temperature\x12\x1e\n\x11relative_humidity\x18\x0b \x01(\x05H\x01\x88\x01\x01\x12\x15\n\x08uv_index\x18\x0c \x01(\x05H\x02\x88\x01\x01\x12<\n\rprecipitation\x18\r \x01(\x0b2%.google.maps.weather.v1.Precipitation\x12%\n\x18thunderstorm_probability\x18\x0e \x01(\x05H\x03\x88\x01\x01\x129\n\x0cair_pressure\x18\x0f \x01(\x0b2#.google.maps.weather.v1.AirPressure\x12*\n\x04wind\x18\x10 \x01(\x0b2\x1c.google.maps.weather.v1.Wind\x126\n\nvisibility\x18\x11 \x01(\x0b2".google.maps.weather.v1.Visibility\x12\x18\n\x0bcloud_cover\x18\x12 \x01(\x05H\x04\x88\x01\x01\x12;\n\rice_thickness\x18\x13 \x01(\x0b2$.google.maps.weather.v1.IceThicknessB\r\n\x0b_is_daytimeB\x14\n\x12_relative_humidityB\x0b\n\t_uv_indexB\x1b\n\x19_thunderstorm_probabilityB\x0e\n\x0c_cloud_coverB\xa5\x01\n\x1acom.google.maps.weather.v1B\x11ForecastHourProtoP\x01Z:cloud.google.com/go/maps/weather/apiv1/weatherpb;weatherpb\xa2\x02\x05GMWV1\xaa\x02\x15Google.Geo.Weather.V1\xca\x02\x15Google\\Geo\\Weather\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.weather.v1.forecast_hour_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.weather.v1B\x11ForecastHourProtoP\x01Z:cloud.google.com/go/maps/weather/apiv1/weatherpb;weatherpb\xa2\x02\x05GMWV1\xaa\x02\x15Google.Geo.Weather.V1\xca\x02\x15Google\\Geo\\Weather\\V1'
    _globals['_FORECASTHOUR']._serialized_start = 414
    _globals['_FORECASTHOUR']._serialized_end = 1474