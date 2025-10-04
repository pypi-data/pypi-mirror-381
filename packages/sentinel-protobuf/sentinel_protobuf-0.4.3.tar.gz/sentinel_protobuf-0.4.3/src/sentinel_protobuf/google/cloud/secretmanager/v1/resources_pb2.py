"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/secretmanager/v1/resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/secretmanager/v1/resources.proto\x12\x1dgoogle.cloud.secretmanager.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd9\t\n\x06Secret\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12G\n\x0breplication\x18\x02 \x01(\x0b2*.google.cloud.secretmanager.v1.ReplicationB\x06\xe0A\x05\xe0A\x01\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12A\n\x06labels\x18\x04 \x03(\x0b21.google.cloud.secretmanager.v1.Secret.LabelsEntry\x129\n\x06topics\x18\x05 \x03(\x0b2$.google.cloud.secretmanager.v1.TopicB\x03\xe0A\x01\x126\n\x0bexpire_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01H\x00\x12-\n\x03ttl\x18\x07 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x04H\x00\x12\x11\n\x04etag\x18\x08 \x01(\tB\x03\xe0A\x01\x12>\n\x08rotation\x18\t \x01(\x0b2\'.google.cloud.secretmanager.v1.RotationB\x03\xe0A\x01\x12W\n\x0fversion_aliases\x18\x0b \x03(\x0b29.google.cloud.secretmanager.v1.Secret.VersionAliasesEntryB\x03\xe0A\x01\x12P\n\x0bannotations\x18\r \x03(\x0b26.google.cloud.secretmanager.v1.Secret.AnnotationsEntryB\x03\xe0A\x01\x12;\n\x13version_destroy_ttl\x18\x0e \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x12b\n\x1bcustomer_managed_encryption\x18\x0f \x01(\x0b28.google.cloud.secretmanager.v1.CustomerManagedEncryptionB\x03\xe0A\x01\x12H\n\x04tags\x18\x10 \x03(\x0b2/.google.cloud.secretmanager.v1.Secret.TagsEntryB\t\xe0A\x04\xe0A\x05\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a5\n\x13VersionAliasesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x028\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x99\x01\xeaA\x95\x01\n#secretmanager.googleapis.com/Secret\x12#projects/{project}/secrets/{secret}\x128projects/{project}/locations/{location}/secrets/{secret}*\x07secrets2\x06secretB\x0c\n\nexpiration"\xc2\x06\n\rSecretVersion\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x125\n\x0cdestroy_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12F\n\x05state\x18\x04 \x01(\x0e22.google.cloud.secretmanager.v1.SecretVersion.StateB\x03\xe0A\x03\x12L\n\x12replication_status\x18\x05 \x01(\x0b20.google.cloud.secretmanager.v1.ReplicationStatus\x12\x11\n\x04etag\x18\x06 \x01(\tB\x03\xe0A\x03\x12.\n!client_specified_payload_checksum\x18\x07 \x01(\x08B\x03\xe0A\x03\x12?\n\x16scheduled_destroy_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12h\n\x1bcustomer_managed_encryption\x18\t \x01(\x0b2>.google.cloud.secretmanager.v1.CustomerManagedEncryptionStatusB\x03\xe0A\x03"H\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\x0c\n\x08DISABLED\x10\x02\x12\r\n\tDESTROYED\x10\x03:\xe2\x01\xeaA\xde\x01\n*secretmanager.googleapis.com/SecretVersion\x12=projects/{project}/secrets/{secret}/versions/{secret_version}\x12Rprojects/{project}/locations/{location}/secrets/{secret}/versions/{secret_version}*\x0esecretVersions2\rsecretVersion"\x90\x04\n\x0bReplication\x12I\n\tautomatic\x18\x01 \x01(\x0b24.google.cloud.secretmanager.v1.Replication.AutomaticH\x00\x12N\n\x0cuser_managed\x18\x02 \x01(\x0b26.google.cloud.secretmanager.v1.Replication.UserManagedH\x00\x1ao\n\tAutomatic\x12b\n\x1bcustomer_managed_encryption\x18\x01 \x01(\x0b28.google.cloud.secretmanager.v1.CustomerManagedEncryptionB\x03\xe0A\x01\x1a\xe5\x01\n\x0bUserManaged\x12U\n\x08replicas\x18\x01 \x03(\x0b2>.google.cloud.secretmanager.v1.Replication.UserManaged.ReplicaB\x03\xe0A\x02\x1a\x7f\n\x07Replica\x12\x10\n\x08location\x18\x01 \x01(\t\x12b\n\x1bcustomer_managed_encryption\x18\x02 \x01(\x0b28.google.cloud.secretmanager.v1.CustomerManagedEncryptionB\x03\xe0A\x01B\r\n\x0breplication"6\n\x19CustomerManagedEncryption\x12\x19\n\x0ckms_key_name\x18\x01 \x01(\tB\x03\xe0A\x02"\xeb\x04\n\x11ReplicationStatus\x12U\n\tautomatic\x18\x01 \x01(\x0b2@.google.cloud.secretmanager.v1.ReplicationStatus.AutomaticStatusH\x00\x12Z\n\x0cuser_managed\x18\x02 \x01(\x0b2B.google.cloud.secretmanager.v1.ReplicationStatus.UserManagedStatusH\x00\x1a{\n\x0fAutomaticStatus\x12h\n\x1bcustomer_managed_encryption\x18\x01 \x01(\x0b2>.google.cloud.secretmanager.v1.CustomerManagedEncryptionStatusB\x03\xe0A\x03\x1a\x8f\x02\n\x11UserManagedStatus\x12g\n\x08replicas\x18\x01 \x03(\x0b2P.google.cloud.secretmanager.v1.ReplicationStatus.UserManagedStatus.ReplicaStatusB\x03\xe0A\x03\x1a\x90\x01\n\rReplicaStatus\x12\x15\n\x08location\x18\x01 \x01(\tB\x03\xe0A\x03\x12h\n\x1bcustomer_managed_encryption\x18\x02 \x01(\x0b2>.google.cloud.secretmanager.v1.CustomerManagedEncryptionStatusB\x03\xe0A\x03B\x14\n\x12replication_status"D\n\x1fCustomerManagedEncryptionStatus\x12!\n\x14kms_key_version_name\x18\x01 \x01(\tB\x03\xe0A\x02"_\n\x05Topic\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08:C\xeaA@\n\x1bpubsub.googleapis.com/Topic\x12!projects/{project}/topics/{topic}"\x80\x01\n\x08Rotation\x12;\n\x12next_rotation_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x127\n\x0frotation_period\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x04"L\n\rSecretPayload\x12\x0c\n\x04data\x18\x01 \x01(\x0c\x12\x1d\n\x0bdata_crc32c\x18\x02 \x01(\x03B\x03\xe0A\x01H\x00\x88\x01\x01B\x0e\n\x0c_data_crc32cB\xe7\x01\n!com.google.cloud.secretmanager.v1B\x0eResourcesProtoP\x01ZGcloud.google.com/go/secretmanager/apiv1/secretmanagerpb;secretmanagerpb\xa2\x02\x03GSM\xaa\x02\x1dGoogle.Cloud.SecretManager.V1\xca\x02\x1dGoogle\\Cloud\\SecretManager\\V1\xea\x02 Google::Cloud::SecretManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.secretmanager.v1.resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.secretmanager.v1B\x0eResourcesProtoP\x01ZGcloud.google.com/go/secretmanager/apiv1/secretmanagerpb;secretmanagerpb\xa2\x02\x03GSM\xaa\x02\x1dGoogle.Cloud.SecretManager.V1\xca\x02\x1dGoogle\\Cloud\\SecretManager\\V1\xea\x02 Google::Cloud::SecretManager::V1'
    _globals['_SECRET_LABELSENTRY']._loaded_options = None
    _globals['_SECRET_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_SECRET_VERSIONALIASESENTRY']._loaded_options = None
    _globals['_SECRET_VERSIONALIASESENTRY']._serialized_options = b'8\x01'
    _globals['_SECRET_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_SECRET_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_SECRET_TAGSENTRY']._loaded_options = None
    _globals['_SECRET_TAGSENTRY']._serialized_options = b'8\x01'
    _globals['_SECRET'].fields_by_name['name']._loaded_options = None
    _globals['_SECRET'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_SECRET'].fields_by_name['replication']._loaded_options = None
    _globals['_SECRET'].fields_by_name['replication']._serialized_options = b'\xe0A\x05\xe0A\x01'
    _globals['_SECRET'].fields_by_name['create_time']._loaded_options = None
    _globals['_SECRET'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SECRET'].fields_by_name['topics']._loaded_options = None
    _globals['_SECRET'].fields_by_name['topics']._serialized_options = b'\xe0A\x01'
    _globals['_SECRET'].fields_by_name['expire_time']._loaded_options = None
    _globals['_SECRET'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x01'
    _globals['_SECRET'].fields_by_name['ttl']._loaded_options = None
    _globals['_SECRET'].fields_by_name['ttl']._serialized_options = b'\xe0A\x04'
    _globals['_SECRET'].fields_by_name['etag']._loaded_options = None
    _globals['_SECRET'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_SECRET'].fields_by_name['rotation']._loaded_options = None
    _globals['_SECRET'].fields_by_name['rotation']._serialized_options = b'\xe0A\x01'
    _globals['_SECRET'].fields_by_name['version_aliases']._loaded_options = None
    _globals['_SECRET'].fields_by_name['version_aliases']._serialized_options = b'\xe0A\x01'
    _globals['_SECRET'].fields_by_name['annotations']._loaded_options = None
    _globals['_SECRET'].fields_by_name['annotations']._serialized_options = b'\xe0A\x01'
    _globals['_SECRET'].fields_by_name['version_destroy_ttl']._loaded_options = None
    _globals['_SECRET'].fields_by_name['version_destroy_ttl']._serialized_options = b'\xe0A\x01'
    _globals['_SECRET'].fields_by_name['customer_managed_encryption']._loaded_options = None
    _globals['_SECRET'].fields_by_name['customer_managed_encryption']._serialized_options = b'\xe0A\x01'
    _globals['_SECRET'].fields_by_name['tags']._loaded_options = None
    _globals['_SECRET'].fields_by_name['tags']._serialized_options = b'\xe0A\x04\xe0A\x05\xe0A\x01'
    _globals['_SECRET']._loaded_options = None
    _globals['_SECRET']._serialized_options = b'\xeaA\x95\x01\n#secretmanager.googleapis.com/Secret\x12#projects/{project}/secrets/{secret}\x128projects/{project}/locations/{location}/secrets/{secret}*\x07secrets2\x06secret'
    _globals['_SECRETVERSION'].fields_by_name['name']._loaded_options = None
    _globals['_SECRETVERSION'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_SECRETVERSION'].fields_by_name['create_time']._loaded_options = None
    _globals['_SECRETVERSION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SECRETVERSION'].fields_by_name['destroy_time']._loaded_options = None
    _globals['_SECRETVERSION'].fields_by_name['destroy_time']._serialized_options = b'\xe0A\x03'
    _globals['_SECRETVERSION'].fields_by_name['state']._loaded_options = None
    _globals['_SECRETVERSION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_SECRETVERSION'].fields_by_name['etag']._loaded_options = None
    _globals['_SECRETVERSION'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_SECRETVERSION'].fields_by_name['client_specified_payload_checksum']._loaded_options = None
    _globals['_SECRETVERSION'].fields_by_name['client_specified_payload_checksum']._serialized_options = b'\xe0A\x03'
    _globals['_SECRETVERSION'].fields_by_name['scheduled_destroy_time']._loaded_options = None
    _globals['_SECRETVERSION'].fields_by_name['scheduled_destroy_time']._serialized_options = b'\xe0A\x03'
    _globals['_SECRETVERSION'].fields_by_name['customer_managed_encryption']._loaded_options = None
    _globals['_SECRETVERSION'].fields_by_name['customer_managed_encryption']._serialized_options = b'\xe0A\x03'
    _globals['_SECRETVERSION']._loaded_options = None
    _globals['_SECRETVERSION']._serialized_options = b'\xeaA\xde\x01\n*secretmanager.googleapis.com/SecretVersion\x12=projects/{project}/secrets/{secret}/versions/{secret_version}\x12Rprojects/{project}/locations/{location}/secrets/{secret}/versions/{secret_version}*\x0esecretVersions2\rsecretVersion'
    _globals['_REPLICATION_AUTOMATIC'].fields_by_name['customer_managed_encryption']._loaded_options = None
    _globals['_REPLICATION_AUTOMATIC'].fields_by_name['customer_managed_encryption']._serialized_options = b'\xe0A\x01'
    _globals['_REPLICATION_USERMANAGED_REPLICA'].fields_by_name['customer_managed_encryption']._loaded_options = None
    _globals['_REPLICATION_USERMANAGED_REPLICA'].fields_by_name['customer_managed_encryption']._serialized_options = b'\xe0A\x01'
    _globals['_REPLICATION_USERMANAGED'].fields_by_name['replicas']._loaded_options = None
    _globals['_REPLICATION_USERMANAGED'].fields_by_name['replicas']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMERMANAGEDENCRYPTION'].fields_by_name['kms_key_name']._loaded_options = None
    _globals['_CUSTOMERMANAGEDENCRYPTION'].fields_by_name['kms_key_name']._serialized_options = b'\xe0A\x02'
    _globals['_REPLICATIONSTATUS_AUTOMATICSTATUS'].fields_by_name['customer_managed_encryption']._loaded_options = None
    _globals['_REPLICATIONSTATUS_AUTOMATICSTATUS'].fields_by_name['customer_managed_encryption']._serialized_options = b'\xe0A\x03'
    _globals['_REPLICATIONSTATUS_USERMANAGEDSTATUS_REPLICASTATUS'].fields_by_name['location']._loaded_options = None
    _globals['_REPLICATIONSTATUS_USERMANAGEDSTATUS_REPLICASTATUS'].fields_by_name['location']._serialized_options = b'\xe0A\x03'
    _globals['_REPLICATIONSTATUS_USERMANAGEDSTATUS_REPLICASTATUS'].fields_by_name['customer_managed_encryption']._loaded_options = None
    _globals['_REPLICATIONSTATUS_USERMANAGEDSTATUS_REPLICASTATUS'].fields_by_name['customer_managed_encryption']._serialized_options = b'\xe0A\x03'
    _globals['_REPLICATIONSTATUS_USERMANAGEDSTATUS'].fields_by_name['replicas']._loaded_options = None
    _globals['_REPLICATIONSTATUS_USERMANAGEDSTATUS'].fields_by_name['replicas']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERMANAGEDENCRYPTIONSTATUS'].fields_by_name['kms_key_version_name']._loaded_options = None
    _globals['_CUSTOMERMANAGEDENCRYPTIONSTATUS'].fields_by_name['kms_key_version_name']._serialized_options = b'\xe0A\x02'
    _globals['_TOPIC'].fields_by_name['name']._loaded_options = None
    _globals['_TOPIC'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_TOPIC']._loaded_options = None
    _globals['_TOPIC']._serialized_options = b'\xeaA@\n\x1bpubsub.googleapis.com/Topic\x12!projects/{project}/topics/{topic}'
    _globals['_ROTATION'].fields_by_name['next_rotation_time']._loaded_options = None
    _globals['_ROTATION'].fields_by_name['next_rotation_time']._serialized_options = b'\xe0A\x01'
    _globals['_ROTATION'].fields_by_name['rotation_period']._loaded_options = None
    _globals['_ROTATION'].fields_by_name['rotation_period']._serialized_options = b'\xe0A\x04'
    _globals['_SECRETPAYLOAD'].fields_by_name['data_crc32c']._loaded_options = None
    _globals['_SECRETPAYLOAD'].fields_by_name['data_crc32c']._serialized_options = b'\xe0A\x01'
    _globals['_SECRET']._serialized_start = 206
    _globals['_SECRET']._serialized_end = 1447
    _globals['_SECRET_LABELSENTRY']._serialized_start = 1080
    _globals['_SECRET_LABELSENTRY']._serialized_end = 1125
    _globals['_SECRET_VERSIONALIASESENTRY']._serialized_start = 1127
    _globals['_SECRET_VERSIONALIASESENTRY']._serialized_end = 1180
    _globals['_SECRET_ANNOTATIONSENTRY']._serialized_start = 1182
    _globals['_SECRET_ANNOTATIONSENTRY']._serialized_end = 1232
    _globals['_SECRET_TAGSENTRY']._serialized_start = 1234
    _globals['_SECRET_TAGSENTRY']._serialized_end = 1277
    _globals['_SECRETVERSION']._serialized_start = 1450
    _globals['_SECRETVERSION']._serialized_end = 2284
    _globals['_SECRETVERSION_STATE']._serialized_start = 1983
    _globals['_SECRETVERSION_STATE']._serialized_end = 2055
    _globals['_REPLICATION']._serialized_start = 2287
    _globals['_REPLICATION']._serialized_end = 2815
    _globals['_REPLICATION_AUTOMATIC']._serialized_start = 2457
    _globals['_REPLICATION_AUTOMATIC']._serialized_end = 2568
    _globals['_REPLICATION_USERMANAGED']._serialized_start = 2571
    _globals['_REPLICATION_USERMANAGED']._serialized_end = 2800
    _globals['_REPLICATION_USERMANAGED_REPLICA']._serialized_start = 2673
    _globals['_REPLICATION_USERMANAGED_REPLICA']._serialized_end = 2800
    _globals['_CUSTOMERMANAGEDENCRYPTION']._serialized_start = 2817
    _globals['_CUSTOMERMANAGEDENCRYPTION']._serialized_end = 2871
    _globals['_REPLICATIONSTATUS']._serialized_start = 2874
    _globals['_REPLICATIONSTATUS']._serialized_end = 3493
    _globals['_REPLICATIONSTATUS_AUTOMATICSTATUS']._serialized_start = 3074
    _globals['_REPLICATIONSTATUS_AUTOMATICSTATUS']._serialized_end = 3197
    _globals['_REPLICATIONSTATUS_USERMANAGEDSTATUS']._serialized_start = 3200
    _globals['_REPLICATIONSTATUS_USERMANAGEDSTATUS']._serialized_end = 3471
    _globals['_REPLICATIONSTATUS_USERMANAGEDSTATUS_REPLICASTATUS']._serialized_start = 3327
    _globals['_REPLICATIONSTATUS_USERMANAGEDSTATUS_REPLICASTATUS']._serialized_end = 3471
    _globals['_CUSTOMERMANAGEDENCRYPTIONSTATUS']._serialized_start = 3495
    _globals['_CUSTOMERMANAGEDENCRYPTIONSTATUS']._serialized_end = 3563
    _globals['_TOPIC']._serialized_start = 3565
    _globals['_TOPIC']._serialized_end = 3660
    _globals['_ROTATION']._serialized_start = 3663
    _globals['_ROTATION']._serialized_end = 3791
    _globals['_SECRETPAYLOAD']._serialized_start = 3793
    _globals['_SECRETPAYLOAD']._serialized_end = 3869