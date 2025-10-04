"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/capacityplanner/v1beta/location.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/capacityplanner/v1beta/location.proto\x12#google.cloud.capacityplanner.v1beta\x1a\x1fgoogle/api/field_behavior.proto"\xe1\x02\n\x12LocationIdentifier\x12J\n\x0elocation_level\x18\x01 \x01(\x0e22.google.cloud.capacityplanner.v1beta.LocationLevel\x12\x13\n\x06source\x18\x02 \x01(\tB\x03\xe0A\x02\x12e\n\x10linked_locations\x18\x03 \x03(\x0b2F.google.cloud.capacityplanner.v1beta.LocationIdentifier.LinkedLocationB\x03\xe0A\x01\x1a\x82\x01\n\x0eLinkedLocation\x12J\n\x0elocation_level\x18\x01 \x01(\x0e22.google.cloud.capacityplanner.v1beta.LocationLevel\x12\x15\n\x08location\x18\x02 \x01(\tB\x03\xe0A\x02\x12\r\n\x05label\x18\x03 \x01(\t*\x7f\n\rLocationLevel\x12\x1e\n\x1aLOCATION_LEVEL_UNSPECIFIED\x10\x00\x12\n\n\x06REGION\x10\x01\x12\x08\n\x04ZONE\x10\x02\x12\n\n\x06GLOBAL\x10\x03\x12\t\n\x05METRO\x10\x04\x12\x0f\n\x0bDUAL_REGION\x10\x05\x12\x10\n\x0cMULTI_REGION\x10\x06B\x82\x02\n\'com.google.cloud.capacityplanner.v1betaB\rLocationProtoP\x01ZQcloud.google.com/go/capacityplanner/apiv1beta/capacityplannerpb;capacityplannerpb\xaa\x02#Google.Cloud.CapacityPlanner.V1Beta\xca\x02#Google\\Cloud\\CapacityPlanner\\V1beta\xea\x02&Google::Cloud::CapacityPlanner::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.capacityplanner.v1beta.location_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.capacityplanner.v1betaB\rLocationProtoP\x01ZQcloud.google.com/go/capacityplanner/apiv1beta/capacityplannerpb;capacityplannerpb\xaa\x02#Google.Cloud.CapacityPlanner.V1Beta\xca\x02#Google\\Cloud\\CapacityPlanner\\V1beta\xea\x02&Google::Cloud::CapacityPlanner::V1beta"
    _globals['_LOCATIONIDENTIFIER_LINKEDLOCATION'].fields_by_name['location']._loaded_options = None
    _globals['_LOCATIONIDENTIFIER_LINKEDLOCATION'].fields_by_name['location']._serialized_options = b'\xe0A\x02'
    _globals['_LOCATIONIDENTIFIER'].fields_by_name['source']._loaded_options = None
    _globals['_LOCATIONIDENTIFIER'].fields_by_name['source']._serialized_options = b'\xe0A\x02'
    _globals['_LOCATIONIDENTIFIER'].fields_by_name['linked_locations']._loaded_options = None
    _globals['_LOCATIONIDENTIFIER'].fields_by_name['linked_locations']._serialized_options = b'\xe0A\x01'
    _globals['_LOCATIONLEVEL']._serialized_start = 480
    _globals['_LOCATIONLEVEL']._serialized_end = 607
    _globals['_LOCATIONIDENTIFIER']._serialized_start = 125
    _globals['_LOCATIONIDENTIFIER']._serialized_end = 478
    _globals['_LOCATIONIDENTIFIER_LINKEDLOCATION']._serialized_start = 348
    _globals['_LOCATIONIDENTIFIER_LINKEDLOCATION']._serialized_end = 478