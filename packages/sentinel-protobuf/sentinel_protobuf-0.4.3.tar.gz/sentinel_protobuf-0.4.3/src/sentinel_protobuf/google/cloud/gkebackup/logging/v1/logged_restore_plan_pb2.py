"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/gkebackup/logging/v1/logged_restore_plan.proto')
_sym_db = _symbol_database.Default()
from ......google.cloud.gkebackup.logging.v1 import logged_common_pb2 as google_dot_cloud_dot_gkebackup_dot_logging_dot_v1_dot_logged__common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/cloud/gkebackup/logging/v1/logged_restore_plan.proto\x12!google.cloud.gkebackup.logging.v1\x1a5google/cloud/gkebackup/logging/v1/logged_common.proto"\x99\x02\n\x11LoggedRestorePlan\x12\x13\n\x0bdescription\x18\x01 \x01(\t\x12\x13\n\x0bbackup_plan\x18\x02 \x01(\t\x12\x0f\n\x07cluster\x18\x03 \x01(\t\x12H\n\x0erestore_config\x18\x04 \x01(\x0b20.google.cloud.gkebackup.logging.v1.RestoreConfig\x12P\n\x06labels\x18\x05 \x03(\x0b2@.google.cloud.gkebackup.logging.v1.LoggedRestorePlan.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x97\x15\n\rRestoreConfig\x12l\n\x1avolume_data_restore_policy\x18\x01 \x01(\x0e2H.google.cloud.gkebackup.logging.v1.RestoreConfig.VolumeDataRestorePolicy\x12x\n cluster_resource_conflict_policy\x18\x02 \x01(\x0e2N.google.cloud.gkebackup.logging.v1.RestoreConfig.ClusterResourceConflictPolicy\x12x\n namespaced_resource_restore_mode\x18\x03 \x01(\x0e2N.google.cloud.gkebackup.logging.v1.RestoreConfig.NamespacedResourceRestoreMode\x12t\n\x1ecluster_resource_restore_scope\x18\x04 \x01(\x0b2L.google.cloud.gkebackup.logging.v1.RestoreConfig.ClusterResourceRestoreScope\x12\x18\n\x0eall_namespaces\x18\x05 \x01(\x08H\x00\x12L\n\x13selected_namespaces\x18\x06 \x01(\x0b2-.google.cloud.gkebackup.logging.v1.NamespacesH\x00\x12S\n\x15selected_applications\x18\x07 \x01(\x0b22.google.cloud.gkebackup.logging.v1.NamespacedNamesH\x00\x12\x17\n\rno_namespaces\x18\t \x01(\x08H\x00\x12L\n\x13excluded_namespaces\x18\n \x01(\x0b2-.google.cloud.gkebackup.logging.v1.NamespacesH\x00\x12]\n\x12substitution_rules\x18\x08 \x03(\x0b2A.google.cloud.gkebackup.logging.v1.RestoreConfig.SubstitutionRule\x12a\n\x14transformation_rules\x18\x0b \x03(\x0b2C.google.cloud.gkebackup.logging.v1.RestoreConfig.TransformationRule\x1a:\n\tGroupKind\x12\x16\n\x0eresource_group\x18\x01 \x01(\t\x12\x15\n\rresource_kind\x18\x02 \x01(\t\x1a\x82\x02\n\x1bClusterResourceRestoreScope\x12X\n\x14selected_group_kinds\x18\x01 \x03(\x0b2:.google.cloud.gkebackup.logging.v1.RestoreConfig.GroupKind\x12X\n\x14excluded_group_kinds\x18\x02 \x03(\x0b2:.google.cloud.gkebackup.logging.v1.RestoreConfig.GroupKind\x12\x17\n\x0fall_group_kinds\x18\x03 \x01(\x08\x12\x16\n\x0eno_group_kinds\x18\x04 \x01(\x08\x1a\xd2\x01\n\x10SubstitutionRule\x12\x19\n\x11target_namespaces\x18\x01 \x03(\t\x12V\n\x12target_group_kinds\x18\x02 \x03(\x0b2:.google.cloud.gkebackup.logging.v1.RestoreConfig.GroupKind\x12\x18\n\x10target_json_path\x18\x03 \x01(\t\x12\x1e\n\x16original_value_pattern\x18\x04 \x01(\t\x12\x11\n\tnew_value\x18\x05 \x01(\t\x1a\xfe\x01\n\x18TransformationRuleAction\x12X\n\x02op\x18\x01 \x01(\x0e2L.google.cloud.gkebackup.logging.v1.RestoreConfig.TransformationRuleAction.Op\x12\x11\n\tfrom_path\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\r\n\x05value\x18\x04 \x01(\t"X\n\x02Op\x12\x12\n\x0eOP_UNSPECIFIED\x10\x00\x12\n\n\x06REMOVE\x10\x01\x12\x08\n\x04MOVE\x10\x02\x12\x08\n\x04COPY\x10\x03\x12\x07\n\x03ADD\x10\x04\x12\x08\n\x04TEST\x10\x05\x12\x0b\n\x07REPLACE\x10\x06\x1a\x88\x01\n\x0eResourceFilter\x12\x12\n\nnamespaces\x18\x01 \x03(\t\x12O\n\x0bgroup_kinds\x18\x02 \x03(\x0b2:.google.cloud.gkebackup.logging.v1.RestoreConfig.GroupKind\x12\x11\n\tjson_path\x18\x03 \x01(\t\x1a\xe5\x01\n\x12TransformationRule\x12`\n\rfield_actions\x18\x01 \x03(\x0b2I.google.cloud.gkebackup.logging.v1.RestoreConfig.TransformationRuleAction\x12X\n\x0fresource_filter\x18\x02 \x01(\x0b2?.google.cloud.gkebackup.logging.v1.RestoreConfig.ResourceFilter\x12\x13\n\x0bdescription\x18\x03 \x01(\t"\xaf\x01\n\x17VolumeDataRestorePolicy\x12*\n&VOLUME_DATA_RESTORE_POLICY_UNSPECIFIED\x10\x00\x12#\n\x1fRESTORE_VOLUME_DATA_FROM_BACKUP\x10\x01\x12#\n\x1fREUSE_VOLUME_HANDLE_FROM_BACKUP\x10\x02\x12\x1e\n\x1aNO_VOLUME_DATA_RESTORATION\x10\x03"\x83\x01\n\x1dClusterResourceConflictPolicy\x120\n,CLUSTER_RESOURCE_CONFLICT_POLICY_UNSPECIFIED\x10\x00\x12\x18\n\x14USE_EXISTING_VERSION\x10\x01\x12\x16\n\x12USE_BACKUP_VERSION\x10\x02"\xe0\x01\n\x1dNamespacedResourceRestoreMode\x120\n,NAMESPACED_RESOURCE_RESTORE_MODE_UNSPECIFIED\x10\x00\x12\x16\n\x12DELETE_AND_RESTORE\x10\x01\x12\x14\n\x10FAIL_ON_CONFLICT\x10\x02\x12\x1a\n\x16MERGE_SKIP_ON_CONFLICT\x10\x03\x12$\n MERGE_REPLACE_VOLUME_ON_CONFLICT\x10\x04\x12\x1d\n\x19MERGE_REPLACE_ON_CONFLICT\x10\x05B#\n!namespaced_resource_restore_scopeB\xee\x01\n!google.cloud.gkebackup.logging.v1B\x16LoggedRestorePlanProtoP\x01Z?cloud.google.com/go/gkebackup/logging/apiv1/loggingpb;loggingpb\xaa\x02!Google.Cloud.GkeBackup.Logging.V1\xca\x02!Google\\Cloud\\GkeBackup\\Logging\\V1\xea\x02%Google::Cloud::GkeBackup::Logging::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkebackup.logging.v1.logged_restore_plan_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!google.cloud.gkebackup.logging.v1B\x16LoggedRestorePlanProtoP\x01Z?cloud.google.com/go/gkebackup/logging/apiv1/loggingpb;loggingpb\xaa\x02!Google.Cloud.GkeBackup.Logging.V1\xca\x02!Google\\Cloud\\GkeBackup\\Logging\\V1\xea\x02%Google::Cloud::GkeBackup::Logging::V1'
    _globals['_LOGGEDRESTOREPLAN_LABELSENTRY']._loaded_options = None
    _globals['_LOGGEDRESTOREPLAN_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_LOGGEDRESTOREPLAN']._serialized_start = 154
    _globals['_LOGGEDRESTOREPLAN']._serialized_end = 435
    _globals['_LOGGEDRESTOREPLAN_LABELSENTRY']._serialized_start = 390
    _globals['_LOGGEDRESTOREPLAN_LABELSENTRY']._serialized_end = 435
    _globals['_RESTORECONFIG']._serialized_start = 438
    _globals['_RESTORECONFIG']._serialized_end = 3149
    _globals['_RESTORECONFIG_GROUPKIND']._serialized_start = 1413
    _globals['_RESTORECONFIG_GROUPKIND']._serialized_end = 1471
    _globals['_RESTORECONFIG_CLUSTERRESOURCERESTORESCOPE']._serialized_start = 1474
    _globals['_RESTORECONFIG_CLUSTERRESOURCERESTORESCOPE']._serialized_end = 1732
    _globals['_RESTORECONFIG_SUBSTITUTIONRULE']._serialized_start = 1735
    _globals['_RESTORECONFIG_SUBSTITUTIONRULE']._serialized_end = 1945
    _globals['_RESTORECONFIG_TRANSFORMATIONRULEACTION']._serialized_start = 1948
    _globals['_RESTORECONFIG_TRANSFORMATIONRULEACTION']._serialized_end = 2202
    _globals['_RESTORECONFIG_TRANSFORMATIONRULEACTION_OP']._serialized_start = 2114
    _globals['_RESTORECONFIG_TRANSFORMATIONRULEACTION_OP']._serialized_end = 2202
    _globals['_RESTORECONFIG_RESOURCEFILTER']._serialized_start = 2205
    _globals['_RESTORECONFIG_RESOURCEFILTER']._serialized_end = 2341
    _globals['_RESTORECONFIG_TRANSFORMATIONRULE']._serialized_start = 2344
    _globals['_RESTORECONFIG_TRANSFORMATIONRULE']._serialized_end = 2573
    _globals['_RESTORECONFIG_VOLUMEDATARESTOREPOLICY']._serialized_start = 2576
    _globals['_RESTORECONFIG_VOLUMEDATARESTOREPOLICY']._serialized_end = 2751
    _globals['_RESTORECONFIG_CLUSTERRESOURCECONFLICTPOLICY']._serialized_start = 2754
    _globals['_RESTORECONFIG_CLUSTERRESOURCECONFLICTPOLICY']._serialized_end = 2885
    _globals['_RESTORECONFIG_NAMESPACEDRESOURCERESTOREMODE']._serialized_start = 2888
    _globals['_RESTORECONFIG_NAMESPACEDRESOURCERESTOREMODE']._serialized_end = 3112