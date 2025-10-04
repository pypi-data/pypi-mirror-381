"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/maps/regionlookup/v1alpha/region_identifier.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/maps/regionlookup/v1alpha/region_identifier.proto\x12 google.maps.regionlookup.v1alpha\x1a\x1fgoogle/api/field_behavior.proto"\xd9\x03\n\x10RegionIdentifier\x12\x0f\n\x05place\x18\x04 \x01(\tH\x00\x12\x13\n\tunit_code\x18\x05 \x01(\tH\x00\x12U\n\nplace_type\x18\x06 \x01(\x0e2<.google.maps.regionlookup.v1alpha.RegionIdentifier.PlaceTypeB\x03\xe0A\x02\x12\x15\n\rlanguage_code\x18\x07 \x01(\t\x12\x13\n\x0bregion_code\x18\x08 \x01(\t"\x8f\x02\n\tPlaceType\x12\x1a\n\x16PLACE_TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bPOSTAL_CODE\x10\x01\x12\x1f\n\x1bADMINISTRATIVE_AREA_LEVEL_1\x10\x02\x12\x1f\n\x1bADMINISTRATIVE_AREA_LEVEL_2\x10\x03\x12\x0c\n\x08LOCALITY\x10\x04\x12\x10\n\x0cNEIGHBORHOOD\x10\x05\x12\x0b\n\x07COUNTRY\x10\x06\x12\x0f\n\x0bSUBLOCALITY\x10\x07\x12\x1f\n\x1bADMINISTRATIVE_AREA_LEVEL_3\x10\x08\x12\x1f\n\x1bADMINISTRATIVE_AREA_LEVEL_4\x10\t\x12\x13\n\x0fSCHOOL_DISTRICT\x10\nB\n\n\x08locationB\xe1\x01\n$com.google.maps.regionlookup.v1alphaB\x15RegionIdentifierProtoP\x01ZNcloud.google.com/go/maps/regionlookup/apiv1alpha/regionlookuppb;regionlookuppb\xf8\x01\x01\xa2\x02\x06MRLV1A\xaa\x02 Google.Maps.RegionLookup.V1Alpha\xca\x02 Google\\Maps\\RegionLookup\\V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.regionlookup.v1alpha.region_identifier_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.maps.regionlookup.v1alphaB\x15RegionIdentifierProtoP\x01ZNcloud.google.com/go/maps/regionlookup/apiv1alpha/regionlookuppb;regionlookuppb\xf8\x01\x01\xa2\x02\x06MRLV1A\xaa\x02 Google.Maps.RegionLookup.V1Alpha\xca\x02 Google\\Maps\\RegionLookup\\V1alpha'
    _globals['_REGIONIDENTIFIER'].fields_by_name['place_type']._loaded_options = None
    _globals['_REGIONIDENTIFIER'].fields_by_name['place_type']._serialized_options = b'\xe0A\x02'
    _globals['_REGIONIDENTIFIER']._serialized_start = 128
    _globals['_REGIONIDENTIFIER']._serialized_end = 601
    _globals['_REGIONIDENTIFIER_PLACETYPE']._serialized_start = 318
    _globals['_REGIONIDENTIFIER_PLACETYPE']._serialized_end = 589