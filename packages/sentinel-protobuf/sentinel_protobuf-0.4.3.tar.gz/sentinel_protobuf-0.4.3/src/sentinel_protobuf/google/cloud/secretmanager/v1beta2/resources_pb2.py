"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/secretmanager/v1beta2/resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/secretmanager/v1beta2/resources.proto\x12"google.cloud.secretmanager.v1beta2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x85\t\n\x06Secret\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12L\n\x0breplication\x18\x02 \x01(\x0b2/.google.cloud.secretmanager.v1beta2.ReplicationB\x06\xe0A\x05\xe0A\x01\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12F\n\x06labels\x18\x04 \x03(\x0b26.google.cloud.secretmanager.v1beta2.Secret.LabelsEntry\x12>\n\x06topics\x18\x05 \x03(\x0b2).google.cloud.secretmanager.v1beta2.TopicB\x03\xe0A\x01\x126\n\x0bexpire_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01H\x00\x12-\n\x03ttl\x18\x07 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x04H\x00\x12\x11\n\x04etag\x18\x08 \x01(\tB\x03\xe0A\x01\x12C\n\x08rotation\x18\t \x01(\x0b2,.google.cloud.secretmanager.v1beta2.RotationB\x03\xe0A\x01\x12\\\n\x0fversion_aliases\x18\x0b \x03(\x0b2>.google.cloud.secretmanager.v1beta2.Secret.VersionAliasesEntryB\x03\xe0A\x01\x12U\n\x0bannotations\x18\r \x03(\x0b2;.google.cloud.secretmanager.v1beta2.Secret.AnnotationsEntryB\x03\xe0A\x01\x12;\n\x13version_destroy_ttl\x18\x0e \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x12g\n\x1bcustomer_managed_encryption\x18\x0f \x01(\x0b2=.google.cloud.secretmanager.v1beta2.CustomerManagedEncryptionB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a5\n\x13VersionAliasesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x028\x01\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x99\x01\xeaA\x95\x01\n#secretmanager.googleapis.com/Secret\x12#projects/{project}/secrets/{secret}\x128projects/{project}/locations/{location}/secrets/{secret}*\x07secrets2\x06secretB\x0c\n\nexpiration"\xd1\x06\n\rSecretVersion\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x125\n\x0cdestroy_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12K\n\x05state\x18\x04 \x01(\x0e27.google.cloud.secretmanager.v1beta2.SecretVersion.StateB\x03\xe0A\x03\x12Q\n\x12replication_status\x18\x05 \x01(\x0b25.google.cloud.secretmanager.v1beta2.ReplicationStatus\x12\x11\n\x04etag\x18\x06 \x01(\tB\x03\xe0A\x03\x12.\n!client_specified_payload_checksum\x18\x07 \x01(\x08B\x03\xe0A\x03\x12?\n\x16scheduled_destroy_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12m\n\x1bcustomer_managed_encryption\x18\t \x01(\x0b2C.google.cloud.secretmanager.v1beta2.CustomerManagedEncryptionStatusB\x03\xe0A\x03"H\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\x0c\n\x08DISABLED\x10\x02\x12\r\n\tDESTROYED\x10\x03:\xe2\x01\xeaA\xde\x01\n*secretmanager.googleapis.com/SecretVersion\x12=projects/{project}/secrets/{secret}/versions/{secret_version}\x12Rprojects/{project}/locations/{location}/secrets/{secret}/versions/{secret_version}*\x0esecretVersions2\rsecretVersion"\xaa\x04\n\x0bReplication\x12N\n\tautomatic\x18\x01 \x01(\x0b29.google.cloud.secretmanager.v1beta2.Replication.AutomaticH\x00\x12S\n\x0cuser_managed\x18\x02 \x01(\x0b2;.google.cloud.secretmanager.v1beta2.Replication.UserManagedH\x00\x1at\n\tAutomatic\x12g\n\x1bcustomer_managed_encryption\x18\x01 \x01(\x0b2=.google.cloud.secretmanager.v1beta2.CustomerManagedEncryptionB\x03\xe0A\x01\x1a\xf0\x01\n\x0bUserManaged\x12Z\n\x08replicas\x18\x01 \x03(\x0b2C.google.cloud.secretmanager.v1beta2.Replication.UserManaged.ReplicaB\x03\xe0A\x02\x1a\x84\x01\n\x07Replica\x12\x10\n\x08location\x18\x01 \x01(\t\x12g\n\x1bcustomer_managed_encryption\x18\x02 \x01(\x0b2=.google.cloud.secretmanager.v1beta2.CustomerManagedEncryptionB\x03\xe0A\x01B\r\n\x0breplication"6\n\x19CustomerManagedEncryption\x12\x19\n\x0ckms_key_name\x18\x01 \x01(\tB\x03\xe0A\x02"\x85\x05\n\x11ReplicationStatus\x12Z\n\tautomatic\x18\x01 \x01(\x0b2E.google.cloud.secretmanager.v1beta2.ReplicationStatus.AutomaticStatusH\x00\x12_\n\x0cuser_managed\x18\x02 \x01(\x0b2G.google.cloud.secretmanager.v1beta2.ReplicationStatus.UserManagedStatusH\x00\x1a\x80\x01\n\x0fAutomaticStatus\x12m\n\x1bcustomer_managed_encryption\x18\x01 \x01(\x0b2C.google.cloud.secretmanager.v1beta2.CustomerManagedEncryptionStatusB\x03\xe0A\x03\x1a\x99\x02\n\x11UserManagedStatus\x12l\n\x08replicas\x18\x01 \x03(\x0b2U.google.cloud.secretmanager.v1beta2.ReplicationStatus.UserManagedStatus.ReplicaStatusB\x03\xe0A\x03\x1a\x95\x01\n\rReplicaStatus\x12\x15\n\x08location\x18\x01 \x01(\tB\x03\xe0A\x03\x12m\n\x1bcustomer_managed_encryption\x18\x02 \x01(\x0b2C.google.cloud.secretmanager.v1beta2.CustomerManagedEncryptionStatusB\x03\xe0A\x03B\x14\n\x12replication_status"D\n\x1fCustomerManagedEncryptionStatus\x12!\n\x14kms_key_version_name\x18\x01 \x01(\tB\x03\xe0A\x02"_\n\x05Topic\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02:C\xeaA@\n\x1bpubsub.googleapis.com/Topic\x12!projects/{project}/topics/{topic}"\x80\x01\n\x08Rotation\x12;\n\x12next_rotation_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x127\n\x0frotation_period\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x04"L\n\rSecretPayload\x12\x0c\n\x04data\x18\x01 \x01(\x0c\x12\x1d\n\x0bdata_crc32c\x18\x02 \x01(\x03B\x03\xe0A\x01H\x00\x88\x01\x01B\x0e\n\x0c_data_crc32cB\x80\x02\n&com.google.cloud.secretmanager.v1beta2B\x0eResourcesProtoP\x01ZLcloud.google.com/go/secretmanager/apiv1beta2/secretmanagerpb;secretmanagerpb\xa2\x02\x03GSM\xaa\x02"Google.Cloud.SecretManager.V1Beta2\xca\x02"Google\\Cloud\\SecretManager\\V1beta2\xea\x02%Google::Cloud::SecretManager::V1beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.secretmanager.v1beta2.resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.secretmanager.v1beta2B\x0eResourcesProtoP\x01ZLcloud.google.com/go/secretmanager/apiv1beta2/secretmanagerpb;secretmanagerpb\xa2\x02\x03GSM\xaa\x02"Google.Cloud.SecretManager.V1Beta2\xca\x02"Google\\Cloud\\SecretManager\\V1beta2\xea\x02%Google::Cloud::SecretManager::V1beta2'
    _globals['_SECRET_LABELSENTRY']._loaded_options = None
    _globals['_SECRET_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_SECRET_VERSIONALIASESENTRY']._loaded_options = None
    _globals['_SECRET_VERSIONALIASESENTRY']._serialized_options = b'8\x01'
    _globals['_SECRET_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_SECRET_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
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
    _globals['_TOPIC'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_TOPIC']._loaded_options = None
    _globals['_TOPIC']._serialized_options = b'\xeaA@\n\x1bpubsub.googleapis.com/Topic\x12!projects/{project}/topics/{topic}'
    _globals['_ROTATION'].fields_by_name['next_rotation_time']._loaded_options = None
    _globals['_ROTATION'].fields_by_name['next_rotation_time']._serialized_options = b'\xe0A\x01'
    _globals['_ROTATION'].fields_by_name['rotation_period']._loaded_options = None
    _globals['_ROTATION'].fields_by_name['rotation_period']._serialized_options = b'\xe0A\x04'
    _globals['_SECRETPAYLOAD'].fields_by_name['data_crc32c']._loaded_options = None
    _globals['_SECRETPAYLOAD'].fields_by_name['data_crc32c']._serialized_options = b'\xe0A\x01'
    _globals['_SECRET']._serialized_start = 216
    _globals['_SECRET']._serialized_end = 1373
    _globals['_SECRET_LABELSENTRY']._serialized_start = 1051
    _globals['_SECRET_LABELSENTRY']._serialized_end = 1096
    _globals['_SECRET_VERSIONALIASESENTRY']._serialized_start = 1098
    _globals['_SECRET_VERSIONALIASESENTRY']._serialized_end = 1151
    _globals['_SECRET_ANNOTATIONSENTRY']._serialized_start = 1153
    _globals['_SECRET_ANNOTATIONSENTRY']._serialized_end = 1203
    _globals['_SECRETVERSION']._serialized_start = 1376
    _globals['_SECRETVERSION']._serialized_end = 2225
    _globals['_SECRETVERSION_STATE']._serialized_start = 1924
    _globals['_SECRETVERSION_STATE']._serialized_end = 1996
    _globals['_REPLICATION']._serialized_start = 2228
    _globals['_REPLICATION']._serialized_end = 2782
    _globals['_REPLICATION_AUTOMATIC']._serialized_start = 2408
    _globals['_REPLICATION_AUTOMATIC']._serialized_end = 2524
    _globals['_REPLICATION_USERMANAGED']._serialized_start = 2527
    _globals['_REPLICATION_USERMANAGED']._serialized_end = 2767
    _globals['_REPLICATION_USERMANAGED_REPLICA']._serialized_start = 2635
    _globals['_REPLICATION_USERMANAGED_REPLICA']._serialized_end = 2767
    _globals['_CUSTOMERMANAGEDENCRYPTION']._serialized_start = 2784
    _globals['_CUSTOMERMANAGEDENCRYPTION']._serialized_end = 2838
    _globals['_REPLICATIONSTATUS']._serialized_start = 2841
    _globals['_REPLICATIONSTATUS']._serialized_end = 3486
    _globals['_REPLICATIONSTATUS_AUTOMATICSTATUS']._serialized_start = 3052
    _globals['_REPLICATIONSTATUS_AUTOMATICSTATUS']._serialized_end = 3180
    _globals['_REPLICATIONSTATUS_USERMANAGEDSTATUS']._serialized_start = 3183
    _globals['_REPLICATIONSTATUS_USERMANAGEDSTATUS']._serialized_end = 3464
    _globals['_REPLICATIONSTATUS_USERMANAGEDSTATUS_REPLICASTATUS']._serialized_start = 3315
    _globals['_REPLICATIONSTATUS_USERMANAGEDSTATUS_REPLICASTATUS']._serialized_end = 3464
    _globals['_CUSTOMERMANAGEDENCRYPTIONSTATUS']._serialized_start = 3488
    _globals['_CUSTOMERMANAGEDENCRYPTIONSTATUS']._serialized_end = 3556
    _globals['_TOPIC']._serialized_start = 3558
    _globals['_TOPIC']._serialized_end = 3653
    _globals['_ROTATION']._serialized_start = 3656
    _globals['_ROTATION']._serialized_end = 3784
    _globals['_SECRETPAYLOAD']._serialized_start = 3786
    _globals['_SECRETPAYLOAD']._serialized_end = 3862