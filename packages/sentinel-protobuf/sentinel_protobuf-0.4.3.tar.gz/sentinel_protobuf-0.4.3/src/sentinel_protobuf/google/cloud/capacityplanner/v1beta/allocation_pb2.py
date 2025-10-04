"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/capacityplanner/v1beta/allocation.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/capacityplanner/v1beta/allocation.proto\x12#google.cloud.capacityplanner.v1beta\x1a\x1fgoogle/protobuf/timestamp.proto"\xd4\r\n\nAllocation\x12d\n\x13specific_allocation\x18\x06 \x01(\x0b2E.google.cloud.capacityplanner.v1beta.Allocation.SpecificSKUAllocationH\x00\x12\n\n\x02id\x18\x01 \x01(\x03\x12/\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0c\n\x04zone\x18\x03 \x01(\t\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x12\x12\n\nallocation\x18\x05 \x01(\t\x12\x18\n\x10owner_project_id\x18\n \x01(\t\x12F\n\x06status\x18\x07 \x01(\x0e26.google.cloud.capacityplanner.v1beta.Allocation.Status\x12U\n\x0eshare_settings\x18\x08 \x01(\x0b2=.google.cloud.capacityplanner.v1beta.Allocation.ShareSettings\x124\n\x10auto_delete_time\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a\x85\x07\n\x15SpecificSKUAllocation\x12~\n\x13instance_properties\x18\x01 \x01(\x0b2a.google.cloud.capacityplanner.v1beta.Allocation.SpecificSKUAllocation.AllocatedInstanceProperties\x12\r\n\x05count\x18\x02 \x01(\x03\x12\x12\n\nused_count\x18\x03 \x01(\x03\x12\x15\n\rassured_count\x18\x04 \x01(\x03\x1a\xb1\x05\n\x1bAllocatedInstanceProperties\x12\x14\n\x0cmachine_type\x18\x01 \x01(\t\x12\x8e\x01\n\x11guest_accelerator\x18\x02 \x03(\x0b2s.google.cloud.capacityplanner.v1beta.Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AcceleratorConfig\x12\x18\n\x10min_cpu_platform\x18\x03 \x01(\t\x12\x82\x01\n\tlocal_ssd\x18\x04 \x03(\x0b2o.google.cloud.capacityplanner.v1beta.Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk\x1a0\n\x11AcceleratorConfig\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05count\x18\x02 \x01(\x05\x1a\x99\x02\n\rAllocatedDisk\x12\x14\n\x0cdisk_size_gb\x18\x01 \x01(\x03\x12\x95\x01\n\x0edisk_interface\x18\x02 \x01(\x0e2}.google.cloud.capacityplanner.v1beta.Allocation.SpecificSKUAllocation.AllocatedInstanceProperties.AllocatedDisk.DiskInterface"Z\n\rDiskInterface\x12\x1e\n\x1aDISK_INTERFACE_UNSPECIFIED\x10\x00\x12\x08\n\x04SCSI\x10\x01\x12\x08\n\x04NVME\x10\x02\x12\n\n\x06NVDIMM\x10\x03\x12\t\n\x05ISCSI\x10\x04\x1a\x88\x02\n\rShareSettings\x12[\n\nshare_type\x18\x01 \x01(\x0e2G.google.cloud.capacityplanner.v1beta.Allocation.ShareSettings.ShareType\x12\x10\n\x08projects\x18\x02 \x03(\t"\x87\x01\n\tShareType\x12\x1a\n\x16SHARE_TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cORGANIZATION\x10\x01\x12\x15\n\x11SPECIFIC_PROJECTS\x10\x02\x12\t\n\x05LOCAL\x10\x03\x12*\n&DIRECT_PROJECTS_UNDER_SPECIFIC_FOLDERS\x10\x04"b\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0b\n\x07INVALID\x10\x01\x12\x0c\n\x08CREATING\x10\x02\x12\t\n\x05READY\x10\x03\x12\x0c\n\x08DELETING\x10\x04\x12\x0c\n\x08UPDATING\x10\x05B\x06\n\x04typeB\x84\x02\n\'com.google.cloud.capacityplanner.v1betaB\x0fAllocationProtoP\x01ZQcloud.google.com/go/capacityplanner/apiv1beta/capacityplannerpb;capacityplannerpb\xaa\x02#Google.Cloud.CapacityPlanner.V1Beta\xca\x02#Google\\Cloud\\CapacityPlanner\\V1beta\xea\x02&Google::Cloud::CapacityPlanner::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.capacityplanner.v1beta.allocation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.capacityplanner.v1betaB\x0fAllocationProtoP\x01ZQcloud.google.com/go/capacityplanner/apiv1beta/capacityplannerpb;capacityplannerpb\xaa\x02#Google.Cloud.CapacityPlanner.V1Beta\xca\x02#Google\\Cloud\\CapacityPlanner\\V1beta\xea\x02&Google::Cloud::CapacityPlanner::V1beta"
    _globals['_ALLOCATION']._serialized_start = 127
    _globals['_ALLOCATION']._serialized_end = 1875
    _globals['_ALLOCATION_SPECIFICSKUALLOCATION']._serialized_start = 599
    _globals['_ALLOCATION_SPECIFICSKUALLOCATION']._serialized_end = 1500
    _globals['_ALLOCATION_SPECIFICSKUALLOCATION_ALLOCATEDINSTANCEPROPERTIES']._serialized_start = 811
    _globals['_ALLOCATION_SPECIFICSKUALLOCATION_ALLOCATEDINSTANCEPROPERTIES']._serialized_end = 1500
    _globals['_ALLOCATION_SPECIFICSKUALLOCATION_ALLOCATEDINSTANCEPROPERTIES_ACCELERATORCONFIG']._serialized_start = 1168
    _globals['_ALLOCATION_SPECIFICSKUALLOCATION_ALLOCATEDINSTANCEPROPERTIES_ACCELERATORCONFIG']._serialized_end = 1216
    _globals['_ALLOCATION_SPECIFICSKUALLOCATION_ALLOCATEDINSTANCEPROPERTIES_ALLOCATEDDISK']._serialized_start = 1219
    _globals['_ALLOCATION_SPECIFICSKUALLOCATION_ALLOCATEDINSTANCEPROPERTIES_ALLOCATEDDISK']._serialized_end = 1500
    _globals['_ALLOCATION_SPECIFICSKUALLOCATION_ALLOCATEDINSTANCEPROPERTIES_ALLOCATEDDISK_DISKINTERFACE']._serialized_start = 1410
    _globals['_ALLOCATION_SPECIFICSKUALLOCATION_ALLOCATEDINSTANCEPROPERTIES_ALLOCATEDDISK_DISKINTERFACE']._serialized_end = 1500
    _globals['_ALLOCATION_SHARESETTINGS']._serialized_start = 1503
    _globals['_ALLOCATION_SHARESETTINGS']._serialized_end = 1767
    _globals['_ALLOCATION_SHARESETTINGS_SHARETYPE']._serialized_start = 1632
    _globals['_ALLOCATION_SHARESETTINGS_SHARETYPE']._serialized_end = 1767
    _globals['_ALLOCATION_STATUS']._serialized_start = 1769
    _globals['_ALLOCATION_STATUS']._serialized_end = 1867