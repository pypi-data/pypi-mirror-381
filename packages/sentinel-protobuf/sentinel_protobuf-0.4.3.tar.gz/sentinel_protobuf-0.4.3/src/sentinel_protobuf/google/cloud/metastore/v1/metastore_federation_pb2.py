"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/metastore/v1/metastore_federation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.metastore.v1 import metastore_pb2 as google_dot_cloud_dot_metastore_dot_v1_dot_metastore__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/metastore/v1/metastore_federation.proto\x12\x19google.cloud.metastore.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/metastore/v1/metastore.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xab\x06\n\nFederation\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12A\n\x06labels\x18\x04 \x03(\x0b21.google.cloud.metastore.v1.Federation.LabelsEntry\x12\x14\n\x07version\x18\x05 \x01(\tB\x03\xe0A\x05\x12X\n\x12backend_metastores\x18\x06 \x03(\x0b2<.google.cloud.metastore.v1.Federation.BackendMetastoresEntry\x12\x19\n\x0cendpoint_uri\x18\x07 \x01(\tB\x03\xe0A\x03\x12?\n\x05state\x18\x08 \x01(\x0e2+.google.cloud.metastore.v1.Federation.StateB\x03\xe0A\x03\x12\x1a\n\rstate_message\x18\t \x01(\tB\x03\xe0A\x03\x12\x10\n\x03uid\x18\n \x01(\tB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1ae\n\x16BackendMetastoresEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12:\n\x05value\x18\x02 \x01(\x0b2+.google.cloud.metastore.v1.BackendMetastore:\x028\x01"_\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08DELETING\x10\x04\x12\t\n\x05ERROR\x10\x05:j\xeaAg\n#metastore.googleapis.com/Federation\x12@projects/{project}/locations/{location}/federations/{federation}"\xca\x01\n\x10BackendMetastore\x12\x0c\n\x04name\x18\x01 \x01(\t\x12Q\n\x0emetastore_type\x18\x02 \x01(\x0e29.google.cloud.metastore.v1.BackendMetastore.MetastoreType"U\n\rMetastoreType\x12\x1e\n\x1aMETASTORE_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08BIGQUERY\x10\x02\x12\x16\n\x12DATAPROC_METASTORE\x10\x03"\xb2\x01\n\x16ListFederationsRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#metastore.googleapis.com/Federation\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x83\x01\n\x17ListFederationsResponse\x12:\n\x0bfederations\x18\x01 \x03(\x0b2%.google.cloud.metastore.v1.Federation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"Q\n\x14GetFederationRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#metastore.googleapis.com/Federation"\xcb\x01\n\x17CreateFederationRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#metastore.googleapis.com/Federation\x12\x1a\n\rfederation_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12>\n\nfederation\x18\x03 \x01(\x0b2%.google.cloud.metastore.v1.FederationB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xa8\x01\n\x17UpdateFederationRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12>\n\nfederation\x18\x02 \x01(\x0b2%.google.cloud.metastore.v1.FederationB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"m\n\x17DeleteFederationRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#metastore.googleapis.com/Federation\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x012\xdc\t\n\x1bDataprocMetastoreFederation\x12\xba\x01\n\x0fListFederations\x121.google.cloud.metastore.v1.ListFederationsRequest\x1a2.google.cloud.metastore.v1.ListFederationsResponse"@\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=projects/*/locations/*}/federations\x12\xa7\x01\n\rGetFederation\x12/.google.cloud.metastore.v1.GetFederationRequest\x1a%.google.cloud.metastore.v1.Federation">\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1/{name=projects/*/locations/*/federations/*}\x12\x89\x02\n\x10CreateFederation\x122.google.cloud.metastore.v1.CreateFederationRequest\x1a\x1d.google.longrunning.Operation"\xa1\x01\xcaA9\n\nFederation\x12+google.cloud.metastore.v1.OperationMetadata\xdaA\x1fparent,federation,federation_id\x82\xd3\xe4\x93\x02="//v1/{parent=projects/*/locations/*}/federations:\nfederation\x12\x8b\x02\n\x10UpdateFederation\x122.google.cloud.metastore.v1.UpdateFederationRequest\x1a\x1d.google.longrunning.Operation"\xa3\x01\xcaA9\n\nFederation\x12+google.cloud.metastore.v1.OperationMetadata\xdaA\x16federation,update_mask\x82\xd3\xe4\x93\x02H2:/v1/{federation.name=projects/*/locations/*/federations/*}:\nfederation\x12\xed\x01\n\x10DeleteFederation\x122.google.cloud.metastore.v1.DeleteFederationRequest\x1a\x1d.google.longrunning.Operation"\x85\x01\xcaAD\n\x15google.protobuf.Empty\x12+google.cloud.metastore.v1.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1/{name=projects/*/locations/*/federations/*}\x1aL\xcaA\x18metastore.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBx\n\x1dcom.google.cloud.metastore.v1B\x18MetastoreFederationProtoP\x01Z;cloud.google.com/go/metastore/apiv1/metastorepb;metastorepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.metastore.v1.metastore_federation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.metastore.v1B\x18MetastoreFederationProtoP\x01Z;cloud.google.com/go/metastore/apiv1/metastorepb;metastorepb'
    _globals['_FEDERATION_LABELSENTRY']._loaded_options = None
    _globals['_FEDERATION_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_FEDERATION_BACKENDMETASTORESENTRY']._loaded_options = None
    _globals['_FEDERATION_BACKENDMETASTORESENTRY']._serialized_options = b'8\x01'
    _globals['_FEDERATION'].fields_by_name['name']._loaded_options = None
    _globals['_FEDERATION'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_FEDERATION'].fields_by_name['create_time']._loaded_options = None
    _globals['_FEDERATION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEDERATION'].fields_by_name['update_time']._loaded_options = None
    _globals['_FEDERATION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEDERATION'].fields_by_name['version']._loaded_options = None
    _globals['_FEDERATION'].fields_by_name['version']._serialized_options = b'\xe0A\x05'
    _globals['_FEDERATION'].fields_by_name['endpoint_uri']._loaded_options = None
    _globals['_FEDERATION'].fields_by_name['endpoint_uri']._serialized_options = b'\xe0A\x03'
    _globals['_FEDERATION'].fields_by_name['state']._loaded_options = None
    _globals['_FEDERATION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_FEDERATION'].fields_by_name['state_message']._loaded_options = None
    _globals['_FEDERATION'].fields_by_name['state_message']._serialized_options = b'\xe0A\x03'
    _globals['_FEDERATION'].fields_by_name['uid']._loaded_options = None
    _globals['_FEDERATION'].fields_by_name['uid']._serialized_options = b'\xe0A\x03'
    _globals['_FEDERATION']._loaded_options = None
    _globals['_FEDERATION']._serialized_options = b'\xeaAg\n#metastore.googleapis.com/Federation\x12@projects/{project}/locations/{location}/federations/{federation}'
    _globals['_LISTFEDERATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFEDERATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#metastore.googleapis.com/Federation'
    _globals['_LISTFEDERATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTFEDERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTFEDERATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTFEDERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTFEDERATIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTFEDERATIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTFEDERATIONSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTFEDERATIONSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETFEDERATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFEDERATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#metastore.googleapis.com/Federation'
    _globals['_CREATEFEDERATIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEFEDERATIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#metastore.googleapis.com/Federation'
    _globals['_CREATEFEDERATIONREQUEST'].fields_by_name['federation_id']._loaded_options = None
    _globals['_CREATEFEDERATIONREQUEST'].fields_by_name['federation_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEFEDERATIONREQUEST'].fields_by_name['federation']._loaded_options = None
    _globals['_CREATEFEDERATIONREQUEST'].fields_by_name['federation']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEFEDERATIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEFEDERATIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEFEDERATIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEFEDERATIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEFEDERATIONREQUEST'].fields_by_name['federation']._loaded_options = None
    _globals['_UPDATEFEDERATIONREQUEST'].fields_by_name['federation']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEFEDERATIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEFEDERATIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEFEDERATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEFEDERATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#metastore.googleapis.com/Federation'
    _globals['_DELETEFEDERATIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEFEDERATIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DATAPROCMETASTOREFEDERATION']._loaded_options = None
    _globals['_DATAPROCMETASTOREFEDERATION']._serialized_options = b'\xcaA\x18metastore.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DATAPROCMETASTOREFEDERATION'].methods_by_name['ListFederations']._loaded_options = None
    _globals['_DATAPROCMETASTOREFEDERATION'].methods_by_name['ListFederations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=projects/*/locations/*}/federations'
    _globals['_DATAPROCMETASTOREFEDERATION'].methods_by_name['GetFederation']._loaded_options = None
    _globals['_DATAPROCMETASTOREFEDERATION'].methods_by_name['GetFederation']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1/{name=projects/*/locations/*/federations/*}'
    _globals['_DATAPROCMETASTOREFEDERATION'].methods_by_name['CreateFederation']._loaded_options = None
    _globals['_DATAPROCMETASTOREFEDERATION'].methods_by_name['CreateFederation']._serialized_options = b'\xcaA9\n\nFederation\x12+google.cloud.metastore.v1.OperationMetadata\xdaA\x1fparent,federation,federation_id\x82\xd3\xe4\x93\x02="//v1/{parent=projects/*/locations/*}/federations:\nfederation'
    _globals['_DATAPROCMETASTOREFEDERATION'].methods_by_name['UpdateFederation']._loaded_options = None
    _globals['_DATAPROCMETASTOREFEDERATION'].methods_by_name['UpdateFederation']._serialized_options = b'\xcaA9\n\nFederation\x12+google.cloud.metastore.v1.OperationMetadata\xdaA\x16federation,update_mask\x82\xd3\xe4\x93\x02H2:/v1/{federation.name=projects/*/locations/*/federations/*}:\nfederation'
    _globals['_DATAPROCMETASTOREFEDERATION'].methods_by_name['DeleteFederation']._loaded_options = None
    _globals['_DATAPROCMETASTOREFEDERATION'].methods_by_name['DeleteFederation']._serialized_options = b'\xcaAD\n\x15google.protobuf.Empty\x12+google.cloud.metastore.v1.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1/{name=projects/*/locations/*/federations/*}'
    _globals['_FEDERATION']._serialized_start = 375
    _globals['_FEDERATION']._serialized_end = 1186
    _globals['_FEDERATION_LABELSENTRY']._serialized_start = 833
    _globals['_FEDERATION_LABELSENTRY']._serialized_end = 878
    _globals['_FEDERATION_BACKENDMETASTORESENTRY']._serialized_start = 880
    _globals['_FEDERATION_BACKENDMETASTORESENTRY']._serialized_end = 981
    _globals['_FEDERATION_STATE']._serialized_start = 983
    _globals['_FEDERATION_STATE']._serialized_end = 1078
    _globals['_BACKENDMETASTORE']._serialized_start = 1189
    _globals['_BACKENDMETASTORE']._serialized_end = 1391
    _globals['_BACKENDMETASTORE_METASTORETYPE']._serialized_start = 1306
    _globals['_BACKENDMETASTORE_METASTORETYPE']._serialized_end = 1391
    _globals['_LISTFEDERATIONSREQUEST']._serialized_start = 1394
    _globals['_LISTFEDERATIONSREQUEST']._serialized_end = 1572
    _globals['_LISTFEDERATIONSRESPONSE']._serialized_start = 1575
    _globals['_LISTFEDERATIONSRESPONSE']._serialized_end = 1706
    _globals['_GETFEDERATIONREQUEST']._serialized_start = 1708
    _globals['_GETFEDERATIONREQUEST']._serialized_end = 1789
    _globals['_CREATEFEDERATIONREQUEST']._serialized_start = 1792
    _globals['_CREATEFEDERATIONREQUEST']._serialized_end = 1995
    _globals['_UPDATEFEDERATIONREQUEST']._serialized_start = 1998
    _globals['_UPDATEFEDERATIONREQUEST']._serialized_end = 2166
    _globals['_DELETEFEDERATIONREQUEST']._serialized_start = 2168
    _globals['_DELETEFEDERATIONREQUEST']._serialized_end = 2277
    _globals['_DATAPROCMETASTOREFEDERATION']._serialized_start = 2280
    _globals['_DATAPROCMETASTOREFEDERATION']._serialized_end = 3524