"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/backupdr/v1/backupdr.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.backupdr.v1 import backupplan_pb2 as google_dot_cloud_dot_backupdr_dot_v1_dot_backupplan__pb2
from .....google.cloud.backupdr.v1 import backupplanassociation_pb2 as google_dot_cloud_dot_backupdr_dot_v1_dot_backupplanassociation__pb2
from .....google.cloud.backupdr.v1 import backupvault_pb2 as google_dot_cloud_dot_backupdr_dot_v1_dot_backupvault__pb2
from .....google.cloud.backupdr.v1 import backupvault_cloudsql_pb2 as google_dot_cloud_dot_backupdr_dot_v1_dot_backupvault__cloudsql__pb2
from .....google.cloud.backupdr.v1 import datasourcereference_pb2 as google_dot_cloud_dot_backupdr_dot_v1_dot_datasourcereference__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/backupdr/v1/backupdr.proto\x12\x18google.cloud.backupdr.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/backupdr/v1/backupplan.proto\x1a4google/cloud/backupdr/v1/backupplanassociation.proto\x1a*google/cloud/backupdr/v1/backupvault.proto\x1a3google/cloud/backupdr/v1/backupvault_cloudsql.proto\x1a2google/cloud/backupdr/v1/datasourcereference.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xbe\x01\n\rNetworkConfig\x12\x14\n\x07network\x18\x01 \x01(\tB\x03\xe0A\x01\x12N\n\x0cpeering_mode\x18\x02 \x01(\x0e23.google.cloud.backupdr.v1.NetworkConfig.PeeringModeB\x03\xe0A\x01"G\n\x0bPeeringMode\x12\x1c\n\x18PEERING_MODE_UNSPECIFIED\x10\x00\x12\x1a\n\x16PRIVATE_SERVICE_ACCESS\x10\x01"6\n\rManagementURI\x12\x13\n\x06web_ui\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x10\n\x03api\x18\x02 \x01(\tB\x03\xe0A\x03"w\n#WorkforceIdentityBasedManagementURI\x12\'\n\x1afirst_party_management_uri\x18\x01 \x01(\tB\x03\xe0A\x03\x12\'\n\x1athird_party_management_uri\x18\x02 \x01(\tB\x03\xe0A\x03"|\n$WorkforceIdentityBasedOAuth2ClientID\x12)\n\x1cfirst_party_oauth2_client_id\x18\x01 \x01(\tB\x03\xe0A\x03\x12)\n\x1cthird_party_oauth2_client_id\x18\x02 \x01(\tB\x03\xe0A\x03"\xd1\n\n\x10ManagementServer\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x08\x12\x18\n\x0bdescription\x18\t \x01(\tB\x03\xe0A\x01\x12K\n\x06labels\x18\x04 \x03(\x0b26.google.cloud.backupdr.v1.ManagementServer.LabelsEntryB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12J\n\x04type\x18\x0e \x01(\x0e27.google.cloud.backupdr.v1.ManagementServer.InstanceTypeB\x03\xe0A\x01\x12D\n\x0emanagement_uri\x18\x0b \x01(\x0b2\'.google.cloud.backupdr.v1.ManagementURIB\x03\xe0A\x03\x12s\n\'workforce_identity_based_management_uri\x18\x10 \x01(\x0b2=.google.cloud.backupdr.v1.WorkforceIdentityBasedManagementURIB\x03\xe0A\x03\x12L\n\x05state\x18\x07 \x01(\x0e28.google.cloud.backupdr.v1.ManagementServer.InstanceStateB\x03\xe0A\x03\x12>\n\x08networks\x18\x08 \x03(\x0b2\'.google.cloud.backupdr.v1.NetworkConfigB\x03\xe0A\x01\x12\x11\n\x04etag\x18\r \x01(\tB\x03\xe0A\x01\x12\x1d\n\x10oauth2_client_id\x18\x0f \x01(\tB\x03\xe0A\x03\x12v\n)workforce_identity_based_oauth2_client_id\x18\x11 \x01(\x0b2>.google.cloud.backupdr.v1.WorkforceIdentityBasedOAuth2ClientIDB\x03\xe0A\x03\x12\x19\n\x0cba_proxy_uri\x18\x12 \x03(\tB\x03\xe0A\x03\x126\n\rsatisfies_pzs\x18\x13 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x14 \x01(\x08B\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"A\n\x0cInstanceType\x12\x1d\n\x19INSTANCE_TYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0eBACKUP_RESTORE\x10\x01"\x8f\x01\n\rInstanceState\x12\x1e\n\x1aINSTANCE_STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\t\n\x05READY\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08DELETING\x10\x04\x12\r\n\tREPAIRING\x10\x05\x12\x0f\n\x0bMAINTENANCE\x10\x06\x12\t\n\x05ERROR\x10\x07:\xa1\x01\xeaA\x9d\x01\n(backupdr.googleapis.com/ManagementServer\x12Lprojects/{project}/locations/{location}/managementServers/{managementserver}*\x11managementServers2\x10managementServer"\xdf\x01\n\x1cListManagementServersRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(backupdr.googleapis.com/ManagementServer\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x18\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01H\x00\x88\x01\x01\x12\x1a\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01H\x01\x88\x01\x01B\t\n\x07_filterB\x0b\n\t_order_by"\x95\x01\n\x1dListManagementServersResponse\x12F\n\x12management_servers\x18\x01 \x03(\x0b2*.google.cloud.backupdr.v1.ManagementServer\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\\\n\x1aGetManagementServerRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(backupdr.googleapis.com/ManagementServer"\xe9\x01\n\x1dCreateManagementServerRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(backupdr.googleapis.com/ManagementServer\x12!\n\x14management_server_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12J\n\x11management_server\x18\x03 \x01(\x0b2*.google.cloud.backupdr.v1.ManagementServerB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"x\n\x1dDeleteManagementServerRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(backupdr.googleapis.com/ManagementServer\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\xfc\x01\n\x18InitializeServiceRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rresource_type\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x03 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12w\n(cloud_sql_instance_initialization_config\x18\x04 \x01(\x0b2>.google.cloud.backupdr.v1.CloudSqlInstanceInitializationConfigB\x03\xe0A\x01H\x00B\x17\n\x15initialization_config"P\n\x19InitializeServiceResponse\x12\x19\n\x11backup_vault_name\x18\x01 \x01(\t\x12\x18\n\x10backup_plan_name\x18\x02 \x01(\t"\x96\x03\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x03\x12]\n\x0fadditional_info\x18\x08 \x03(\x0b2?.google.cloud.backupdr.v1.OperationMetadata.AdditionalInfoEntryB\x03\xe0A\x03\x1a5\n\x13AdditionalInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x012\xda?\n\x08BackupDR\x12\xd0\x01\n\x15ListManagementServers\x126.google.cloud.backupdr.v1.ListManagementServersRequest\x1a7.google.cloud.backupdr.v1.ListManagementServersResponse"F\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v1/{parent=projects/*/locations/*}/managementServers\x12\xbd\x01\n\x13GetManagementServer\x124.google.cloud.backupdr.v1.GetManagementServerRequest\x1a*.google.cloud.backupdr.v1.ManagementServer"D\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v1/{name=projects/*/locations/*/managementServers/*}\x12\x9b\x02\n\x16CreateManagementServer\x127.google.cloud.backupdr.v1.CreateManagementServerRequest\x1a\x1d.google.longrunning.Operation"\xa8\x01\xcaA%\n\x10ManagementServer\x12\x11OperationMetadata\xdaA-parent,management_server,management_server_id\x82\xd3\xe4\x93\x02J"5/v1/{parent=projects/*/locations/*}/managementServers:\x11management_server\x12\xe3\x01\n\x16DeleteManagementServer\x127.google.cloud.backupdr.v1.DeleteManagementServerRequest\x1a\x1d.google.longrunning.Operation"q\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v1/{name=projects/*/locations/*/managementServers/*}\x12\xf8\x01\n\x11CreateBackupVault\x122.google.cloud.backupdr.v1.CreateBackupVaultRequest\x1a\x1d.google.longrunning.Operation"\x8f\x01\xcaA \n\x0bBackupVault\x12\x11OperationMetadata\xdaA#parent,backup_vault,backup_vault_id\x82\xd3\xe4\x93\x02@"0/v1/{parent=projects/*/locations/*}/backupVaults:\x0cbackup_vault\x12\xbc\x01\n\x10ListBackupVaults\x121.google.cloud.backupdr.v1.ListBackupVaultsRequest\x1a2.google.cloud.backupdr.v1.ListBackupVaultsResponse"A\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v1/{parent=projects/*/locations/*}/backupVaults\x12\xdd\x01\n\x17FetchUsableBackupVaults\x128.google.cloud.backupdr.v1.FetchUsableBackupVaultsRequest\x1a9.google.cloud.backupdr.v1.FetchUsableBackupVaultsResponse"M\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1/{parent=projects/*/locations/*}/backupVaults:fetchUsable\x12\xa9\x01\n\x0eGetBackupVault\x12/.google.cloud.backupdr.v1.GetBackupVaultRequest\x1a%.google.cloud.backupdr.v1.BackupVault"?\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v1/{name=projects/*/locations/*/backupVaults/*}\x12\xfa\x01\n\x11UpdateBackupVault\x122.google.cloud.backupdr.v1.UpdateBackupVaultRequest\x1a\x1d.google.longrunning.Operation"\x91\x01\xcaA \n\x0bBackupVault\x12\x11OperationMetadata\xdaA\x18backup_vault,update_mask\x82\xd3\xe4\x93\x02M2=/v1/{backup_vault.name=projects/*/locations/*/backupVaults/*}:\x0cbackup_vault\x12\xd4\x01\n\x11DeleteBackupVault\x122.google.cloud.backupdr.v1.DeleteBackupVaultRequest\x1a\x1d.google.longrunning.Operation"l\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x022*0/v1/{name=projects/*/locations/*/backupVaults/*}\x12\xc7\x01\n\x0fListDataSources\x120.google.cloud.backupdr.v1.ListDataSourcesRequest\x1a1.google.cloud.backupdr.v1.ListDataSourcesResponse"O\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v1/{parent=projects/*/locations/*/backupVaults/*}/dataSources\x12\xb4\x01\n\rGetDataSource\x12..google.cloud.backupdr.v1.GetDataSourceRequest\x1a$.google.cloud.backupdr.v1.DataSource"M\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1/{name=projects/*/locations/*/backupVaults/*/dataSources/*}\x12\x82\x02\n\x10UpdateDataSource\x121.google.cloud.backupdr.v1.UpdateDataSourceRequest\x1a\x1d.google.longrunning.Operation"\x9b\x01\xcaA\x1f\n\nDataSource\x12\x11OperationMetadata\xdaA\x17data_source,update_mask\x82\xd3\xe4\x93\x02Y2J/v1/{data_source.name=projects/*/locations/*/backupVaults/*/dataSources/*}:\x0bdata_source\x12\xc5\x01\n\x0bListBackups\x12,.google.cloud.backupdr.v1.ListBackupsRequest\x1a-.google.cloud.backupdr.v1.ListBackupsResponse"Y\xdaA\x06parent\x82\xd3\xe4\x93\x02J\x12H/v1/{parent=projects/*/locations/*/backupVaults/*/dataSources/*}/backups\x12\xb2\x01\n\tGetBackup\x12*.google.cloud.backupdr.v1.GetBackupRequest\x1a .google.cloud.backupdr.v1.Backup"W\xdaA\x04name\x82\xd3\xe4\x93\x02J\x12H/v1/{name=projects/*/locations/*/backupVaults/*/dataSources/*/backups/*}\x12\xf1\x01\n\x0cUpdateBackup\x12-.google.cloud.backupdr.v1.UpdateBackupRequest\x1a\x1d.google.longrunning.Operation"\x92\x01\xcaA\x1b\n\x06Backup\x12\x11OperationMetadata\xdaA\x12backup,update_mask\x82\xd3\xe4\x93\x02Y2O/v1/{backup.name=projects/*/locations/*/backupVaults/*/dataSources/*/backups/*}:\x06backup\x12\xd3\x01\n\x0cDeleteBackup\x12-.google.cloud.backupdr.v1.DeleteBackupRequest\x1a\x1d.google.longrunning.Operation"u\xcaA\x1b\n\x06Backup\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02J*H/v1/{name=projects/*/locations/*/backupVaults/*/dataSources/*/backups/*}\x12\xf0\x01\n\rRestoreBackup\x12..google.cloud.backupdr.v1.RestoreBackupRequest\x1a\x1d.google.longrunning.Operation"\x8f\x01\xcaA*\n\x15RestoreBackupResponse\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02U"P/v1/{name=projects/*/locations/*/backupVaults/*/dataSources/*/backups/*}:restore:\x01*\x12\xf1\x01\n\x10CreateBackupPlan\x121.google.cloud.backupdr.v1.CreateBackupPlanRequest\x1a\x1d.google.longrunning.Operation"\x8a\x01\xcaA\x1f\n\nBackupPlan\x12\x11OperationMetadata\xdaA!parent,backup_plan,backup_plan_id\x82\xd3\xe4\x93\x02>"//v1/{parent=projects/*/locations/*}/backupPlans:\x0bbackup_plan\x12\xf3\x01\n\x10UpdateBackupPlan\x121.google.cloud.backupdr.v1.UpdateBackupPlanRequest\x1a\x1d.google.longrunning.Operation"\x8c\x01\xcaA\x1f\n\nBackupPlan\x12\x11OperationMetadata\xdaA\x17backup_plan,update_mask\x82\xd3\xe4\x93\x02J2;/v1/{backup_plan.name=projects/*/locations/*/backupPlans/*}:\x0bbackup_plan\x12\xa5\x01\n\rGetBackupPlan\x12..google.cloud.backupdr.v1.GetBackupPlanRequest\x1a$.google.cloud.backupdr.v1.BackupPlan">\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1/{name=projects/*/locations/*/backupPlans/*}\x12\xb8\x01\n\x0fListBackupPlans\x120.google.cloud.backupdr.v1.ListBackupPlansRequest\x1a1.google.cloud.backupdr.v1.ListBackupPlansResponse"@\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=projects/*/locations/*}/backupPlans\x12\xd1\x01\n\x10DeleteBackupPlan\x121.google.cloud.backupdr.v1.DeleteBackupPlanRequest\x1a\x1d.google.longrunning.Operation"k\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1/{name=projects/*/locations/*/backupPlans/*}\x12\xc9\x01\n\x15GetBackupPlanRevision\x126.google.cloud.backupdr.v1.GetBackupPlanRevisionRequest\x1a,.google.cloud.backupdr.v1.BackupPlanRevision"J\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v1/{name=projects/*/locations/*/backupPlans/*/revisions/*}\x12\xdc\x01\n\x17ListBackupPlanRevisions\x128.google.cloud.backupdr.v1.ListBackupPlanRevisionsRequest\x1a9.google.cloud.backupdr.v1.ListBackupPlanRevisionsResponse"L\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v1/{parent=projects/*/locations/*/backupPlans/*}/revisions\x12\xc1\x02\n\x1bCreateBackupPlanAssociation\x12<.google.cloud.backupdr.v1.CreateBackupPlanAssociationRequest\x1a\x1d.google.longrunning.Operation"\xc4\x01\xcaA*\n\x15BackupPlanAssociation\x12\x11OperationMetadata\xdaA9parent,backup_plan_association,backup_plan_association_id\x82\xd3\xe4\x93\x02U":/v1/{parent=projects/*/locations/*}/backupPlanAssociations:\x17backup_plan_association\x12\xc3\x02\n\x1bUpdateBackupPlanAssociation\x12<.google.cloud.backupdr.v1.UpdateBackupPlanAssociationRequest\x1a\x1d.google.longrunning.Operation"\xc6\x01\xcaA*\n\x15BackupPlanAssociation\x12\x11OperationMetadata\xdaA#backup_plan_association,update_mask\x82\xd3\xe4\x93\x02m2R/v1/{backup_plan_association.name=projects/*/locations/*/backupPlanAssociations/*}:\x17backup_plan_association\x12\xd1\x01\n\x18GetBackupPlanAssociation\x129.google.cloud.backupdr.v1.GetBackupPlanAssociationRequest\x1a/.google.cloud.backupdr.v1.BackupPlanAssociation"I\xdaA\x04name\x82\xd3\xe4\x93\x02<\x12:/v1/{name=projects/*/locations/*/backupPlanAssociations/*}\x12\xe4\x01\n\x1aListBackupPlanAssociations\x12;.google.cloud.backupdr.v1.ListBackupPlanAssociationsRequest\x1a<.google.cloud.backupdr.v1.ListBackupPlanAssociationsResponse"K\xdaA\x06parent\x82\xd3\xe4\x93\x02<\x12:/v1/{parent=projects/*/locations/*}/backupPlanAssociations\x12\xb7\x02\n*FetchBackupPlanAssociationsForResourceType\x12K.google.cloud.backupdr.v1.FetchBackupPlanAssociationsForResourceTypeRequest\x1aL.google.cloud.backupdr.v1.FetchBackupPlanAssociationsForResourceTypeResponse"n\xdaA\x14parent,resource_type\x82\xd3\xe4\x93\x02Q\x12O/v1/{parent=projects/*/locations/*}/backupPlanAssociations:fetchForResourceType\x12\xf2\x01\n\x1bDeleteBackupPlanAssociation\x12<.google.cloud.backupdr.v1.DeleteBackupPlanAssociationRequest\x1a\x1d.google.longrunning.Operation"v\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02<*:/v1/{name=projects/*/locations/*/backupPlanAssociations/*}\x12\xf0\x01\n\rTriggerBackup\x12..google.cloud.backupdr.v1.TriggerBackupRequest\x1a\x1d.google.longrunning.Operation"\x8f\x01\xcaA*\n\x15BackupPlanAssociation\x12\x11OperationMetadata\xdaA\x0cname,rule_id\x82\xd3\xe4\x93\x02M"H/v1/{name=projects/*/locations/*/backupPlanAssociations/*}:triggerBackup:\x01*\x12\xc9\x01\n\x16GetDataSourceReference\x127.google.cloud.backupdr.v1.GetDataSourceReferenceRequest\x1a-.google.cloud.backupdr.v1.DataSourceReference"G\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/v1/{name=projects/*/locations/*/dataSourceReferences/*}\x12\xaf\x02\n(FetchDataSourceReferencesForResourceType\x12I.google.cloud.backupdr.v1.FetchDataSourceReferencesForResourceTypeRequest\x1aJ.google.cloud.backupdr.v1.FetchDataSourceReferencesForResourceTypeResponse"l\xdaA\x14parent,resource_type\x82\xd3\xe4\x93\x02O\x12M/v1/{parent=projects/*/locations/*}/dataSourceReferences:fetchForResourceType\x12\xde\x01\n\x11InitializeService\x122.google.cloud.backupdr.v1.InitializeServiceRequest\x1a\x1d.google.longrunning.Operation"v\xcaA.\n\x19InitializeServiceResponse\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02?":/v1/{name=projects/*/locations/*/serviceConfig}:initialize:\x01*\x1aK\xcaA\x17backupdr.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xbd\x01\n\x1ccom.google.cloud.backupdr.v1B\rBackupDRProtoP\x01Z8cloud.google.com/go/backupdr/apiv1/backupdrpb;backupdrpb\xaa\x02\x18Google.Cloud.BackupDR.V1\xca\x02\x18Google\\Cloud\\BackupDR\\V1\xea\x02\x1bGoogle::Cloud::BackupDR::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.backupdr.v1.backupdr_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.backupdr.v1B\rBackupDRProtoP\x01Z8cloud.google.com/go/backupdr/apiv1/backupdrpb;backupdrpb\xaa\x02\x18Google.Cloud.BackupDR.V1\xca\x02\x18Google\\Cloud\\BackupDR\\V1\xea\x02\x1bGoogle::Cloud::BackupDR::V1'
    _globals['_NETWORKCONFIG'].fields_by_name['network']._loaded_options = None
    _globals['_NETWORKCONFIG'].fields_by_name['network']._serialized_options = b'\xe0A\x01'
    _globals['_NETWORKCONFIG'].fields_by_name['peering_mode']._loaded_options = None
    _globals['_NETWORKCONFIG'].fields_by_name['peering_mode']._serialized_options = b'\xe0A\x01'
    _globals['_MANAGEMENTURI'].fields_by_name['web_ui']._loaded_options = None
    _globals['_MANAGEMENTURI'].fields_by_name['web_ui']._serialized_options = b'\xe0A\x03'
    _globals['_MANAGEMENTURI'].fields_by_name['api']._loaded_options = None
    _globals['_MANAGEMENTURI'].fields_by_name['api']._serialized_options = b'\xe0A\x03'
    _globals['_WORKFORCEIDENTITYBASEDMANAGEMENTURI'].fields_by_name['first_party_management_uri']._loaded_options = None
    _globals['_WORKFORCEIDENTITYBASEDMANAGEMENTURI'].fields_by_name['first_party_management_uri']._serialized_options = b'\xe0A\x03'
    _globals['_WORKFORCEIDENTITYBASEDMANAGEMENTURI'].fields_by_name['third_party_management_uri']._loaded_options = None
    _globals['_WORKFORCEIDENTITYBASEDMANAGEMENTURI'].fields_by_name['third_party_management_uri']._serialized_options = b'\xe0A\x03'
    _globals['_WORKFORCEIDENTITYBASEDOAUTH2CLIENTID'].fields_by_name['first_party_oauth2_client_id']._loaded_options = None
    _globals['_WORKFORCEIDENTITYBASEDOAUTH2CLIENTID'].fields_by_name['first_party_oauth2_client_id']._serialized_options = b'\xe0A\x03'
    _globals['_WORKFORCEIDENTITYBASEDOAUTH2CLIENTID'].fields_by_name['third_party_oauth2_client_id']._loaded_options = None
    _globals['_WORKFORCEIDENTITYBASEDOAUTH2CLIENTID'].fields_by_name['third_party_oauth2_client_id']._serialized_options = b'\xe0A\x03'
    _globals['_MANAGEMENTSERVER_LABELSENTRY']._loaded_options = None
    _globals['_MANAGEMENTSERVER_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_MANAGEMENTSERVER'].fields_by_name['name']._loaded_options = None
    _globals['_MANAGEMENTSERVER'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x08'
    _globals['_MANAGEMENTSERVER'].fields_by_name['description']._loaded_options = None
    _globals['_MANAGEMENTSERVER'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_MANAGEMENTSERVER'].fields_by_name['labels']._loaded_options = None
    _globals['_MANAGEMENTSERVER'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_MANAGEMENTSERVER'].fields_by_name['create_time']._loaded_options = None
    _globals['_MANAGEMENTSERVER'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MANAGEMENTSERVER'].fields_by_name['update_time']._loaded_options = None
    _globals['_MANAGEMENTSERVER'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_MANAGEMENTSERVER'].fields_by_name['type']._loaded_options = None
    _globals['_MANAGEMENTSERVER'].fields_by_name['type']._serialized_options = b'\xe0A\x01'
    _globals['_MANAGEMENTSERVER'].fields_by_name['management_uri']._loaded_options = None
    _globals['_MANAGEMENTSERVER'].fields_by_name['management_uri']._serialized_options = b'\xe0A\x03'
    _globals['_MANAGEMENTSERVER'].fields_by_name['workforce_identity_based_management_uri']._loaded_options = None
    _globals['_MANAGEMENTSERVER'].fields_by_name['workforce_identity_based_management_uri']._serialized_options = b'\xe0A\x03'
    _globals['_MANAGEMENTSERVER'].fields_by_name['state']._loaded_options = None
    _globals['_MANAGEMENTSERVER'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_MANAGEMENTSERVER'].fields_by_name['networks']._loaded_options = None
    _globals['_MANAGEMENTSERVER'].fields_by_name['networks']._serialized_options = b'\xe0A\x01'
    _globals['_MANAGEMENTSERVER'].fields_by_name['etag']._loaded_options = None
    _globals['_MANAGEMENTSERVER'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_MANAGEMENTSERVER'].fields_by_name['oauth2_client_id']._loaded_options = None
    _globals['_MANAGEMENTSERVER'].fields_by_name['oauth2_client_id']._serialized_options = b'\xe0A\x03'
    _globals['_MANAGEMENTSERVER'].fields_by_name['workforce_identity_based_oauth2_client_id']._loaded_options = None
    _globals['_MANAGEMENTSERVER'].fields_by_name['workforce_identity_based_oauth2_client_id']._serialized_options = b'\xe0A\x03'
    _globals['_MANAGEMENTSERVER'].fields_by_name['ba_proxy_uri']._loaded_options = None
    _globals['_MANAGEMENTSERVER'].fields_by_name['ba_proxy_uri']._serialized_options = b'\xe0A\x03'
    _globals['_MANAGEMENTSERVER'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_MANAGEMENTSERVER'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_MANAGEMENTSERVER'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_MANAGEMENTSERVER'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_MANAGEMENTSERVER']._loaded_options = None
    _globals['_MANAGEMENTSERVER']._serialized_options = b'\xeaA\x9d\x01\n(backupdr.googleapis.com/ManagementServer\x12Lprojects/{project}/locations/{location}/managementServers/{managementserver}*\x11managementServers2\x10managementServer'
    _globals['_LISTMANAGEMENTSERVERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMANAGEMENTSERVERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(backupdr.googleapis.com/ManagementServer'
    _globals['_LISTMANAGEMENTSERVERSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTMANAGEMENTSERVERSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMANAGEMENTSERVERSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTMANAGEMENTSERVERSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMANAGEMENTSERVERSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTMANAGEMENTSERVERSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMANAGEMENTSERVERSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTMANAGEMENTSERVERSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETMANAGEMENTSERVERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMANAGEMENTSERVERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(backupdr.googleapis.com/ManagementServer'
    _globals['_CREATEMANAGEMENTSERVERREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEMANAGEMENTSERVERREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(backupdr.googleapis.com/ManagementServer'
    _globals['_CREATEMANAGEMENTSERVERREQUEST'].fields_by_name['management_server_id']._loaded_options = None
    _globals['_CREATEMANAGEMENTSERVERREQUEST'].fields_by_name['management_server_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEMANAGEMENTSERVERREQUEST'].fields_by_name['management_server']._loaded_options = None
    _globals['_CREATEMANAGEMENTSERVERREQUEST'].fields_by_name['management_server']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEMANAGEMENTSERVERREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEMANAGEMENTSERVERREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEMANAGEMENTSERVERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEMANAGEMENTSERVERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(backupdr.googleapis.com/ManagementServer'
    _globals['_DELETEMANAGEMENTSERVERREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEMANAGEMENTSERVERREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_INITIALIZESERVICEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_INITIALIZESERVICEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_INITIALIZESERVICEREQUEST'].fields_by_name['resource_type']._loaded_options = None
    _globals['_INITIALIZESERVICEREQUEST'].fields_by_name['resource_type']._serialized_options = b'\xe0A\x02'
    _globals['_INITIALIZESERVICEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_INITIALIZESERVICEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_INITIALIZESERVICEREQUEST'].fields_by_name['cloud_sql_instance_initialization_config']._loaded_options = None
    _globals['_INITIALIZESERVICEREQUEST'].fields_by_name['cloud_sql_instance_initialization_config']._serialized_options = b'\xe0A\x01'
    _globals['_OPERATIONMETADATA_ADDITIONALINFOENTRY']._loaded_options = None
    _globals['_OPERATIONMETADATA_ADDITIONALINFOENTRY']._serialized_options = b'8\x01'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['additional_info']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['additional_info']._serialized_options = b'\xe0A\x03'
    _globals['_BACKUPDR']._loaded_options = None
    _globals['_BACKUPDR']._serialized_options = b'\xcaA\x17backupdr.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_BACKUPDR'].methods_by_name['ListManagementServers']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['ListManagementServers']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v1/{parent=projects/*/locations/*}/managementServers'
    _globals['_BACKUPDR'].methods_by_name['GetManagementServer']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['GetManagementServer']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v1/{name=projects/*/locations/*/managementServers/*}'
    _globals['_BACKUPDR'].methods_by_name['CreateManagementServer']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['CreateManagementServer']._serialized_options = b'\xcaA%\n\x10ManagementServer\x12\x11OperationMetadata\xdaA-parent,management_server,management_server_id\x82\xd3\xe4\x93\x02J"5/v1/{parent=projects/*/locations/*}/managementServers:\x11management_server'
    _globals['_BACKUPDR'].methods_by_name['DeleteManagementServer']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['DeleteManagementServer']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v1/{name=projects/*/locations/*/managementServers/*}'
    _globals['_BACKUPDR'].methods_by_name['CreateBackupVault']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['CreateBackupVault']._serialized_options = b'\xcaA \n\x0bBackupVault\x12\x11OperationMetadata\xdaA#parent,backup_vault,backup_vault_id\x82\xd3\xe4\x93\x02@"0/v1/{parent=projects/*/locations/*}/backupVaults:\x0cbackup_vault'
    _globals['_BACKUPDR'].methods_by_name['ListBackupVaults']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['ListBackupVaults']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v1/{parent=projects/*/locations/*}/backupVaults'
    _globals['_BACKUPDR'].methods_by_name['FetchUsableBackupVaults']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['FetchUsableBackupVaults']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1/{parent=projects/*/locations/*}/backupVaults:fetchUsable'
    _globals['_BACKUPDR'].methods_by_name['GetBackupVault']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['GetBackupVault']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v1/{name=projects/*/locations/*/backupVaults/*}'
    _globals['_BACKUPDR'].methods_by_name['UpdateBackupVault']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['UpdateBackupVault']._serialized_options = b'\xcaA \n\x0bBackupVault\x12\x11OperationMetadata\xdaA\x18backup_vault,update_mask\x82\xd3\xe4\x93\x02M2=/v1/{backup_vault.name=projects/*/locations/*/backupVaults/*}:\x0cbackup_vault'
    _globals['_BACKUPDR'].methods_by_name['DeleteBackupVault']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['DeleteBackupVault']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x022*0/v1/{name=projects/*/locations/*/backupVaults/*}'
    _globals['_BACKUPDR'].methods_by_name['ListDataSources']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['ListDataSources']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v1/{parent=projects/*/locations/*/backupVaults/*}/dataSources'
    _globals['_BACKUPDR'].methods_by_name['GetDataSource']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['GetDataSource']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1/{name=projects/*/locations/*/backupVaults/*/dataSources/*}'
    _globals['_BACKUPDR'].methods_by_name['UpdateDataSource']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['UpdateDataSource']._serialized_options = b'\xcaA\x1f\n\nDataSource\x12\x11OperationMetadata\xdaA\x17data_source,update_mask\x82\xd3\xe4\x93\x02Y2J/v1/{data_source.name=projects/*/locations/*/backupVaults/*/dataSources/*}:\x0bdata_source'
    _globals['_BACKUPDR'].methods_by_name['ListBackups']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['ListBackups']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02J\x12H/v1/{parent=projects/*/locations/*/backupVaults/*/dataSources/*}/backups'
    _globals['_BACKUPDR'].methods_by_name['GetBackup']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['GetBackup']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02J\x12H/v1/{name=projects/*/locations/*/backupVaults/*/dataSources/*/backups/*}'
    _globals['_BACKUPDR'].methods_by_name['UpdateBackup']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['UpdateBackup']._serialized_options = b'\xcaA\x1b\n\x06Backup\x12\x11OperationMetadata\xdaA\x12backup,update_mask\x82\xd3\xe4\x93\x02Y2O/v1/{backup.name=projects/*/locations/*/backupVaults/*/dataSources/*/backups/*}:\x06backup'
    _globals['_BACKUPDR'].methods_by_name['DeleteBackup']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['DeleteBackup']._serialized_options = b'\xcaA\x1b\n\x06Backup\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02J*H/v1/{name=projects/*/locations/*/backupVaults/*/dataSources/*/backups/*}'
    _globals['_BACKUPDR'].methods_by_name['RestoreBackup']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['RestoreBackup']._serialized_options = b'\xcaA*\n\x15RestoreBackupResponse\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02U"P/v1/{name=projects/*/locations/*/backupVaults/*/dataSources/*/backups/*}:restore:\x01*'
    _globals['_BACKUPDR'].methods_by_name['CreateBackupPlan']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['CreateBackupPlan']._serialized_options = b'\xcaA\x1f\n\nBackupPlan\x12\x11OperationMetadata\xdaA!parent,backup_plan,backup_plan_id\x82\xd3\xe4\x93\x02>"//v1/{parent=projects/*/locations/*}/backupPlans:\x0bbackup_plan'
    _globals['_BACKUPDR'].methods_by_name['UpdateBackupPlan']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['UpdateBackupPlan']._serialized_options = b'\xcaA\x1f\n\nBackupPlan\x12\x11OperationMetadata\xdaA\x17backup_plan,update_mask\x82\xd3\xe4\x93\x02J2;/v1/{backup_plan.name=projects/*/locations/*/backupPlans/*}:\x0bbackup_plan'
    _globals['_BACKUPDR'].methods_by_name['GetBackupPlan']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['GetBackupPlan']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1/{name=projects/*/locations/*/backupPlans/*}'
    _globals['_BACKUPDR'].methods_by_name['ListBackupPlans']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['ListBackupPlans']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=projects/*/locations/*}/backupPlans'
    _globals['_BACKUPDR'].methods_by_name['DeleteBackupPlan']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['DeleteBackupPlan']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1/{name=projects/*/locations/*/backupPlans/*}'
    _globals['_BACKUPDR'].methods_by_name['GetBackupPlanRevision']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['GetBackupPlanRevision']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v1/{name=projects/*/locations/*/backupPlans/*/revisions/*}'
    _globals['_BACKUPDR'].methods_by_name['ListBackupPlanRevisions']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['ListBackupPlanRevisions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v1/{parent=projects/*/locations/*/backupPlans/*}/revisions'
    _globals['_BACKUPDR'].methods_by_name['CreateBackupPlanAssociation']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['CreateBackupPlanAssociation']._serialized_options = b'\xcaA*\n\x15BackupPlanAssociation\x12\x11OperationMetadata\xdaA9parent,backup_plan_association,backup_plan_association_id\x82\xd3\xe4\x93\x02U":/v1/{parent=projects/*/locations/*}/backupPlanAssociations:\x17backup_plan_association'
    _globals['_BACKUPDR'].methods_by_name['UpdateBackupPlanAssociation']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['UpdateBackupPlanAssociation']._serialized_options = b'\xcaA*\n\x15BackupPlanAssociation\x12\x11OperationMetadata\xdaA#backup_plan_association,update_mask\x82\xd3\xe4\x93\x02m2R/v1/{backup_plan_association.name=projects/*/locations/*/backupPlanAssociations/*}:\x17backup_plan_association'
    _globals['_BACKUPDR'].methods_by_name['GetBackupPlanAssociation']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['GetBackupPlanAssociation']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02<\x12:/v1/{name=projects/*/locations/*/backupPlanAssociations/*}'
    _globals['_BACKUPDR'].methods_by_name['ListBackupPlanAssociations']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['ListBackupPlanAssociations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02<\x12:/v1/{parent=projects/*/locations/*}/backupPlanAssociations'
    _globals['_BACKUPDR'].methods_by_name['FetchBackupPlanAssociationsForResourceType']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['FetchBackupPlanAssociationsForResourceType']._serialized_options = b'\xdaA\x14parent,resource_type\x82\xd3\xe4\x93\x02Q\x12O/v1/{parent=projects/*/locations/*}/backupPlanAssociations:fetchForResourceType'
    _globals['_BACKUPDR'].methods_by_name['DeleteBackupPlanAssociation']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['DeleteBackupPlanAssociation']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02<*:/v1/{name=projects/*/locations/*/backupPlanAssociations/*}'
    _globals['_BACKUPDR'].methods_by_name['TriggerBackup']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['TriggerBackup']._serialized_options = b'\xcaA*\n\x15BackupPlanAssociation\x12\x11OperationMetadata\xdaA\x0cname,rule_id\x82\xd3\xe4\x93\x02M"H/v1/{name=projects/*/locations/*/backupPlanAssociations/*}:triggerBackup:\x01*'
    _globals['_BACKUPDR'].methods_by_name['GetDataSourceReference']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['GetDataSourceReference']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:\x128/v1/{name=projects/*/locations/*/dataSourceReferences/*}'
    _globals['_BACKUPDR'].methods_by_name['FetchDataSourceReferencesForResourceType']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['FetchDataSourceReferencesForResourceType']._serialized_options = b'\xdaA\x14parent,resource_type\x82\xd3\xe4\x93\x02O\x12M/v1/{parent=projects/*/locations/*}/dataSourceReferences:fetchForResourceType'
    _globals['_BACKUPDR'].methods_by_name['InitializeService']._loaded_options = None
    _globals['_BACKUPDR'].methods_by_name['InitializeService']._serialized_options = b'\xcaA.\n\x19InitializeServiceResponse\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02?":/v1/{name=projects/*/locations/*/serviceConfig}:initialize:\x01*'
    _globals['_NETWORKCONFIG']._serialized_start = 591
    _globals['_NETWORKCONFIG']._serialized_end = 781
    _globals['_NETWORKCONFIG_PEERINGMODE']._serialized_start = 710
    _globals['_NETWORKCONFIG_PEERINGMODE']._serialized_end = 781
    _globals['_MANAGEMENTURI']._serialized_start = 783
    _globals['_MANAGEMENTURI']._serialized_end = 837
    _globals['_WORKFORCEIDENTITYBASEDMANAGEMENTURI']._serialized_start = 839
    _globals['_WORKFORCEIDENTITYBASEDMANAGEMENTURI']._serialized_end = 958
    _globals['_WORKFORCEIDENTITYBASEDOAUTH2CLIENTID']._serialized_start = 960
    _globals['_WORKFORCEIDENTITYBASEDOAUTH2CLIENTID']._serialized_end = 1084
    _globals['_MANAGEMENTSERVER']._serialized_start = 1087
    _globals['_MANAGEMENTSERVER']._serialized_end = 2448
    _globals['_MANAGEMENTSERVER_LABELSENTRY']._serialized_start = 2026
    _globals['_MANAGEMENTSERVER_LABELSENTRY']._serialized_end = 2071
    _globals['_MANAGEMENTSERVER_INSTANCETYPE']._serialized_start = 2073
    _globals['_MANAGEMENTSERVER_INSTANCETYPE']._serialized_end = 2138
    _globals['_MANAGEMENTSERVER_INSTANCESTATE']._serialized_start = 2141
    _globals['_MANAGEMENTSERVER_INSTANCESTATE']._serialized_end = 2284
    _globals['_LISTMANAGEMENTSERVERSREQUEST']._serialized_start = 2451
    _globals['_LISTMANAGEMENTSERVERSREQUEST']._serialized_end = 2674
    _globals['_LISTMANAGEMENTSERVERSRESPONSE']._serialized_start = 2677
    _globals['_LISTMANAGEMENTSERVERSRESPONSE']._serialized_end = 2826
    _globals['_GETMANAGEMENTSERVERREQUEST']._serialized_start = 2828
    _globals['_GETMANAGEMENTSERVERREQUEST']._serialized_end = 2920
    _globals['_CREATEMANAGEMENTSERVERREQUEST']._serialized_start = 2923
    _globals['_CREATEMANAGEMENTSERVERREQUEST']._serialized_end = 3156
    _globals['_DELETEMANAGEMENTSERVERREQUEST']._serialized_start = 3158
    _globals['_DELETEMANAGEMENTSERVERREQUEST']._serialized_end = 3278
    _globals['_INITIALIZESERVICEREQUEST']._serialized_start = 3281
    _globals['_INITIALIZESERVICEREQUEST']._serialized_end = 3533
    _globals['_INITIALIZESERVICERESPONSE']._serialized_start = 3535
    _globals['_INITIALIZESERVICERESPONSE']._serialized_end = 3615
    _globals['_OPERATIONMETADATA']._serialized_start = 3618
    _globals['_OPERATIONMETADATA']._serialized_end = 4024
    _globals['_OPERATIONMETADATA_ADDITIONALINFOENTRY']._serialized_start = 3971
    _globals['_OPERATIONMETADATA_ADDITIONALINFOENTRY']._serialized_end = 4024
    _globals['_BACKUPDR']._serialized_start = 4027
    _globals['_BACKUPDR']._serialized_end = 12181