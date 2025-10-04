"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/maps/places/v1/ev_charging.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/maps/places/v1/ev_charging.proto\x12\x15google.maps.places.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\xb1\x03\n\x0fEVChargeOptions\x12\x17\n\x0fconnector_count\x18\x01 \x01(\x05\x12Z\n\x15connector_aggregation\x18\x02 \x03(\x0b2;.google.maps.places.v1.EVChargeOptions.ConnectorAggregation\x1a\xa8\x02\n\x14ConnectorAggregation\x124\n\x04type\x18\x01 \x01(\x0e2&.google.maps.places.v1.EVConnectorType\x12\x1a\n\x12max_charge_rate_kw\x18\x02 \x01(\x01\x12\r\n\x05count\x18\x03 \x01(\x05\x12\x1c\n\x0favailable_count\x18\x04 \x01(\x05H\x00\x88\x01\x01\x12!\n\x14out_of_service_count\x18\x05 \x01(\x05H\x01\x88\x01\x01\x12A\n\x1davailability_last_update_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x12\n\x10_available_countB\x17\n\x15_out_of_service_count*\x81\x03\n\x0fEVConnectorType\x12!\n\x1dEV_CONNECTOR_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17EV_CONNECTOR_TYPE_OTHER\x10\x01\x12\x1b\n\x17EV_CONNECTOR_TYPE_J1772\x10\x02\x12\x1c\n\x18EV_CONNECTOR_TYPE_TYPE_2\x10\x03\x12\x1d\n\x19EV_CONNECTOR_TYPE_CHADEMO\x10\x04\x12!\n\x1dEV_CONNECTOR_TYPE_CCS_COMBO_1\x10\x05\x12!\n\x1dEV_CONNECTOR_TYPE_CCS_COMBO_2\x10\x06\x12\x1b\n\x17EV_CONNECTOR_TYPE_TESLA\x10\x07\x12&\n"EV_CONNECTOR_TYPE_UNSPECIFIED_GB_T\x10\x08\x12-\n)EV_CONNECTOR_TYPE_UNSPECIFIED_WALL_OUTLET\x10\t\x12\x1a\n\x16EV_CONNECTOR_TYPE_NACS\x10\nB\xa0\x01\n\x19com.google.maps.places.v1B\x0fEvChargingProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.places.v1.ev_charging_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.maps.places.v1B\x0fEvChargingProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1'
    _globals['_EVCONNECTORTYPE']._serialized_start = 536
    _globals['_EVCONNECTORTYPE']._serialized_end = 921
    _globals['_EVCHARGEOPTIONS']._serialized_start = 100
    _globals['_EVCHARGEOPTIONS']._serialized_end = 533
    _globals['_EVCHARGEOPTIONS_CONNECTORAGGREGATION']._serialized_start = 237
    _globals['_EVCHARGEOPTIONS_CONNECTORAGGREGATION']._serialized_end = 533