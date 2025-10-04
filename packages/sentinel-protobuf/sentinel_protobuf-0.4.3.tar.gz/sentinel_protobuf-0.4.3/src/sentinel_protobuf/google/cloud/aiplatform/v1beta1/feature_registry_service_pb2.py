"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/feature_registry_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import feature_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_feature__pb2
from .....google.cloud.aiplatform.v1beta1 import feature_group_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_feature__group__pb2
from .....google.cloud.aiplatform.v1beta1 import feature_monitor_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_feature__monitor__pb2
from .....google.cloud.aiplatform.v1beta1 import feature_monitor_job_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_feature__monitor__job__pb2
from .....google.cloud.aiplatform.v1beta1 import featurestore_service_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_featurestore__service__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/aiplatform/v1beta1/feature_registry_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/aiplatform/v1beta1/feature.proto\x1a3google/cloud/aiplatform/v1beta1/feature_group.proto\x1a5google/cloud/aiplatform/v1beta1/feature_monitor.proto\x1a9google/cloud/aiplatform/v1beta1/feature_monitor_job.proto\x1a:google/cloud/aiplatform/v1beta1/featurestore_service.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xc5\x01\n\x19CreateFeatureGroupRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&aiplatform.googleapis.com/FeatureGroup\x12I\n\rfeature_group\x18\x02 \x01(\x0b2-.google.cloud.aiplatform.v1beta1.FeatureGroupB\x03\xe0A\x02\x12\x1d\n\x10feature_group_id\x18\x03 \x01(\tB\x03\xe0A\x02"V\n\x16GetFeatureGroupRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/FeatureGroup"\xa3\x01\n\x18ListFeatureGroupsRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&aiplatform.googleapis.com/FeatureGroup\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"{\n\x19ListFeatureGroupsResponse\x12E\n\x0efeature_groups\x18\x01 \x03(\x0b2-.google.cloud.aiplatform.v1beta1.FeatureGroup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x97\x01\n\x19UpdateFeatureGroupRequest\x12I\n\rfeature_group\x18\x01 \x01(\x0b2-.google.cloud.aiplatform.v1beta1.FeatureGroupB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"h\n\x19DeleteFeatureGroupRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/FeatureGroup\x12\r\n\x05force\x18\x02 \x01(\x08"\xcf\x01\n\x1bCreateFeatureMonitorRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(aiplatform.googleapis.com/FeatureMonitor\x12M\n\x0ffeature_monitor\x18\x02 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.FeatureMonitorB\x03\xe0A\x02\x12\x1f\n\x12feature_monitor_id\x18\x03 \x01(\tB\x03\xe0A\x02"Z\n\x18GetFeatureMonitorRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/FeatureMonitor"\xbb\x01\n\x1aListFeatureMonitorsRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(aiplatform.googleapis.com/FeatureMonitor\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\xa2\x01\n\x1bUpdateFeatureMonitorRequest\x12M\n\x0ffeature_monitor\x18\x01 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.FeatureMonitorB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"]\n\x1bDeleteFeatureMonitorRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/FeatureMonitor"\x81\x01\n\x1bListFeatureMonitorsResponse\x12I\n\x10feature_monitors\x18\x01 \x03(\x0b2/.google.cloud.aiplatform.v1beta1.FeatureMonitor\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"z\n#CreateFeatureGroupOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"z\n#UpdateFeatureGroupOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"}\n&CreateRegistryFeatureOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"u\n\x1eUpdateFeatureOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"|\n%CreateFeatureMonitorOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"|\n%UpdateFeatureMonitorOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"\xe3\x01\n\x1eCreateFeatureMonitorJobRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+aiplatform.googleapis.com/FeatureMonitorJob\x12T\n\x13feature_monitor_job\x18\x02 \x01(\x0b22.google.cloud.aiplatform.v1beta1.FeatureMonitorJobB\x03\xe0A\x02\x12&\n\x16feature_monitor_job_id\x18\x03 \x01(\x03B\x06\xe0A\x01\xe0A\x03"`\n\x1bGetFeatureMonitorJobRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+aiplatform.googleapis.com/FeatureMonitorJob"\xc1\x01\n\x1dListFeatureMonitorJobsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+aiplatform.googleapis.com/FeatureMonitorJob\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x8b\x01\n\x1eListFeatureMonitorJobsResponse\x12P\n\x14feature_monitor_jobs\x18\x01 \x03(\x0b22.google.cloud.aiplatform.v1beta1.FeatureMonitorJob\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xfb&\n\x16FeatureRegistryService\x12\x9d\x02\n\x12CreateFeatureGroup\x12:.google.cloud.aiplatform.v1beta1.CreateFeatureGroupRequest\x1a\x1d.google.longrunning.Operation"\xab\x01\xcaA3\n\x0cFeatureGroup\x12#CreateFeatureGroupOperationMetadata\xdaA%parent,feature_group,feature_group_id\x82\xd3\xe4\x93\x02G"6/v1beta1/{parent=projects/*/locations/*}/featureGroups:\rfeature_group\x12\xc0\x01\n\x0fGetFeatureGroup\x127.google.cloud.aiplatform.v1beta1.GetFeatureGroupRequest\x1a-.google.cloud.aiplatform.v1beta1.FeatureGroup"E\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1beta1/{name=projects/*/locations/*/featureGroups/*}\x12\xd3\x01\n\x11ListFeatureGroups\x129.google.cloud.aiplatform.v1beta1.ListFeatureGroupsRequest\x1a:.google.cloud.aiplatform.v1beta1.ListFeatureGroupsResponse"G\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1beta1/{parent=projects/*/locations/*}/featureGroups\x12\x9f\x02\n\x12UpdateFeatureGroup\x12:.google.cloud.aiplatform.v1beta1.UpdateFeatureGroupRequest\x1a\x1d.google.longrunning.Operation"\xad\x01\xcaA3\n\x0cFeatureGroup\x12#UpdateFeatureGroupOperationMetadata\xdaA\x19feature_group,update_mask\x82\xd3\xe4\x93\x02U2D/v1beta1/{feature_group.name=projects/*/locations/*/featureGroups/*}:\rfeature_group\x12\xef\x01\n\x12DeleteFeatureGroup\x12:.google.cloud.aiplatform.v1beta1.DeleteFeatureGroupRequest\x1a\x1d.google.longrunning.Operation"~\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\nname,force\x82\xd3\xe4\x93\x028*6/v1beta1/{name=projects/*/locations/*/featureGroups/*}\x12\x82\x02\n\rCreateFeature\x125.google.cloud.aiplatform.v1beta1.CreateFeatureRequest\x1a\x1d.google.longrunning.Operation"\x9a\x01\xcaA)\n\x07Feature\x12\x1eCreateFeatureOperationMetadata\xdaA\x19parent,feature,feature_id\x82\xd3\xe4\x93\x02L"A/v1beta1/{parent=projects/*/locations/*/featureGroups/*}/features:\x07feature\x12\xa4\x02\n\x13BatchCreateFeatures\x12;.google.cloud.aiplatform.v1beta1.BatchCreateFeaturesRequest\x1a\x1d.google.longrunning.Operation"\xb0\x01\xcaAC\n\x1bBatchCreateFeaturesResponse\x12$BatchCreateFeaturesOperationMetadata\xdaA\x0fparent,requests\x82\xd3\xe4\x93\x02R"M/v1beta1/{parent=projects/*/locations/*/featureGroups/*}/features:batchCreate:\x01*\x12\xbc\x01\n\nGetFeature\x122.google.cloud.aiplatform.v1beta1.GetFeatureRequest\x1a(.google.cloud.aiplatform.v1beta1.Feature"P\xdaA\x04name\x82\xd3\xe4\x93\x02C\x12A/v1beta1/{name=projects/*/locations/*/featureGroups/*/features/*}\x12\xcf\x01\n\x0cListFeatures\x124.google.cloud.aiplatform.v1beta1.ListFeaturesRequest\x1a5.google.cloud.aiplatform.v1beta1.ListFeaturesResponse"R\xdaA\x06parent\x82\xd3\xe4\x93\x02C\x12A/v1beta1/{parent=projects/*/locations/*/featureGroups/*}/features\x12\x84\x02\n\rUpdateFeature\x125.google.cloud.aiplatform.v1beta1.UpdateFeatureRequest\x1a\x1d.google.longrunning.Operation"\x9c\x01\xcaA)\n\x07Feature\x12\x1eUpdateFeatureOperationMetadata\xdaA\x13feature,update_mask\x82\xd3\xe4\x93\x02T2I/v1beta1/{feature.name=projects/*/locations/*/featureGroups/*/features/*}:\x07feature\x12\xeb\x01\n\rDeleteFeature\x125.google.cloud.aiplatform.v1beta1.DeleteFeatureRequest\x1a\x1d.google.longrunning.Operation"\x83\x01\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02C*A/v1beta1/{name=projects/*/locations/*/featureGroups/*/features/*}\x12\xbd\x02\n\x14CreateFeatureMonitor\x12<.google.cloud.aiplatform.v1beta1.CreateFeatureMonitorRequest\x1a\x1d.google.longrunning.Operation"\xc7\x01\xcaA7\n\x0eFeatureMonitor\x12%CreateFeatureMonitorOperationMetadata\xdaA)parent,feature_monitor,feature_monitor_id\x82\xd3\xe4\x93\x02["H/v1beta1/{parent=projects/*/locations/*/featureGroups/*}/featureMonitors:\x0ffeature_monitor\x12\xd8\x01\n\x11GetFeatureMonitor\x129.google.cloud.aiplatform.v1beta1.GetFeatureMonitorRequest\x1a/.google.cloud.aiplatform.v1beta1.FeatureMonitor"W\xdaA\x04name\x82\xd3\xe4\x93\x02J\x12H/v1beta1/{name=projects/*/locations/*/featureGroups/*/featureMonitors/*}\x12\xeb\x01\n\x13ListFeatureMonitors\x12;.google.cloud.aiplatform.v1beta1.ListFeatureMonitorsRequest\x1a<.google.cloud.aiplatform.v1beta1.ListFeatureMonitorsResponse"Y\xdaA\x06parent\x82\xd3\xe4\x93\x02J\x12H/v1beta1/{parent=projects/*/locations/*/featureGroups/*}/featureMonitors\x12\xbf\x02\n\x14UpdateFeatureMonitor\x12<.google.cloud.aiplatform.v1beta1.UpdateFeatureMonitorRequest\x1a\x1d.google.longrunning.Operation"\xc9\x01\xcaA7\n\x0eFeatureMonitor\x12%UpdateFeatureMonitorOperationMetadata\xdaA\x1bfeature_monitor,update_mask\x82\xd3\xe4\x93\x02k2X/v1beta1/{feature_monitor.name=projects/*/locations/*/featureGroups/*/featureMonitors/*}:\x0ffeature_monitor\x12\x80\x02\n\x14DeleteFeatureMonitor\x12<.google.cloud.aiplatform.v1beta1.DeleteFeatureMonitorRequest\x1a\x1d.google.longrunning.Operation"\x8a\x01\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02J*H/v1beta1/{name=projects/*/locations/*/featureGroups/*/featureMonitors/*}\x12\xbf\x02\n\x17CreateFeatureMonitorJob\x12?.google.cloud.aiplatform.v1beta1.CreateFeatureMonitorJobRequest\x1a2.google.cloud.aiplatform.v1beta1.FeatureMonitorJob"\xae\x01\xdaA1parent,feature_monitor_job,feature_monitor_job_id\x82\xd3\xe4\x93\x02t"]/v1beta1/{parent=projects/*/locations/*/featureGroups/*/featureMonitors/*}/featureMonitorJobs:\x13feature_monitor_job\x12\xf6\x01\n\x14GetFeatureMonitorJob\x12<.google.cloud.aiplatform.v1beta1.GetFeatureMonitorJobRequest\x1a2.google.cloud.aiplatform.v1beta1.FeatureMonitorJob"l\xdaA\x04name\x82\xd3\xe4\x93\x02_\x12]/v1beta1/{name=projects/*/locations/*/featureGroups/*/featureMonitors/*/featureMonitorJobs/*}\x12\x89\x02\n\x16ListFeatureMonitorJobs\x12>.google.cloud.aiplatform.v1beta1.ListFeatureMonitorJobsRequest\x1a?.google.cloud.aiplatform.v1beta1.ListFeatureMonitorJobsResponse"n\xdaA\x06parent\x82\xd3\xe4\x93\x02_\x12]/v1beta1/{parent=projects/*/locations/*/featureGroups/*/featureMonitors/*}/featureMonitorJobs\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf2\x01\n#com.google.cloud.aiplatform.v1beta1B\x1bFeatureRegistryServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.feature_registry_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x1bFeatureRegistryServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CREATEFEATUREGROUPREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEFEATUREGROUPREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&aiplatform.googleapis.com/FeatureGroup'
    _globals['_CREATEFEATUREGROUPREQUEST'].fields_by_name['feature_group']._loaded_options = None
    _globals['_CREATEFEATUREGROUPREQUEST'].fields_by_name['feature_group']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEFEATUREGROUPREQUEST'].fields_by_name['feature_group_id']._loaded_options = None
    _globals['_CREATEFEATUREGROUPREQUEST'].fields_by_name['feature_group_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETFEATUREGROUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFEATUREGROUPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/FeatureGroup'
    _globals['_LISTFEATUREGROUPSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFEATUREGROUPSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&aiplatform.googleapis.com/FeatureGroup'
    _globals['_UPDATEFEATUREGROUPREQUEST'].fields_by_name['feature_group']._loaded_options = None
    _globals['_UPDATEFEATUREGROUPREQUEST'].fields_by_name['feature_group']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEFEATUREGROUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEFEATUREGROUPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/FeatureGroup'
    _globals['_CREATEFEATUREMONITORREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEFEATUREMONITORREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(aiplatform.googleapis.com/FeatureMonitor'
    _globals['_CREATEFEATUREMONITORREQUEST'].fields_by_name['feature_monitor']._loaded_options = None
    _globals['_CREATEFEATUREMONITORREQUEST'].fields_by_name['feature_monitor']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEFEATUREMONITORREQUEST'].fields_by_name['feature_monitor_id']._loaded_options = None
    _globals['_CREATEFEATUREMONITORREQUEST'].fields_by_name['feature_monitor_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETFEATUREMONITORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFEATUREMONITORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/FeatureMonitor'
    _globals['_LISTFEATUREMONITORSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFEATUREMONITORSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(aiplatform.googleapis.com/FeatureMonitor'
    _globals['_LISTFEATUREMONITORSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTFEATUREMONITORSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTFEATUREMONITORSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTFEATUREMONITORSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTFEATUREMONITORSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTFEATUREMONITORSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTFEATUREMONITORSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTFEATUREMONITORSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEFEATUREMONITORREQUEST'].fields_by_name['feature_monitor']._loaded_options = None
    _globals['_UPDATEFEATUREMONITORREQUEST'].fields_by_name['feature_monitor']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEFEATUREMONITORREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEFEATUREMONITORREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEFEATUREMONITORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEFEATUREMONITORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/FeatureMonitor'
    _globals['_CREATEFEATUREMONITORJOBREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEFEATUREMONITORJOBREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+aiplatform.googleapis.com/FeatureMonitorJob'
    _globals['_CREATEFEATUREMONITORJOBREQUEST'].fields_by_name['feature_monitor_job']._loaded_options = None
    _globals['_CREATEFEATUREMONITORJOBREQUEST'].fields_by_name['feature_monitor_job']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEFEATUREMONITORJOBREQUEST'].fields_by_name['feature_monitor_job_id']._loaded_options = None
    _globals['_CREATEFEATUREMONITORJOBREQUEST'].fields_by_name['feature_monitor_job_id']._serialized_options = b'\xe0A\x01\xe0A\x03'
    _globals['_GETFEATUREMONITORJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFEATUREMONITORJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+aiplatform.googleapis.com/FeatureMonitorJob'
    _globals['_LISTFEATUREMONITORJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFEATUREMONITORJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+aiplatform.googleapis.com/FeatureMonitorJob'
    _globals['_LISTFEATUREMONITORJOBSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTFEATUREMONITORJOBSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTFEATUREMONITORJOBSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTFEATUREMONITORJOBSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTFEATUREMONITORJOBSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTFEATUREMONITORJOBSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTFEATUREMONITORJOBSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTFEATUREMONITORJOBSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREREGISTRYSERVICE']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['CreateFeatureGroup']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['CreateFeatureGroup']._serialized_options = b'\xcaA3\n\x0cFeatureGroup\x12#CreateFeatureGroupOperationMetadata\xdaA%parent,feature_group,feature_group_id\x82\xd3\xe4\x93\x02G"6/v1beta1/{parent=projects/*/locations/*}/featureGroups:\rfeature_group'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['GetFeatureGroup']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['GetFeatureGroup']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1beta1/{name=projects/*/locations/*/featureGroups/*}'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['ListFeatureGroups']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['ListFeatureGroups']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1beta1/{parent=projects/*/locations/*}/featureGroups'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['UpdateFeatureGroup']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['UpdateFeatureGroup']._serialized_options = b'\xcaA3\n\x0cFeatureGroup\x12#UpdateFeatureGroupOperationMetadata\xdaA\x19feature_group,update_mask\x82\xd3\xe4\x93\x02U2D/v1beta1/{feature_group.name=projects/*/locations/*/featureGroups/*}:\rfeature_group'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['DeleteFeatureGroup']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['DeleteFeatureGroup']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\nname,force\x82\xd3\xe4\x93\x028*6/v1beta1/{name=projects/*/locations/*/featureGroups/*}'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['CreateFeature']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['CreateFeature']._serialized_options = b'\xcaA)\n\x07Feature\x12\x1eCreateFeatureOperationMetadata\xdaA\x19parent,feature,feature_id\x82\xd3\xe4\x93\x02L"A/v1beta1/{parent=projects/*/locations/*/featureGroups/*}/features:\x07feature'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['BatchCreateFeatures']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['BatchCreateFeatures']._serialized_options = b'\xcaAC\n\x1bBatchCreateFeaturesResponse\x12$BatchCreateFeaturesOperationMetadata\xdaA\x0fparent,requests\x82\xd3\xe4\x93\x02R"M/v1beta1/{parent=projects/*/locations/*/featureGroups/*}/features:batchCreate:\x01*'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['GetFeature']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['GetFeature']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02C\x12A/v1beta1/{name=projects/*/locations/*/featureGroups/*/features/*}'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['ListFeatures']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['ListFeatures']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02C\x12A/v1beta1/{parent=projects/*/locations/*/featureGroups/*}/features'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['UpdateFeature']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['UpdateFeature']._serialized_options = b'\xcaA)\n\x07Feature\x12\x1eUpdateFeatureOperationMetadata\xdaA\x13feature,update_mask\x82\xd3\xe4\x93\x02T2I/v1beta1/{feature.name=projects/*/locations/*/featureGroups/*/features/*}:\x07feature'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['DeleteFeature']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['DeleteFeature']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02C*A/v1beta1/{name=projects/*/locations/*/featureGroups/*/features/*}'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['CreateFeatureMonitor']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['CreateFeatureMonitor']._serialized_options = b'\xcaA7\n\x0eFeatureMonitor\x12%CreateFeatureMonitorOperationMetadata\xdaA)parent,feature_monitor,feature_monitor_id\x82\xd3\xe4\x93\x02["H/v1beta1/{parent=projects/*/locations/*/featureGroups/*}/featureMonitors:\x0ffeature_monitor'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['GetFeatureMonitor']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['GetFeatureMonitor']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02J\x12H/v1beta1/{name=projects/*/locations/*/featureGroups/*/featureMonitors/*}'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['ListFeatureMonitors']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['ListFeatureMonitors']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02J\x12H/v1beta1/{parent=projects/*/locations/*/featureGroups/*}/featureMonitors'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['UpdateFeatureMonitor']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['UpdateFeatureMonitor']._serialized_options = b'\xcaA7\n\x0eFeatureMonitor\x12%UpdateFeatureMonitorOperationMetadata\xdaA\x1bfeature_monitor,update_mask\x82\xd3\xe4\x93\x02k2X/v1beta1/{feature_monitor.name=projects/*/locations/*/featureGroups/*/featureMonitors/*}:\x0ffeature_monitor'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['DeleteFeatureMonitor']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['DeleteFeatureMonitor']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02J*H/v1beta1/{name=projects/*/locations/*/featureGroups/*/featureMonitors/*}'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['CreateFeatureMonitorJob']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['CreateFeatureMonitorJob']._serialized_options = b'\xdaA1parent,feature_monitor_job,feature_monitor_job_id\x82\xd3\xe4\x93\x02t"]/v1beta1/{parent=projects/*/locations/*/featureGroups/*/featureMonitors/*}/featureMonitorJobs:\x13feature_monitor_job'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['GetFeatureMonitorJob']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['GetFeatureMonitorJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02_\x12]/v1beta1/{name=projects/*/locations/*/featureGroups/*/featureMonitors/*/featureMonitorJobs/*}'
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['ListFeatureMonitorJobs']._loaded_options = None
    _globals['_FEATUREREGISTRYSERVICE'].methods_by_name['ListFeatureMonitorJobs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02_\x12]/v1beta1/{parent=projects/*/locations/*/featureGroups/*/featureMonitors/*}/featureMonitorJobs'
    _globals['_CREATEFEATUREGROUPREQUEST']._serialized_start = 638
    _globals['_CREATEFEATUREGROUPREQUEST']._serialized_end = 835
    _globals['_GETFEATUREGROUPREQUEST']._serialized_start = 837
    _globals['_GETFEATUREGROUPREQUEST']._serialized_end = 923
    _globals['_LISTFEATUREGROUPSREQUEST']._serialized_start = 926
    _globals['_LISTFEATUREGROUPSREQUEST']._serialized_end = 1089
    _globals['_LISTFEATUREGROUPSRESPONSE']._serialized_start = 1091
    _globals['_LISTFEATUREGROUPSRESPONSE']._serialized_end = 1214
    _globals['_UPDATEFEATUREGROUPREQUEST']._serialized_start = 1217
    _globals['_UPDATEFEATUREGROUPREQUEST']._serialized_end = 1368
    _globals['_DELETEFEATUREGROUPREQUEST']._serialized_start = 1370
    _globals['_DELETEFEATUREGROUPREQUEST']._serialized_end = 1474
    _globals['_CREATEFEATUREMONITORREQUEST']._serialized_start = 1477
    _globals['_CREATEFEATUREMONITORREQUEST']._serialized_end = 1684
    _globals['_GETFEATUREMONITORREQUEST']._serialized_start = 1686
    _globals['_GETFEATUREMONITORREQUEST']._serialized_end = 1776
    _globals['_LISTFEATUREMONITORSREQUEST']._serialized_start = 1779
    _globals['_LISTFEATUREMONITORSREQUEST']._serialized_end = 1966
    _globals['_UPDATEFEATUREMONITORREQUEST']._serialized_start = 1969
    _globals['_UPDATEFEATUREMONITORREQUEST']._serialized_end = 2131
    _globals['_DELETEFEATUREMONITORREQUEST']._serialized_start = 2133
    _globals['_DELETEFEATUREMONITORREQUEST']._serialized_end = 2226
    _globals['_LISTFEATUREMONITORSRESPONSE']._serialized_start = 2229
    _globals['_LISTFEATUREMONITORSRESPONSE']._serialized_end = 2358
    _globals['_CREATEFEATUREGROUPOPERATIONMETADATA']._serialized_start = 2360
    _globals['_CREATEFEATUREGROUPOPERATIONMETADATA']._serialized_end = 2482
    _globals['_UPDATEFEATUREGROUPOPERATIONMETADATA']._serialized_start = 2484
    _globals['_UPDATEFEATUREGROUPOPERATIONMETADATA']._serialized_end = 2606
    _globals['_CREATEREGISTRYFEATUREOPERATIONMETADATA']._serialized_start = 2608
    _globals['_CREATEREGISTRYFEATUREOPERATIONMETADATA']._serialized_end = 2733
    _globals['_UPDATEFEATUREOPERATIONMETADATA']._serialized_start = 2735
    _globals['_UPDATEFEATUREOPERATIONMETADATA']._serialized_end = 2852
    _globals['_CREATEFEATUREMONITOROPERATIONMETADATA']._serialized_start = 2854
    _globals['_CREATEFEATUREMONITOROPERATIONMETADATA']._serialized_end = 2978
    _globals['_UPDATEFEATUREMONITOROPERATIONMETADATA']._serialized_start = 2980
    _globals['_UPDATEFEATUREMONITOROPERATIONMETADATA']._serialized_end = 3104
    _globals['_CREATEFEATUREMONITORJOBREQUEST']._serialized_start = 3107
    _globals['_CREATEFEATUREMONITORJOBREQUEST']._serialized_end = 3334
    _globals['_GETFEATUREMONITORJOBREQUEST']._serialized_start = 3336
    _globals['_GETFEATUREMONITORJOBREQUEST']._serialized_end = 3432
    _globals['_LISTFEATUREMONITORJOBSREQUEST']._serialized_start = 3435
    _globals['_LISTFEATUREMONITORJOBSREQUEST']._serialized_end = 3628
    _globals['_LISTFEATUREMONITORJOBSRESPONSE']._serialized_start = 3631
    _globals['_LISTFEATUREMONITORJOBSRESPONSE']._serialized_end = 3770
    _globals['_FEATUREREGISTRYSERVICE']._serialized_start = 3773
    _globals['_FEATUREREGISTRYSERVICE']._serialized_end = 8760