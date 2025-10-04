"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/gkehub/v1alpha/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.gkehub.v1alpha import feature_pb2 as google_dot_cloud_dot_gkehub_dot_v1alpha_dot_feature__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/gkehub/v1alpha/service.proto\x12\x1bgoogle.cloud.gkehub.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a)google/cloud/gkehub/v1alpha/feature.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"n\n\x13ListFeaturesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"h\n\x14ListFeaturesResponse\x127\n\tresources\x18\x01 \x03(\x0b2$.google.cloud.gkehub.v1alpha.Feature\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"!\n\x11GetFeatureRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\x8b\x01\n\x14CreateFeatureRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x12\n\nfeature_id\x18\x02 \x01(\t\x126\n\x08resource\x18\x03 \x01(\x0b2$.google.cloud.gkehub.v1alpha.Feature\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"L\n\x14DeleteFeatureRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05force\x18\x02 \x01(\x08\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"\xa6\x01\n\x14UpdateFeatureRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x126\n\x08resource\x18\x03 \x01(\x0b2$.google.cloud.gkehub.v1alpha.Feature\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xf9\x01\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rstatus_detail\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10cancel_requested\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x032\xd0\x08\n\x06GkeHub\x12\xb7\x01\n\x0cListFeatures\x120.google.cloud.gkehub.v1alpha.ListFeaturesRequest\x1a1.google.cloud.gkehub.v1alpha.ListFeaturesResponse"B\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1alpha/{parent=projects/*/locations/*}/features\x12\xa4\x01\n\nGetFeature\x12..google.cloud.gkehub.v1alpha.GetFeatureRequest\x1a$.google.cloud.gkehub.v1alpha.Feature"@\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1alpha/{name=projects/*/locations/*/features/*}\x12\xe2\x01\n\rCreateFeature\x121.google.cloud.gkehub.v1alpha.CreateFeatureRequest\x1a\x1d.google.longrunning.Operation"\x7f\xcaA\x1c\n\x07Feature\x12\x11OperationMetadata\xdaA\x1aparent,resource,feature_id\x82\xd3\xe4\x93\x02="1/v1alpha/{parent=projects/*/locations/*}/features:\x08resource\x12\xd0\x01\n\rDeleteFeature\x121.google.cloud.gkehub.v1alpha.DeleteFeatureRequest\x1a\x1d.google.longrunning.Operation"m\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x023*1/v1alpha/{name=projects/*/locations/*/features/*}\x12\xe1\x01\n\rUpdateFeature\x121.google.cloud.gkehub.v1alpha.UpdateFeatureRequest\x1a\x1d.google.longrunning.Operation"~\xcaA\x1c\n\x07Feature\x12\x11OperationMetadata\xdaA\x19name,resource,update_mask\x82\xd3\xe4\x93\x02=21/v1alpha/{name=projects/*/locations/*/features/*}:\x08resource\x1aI\xcaA\x15gkehub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xc7\x01\n\x1fcom.google.cloud.gkehub.v1alphaB\x0cServiceProtoP\x01Z7cloud.google.com/go/gkehub/apiv1alpha/gkehubpb;gkehubpb\xaa\x02\x1bGoogle.Cloud.GkeHub.V1Alpha\xca\x02\x1bGoogle\\Cloud\\GkeHub\\V1alpha\xea\x02\x1eGoogle::Cloud::GkeHub::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkehub.v1alpha.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.gkehub.v1alphaB\x0cServiceProtoP\x01Z7cloud.google.com/go/gkehub/apiv1alpha/gkehubpb;gkehubpb\xaa\x02\x1bGoogle.Cloud.GkeHub.V1Alpha\xca\x02\x1bGoogle\\Cloud\\GkeHub\\V1alpha\xea\x02\x1eGoogle::Cloud::GkeHub::V1alpha'
    _globals['_CREATEFEATUREREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEFEATUREREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEFEATUREREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEFEATUREREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEFEATUREREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEFEATUREREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_detail']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_detail']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['cancel_requested']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['cancel_requested']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_GKEHUB']._loaded_options = None
    _globals['_GKEHUB']._serialized_options = b'\xcaA\x15gkehub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_GKEHUB'].methods_by_name['ListFeatures']._loaded_options = None
    _globals['_GKEHUB'].methods_by_name['ListFeatures']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1alpha/{parent=projects/*/locations/*}/features'
    _globals['_GKEHUB'].methods_by_name['GetFeature']._loaded_options = None
    _globals['_GKEHUB'].methods_by_name['GetFeature']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1alpha/{name=projects/*/locations/*/features/*}'
    _globals['_GKEHUB'].methods_by_name['CreateFeature']._loaded_options = None
    _globals['_GKEHUB'].methods_by_name['CreateFeature']._serialized_options = b'\xcaA\x1c\n\x07Feature\x12\x11OperationMetadata\xdaA\x1aparent,resource,feature_id\x82\xd3\xe4\x93\x02="1/v1alpha/{parent=projects/*/locations/*}/features:\x08resource'
    _globals['_GKEHUB'].methods_by_name['DeleteFeature']._loaded_options = None
    _globals['_GKEHUB'].methods_by_name['DeleteFeature']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x023*1/v1alpha/{name=projects/*/locations/*/features/*}'
    _globals['_GKEHUB'].methods_by_name['UpdateFeature']._loaded_options = None
    _globals['_GKEHUB'].methods_by_name['UpdateFeature']._serialized_options = b'\xcaA\x1c\n\x07Feature\x12\x11OperationMetadata\xdaA\x19name,resource,update_mask\x82\xd3\xe4\x93\x02=21/v1alpha/{name=projects/*/locations/*/features/*}:\x08resource'
    _globals['_LISTFEATURESREQUEST']._serialized_start = 309
    _globals['_LISTFEATURESREQUEST']._serialized_end = 419
    _globals['_LISTFEATURESRESPONSE']._serialized_start = 421
    _globals['_LISTFEATURESRESPONSE']._serialized_end = 525
    _globals['_GETFEATUREREQUEST']._serialized_start = 527
    _globals['_GETFEATUREREQUEST']._serialized_end = 560
    _globals['_CREATEFEATUREREQUEST']._serialized_start = 563
    _globals['_CREATEFEATUREREQUEST']._serialized_end = 702
    _globals['_DELETEFEATUREREQUEST']._serialized_start = 704
    _globals['_DELETEFEATUREREQUEST']._serialized_end = 780
    _globals['_UPDATEFEATUREREQUEST']._serialized_start = 783
    _globals['_UPDATEFEATUREREQUEST']._serialized_end = 949
    _globals['_OPERATIONMETADATA']._serialized_start = 952
    _globals['_OPERATIONMETADATA']._serialized_end = 1201
    _globals['_GKEHUB']._serialized_start = 1204
    _globals['_GKEHUB']._serialized_end = 2308