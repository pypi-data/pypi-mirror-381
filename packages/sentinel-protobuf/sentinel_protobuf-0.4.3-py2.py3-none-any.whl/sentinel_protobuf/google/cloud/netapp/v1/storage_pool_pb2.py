"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/netapp/v1/storage_pool.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.netapp.v1 import common_pb2 as google_dot_cloud_dot_netapp_dot_v1_dot_common__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/netapp/v1/storage_pool.proto\x12\x16google.cloud.netapp.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/cloud/netapp/v1/common.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"P\n\x15GetStoragePoolRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!netapp.googleapis.com/StoragePool"\xb1\x01\n\x17ListStoragePoolsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!netapp.googleapis.com/StoragePool\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x05 \x01(\tB\x03\xe0A\x01"\x84\x01\n\x18ListStoragePoolsResponse\x12:\n\rstorage_pools\x18\x01 \x03(\x0b2#.google.cloud.netapp.v1.StoragePool\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\xb3\x01\n\x18CreateStoragePoolRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!netapp.googleapis.com/StoragePool\x12\x1c\n\x0fstorage_pool_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12>\n\x0cstorage_pool\x18\x03 \x01(\x0b2#.google.cloud.netapp.v1.StoragePoolB\x03\xe0A\x02"\x90\x01\n\x18UpdateStoragePoolRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12>\n\x0cstorage_pool\x18\x02 \x01(\x0b2#.google.cloud.netapp.v1.StoragePoolB\x03\xe0A\x02"S\n\x18DeleteStoragePoolRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!netapp.googleapis.com/StoragePool"Y\n\x1eSwitchActiveReplicaZoneRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!netapp.googleapis.com/StoragePool"\xe4\x0c\n\x0bStoragePool\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12@\n\rservice_level\x18\x02 \x01(\x0e2$.google.cloud.netapp.v1.ServiceLevelB\x03\xe0A\x02\x12\x19\n\x0ccapacity_gib\x18\x03 \x01(\x03B\x03\xe0A\x02\x12 \n\x13volume_capacity_gib\x18\x04 \x01(\x03B\x03\xe0A\x03\x12\x19\n\x0cvolume_count\x18\x05 \x01(\x05B\x03\xe0A\x03\x12=\n\x05state\x18\x06 \x01(\x0e2).google.cloud.netapp.v1.StoragePool.StateB\x03\xe0A\x03\x12\x1a\n\rstate_details\x18\x07 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\t \x01(\tB\x03\xe0A\x01\x12D\n\x06labels\x18\n \x03(\x0b2/.google.cloud.netapp.v1.StoragePool.LabelsEntryB\x03\xe0A\x01\x127\n\x07network\x18\x0b \x01(\tB&\xe0A\x02\xfaA \n\x1ecompute.googleapis.com/Network\x12G\n\x10active_directory\x18\x0c \x01(\tB-\xe0A\x01\xfaA\'\n%netapp.googleapis.com/ActiveDirectory\x12;\n\nkms_config\x18\r \x01(\tB\'\xe0A\x01\xfaA!\n\x1fnetapp.googleapis.com/KmsConfig\x12\x19\n\x0cldap_enabled\x18\x0e \x01(\x08B\x03\xe0A\x01\x12\x16\n\tpsa_range\x18\x0f \x01(\tB\x03\xe0A\x01\x12D\n\x0fencryption_type\x18\x10 \x01(\x0e2&.google.cloud.netapp.v1.EncryptionTypeB\x03\xe0A\x03\x12&\n\x15global_access_allowed\x18\x11 \x01(\x08B\x02\x18\x01H\x00\x88\x01\x01\x12\x1f\n\x12allow_auto_tiering\x18\x12 \x01(\x08B\x03\xe0A\x01\x12\x19\n\x0creplica_zone\x18\x14 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04zone\x18\x15 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rsatisfies_pzs\x18\x17 \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x18 \x01(\x08B\x03\xe0A\x03\x12\'\n\x1acustom_performance_enabled\x18\x19 \x01(\x08B\x03\xe0A\x01\x12#\n\x16total_throughput_mibps\x18\x1a \x01(\x03B\x03\xe0A\x01\x12\x17\n\ntotal_iops\x18\x1b \x01(\x03B\x03\xe0A\x01\x12\x1e\n\x11hot_tier_size_gib\x18\x1c \x01(\x03B\x03\xe0A\x01\x12-\n\x1benable_hot_tier_auto_resize\x18\x1d \x01(\x08B\x03\xe0A\x01H\x01\x88\x01\x01\x126\n\x08qos_type\x18\x1e \x01(\x0e2\x1f.google.cloud.netapp.v1.QosTypeB\x03\xe0A\x01\x12\'\n\x1aavailable_throughput_mibps\x18\x1f \x01(\x01B\x03\xe0A\x03\x12$\n\x17cold_tier_size_used_gib\x18! \x01(\x03B\x03\xe0A\x03\x12#\n\x16hot_tier_size_used_gib\x18" \x01(\x03B\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"{\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\t\n\x05READY\x10\x01\x12\x0c\n\x08CREATING\x10\x02\x12\x0c\n\x08DELETING\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x12\r\n\tRESTORING\x10\x05\x12\x0c\n\x08DISABLED\x10\x06\x12\t\n\x05ERROR\x10\x07:\x87\x01\xeaA\x83\x01\n!netapp.googleapis.com/StoragePool\x12Cprojects/{project}/locations/{location}/storagePools/{storage_pool}*\x0cstoragePools2\x0bstoragePoolB\x18\n\x16_global_access_allowedB\x1e\n\x1c_enable_hot_tier_auto_resize"\xa8\x01\n\x1fValidateDirectoryServiceRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!netapp.googleapis.com/StoragePool\x12L\n\x16directory_service_type\x18\x02 \x01(\x0e2,.google.cloud.netapp.v1.DirectoryServiceTypeB\xb2\x01\n\x1acom.google.cloud.netapp.v1B\x10StoragePoolProtoP\x01Z2cloud.google.com/go/netapp/apiv1/netapppb;netapppb\xaa\x02\x16Google.Cloud.NetApp.V1\xca\x02\x16Google\\Cloud\\NetApp\\V1\xea\x02\x19Google::Cloud::NetApp::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.netapp.v1.storage_pool_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.netapp.v1B\x10StoragePoolProtoP\x01Z2cloud.google.com/go/netapp/apiv1/netapppb;netapppb\xaa\x02\x16Google.Cloud.NetApp.V1\xca\x02\x16Google\\Cloud\\NetApp\\V1\xea\x02\x19Google::Cloud::NetApp::V1'
    _globals['_GETSTORAGEPOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSTORAGEPOOLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!netapp.googleapis.com/StoragePool'
    _globals['_LISTSTORAGEPOOLSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSTORAGEPOOLSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!netapp.googleapis.com/StoragePool'
    _globals['_LISTSTORAGEPOOLSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTSTORAGEPOOLSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSTORAGEPOOLSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTSTORAGEPOOLSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSTORAGEPOOLSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTSTORAGEPOOLSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSTORAGEPOOLSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTSTORAGEPOOLSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_CREATESTORAGEPOOLREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESTORAGEPOOLREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!netapp.googleapis.com/StoragePool'
    _globals['_CREATESTORAGEPOOLREQUEST'].fields_by_name['storage_pool_id']._loaded_options = None
    _globals['_CREATESTORAGEPOOLREQUEST'].fields_by_name['storage_pool_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESTORAGEPOOLREQUEST'].fields_by_name['storage_pool']._loaded_options = None
    _globals['_CREATESTORAGEPOOLREQUEST'].fields_by_name['storage_pool']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESTORAGEPOOLREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESTORAGEPOOLREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESTORAGEPOOLREQUEST'].fields_by_name['storage_pool']._loaded_options = None
    _globals['_UPDATESTORAGEPOOLREQUEST'].fields_by_name['storage_pool']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESTORAGEPOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESTORAGEPOOLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!netapp.googleapis.com/StoragePool'
    _globals['_SWITCHACTIVEREPLICAZONEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_SWITCHACTIVEREPLICAZONEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!netapp.googleapis.com/StoragePool'
    _globals['_STORAGEPOOL_LABELSENTRY']._loaded_options = None
    _globals['_STORAGEPOOL_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_STORAGEPOOL'].fields_by_name['name']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_STORAGEPOOL'].fields_by_name['service_level']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['service_level']._serialized_options = b'\xe0A\x02'
    _globals['_STORAGEPOOL'].fields_by_name['capacity_gib']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['capacity_gib']._serialized_options = b'\xe0A\x02'
    _globals['_STORAGEPOOL'].fields_by_name['volume_capacity_gib']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['volume_capacity_gib']._serialized_options = b'\xe0A\x03'
    _globals['_STORAGEPOOL'].fields_by_name['volume_count']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['volume_count']._serialized_options = b'\xe0A\x03'
    _globals['_STORAGEPOOL'].fields_by_name['state']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_STORAGEPOOL'].fields_by_name['state_details']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['state_details']._serialized_options = b'\xe0A\x03'
    _globals['_STORAGEPOOL'].fields_by_name['create_time']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_STORAGEPOOL'].fields_by_name['description']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGEPOOL'].fields_by_name['labels']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGEPOOL'].fields_by_name['network']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['network']._serialized_options = b'\xe0A\x02\xfaA \n\x1ecompute.googleapis.com/Network'
    _globals['_STORAGEPOOL'].fields_by_name['active_directory']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['active_directory']._serialized_options = b"\xe0A\x01\xfaA'\n%netapp.googleapis.com/ActiveDirectory"
    _globals['_STORAGEPOOL'].fields_by_name['kms_config']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['kms_config']._serialized_options = b'\xe0A\x01\xfaA!\n\x1fnetapp.googleapis.com/KmsConfig'
    _globals['_STORAGEPOOL'].fields_by_name['ldap_enabled']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['ldap_enabled']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGEPOOL'].fields_by_name['psa_range']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['psa_range']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGEPOOL'].fields_by_name['encryption_type']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['encryption_type']._serialized_options = b'\xe0A\x03'
    _globals['_STORAGEPOOL'].fields_by_name['global_access_allowed']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['global_access_allowed']._serialized_options = b'\x18\x01'
    _globals['_STORAGEPOOL'].fields_by_name['allow_auto_tiering']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['allow_auto_tiering']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGEPOOL'].fields_by_name['replica_zone']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['replica_zone']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGEPOOL'].fields_by_name['zone']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['zone']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGEPOOL'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_STORAGEPOOL'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_STORAGEPOOL'].fields_by_name['custom_performance_enabled']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['custom_performance_enabled']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGEPOOL'].fields_by_name['total_throughput_mibps']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['total_throughput_mibps']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGEPOOL'].fields_by_name['total_iops']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['total_iops']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGEPOOL'].fields_by_name['hot_tier_size_gib']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['hot_tier_size_gib']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGEPOOL'].fields_by_name['enable_hot_tier_auto_resize']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['enable_hot_tier_auto_resize']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGEPOOL'].fields_by_name['qos_type']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['qos_type']._serialized_options = b'\xe0A\x01'
    _globals['_STORAGEPOOL'].fields_by_name['available_throughput_mibps']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['available_throughput_mibps']._serialized_options = b'\xe0A\x03'
    _globals['_STORAGEPOOL'].fields_by_name['cold_tier_size_used_gib']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['cold_tier_size_used_gib']._serialized_options = b'\xe0A\x03'
    _globals['_STORAGEPOOL'].fields_by_name['hot_tier_size_used_gib']._loaded_options = None
    _globals['_STORAGEPOOL'].fields_by_name['hot_tier_size_used_gib']._serialized_options = b'\xe0A\x03'
    _globals['_STORAGEPOOL']._loaded_options = None
    _globals['_STORAGEPOOL']._serialized_options = b'\xeaA\x83\x01\n!netapp.googleapis.com/StoragePool\x12Cprojects/{project}/locations/{location}/storagePools/{storage_pool}*\x0cstoragePools2\x0bstoragePool'
    _globals['_VALIDATEDIRECTORYSERVICEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_VALIDATEDIRECTORYSERVICEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!netapp.googleapis.com/StoragePool'
    _globals['_GETSTORAGEPOOLREQUEST']._serialized_start = 233
    _globals['_GETSTORAGEPOOLREQUEST']._serialized_end = 313
    _globals['_LISTSTORAGEPOOLSREQUEST']._serialized_start = 316
    _globals['_LISTSTORAGEPOOLSREQUEST']._serialized_end = 493
    _globals['_LISTSTORAGEPOOLSRESPONSE']._serialized_start = 496
    _globals['_LISTSTORAGEPOOLSRESPONSE']._serialized_end = 628
    _globals['_CREATESTORAGEPOOLREQUEST']._serialized_start = 631
    _globals['_CREATESTORAGEPOOLREQUEST']._serialized_end = 810
    _globals['_UPDATESTORAGEPOOLREQUEST']._serialized_start = 813
    _globals['_UPDATESTORAGEPOOLREQUEST']._serialized_end = 957
    _globals['_DELETESTORAGEPOOLREQUEST']._serialized_start = 959
    _globals['_DELETESTORAGEPOOLREQUEST']._serialized_end = 1042
    _globals['_SWITCHACTIVEREPLICAZONEREQUEST']._serialized_start = 1044
    _globals['_SWITCHACTIVEREPLICAZONEREQUEST']._serialized_end = 1133
    _globals['_STORAGEPOOL']._serialized_start = 1136
    _globals['_STORAGEPOOL']._serialized_end = 2772
    _globals['_STORAGEPOOL_LABELSENTRY']._serialized_start = 2406
    _globals['_STORAGEPOOL_LABELSENTRY']._serialized_end = 2451
    _globals['_STORAGEPOOL_STATE']._serialized_start = 2453
    _globals['_STORAGEPOOL_STATE']._serialized_end = 2576
    _globals['_VALIDATEDIRECTORYSERVICEREQUEST']._serialized_start = 2775
    _globals['_VALIDATEDIRECTORYSERVICEREQUEST']._serialized_end = 2943