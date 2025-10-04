"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/gkehub/v1alpha/configmanagement/configmanagement.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/cloud/gkehub/v1alpha/configmanagement/configmanagement.proto\x12,google.cloud.gkehub.configmanagement.v1alpha\x1a\x1fgoogle/protobuf/timestamp.proto"\xd4\x04\n\x0fMembershipState\x12\x14\n\x0ccluster_name\x18\x01 \x01(\t\x12U\n\x0fmembership_spec\x18\x02 \x01(\x0b2<.google.cloud.gkehub.configmanagement.v1alpha.MembershipSpec\x12S\n\x0eoperator_state\x18\x03 \x01(\x0b2;.google.cloud.gkehub.configmanagement.v1alpha.OperatorState\x12X\n\x11config_sync_state\x18\x04 \x01(\x0b2=.google.cloud.gkehub.configmanagement.v1alpha.ConfigSyncState\x12d\n\x17policy_controller_state\x18\x05 \x01(\x0b2C.google.cloud.gkehub.configmanagement.v1alpha.PolicyControllerState\x12S\n\x0ebinauthz_state\x18\x06 \x01(\x0b2;.google.cloud.gkehub.configmanagement.v1alpha.BinauthzState\x12j\n\x1ahierarchy_controller_state\x18\x07 \x01(\x0b2F.google.cloud.gkehub.configmanagement.v1alpha.HierarchyControllerState"\x82\x03\n\x0eMembershipSpec\x12M\n\x0bconfig_sync\x18\x01 \x01(\x0b28.google.cloud.gkehub.configmanagement.v1alpha.ConfigSync\x12Y\n\x11policy_controller\x18\x02 \x01(\x0b2>.google.cloud.gkehub.configmanagement.v1alpha.PolicyController\x12N\n\x08binauthz\x18\x03 \x01(\x0b2<.google.cloud.gkehub.configmanagement.v1alpha.BinauthzConfig\x12e\n\x14hierarchy_controller\x18\x04 \x01(\x0b2G.google.cloud.gkehub.configmanagement.v1alpha.HierarchyControllerConfig\x12\x0f\n\x07version\x18\n \x01(\t"i\n\nConfigSync\x12D\n\x03git\x18\x07 \x01(\x0b27.google.cloud.gkehub.configmanagement.v1alpha.GitConfig\x12\x15\n\rsource_format\x18\x08 \x01(\t"\xbe\x01\n\tGitConfig\x12\x11\n\tsync_repo\x18\x01 \x01(\t\x12\x13\n\x0bsync_branch\x18\x02 \x01(\t\x12\x12\n\npolicy_dir\x18\x03 \x01(\t\x12\x16\n\x0esync_wait_secs\x18\x04 \x01(\x03\x12\x10\n\x08sync_rev\x18\x05 \x01(\t\x12\x13\n\x0bsecret_type\x18\x06 \x01(\t\x12\x13\n\x0bhttps_proxy\x18\x07 \x01(\t\x12!\n\x19gcp_service_account_email\x18\x08 \x01(\t"\xa3\x02\n\x10PolicyController\x12\x0f\n\x07enabled\x18\x01 \x01(\x08\x12\'\n\x1atemplate_library_installed\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12#\n\x16audit_interval_seconds\x18\x03 \x01(\x03H\x01\x88\x01\x01\x12\x1d\n\x15exemptable_namespaces\x18\x04 \x03(\t\x12!\n\x19referential_rules_enabled\x18\x05 \x01(\x08\x12\x1a\n\x12log_denies_enabled\x18\x06 \x01(\x08\x12\x18\n\x10mutation_enabled\x18\x07 \x01(\x08B\x1d\n\x1b_template_library_installedB\x19\n\x17_audit_interval_seconds"!\n\x0eBinauthzConfig\x12\x0f\n\x07enabled\x18\x01 \x01(\x08"x\n\x19HierarchyControllerConfig\x12\x0f\n\x07enabled\x18\x01 \x01(\x08\x12\x1e\n\x16enable_pod_tree_labels\x18\x02 \x01(\x08\x12*\n"enable_hierarchical_resource_quota\x18\x03 \x01(\x08"\xc2\x01\n"HierarchyControllerDeploymentState\x12J\n\x03hnc\x18\x01 \x01(\x0e2=.google.cloud.gkehub.configmanagement.v1alpha.DeploymentState\x12P\n\textension\x18\x02 \x01(\x0e2=.google.cloud.gkehub.configmanagement.v1alpha.DeploymentState"<\n\x1aHierarchyControllerVersion\x12\x0b\n\x03hnc\x18\x01 \x01(\t\x12\x11\n\textension\x18\x02 \x01(\t"\xd6\x01\n\x18HierarchyControllerState\x12Y\n\x07version\x18\x01 \x01(\x0b2H.google.cloud.gkehub.configmanagement.v1alpha.HierarchyControllerVersion\x12_\n\x05state\x18\x02 \x01(\x0b2P.google.cloud.gkehub.configmanagement.v1alpha.HierarchyControllerDeploymentState"\xc5\x01\n\rOperatorState\x12\x0f\n\x07version\x18\x01 \x01(\t\x12W\n\x10deployment_state\x18\x02 \x01(\x0e2=.google.cloud.gkehub.configmanagement.v1alpha.DeploymentState\x12J\n\x06errors\x18\x03 \x03(\x0b2:.google.cloud.gkehub.configmanagement.v1alpha.InstallError"%\n\x0cInstallError\x12\x15\n\rerror_message\x18\x01 \x01(\t"\x93\x02\n\x0fConfigSyncState\x12P\n\x07version\x18\x01 \x01(\x0b2?.google.cloud.gkehub.configmanagement.v1alpha.ConfigSyncVersion\x12a\n\x10deployment_state\x18\x02 \x01(\x0b2G.google.cloud.gkehub.configmanagement.v1alpha.ConfigSyncDeploymentState\x12K\n\nsync_state\x18\x03 \x01(\x0b27.google.cloud.gkehub.configmanagement.v1alpha.SyncState"\x8d\x01\n\x11ConfigSyncVersion\x12\x10\n\x08importer\x18\x01 \x01(\t\x12\x0e\n\x06syncer\x18\x02 \x01(\t\x12\x10\n\x08git_sync\x18\x03 \x01(\t\x12\x0f\n\x07monitor\x18\x04 \x01(\t\x12\x1a\n\x12reconciler_manager\x18\x05 \x01(\t\x12\x17\n\x0froot_reconciler\x18\x06 \x01(\t"\x8f\x04\n\x19ConfigSyncDeploymentState\x12O\n\x08importer\x18\x01 \x01(\x0e2=.google.cloud.gkehub.configmanagement.v1alpha.DeploymentState\x12M\n\x06syncer\x18\x02 \x01(\x0e2=.google.cloud.gkehub.configmanagement.v1alpha.DeploymentState\x12O\n\x08git_sync\x18\x03 \x01(\x0e2=.google.cloud.gkehub.configmanagement.v1alpha.DeploymentState\x12N\n\x07monitor\x18\x04 \x01(\x0e2=.google.cloud.gkehub.configmanagement.v1alpha.DeploymentState\x12Y\n\x12reconciler_manager\x18\x05 \x01(\x0e2=.google.cloud.gkehub.configmanagement.v1alpha.DeploymentState\x12V\n\x0froot_reconciler\x18\x06 \x01(\x0e2=.google.cloud.gkehub.configmanagement.v1alpha.DeploymentState"\xc5\x03\n\tSyncState\x12\x14\n\x0csource_token\x18\x01 \x01(\t\x12\x14\n\x0cimport_token\x18\x02 \x01(\t\x12\x12\n\nsync_token\x18\x03 \x01(\t\x12\x15\n\tlast_sync\x18\x04 \x01(\tB\x02\x18\x01\x122\n\x0elast_sync_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12N\n\x04code\x18\x05 \x01(\x0e2@.google.cloud.gkehub.configmanagement.v1alpha.SyncState.SyncCode\x12G\n\x06errors\x18\x06 \x03(\x0b27.google.cloud.gkehub.configmanagement.v1alpha.SyncError"\x93\x01\n\x08SyncCode\x12\x19\n\x15SYNC_CODE_UNSPECIFIED\x10\x00\x12\n\n\x06SYNCED\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\t\n\x05ERROR\x10\x03\x12\x12\n\x0eNOT_CONFIGURED\x10\x04\x12\x11\n\rNOT_INSTALLED\x10\x05\x12\x10\n\x0cUNAUTHORIZED\x10\x06\x12\x0f\n\x0bUNREACHABLE\x10\x07"\x86\x01\n\tSyncError\x12\x0c\n\x04code\x18\x01 \x01(\t\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12T\n\x0ferror_resources\x18\x03 \x03(\x0b2;.google.cloud.gkehub.configmanagement.v1alpha.ErrorResource"\xad\x01\n\rErrorResource\x12\x13\n\x0bsource_path\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x1a\n\x12resource_namespace\x18\x03 \x01(\t\x12T\n\x0cresource_gvk\x18\x04 \x01(\x0b2>.google.cloud.gkehub.configmanagement.v1alpha.GroupVersionKind"@\n\x10GroupVersionKind\x12\r\n\x05group\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0c\n\x04kind\x18\x03 \x01(\t"\xd2\x01\n\x15PolicyControllerState\x12V\n\x07version\x18\x01 \x01(\x0b2E.google.cloud.gkehub.configmanagement.v1alpha.PolicyControllerVersion\x12a\n\x10deployment_state\x18\x02 \x01(\x0b2G.google.cloud.gkehub.configmanagement.v1alpha.GatekeeperDeploymentState"*\n\x17PolicyControllerVersion\x12\x0f\n\x07version\x18\x01 \x01(\t"\xaf\x01\n\rBinauthzState\x12N\n\x07webhook\x18\x01 \x01(\x0e2=.google.cloud.gkehub.configmanagement.v1alpha.DeploymentState\x12N\n\x07version\x18\x02 \x01(\x0b2=.google.cloud.gkehub.configmanagement.v1alpha.BinauthzVersion"*\n\x0fBinauthzVersion\x12\x17\n\x0fwebhook_version\x18\x01 \x01(\t"\xbc\x02\n\x19GatekeeperDeploymentState\x12j\n#gatekeeper_controller_manager_state\x18\x01 \x01(\x0e2=.google.cloud.gkehub.configmanagement.v1alpha.DeploymentState\x12W\n\x10gatekeeper_audit\x18\x02 \x01(\x0e2=.google.cloud.gkehub.configmanagement.v1alpha.DeploymentState\x12Z\n\x13gatekeeper_mutation\x18\x03 \x01(\x0e2=.google.cloud.gkehub.configmanagement.v1alpha.DeploymentState*`\n\x0fDeploymentState\x12 \n\x1cDEPLOYMENT_STATE_UNSPECIFIED\x10\x00\x12\x11\n\rNOT_INSTALLED\x10\x01\x12\r\n\tINSTALLED\x10\x02\x12\t\n\x05ERROR\x10\x03B\xba\x02\n0com.google.cloud.gkehub.configmanagement.v1alphaB\x15ConfigManagementProtoP\x01Z\\cloud.google.com/go/gkehub/configmanagement/apiv1alpha/configmanagementpb;configmanagementpb\xaa\x02,Google.Cloud.GkeHub.ConfigManagement.V1Alpha\xca\x02,Google\\Cloud\\GkeHub\\ConfigManagement\\V1alpha\xea\x020Google::Cloud::GkeHub::ConfigManagement::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkehub.v1alpha.configmanagement.configmanagement_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n0com.google.cloud.gkehub.configmanagement.v1alphaB\x15ConfigManagementProtoP\x01Z\\cloud.google.com/go/gkehub/configmanagement/apiv1alpha/configmanagementpb;configmanagementpb\xaa\x02,Google.Cloud.GkeHub.ConfigManagement.V1Alpha\xca\x02,Google\\Cloud\\GkeHub\\ConfigManagement\\V1alpha\xea\x020Google::Cloud::GkeHub::ConfigManagement::V1alpha'
    _globals['_SYNCSTATE'].fields_by_name['last_sync']._loaded_options = None
    _globals['_SYNCSTATE'].fields_by_name['last_sync']._serialized_options = b'\x18\x01'
    _globals['_DEPLOYMENTSTATE']._serialized_start = 5189
    _globals['_DEPLOYMENTSTATE']._serialized_end = 5285
    _globals['_MEMBERSHIPSTATE']._serialized_start = 151
    _globals['_MEMBERSHIPSTATE']._serialized_end = 747
    _globals['_MEMBERSHIPSPEC']._serialized_start = 750
    _globals['_MEMBERSHIPSPEC']._serialized_end = 1136
    _globals['_CONFIGSYNC']._serialized_start = 1138
    _globals['_CONFIGSYNC']._serialized_end = 1243
    _globals['_GITCONFIG']._serialized_start = 1246
    _globals['_GITCONFIG']._serialized_end = 1436
    _globals['_POLICYCONTROLLER']._serialized_start = 1439
    _globals['_POLICYCONTROLLER']._serialized_end = 1730
    _globals['_BINAUTHZCONFIG']._serialized_start = 1732
    _globals['_BINAUTHZCONFIG']._serialized_end = 1765
    _globals['_HIERARCHYCONTROLLERCONFIG']._serialized_start = 1767
    _globals['_HIERARCHYCONTROLLERCONFIG']._serialized_end = 1887
    _globals['_HIERARCHYCONTROLLERDEPLOYMENTSTATE']._serialized_start = 1890
    _globals['_HIERARCHYCONTROLLERDEPLOYMENTSTATE']._serialized_end = 2084
    _globals['_HIERARCHYCONTROLLERVERSION']._serialized_start = 2086
    _globals['_HIERARCHYCONTROLLERVERSION']._serialized_end = 2146
    _globals['_HIERARCHYCONTROLLERSTATE']._serialized_start = 2149
    _globals['_HIERARCHYCONTROLLERSTATE']._serialized_end = 2363
    _globals['_OPERATORSTATE']._serialized_start = 2366
    _globals['_OPERATORSTATE']._serialized_end = 2563
    _globals['_INSTALLERROR']._serialized_start = 2565
    _globals['_INSTALLERROR']._serialized_end = 2602
    _globals['_CONFIGSYNCSTATE']._serialized_start = 2605
    _globals['_CONFIGSYNCSTATE']._serialized_end = 2880
    _globals['_CONFIGSYNCVERSION']._serialized_start = 2883
    _globals['_CONFIGSYNCVERSION']._serialized_end = 3024
    _globals['_CONFIGSYNCDEPLOYMENTSTATE']._serialized_start = 3027
    _globals['_CONFIGSYNCDEPLOYMENTSTATE']._serialized_end = 3554
    _globals['_SYNCSTATE']._serialized_start = 3557
    _globals['_SYNCSTATE']._serialized_end = 4010
    _globals['_SYNCSTATE_SYNCCODE']._serialized_start = 3863
    _globals['_SYNCSTATE_SYNCCODE']._serialized_end = 4010
    _globals['_SYNCERROR']._serialized_start = 4013
    _globals['_SYNCERROR']._serialized_end = 4147
    _globals['_ERRORRESOURCE']._serialized_start = 4150
    _globals['_ERRORRESOURCE']._serialized_end = 4323
    _globals['_GROUPVERSIONKIND']._serialized_start = 4325
    _globals['_GROUPVERSIONKIND']._serialized_end = 4389
    _globals['_POLICYCONTROLLERSTATE']._serialized_start = 4392
    _globals['_POLICYCONTROLLERSTATE']._serialized_end = 4602
    _globals['_POLICYCONTROLLERVERSION']._serialized_start = 4604
    _globals['_POLICYCONTROLLERVERSION']._serialized_end = 4646
    _globals['_BINAUTHZSTATE']._serialized_start = 4649
    _globals['_BINAUTHZSTATE']._serialized_end = 4824
    _globals['_BINAUTHZVERSION']._serialized_start = 4826
    _globals['_BINAUTHZVERSION']._serialized_end = 4868
    _globals['_GATEKEEPERDEPLOYMENTSTATE']._serialized_start = 4871
    _globals['_GATEKEEPERDEPLOYMENTSTATE']._serialized_end = 5187