"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1alpha/estimate_billing_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1alpha import import_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_import__config__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/cloud/discoveryengine/v1alpha/estimate_billing_service.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a8google/cloud/discoveryengine/v1alpha/import_config.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf8\x05\n\x17EstimateDataSizeRequest\x12n\n\x13website_data_source\x18\x02 \x01(\x0b2O.google.cloud.discoveryengine.v1alpha.EstimateDataSizeRequest.WebsiteDataSourceH\x00\x12h\n\x10file_data_source\x18\x03 \x01(\x0b2L.google.cloud.discoveryengine.v1alpha.EstimateDataSizeRequest.FileDataSourceH\x00\x12A\n\x08location\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'discoveryengine.googleapis.com/Location\x1a\xfb\x01\n\x11WebsiteDataSource\x12\x88\x01\n\x16estimator_uri_patterns\x18\x01 \x03(\x0b2c.google.cloud.discoveryengine.v1alpha.EstimateDataSizeRequest.WebsiteDataSource.EstimatorUriPatternB\x03\xe0A\x02\x1a[\n\x13EstimatorUriPattern\x12\x1c\n\x14provided_uri_pattern\x18\x01 \x01(\t\x12\x13\n\x0bexact_match\x18\x02 \x01(\x08\x12\x11\n\texclusive\x18\x03 \x01(\x08\x1a\xb2\x01\n\x0eFileDataSource\x12E\n\ngcs_source\x18\x01 \x01(\x0b2/.google.cloud.discoveryengine.v1alpha.GcsSourceH\x00\x12O\n\x0fbigquery_source\x18\x02 \x01(\x0b24.google.cloud.discoveryengine.v1alpha.BigQuerySourceH\x00B\x08\n\x06sourceB\r\n\x0bdata_source"K\n\x18EstimateDataSizeResponse\x12\x17\n\x0fdata_size_bytes\x18\x01 \x01(\x03\x12\x16\n\x0edocument_count\x18\x02 \x01(\x03"K\n\x18EstimateDataSizeMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp2\xa9\x03\n\x16EstimateBillingService\x12\xba\x02\n\x10EstimateDataSize\x12=.google.cloud.discoveryengine.v1alpha.EstimateDataSizeRequest\x1a\x1d.google.longrunning.Operation"\xc7\x01\xcaA~\n=google.cloud.discoveryengine.v1alpha.EstimateDataSizeResponse\x12=google.cloud.discoveryengine.v1alpha.EstimateDataSizeMetadata\x82\xd3\xe4\x93\x02@";/v1alpha/{location=projects/*/locations/*}:estimateDataSize:\x01*\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa7\x02\n(com.google.cloud.discoveryengine.v1alphaB\x1bEstimateBillingServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.estimate_billing_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x1bEstimateBillingServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_ESTIMATEDATASIZEREQUEST_WEBSITEDATASOURCE'].fields_by_name['estimator_uri_patterns']._loaded_options = None
    _globals['_ESTIMATEDATASIZEREQUEST_WEBSITEDATASOURCE'].fields_by_name['estimator_uri_patterns']._serialized_options = b'\xe0A\x02'
    _globals['_ESTIMATEDATASIZEREQUEST'].fields_by_name['location']._loaded_options = None
    _globals['_ESTIMATEDATASIZEREQUEST'].fields_by_name['location']._serialized_options = b"\xe0A\x02\xfaA)\n'discoveryengine.googleapis.com/Location"
    _globals['_ESTIMATEBILLINGSERVICE']._loaded_options = None
    _globals['_ESTIMATEBILLINGSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ESTIMATEBILLINGSERVICE'].methods_by_name['EstimateDataSize']._loaded_options = None
    _globals['_ESTIMATEBILLINGSERVICE'].methods_by_name['EstimateDataSize']._serialized_options = b'\xcaA~\n=google.cloud.discoveryengine.v1alpha.EstimateDataSizeResponse\x12=google.cloud.discoveryengine.v1alpha.EstimateDataSizeMetadata\x82\xd3\xe4\x93\x02@";/v1alpha/{location=projects/*/locations/*}:estimateDataSize:\x01*'
    _globals['_ESTIMATEDATASIZEREQUEST']._serialized_start = 353
    _globals['_ESTIMATEDATASIZEREQUEST']._serialized_end = 1113
    _globals['_ESTIMATEDATASIZEREQUEST_WEBSITEDATASOURCE']._serialized_start = 666
    _globals['_ESTIMATEDATASIZEREQUEST_WEBSITEDATASOURCE']._serialized_end = 917
    _globals['_ESTIMATEDATASIZEREQUEST_WEBSITEDATASOURCE_ESTIMATORURIPATTERN']._serialized_start = 826
    _globals['_ESTIMATEDATASIZEREQUEST_WEBSITEDATASOURCE_ESTIMATORURIPATTERN']._serialized_end = 917
    _globals['_ESTIMATEDATASIZEREQUEST_FILEDATASOURCE']._serialized_start = 920
    _globals['_ESTIMATEDATASIZEREQUEST_FILEDATASOURCE']._serialized_end = 1098
    _globals['_ESTIMATEDATASIZERESPONSE']._serialized_start = 1115
    _globals['_ESTIMATEDATASIZERESPONSE']._serialized_end = 1190
    _globals['_ESTIMATEDATASIZEMETADATA']._serialized_start = 1192
    _globals['_ESTIMATEDATASIZEMETADATA']._serialized_end = 1267
    _globals['_ESTIMATEBILLINGSERVICE']._serialized_start = 1270
    _globals['_ESTIMATEBILLINGSERVICE']._serialized_end = 1695