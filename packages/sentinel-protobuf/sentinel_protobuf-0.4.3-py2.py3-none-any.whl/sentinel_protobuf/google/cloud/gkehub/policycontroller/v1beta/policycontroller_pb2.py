"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/gkehub/policycontroller/v1beta/policycontroller.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/cloud/gkehub/policycontroller/v1beta/policycontroller.proto\x12+google.cloud.gkehub.policycontroller.v1beta"\xf3\x04\n\x0fMembershipState\x12k\n\x10component_states\x18\x03 \x03(\x0b2Q.google.cloud.gkehub.policycontroller.v1beta.MembershipState.ComponentStatesEntry\x12Z\n\x05state\x18\x04 \x01(\x0e2K.google.cloud.gkehub.policycontroller.v1beta.MembershipState.LifecycleState\x12]\n\x14policy_content_state\x18\x06 \x01(\x0b2?.google.cloud.gkehub.policycontroller.v1beta.PolicyContentState\x1as\n\x14ComponentStatesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12J\n\x05value\x18\x02 \x01(\x0b2;.google.cloud.gkehub.policycontroller.v1beta.OnClusterState:\x028\x01"\xc2\x01\n\x0eLifecycleState\x12\x1f\n\x1bLIFECYCLE_STATE_UNSPECIFIED\x10\x00\x12\x11\n\rNOT_INSTALLED\x10\x01\x12\x0e\n\nINSTALLING\x10\x02\x12\n\n\x06ACTIVE\x10\x03\x12\x0c\n\x08UPDATING\x10\x04\x12\x13\n\x0fDECOMMISSIONING\x10\x05\x12\x11\n\rCLUSTER_ERROR\x10\x06\x12\r\n\tHUB_ERROR\x10\x07\x12\r\n\tSUSPENDED\x10\x08\x12\x0c\n\x08DETACHED\x10\t"\xb1\x03\n\x12PolicyContentState\x12[\n\x16template_library_state\x18\x01 \x01(\x0b2;.google.cloud.gkehub.policycontroller.v1beta.OnClusterState\x12h\n\rbundle_states\x18\x02 \x03(\x0b2Q.google.cloud.gkehub.policycontroller.v1beta.PolicyContentState.BundleStatesEntry\x12b\n\x1dreferential_sync_config_state\x18\x03 \x01(\x0b2;.google.cloud.gkehub.policycontroller.v1beta.OnClusterState\x1ap\n\x11BundleStatesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12J\n\x05value\x18\x02 \x01(\x0b2;.google.cloud.gkehub.policycontroller.v1beta.OnClusterState:\x028\x01"\x7f\n\x0eMembershipSpec\x12\\\n\x1cpolicy_controller_hub_config\x18\x01 \x01(\x0b26.google.cloud.gkehub.policycontroller.v1beta.HubConfig\x12\x0f\n\x07version\x18\x02 \x01(\t"\xd0\x07\n\tHubConfig\x12X\n\x0cinstall_spec\x18\x01 \x01(\x0e2B.google.cloud.gkehub.policycontroller.v1beta.HubConfig.InstallSpec\x12#\n\x16audit_interval_seconds\x18\x02 \x01(\x03H\x00\x88\x01\x01\x12\x1d\n\x15exemptable_namespaces\x18\x03 \x03(\t\x12!\n\x19referential_rules_enabled\x18\x04 \x01(\x08\x12\x1a\n\x12log_denies_enabled\x18\x05 \x01(\x08\x12\x18\n\x10mutation_enabled\x18\x06 \x01(\x08\x12V\n\nmonitoring\x18\x08 \x01(\x0b2=.google.cloud.gkehub.policycontroller.v1beta.MonitoringConfigH\x01\x88\x01\x01\x12[\n\x0epolicy_content\x18\t \x01(\x0b2>.google.cloud.gkehub.policycontroller.v1beta.PolicyContentSpecH\x02\x88\x01\x01\x12\'\n\x1aconstraint_violation_limit\x18\n \x01(\x03H\x03\x88\x01\x01\x12i\n\x12deployment_configs\x18\x0b \x03(\x0b2M.google.cloud.gkehub.policycontroller.v1beta.HubConfig.DeploymentConfigsEntry\x1a\x87\x01\n\x16DeploymentConfigsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\\\n\x05value\x18\x02 \x01(\x0b2M.google.cloud.gkehub.policycontroller.v1beta.PolicyControllerDeploymentConfig:\x028\x01"\x9c\x01\n\x0bInstallSpec\x12\x1c\n\x18INSTALL_SPEC_UNSPECIFIED\x10\x00\x12\x1e\n\x1aINSTALL_SPEC_NOT_INSTALLED\x10\x01\x12\x18\n\x14INSTALL_SPEC_ENABLED\x10\x02\x12\x1a\n\x16INSTALL_SPEC_SUSPENDED\x10\x03\x12\x19\n\x15INSTALL_SPEC_DETACHED\x10\x04B\x19\n\x17_audit_interval_secondsB\r\n\x0b_monitoringB\x11\n\x0f_policy_contentB\x1d\n\x1b_constraint_violation_limit"\xbd\x05\n PolicyControllerDeploymentConfig\x12\x1a\n\rreplica_count\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12c\n\x13container_resources\x18\x02 \x01(\x0b2A.google.cloud.gkehub.policycontroller.v1beta.ResourceRequirementsH\x01\x88\x01\x01\x12"\n\x11pod_anti_affinity\x18\x03 \x01(\x08B\x02\x18\x01H\x02\x88\x01\x01\x12q\n\x0fpod_tolerations\x18\x04 \x03(\x0b2X.google.cloud.gkehub.policycontroller.v1beta.PolicyControllerDeploymentConfig.Toleration\x12l\n\x0cpod_affinity\x18\x05 \x01(\x0e2V.google.cloud.gkehub.policycontroller.v1beta.PolicyControllerDeploymentConfig.Affinity\x1a\x88\x01\n\nToleration\x12\x10\n\x03key\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08operator\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x12\n\x05value\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x13\n\x06effect\x18\x04 \x01(\tH\x03\x88\x01\x01B\x06\n\x04_keyB\x0b\n\t_operatorB\x08\n\x06_valueB\t\n\x07_effect"H\n\x08Affinity\x12\x18\n\x14AFFINITY_UNSPECIFIED\x10\x00\x12\x0f\n\x0bNO_AFFINITY\x10\x01\x12\x11\n\rANTI_AFFINITY\x10\x02B\x10\n\x0e_replica_countB\x16\n\x14_container_resourcesB\x14\n\x12_pod_anti_affinity"\xd0\x01\n\x14ResourceRequirements\x12N\n\x06limits\x18\x01 \x01(\x0b29.google.cloud.gkehub.policycontroller.v1beta.ResourceListH\x00\x88\x01\x01\x12P\n\x08requests\x18\x02 \x01(\x0b29.google.cloud.gkehub.policycontroller.v1beta.ResourceListH\x01\x88\x01\x01B\t\n\x07_limitsB\x0b\n\t_requests"H\n\x0cResourceList\x12\x13\n\x06memory\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x03cpu\x18\x02 \x01(\tH\x01\x88\x01\x01B\t\n\x07_memoryB\x06\n\x04_cpu"\xc8\x01\n\x15TemplateLibraryConfig\x12e\n\x0cinstallation\x18\x02 \x01(\x0e2O.google.cloud.gkehub.policycontroller.v1beta.TemplateLibraryConfig.Installation"H\n\x0cInstallation\x12\x1c\n\x18INSTALLATION_UNSPECIFIED\x10\x00\x12\x11\n\rNOT_INSTALLED\x10\x01\x12\x07\n\x03ALL\x10\x02"\xd4\x01\n\x10MonitoringConfig\x12a\n\x08backends\x18\x01 \x03(\x0e2O.google.cloud.gkehub.policycontroller.v1beta.MonitoringConfig.MonitoringBackend"]\n\x11MonitoringBackend\x12"\n\x1eMONITORING_BACKEND_UNSPECIFIED\x10\x00\x12\x0e\n\nPROMETHEUS\x10\x01\x12\x14\n\x10CLOUD_MONITORING\x10\x02"}\n\x0eOnClusterState\x12Z\n\x05state\x18\x01 \x01(\x0e2K.google.cloud.gkehub.policycontroller.v1beta.MembershipState.LifecycleState\x12\x0f\n\x07details\x18\x02 \x01(\t"0\n\x11BundleInstallSpec\x12\x1b\n\x13exempted_namespaces\x18\x02 \x03(\t"\xbf\x02\n\x11PolicyContentSpec\x12\\\n\x07bundles\x18\x01 \x03(\x0b2K.google.cloud.gkehub.policycontroller.v1beta.PolicyContentSpec.BundlesEntry\x12\\\n\x10template_library\x18\x02 \x01(\x0b2B.google.cloud.gkehub.policycontroller.v1beta.TemplateLibraryConfig\x1an\n\x0cBundlesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12M\n\x05value\x18\x02 \x01(\x0b2>.google.cloud.gkehub.policycontroller.v1beta.BundleInstallSpec:\x028\x01B\xb5\x02\n/com.google.cloud.gkehub.policycontroller.v1betaB\x15PolicyControllerProtoP\x01Z[cloud.google.com/go/gkehub/policycontroller/apiv1beta/policycontrollerpb;policycontrollerpb\xaa\x02+Google.Cloud.GkeHub.PolicyController.V1Beta\xca\x02+Google\\Cloud\\GkeHub\\PolicyController\\V1beta\xea\x02/Google::Cloud::GkeHub::PolicyController::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkehub.policycontroller.v1beta.policycontroller_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.cloud.gkehub.policycontroller.v1betaB\x15PolicyControllerProtoP\x01Z[cloud.google.com/go/gkehub/policycontroller/apiv1beta/policycontrollerpb;policycontrollerpb\xaa\x02+Google.Cloud.GkeHub.PolicyController.V1Beta\xca\x02+Google\\Cloud\\GkeHub\\PolicyController\\V1beta\xea\x02/Google::Cloud::GkeHub::PolicyController::V1beta'
    _globals['_MEMBERSHIPSTATE_COMPONENTSTATESENTRY']._loaded_options = None
    _globals['_MEMBERSHIPSTATE_COMPONENTSTATESENTRY']._serialized_options = b'8\x01'
    _globals['_POLICYCONTENTSTATE_BUNDLESTATESENTRY']._loaded_options = None
    _globals['_POLICYCONTENTSTATE_BUNDLESTATESENTRY']._serialized_options = b'8\x01'
    _globals['_HUBCONFIG_DEPLOYMENTCONFIGSENTRY']._loaded_options = None
    _globals['_HUBCONFIG_DEPLOYMENTCONFIGSENTRY']._serialized_options = b'8\x01'
    _globals['_POLICYCONTROLLERDEPLOYMENTCONFIG'].fields_by_name['pod_anti_affinity']._loaded_options = None
    _globals['_POLICYCONTROLLERDEPLOYMENTCONFIG'].fields_by_name['pod_anti_affinity']._serialized_options = b'\x18\x01'
    _globals['_POLICYCONTENTSPEC_BUNDLESENTRY']._loaded_options = None
    _globals['_POLICYCONTENTSPEC_BUNDLESENTRY']._serialized_options = b'8\x01'
    _globals['_MEMBERSHIPSTATE']._serialized_start = 116
    _globals['_MEMBERSHIPSTATE']._serialized_end = 743
    _globals['_MEMBERSHIPSTATE_COMPONENTSTATESENTRY']._serialized_start = 431
    _globals['_MEMBERSHIPSTATE_COMPONENTSTATESENTRY']._serialized_end = 546
    _globals['_MEMBERSHIPSTATE_LIFECYCLESTATE']._serialized_start = 549
    _globals['_MEMBERSHIPSTATE_LIFECYCLESTATE']._serialized_end = 743
    _globals['_POLICYCONTENTSTATE']._serialized_start = 746
    _globals['_POLICYCONTENTSTATE']._serialized_end = 1179
    _globals['_POLICYCONTENTSTATE_BUNDLESTATESENTRY']._serialized_start = 1067
    _globals['_POLICYCONTENTSTATE_BUNDLESTATESENTRY']._serialized_end = 1179
    _globals['_MEMBERSHIPSPEC']._serialized_start = 1181
    _globals['_MEMBERSHIPSPEC']._serialized_end = 1308
    _globals['_HUBCONFIG']._serialized_start = 1311
    _globals['_HUBCONFIG']._serialized_end = 2287
    _globals['_HUBCONFIG_DEPLOYMENTCONFIGSENTRY']._serialized_start = 1901
    _globals['_HUBCONFIG_DEPLOYMENTCONFIGSENTRY']._serialized_end = 2036
    _globals['_HUBCONFIG_INSTALLSPEC']._serialized_start = 2039
    _globals['_HUBCONFIG_INSTALLSPEC']._serialized_end = 2195
    _globals['_POLICYCONTROLLERDEPLOYMENTCONFIG']._serialized_start = 2290
    _globals['_POLICYCONTROLLERDEPLOYMENTCONFIG']._serialized_end = 2991
    _globals['_POLICYCONTROLLERDEPLOYMENTCONFIG_TOLERATION']._serialized_start = 2717
    _globals['_POLICYCONTROLLERDEPLOYMENTCONFIG_TOLERATION']._serialized_end = 2853
    _globals['_POLICYCONTROLLERDEPLOYMENTCONFIG_AFFINITY']._serialized_start = 2855
    _globals['_POLICYCONTROLLERDEPLOYMENTCONFIG_AFFINITY']._serialized_end = 2927
    _globals['_RESOURCEREQUIREMENTS']._serialized_start = 2994
    _globals['_RESOURCEREQUIREMENTS']._serialized_end = 3202
    _globals['_RESOURCELIST']._serialized_start = 3204
    _globals['_RESOURCELIST']._serialized_end = 3276
    _globals['_TEMPLATELIBRARYCONFIG']._serialized_start = 3279
    _globals['_TEMPLATELIBRARYCONFIG']._serialized_end = 3479
    _globals['_TEMPLATELIBRARYCONFIG_INSTALLATION']._serialized_start = 3407
    _globals['_TEMPLATELIBRARYCONFIG_INSTALLATION']._serialized_end = 3479
    _globals['_MONITORINGCONFIG']._serialized_start = 3482
    _globals['_MONITORINGCONFIG']._serialized_end = 3694
    _globals['_MONITORINGCONFIG_MONITORINGBACKEND']._serialized_start = 3601
    _globals['_MONITORINGCONFIG_MONITORINGBACKEND']._serialized_end = 3694
    _globals['_ONCLUSTERSTATE']._serialized_start = 3696
    _globals['_ONCLUSTERSTATE']._serialized_end = 3821
    _globals['_BUNDLEINSTALLSPEC']._serialized_start = 3823
    _globals['_BUNDLEINSTALLSPEC']._serialized_end = 3871
    _globals['_POLICYCONTENTSPEC']._serialized_start = 3874
    _globals['_POLICYCONTENTSPEC']._serialized_end = 4193
    _globals['_POLICYCONTENTSPEC_BUNDLESENTRY']._serialized_start = 4083
    _globals['_POLICYCONTENTSPEC_BUNDLESENTRY']._serialized_end = 4193