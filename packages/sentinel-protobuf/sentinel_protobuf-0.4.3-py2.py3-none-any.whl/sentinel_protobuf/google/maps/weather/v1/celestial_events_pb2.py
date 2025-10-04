"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/maps/weather/v1/celestial_events.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/maps/weather/v1/celestial_events.proto\x12\x16google.maps.weather.v1\x1a\x1fgoogle/protobuf/timestamp.proto"n\n\tSunEvents\x120\n\x0csunrise_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bsunset_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xaa\x01\n\nMoonEvents\x122\n\x0emoonrise_times\x18\x04 \x03(\x0b2\x1a.google.protobuf.Timestamp\x121\n\rmoonset_times\x18\x05 \x03(\x0b2\x1a.google.protobuf.Timestamp\x125\n\nmoon_phase\x18\x03 \x01(\x0e2!.google.maps.weather.v1.MoonPhase*\xbb\x01\n\tMoonPhase\x12\x1a\n\x16MOON_PHASE_UNSPECIFIED\x10\x00\x12\x0c\n\x08NEW_MOON\x10\x01\x12\x13\n\x0fWAXING_CRESCENT\x10\x02\x12\x11\n\rFIRST_QUARTER\x10\x03\x12\x12\n\x0eWAXING_GIBBOUS\x10\x04\x12\r\n\tFULL_MOON\x10\x05\x12\x12\n\x0eWANING_GIBBOUS\x10\x06\x12\x10\n\x0cLAST_QUARTER\x10\x07\x12\x13\n\x0fWANING_CRESCENT\x10\x08B\xa8\x01\n\x1acom.google.maps.weather.v1B\x14CelestialEventsProtoP\x01Z:cloud.google.com/go/maps/weather/apiv1/weatherpb;weatherpb\xa2\x02\x05GMWV1\xaa\x02\x15Google.Geo.Weather.V1\xca\x02\x15Google\\Geo\\Weather\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.weather.v1.celestial_events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.weather.v1B\x14CelestialEventsProtoP\x01Z:cloud.google.com/go/maps/weather/apiv1/weatherpb;weatherpb\xa2\x02\x05GMWV1\xaa\x02\x15Google.Geo.Weather.V1\xca\x02\x15Google\\Geo\\Weather\\V1'
    _globals['_MOONPHASE']._serialized_start = 392
    _globals['_MOONPHASE']._serialized_end = 579
    _globals['_SUNEVENTS']._serialized_start = 106
    _globals['_SUNEVENTS']._serialized_end = 216
    _globals['_MOONEVENTS']._serialized_start = 219
    _globals['_MOONEVENTS']._serialized_end = 389