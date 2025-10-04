"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/admanager/v1/geo_target_messages.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/ads/admanager/v1/geo_target_messages.proto\x12\x17google.ads.admanager.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xb8\x03\n\tGeoTarget\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1e\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12I\n\x10canonical_parent\x18\x03 \x01(\tB*\xe0A\x03\xfaA$\n"admanager.googleapis.com/GeoTargetH\x01\x88\x01\x01\x12\x19\n\x0cparent_names\x18\x04 \x03(\tB\x03\xe0A\x03\x12\x1d\n\x0bregion_code\x18\x05 \x01(\tB\x03\xe0A\x03H\x02\x88\x01\x01\x12\x16\n\x04type\x18\x06 \x01(\tB\x03\xe0A\x03H\x03\x88\x01\x01\x12\x1c\n\ntargetable\x18\x07 \x01(\x08B\x03\xe0A\x03H\x04\x88\x01\x01:o\xeaAl\n"admanager.googleapis.com/GeoTarget\x12/networks/{network_code}/geoTargets/{geo_target}*\ngeoTargets2\tgeoTargetB\x0f\n\r_display_nameB\x13\n\x11_canonical_parentB\x0e\n\x0c_region_codeB\x07\n\x05_typeB\r\n\x0b_targetableB\xca\x01\n\x1bcom.google.ads.admanager.v1B\x16GeoTargetMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.geo_target_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x16GeoTargetMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_GEOTARGET'].fields_by_name['name']._loaded_options = None
    _globals['_GEOTARGET'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_GEOTARGET'].fields_by_name['display_name']._loaded_options = None
    _globals['_GEOTARGET'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_GEOTARGET'].fields_by_name['canonical_parent']._loaded_options = None
    _globals['_GEOTARGET'].fields_by_name['canonical_parent']._serialized_options = b'\xe0A\x03\xfaA$\n"admanager.googleapis.com/GeoTarget'
    _globals['_GEOTARGET'].fields_by_name['parent_names']._loaded_options = None
    _globals['_GEOTARGET'].fields_by_name['parent_names']._serialized_options = b'\xe0A\x03'
    _globals['_GEOTARGET'].fields_by_name['region_code']._loaded_options = None
    _globals['_GEOTARGET'].fields_by_name['region_code']._serialized_options = b'\xe0A\x03'
    _globals['_GEOTARGET'].fields_by_name['type']._loaded_options = None
    _globals['_GEOTARGET'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_GEOTARGET'].fields_by_name['targetable']._loaded_options = None
    _globals['_GEOTARGET'].fields_by_name['targetable']._serialized_options = b'\xe0A\x03'
    _globals['_GEOTARGET']._loaded_options = None
    _globals['_GEOTARGET']._serialized_options = b'\xeaAl\n"admanager.googleapis.com/GeoTarget\x12/networks/{network_code}/geoTargets/{geo_target}*\ngeoTargets2\tgeoTarget'
    _globals['_GEOTARGET']._serialized_start = 139
    _globals['_GEOTARGET']._serialized_end = 579