"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/maps/weather/v1/weather_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.maps.weather.v1 import air_pressure_pb2 as google_dot_maps_dot_weather_dot_v1_dot_air__pressure__pb2
from .....google.maps.weather.v1 import forecast_day_pb2 as google_dot_maps_dot_weather_dot_v1_dot_forecast__day__pb2
from .....google.maps.weather.v1 import forecast_hour_pb2 as google_dot_maps_dot_weather_dot_v1_dot_forecast__hour__pb2
from .....google.maps.weather.v1 import history_hour_pb2 as google_dot_maps_dot_weather_dot_v1_dot_history__hour__pb2
from .....google.maps.weather.v1 import precipitation_pb2 as google_dot_maps_dot_weather_dot_v1_dot_precipitation__pb2
from .....google.maps.weather.v1 import public_alerts_pb2 as google_dot_maps_dot_weather_dot_v1_dot_public__alerts__pb2
from .....google.maps.weather.v1 import temperature_pb2 as google_dot_maps_dot_weather_dot_v1_dot_temperature__pb2
from .....google.maps.weather.v1 import units_system_pb2 as google_dot_maps_dot_weather_dot_v1_dot_units__system__pb2
from .....google.maps.weather.v1 import visibility_pb2 as google_dot_maps_dot_weather_dot_v1_dot_visibility__pb2
from .....google.maps.weather.v1 import weather_condition_pb2 as google_dot_maps_dot_weather_dot_v1_dot_weather__condition__pb2
from .....google.maps.weather.v1 import wind_pb2 as google_dot_maps_dot_weather_dot_v1_dot_wind__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import datetime_pb2 as google_dot_type_dot_datetime__pb2
from .....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/maps/weather/v1/weather_service.proto\x12\x16google.maps.weather.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a)google/maps/weather/v1/air_pressure.proto\x1a)google/maps/weather/v1/forecast_day.proto\x1a*google/maps/weather/v1/forecast_hour.proto\x1a)google/maps/weather/v1/history_hour.proto\x1a*google/maps/weather/v1/precipitation.proto\x1a*google/maps/weather/v1/public_alerts.proto\x1a(google/maps/weather/v1/temperature.proto\x1a)google/maps/weather/v1/units_system.proto\x1a\'google/maps/weather/v1/visibility.proto\x1a.google/maps/weather/v1/weather_condition.proto\x1a!google/maps/weather/v1/wind.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoogle/type/datetime.proto\x1a\x18google/type/latlng.proto"\xbf\x01\n\x1eLookupCurrentConditionsRequest\x12*\n\x08location\x18\x01 \x01(\x0b2\x13.google.type.LatLngB\x03\xe0A\x02\x12>\n\x0cunits_system\x18\x02 \x01(\x0e2#.google.maps.weather.v1.UnitsSystemB\x03\xe0A\x01\x12\x1f\n\rlanguage_code\x18\x03 \x01(\tB\x03\xe0A\x01H\x00\x88\x01\x01B\x10\n\x0e_language_code"\x9d\x0b\n\x1fLookupCurrentConditionsResponse\x120\n\x0ccurrent_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12(\n\ttime_zone\x18\x02 \x01(\x0b2\x15.google.type.TimeZone\x12\x17\n\nis_daytime\x18\x03 \x01(\x08H\x00\x88\x01\x01\x12C\n\x11weather_condition\x18\x04 \x01(\x0b2(.google.maps.weather.v1.WeatherCondition\x128\n\x0btemperature\x18\x05 \x01(\x0b2#.google.maps.weather.v1.Temperature\x12C\n\x16feels_like_temperature\x18\x06 \x01(\x0b2#.google.maps.weather.v1.Temperature\x126\n\tdew_point\x18\x07 \x01(\x0b2#.google.maps.weather.v1.Temperature\x127\n\nheat_index\x18\x08 \x01(\x0b2#.google.maps.weather.v1.Temperature\x127\n\nwind_chill\x18\t \x01(\x0b2#.google.maps.weather.v1.Temperature\x12\x1e\n\x11relative_humidity\x18\n \x01(\x05H\x01\x88\x01\x01\x12\x15\n\x08uv_index\x18\x0b \x01(\x05H\x02\x88\x01\x01\x12<\n\rprecipitation\x18\x0c \x01(\x0b2%.google.maps.weather.v1.Precipitation\x12%\n\x18thunderstorm_probability\x18\r \x01(\x05H\x03\x88\x01\x01\x129\n\x0cair_pressure\x18\x0e \x01(\x0b2#.google.maps.weather.v1.AirPressure\x12*\n\x04wind\x18\x0f \x01(\x0b2\x1c.google.maps.weather.v1.Wind\x126\n\nvisibility\x18\x10 \x01(\x0b2".google.maps.weather.v1.Visibility\x12\x18\n\x0bcloud_cover\x18\x11 \x01(\x05H\x04\x88\x01\x01\x12t\n\x1acurrent_conditions_history\x18\x12 \x01(\x0b2P.google.maps.weather.v1.LookupCurrentConditionsResponse.CurrentConditionsHistory\x1a\xec\x02\n\x18CurrentConditionsHistory\x12?\n\x12temperature_change\x18\x01 \x01(\x0b2#.google.maps.weather.v1.Temperature\x12<\n\x0fmax_temperature\x18\x02 \x01(\x0b2#.google.maps.weather.v1.Temperature\x12<\n\x0fmin_temperature\x18\x03 \x01(\x0b2#.google.maps.weather.v1.Temperature\x12K\n\x08snow_qpf\x18\x05 \x01(\x0b29.google.maps.weather.v1.QuantitativePrecipitationForecast\x12F\n\x03qpf\x18\x06 \x01(\x0b29.google.maps.weather.v1.QuantitativePrecipitationForecastB\r\n\x0b_is_daytimeB\x14\n\x12_relative_humidityB\x0b\n\t_uv_indexB\x1b\n\x19_thunderstorm_probabilityB\x0e\n\x0c_cloud_cover"\x8f\x02\n\x1aLookupForecastHoursRequest\x12*\n\x08location\x18\x01 \x01(\x0b2\x13.google.type.LatLngB\x03\xe0A\x02\x12\x17\n\x05hours\x18\x02 \x01(\x05B\x03\xe0A\x01H\x00\x88\x01\x01\x12>\n\x0cunits_system\x18\x03 \x01(\x0e2#.google.maps.weather.v1.UnitsSystemB\x03\xe0A\x01\x12\x1f\n\rlanguage_code\x18\x04 \x01(\tB\x03\xe0A\x01H\x01\x88\x01\x01\x12\x16\n\tpage_size\x18\x05 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x06 \x01(\tB\x03\xe0A\x01B\x08\n\x06_hoursB\x10\n\x0e_language_code"\x9e\x01\n\x1bLookupForecastHoursResponse\x12<\n\x0eforecast_hours\x18\x01 \x03(\x0b2$.google.maps.weather.v1.ForecastHour\x12(\n\ttime_zone\x18\x02 \x01(\x0b2\x15.google.type.TimeZone\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t"\x8c\x02\n\x19LookupForecastDaysRequest\x12*\n\x08location\x18\x01 \x01(\x0b2\x13.google.type.LatLngB\x03\xe0A\x02\x12\x16\n\x04days\x18\x02 \x01(\x05B\x03\xe0A\x01H\x00\x88\x01\x01\x12>\n\x0cunits_system\x18\x03 \x01(\x0e2#.google.maps.weather.v1.UnitsSystemB\x03\xe0A\x01\x12\x1f\n\rlanguage_code\x18\x04 \x01(\tB\x03\xe0A\x01H\x01\x88\x01\x01\x12\x16\n\tpage_size\x18\x05 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x06 \x01(\tB\x03\xe0A\x01B\x07\n\x05_daysB\x10\n\x0e_language_code"\x9b\x01\n\x1aLookupForecastDaysResponse\x12:\n\rforecast_days\x18\x01 \x03(\x0b2#.google.maps.weather.v1.ForecastDay\x12(\n\ttime_zone\x18\x02 \x01(\x0b2\x15.google.type.TimeZone\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t"\x8e\x02\n\x19LookupHistoryHoursRequest\x12*\n\x08location\x18\x01 \x01(\x0b2\x13.google.type.LatLngB\x03\xe0A\x02\x12\x17\n\x05hours\x18\x02 \x01(\x05B\x03\xe0A\x01H\x00\x88\x01\x01\x12>\n\x0cunits_system\x18\x03 \x01(\x0e2#.google.maps.weather.v1.UnitsSystemB\x03\xe0A\x01\x12\x1f\n\rlanguage_code\x18\x04 \x01(\tB\x03\xe0A\x01H\x01\x88\x01\x01\x12\x16\n\tpage_size\x18\x05 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x06 \x01(\tB\x03\xe0A\x01B\x08\n\x06_hoursB\x10\n\x0e_language_code"\x9b\x01\n\x1aLookupHistoryHoursResponse\x12:\n\rhistory_hours\x18\x01 \x03(\x0b2#.google.maps.weather.v1.HistoryHour\x12(\n\ttime_zone\x18\x02 \x01(\x0b2\x15.google.type.TimeZone\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t"\xab\x01\n\x19LookupPublicAlertsRequest\x12*\n\x08location\x18\x01 \x01(\x0b2\x13.google.type.LatLngB\x03\xe0A\x02\x12\x1f\n\rlanguage_code\x18\x02 \x01(\tB\x03\xe0A\x01H\x00\x88\x01\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01B\x10\n\x0e_language_code"\x88\x01\n\x1aLookupPublicAlertsResponse\x12<\n\x0eweather_alerts\x18\x01 \x03(\x0b2$.google.maps.weather.v1.PublicAlerts\x12\x13\n\x0bregion_code\x18\x02 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t2\x8b\x07\n\x07Weather\x12\xb0\x01\n\x17LookupCurrentConditions\x126.google.maps.weather.v1.LookupCurrentConditionsRequest\x1a7.google.maps.weather.v1.LookupCurrentConditionsResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/currentConditions:lookup\x12\xa1\x01\n\x13LookupForecastHours\x122.google.maps.weather.v1.LookupForecastHoursRequest\x1a3.google.maps.weather.v1.LookupForecastHoursResponse"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/forecast/hours:lookup\x12\x9d\x01\n\x12LookupForecastDays\x121.google.maps.weather.v1.LookupForecastDaysRequest\x1a2.google.maps.weather.v1.LookupForecastDaysResponse" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/forecast/days:lookup\x12\x9d\x01\n\x12LookupHistoryHours\x121.google.maps.weather.v1.LookupHistoryHoursRequest\x1a2.google.maps.weather.v1.LookupHistoryHoursResponse" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/history/hours:lookup\x12\x9c\x01\n\x12LookupPublicAlerts\x121.google.maps.weather.v1.LookupPublicAlertsRequest\x1a2.google.maps.weather.v1.LookupPublicAlertsResponse"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/publicAlerts:lookup\x1aJ\xcaA\x16weather.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa7\x01\n\x1acom.google.maps.weather.v1B\x13WeatherServiceProtoP\x01Z:cloud.google.com/go/maps/weather/apiv1/weatherpb;weatherpb\xa2\x02\x05GMWV1\xaa\x02\x15Google.Geo.Weather.V1\xca\x02\x15Google\\Geo\\Weather\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.weather.v1.weather_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.weather.v1B\x13WeatherServiceProtoP\x01Z:cloud.google.com/go/maps/weather/apiv1/weatherpb;weatherpb\xa2\x02\x05GMWV1\xaa\x02\x15Google.Geo.Weather.V1\xca\x02\x15Google\\Geo\\Weather\\V1'
    _globals['_LOOKUPCURRENTCONDITIONSREQUEST'].fields_by_name['location']._loaded_options = None
    _globals['_LOOKUPCURRENTCONDITIONSREQUEST'].fields_by_name['location']._serialized_options = b'\xe0A\x02'
    _globals['_LOOKUPCURRENTCONDITIONSREQUEST'].fields_by_name['units_system']._loaded_options = None
    _globals['_LOOKUPCURRENTCONDITIONSREQUEST'].fields_by_name['units_system']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKUPCURRENTCONDITIONSREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_LOOKUPCURRENTCONDITIONSREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKUPFORECASTHOURSREQUEST'].fields_by_name['location']._loaded_options = None
    _globals['_LOOKUPFORECASTHOURSREQUEST'].fields_by_name['location']._serialized_options = b'\xe0A\x02'
    _globals['_LOOKUPFORECASTHOURSREQUEST'].fields_by_name['hours']._loaded_options = None
    _globals['_LOOKUPFORECASTHOURSREQUEST'].fields_by_name['hours']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKUPFORECASTHOURSREQUEST'].fields_by_name['units_system']._loaded_options = None
    _globals['_LOOKUPFORECASTHOURSREQUEST'].fields_by_name['units_system']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKUPFORECASTHOURSREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_LOOKUPFORECASTHOURSREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKUPFORECASTHOURSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LOOKUPFORECASTHOURSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKUPFORECASTHOURSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LOOKUPFORECASTHOURSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKUPFORECASTDAYSREQUEST'].fields_by_name['location']._loaded_options = None
    _globals['_LOOKUPFORECASTDAYSREQUEST'].fields_by_name['location']._serialized_options = b'\xe0A\x02'
    _globals['_LOOKUPFORECASTDAYSREQUEST'].fields_by_name['days']._loaded_options = None
    _globals['_LOOKUPFORECASTDAYSREQUEST'].fields_by_name['days']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKUPFORECASTDAYSREQUEST'].fields_by_name['units_system']._loaded_options = None
    _globals['_LOOKUPFORECASTDAYSREQUEST'].fields_by_name['units_system']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKUPFORECASTDAYSREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_LOOKUPFORECASTDAYSREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKUPFORECASTDAYSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LOOKUPFORECASTDAYSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKUPFORECASTDAYSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LOOKUPFORECASTDAYSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKUPHISTORYHOURSREQUEST'].fields_by_name['location']._loaded_options = None
    _globals['_LOOKUPHISTORYHOURSREQUEST'].fields_by_name['location']._serialized_options = b'\xe0A\x02'
    _globals['_LOOKUPHISTORYHOURSREQUEST'].fields_by_name['hours']._loaded_options = None
    _globals['_LOOKUPHISTORYHOURSREQUEST'].fields_by_name['hours']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKUPHISTORYHOURSREQUEST'].fields_by_name['units_system']._loaded_options = None
    _globals['_LOOKUPHISTORYHOURSREQUEST'].fields_by_name['units_system']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKUPHISTORYHOURSREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_LOOKUPHISTORYHOURSREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKUPHISTORYHOURSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LOOKUPHISTORYHOURSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKUPHISTORYHOURSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LOOKUPHISTORYHOURSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKUPPUBLICALERTSREQUEST'].fields_by_name['location']._loaded_options = None
    _globals['_LOOKUPPUBLICALERTSREQUEST'].fields_by_name['location']._serialized_options = b'\xe0A\x02'
    _globals['_LOOKUPPUBLICALERTSREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_LOOKUPPUBLICALERTSREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKUPPUBLICALERTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LOOKUPPUBLICALERTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKUPPUBLICALERTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LOOKUPPUBLICALERTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_WEATHER']._loaded_options = None
    _globals['_WEATHER']._serialized_options = b'\xcaA\x16weather.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_WEATHER'].methods_by_name['LookupCurrentConditions']._loaded_options = None
    _globals['_WEATHER'].methods_by_name['LookupCurrentConditions']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/currentConditions:lookup'
    _globals['_WEATHER'].methods_by_name['LookupForecastHours']._loaded_options = None
    _globals['_WEATHER'].methods_by_name['LookupForecastHours']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/forecast/hours:lookup'
    _globals['_WEATHER'].methods_by_name['LookupForecastDays']._loaded_options = None
    _globals['_WEATHER'].methods_by_name['LookupForecastDays']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/forecast/days:lookup'
    _globals['_WEATHER'].methods_by_name['LookupHistoryHours']._loaded_options = None
    _globals['_WEATHER'].methods_by_name['LookupHistoryHours']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/history/hours:lookup'
    _globals['_WEATHER'].methods_by_name['LookupPublicAlerts']._loaded_options = None
    _globals['_WEATHER'].methods_by_name['LookupPublicAlerts']._serialized_options = b'\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/publicAlerts:lookup'
    _globals['_LOOKUPCURRENTCONDITIONSREQUEST']._serialized_start = 718
    _globals['_LOOKUPCURRENTCONDITIONSREQUEST']._serialized_end = 909
    _globals['_LOOKUPCURRENTCONDITIONSRESPONSE']._serialized_start = 912
    _globals['_LOOKUPCURRENTCONDITIONSRESPONSE']._serialized_end = 2349
    _globals['_LOOKUPCURRENTCONDITIONSRESPONSE_CURRENTCONDITIONSHISTORY']._serialized_start = 1890
    _globals['_LOOKUPCURRENTCONDITIONSRESPONSE_CURRENTCONDITIONSHISTORY']._serialized_end = 2254
    _globals['_LOOKUPFORECASTHOURSREQUEST']._serialized_start = 2352
    _globals['_LOOKUPFORECASTHOURSREQUEST']._serialized_end = 2623
    _globals['_LOOKUPFORECASTHOURSRESPONSE']._serialized_start = 2626
    _globals['_LOOKUPFORECASTHOURSRESPONSE']._serialized_end = 2784
    _globals['_LOOKUPFORECASTDAYSREQUEST']._serialized_start = 2787
    _globals['_LOOKUPFORECASTDAYSREQUEST']._serialized_end = 3055
    _globals['_LOOKUPFORECASTDAYSRESPONSE']._serialized_start = 3058
    _globals['_LOOKUPFORECASTDAYSRESPONSE']._serialized_end = 3213
    _globals['_LOOKUPHISTORYHOURSREQUEST']._serialized_start = 3216
    _globals['_LOOKUPHISTORYHOURSREQUEST']._serialized_end = 3486
    _globals['_LOOKUPHISTORYHOURSRESPONSE']._serialized_start = 3489
    _globals['_LOOKUPHISTORYHOURSRESPONSE']._serialized_end = 3644
    _globals['_LOOKUPPUBLICALERTSREQUEST']._serialized_start = 3647
    _globals['_LOOKUPPUBLICALERTSREQUEST']._serialized_end = 3818
    _globals['_LOOKUPPUBLICALERTSRESPONSE']._serialized_start = 3821
    _globals['_LOOKUPPUBLICALERTSRESPONSE']._serialized_end = 3957
    _globals['_WEATHER']._serialized_start = 3960
    _globals['_WEATHER']._serialized_end = 4867