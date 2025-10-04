"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/maps/weather/v1/public_alerts.proto')
_sym_db = _symbol_database.Default()
from .....google.maps.weather.v1 import public_alerts_enums_pb2 as google_dot_maps_dot_weather_dot_v1_dot_public__alerts__enums__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import localized_text_pb2 as google_dot_type_dot_localized__text__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/maps/weather/v1/public_alerts.proto\x12\x16google.maps.weather.v1\x1a0google/maps/weather/v1/public_alerts_enums.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a google/type/localized_text.proto"g\n\nDataSource\x124\n\tpublisher\x18\x01 \x01(\x0e2!.google.maps.weather.v1.Publisher\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rauthority_uri\x18\x03 \x01(\t"K\n\x14SafetyRecommendation\x12\x11\n\tdirective\x18\x01 \x01(\t\x12\x14\n\x07subtext\x18\x02 \x01(\tH\x00\x88\x01\x01B\n\n\x08_subtext"\xc8\x05\n\x0cPublicAlerts\x12\x10\n\x08alert_id\x18\x01 \x01(\t\x12/\n\x0balert_title\x18\x02 \x01(\x0b2\x1a.google.type.LocalizedText\x12<\n\nevent_type\x18\x03 \x01(\x0e2(.google.maps.weather.v1.WeatherEventType\x12\x11\n\tarea_name\x18\x04 \x01(\t\x12\x14\n\x07polygon\x18\x05 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0bdescription\x18\x06 \x01(\tH\x01\x88\x01\x01\x122\n\x08severity\x18\x07 \x01(\x0e2 .google.maps.weather.v1.Severity\x129\n\tcertainty\x18\x08 \x01(\x0e2!.google.maps.weather.v1.CertaintyH\x02\x88\x01\x01\x125\n\x07urgency\x18\t \x01(\x0e2\x1f.google.maps.weather.v1.UrgencyH\x03\x88\x01\x01\x12\x13\n\x0binstruction\x18\n \x03(\t\x12L\n\x16safety_recommendations\x18\x0b \x03(\x0b2,.google.maps.weather.v1.SafetyRecommendation\x12\x17\n\x0ftimezone_offset\x18\x0c \x01(\t\x12.\n\nstart_time\x18\r \x01(\x0b2\x1a.google.protobuf.Timestamp\x123\n\x0fexpiration_time\x18\x0e \x01(\x0b2\x1a.google.protobuf.Timestamp\x127\n\x0bdata_source\x18\x0f \x01(\x0b2".google.maps.weather.v1.DataSourceB\n\n\x08_polygonB\x0e\n\x0c_descriptionB\x0c\n\n_certaintyB\n\n\x08_urgencyB\xa5\x01\n\x1acom.google.maps.weather.v1B\x11PublicAlertsProtoP\x01Z:cloud.google.com/go/maps/weather/apiv1/weatherpb;weatherpb\xa2\x02\x05GMWV1\xaa\x02\x15Google.Geo.Weather.V1\xca\x02\x15Google\\Geo\\Weather\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.weather.v1.public_alerts_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.maps.weather.v1B\x11PublicAlertsProtoP\x01Z:cloud.google.com/go/maps/weather/apiv1/weatherpb;weatherpb\xa2\x02\x05GMWV1\xaa\x02\x15Google.Geo.Weather.V1\xca\x02\x15Google\\Geo\\Weather\\V1'
    _globals['_DATASOURCE']._serialized_start = 187
    _globals['_DATASOURCE']._serialized_end = 290
    _globals['_SAFETYRECOMMENDATION']._serialized_start = 292
    _globals['_SAFETYRECOMMENDATION']._serialized_end = 367
    _globals['_PUBLICALERTS']._serialized_start = 370
    _globals['_PUBLICALERTS']._serialized_end = 1082