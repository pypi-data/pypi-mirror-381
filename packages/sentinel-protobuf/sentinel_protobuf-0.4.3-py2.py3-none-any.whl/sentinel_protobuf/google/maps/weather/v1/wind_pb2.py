"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/maps/weather/v1/wind.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!google/maps/weather/v1/wind.proto\x12\x16google.maps.weather.v1"\xa3\x01\n\x04Wind\x128\n\tdirection\x18\x01 \x01(\x0b2%.google.maps.weather.v1.WindDirection\x120\n\x05speed\x18\x02 \x01(\x0b2!.google.maps.weather.v1.WindSpeed\x12/\n\x04gust\x18\x03 \x01(\x0b2!.google.maps.weather.v1.WindSpeed"n\n\rWindDirection\x12\x14\n\x07degrees\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12;\n\x08cardinal\x18\x02 \x01(\x0e2).google.maps.weather.v1.CardinalDirectionB\n\n\x08_degrees"Z\n\tWindSpeed\x12\x12\n\x05value\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12/\n\x04unit\x18\x02 \x01(\x0e2!.google.maps.weather.v1.SpeedUnitB\x08\n\x06_value*\xc1\x02\n\x11CardinalDirection\x12"\n\x1eCARDINAL_DIRECTION_UNSPECIFIED\x10\x00\x12\t\n\x05NORTH\x10\x01\x12\x13\n\x0fNORTH_NORTHEAST\x10\x02\x12\r\n\tNORTHEAST\x10\x03\x12\x12\n\x0eEAST_NORTHEAST\x10\x04\x12\x08\n\x04EAST\x10\x05\x12\x12\n\x0eEAST_SOUTHEAST\x10\x06\x12\r\n\tSOUTHEAST\x10\x07\x12\x13\n\x0fSOUTH_SOUTHEAST\x10\x08\x12\t\n\x05SOUTH\x10\t\x12\x13\n\x0fSOUTH_SOUTHWEST\x10\n\x12\r\n\tSOUTHWEST\x10\x0b\x12\x12\n\x0eWEST_SOUTHWEST\x10\x0c\x12\x08\n\x04WEST\x10\r\x12\x12\n\x0eWEST_NORTHWEST\x10\x0e\x12\r\n\tNORTHWEST\x10\x0f\x12\x13\n\x0fNORTH_NORTHWEST\x10\x10*T\n\tSpeedUnit\x12\x1a\n\x16SPEED_UNIT_UNSPECIFIED\x10\x00\x12\x17\n\x13KILOMETERS_PER_HOUR\x10\x01\x12\x12\n\x0eMILES_PER_HOUR\x10\x02B\x9d\x01\n\x1acom.google.maps.weather.v1B\tWindProtoP\x01Z:cloud.google.com/go/maps/weather/apiv1/weatherpb;weatherpb\xa2\x02\x05GMWV1\xaa\x02\x15Google.Geo.Weather.V1\xca\x02\x15Google\\Geo\\Weather\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.weather.v1.wind_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.weather.v1B\tWindProtoP\x01Z:cloud.google.com/go/maps/weather/apiv1/weatherpb;weatherpb\xa2\x02\x05GMWV1\xaa\x02\x15Google.Geo.Weather.V1\xca\x02\x15Google\\Geo\\Weather\\V1'
    _globals['_CARDINALDIRECTION']._serialized_start = 432
    _globals['_CARDINALDIRECTION']._serialized_end = 753
    _globals['_SPEEDUNIT']._serialized_start = 755
    _globals['_SPEEDUNIT']._serialized_end = 839
    _globals['_WIND']._serialized_start = 62
    _globals['_WIND']._serialized_end = 225
    _globals['_WINDDIRECTION']._serialized_start = 227
    _globals['_WINDDIRECTION']._serialized_end = 337
    _globals['_WINDSPEED']._serialized_start = 339
    _globals['_WINDSPEED']._serialized_end = 429