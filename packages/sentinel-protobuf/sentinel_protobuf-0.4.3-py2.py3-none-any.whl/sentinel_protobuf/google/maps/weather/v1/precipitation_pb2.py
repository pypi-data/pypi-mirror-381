"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/maps/weather/v1/precipitation.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/maps/weather/v1/precipitation.proto\x12\x16google.maps.weather.v1"\xeb\x01\n\rPrecipitation\x12E\n\x0bprobability\x18\x01 \x01(\x0b20.google.maps.weather.v1.PrecipitationProbability\x12K\n\x08snow_qpf\x18\x03 \x01(\x0b29.google.maps.weather.v1.QuantitativePrecipitationForecast\x12F\n\x03qpf\x18\x04 \x01(\x0b29.google.maps.weather.v1.QuantitativePrecipitationForecast"u\n\x18PrecipitationProbability\x12\x14\n\x07percent\x18\x01 \x01(\x05H\x00\x88\x01\x01\x127\n\x04type\x18\x02 \x01(\x0e2).google.maps.weather.v1.PrecipitationTypeB\n\n\x08_percent"\xd0\x01\n!QuantitativePrecipitationForecast\x12\x15\n\x08quantity\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12L\n\x04unit\x18\x02 \x01(\x0e2>.google.maps.weather.v1.QuantitativePrecipitationForecast.Unit"9\n\x04Unit\x12\x14\n\x10UNIT_UNSPECIFIED\x10\x00\x12\x0f\n\x0bMILLIMETERS\x10\x03\x12\n\n\x06INCHES\x10\x02B\x0b\n\t_quantity*\xa6\x01\n\x11PrecipitationType\x12"\n\x1ePRECIPITATION_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x08\x12\x08\n\x04SNOW\x10\x01\x12\x08\n\x04RAIN\x10\x02\x12\x0e\n\nLIGHT_RAIN\x10\x03\x12\x0e\n\nHEAVY_RAIN\x10\x04\x12\x11\n\rRAIN_AND_SNOW\x10\x05\x12\t\n\x05SLEET\x10\x06\x12\x11\n\rFREEZING_RAIN\x10\x07B\xa6\x01\n\x1acom.google.maps.weather.v1B\x12PrecipitationProtoP\x01Z:cloud.google.com/go/maps/weather/apiv1/weatherpb;weatherpb\xa2\x02\x05GMWV1\xaa\x02\x15Google.Geo.Weather.V1\xca\x02\x15Google\\Geo\\Weather\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.weather.v1.precipitation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.weather.v1B\x12PrecipitationProtoP\x01Z:cloud.google.com/go/maps/weather/apiv1/weatherpb;weatherpb\xa2\x02\x05GMWV1\xaa\x02\x15Google.Geo.Weather.V1\xca\x02\x15Google\\Geo\\Weather\\V1'
    _globals['_PRECIPITATIONTYPE']._serialized_start = 639
    _globals['_PRECIPITATIONTYPE']._serialized_end = 805
    _globals['_PRECIPITATION']._serialized_start = 71
    _globals['_PRECIPITATION']._serialized_end = 306
    _globals['_PRECIPITATIONPROBABILITY']._serialized_start = 308
    _globals['_PRECIPITATIONPROBABILITY']._serialized_end = 425
    _globals['_QUANTITATIVEPRECIPITATIONFORECAST']._serialized_start = 428
    _globals['_QUANTITATIVEPRECIPITATIONFORECAST']._serialized_end = 636
    _globals['_QUANTITATIVEPRECIPITATIONFORECAST_UNIT']._serialized_start = 566
    _globals['_QUANTITATIVEPRECIPITATIONFORECAST_UNIT']._serialized_end = 623