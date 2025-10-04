"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/maps/places/v1/address_descriptor.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.type import localized_text_pb2 as google_dot_type_dot_localized__text__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/maps/places/v1/address_descriptor.proto\x12\x15google.maps.places.v1\x1a\x19google/api/resource.proto\x1a google/type/localized_text.proto"\x96\x07\n\x11AddressDescriptor\x12D\n\tlandmarks\x18\x01 \x03(\x0b21.google.maps.places.v1.AddressDescriptor.Landmark\x12<\n\x05areas\x18\x02 \x03(\x0b2-.google.maps.places.v1.AddressDescriptor.Area\x1a\xde\x03\n\x08Landmark\x12.\n\x04name\x18\x01 \x01(\tB \xfaA\x1d\n\x1bplaces.googleapis.com/Place\x12\x10\n\x08place_id\x18\x02 \x01(\t\x120\n\x0cdisplay_name\x18\x03 \x01(\x0b2\x1a.google.type.LocalizedText\x12\r\n\x05types\x18\x04 \x03(\t\x12c\n\x14spatial_relationship\x18\x05 \x01(\x0e2E.google.maps.places.v1.AddressDescriptor.Landmark.SpatialRelationship\x12%\n\x1dstraight_line_distance_meters\x18\x06 \x01(\x02\x12#\n\x16travel_distance_meters\x18\x07 \x01(\x02H\x00\x88\x01\x01"\x82\x01\n\x13SpatialRelationship\x12\x08\n\x04NEAR\x10\x00\x12\n\n\x06WITHIN\x10\x01\x12\n\n\x06BESIDE\x10\x02\x12\x13\n\x0fACROSS_THE_ROAD\x10\x03\x12\x11\n\rDOWN_THE_ROAD\x10\x04\x12\x15\n\x11AROUND_THE_CORNER\x10\x05\x12\n\n\x06BEHIND\x10\x06B\x19\n\x17_travel_distance_meters\x1a\x9b\x02\n\x04Area\x12.\n\x04name\x18\x01 \x01(\tB \xfaA\x1d\n\x1bplaces.googleapis.com/Place\x12\x10\n\x08place_id\x18\x02 \x01(\t\x120\n\x0cdisplay_name\x18\x03 \x01(\x0b2\x1a.google.type.LocalizedText\x12N\n\x0bcontainment\x18\x04 \x01(\x0e29.google.maps.places.v1.AddressDescriptor.Area.Containment"O\n\x0bContainment\x12\x1b\n\x17CONTAINMENT_UNSPECIFIED\x10\x00\x12\n\n\x06WITHIN\x10\x01\x12\r\n\tOUTSKIRTS\x10\x02\x12\x08\n\x04NEAR\x10\x03B\xa7\x01\n\x19com.google.maps.places.v1B\x16AddressDescriptorProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.places.v1.address_descriptor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.maps.places.v1B\x16AddressDescriptorProtoP\x01Z7cloud.google.com/go/maps/places/apiv1/placespb;placespb\xa2\x02\x06GMPSV1\xaa\x02\x15Google.Maps.Places.V1\xca\x02\x15Google\\Maps\\Places\\V1'
    _globals['_ADDRESSDESCRIPTOR_LANDMARK'].fields_by_name['name']._loaded_options = None
    _globals['_ADDRESSDESCRIPTOR_LANDMARK'].fields_by_name['name']._serialized_options = b'\xfaA\x1d\n\x1bplaces.googleapis.com/Place'
    _globals['_ADDRESSDESCRIPTOR_AREA'].fields_by_name['name']._loaded_options = None
    _globals['_ADDRESSDESCRIPTOR_AREA'].fields_by_name['name']._serialized_options = b'\xfaA\x1d\n\x1bplaces.googleapis.com/Place'
    _globals['_ADDRESSDESCRIPTOR']._serialized_start = 135
    _globals['_ADDRESSDESCRIPTOR']._serialized_end = 1053
    _globals['_ADDRESSDESCRIPTOR_LANDMARK']._serialized_start = 289
    _globals['_ADDRESSDESCRIPTOR_LANDMARK']._serialized_end = 767
    _globals['_ADDRESSDESCRIPTOR_LANDMARK_SPATIALRELATIONSHIP']._serialized_start = 610
    _globals['_ADDRESSDESCRIPTOR_LANDMARK_SPATIALRELATIONSHIP']._serialized_end = 740
    _globals['_ADDRESSDESCRIPTOR_AREA']._serialized_start = 770
    _globals['_ADDRESSDESCRIPTOR_AREA']._serialized_end = 1053
    _globals['_ADDRESSDESCRIPTOR_AREA_CONTAINMENT']._serialized_start = 974
    _globals['_ADDRESSDESCRIPTOR_AREA_CONTAINMENT']._serialized_end = 1053