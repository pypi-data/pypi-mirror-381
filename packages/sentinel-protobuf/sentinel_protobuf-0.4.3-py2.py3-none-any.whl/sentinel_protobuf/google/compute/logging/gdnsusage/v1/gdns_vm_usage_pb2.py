"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/compute/logging/gdnsusage/v1/gdns_vm_usage.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/compute/logging/gdnsusage/v1/gdns_vm_usage.proto\x12#google.compute.logging.gdnsusage.v1"\xa0\x02\n\x16GdnsVmUsagePlatformLog\x12C\n\tsource_vm\x18\x01 \x01(\x0b2+.google.compute.logging.gdnsusage.v1.VmInfoH\x00\x88\x01\x01\x12H\n\x0edestination_vm\x18\x02 \x01(\x0b2+.google.compute.logging.gdnsusage.v1.VmInfoH\x01\x88\x01\x01\x12\x1a\n\rdebug_message\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x18\n\x0bquery_count\x18\x05 \x01(\x05H\x03\x88\x01\x01B\x0c\n\n_source_vmB\x11\n\x0f_destination_vmB\x10\n\x0e_debug_messageB\x0e\n\x0c_query_count"d\n\x06VmInfo\x12\x17\n\nproject_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0f\n\x02vm\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x11\n\x04zone\x18\x03 \x01(\tH\x02\x88\x01\x01B\r\n\x0b_project_idB\x05\n\x03_vmB\x07\n\x05_zoneB\xfd\x01\n#google.compute.logging.gdnsusage.v1B\x10GdnsVmUsageProtoP\x01ZLgoogle.golang.org/genproto/googleapis/compute/logging/gdnsusage/v1;gdnsusage\xaa\x02#Google.Compute.Logging.GdnsUsage.V1\xca\x02#Google\\Compute\\Logging\\GdnsUsage\\V1\xea\x02\'Google::Compute::Logging::GdnsUsage::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.compute.logging.gdnsusage.v1.gdns_vm_usage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n#google.compute.logging.gdnsusage.v1B\x10GdnsVmUsageProtoP\x01ZLgoogle.golang.org/genproto/googleapis/compute/logging/gdnsusage/v1;gdnsusage\xaa\x02#Google.Compute.Logging.GdnsUsage.V1\xca\x02#Google\\Compute\\Logging\\GdnsUsage\\V1\xea\x02'Google::Compute::Logging::GdnsUsage::V1"
    _globals['_GDNSVMUSAGEPLATFORMLOG']._serialized_start = 97
    _globals['_GDNSVMUSAGEPLATFORMLOG']._serialized_end = 385
    _globals['_VMINFO']._serialized_start = 387
    _globals['_VMINFO']._serialized_end = 487