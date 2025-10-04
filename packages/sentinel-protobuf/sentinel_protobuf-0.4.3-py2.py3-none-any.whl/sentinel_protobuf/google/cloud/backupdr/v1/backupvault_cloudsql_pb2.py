"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/backupdr/v1/backupvault_cloudsql.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/backupdr/v1/backupvault_cloudsql.proto\x12\x18google.cloud.backupdr.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe2\x01\n$CloudSqlInstanceDataSourceProperties\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x03\xfaA"\n sqladmin.googleapis.com/Instance\x12\'\n\x1adatabase_installed_version\x18\x02 \x01(\tB\x03\xe0A\x03\x12=\n\x14instance_create_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1a\n\rinstance_tier\x18\x05 \x01(\tB\x03\xe0A\x03"\xc5\x01\n CloudSqlInstanceBackupProperties\x12\'\n\x1adatabase_installed_version\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cfinal_backup\x18\x03 \x01(\x08B\x03\xe0A\x03\x12A\n\x0fsource_instance\x18\x04 \x01(\tB(\xe0A\x03\xfaA"\n sqladmin.googleapis.com/Instance\x12\x1a\n\rinstance_tier\x18\x06 \x01(\tB\x03\xe0A\x03"\xeb\x01\n-CloudSqlInstanceDataSourceReferenceProperties\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x03\xfaA"\n sqladmin.googleapis.com/Instance\x12\'\n\x1adatabase_installed_version\x18\x02 \x01(\tB\x03\xe0A\x03\x12=\n\x14instance_create_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1a\n\rinstance_tier\x18\x05 \x01(\tB\x03\xe0A\x03"\xcd\x01\n$CloudSqlInstanceInitializationConfig\x12\\\n\x07edition\x18\x01 \x01(\x0e2F.google.cloud.backupdr.v1.CloudSqlInstanceInitializationConfig.EditionB\x03\xe0A\x02"G\n\x07Edition\x12\x17\n\x13EDITION_UNSPECIFIED\x10\x00\x12\x0e\n\nENTERPRISE\x10\x01\x12\x13\n\x0fENTERPRISE_PLUS\x10\x02"p\n/CloudSqlInstanceBackupPlanAssociationProperties\x12=\n\x14instance_create_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03B\x96\x02\n\x1ccom.google.cloud.backupdr.v1B\x18BackupvaultCloudSqlProtoP\x01Z8cloud.google.com/go/backupdr/apiv1/backupdrpb;backupdrpb\xaa\x02\x18Google.Cloud.BackupDR.V1\xca\x02\x18Google\\Cloud\\BackupDR\\V1\xea\x02\x1bGoogle::Cloud::BackupDR::V1\xeaAK\n sqladmin.googleapis.com/Instance\x12\'projects/{project}/instances/{instance}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.backupdr.v1.backupvault_cloudsql_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n\x1ccom.google.cloud.backupdr.v1B\x18BackupvaultCloudSqlProtoP\x01Z8cloud.google.com/go/backupdr/apiv1/backupdrpb;backupdrpb\xaa\x02\x18Google.Cloud.BackupDR.V1\xca\x02\x18Google\\Cloud\\BackupDR\\V1\xea\x02\x1bGoogle::Cloud::BackupDR::V1\xeaAK\n sqladmin.googleapis.com/Instance\x12'projects/{project}/instances/{instance}"
    _globals['_CLOUDSQLINSTANCEDATASOURCEPROPERTIES'].fields_by_name['name']._loaded_options = None
    _globals['_CLOUDSQLINSTANCEDATASOURCEPROPERTIES'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xfaA"\n sqladmin.googleapis.com/Instance'
    _globals['_CLOUDSQLINSTANCEDATASOURCEPROPERTIES'].fields_by_name['database_installed_version']._loaded_options = None
    _globals['_CLOUDSQLINSTANCEDATASOURCEPROPERTIES'].fields_by_name['database_installed_version']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDSQLINSTANCEDATASOURCEPROPERTIES'].fields_by_name['instance_create_time']._loaded_options = None
    _globals['_CLOUDSQLINSTANCEDATASOURCEPROPERTIES'].fields_by_name['instance_create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDSQLINSTANCEDATASOURCEPROPERTIES'].fields_by_name['instance_tier']._loaded_options = None
    _globals['_CLOUDSQLINSTANCEDATASOURCEPROPERTIES'].fields_by_name['instance_tier']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDSQLINSTANCEBACKUPPROPERTIES'].fields_by_name['database_installed_version']._loaded_options = None
    _globals['_CLOUDSQLINSTANCEBACKUPPROPERTIES'].fields_by_name['database_installed_version']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDSQLINSTANCEBACKUPPROPERTIES'].fields_by_name['final_backup']._loaded_options = None
    _globals['_CLOUDSQLINSTANCEBACKUPPROPERTIES'].fields_by_name['final_backup']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDSQLINSTANCEBACKUPPROPERTIES'].fields_by_name['source_instance']._loaded_options = None
    _globals['_CLOUDSQLINSTANCEBACKUPPROPERTIES'].fields_by_name['source_instance']._serialized_options = b'\xe0A\x03\xfaA"\n sqladmin.googleapis.com/Instance'
    _globals['_CLOUDSQLINSTANCEBACKUPPROPERTIES'].fields_by_name['instance_tier']._loaded_options = None
    _globals['_CLOUDSQLINSTANCEBACKUPPROPERTIES'].fields_by_name['instance_tier']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDSQLINSTANCEDATASOURCEREFERENCEPROPERTIES'].fields_by_name['name']._loaded_options = None
    _globals['_CLOUDSQLINSTANCEDATASOURCEREFERENCEPROPERTIES'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xfaA"\n sqladmin.googleapis.com/Instance'
    _globals['_CLOUDSQLINSTANCEDATASOURCEREFERENCEPROPERTIES'].fields_by_name['database_installed_version']._loaded_options = None
    _globals['_CLOUDSQLINSTANCEDATASOURCEREFERENCEPROPERTIES'].fields_by_name['database_installed_version']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDSQLINSTANCEDATASOURCEREFERENCEPROPERTIES'].fields_by_name['instance_create_time']._loaded_options = None
    _globals['_CLOUDSQLINSTANCEDATASOURCEREFERENCEPROPERTIES'].fields_by_name['instance_create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDSQLINSTANCEDATASOURCEREFERENCEPROPERTIES'].fields_by_name['instance_tier']._loaded_options = None
    _globals['_CLOUDSQLINSTANCEDATASOURCEREFERENCEPROPERTIES'].fields_by_name['instance_tier']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDSQLINSTANCEINITIALIZATIONCONFIG'].fields_by_name['edition']._loaded_options = None
    _globals['_CLOUDSQLINSTANCEINITIALIZATIONCONFIG'].fields_by_name['edition']._serialized_options = b'\xe0A\x02'
    _globals['_CLOUDSQLINSTANCEBACKUPPLANASSOCIATIONPROPERTIES'].fields_by_name['instance_create_time']._loaded_options = None
    _globals['_CLOUDSQLINSTANCEBACKUPPLANASSOCIATIONPROPERTIES'].fields_by_name['instance_create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDSQLINSTANCEDATASOURCEPROPERTIES']._serialized_start = 175
    _globals['_CLOUDSQLINSTANCEDATASOURCEPROPERTIES']._serialized_end = 401
    _globals['_CLOUDSQLINSTANCEBACKUPPROPERTIES']._serialized_start = 404
    _globals['_CLOUDSQLINSTANCEBACKUPPROPERTIES']._serialized_end = 601
    _globals['_CLOUDSQLINSTANCEDATASOURCEREFERENCEPROPERTIES']._serialized_start = 604
    _globals['_CLOUDSQLINSTANCEDATASOURCEREFERENCEPROPERTIES']._serialized_end = 839
    _globals['_CLOUDSQLINSTANCEINITIALIZATIONCONFIG']._serialized_start = 842
    _globals['_CLOUDSQLINSTANCEINITIALIZATIONCONFIG']._serialized_end = 1047
    _globals['_CLOUDSQLINSTANCEINITIALIZATIONCONFIG_EDITION']._serialized_start = 976
    _globals['_CLOUDSQLINSTANCEINITIALIZATIONCONFIG_EDITION']._serialized_end = 1047
    _globals['_CLOUDSQLINSTANCEBACKUPPLANASSOCIATIONPROPERTIES']._serialized_start = 1049
    _globals['_CLOUDSQLINSTANCEBACKUPPLANASSOCIATIONPROPERTIES']._serialized_end = 1161