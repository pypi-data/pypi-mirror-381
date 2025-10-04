"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/networkservices/v1/mesh.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.networkservices.v1 import common_pb2 as google_dot_cloud_dot_networkservices_dot_v1_dot_common__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/networkservices/v1/mesh.proto\x12\x1fgoogle.cloud.networkservices.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/networkservices/v1/common.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x91\x04\n\x04Mesh\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x16\n\tself_link\x18\t \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12F\n\x06labels\x18\x04 \x03(\x0b21.google.cloud.networkservices.v1.Mesh.LabelsEntryB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x1e\n\x11interception_port\x18\x08 \x01(\x05B\x03\xe0A\x01\x12N\n\renvoy_headers\x18\x10 \x01(\x0e2-.google.cloud.networkservices.v1.EnvoyHeadersB\x03\xe0A\x01H\x00\x88\x01\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:_\xeaA\\\n#networkservices.googleapis.com/Mesh\x125projects/{project}/locations/{location}/meshes/{mesh}B\x10\n\x0e_envoy_headers"\x9c\x01\n\x11ListMeshesRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#networkservices.googleapis.com/Mesh\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12#\n\x16return_partial_success\x18\x04 \x01(\x08B\x03\xe0A\x01"y\n\x12ListMeshesResponse\x125\n\x06meshes\x18\x01 \x03(\x0b2%.google.cloud.networkservices.v1.Mesh\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"K\n\x0eGetMeshRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#networkservices.googleapis.com/Mesh"\xa0\x01\n\x11CreateMeshRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#networkservices.googleapis.com/Mesh\x12\x14\n\x07mesh_id\x18\x02 \x01(\tB\x03\xe0A\x02\x128\n\x04mesh\x18\x03 \x01(\x0b2%.google.cloud.networkservices.v1.MeshB\x03\xe0A\x02"\x83\x01\n\x11UpdateMeshRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x128\n\x04mesh\x18\x02 \x01(\x0b2%.google.cloud.networkservices.v1.MeshB\x03\xe0A\x02"N\n\x11DeleteMeshRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#networkservices.googleapis.com/MeshB\xe4\x02\n#com.google.cloud.networkservices.v1B\tMeshProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1\xeaAw\n(compute.googleapis.com/ServiceAttachment\x12Kprojects/{project}/regions/{region}/serviceAttachments/{service_attachment}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networkservices.v1.mesh_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.networkservices.v1B\tMeshProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1\xeaAw\n(compute.googleapis.com/ServiceAttachment\x12Kprojects/{project}/regions/{region}/serviceAttachments/{service_attachment}'
    _globals['_MESH_LABELSENTRY']._loaded_options = None
    _globals['_MESH_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_MESH'].fields_by_name['name']._loaded_options = None
    _globals['_MESH'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_MESH'].fields_by_name['self_link']._loaded_options = None
    _globals['_MESH'].fields_by_name['self_link']._serialized_options = b'\xe0A\x03'
    _globals['_MESH'].fields_by_name['create_time']._loaded_options = None
    _globals['_MESH'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MESH'].fields_by_name['update_time']._loaded_options = None
    _globals['_MESH'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_MESH'].fields_by_name['labels']._loaded_options = None
    _globals['_MESH'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_MESH'].fields_by_name['description']._loaded_options = None
    _globals['_MESH'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_MESH'].fields_by_name['interception_port']._loaded_options = None
    _globals['_MESH'].fields_by_name['interception_port']._serialized_options = b'\xe0A\x01'
    _globals['_MESH'].fields_by_name['envoy_headers']._loaded_options = None
    _globals['_MESH'].fields_by_name['envoy_headers']._serialized_options = b'\xe0A\x01'
    _globals['_MESH']._loaded_options = None
    _globals['_MESH']._serialized_options = b'\xeaA\\\n#networkservices.googleapis.com/Mesh\x125projects/{project}/locations/{location}/meshes/{mesh}'
    _globals['_LISTMESHESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMESHESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#networkservices.googleapis.com/Mesh'
    _globals['_LISTMESHESREQUEST'].fields_by_name['return_partial_success']._loaded_options = None
    _globals['_LISTMESHESREQUEST'].fields_by_name['return_partial_success']._serialized_options = b'\xe0A\x01'
    _globals['_GETMESHREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMESHREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#networkservices.googleapis.com/Mesh'
    _globals['_CREATEMESHREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEMESHREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#networkservices.googleapis.com/Mesh'
    _globals['_CREATEMESHREQUEST'].fields_by_name['mesh_id']._loaded_options = None
    _globals['_CREATEMESHREQUEST'].fields_by_name['mesh_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEMESHREQUEST'].fields_by_name['mesh']._loaded_options = None
    _globals['_CREATEMESHREQUEST'].fields_by_name['mesh']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEMESHREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEMESHREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEMESHREQUEST'].fields_by_name['mesh']._loaded_options = None
    _globals['_UPDATEMESHREQUEST'].fields_by_name['mesh']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEMESHREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEMESHREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#networkservices.googleapis.com/Mesh'
    _globals['_MESH']._serialized_start = 253
    _globals['_MESH']._serialized_end = 782
    _globals['_MESH_LABELSENTRY']._serialized_start = 622
    _globals['_MESH_LABELSENTRY']._serialized_end = 667
    _globals['_LISTMESHESREQUEST']._serialized_start = 785
    _globals['_LISTMESHESREQUEST']._serialized_end = 941
    _globals['_LISTMESHESRESPONSE']._serialized_start = 943
    _globals['_LISTMESHESRESPONSE']._serialized_end = 1064
    _globals['_GETMESHREQUEST']._serialized_start = 1066
    _globals['_GETMESHREQUEST']._serialized_end = 1141
    _globals['_CREATEMESHREQUEST']._serialized_start = 1144
    _globals['_CREATEMESHREQUEST']._serialized_end = 1304
    _globals['_UPDATEMESHREQUEST']._serialized_start = 1307
    _globals['_UPDATEMESHREQUEST']._serialized_end = 1438
    _globals['_DELETEMESHREQUEST']._serialized_start = 1440
    _globals['_DELETEMESHREQUEST']._serialized_end = 1518