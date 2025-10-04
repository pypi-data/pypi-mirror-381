"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/maps/weather/v1/weather_condition.proto')
_sym_db = _symbol_database.Default()
from .....google.type import localized_text_pb2 as google_dot_type_dot_localized__text__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/maps/weather/v1/weather_condition.proto\x12\x16google.maps.weather.v1\x1a google/type/localized_text.proto"\xe8\x07\n\x10WeatherCondition\x12\x15\n\ricon_base_uri\x18\x01 \x01(\t\x12/\n\x0bdescription\x18\x02 \x01(\x0b2\x1a.google.type.LocalizedText\x12;\n\x04type\x18\x03 \x01(\x0e2-.google.maps.weather.v1.WeatherCondition.Type"\xce\x06\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05CLEAR\x10\x01\x12\x10\n\x0cMOSTLY_CLEAR\x10\x02\x12\x11\n\rPARTLY_CLOUDY\x10\x03\x12\x11\n\rMOSTLY_CLOUDY\x10\x04\x12\n\n\x06CLOUDY\x10\x05\x12\t\n\x05WINDY\x10\x06\x12\x11\n\rWIND_AND_RAIN\x10\x07\x12\x16\n\x12LIGHT_RAIN_SHOWERS\x10\x08\x12\x15\n\x11CHANCE_OF_SHOWERS\x10\t\x12\x15\n\x11SCATTERED_SHOWERS\x10\n\x12\x10\n\x0cRAIN_SHOWERS\x10\x0c\x12\x16\n\x12HEAVY_RAIN_SHOWERS\x10\r\x12\x1a\n\x16LIGHT_TO_MODERATE_RAIN\x10\x0e\x12\x1a\n\x16MODERATE_TO_HEAVY_RAIN\x10\x0f\x12\x08\n\x04RAIN\x10\x10\x12\x0e\n\nLIGHT_RAIN\x10\x11\x12\x0e\n\nHEAVY_RAIN\x10\x12\x12\x1b\n\x17RAIN_PERIODICALLY_HEAVY\x10\x13\x12\x16\n\x12LIGHT_SNOW_SHOWERS\x10\x14\x12\x1a\n\x16CHANCE_OF_SNOW_SHOWERS\x10\x15\x12\x1a\n\x16SCATTERED_SNOW_SHOWERS\x10\x16\x12\x10\n\x0cSNOW_SHOWERS\x10\x17\x12\x16\n\x12HEAVY_SNOW_SHOWERS\x10\x18\x12\x1a\n\x16LIGHT_TO_MODERATE_SNOW\x10\x19\x12\x1a\n\x16MODERATE_TO_HEAVY_SNOW\x10\x1a\x12\x08\n\x04SNOW\x10\x1b\x12\x0e\n\nLIGHT_SNOW\x10\x1c\x12\x0e\n\nHEAVY_SNOW\x10\x1d\x12\r\n\tSNOWSTORM\x10\x1e\x12\x1b\n\x17SNOW_PERIODICALLY_HEAVY\x10\x1f\x12\x14\n\x10HEAVY_SNOW_STORM\x10 \x12\x10\n\x0cBLOWING_SNOW\x10!\x12\x11\n\rRAIN_AND_SNOW\x10"\x12\x08\n\x04HAIL\x10#\x12\x10\n\x0cHAIL_SHOWERS\x10$\x12\x10\n\x0cTHUNDERSTORM\x10%\x12\x11\n\rTHUNDERSHOWER\x10&\x12\x1b\n\x17LIGHT_THUNDERSTORM_RAIN\x10\'\x12\x1b\n\x17SCATTERED_THUNDERSTORMS\x10(\x12\x16\n\x12HEAVY_THUNDERSTORM\x10)B\xa9\x01\n\x1acom.google.maps.weather.v1B\x15WeatherConditionProtoP\x01Z:cloud.google.com/go/maps/weather/apiv1/weatherpb;weatherpb\xa2\x02\x05GMWV1\xaa\x02\x15Google.Geo.Weather.V1\xca\x02\x15Google\\Geo\\Weather\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.weather.v1.weather_condition_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.weather.v1B\x15WeatherConditionProtoP\x01Z:cloud.google.com/go/maps/weather/apiv1/weatherpb;weatherpb\xa2\x02\x05GMWV1\xaa\x02\x15Google.Geo.Weather.V1\xca\x02\x15Google\\Geo\\Weather\\V1'
    _globals['_WEATHERCONDITION']._serialized_start = 109
    _globals['_WEATHERCONDITION']._serialized_end = 1109
    _globals['_WEATHERCONDITION_TYPE']._serialized_start = 263
    _globals['_WEATHERCONDITION_TYPE']._serialized_end = 1109