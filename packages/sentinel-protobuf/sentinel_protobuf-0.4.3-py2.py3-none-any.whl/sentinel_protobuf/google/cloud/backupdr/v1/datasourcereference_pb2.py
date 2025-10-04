"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/backupdr/v1/datasourcereference.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.backupdr.v1 import backupvault_pb2 as google_dot_cloud_dot_backupdr_dot_v1_dot_backupvault__pb2
from .....google.cloud.backupdr.v1 import backupvault_cloudsql_pb2 as google_dot_cloud_dot_backupdr_dot_v1_dot_backupvault__cloudsql__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/backupdr/v1/datasourcereference.proto\x12\x18google.cloud.backupdr.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/cloud/backupdr/v1/backupvault.proto\x1a3google/cloud/backupdr/v1/backupvault_cloudsql.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x9a\x05\n\x13DataSourceReference\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12?\n\x0bdata_source\x18\x02 \x01(\tB*\xe0A\x03\xfaA$\n"backupdr.googleapis.com/DataSource\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12Y\n\x1fdata_source_backup_config_state\x18\x04 \x01(\x0e2+.google.cloud.backupdr.v1.BackupConfigStateB\x03\xe0A\x03\x12%\n\x18data_source_backup_count\x18\x05 \x01(\x03B\x03\xe0A\x03\x12a\n\x1edata_source_backup_config_info\x18\x06 \x01(\x0b24.google.cloud.backupdr.v1.DataSourceBackupConfigInfoB\x03\xe0A\x03\x12_\n\x1ddata_source_gcp_resource_info\x18\x07 \x01(\x0b23.google.cloud.backupdr.v1.DataSourceGcpResourceInfoB\x03\xe0A\x03:\xb2\x01\xeaA\xae\x01\n+backupdr.googleapis.com/DataSourceReference\x12Tprojects/{project}/locations/{location}/dataSourceReferences/{data_source_reference}*\x14dataSourceReferences2\x13dataSourceReference"\xca\x01\n\x1aDataSourceBackupConfigInfo\x12Z\n\x11last_backup_state\x18\x01 \x01(\x0e2:.google.cloud.backupdr.v1.BackupConfigInfo.LastBackupStateB\x03\xe0A\x03\x12P\n\'last_successful_backup_consistency_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"\xf2\x01\n\x19DataSourceGcpResourceInfo\x12\x1d\n\x10gcp_resourcename\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04type\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x15\n\x08location\x18\x03 \x01(\tB\x03\xe0A\x03\x12u\n\x1dcloud_sql_instance_properties\x18\x04 \x01(\x0b2G.google.cloud.backupdr.v1.CloudSqlInstanceDataSourceReferencePropertiesB\x03\xe0A\x03H\x00B\x15\n\x13resource_properties"b\n\x1dGetDataSourceReferenceRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+backupdr.googleapis.com/DataSourceReference"\xef\x01\n/FetchDataSourceReferencesForResourceTypeRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+backupdr.googleapis.com/DataSourceReference\x12\x1a\n\rresource_type\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x06 \x01(\tB\x03\xe0A\x01"\x9a\x01\n0FetchDataSourceReferencesForResourceTypeResponse\x12M\n\x16data_source_references\x18\x01 \x03(\x0b2-.google.cloud.backupdr.v1.DataSourceReference\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\tB\xc8\x01\n\x1ccom.google.cloud.backupdr.v1B\x18DataSourceReferenceProtoP\x01Z8cloud.google.com/go/backupdr/apiv1/backupdrpb;backupdrpb\xaa\x02\x18Google.Cloud.BackupDR.V1\xca\x02\x18Google\\Cloud\\BackupDR\\V1\xea\x02\x1bGoogle::Cloud::BackupDR::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.backupdr.v1.datasourcereference_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.backupdr.v1B\x18DataSourceReferenceProtoP\x01Z8cloud.google.com/go/backupdr/apiv1/backupdrpb;backupdrpb\xaa\x02\x18Google.Cloud.BackupDR.V1\xca\x02\x18Google\\Cloud\\BackupDR\\V1\xea\x02\x1bGoogle::Cloud::BackupDR::V1'
    _globals['_DATASOURCEREFERENCE'].fields_by_name['name']._loaded_options = None
    _globals['_DATASOURCEREFERENCE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_DATASOURCEREFERENCE'].fields_by_name['data_source']._loaded_options = None
    _globals['_DATASOURCEREFERENCE'].fields_by_name['data_source']._serialized_options = b'\xe0A\x03\xfaA$\n"backupdr.googleapis.com/DataSource'
    _globals['_DATASOURCEREFERENCE'].fields_by_name['create_time']._loaded_options = None
    _globals['_DATASOURCEREFERENCE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATASOURCEREFERENCE'].fields_by_name['data_source_backup_config_state']._loaded_options = None
    _globals['_DATASOURCEREFERENCE'].fields_by_name['data_source_backup_config_state']._serialized_options = b'\xe0A\x03'
    _globals['_DATASOURCEREFERENCE'].fields_by_name['data_source_backup_count']._loaded_options = None
    _globals['_DATASOURCEREFERENCE'].fields_by_name['data_source_backup_count']._serialized_options = b'\xe0A\x03'
    _globals['_DATASOURCEREFERENCE'].fields_by_name['data_source_backup_config_info']._loaded_options = None
    _globals['_DATASOURCEREFERENCE'].fields_by_name['data_source_backup_config_info']._serialized_options = b'\xe0A\x03'
    _globals['_DATASOURCEREFERENCE'].fields_by_name['data_source_gcp_resource_info']._loaded_options = None
    _globals['_DATASOURCEREFERENCE'].fields_by_name['data_source_gcp_resource_info']._serialized_options = b'\xe0A\x03'
    _globals['_DATASOURCEREFERENCE']._loaded_options = None
    _globals['_DATASOURCEREFERENCE']._serialized_options = b'\xeaA\xae\x01\n+backupdr.googleapis.com/DataSourceReference\x12Tprojects/{project}/locations/{location}/dataSourceReferences/{data_source_reference}*\x14dataSourceReferences2\x13dataSourceReference'
    _globals['_DATASOURCEBACKUPCONFIGINFO'].fields_by_name['last_backup_state']._loaded_options = None
    _globals['_DATASOURCEBACKUPCONFIGINFO'].fields_by_name['last_backup_state']._serialized_options = b'\xe0A\x03'
    _globals['_DATASOURCEBACKUPCONFIGINFO'].fields_by_name['last_successful_backup_consistency_time']._loaded_options = None
    _globals['_DATASOURCEBACKUPCONFIGINFO'].fields_by_name['last_successful_backup_consistency_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATASOURCEGCPRESOURCEINFO'].fields_by_name['gcp_resourcename']._loaded_options = None
    _globals['_DATASOURCEGCPRESOURCEINFO'].fields_by_name['gcp_resourcename']._serialized_options = b'\xe0A\x03'
    _globals['_DATASOURCEGCPRESOURCEINFO'].fields_by_name['type']._loaded_options = None
    _globals['_DATASOURCEGCPRESOURCEINFO'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_DATASOURCEGCPRESOURCEINFO'].fields_by_name['location']._loaded_options = None
    _globals['_DATASOURCEGCPRESOURCEINFO'].fields_by_name['location']._serialized_options = b'\xe0A\x03'
    _globals['_DATASOURCEGCPRESOURCEINFO'].fields_by_name['cloud_sql_instance_properties']._loaded_options = None
    _globals['_DATASOURCEGCPRESOURCEINFO'].fields_by_name['cloud_sql_instance_properties']._serialized_options = b'\xe0A\x03'
    _globals['_GETDATASOURCEREFERENCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATASOURCEREFERENCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+backupdr.googleapis.com/DataSourceReference'
    _globals['_FETCHDATASOURCEREFERENCESFORRESOURCETYPEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_FETCHDATASOURCEREFERENCESFORRESOURCETYPEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+backupdr.googleapis.com/DataSourceReference'
    _globals['_FETCHDATASOURCEREFERENCESFORRESOURCETYPEREQUEST'].fields_by_name['resource_type']._loaded_options = None
    _globals['_FETCHDATASOURCEREFERENCESFORRESOURCETYPEREQUEST'].fields_by_name['resource_type']._serialized_options = b'\xe0A\x02'
    _globals['_FETCHDATASOURCEREFERENCESFORRESOURCETYPEREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_FETCHDATASOURCEREFERENCESFORRESOURCETYPEREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_FETCHDATASOURCEREFERENCESFORRESOURCETYPEREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_FETCHDATASOURCEREFERENCESFORRESOURCETYPEREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_FETCHDATASOURCEREFERENCESFORRESOURCETYPEREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_FETCHDATASOURCEREFERENCESFORRESOURCETYPEREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_FETCHDATASOURCEREFERENCESFORRESOURCETYPEREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_FETCHDATASOURCEREFERENCESFORRESOURCETYPEREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_DATASOURCEREFERENCE']._serialized_start = 271
    _globals['_DATASOURCEREFERENCE']._serialized_end = 937
    _globals['_DATASOURCEBACKUPCONFIGINFO']._serialized_start = 940
    _globals['_DATASOURCEBACKUPCONFIGINFO']._serialized_end = 1142
    _globals['_DATASOURCEGCPRESOURCEINFO']._serialized_start = 1145
    _globals['_DATASOURCEGCPRESOURCEINFO']._serialized_end = 1387
    _globals['_GETDATASOURCEREFERENCEREQUEST']._serialized_start = 1389
    _globals['_GETDATASOURCEREFERENCEREQUEST']._serialized_end = 1487
    _globals['_FETCHDATASOURCEREFERENCESFORRESOURCETYPEREQUEST']._serialized_start = 1490
    _globals['_FETCHDATASOURCEREFERENCESFORRESOURCETYPEREQUEST']._serialized_end = 1729
    _globals['_FETCHDATASOURCEREFERENCESFORRESOURCETYPERESPONSE']._serialized_start = 1732
    _globals['_FETCHDATASOURCEREFERENCESFORRESOURCETYPERESPONSE']._serialized_end = 1886