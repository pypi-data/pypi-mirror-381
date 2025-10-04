"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/locationfinder/v1/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.cloud.locationfinder.v1 import cloud_location_pb2 as google_dot_cloud_dot_locationfinder_dot_v1_dot_cloud__location__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/locationfinder/v1/service.proto\x12\x1egoogle.cloud.locationfinder.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a3google/cloud/locationfinder/v1/cloud_location.proto2\xfc\x05\n\x13CloudLocationFinder\x12\xd0\x01\n\x12ListCloudLocations\x129.google.cloud.locationfinder.v1.ListCloudLocationsRequest\x1a:.google.cloud.locationfinder.v1.ListCloudLocationsResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1/{parent=projects/*/locations/*}/cloudLocations\x12\xbd\x01\n\x10GetCloudLocation\x127.google.cloud.locationfinder.v1.GetCloudLocationRequest\x1a-.google.cloud.locationfinder.v1.CloudLocation"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1/{name=projects/*/locations/*/cloudLocations/*}\x12\xf9\x01\n\x14SearchCloudLocations\x12;.google.cloud.locationfinder.v1.SearchCloudLocationsRequest\x1a<.google.cloud.locationfinder.v1.SearchCloudLocationsResponse"f\xdaA"parent,source_cloud_location,query\x82\xd3\xe4\x93\x02;\x129/v1/{parent=projects/*/locations/*}/cloudLocations:search\x1aV\xcaA"cloudlocationfinder.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe6\x01\n"com.google.cloud.locationfinder.v1B\x0cServiceProtoP\x01ZJcloud.google.com/go/locationfinder/apiv1/locationfinderpb;locationfinderpb\xaa\x02\x1eGoogle.Cloud.LocationFinder.V1\xca\x02\x1eGoogle\\Cloud\\LocationFinder\\V1\xea\x02!Google::Cloud::LocationFinder::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.locationfinder.v1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.locationfinder.v1B\x0cServiceProtoP\x01ZJcloud.google.com/go/locationfinder/apiv1/locationfinderpb;locationfinderpb\xaa\x02\x1eGoogle.Cloud.LocationFinder.V1\xca\x02\x1eGoogle\\Cloud\\LocationFinder\\V1\xea\x02!Google::Cloud::LocationFinder::V1'
    _globals['_CLOUDLOCATIONFINDER']._loaded_options = None
    _globals['_CLOUDLOCATIONFINDER']._serialized_options = b'\xcaA"cloudlocationfinder.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CLOUDLOCATIONFINDER'].methods_by_name['ListCloudLocations']._loaded_options = None
    _globals['_CLOUDLOCATIONFINDER'].methods_by_name['ListCloudLocations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1/{parent=projects/*/locations/*}/cloudLocations'
    _globals['_CLOUDLOCATIONFINDER'].methods_by_name['GetCloudLocation']._loaded_options = None
    _globals['_CLOUDLOCATIONFINDER'].methods_by_name['GetCloudLocation']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1/{name=projects/*/locations/*/cloudLocations/*}'
    _globals['_CLOUDLOCATIONFINDER'].methods_by_name['SearchCloudLocations']._loaded_options = None
    _globals['_CLOUDLOCATIONFINDER'].methods_by_name['SearchCloudLocations']._serialized_options = b'\xdaA"parent,source_cloud_location,query\x82\xd3\xe4\x93\x02;\x129/v1/{parent=projects/*/locations/*}/cloudLocations:search'
    _globals['_CLOUDLOCATIONFINDER']._serialized_start = 189
    _globals['_CLOUDLOCATIONFINDER']._serialized_end = 953