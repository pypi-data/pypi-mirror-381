"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/locationfinder/v1/cloud_location.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/locationfinder/v1/cloud_location.proto\x12\x1egoogle.cloud.locationfinder.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xc2\x07\n\rCloudLocation\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12[\n\x19containing_cloud_location\x18\x02 \x01(\tB8\xe0A\x03\xfaA2\n0cloudlocationfinder.googleapis.com/CloudLocation\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x01\x12X\n\x0ecloud_provider\x18\x04 \x01(\x0e2;.google.cloud.locationfinder.v1.CloudLocation.CloudProviderB\x03\xe0A\x01\x12\x1b\n\x0eterritory_code\x18\x05 \x01(\tB\x03\xe0A\x01\x12a\n\x13cloud_location_type\x18\x06 \x01(\x0e2?.google.cloud.locationfinder.v1.CloudLocation.CloudLocationTypeB\x03\xe0A\x01\x12/\n\x1dcarbon_free_energy_percentage\x18\x07 \x01(\x02B\x03\xe0A\x01H\x00\x88\x01\x01"\x91\x01\n\rCloudProvider\x12\x1e\n\x1aCLOUD_PROVIDER_UNSPECIFIED\x10\x00\x12\x16\n\x12CLOUD_PROVIDER_GCP\x10\x01\x12\x16\n\x12CLOUD_PROVIDER_AWS\x10\x02\x12\x18\n\x14CLOUD_PROVIDER_AZURE\x10\x03\x12\x16\n\x12CLOUD_PROVIDER_OCI\x10\x04"\xc3\x01\n\x11CloudLocationType\x12#\n\x1fCLOUD_LOCATION_TYPE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aCLOUD_LOCATION_TYPE_REGION\x10\x01\x12\x1c\n\x18CLOUD_LOCATION_TYPE_ZONE\x10\x02\x12(\n$CLOUD_LOCATION_TYPE_REGION_EXTENSION\x10\x03\x12!\n\x1dCLOUD_LOCATION_TYPE_GDCC_ZONE\x10\x04:\x9e\x01\xeaA\x9a\x01\n0cloudlocationfinder.googleapis.com/CloudLocation\x12Gprojects/{project}/locations/{location}/cloudLocations/{cloud_location}*\x0ecloudLocations2\rcloudLocationB \n\x1e_carbon_free_energy_percentage"\xab\x01\n\x19ListCloudLocationsRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\x120cloudlocationfinder.googleapis.com/CloudLocation\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"\x87\x01\n\x1aListCloudLocationsResponse\x12K\n\x0fcloud_locations\x18\x01 \x03(\x0b2-.google.cloud.locationfinder.v1.CloudLocationB\x03\xe0A\x03\x12\x1c\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0A\x03"a\n\x17GetCloudLocationRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0cloudlocationfinder.googleapis.com/CloudLocation"\x85\x02\n\x1bSearchCloudLocationsRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\x120cloudlocationfinder.googleapis.com/CloudLocation\x12W\n\x15source_cloud_location\x18\x02 \x01(\tB8\xe0A\x02\xfaA2\n0cloudlocationfinder.googleapis.com/CloudLocation\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x12\n\x05query\x18\x06 \x01(\tB\x03\xe0A\x01"\x89\x01\n\x1cSearchCloudLocationsResponse\x12K\n\x0fcloud_locations\x18\x01 \x03(\x0b2-.google.cloud.locationfinder.v1.CloudLocationB\x03\xe0A\x03\x12\x1c\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0A\x03B\xec\x01\n"com.google.cloud.locationfinder.v1B\x12CloudLocationProtoP\x01ZJcloud.google.com/go/locationfinder/apiv1/locationfinderpb;locationfinderpb\xaa\x02\x1eGoogle.Cloud.LocationFinder.V1\xca\x02\x1eGoogle\\Cloud\\LocationFinder\\V1\xea\x02!Google::Cloud::LocationFinder::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.locationfinder.v1.cloud_location_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.locationfinder.v1B\x12CloudLocationProtoP\x01ZJcloud.google.com/go/locationfinder/apiv1/locationfinderpb;locationfinderpb\xaa\x02\x1eGoogle.Cloud.LocationFinder.V1\xca\x02\x1eGoogle\\Cloud\\LocationFinder\\V1\xea\x02!Google::Cloud::LocationFinder::V1'
    _globals['_CLOUDLOCATION'].fields_by_name['name']._loaded_options = None
    _globals['_CLOUDLOCATION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_CLOUDLOCATION'].fields_by_name['containing_cloud_location']._loaded_options = None
    _globals['_CLOUDLOCATION'].fields_by_name['containing_cloud_location']._serialized_options = b'\xe0A\x03\xfaA2\n0cloudlocationfinder.googleapis.com/CloudLocation'
    _globals['_CLOUDLOCATION'].fields_by_name['display_name']._loaded_options = None
    _globals['_CLOUDLOCATION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDLOCATION'].fields_by_name['cloud_provider']._loaded_options = None
    _globals['_CLOUDLOCATION'].fields_by_name['cloud_provider']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDLOCATION'].fields_by_name['territory_code']._loaded_options = None
    _globals['_CLOUDLOCATION'].fields_by_name['territory_code']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDLOCATION'].fields_by_name['cloud_location_type']._loaded_options = None
    _globals['_CLOUDLOCATION'].fields_by_name['cloud_location_type']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDLOCATION'].fields_by_name['carbon_free_energy_percentage']._loaded_options = None
    _globals['_CLOUDLOCATION'].fields_by_name['carbon_free_energy_percentage']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDLOCATION']._loaded_options = None
    _globals['_CLOUDLOCATION']._serialized_options = b'\xeaA\x9a\x01\n0cloudlocationfinder.googleapis.com/CloudLocation\x12Gprojects/{project}/locations/{location}/cloudLocations/{cloud_location}*\x0ecloudLocations2\rcloudLocation'
    _globals['_LISTCLOUDLOCATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCLOUDLOCATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\x120cloudlocationfinder.googleapis.com/CloudLocation'
    _globals['_LISTCLOUDLOCATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCLOUDLOCATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCLOUDLOCATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCLOUDLOCATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCLOUDLOCATIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTCLOUDLOCATIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCLOUDLOCATIONSRESPONSE'].fields_by_name['cloud_locations']._loaded_options = None
    _globals['_LISTCLOUDLOCATIONSRESPONSE'].fields_by_name['cloud_locations']._serialized_options = b'\xe0A\x03'
    _globals['_LISTCLOUDLOCATIONSRESPONSE'].fields_by_name['next_page_token']._loaded_options = None
    _globals['_LISTCLOUDLOCATIONSRESPONSE'].fields_by_name['next_page_token']._serialized_options = b'\xe0A\x03'
    _globals['_GETCLOUDLOCATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCLOUDLOCATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0cloudlocationfinder.googleapis.com/CloudLocation'
    _globals['_SEARCHCLOUDLOCATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_SEARCHCLOUDLOCATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\x120cloudlocationfinder.googleapis.com/CloudLocation'
    _globals['_SEARCHCLOUDLOCATIONSREQUEST'].fields_by_name['source_cloud_location']._loaded_options = None
    _globals['_SEARCHCLOUDLOCATIONSREQUEST'].fields_by_name['source_cloud_location']._serialized_options = b'\xe0A\x02\xfaA2\n0cloudlocationfinder.googleapis.com/CloudLocation'
    _globals['_SEARCHCLOUDLOCATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_SEARCHCLOUDLOCATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHCLOUDLOCATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_SEARCHCLOUDLOCATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHCLOUDLOCATIONSREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_SEARCHCLOUDLOCATIONSREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHCLOUDLOCATIONSRESPONSE'].fields_by_name['cloud_locations']._loaded_options = None
    _globals['_SEARCHCLOUDLOCATIONSRESPONSE'].fields_by_name['cloud_locations']._serialized_options = b'\xe0A\x03'
    _globals['_SEARCHCLOUDLOCATIONSRESPONSE'].fields_by_name['next_page_token']._loaded_options = None
    _globals['_SEARCHCLOUDLOCATIONSRESPONSE'].fields_by_name['next_page_token']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDLOCATION']._serialized_start = 148
    _globals['_CLOUDLOCATION']._serialized_end = 1110
    _globals['_CLOUDLOCATION_CLOUDPROVIDER']._serialized_start = 572
    _globals['_CLOUDLOCATION_CLOUDPROVIDER']._serialized_end = 717
    _globals['_CLOUDLOCATION_CLOUDLOCATIONTYPE']._serialized_start = 720
    _globals['_CLOUDLOCATION_CLOUDLOCATIONTYPE']._serialized_end = 915
    _globals['_LISTCLOUDLOCATIONSREQUEST']._serialized_start = 1113
    _globals['_LISTCLOUDLOCATIONSREQUEST']._serialized_end = 1284
    _globals['_LISTCLOUDLOCATIONSRESPONSE']._serialized_start = 1287
    _globals['_LISTCLOUDLOCATIONSRESPONSE']._serialized_end = 1422
    _globals['_GETCLOUDLOCATIONREQUEST']._serialized_start = 1424
    _globals['_GETCLOUDLOCATIONREQUEST']._serialized_end = 1521
    _globals['_SEARCHCLOUDLOCATIONSREQUEST']._serialized_start = 1524
    _globals['_SEARCHCLOUDLOCATIONSREQUEST']._serialized_end = 1785
    _globals['_SEARCHCLOUDLOCATIONSRESPONSE']._serialized_start = 1788
    _globals['_SEARCHCLOUDLOCATIONSRESPONSE']._serialized_end = 1925