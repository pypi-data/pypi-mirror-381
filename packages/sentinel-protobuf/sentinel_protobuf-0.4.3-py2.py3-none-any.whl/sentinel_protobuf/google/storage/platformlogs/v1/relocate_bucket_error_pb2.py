"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/storage/platformlogs/v1/relocate_bucket_error.proto')
_sym_db = _symbol_database.Default()
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/storage/platformlogs/v1/relocate_bucket_error.proto\x12\x1egoogle.storage.platformlogs.v1\x1a\x17google/rpc/status.proto"\xa8\x04\n\x13RelocateBucketError\x12\x10\n\x08resource\x18\x01 \x01(\t\x12\x11\n\tobject_id\x18\x02 \x01(\t\x12\x17\n\x0fsource_location\x18\x03 \x01(\t\x12\x1c\n\x14destination_location\x18\x04 \x01(\t\x12v\n\x1esource_custom_placement_config\x18\x05 \x01(\x0b2I.google.storage.platformlogs.v1.RelocateBucketError.CustomPlacementConfigH\x00\x88\x01\x01\x12{\n#destination_custom_placement_config\x18\x06 \x01(\x0b2I.google.storage.platformlogs.v1.RelocateBucketError.CustomPlacementConfigH\x01\x88\x01\x01\x12-\n\x11relocation_errors\x18\x07 \x03(\x0b2\x12.google.rpc.Status\x12\x15\n\rvalidate_only\x18\x08 \x01(\x08\x1a/\n\x15CustomPlacementConfig\x12\x16\n\x0edata_locations\x18\x01 \x03(\tB!\n\x1f_source_custom_placement_configB&\n$_destination_custom_placement_configB\x87\x02\n"com.google.storage.platformlogs.v1B\x18RelocateBucketErrorProtoP\x01ZLcloud.google.com/go/storage/platformlogs/apiv1/platformlogspb;platformlogspb\xaa\x02$Google.Cloud.Storage.PlatformLogs.V1\xca\x02$Google\\Cloud\\Storage\\PlatformLogs\\V1\xea\x02(Google::Cloud::Storage::PlatformLogs::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.storage.platformlogs.v1.relocate_bucket_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.storage.platformlogs.v1B\x18RelocateBucketErrorProtoP\x01ZLcloud.google.com/go/storage/platformlogs/apiv1/platformlogspb;platformlogspb\xaa\x02$Google.Cloud.Storage.PlatformLogs.V1\xca\x02$Google\\Cloud\\Storage\\PlatformLogs\\V1\xea\x02(Google::Cloud::Storage::PlatformLogs::V1'
    _globals['_RELOCATEBUCKETERROR']._serialized_start = 120
    _globals['_RELOCATEBUCKETERROR']._serialized_end = 672
    _globals['_RELOCATEBUCKETERROR_CUSTOMPLACEMENTCONFIG']._serialized_start = 550
    _globals['_RELOCATEBUCKETERROR_CUSTOMPLACEMENTCONFIG']._serialized_end = 597