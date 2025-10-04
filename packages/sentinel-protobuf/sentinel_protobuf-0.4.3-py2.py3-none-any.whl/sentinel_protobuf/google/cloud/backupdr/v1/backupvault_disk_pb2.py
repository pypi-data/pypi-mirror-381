"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/backupdr/v1/backupvault_disk.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.backupdr.v1 import backupvault_gce_pb2 as google_dot_cloud_dot_backupdr_dot_v1_dot_backupvault__gce__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/backupdr/v1/backupvault_disk.proto\x12\x18google.cloud.backupdr.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a.google/cloud/backupdr/v1/backupvault_gce.proto"@\n\x15DiskTargetEnvironment\x12\x14\n\x07project\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04zone\x18\x02 \x01(\tB\x03\xe0A\x02"d\n\x1bRegionDiskTargetEnvironment\x12\x14\n\x07project\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06region\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rreplica_zones\x18\x03 \x03(\tB\x03\xe0A\x02"\xa5\x0b\n\x15DiskRestoreProperties\x12\x16\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02H\x00\x88\x01\x01\x12\x1d\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01H\x01\x88\x01\x01\x12\x19\n\x07size_gb\x18\x03 \x01(\x03B\x03\xe0A\x02H\x02\x88\x01\x01\x12\x15\n\x08licenses\x18\x04 \x03(\tB\x03\xe0A\x01\x12G\n\x10guest_os_feature\x18\x05 \x03(\x0b2(.google.cloud.backupdr.v1.GuestOsFeatureB\x03\xe0A\x01\x12V\n\x13disk_encryption_key\x18\x06 \x01(\x0b2/.google.cloud.backupdr.v1.CustomerEncryptionKeyB\x03\xe0A\x01H\x03\x88\x01\x01\x12+\n\x19physical_block_size_bytes\x18\x07 \x01(\x03B\x03\xe0A\x01H\x04\x88\x01\x01\x12"\n\x10provisioned_iops\x18\x08 \x01(\x03B\x03\xe0A\x01H\x05\x88\x01\x01\x12(\n\x16provisioned_throughput\x18\t \x01(\x03B\x03\xe0A\x01H\x06\x88\x01\x01\x12-\n\x1benable_confidential_compute\x18\n \x01(\x08B\x03\xe0A\x01H\x07\x88\x01\x01\x12E\n\x0cstorage_pool\x18\x0b \x01(\tB*\xe0A\x01\xfaA$\n"compute.googleapis.com/StoragePoolH\x08\x88\x01\x01\x12Y\n\x0baccess_mode\x18\x0c \x01(\x0e2:.google.cloud.backupdr.v1.DiskRestoreProperties.AccessModeB\x03\xe0A\x01H\t\x88\x01\x01\x12\\\n\x0carchitecture\x18\x0e \x01(\x0e2<.google.cloud.backupdr.v1.DiskRestoreProperties.ArchitectureB\x03\xe0A\x01H\n\x88\x01\x01\x12\x1c\n\x0fresource_policy\x18\x0f \x03(\tB\x03\xe0A\x01\x12\x16\n\x04type\x18\x10 \x01(\tB\x03\xe0A\x02H\x0b\x88\x01\x01\x12P\n\x06labels\x18\x11 \x03(\x0b2;.google.cloud.backupdr.v1.DiskRestoreProperties.LabelsEntryB\x03\xe0A\x01\x12l\n\x15resource_manager_tags\x18\x12 \x03(\x0b2H.google.cloud.backupdr.v1.DiskRestoreProperties.ResourceManagerTagsEntryB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a:\n\x18ResourceManagerTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"L\n\nAccessMode\x12\x15\n\x11READ_WRITE_SINGLE\x10\x00\x12\x13\n\x0fREAD_WRITE_MANY\x10\x01\x12\x12\n\x0eREAD_ONLY_MANY\x10\x02"C\n\x0cArchitecture\x12\x1c\n\x18ARCHITECTURE_UNSPECIFIED\x10\x00\x12\n\n\x06X86_64\x10\x01\x12\t\n\x05ARM64\x10\x02B\x07\n\x05_nameB\x0e\n\x0c_descriptionB\n\n\x08_size_gbB\x16\n\x14_disk_encryption_keyB\x1c\n\x1a_physical_block_size_bytesB\x13\n\x11_provisioned_iopsB\x19\n\x17_provisioned_throughputB\x1e\n\x1c_enable_confidential_computeB\x0f\n\r_storage_poolB\x0e\n\x0c_access_modeB\x0f\n\r_architectureB\x07\n\x05_type"\xff\x03\n\x14DiskBackupProperties\x12\x18\n\x0bdescription\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x08licenses\x18\x02 \x03(\t\x12B\n\x10guest_os_feature\x18\x03 \x03(\x0b2(.google.cloud.backupdr.v1.GuestOsFeature\x12V\n\x0carchitecture\x18\x04 \x01(\x0e2;.google.cloud.backupdr.v1.DiskBackupProperties.ArchitectureH\x01\x88\x01\x01\x12\x11\n\x04type\x18\x05 \x01(\tH\x02\x88\x01\x01\x12\x14\n\x07size_gb\x18\x06 \x01(\x03H\x03\x88\x01\x01\x12\x13\n\x06region\x18\x07 \x01(\tH\x04\x88\x01\x01\x12\x11\n\x04zone\x18\x08 \x01(\tH\x05\x88\x01\x01\x12\x15\n\rreplica_zones\x18\t \x03(\t\x12\x18\n\x0bsource_disk\x18\n \x01(\tH\x06\x88\x01\x01"C\n\x0cArchitecture\x12\x1c\n\x18ARCHITECTURE_UNSPECIFIED\x10\x00\x12\n\n\x06X86_64\x10\x01\x12\t\n\x05ARM64\x10\x02B\x0e\n\x0c_descriptionB\x0f\n\r_architectureB\x07\n\x05_typeB\n\n\x08_size_gbB\t\n\x07_regionB\x07\n\x05_zoneB\x0e\n\x0c_source_disk"\\\n\x18DiskDataSourceProperties\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0f\n\x07size_gb\x18\x04 \x01(\x03B\xa8\x02\n\x1ccom.google.cloud.backupdr.v1B\x14BackupvaultDiskProtoP\x01Z8cloud.google.com/go/backupdr/apiv1/backupdrpb;backupdrpb\xaa\x02\x18Google.Cloud.BackupDR.V1\xca\x02\x18Google\\Cloud\\BackupDR\\V1\xea\x02\x1bGoogle::Cloud::BackupDR::V1\xeaAa\n"compute.googleapis.com/StoragePool\x12;projects/{project}/zones/{zone}/storagePools/{storage_pool}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.backupdr.v1.backupvault_disk_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.backupdr.v1B\x14BackupvaultDiskProtoP\x01Z8cloud.google.com/go/backupdr/apiv1/backupdrpb;backupdrpb\xaa\x02\x18Google.Cloud.BackupDR.V1\xca\x02\x18Google\\Cloud\\BackupDR\\V1\xea\x02\x1bGoogle::Cloud::BackupDR::V1\xeaAa\n"compute.googleapis.com/StoragePool\x12;projects/{project}/zones/{zone}/storagePools/{storage_pool}'
    _globals['_DISKTARGETENVIRONMENT'].fields_by_name['project']._loaded_options = None
    _globals['_DISKTARGETENVIRONMENT'].fields_by_name['project']._serialized_options = b'\xe0A\x02'
    _globals['_DISKTARGETENVIRONMENT'].fields_by_name['zone']._loaded_options = None
    _globals['_DISKTARGETENVIRONMENT'].fields_by_name['zone']._serialized_options = b'\xe0A\x02'
    _globals['_REGIONDISKTARGETENVIRONMENT'].fields_by_name['project']._loaded_options = None
    _globals['_REGIONDISKTARGETENVIRONMENT'].fields_by_name['project']._serialized_options = b'\xe0A\x02'
    _globals['_REGIONDISKTARGETENVIRONMENT'].fields_by_name['region']._loaded_options = None
    _globals['_REGIONDISKTARGETENVIRONMENT'].fields_by_name['region']._serialized_options = b'\xe0A\x02'
    _globals['_REGIONDISKTARGETENVIRONMENT'].fields_by_name['replica_zones']._loaded_options = None
    _globals['_REGIONDISKTARGETENVIRONMENT'].fields_by_name['replica_zones']._serialized_options = b'\xe0A\x02'
    _globals['_DISKRESTOREPROPERTIES_LABELSENTRY']._loaded_options = None
    _globals['_DISKRESTOREPROPERTIES_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_DISKRESTOREPROPERTIES_RESOURCEMANAGERTAGSENTRY']._loaded_options = None
    _globals['_DISKRESTOREPROPERTIES_RESOURCEMANAGERTAGSENTRY']._serialized_options = b'8\x01'
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['name']._loaded_options = None
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['description']._loaded_options = None
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['size_gb']._loaded_options = None
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['size_gb']._serialized_options = b'\xe0A\x02'
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['licenses']._loaded_options = None
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['licenses']._serialized_options = b'\xe0A\x01'
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['guest_os_feature']._loaded_options = None
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['guest_os_feature']._serialized_options = b'\xe0A\x01'
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['disk_encryption_key']._loaded_options = None
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['disk_encryption_key']._serialized_options = b'\xe0A\x01'
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['physical_block_size_bytes']._loaded_options = None
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['physical_block_size_bytes']._serialized_options = b'\xe0A\x01'
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['provisioned_iops']._loaded_options = None
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['provisioned_iops']._serialized_options = b'\xe0A\x01'
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['provisioned_throughput']._loaded_options = None
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['provisioned_throughput']._serialized_options = b'\xe0A\x01'
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['enable_confidential_compute']._loaded_options = None
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['enable_confidential_compute']._serialized_options = b'\xe0A\x01'
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['storage_pool']._loaded_options = None
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['storage_pool']._serialized_options = b'\xe0A\x01\xfaA$\n"compute.googleapis.com/StoragePool'
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['access_mode']._loaded_options = None
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['access_mode']._serialized_options = b'\xe0A\x01'
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['architecture']._loaded_options = None
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['architecture']._serialized_options = b'\xe0A\x01'
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['resource_policy']._loaded_options = None
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['resource_policy']._serialized_options = b'\xe0A\x01'
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['type']._loaded_options = None
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['labels']._loaded_options = None
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['resource_manager_tags']._loaded_options = None
    _globals['_DISKRESTOREPROPERTIES'].fields_by_name['resource_manager_tags']._serialized_options = b'\xe0A\x01'
    _globals['_DISKTARGETENVIRONMENT']._serialized_start = 185
    _globals['_DISKTARGETENVIRONMENT']._serialized_end = 249
    _globals['_REGIONDISKTARGETENVIRONMENT']._serialized_start = 251
    _globals['_REGIONDISKTARGETENVIRONMENT']._serialized_end = 351
    _globals['_DISKRESTOREPROPERTIES']._serialized_start = 354
    _globals['_DISKRESTOREPROPERTIES']._serialized_end = 1799
    _globals['_DISKRESTOREPROPERTIES_LABELSENTRY']._serialized_start = 1317
    _globals['_DISKRESTOREPROPERTIES_LABELSENTRY']._serialized_end = 1362
    _globals['_DISKRESTOREPROPERTIES_RESOURCEMANAGERTAGSENTRY']._serialized_start = 1364
    _globals['_DISKRESTOREPROPERTIES_RESOURCEMANAGERTAGSENTRY']._serialized_end = 1422
    _globals['_DISKRESTOREPROPERTIES_ACCESSMODE']._serialized_start = 1424
    _globals['_DISKRESTOREPROPERTIES_ACCESSMODE']._serialized_end = 1500
    _globals['_DISKRESTOREPROPERTIES_ARCHITECTURE']._serialized_start = 1502
    _globals['_DISKRESTOREPROPERTIES_ARCHITECTURE']._serialized_end = 1569
    _globals['_DISKBACKUPPROPERTIES']._serialized_start = 1802
    _globals['_DISKBACKUPPROPERTIES']._serialized_end = 2313
    _globals['_DISKBACKUPPROPERTIES_ARCHITECTURE']._serialized_start = 1502
    _globals['_DISKBACKUPPROPERTIES_ARCHITECTURE']._serialized_end = 1569
    _globals['_DISKDATASOURCEPROPERTIES']._serialized_start = 2315
    _globals['_DISKDATASOURCEPROPERTIES']._serialized_end = 2407