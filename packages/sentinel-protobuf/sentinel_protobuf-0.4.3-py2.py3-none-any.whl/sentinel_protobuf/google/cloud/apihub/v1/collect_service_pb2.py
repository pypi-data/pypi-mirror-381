"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/apihub/v1/collect_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.apihub.v1 import common_fields_pb2 as google_dot_cloud_dot_apihub_dot_v1_dot_common__fields__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/apihub/v1/collect_service.proto\x12\x16google.cloud.apihub.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/cloud/apihub/v1/common_fields.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb1\x02\n\x15CollectApiDataRequest\x12;\n\x08location\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12D\n\x0fcollection_type\x18\x02 \x01(\x0e2&.google.cloud.apihub.v1.CollectionTypeB\x03\xe0A\x02\x12E\n\x0fplugin_instance\x18\x03 \x01(\tB,\xe0A\x02\xfaA&\n$apihub.googleapis.com/PluginInstance\x12\x16\n\taction_id\x18\x04 \x01(\tB\x03\xe0A\x02\x126\n\x08api_data\x18\x05 \x01(\x0b2\x1f.google.cloud.apihub.v1.ApiDataB\x03\xe0A\x02"\\\n\x07ApiData\x12I\n\x11api_metadata_list\x18\x01 \x01(\x0b2\'.google.cloud.apihub.v1.ApiMetadataListB\x03\xe0A\x01H\x00B\x06\n\x04Data"Q\n\x0fApiMetadataList\x12>\n\x0capi_metadata\x18\x01 \x03(\x0b2#.google.cloud.apihub.v1.APIMetadataB\x03\xe0A\x02"\x94\x02\n\x0bAPIMetadata\x12-\n\x03api\x18\x01 \x01(\x0b2\x1b.google.cloud.apihub.v1.ApiB\x03\xe0A\x02\x12>\n\x08versions\x18\x02 \x03(\x0b2\'.google.cloud.apihub.v1.VersionMetadataB\x03\xe0A\x01\x12\x18\n\x0boriginal_id\x18\x03 \x01(\tB\x03\xe0A\x01\x12=\n\x14original_create_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x12=\n\x14original_update_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02"\xe0\x02\n\x0fVersionMetadata\x125\n\x07version\x18\x01 \x01(\x0b2\x1f.google.cloud.apihub.v1.VersionB\x03\xe0A\x02\x128\n\x05specs\x18\x02 \x03(\x0b2$.google.cloud.apihub.v1.SpecMetadataB\x03\xe0A\x01\x12D\n\x0bdeployments\x18\x04 \x03(\x0b2*.google.cloud.apihub.v1.DeploymentMetadataB\x03\xe0A\x01\x12\x18\n\x0boriginal_id\x18\x05 \x01(\tB\x03\xe0A\x01\x12=\n\x14original_create_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x12=\n\x14original_update_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02"\xd7\x01\n\x0cSpecMetadata\x12/\n\x04spec\x18\x01 \x01(\x0b2\x1c.google.cloud.apihub.v1.SpecB\x03\xe0A\x02\x12\x18\n\x0boriginal_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12=\n\x14original_create_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x12=\n\x14original_update_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02"\xe9\x01\n\x12DeploymentMetadata\x12;\n\ndeployment\x18\x01 \x01(\x0b2".google.cloud.apihub.v1.DeploymentB\x03\xe0A\x02\x12\x18\n\x0boriginal_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12=\n\x14original_create_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x12=\n\x14original_update_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02"\x18\n\x16CollectApiDataResponse*i\n\x0eCollectionType\x12\x1f\n\x1bCOLLECTION_TYPE_UNSPECIFIED\x10\x00\x12\x1a\n\x16COLLECTION_TYPE_UPSERT\x10\x01\x12\x1a\n\x16COLLECTION_TYPE_DELETE\x10\x022\xcf\x02\n\rApiHubCollect\x12\xf2\x01\n\x0eCollectApiData\x12-.google.cloud.apihub.v1.CollectApiDataRequest\x1a\x1d.google.longrunning.Operation"\x91\x01\xcaA+\n\x16CollectApiDataResponse\x12\x11OperationMetadata\xdaA!location,collection_type,api_data\x82\xd3\xe4\x93\x029"4/v1/{location=projects/*/locations/*}:collectApiData:\x01*\x1aI\xcaA\x15apihub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xb5\x01\n\x1acom.google.cloud.apihub.v1B\x13CollectServiceProtoP\x01Z2cloud.google.com/go/apihub/apiv1/apihubpb;apihubpb\xaa\x02\x16Google.Cloud.ApiHub.V1\xca\x02\x16Google\\Cloud\\ApiHub\\V1\xea\x02\x19Google::Cloud::ApiHub::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.apihub.v1.collect_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.apihub.v1B\x13CollectServiceProtoP\x01Z2cloud.google.com/go/apihub/apiv1/apihubpb;apihubpb\xaa\x02\x16Google.Cloud.ApiHub.V1\xca\x02\x16Google\\Cloud\\ApiHub\\V1\xea\x02\x19Google::Cloud::ApiHub::V1'
    _globals['_COLLECTAPIDATAREQUEST'].fields_by_name['location']._loaded_options = None
    _globals['_COLLECTAPIDATAREQUEST'].fields_by_name['location']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_COLLECTAPIDATAREQUEST'].fields_by_name['collection_type']._loaded_options = None
    _globals['_COLLECTAPIDATAREQUEST'].fields_by_name['collection_type']._serialized_options = b'\xe0A\x02'
    _globals['_COLLECTAPIDATAREQUEST'].fields_by_name['plugin_instance']._loaded_options = None
    _globals['_COLLECTAPIDATAREQUEST'].fields_by_name['plugin_instance']._serialized_options = b'\xe0A\x02\xfaA&\n$apihub.googleapis.com/PluginInstance'
    _globals['_COLLECTAPIDATAREQUEST'].fields_by_name['action_id']._loaded_options = None
    _globals['_COLLECTAPIDATAREQUEST'].fields_by_name['action_id']._serialized_options = b'\xe0A\x02'
    _globals['_COLLECTAPIDATAREQUEST'].fields_by_name['api_data']._loaded_options = None
    _globals['_COLLECTAPIDATAREQUEST'].fields_by_name['api_data']._serialized_options = b'\xe0A\x02'
    _globals['_APIDATA'].fields_by_name['api_metadata_list']._loaded_options = None
    _globals['_APIDATA'].fields_by_name['api_metadata_list']._serialized_options = b'\xe0A\x01'
    _globals['_APIMETADATALIST'].fields_by_name['api_metadata']._loaded_options = None
    _globals['_APIMETADATALIST'].fields_by_name['api_metadata']._serialized_options = b'\xe0A\x02'
    _globals['_APIMETADATA'].fields_by_name['api']._loaded_options = None
    _globals['_APIMETADATA'].fields_by_name['api']._serialized_options = b'\xe0A\x02'
    _globals['_APIMETADATA'].fields_by_name['versions']._loaded_options = None
    _globals['_APIMETADATA'].fields_by_name['versions']._serialized_options = b'\xe0A\x01'
    _globals['_APIMETADATA'].fields_by_name['original_id']._loaded_options = None
    _globals['_APIMETADATA'].fields_by_name['original_id']._serialized_options = b'\xe0A\x01'
    _globals['_APIMETADATA'].fields_by_name['original_create_time']._loaded_options = None
    _globals['_APIMETADATA'].fields_by_name['original_create_time']._serialized_options = b'\xe0A\x01'
    _globals['_APIMETADATA'].fields_by_name['original_update_time']._loaded_options = None
    _globals['_APIMETADATA'].fields_by_name['original_update_time']._serialized_options = b'\xe0A\x02'
    _globals['_VERSIONMETADATA'].fields_by_name['version']._loaded_options = None
    _globals['_VERSIONMETADATA'].fields_by_name['version']._serialized_options = b'\xe0A\x02'
    _globals['_VERSIONMETADATA'].fields_by_name['specs']._loaded_options = None
    _globals['_VERSIONMETADATA'].fields_by_name['specs']._serialized_options = b'\xe0A\x01'
    _globals['_VERSIONMETADATA'].fields_by_name['deployments']._loaded_options = None
    _globals['_VERSIONMETADATA'].fields_by_name['deployments']._serialized_options = b'\xe0A\x01'
    _globals['_VERSIONMETADATA'].fields_by_name['original_id']._loaded_options = None
    _globals['_VERSIONMETADATA'].fields_by_name['original_id']._serialized_options = b'\xe0A\x01'
    _globals['_VERSIONMETADATA'].fields_by_name['original_create_time']._loaded_options = None
    _globals['_VERSIONMETADATA'].fields_by_name['original_create_time']._serialized_options = b'\xe0A\x01'
    _globals['_VERSIONMETADATA'].fields_by_name['original_update_time']._loaded_options = None
    _globals['_VERSIONMETADATA'].fields_by_name['original_update_time']._serialized_options = b'\xe0A\x02'
    _globals['_SPECMETADATA'].fields_by_name['spec']._loaded_options = None
    _globals['_SPECMETADATA'].fields_by_name['spec']._serialized_options = b'\xe0A\x02'
    _globals['_SPECMETADATA'].fields_by_name['original_id']._loaded_options = None
    _globals['_SPECMETADATA'].fields_by_name['original_id']._serialized_options = b'\xe0A\x01'
    _globals['_SPECMETADATA'].fields_by_name['original_create_time']._loaded_options = None
    _globals['_SPECMETADATA'].fields_by_name['original_create_time']._serialized_options = b'\xe0A\x01'
    _globals['_SPECMETADATA'].fields_by_name['original_update_time']._loaded_options = None
    _globals['_SPECMETADATA'].fields_by_name['original_update_time']._serialized_options = b'\xe0A\x02'
    _globals['_DEPLOYMENTMETADATA'].fields_by_name['deployment']._loaded_options = None
    _globals['_DEPLOYMENTMETADATA'].fields_by_name['deployment']._serialized_options = b'\xe0A\x02'
    _globals['_DEPLOYMENTMETADATA'].fields_by_name['original_id']._loaded_options = None
    _globals['_DEPLOYMENTMETADATA'].fields_by_name['original_id']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYMENTMETADATA'].fields_by_name['original_create_time']._loaded_options = None
    _globals['_DEPLOYMENTMETADATA'].fields_by_name['original_create_time']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYMENTMETADATA'].fields_by_name['original_update_time']._loaded_options = None
    _globals['_DEPLOYMENTMETADATA'].fields_by_name['original_update_time']._serialized_options = b'\xe0A\x02'
    _globals['_APIHUBCOLLECT']._loaded_options = None
    _globals['_APIHUBCOLLECT']._serialized_options = b'\xcaA\x15apihub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_APIHUBCOLLECT'].methods_by_name['CollectApiData']._loaded_options = None
    _globals['_APIHUBCOLLECT'].methods_by_name['CollectApiData']._serialized_options = b'\xcaA+\n\x16CollectApiDataResponse\x12\x11OperationMetadata\xdaA!location,collection_type,api_data\x82\xd3\xe4\x93\x029"4/v1/{location=projects/*/locations/*}:collectApiData:\x01*'
    _globals['_COLLECTIONTYPE']._serialized_start = 1900
    _globals['_COLLECTIONTYPE']._serialized_end = 2005
    _globals['_COLLECTAPIDATAREQUEST']._serialized_start = 302
    _globals['_COLLECTAPIDATAREQUEST']._serialized_end = 607
    _globals['_APIDATA']._serialized_start = 609
    _globals['_APIDATA']._serialized_end = 701
    _globals['_APIMETADATALIST']._serialized_start = 703
    _globals['_APIMETADATALIST']._serialized_end = 784
    _globals['_APIMETADATA']._serialized_start = 787
    _globals['_APIMETADATA']._serialized_end = 1063
    _globals['_VERSIONMETADATA']._serialized_start = 1066
    _globals['_VERSIONMETADATA']._serialized_end = 1418
    _globals['_SPECMETADATA']._serialized_start = 1421
    _globals['_SPECMETADATA']._serialized_end = 1636
    _globals['_DEPLOYMENTMETADATA']._serialized_start = 1639
    _globals['_DEPLOYMENTMETADATA']._serialized_end = 1872
    _globals['_COLLECTAPIDATARESPONSE']._serialized_start = 1874
    _globals['_COLLECTAPIDATARESPONSE']._serialized_end = 1898
    _globals['_APIHUBCOLLECT']._serialized_start = 2008
    _globals['_APIHUBCOLLECT']._serialized_end = 2343