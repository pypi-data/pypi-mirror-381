"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/gkehub/v1beta/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.gkehub.v1beta import feature_pb2 as google_dot_cloud_dot_gkehub_dot_v1beta_dot_feature__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/gkehub/v1beta/service.proto\x12\x1agoogle.cloud.gkehub.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a(google/cloud/gkehub/v1beta/feature.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"n\n\x13ListFeaturesRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"g\n\x14ListFeaturesResponse\x126\n\tresources\x18\x01 \x03(\x0b2#.google.cloud.gkehub.v1beta.Feature\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"!\n\x11GetFeatureRequest\x12\x0c\n\x04name\x18\x01 \x01(\t"\x8a\x01\n\x14CreateFeatureRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x12\n\nfeature_id\x18\x02 \x01(\t\x125\n\x08resource\x18\x03 \x01(\x0b2#.google.cloud.gkehub.v1beta.Feature\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"L\n\x14DeleteFeatureRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05force\x18\x02 \x01(\x08\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"\xa5\x01\n\x14UpdateFeatureRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x125\n\x08resource\x18\x03 \x01(\x0b2#.google.cloud.gkehub.v1beta.Feature\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xf9\x01\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rstatus_detail\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10cancel_requested\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x032\xc4\x08\n\x06GkeHub\x12\xb4\x01\n\x0cListFeatures\x12/.google.cloud.gkehub.v1beta.ListFeaturesRequest\x1a0.google.cloud.gkehub.v1beta.ListFeaturesResponse"A\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v1beta/{parent=projects/*/locations/*}/features\x12\xa1\x01\n\nGetFeature\x12-.google.cloud.gkehub.v1beta.GetFeatureRequest\x1a#.google.cloud.gkehub.v1beta.Feature"?\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v1beta/{name=projects/*/locations/*/features/*}\x12\xe0\x01\n\rCreateFeature\x120.google.cloud.gkehub.v1beta.CreateFeatureRequest\x1a\x1d.google.longrunning.Operation"~\xcaA\x1c\n\x07Feature\x12\x11OperationMetadata\xdaA\x1aparent,resource,feature_id\x82\xd3\xe4\x93\x02<"0/v1beta/{parent=projects/*/locations/*}/features:\x08resource\x12\xce\x01\n\rDeleteFeature\x120.google.cloud.gkehub.v1beta.DeleteFeatureRequest\x1a\x1d.google.longrunning.Operation"l\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x022*0/v1beta/{name=projects/*/locations/*/features/*}\x12\xdf\x01\n\rUpdateFeature\x120.google.cloud.gkehub.v1beta.UpdateFeatureRequest\x1a\x1d.google.longrunning.Operation"}\xcaA\x1c\n\x07Feature\x12\x11OperationMetadata\xdaA\x19name,resource,update_mask\x82\xd3\xe4\x93\x02<20/v1beta/{name=projects/*/locations/*/features/*}:\x08resource\x1aI\xcaA\x15gkehub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xc2\x01\n\x1ecom.google.cloud.gkehub.v1betaB\x0cServiceProtoP\x01Z6cloud.google.com/go/gkehub/apiv1beta/gkehubpb;gkehubpb\xaa\x02\x1aGoogle.Cloud.GkeHub.V1Beta\xca\x02\x1aGoogle\\Cloud\\GkeHub\\V1beta\xea\x02\x1dGoogle::Cloud::GkeHub::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkehub.v1beta.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.gkehub.v1betaB\x0cServiceProtoP\x01Z6cloud.google.com/go/gkehub/apiv1beta/gkehubpb;gkehubpb\xaa\x02\x1aGoogle.Cloud.GkeHub.V1Beta\xca\x02\x1aGoogle\\Cloud\\GkeHub\\V1beta\xea\x02\x1dGoogle::Cloud::GkeHub::V1beta'
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
    _globals['_GKEHUB'].methods_by_name['ListFeatures']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v1beta/{parent=projects/*/locations/*}/features'
    _globals['_GKEHUB'].methods_by_name['GetFeature']._loaded_options = None
    _globals['_GKEHUB'].methods_by_name['GetFeature']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v1beta/{name=projects/*/locations/*/features/*}'
    _globals['_GKEHUB'].methods_by_name['CreateFeature']._loaded_options = None
    _globals['_GKEHUB'].methods_by_name['CreateFeature']._serialized_options = b'\xcaA\x1c\n\x07Feature\x12\x11OperationMetadata\xdaA\x1aparent,resource,feature_id\x82\xd3\xe4\x93\x02<"0/v1beta/{parent=projects/*/locations/*}/features:\x08resource'
    _globals['_GKEHUB'].methods_by_name['DeleteFeature']._loaded_options = None
    _globals['_GKEHUB'].methods_by_name['DeleteFeature']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x022*0/v1beta/{name=projects/*/locations/*/features/*}'
    _globals['_GKEHUB'].methods_by_name['UpdateFeature']._loaded_options = None
    _globals['_GKEHUB'].methods_by_name['UpdateFeature']._serialized_options = b'\xcaA\x1c\n\x07Feature\x12\x11OperationMetadata\xdaA\x19name,resource,update_mask\x82\xd3\xe4\x93\x02<20/v1beta/{name=projects/*/locations/*/features/*}:\x08resource'
    _globals['_LISTFEATURESREQUEST']._serialized_start = 306
    _globals['_LISTFEATURESREQUEST']._serialized_end = 416
    _globals['_LISTFEATURESRESPONSE']._serialized_start = 418
    _globals['_LISTFEATURESRESPONSE']._serialized_end = 521
    _globals['_GETFEATUREREQUEST']._serialized_start = 523
    _globals['_GETFEATUREREQUEST']._serialized_end = 556
    _globals['_CREATEFEATUREREQUEST']._serialized_start = 559
    _globals['_CREATEFEATUREREQUEST']._serialized_end = 697
    _globals['_DELETEFEATUREREQUEST']._serialized_start = 699
    _globals['_DELETEFEATUREREQUEST']._serialized_end = 775
    _globals['_UPDATEFEATUREREQUEST']._serialized_start = 778
    _globals['_UPDATEFEATUREREQUEST']._serialized_end = 943
    _globals['_OPERATIONMETADATA']._serialized_start = 946
    _globals['_OPERATIONMETADATA']._serialized_end = 1195
    _globals['_GKEHUB']._serialized_start = 1198
    _globals['_GKEHUB']._serialized_end = 2290