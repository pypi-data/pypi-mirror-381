"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/networkmanagement/v1beta1/reachability.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.networkmanagement.v1beta1 import connectivity_test_pb2 as google_dot_cloud_dot_networkmanagement_dot_v1beta1_dot_connectivity__test__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/networkmanagement/v1beta1/reachability.proto\x12&google.cloud.networkmanagement.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a>google/cloud/networkmanagement/v1beta1/connectivity_test.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xac\x01\n\x1cListConnectivityTestsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x9a\x01\n\x1dListConnectivityTestsResponse\x12K\n\tresources\x18\x01 \x03(\x0b28.google.cloud.networkmanagement.v1beta1.ConnectivityTest\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"e\n\x1aGetConnectivityTestRequest\x12G\n\x04name\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1networkmanagement.googleapis.com/ConnectivityTest"\xcb\x01\n\x1dCreateConnectivityTestRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x14\n\x07test_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12O\n\x08resource\x18\x03 \x01(\x0b28.google.cloud.networkmanagement.v1beta1.ConnectivityTestB\x03\xe0A\x02"\xa6\x01\n\x1dUpdateConnectivityTestRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12O\n\x08resource\x18\x02 \x01(\x0b28.google.cloud.networkmanagement.v1beta1.ConnectivityTestB\x03\xe0A\x02"h\n\x1dDeleteConnectivityTestRequest\x12G\n\x04name\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1networkmanagement.googleapis.com/ConnectivityTest"g\n\x1cRerunConnectivityTestRequest\x12G\n\x04name\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1networkmanagement.googleapis.com/ConnectivityTest"\xd6\x01\n\x11OperationMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0e\n\x06target\x18\x03 \x01(\t\x12\x0c\n\x04verb\x18\x04 \x01(\t\x12\x15\n\rstatus_detail\x18\x05 \x01(\t\x12\x18\n\x10cancel_requested\x18\x06 \x01(\x08\x12\x13\n\x0bapi_version\x18\x07 \x01(\t2\xa3\r\n\x13ReachabilityService\x12\xed\x01\n\x15ListConnectivityTests\x12D.google.cloud.networkmanagement.v1beta1.ListConnectivityTestsRequest\x1aE.google.cloud.networkmanagement.v1beta1.ListConnectivityTestsResponse"G\x82\xd3\xe4\x93\x02A\x12?/v1beta1/{parent=projects/*/locations/global}/connectivityTests\x12\xdc\x01\n\x13GetConnectivityTest\x12B.google.cloud.networkmanagement.v1beta1.GetConnectivityTestRequest\x1a8.google.cloud.networkmanagement.v1beta1.ConnectivityTest"G\x82\xd3\xe4\x93\x02A\x12?/v1beta1/{name=projects/*/locations/global/connectivityTests/*}\x12\xa1\x02\n\x16CreateConnectivityTest\x12E.google.cloud.networkmanagement.v1beta1.CreateConnectivityTestRequest\x1a\x1d.google.longrunning.Operation"\xa0\x01\xcaAL\n7google.cloud.networkmanagement.v1beta1.ConnectivityTest\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02K"?/v1beta1/{parent=projects/*/locations/global}/connectivityTests:\x08resource\x12\xaa\x02\n\x16UpdateConnectivityTest\x12E.google.cloud.networkmanagement.v1beta1.UpdateConnectivityTestRequest\x1a\x1d.google.longrunning.Operation"\xa9\x01\xcaAL\n7google.cloud.networkmanagement.v1beta1.ConnectivityTest\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02T2H/v1beta1/{resource.name=projects/*/locations/global/connectivityTests/*}:\x08resource\x12\x9e\x02\n\x15RerunConnectivityTest\x12D.google.cloud.networkmanagement.v1beta1.RerunConnectivityTestRequest\x1a\x1d.google.longrunning.Operation"\x9f\x01\xcaAL\n7google.cloud.networkmanagement.v1beta1.ConnectivityTest\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02J"E/v1beta1/{name=projects/*/locations/global/connectivityTests/*}:rerun:\x01*\x12\xf4\x01\n\x16DeleteConnectivityTest\x12E.google.cloud.networkmanagement.v1beta1.DeleteConnectivityTestRequest\x1a\x1d.google.longrunning.Operation"t\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02A*?/v1beta1/{name=projects/*/locations/global/connectivityTests/*}\x1aT\xcaA networkmanagement.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa0\x02\n*com.google.cloud.networkmanagement.v1beta1B\x18ReachabilityServiceProtoP\x01ZXcloud.google.com/go/networkmanagement/apiv1beta1/networkmanagementpb;networkmanagementpb\xaa\x02&Google.Cloud.NetworkManagement.V1Beta1\xca\x02&Google\\Cloud\\NetworkManagement\\V1beta1\xea\x02)Google::Cloud::NetworkManagement::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networkmanagement.v1beta1.reachability_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.networkmanagement.v1beta1B\x18ReachabilityServiceProtoP\x01ZXcloud.google.com/go/networkmanagement/apiv1beta1/networkmanagementpb;networkmanagementpb\xaa\x02&Google.Cloud.NetworkManagement.V1Beta1\xca\x02&Google\\Cloud\\NetworkManagement\\V1beta1\xea\x02)Google::Cloud::NetworkManagement::V1beta1'
    _globals['_LISTCONNECTIVITYTESTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONNECTIVITYTESTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_GETCONNECTIVITYTESTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONNECTIVITYTESTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA3\n1networkmanagement.googleapis.com/ConnectivityTest'
    _globals['_CREATECONNECTIVITYTESTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECONNECTIVITYTESTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_CREATECONNECTIVITYTESTREQUEST'].fields_by_name['test_id']._loaded_options = None
    _globals['_CREATECONNECTIVITYTESTREQUEST'].fields_by_name['test_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECONNECTIVITYTESTREQUEST'].fields_by_name['resource']._loaded_options = None
    _globals['_CREATECONNECTIVITYTESTREQUEST'].fields_by_name['resource']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONNECTIVITYTESTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECONNECTIVITYTESTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONNECTIVITYTESTREQUEST'].fields_by_name['resource']._loaded_options = None
    _globals['_UPDATECONNECTIVITYTESTREQUEST'].fields_by_name['resource']._serialized_options = b'\xe0A\x02'
    _globals['_DELETECONNECTIVITYTESTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECONNECTIVITYTESTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA3\n1networkmanagement.googleapis.com/ConnectivityTest'
    _globals['_RERUNCONNECTIVITYTESTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RERUNCONNECTIVITYTESTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA3\n1networkmanagement.googleapis.com/ConnectivityTest'
    _globals['_REACHABILITYSERVICE']._loaded_options = None
    _globals['_REACHABILITYSERVICE']._serialized_options = b'\xcaA networkmanagement.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_REACHABILITYSERVICE'].methods_by_name['ListConnectivityTests']._loaded_options = None
    _globals['_REACHABILITYSERVICE'].methods_by_name['ListConnectivityTests']._serialized_options = b'\x82\xd3\xe4\x93\x02A\x12?/v1beta1/{parent=projects/*/locations/global}/connectivityTests'
    _globals['_REACHABILITYSERVICE'].methods_by_name['GetConnectivityTest']._loaded_options = None
    _globals['_REACHABILITYSERVICE'].methods_by_name['GetConnectivityTest']._serialized_options = b'\x82\xd3\xe4\x93\x02A\x12?/v1beta1/{name=projects/*/locations/global/connectivityTests/*}'
    _globals['_REACHABILITYSERVICE'].methods_by_name['CreateConnectivityTest']._loaded_options = None
    _globals['_REACHABILITYSERVICE'].methods_by_name['CreateConnectivityTest']._serialized_options = b'\xcaAL\n7google.cloud.networkmanagement.v1beta1.ConnectivityTest\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02K"?/v1beta1/{parent=projects/*/locations/global}/connectivityTests:\x08resource'
    _globals['_REACHABILITYSERVICE'].methods_by_name['UpdateConnectivityTest']._loaded_options = None
    _globals['_REACHABILITYSERVICE'].methods_by_name['UpdateConnectivityTest']._serialized_options = b'\xcaAL\n7google.cloud.networkmanagement.v1beta1.ConnectivityTest\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02T2H/v1beta1/{resource.name=projects/*/locations/global/connectivityTests/*}:\x08resource'
    _globals['_REACHABILITYSERVICE'].methods_by_name['RerunConnectivityTest']._loaded_options = None
    _globals['_REACHABILITYSERVICE'].methods_by_name['RerunConnectivityTest']._serialized_options = b'\xcaAL\n7google.cloud.networkmanagement.v1beta1.ConnectivityTest\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02J"E/v1beta1/{name=projects/*/locations/global/connectivityTests/*}:rerun:\x01*'
    _globals['_REACHABILITYSERVICE'].methods_by_name['DeleteConnectivityTest']._loaded_options = None
    _globals['_REACHABILITYSERVICE'].methods_by_name['DeleteConnectivityTest']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\x82\xd3\xe4\x93\x02A*?/v1beta1/{name=projects/*/locations/global/connectivityTests/*}'
    _globals['_LISTCONNECTIVITYTESTSREQUEST']._serialized_start = 414
    _globals['_LISTCONNECTIVITYTESTSREQUEST']._serialized_end = 586
    _globals['_LISTCONNECTIVITYTESTSRESPONSE']._serialized_start = 589
    _globals['_LISTCONNECTIVITYTESTSRESPONSE']._serialized_end = 743
    _globals['_GETCONNECTIVITYTESTREQUEST']._serialized_start = 745
    _globals['_GETCONNECTIVITYTESTREQUEST']._serialized_end = 846
    _globals['_CREATECONNECTIVITYTESTREQUEST']._serialized_start = 849
    _globals['_CREATECONNECTIVITYTESTREQUEST']._serialized_end = 1052
    _globals['_UPDATECONNECTIVITYTESTREQUEST']._serialized_start = 1055
    _globals['_UPDATECONNECTIVITYTESTREQUEST']._serialized_end = 1221
    _globals['_DELETECONNECTIVITYTESTREQUEST']._serialized_start = 1223
    _globals['_DELETECONNECTIVITYTESTREQUEST']._serialized_end = 1327
    _globals['_RERUNCONNECTIVITYTESTREQUEST']._serialized_start = 1329
    _globals['_RERUNCONNECTIVITYTESTREQUEST']._serialized_end = 1432
    _globals['_OPERATIONMETADATA']._serialized_start = 1435
    _globals['_OPERATIONMETADATA']._serialized_end = 1649
    _globals['_REACHABILITYSERVICE']._serialized_start = 1652
    _globals['_REACHABILITYSERVICE']._serialized_end = 3351