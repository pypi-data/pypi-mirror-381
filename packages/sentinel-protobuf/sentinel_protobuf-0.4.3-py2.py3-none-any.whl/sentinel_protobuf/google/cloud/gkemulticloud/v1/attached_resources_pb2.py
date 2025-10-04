"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/gkemulticloud/v1/attached_resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.gkemulticloud.v1 import common_resources_pb2 as google_dot_cloud_dot_gkemulticloud_dot_v1_dot_common__resources__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/gkemulticloud/v1/attached_resources.proto\x12\x1dgoogle.cloud.gkemulticloud.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a4google/cloud/gkemulticloud/v1/common_resources.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xcb\r\n\x0fAttachedCluster\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01\x12K\n\x0boidc_config\x18\x03 \x01(\x0b21.google.cloud.gkemulticloud.v1.AttachedOidcConfigB\x03\xe0A\x02\x12\x1d\n\x10platform_version\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0cdistribution\x18\x10 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x0ecluster_region\x18\x16 \x01(\tB\x03\xe0A\x03\x128\n\x05fleet\x18\x05 \x01(\x0b2$.google.cloud.gkemulticloud.v1.FleetB\x03\xe0A\x02\x12H\n\x05state\x18\x06 \x01(\x0e24.google.cloud.gkemulticloud.v1.AttachedCluster.StateB\x03\xe0A\x03\x12\x10\n\x03uid\x18\x07 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0breconciling\x18\x08 \x01(\x08B\x03\xe0A\x03\x124\n\x0bcreate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x0c\n\x04etag\x18\x0b \x01(\t\x12\x1f\n\x12kubernetes_version\x18\x0c \x01(\tB\x03\xe0A\x03\x12Y\n\x0bannotations\x18\r \x03(\x0b2?.google.cloud.gkemulticloud.v1.AttachedCluster.AnnotationsEntryB\x03\xe0A\x01\x12\\\n\x18workload_identity_config\x18\x0e \x01(\x0b25.google.cloud.gkemulticloud.v1.WorkloadIdentityConfigB\x03\xe0A\x03\x12I\n\x0elogging_config\x18\x0f \x01(\x0b2,.google.cloud.gkemulticloud.v1.LoggingConfigB\x03\xe0A\x01\x12H\n\x06errors\x18\x14 \x03(\x0b23.google.cloud.gkemulticloud.v1.AttachedClusterErrorB\x03\xe0A\x03\x12X\n\rauthorization\x18\x15 \x01(\x0b2<.google.cloud.gkemulticloud.v1.AttachedClustersAuthorizationB\x03\xe0A\x01\x12O\n\x11monitoring_config\x18\x17 \x01(\x0b2/.google.cloud.gkemulticloud.v1.MonitoringConfigB\x03\xe0A\x01\x12M\n\x0cproxy_config\x18\x18 \x01(\x0b22.google.cloud.gkemulticloud.v1.AttachedProxyConfigB\x03\xe0A\x01\x12U\n\x14binary_authorization\x18\x19 \x01(\x0b22.google.cloud.gkemulticloud.v1.BinaryAuthorizationB\x03\xe0A\x01\x12Z\n\x17security_posture_config\x18\x1a \x01(\x0b24.google.cloud.gkemulticloud.v1.SecurityPostureConfigB\x03\xe0A\x01\x12N\n\x04tags\x18\x1b \x03(\x0b28.google.cloud.gkemulticloud.v1.AttachedCluster.TagsEntryB\x06\xe0A\x01\xe0A\x04\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"u\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x10\n\x0cPROVISIONING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\x0f\n\x0bRECONCILING\x10\x03\x12\x0c\n\x08STOPPING\x10\x04\x12\t\n\x05ERROR\x10\x05\x12\x0c\n\x08DEGRADED\x10\x06:~\xeaA{\n,gkemulticloud.googleapis.com/AttachedCluster\x12Kprojects/{project}/locations/{location}/attachedClusters/{attached_cluster}"\xbd\x01\n\x1dAttachedClustersAuthorization\x12L\n\x0badmin_users\x18\x01 \x03(\x0b22.google.cloud.gkemulticloud.v1.AttachedClusterUserB\x03\xe0A\x01\x12N\n\x0cadmin_groups\x18\x02 \x03(\x0b23.google.cloud.gkemulticloud.v1.AttachedClusterGroupB\x03\xe0A\x01",\n\x13AttachedClusterUser\x12\x15\n\x08username\x18\x01 \x01(\tB\x03\xe0A\x02"*\n\x14AttachedClusterGroup\x12\x12\n\x05group\x18\x01 \x01(\tB\x03\xe0A\x02";\n\x12AttachedOidcConfig\x12\x12\n\nissuer_url\x18\x01 \x01(\t\x12\x11\n\x04jwks\x18\x02 \x01(\x0cB\x03\xe0A\x01"\xee\x01\n\x14AttachedServerConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12R\n\x0evalid_versions\x18\x02 \x03(\x0b2:.google.cloud.gkemulticloud.v1.AttachedPlatformVersionInfo:t\xeaAq\n1gkemulticloud.googleapis.com/AttachedServerConfig\x12<projects/{project}/locations/{location}/attachedServerConfig".\n\x1bAttachedPlatformVersionInfo\x12\x0f\n\x07version\x18\x01 \x01(\t"\'\n\x14AttachedClusterError\x12\x0f\n\x07message\x18\x01 \x01(\t"a\n\x13AttachedProxyConfig\x12J\n\x11kubernetes_secret\x18\x01 \x01(\x0b2/.google.cloud.gkemulticloud.v1.KubernetesSecret"3\n\x10KubernetesSecret\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\tB\xe9\x01\n!com.google.cloud.gkemulticloud.v1B\x16AttachedResourcesProtoP\x01ZGcloud.google.com/go/gkemulticloud/apiv1/gkemulticloudpb;gkemulticloudpb\xaa\x02\x1dGoogle.Cloud.GkeMultiCloud.V1\xca\x02\x1dGoogle\\Cloud\\GkeMultiCloud\\V1\xea\x02 Google::Cloud::GkeMultiCloud::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkemulticloud.v1.attached_resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.gkemulticloud.v1B\x16AttachedResourcesProtoP\x01ZGcloud.google.com/go/gkemulticloud/apiv1/gkemulticloudpb;gkemulticloudpb\xaa\x02\x1dGoogle.Cloud.GkeMultiCloud.V1\xca\x02\x1dGoogle\\Cloud\\GkeMultiCloud\\V1\xea\x02 Google::Cloud::GkeMultiCloud::V1'
    _globals['_ATTACHEDCLUSTER_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_ATTACHEDCLUSTER_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_ATTACHEDCLUSTER_TAGSENTRY']._loaded_options = None
    _globals['_ATTACHEDCLUSTER_TAGSENTRY']._serialized_options = b'8\x01'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['description']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['oidc_config']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['oidc_config']._serialized_options = b'\xe0A\x02'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['platform_version']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['platform_version']._serialized_options = b'\xe0A\x02'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['distribution']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['distribution']._serialized_options = b'\xe0A\x02'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['cluster_region']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['cluster_region']._serialized_options = b'\xe0A\x03'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['fleet']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['fleet']._serialized_options = b'\xe0A\x02'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['state']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['uid']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['reconciling']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['reconciling']._serialized_options = b'\xe0A\x03'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['create_time']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['update_time']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['kubernetes_version']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['kubernetes_version']._serialized_options = b'\xe0A\x03'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['annotations']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['annotations']._serialized_options = b'\xe0A\x01'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['workload_identity_config']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['workload_identity_config']._serialized_options = b'\xe0A\x03'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['logging_config']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['logging_config']._serialized_options = b'\xe0A\x01'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['errors']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['errors']._serialized_options = b'\xe0A\x03'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['authorization']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['authorization']._serialized_options = b'\xe0A\x01'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['monitoring_config']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['monitoring_config']._serialized_options = b'\xe0A\x01'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['proxy_config']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['proxy_config']._serialized_options = b'\xe0A\x01'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['binary_authorization']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['binary_authorization']._serialized_options = b'\xe0A\x01'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['security_posture_config']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['security_posture_config']._serialized_options = b'\xe0A\x01'
    _globals['_ATTACHEDCLUSTER'].fields_by_name['tags']._loaded_options = None
    _globals['_ATTACHEDCLUSTER'].fields_by_name['tags']._serialized_options = b'\xe0A\x01\xe0A\x04'
    _globals['_ATTACHEDCLUSTER']._loaded_options = None
    _globals['_ATTACHEDCLUSTER']._serialized_options = b'\xeaA{\n,gkemulticloud.googleapis.com/AttachedCluster\x12Kprojects/{project}/locations/{location}/attachedClusters/{attached_cluster}'
    _globals['_ATTACHEDCLUSTERSAUTHORIZATION'].fields_by_name['admin_users']._loaded_options = None
    _globals['_ATTACHEDCLUSTERSAUTHORIZATION'].fields_by_name['admin_users']._serialized_options = b'\xe0A\x01'
    _globals['_ATTACHEDCLUSTERSAUTHORIZATION'].fields_by_name['admin_groups']._loaded_options = None
    _globals['_ATTACHEDCLUSTERSAUTHORIZATION'].fields_by_name['admin_groups']._serialized_options = b'\xe0A\x01'
    _globals['_ATTACHEDCLUSTERUSER'].fields_by_name['username']._loaded_options = None
    _globals['_ATTACHEDCLUSTERUSER'].fields_by_name['username']._serialized_options = b'\xe0A\x02'
    _globals['_ATTACHEDCLUSTERGROUP'].fields_by_name['group']._loaded_options = None
    _globals['_ATTACHEDCLUSTERGROUP'].fields_by_name['group']._serialized_options = b'\xe0A\x02'
    _globals['_ATTACHEDOIDCCONFIG'].fields_by_name['jwks']._loaded_options = None
    _globals['_ATTACHEDOIDCCONFIG'].fields_by_name['jwks']._serialized_options = b'\xe0A\x01'
    _globals['_ATTACHEDSERVERCONFIG']._loaded_options = None
    _globals['_ATTACHEDSERVERCONFIG']._serialized_options = b'\xeaAq\n1gkemulticloud.googleapis.com/AttachedServerConfig\x12<projects/{project}/locations/{location}/attachedServerConfig'
    _globals['_ATTACHEDCLUSTER']._serialized_start = 237
    _globals['_ATTACHEDCLUSTER']._serialized_end = 1976
    _globals['_ATTACHEDCLUSTER_ANNOTATIONSENTRY']._serialized_start = 1634
    _globals['_ATTACHEDCLUSTER_ANNOTATIONSENTRY']._serialized_end = 1684
    _globals['_ATTACHEDCLUSTER_TAGSENTRY']._serialized_start = 1686
    _globals['_ATTACHEDCLUSTER_TAGSENTRY']._serialized_end = 1729
    _globals['_ATTACHEDCLUSTER_STATE']._serialized_start = 1731
    _globals['_ATTACHEDCLUSTER_STATE']._serialized_end = 1848
    _globals['_ATTACHEDCLUSTERSAUTHORIZATION']._serialized_start = 1979
    _globals['_ATTACHEDCLUSTERSAUTHORIZATION']._serialized_end = 2168
    _globals['_ATTACHEDCLUSTERUSER']._serialized_start = 2170
    _globals['_ATTACHEDCLUSTERUSER']._serialized_end = 2214
    _globals['_ATTACHEDCLUSTERGROUP']._serialized_start = 2216
    _globals['_ATTACHEDCLUSTERGROUP']._serialized_end = 2258
    _globals['_ATTACHEDOIDCCONFIG']._serialized_start = 2260
    _globals['_ATTACHEDOIDCCONFIG']._serialized_end = 2319
    _globals['_ATTACHEDSERVERCONFIG']._serialized_start = 2322
    _globals['_ATTACHEDSERVERCONFIG']._serialized_end = 2560
    _globals['_ATTACHEDPLATFORMVERSIONINFO']._serialized_start = 2562
    _globals['_ATTACHEDPLATFORMVERSIONINFO']._serialized_end = 2608
    _globals['_ATTACHEDCLUSTERERROR']._serialized_start = 2610
    _globals['_ATTACHEDCLUSTERERROR']._serialized_end = 2649
    _globals['_ATTACHEDPROXYCONFIG']._serialized_start = 2651
    _globals['_ATTACHEDPROXYCONFIG']._serialized_end = 2748
    _globals['_KUBERNETESSECRET']._serialized_start = 2750
    _globals['_KUBERNETESSECRET']._serialized_end = 2801