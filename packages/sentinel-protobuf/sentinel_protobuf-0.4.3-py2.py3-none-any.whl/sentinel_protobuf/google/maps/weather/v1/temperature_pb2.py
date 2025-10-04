"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/maps/weather/v1/temperature.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/maps/weather/v1/temperature.proto\x12\x16google.maps.weather.v1"f\n\x0bTemperature\x12\x14\n\x07degrees\x18\x01 \x01(\x02H\x00\x88\x01\x01\x125\n\x04unit\x18\x02 \x01(\x0e2\'.google.maps.weather.v1.TemperatureUnitB\n\n\x08_degrees*P\n\x0fTemperatureUnit\x12 \n\x1cTEMPERATURE_UNIT_UNSPECIFIED\x10\x00\x12\x0b\n\x07CELSIUS\x10\x01\x12\x0e\n\nFAHRENHEIT\x10\x02B\xa4\x01\n\x1acom.google.maps.weather.v1B\x10TemperatureProtoP\x01Z:cloud.google.com/go/maps/weather/apiv1/weatherpb;weatherpb\xa2\x02\x05GMWV1\xaa\x02\x15Google.Geo.Weather.V1\xca\x02\x15Google\\Geo\\Weather\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.weather.v1.temperature_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.weather.v1B\x10TemperatureProtoP\x01Z:cloud.google.com/go/maps/weather/apiv1/weatherpb;weatherpb\xa2\x02\x05GMWV1\xaa\x02\x15Google.Geo.Weather.V1\xca\x02\x15Google\\Geo\\Weather\\V1'
    _globals['_TEMPERATUREUNIT']._serialized_start = 172
    _globals['_TEMPERATUREUNIT']._serialized_end = 252
    _globals['_TEMPERATURE']._serialized_start = 68
    _globals['_TEMPERATURE']._serialized_end = 170