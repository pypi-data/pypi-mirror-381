"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/developerconnect/v1/insights_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.developerconnect.v1 import developer_connect_pb2 as google_dot_cloud_dot_developerconnect_dot_v1_dot_developer__connect__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/developerconnect/v1/insights_config.proto\x12 google.cloud.developerconnect.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a8google/cloud/developerconnect/v1/developer_connect.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xfc\x07\n\x0eInsightsConfig\x12"\n\x13app_hub_application\x18\x04 \x01(\tB\x03\xe0A\x01H\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12M\n\x0fruntime_configs\x18\x05 \x03(\x0b2/.google.cloud.developerconnect.v1.RuntimeConfigB\x03\xe0A\x03\x12O\n\x10artifact_configs\x18\x06 \x03(\x0b20.google.cloud.developerconnect.v1.ArtifactConfigB\x03\xe0A\x01\x12J\n\x05state\x18\x07 \x01(\x0e26.google.cloud.developerconnect.v1.InsightsConfig.StateB\x03\xe0A\x01\x12[\n\x0bannotations\x18\x08 \x03(\x0b2A.google.cloud.developerconnect.v1.InsightsConfig.AnnotationsEntryB\x03\xe0A\x01\x12Q\n\x06labels\x18\t \x03(\x0b2<.google.cloud.developerconnect.v1.InsightsConfig.LabelsEntryB\x03\xe0A\x01\x12\x18\n\x0breconciling\x18\n \x01(\x08B\x03\xe0A\x03\x12\'\n\x06errors\x18\x0b \x03(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x1a2\n\x10AnnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"D\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x05\x12\x0c\n\x08COMPLETE\x10\x03\x12\t\n\x05ERROR\x10\x04:\xa3\x01\xeaA\x9f\x01\n.developerconnect.googleapis.com/InsightsConfig\x12Iprojects/{project}/locations/{location}/insightsConfigs/{insights_config}*\x0finsightsConfigs2\x0einsightsConfigR\x01\x01B\x19\n\x17insights_config_context"\xe3\x02\n\rRuntimeConfig\x12J\n\x0cgke_workload\x18\x03 \x01(\x0b2-.google.cloud.developerconnect.v1.GKEWorkloadB\x03\xe0A\x03H\x00\x12Q\n\x10app_hub_workload\x18\x04 \x01(\x0b20.google.cloud.developerconnect.v1.AppHubWorkloadB\x03\xe0A\x03H\x01\x12\x13\n\x03uri\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12I\n\x05state\x18\x02 \x01(\x0e25.google.cloud.developerconnect.v1.RuntimeConfig.StateB\x03\xe0A\x03"8\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06LINKED\x10\x01\x12\x0c\n\x08UNLINKED\x10\x02B\t\n\x07runtimeB\x0e\n\x0cderived_from"?\n\x0bGKEWorkload\x12\x17\n\x07cluster\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12\x17\n\ndeployment\x18\x02 \x01(\tB\x03\xe0A\x03"a\n\x0eAppHubWorkload\x12\x1b\n\x08workload\x18\x01 \x01(\tB\t\xe0A\x02\xe0A\x05\xe0A\x03\x12\x18\n\x0bcriticality\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0benvironment\x18\x03 \x01(\tB\x03\xe0A\x03"\x9c\x02\n\x0eArtifactConfig\x12a\n\x18google_artifact_registry\x18\x02 \x01(\x0b28.google.cloud.developerconnect.v1.GoogleArtifactRegistryB\x03\xe0A\x01H\x00\x12a\n\x18google_artifact_analysis\x18\x03 \x01(\x0b28.google.cloud.developerconnect.v1.GoogleArtifactAnalysisB\x03\xe0A\x01H\x01\x12\x13\n\x03uri\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x05B\x12\n\x10artifact_storageB\x1b\n\x19artifact_metadata_storage"1\n\x16GoogleArtifactAnalysis\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02"\\\n\x16GoogleArtifactRegistry\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12)\n\x19artifact_registry_package\x18\x02 \x01(\tB\x06\xe0A\x02\xe0A\x05"\xf2\x01\n\x1bCreateInsightsConfigRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\x12.developerconnect.googleapis.com/InsightsConfig\x12\x1f\n\x12insights_config_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12N\n\x0finsights_config\x18\x03 \x01(\x0b20.google.cloud.developerconnect.v1.InsightsConfigB\x03\xe0A\x02\x12\x1a\n\rvalidate_only\x18\x04 \x01(\x08B\x03\xe0A\x01"`\n\x18GetInsightsConfigRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.developerconnect.googleapis.com/InsightsConfig"\xc1\x01\n\x1aListInsightsConfigsRequest\x12F\n\x06parent\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\x12.developerconnect.googleapis.com/InsightsConfig\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x97\x01\n\x1bListInsightsConfigsResponse\x12J\n\x10insights_configs\x18\x01 \x03(\x0b20.google.cloud.developerconnect.v1.InsightsConfig\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\xb3\x01\n\x1bDeleteInsightsConfigRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.developerconnect.googleapis.com/InsightsConfig\x12\x1f\n\nrequest_id\x18\x02 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12\x1a\n\rvalidate_only\x18\x03 \x01(\x08B\x03\xe0A\x01\x12\x11\n\x04etag\x18\x04 \x01(\tB\x03\xe0A\x01"\xc6\x01\n\x1bUpdateInsightsConfigRequest\x12N\n\x0finsights_config\x18\x02 \x01(\x0b20.google.cloud.developerconnect.v1.InsightsConfigB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x03 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12\x1a\n\rallow_missing\x18\x04 \x01(\x08B\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x05 \x01(\x08B\x03\xe0A\x012\xef\n\n\x15InsightsConfigService\x12\xd8\x01\n\x13ListInsightsConfigs\x12<.google.cloud.developerconnect.v1.ListInsightsConfigsRequest\x1a=.google.cloud.developerconnect.v1.ListInsightsConfigsResponse"D\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1/{parent=projects/*/locations/*}/insightsConfigs\x12\xb6\x02\n\x14CreateInsightsConfig\x12=.google.cloud.developerconnect.v1.CreateInsightsConfigRequest\x1a\x1d.google.longrunning.Operation"\xbf\x01\xcaAD\n\x0eInsightsConfig\x122google.cloud.developerconnect.v1.OperationMetadata\xdaA)parent,insights_config,insights_config_id\x82\xd3\xe4\x93\x02F"3/v1/{parent=projects/*/locations/*}/insightsConfigs:\x0finsights_config\x12\xc5\x01\n\x11GetInsightsConfig\x12:.google.cloud.developerconnect.v1.GetInsightsConfigRequest\x1a0.google.cloud.developerconnect.v1.InsightsConfig"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1/{name=projects/*/locations/*/insightsConfigs/*}\x12\x9a\x02\n\x14UpdateInsightsConfig\x12=.google.cloud.developerconnect.v1.UpdateInsightsConfigRequest\x1a\x1d.google.longrunning.Operation"\xa3\x01\xcaAD\n\x0eInsightsConfig\x122google.cloud.developerconnect.v1.OperationMetadata\x82\xd3\xe4\x93\x02V2C/v1/{insights_config.name=projects/*/locations/*/insightsConfigs/*}:\x0finsights_config\x12\x87\x02\n\x14DeleteInsightsConfig\x12=.google.cloud.developerconnect.v1.DeleteInsightsConfigRequest\x1a\x1d.google.longrunning.Operation"\x90\x01\xcaAK\n\x15google.protobuf.Empty\x122google.cloud.developerconnect.v1.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1/{name=projects/*/locations/*/insightsConfigs/*}\x1aS\xcaA\x1fdeveloperconnect.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd5\x01\n$com.google.cloud.developerconnect.v1B\x13InsightsConfigProtoP\x01ZPcloud.google.com/go/developerconnect/apiv1/developerconnectpb;developerconnectpb\xaa\x02 Google.Cloud.DeveloperConnect.V1\xca\x02 Google\\Cloud\\DeveloperConnect\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.developerconnect.v1.insights_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.developerconnect.v1B\x13InsightsConfigProtoP\x01ZPcloud.google.com/go/developerconnect/apiv1/developerconnectpb;developerconnectpb\xaa\x02 Google.Cloud.DeveloperConnect.V1\xca\x02 Google\\Cloud\\DeveloperConnect\\V1'
    _globals['_INSIGHTSCONFIG_ANNOTATIONSENTRY']._loaded_options = None
    _globals['_INSIGHTSCONFIG_ANNOTATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_INSIGHTSCONFIG_LABELSENTRY']._loaded_options = None
    _globals['_INSIGHTSCONFIG_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_INSIGHTSCONFIG'].fields_by_name['app_hub_application']._loaded_options = None
    _globals['_INSIGHTSCONFIG'].fields_by_name['app_hub_application']._serialized_options = b'\xe0A\x01'
    _globals['_INSIGHTSCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_INSIGHTSCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_INSIGHTSCONFIG'].fields_by_name['create_time']._loaded_options = None
    _globals['_INSIGHTSCONFIG'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSIGHTSCONFIG'].fields_by_name['update_time']._loaded_options = None
    _globals['_INSIGHTSCONFIG'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSIGHTSCONFIG'].fields_by_name['runtime_configs']._loaded_options = None
    _globals['_INSIGHTSCONFIG'].fields_by_name['runtime_configs']._serialized_options = b'\xe0A\x03'
    _globals['_INSIGHTSCONFIG'].fields_by_name['artifact_configs']._loaded_options = None
    _globals['_INSIGHTSCONFIG'].fields_by_name['artifact_configs']._serialized_options = b'\xe0A\x01'
    _globals['_INSIGHTSCONFIG'].fields_by_name['state']._loaded_options = None
    _globals['_INSIGHTSCONFIG'].fields_by_name['state']._serialized_options = b'\xe0A\x01'
    _globals['_INSIGHTSCONFIG'].fields_by_name['annotations']._loaded_options = None
    _globals['_INSIGHTSCONFIG'].fields_by_name['annotations']._serialized_options = b'\xe0A\x01'
    _globals['_INSIGHTSCONFIG'].fields_by_name['labels']._loaded_options = None
    _globals['_INSIGHTSCONFIG'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_INSIGHTSCONFIG'].fields_by_name['reconciling']._loaded_options = None
    _globals['_INSIGHTSCONFIG'].fields_by_name['reconciling']._serialized_options = b'\xe0A\x03'
    _globals['_INSIGHTSCONFIG'].fields_by_name['errors']._loaded_options = None
    _globals['_INSIGHTSCONFIG'].fields_by_name['errors']._serialized_options = b'\xe0A\x03'
    _globals['_INSIGHTSCONFIG']._loaded_options = None
    _globals['_INSIGHTSCONFIG']._serialized_options = b'\xeaA\x9f\x01\n.developerconnect.googleapis.com/InsightsConfig\x12Iprojects/{project}/locations/{location}/insightsConfigs/{insights_config}*\x0finsightsConfigs2\x0einsightsConfigR\x01\x01'
    _globals['_RUNTIMECONFIG'].fields_by_name['gke_workload']._loaded_options = None
    _globals['_RUNTIMECONFIG'].fields_by_name['gke_workload']._serialized_options = b'\xe0A\x03'
    _globals['_RUNTIMECONFIG'].fields_by_name['app_hub_workload']._loaded_options = None
    _globals['_RUNTIMECONFIG'].fields_by_name['app_hub_workload']._serialized_options = b'\xe0A\x03'
    _globals['_RUNTIMECONFIG'].fields_by_name['uri']._loaded_options = None
    _globals['_RUNTIMECONFIG'].fields_by_name['uri']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_RUNTIMECONFIG'].fields_by_name['state']._loaded_options = None
    _globals['_RUNTIMECONFIG'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_GKEWORKLOAD'].fields_by_name['cluster']._loaded_options = None
    _globals['_GKEWORKLOAD'].fields_by_name['cluster']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_GKEWORKLOAD'].fields_by_name['deployment']._loaded_options = None
    _globals['_GKEWORKLOAD'].fields_by_name['deployment']._serialized_options = b'\xe0A\x03'
    _globals['_APPHUBWORKLOAD'].fields_by_name['workload']._loaded_options = None
    _globals['_APPHUBWORKLOAD'].fields_by_name['workload']._serialized_options = b'\xe0A\x02\xe0A\x05\xe0A\x03'
    _globals['_APPHUBWORKLOAD'].fields_by_name['criticality']._loaded_options = None
    _globals['_APPHUBWORKLOAD'].fields_by_name['criticality']._serialized_options = b'\xe0A\x03'
    _globals['_APPHUBWORKLOAD'].fields_by_name['environment']._loaded_options = None
    _globals['_APPHUBWORKLOAD'].fields_by_name['environment']._serialized_options = b'\xe0A\x03'
    _globals['_ARTIFACTCONFIG'].fields_by_name['google_artifact_registry']._loaded_options = None
    _globals['_ARTIFACTCONFIG'].fields_by_name['google_artifact_registry']._serialized_options = b'\xe0A\x01'
    _globals['_ARTIFACTCONFIG'].fields_by_name['google_artifact_analysis']._loaded_options = None
    _globals['_ARTIFACTCONFIG'].fields_by_name['google_artifact_analysis']._serialized_options = b'\xe0A\x01'
    _globals['_ARTIFACTCONFIG'].fields_by_name['uri']._loaded_options = None
    _globals['_ARTIFACTCONFIG'].fields_by_name['uri']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_GOOGLEARTIFACTANALYSIS'].fields_by_name['project_id']._loaded_options = None
    _globals['_GOOGLEARTIFACTANALYSIS'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_GOOGLEARTIFACTREGISTRY'].fields_by_name['project_id']._loaded_options = None
    _globals['_GOOGLEARTIFACTREGISTRY'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_GOOGLEARTIFACTREGISTRY'].fields_by_name['artifact_registry_package']._loaded_options = None
    _globals['_GOOGLEARTIFACTREGISTRY'].fields_by_name['artifact_registry_package']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_CREATEINSIGHTSCONFIGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEINSIGHTSCONFIGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\x12.developerconnect.googleapis.com/InsightsConfig'
    _globals['_CREATEINSIGHTSCONFIGREQUEST'].fields_by_name['insights_config_id']._loaded_options = None
    _globals['_CREATEINSIGHTSCONFIGREQUEST'].fields_by_name['insights_config_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEINSIGHTSCONFIGREQUEST'].fields_by_name['insights_config']._loaded_options = None
    _globals['_CREATEINSIGHTSCONFIGREQUEST'].fields_by_name['insights_config']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEINSIGHTSCONFIGREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_CREATEINSIGHTSCONFIGREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_GETINSIGHTSCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINSIGHTSCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.developerconnect.googleapis.com/InsightsConfig'
    _globals['_LISTINSIGHTSCONFIGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINSIGHTSCONFIGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA0\x12.developerconnect.googleapis.com/InsightsConfig'
    _globals['_LISTINSIGHTSCONFIGSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTINSIGHTSCONFIGSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSIGHTSCONFIGSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTINSIGHTSCONFIGSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSIGHTSCONFIGSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTINSIGHTSCONFIGSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSIGHTSCONFIGSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTINSIGHTSCONFIGSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEINSIGHTSCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEINSIGHTSCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.developerconnect.googleapis.com/InsightsConfig'
    _globals['_DELETEINSIGHTSCONFIGREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEINSIGHTSCONFIGREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_DELETEINSIGHTSCONFIGREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_DELETEINSIGHTSCONFIGREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEINSIGHTSCONFIGREQUEST'].fields_by_name['etag']._loaded_options = None
    _globals['_DELETEINSIGHTSCONFIGREQUEST'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEINSIGHTSCONFIGREQUEST'].fields_by_name['insights_config']._loaded_options = None
    _globals['_UPDATEINSIGHTSCONFIGREQUEST'].fields_by_name['insights_config']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEINSIGHTSCONFIGREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEINSIGHTSCONFIGREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_UPDATEINSIGHTSCONFIGREQUEST'].fields_by_name['allow_missing']._loaded_options = None
    _globals['_UPDATEINSIGHTSCONFIGREQUEST'].fields_by_name['allow_missing']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEINSIGHTSCONFIGREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_UPDATEINSIGHTSCONFIGREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_INSIGHTSCONFIGSERVICE']._loaded_options = None
    _globals['_INSIGHTSCONFIGSERVICE']._serialized_options = b'\xcaA\x1fdeveloperconnect.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_INSIGHTSCONFIGSERVICE'].methods_by_name['ListInsightsConfigs']._loaded_options = None
    _globals['_INSIGHTSCONFIGSERVICE'].methods_by_name['ListInsightsConfigs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1/{parent=projects/*/locations/*}/insightsConfigs'
    _globals['_INSIGHTSCONFIGSERVICE'].methods_by_name['CreateInsightsConfig']._loaded_options = None
    _globals['_INSIGHTSCONFIGSERVICE'].methods_by_name['CreateInsightsConfig']._serialized_options = b'\xcaAD\n\x0eInsightsConfig\x122google.cloud.developerconnect.v1.OperationMetadata\xdaA)parent,insights_config,insights_config_id\x82\xd3\xe4\x93\x02F"3/v1/{parent=projects/*/locations/*}/insightsConfigs:\x0finsights_config'
    _globals['_INSIGHTSCONFIGSERVICE'].methods_by_name['GetInsightsConfig']._loaded_options = None
    _globals['_INSIGHTSCONFIGSERVICE'].methods_by_name['GetInsightsConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1/{name=projects/*/locations/*/insightsConfigs/*}'
    _globals['_INSIGHTSCONFIGSERVICE'].methods_by_name['UpdateInsightsConfig']._loaded_options = None
    _globals['_INSIGHTSCONFIGSERVICE'].methods_by_name['UpdateInsightsConfig']._serialized_options = b'\xcaAD\n\x0eInsightsConfig\x122google.cloud.developerconnect.v1.OperationMetadata\x82\xd3\xe4\x93\x02V2C/v1/{insights_config.name=projects/*/locations/*/insightsConfigs/*}:\x0finsights_config'
    _globals['_INSIGHTSCONFIGSERVICE'].methods_by_name['DeleteInsightsConfig']._loaded_options = None
    _globals['_INSIGHTSCONFIGSERVICE'].methods_by_name['DeleteInsightsConfig']._serialized_options = b'\xcaAK\n\x15google.protobuf.Empty\x122google.cloud.developerconnect.v1.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1/{name=projects/*/locations/*/insightsConfigs/*}'
    _globals['_INSIGHTSCONFIG']._serialized_start = 419
    _globals['_INSIGHTSCONFIG']._serialized_end = 1439
    _globals['_INSIGHTSCONFIG_ANNOTATIONSENTRY']._serialized_start = 1079
    _globals['_INSIGHTSCONFIG_ANNOTATIONSENTRY']._serialized_end = 1129
    _globals['_INSIGHTSCONFIG_LABELSENTRY']._serialized_start = 1131
    _globals['_INSIGHTSCONFIG_LABELSENTRY']._serialized_end = 1176
    _globals['_INSIGHTSCONFIG_STATE']._serialized_start = 1178
    _globals['_INSIGHTSCONFIG_STATE']._serialized_end = 1246
    _globals['_RUNTIMECONFIG']._serialized_start = 1442
    _globals['_RUNTIMECONFIG']._serialized_end = 1797
    _globals['_RUNTIMECONFIG_STATE']._serialized_start = 1714
    _globals['_RUNTIMECONFIG_STATE']._serialized_end = 1770
    _globals['_GKEWORKLOAD']._serialized_start = 1799
    _globals['_GKEWORKLOAD']._serialized_end = 1862
    _globals['_APPHUBWORKLOAD']._serialized_start = 1864
    _globals['_APPHUBWORKLOAD']._serialized_end = 1961
    _globals['_ARTIFACTCONFIG']._serialized_start = 1964
    _globals['_ARTIFACTCONFIG']._serialized_end = 2248
    _globals['_GOOGLEARTIFACTANALYSIS']._serialized_start = 2250
    _globals['_GOOGLEARTIFACTANALYSIS']._serialized_end = 2299
    _globals['_GOOGLEARTIFACTREGISTRY']._serialized_start = 2301
    _globals['_GOOGLEARTIFACTREGISTRY']._serialized_end = 2393
    _globals['_CREATEINSIGHTSCONFIGREQUEST']._serialized_start = 2396
    _globals['_CREATEINSIGHTSCONFIGREQUEST']._serialized_end = 2638
    _globals['_GETINSIGHTSCONFIGREQUEST']._serialized_start = 2640
    _globals['_GETINSIGHTSCONFIGREQUEST']._serialized_end = 2736
    _globals['_LISTINSIGHTSCONFIGSREQUEST']._serialized_start = 2739
    _globals['_LISTINSIGHTSCONFIGSREQUEST']._serialized_end = 2932
    _globals['_LISTINSIGHTSCONFIGSRESPONSE']._serialized_start = 2935
    _globals['_LISTINSIGHTSCONFIGSRESPONSE']._serialized_end = 3086
    _globals['_DELETEINSIGHTSCONFIGREQUEST']._serialized_start = 3089
    _globals['_DELETEINSIGHTSCONFIGREQUEST']._serialized_end = 3268
    _globals['_UPDATEINSIGHTSCONFIGREQUEST']._serialized_start = 3271
    _globals['_UPDATEINSIGHTSCONFIGREQUEST']._serialized_end = 3469
    _globals['_INSIGHTSCONFIGSERVICE']._serialized_start = 3472
    _globals['_INSIGHTSCONFIGSERVICE']._serialized_end = 4863