"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/gkehub/v1/configmanagement/configmanagement.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/gkehub/v1/configmanagement/configmanagement.proto\x12\'google.cloud.gkehub.configmanagement.v1\x1a\x1fgoogle/protobuf/timestamp.proto"\xe6\x03\n\x0fMembershipState\x12\x14\n\x0ccluster_name\x18\x01 \x01(\t\x12P\n\x0fmembership_spec\x18\x02 \x01(\x0b27.google.cloud.gkehub.configmanagement.v1.MembershipSpec\x12N\n\x0eoperator_state\x18\x03 \x01(\x0b26.google.cloud.gkehub.configmanagement.v1.OperatorState\x12S\n\x11config_sync_state\x18\x04 \x01(\x0b28.google.cloud.gkehub.configmanagement.v1.ConfigSyncState\x12_\n\x17policy_controller_state\x18\x05 \x01(\x0b2>.google.cloud.gkehub.configmanagement.v1.PolicyControllerState\x12e\n\x1ahierarchy_controller_state\x18\x07 \x01(\x0b2A.google.cloud.gkehub.configmanagement.v1.HierarchyControllerState"\xe7\x03\n\x0eMembershipSpec\x12H\n\x0bconfig_sync\x18\x01 \x01(\x0b23.google.cloud.gkehub.configmanagement.v1.ConfigSync\x12T\n\x11policy_controller\x18\x02 \x01(\x0b29.google.cloud.gkehub.configmanagement.v1.PolicyController\x12`\n\x14hierarchy_controller\x18\x04 \x01(\x0b2B.google.cloud.gkehub.configmanagement.v1.HierarchyControllerConfig\x12\x0f\n\x07version\x18\n \x01(\t\x12\x0f\n\x07cluster\x18\x0b \x01(\t\x12V\n\nmanagement\x18\x0c \x01(\x0e2B.google.cloud.gkehub.configmanagement.v1.MembershipSpec.Management"Y\n\nManagement\x12\x1a\n\x16MANAGEMENT_UNSPECIFIED\x10\x00\x12\x18\n\x14MANAGEMENT_AUTOMATIC\x10\x01\x12\x15\n\x11MANAGEMENT_MANUAL\x10\x02"\x89\x02\n\nConfigSync\x12?\n\x03git\x18\x07 \x01(\x0b22.google.cloud.gkehub.configmanagement.v1.GitConfig\x12\x15\n\rsource_format\x18\x08 \x01(\t\x12\x14\n\x07enabled\x18\n \x01(\x08H\x00\x88\x01\x01\x12\x15\n\rprevent_drift\x18\x0b \x01(\x08\x12?\n\x03oci\x18\x0c \x01(\x0b22.google.cloud.gkehub.configmanagement.v1.OciConfig\x12)\n!metrics_gcp_service_account_email\x18\x0f \x01(\tB\n\n\x08_enabled"\xbe\x01\n\tGitConfig\x12\x11\n\tsync_repo\x18\x01 \x01(\t\x12\x13\n\x0bsync_branch\x18\x02 \x01(\t\x12\x12\n\npolicy_dir\x18\x03 \x01(\t\x12\x16\n\x0esync_wait_secs\x18\x04 \x01(\x03\x12\x10\n\x08sync_rev\x18\x05 \x01(\t\x12\x13\n\x0bsecret_type\x18\x06 \x01(\t\x12\x13\n\x0bhttps_proxy\x18\x07 \x01(\t\x12!\n\x19gcp_service_account_email\x18\x08 \x01(\t"\x82\x01\n\tOciConfig\x12\x11\n\tsync_repo\x18\x01 \x01(\t\x12\x12\n\npolicy_dir\x18\x02 \x01(\t\x12\x16\n\x0esync_wait_secs\x18\x03 \x01(\x03\x12\x13\n\x0bsecret_type\x18\x04 \x01(\t\x12!\n\x19gcp_service_account_email\x18\x05 \x01(\t"\x89\x02\n\x10PolicyController\x12\x0f\n\x07enabled\x18\x01 \x01(\x08\x12\'\n\x1atemplate_library_installed\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12#\n\x16audit_interval_seconds\x18\x03 \x01(\x03H\x01\x88\x01\x01\x12\x1d\n\x15exemptable_namespaces\x18\x04 \x03(\t\x12!\n\x19referential_rules_enabled\x18\x05 \x01(\x08\x12\x1a\n\x12log_denies_enabled\x18\x06 \x01(\x08B\x1d\n\x1b_template_library_installedB\x19\n\x17_audit_interval_seconds"x\n\x19HierarchyControllerConfig\x12\x0f\n\x07enabled\x18\x01 \x01(\x08\x12\x1e\n\x16enable_pod_tree_labels\x18\x02 \x01(\x08\x12*\n"enable_hierarchical_resource_quota\x18\x03 \x01(\x08"\xb8\x01\n"HierarchyControllerDeploymentState\x12E\n\x03hnc\x18\x01 \x01(\x0e28.google.cloud.gkehub.configmanagement.v1.DeploymentState\x12K\n\textension\x18\x02 \x01(\x0e28.google.cloud.gkehub.configmanagement.v1.DeploymentState"<\n\x1aHierarchyControllerVersion\x12\x0b\n\x03hnc\x18\x01 \x01(\t\x12\x11\n\textension\x18\x02 \x01(\t"\xcc\x01\n\x18HierarchyControllerState\x12T\n\x07version\x18\x01 \x01(\x0b2C.google.cloud.gkehub.configmanagement.v1.HierarchyControllerVersion\x12Z\n\x05state\x18\x02 \x01(\x0b2K.google.cloud.gkehub.configmanagement.v1.HierarchyControllerDeploymentState"\xbb\x01\n\rOperatorState\x12\x0f\n\x07version\x18\x01 \x01(\t\x12R\n\x10deployment_state\x18\x02 \x01(\x0e28.google.cloud.gkehub.configmanagement.v1.DeploymentState\x12E\n\x06errors\x18\x03 \x03(\x0b25.google.cloud.gkehub.configmanagement.v1.InstallError"%\n\x0cInstallError\x12\x15\n\rerror_message\x18\x01 \x01(\t"\xc4\x06\n\x0fConfigSyncState\x12K\n\x07version\x18\x01 \x01(\x0b2:.google.cloud.gkehub.configmanagement.v1.ConfigSyncVersion\x12\\\n\x10deployment_state\x18\x02 \x01(\x0b2B.google.cloud.gkehub.configmanagement.v1.ConfigSyncDeploymentState\x12F\n\nsync_state\x18\x03 \x01(\x0b22.google.cloud.gkehub.configmanagement.v1.SyncState\x12H\n\x06errors\x18\x04 \x03(\x0b28.google.cloud.gkehub.configmanagement.v1.ConfigSyncError\x12W\n\x0crootsync_crd\x18\x05 \x01(\x0e2A.google.cloud.gkehub.configmanagement.v1.ConfigSyncState.CRDState\x12W\n\x0creposync_crd\x18\x06 \x01(\x0e2A.google.cloud.gkehub.configmanagement.v1.ConfigSyncState.CRDState\x12M\n\x05state\x18\x07 \x01(\x0e2>.google.cloud.gkehub.configmanagement.v1.ConfigSyncState.State"h\n\x08CRDState\x12\x19\n\x15CRD_STATE_UNSPECIFIED\x10\x00\x12\x11\n\rNOT_INSTALLED\x10\x01\x12\r\n\tINSTALLED\x10\x02\x12\x0f\n\x0bTERMINATING\x10\x03\x12\x0e\n\nINSTALLING\x10\x04"\x88\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x1d\n\x19CONFIG_SYNC_NOT_INSTALLED\x10\x01\x12\x19\n\x15CONFIG_SYNC_INSTALLED\x10\x02\x12\x15\n\x11CONFIG_SYNC_ERROR\x10\x03\x12\x17\n\x13CONFIG_SYNC_PENDING\x10\x04"(\n\x0fConfigSyncError\x12\x15\n\rerror_message\x18\x01 \x01(\t"\xa8\x01\n\x11ConfigSyncVersion\x12\x10\n\x08importer\x18\x01 \x01(\t\x12\x0e\n\x06syncer\x18\x02 \x01(\t\x12\x10\n\x08git_sync\x18\x03 \x01(\t\x12\x0f\n\x07monitor\x18\x04 \x01(\t\x12\x1a\n\x12reconciler_manager\x18\x05 \x01(\t\x12\x17\n\x0froot_reconciler\x18\x06 \x01(\t\x12\x19\n\x11admission_webhook\x18\x07 \x01(\t"\xc6\x04\n\x19ConfigSyncDeploymentState\x12J\n\x08importer\x18\x01 \x01(\x0e28.google.cloud.gkehub.configmanagement.v1.DeploymentState\x12H\n\x06syncer\x18\x02 \x01(\x0e28.google.cloud.gkehub.configmanagement.v1.DeploymentState\x12J\n\x08git_sync\x18\x03 \x01(\x0e28.google.cloud.gkehub.configmanagement.v1.DeploymentState\x12I\n\x07monitor\x18\x04 \x01(\x0e28.google.cloud.gkehub.configmanagement.v1.DeploymentState\x12T\n\x12reconciler_manager\x18\x05 \x01(\x0e28.google.cloud.gkehub.configmanagement.v1.DeploymentState\x12Q\n\x0froot_reconciler\x18\x06 \x01(\x0e28.google.cloud.gkehub.configmanagement.v1.DeploymentState\x12S\n\x11admission_webhook\x18\x07 \x01(\x0e28.google.cloud.gkehub.configmanagement.v1.DeploymentState"\xbb\x03\n\tSyncState\x12\x14\n\x0csource_token\x18\x01 \x01(\t\x12\x14\n\x0cimport_token\x18\x02 \x01(\t\x12\x12\n\nsync_token\x18\x03 \x01(\t\x12\x15\n\tlast_sync\x18\x04 \x01(\tB\x02\x18\x01\x122\n\x0elast_sync_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12I\n\x04code\x18\x05 \x01(\x0e2;.google.cloud.gkehub.configmanagement.v1.SyncState.SyncCode\x12B\n\x06errors\x18\x06 \x03(\x0b22.google.cloud.gkehub.configmanagement.v1.SyncError"\x93\x01\n\x08SyncCode\x12\x19\n\x15SYNC_CODE_UNSPECIFIED\x10\x00\x12\n\n\x06SYNCED\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\t\n\x05ERROR\x10\x03\x12\x12\n\x0eNOT_CONFIGURED\x10\x04\x12\x11\n\rNOT_INSTALLED\x10\x05\x12\x10\n\x0cUNAUTHORIZED\x10\x06\x12\x0f\n\x0bUNREACHABLE\x10\x07"\x81\x01\n\tSyncError\x12\x0c\n\x04code\x18\x01 \x01(\t\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12O\n\x0ferror_resources\x18\x03 \x03(\x0b26.google.cloud.gkehub.configmanagement.v1.ErrorResource"\xa8\x01\n\rErrorResource\x12\x13\n\x0bsource_path\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x1a\n\x12resource_namespace\x18\x03 \x01(\t\x12O\n\x0cresource_gvk\x18\x04 \x01(\x0b29.google.cloud.gkehub.configmanagement.v1.GroupVersionKind"@\n\x10GroupVersionKind\x12\r\n\x05group\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0c\n\x04kind\x18\x03 \x01(\t"\xc8\x01\n\x15PolicyControllerState\x12Q\n\x07version\x18\x01 \x01(\x0b2@.google.cloud.gkehub.configmanagement.v1.PolicyControllerVersion\x12\\\n\x10deployment_state\x18\x02 \x01(\x0b2B.google.cloud.gkehub.configmanagement.v1.GatekeeperDeploymentState"*\n\x17PolicyControllerVersion\x12\x0f\n\x07version\x18\x01 \x01(\t"\xd6\x01\n\x19GatekeeperDeploymentState\x12e\n#gatekeeper_controller_manager_state\x18\x01 \x01(\x0e28.google.cloud.gkehub.configmanagement.v1.DeploymentState\x12R\n\x10gatekeeper_audit\x18\x02 \x01(\x0e28.google.cloud.gkehub.configmanagement.v1.DeploymentState*m\n\x0fDeploymentState\x12 \n\x1cDEPLOYMENT_STATE_UNSPECIFIED\x10\x00\x12\x11\n\rNOT_INSTALLED\x10\x01\x12\r\n\tINSTALLED\x10\x02\x12\t\n\x05ERROR\x10\x03\x12\x0b\n\x07PENDING\x10\x04B\xa1\x02\n+com.google.cloud.gkehub.configmanagement.v1B\x15ConfigManagementProtoP\x01ZWcloud.google.com/go/gkehub/configmanagement/apiv1/configmanagementpb;configmanagementpb\xaa\x02\'Google.Cloud.GkeHub.ConfigManagement.V1\xca\x02\'Google\\Cloud\\GkeHub\\ConfigManagement\\V1\xea\x02+Google::Cloud::GkeHub::ConfigManagement::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkehub.v1.configmanagement.configmanagement_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.cloud.gkehub.configmanagement.v1B\x15ConfigManagementProtoP\x01ZWcloud.google.com/go/gkehub/configmanagement/apiv1/configmanagementpb;configmanagementpb\xaa\x02'Google.Cloud.GkeHub.ConfigManagement.V1\xca\x02'Google\\Cloud\\GkeHub\\ConfigManagement\\V1\xea\x02+Google::Cloud::GkeHub::ConfigManagement::V1"
    _globals['_SYNCSTATE'].fields_by_name['last_sync']._loaded_options = None
    _globals['_SYNCSTATE'].fields_by_name['last_sync']._serialized_options = b'\x18\x01'
    _globals['_DEPLOYMENTSTATE']._serialized_start = 5704
    _globals['_DEPLOYMENTSTATE']._serialized_end = 5813
    _globals['_MEMBERSHIPSTATE']._serialized_start = 141
    _globals['_MEMBERSHIPSTATE']._serialized_end = 627
    _globals['_MEMBERSHIPSPEC']._serialized_start = 630
    _globals['_MEMBERSHIPSPEC']._serialized_end = 1117
    _globals['_MEMBERSHIPSPEC_MANAGEMENT']._serialized_start = 1028
    _globals['_MEMBERSHIPSPEC_MANAGEMENT']._serialized_end = 1117
    _globals['_CONFIGSYNC']._serialized_start = 1120
    _globals['_CONFIGSYNC']._serialized_end = 1385
    _globals['_GITCONFIG']._serialized_start = 1388
    _globals['_GITCONFIG']._serialized_end = 1578
    _globals['_OCICONFIG']._serialized_start = 1581
    _globals['_OCICONFIG']._serialized_end = 1711
    _globals['_POLICYCONTROLLER']._serialized_start = 1714
    _globals['_POLICYCONTROLLER']._serialized_end = 1979
    _globals['_HIERARCHYCONTROLLERCONFIG']._serialized_start = 1981
    _globals['_HIERARCHYCONTROLLERCONFIG']._serialized_end = 2101
    _globals['_HIERARCHYCONTROLLERDEPLOYMENTSTATE']._serialized_start = 2104
    _globals['_HIERARCHYCONTROLLERDEPLOYMENTSTATE']._serialized_end = 2288
    _globals['_HIERARCHYCONTROLLERVERSION']._serialized_start = 2290
    _globals['_HIERARCHYCONTROLLERVERSION']._serialized_end = 2350
    _globals['_HIERARCHYCONTROLLERSTATE']._serialized_start = 2353
    _globals['_HIERARCHYCONTROLLERSTATE']._serialized_end = 2557
    _globals['_OPERATORSTATE']._serialized_start = 2560
    _globals['_OPERATORSTATE']._serialized_end = 2747
    _globals['_INSTALLERROR']._serialized_start = 2749
    _globals['_INSTALLERROR']._serialized_end = 2786
    _globals['_CONFIGSYNCSTATE']._serialized_start = 2789
    _globals['_CONFIGSYNCSTATE']._serialized_end = 3625
    _globals['_CONFIGSYNCSTATE_CRDSTATE']._serialized_start = 3382
    _globals['_CONFIGSYNCSTATE_CRDSTATE']._serialized_end = 3486
    _globals['_CONFIGSYNCSTATE_STATE']._serialized_start = 3489
    _globals['_CONFIGSYNCSTATE_STATE']._serialized_end = 3625
    _globals['_CONFIGSYNCERROR']._serialized_start = 3627
    _globals['_CONFIGSYNCERROR']._serialized_end = 3667
    _globals['_CONFIGSYNCVERSION']._serialized_start = 3670
    _globals['_CONFIGSYNCVERSION']._serialized_end = 3838
    _globals['_CONFIGSYNCDEPLOYMENTSTATE']._serialized_start = 3841
    _globals['_CONFIGSYNCDEPLOYMENTSTATE']._serialized_end = 4423
    _globals['_SYNCSTATE']._serialized_start = 4426
    _globals['_SYNCSTATE']._serialized_end = 4869
    _globals['_SYNCSTATE_SYNCCODE']._serialized_start = 4722
    _globals['_SYNCSTATE_SYNCCODE']._serialized_end = 4869
    _globals['_SYNCERROR']._serialized_start = 4872
    _globals['_SYNCERROR']._serialized_end = 5001
    _globals['_ERRORRESOURCE']._serialized_start = 5004
    _globals['_ERRORRESOURCE']._serialized_end = 5172
    _globals['_GROUPVERSIONKIND']._serialized_start = 5174
    _globals['_GROUPVERSIONKIND']._serialized_end = 5238
    _globals['_POLICYCONTROLLERSTATE']._serialized_start = 5241
    _globals['_POLICYCONTROLLERSTATE']._serialized_end = 5441
    _globals['_POLICYCONTROLLERVERSION']._serialized_start = 5443
    _globals['_POLICYCONTROLLERVERSION']._serialized_end = 5485
    _globals['_GATEKEEPERDEPLOYMENTSTATE']._serialized_start = 5488
    _globals['_GATEKEEPERDEPLOYMENTSTATE']._serialized_end = 5702