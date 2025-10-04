"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/gkehub/v1/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.gkehub.v1 import feature_pb2 as google_dot_cloud_dot_gkehub_dot_v1_dot_feature__pb2
from .....google.cloud.gkehub.v1 import membership_pb2 as google_dot_cloud_dot_gkehub_dot_v1_dot_membership__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/cloud/gkehub/v1/service.proto\x12\x16google.cloud.gkehub.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a$google/cloud/gkehub/v1/feature.proto\x1a\'google/cloud/gkehub/v1/membership.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xaf\x01\n\x16ListMembershipsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 gkehub.googleapis.com/Membership\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"~\n\x17ListMembershipsResponse\x125\n\tresources\x18\x01 \x03(\x0b2".google.cloud.gkehub.v1.Membership\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"N\n\x14GetMembershipRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n gkehub.googleapis.com/Membership"\xc3\x01\n\x17CreateMembershipRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 gkehub.googleapis.com/Membership\x12\x1a\n\rmembership_id\x18\x02 \x01(\tB\x03\xe0A\x02\x129\n\x08resource\x18\x03 \x01(\x0b2".google.cloud.gkehub.v1.MembershipB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"~\n\x17DeleteMembershipRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n gkehub.googleapis.com/Membership\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x12\n\x05force\x18\x03 \x01(\x08B\x03\xe0A\x01"\xdb\x01\n\x17UpdateMembershipRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n gkehub.googleapis.com/Membership\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x129\n\x08resource\x18\x03 \x01(\x0b2".google.cloud.gkehub.v1.MembershipB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xf2\x01\n\x1eGenerateConnectManifestRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n gkehub.googleapis.com/Membership\x12\x16\n\tnamespace\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x12\n\x05proxy\x18\x03 \x01(\x0cB\x03\xe0A\x01\x12\x14\n\x07version\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x17\n\nis_upgrade\x18\x05 \x01(\x08B\x03\xe0A\x01\x12\x15\n\x08registry\x18\x06 \x01(\tB\x03\xe0A\x01\x12&\n\x19image_pull_secret_content\x18\x07 \x01(\x0cB\x03\xe0A\x01"a\n\x1fGenerateConnectManifestResponse\x12>\n\x08manifest\x18\x01 \x03(\x0b2,.google.cloud.gkehub.v1.ConnectAgentResource"X\n\x14ConnectAgentResource\x12.\n\x04type\x18\x01 \x01(\x0b2 .google.cloud.gkehub.v1.TypeMeta\x12\x10\n\x08manifest\x18\x02 \x01(\t"-\n\x08TypeMeta\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x13\n\x0bapi_version\x18\x02 \x01(\t"\x92\x01\n\x13ListFeaturesRequest\x122\n\x06parent\x18\x01 \x01(\tB"\xfaA\x1f\x12\x1dgkehub.googleapis.com/Feature\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"c\n\x14ListFeaturesResponse\x122\n\tresources\x18\x01 \x03(\x0b2\x1f.google.cloud.gkehub.v1.Feature\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"E\n\x11GetFeatureRequest\x120\n\x04name\x18\x01 \x01(\tB"\xfaA\x1f\n\x1dgkehub.googleapis.com/Feature"\xa5\x01\n\x14CreateFeatureRequest\x122\n\x06parent\x18\x01 \x01(\tB"\xfaA\x1f\x12\x1dgkehub.googleapis.com/Feature\x12\x12\n\nfeature_id\x18\x02 \x01(\t\x121\n\x08resource\x18\x03 \x01(\x0b2\x1f.google.cloud.gkehub.v1.Feature\x12\x12\n\nrequest_id\x18\x04 \x01(\t"p\n\x14DeleteFeatureRequest\x120\n\x04name\x18\x01 \x01(\tB"\xfaA\x1f\n\x1dgkehub.googleapis.com/Feature\x12\r\n\x05force\x18\x02 \x01(\x08\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"\xc0\x01\n\x14UpdateFeatureRequest\x120\n\x04name\x18\x01 \x01(\tB"\xfaA\x1f\n\x1dgkehub.googleapis.com/Feature\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x121\n\x08resource\x18\x03 \x01(\x0b2\x1f.google.cloud.gkehub.v1.Feature\x12\x12\n\nrequest_id\x18\x04 \x01(\t"\xf9\x01\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rstatus_detail\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x1d\n\x10cancel_requested\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x032\xf0\x11\n\x06GkeHub\x12\xb4\x01\n\x0fListMemberships\x12..google.cloud.gkehub.v1.ListMembershipsRequest\x1a/.google.cloud.gkehub.v1.ListMembershipsResponse"@\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=projects/*/locations/*}/memberships\x12\xa8\x01\n\x0cListFeatures\x12+.google.cloud.gkehub.v1.ListFeaturesRequest\x1a,.google.cloud.gkehub.v1.ListFeaturesResponse"=\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/features\x12\xa1\x01\n\rGetMembership\x12,.google.cloud.gkehub.v1.GetMembershipRequest\x1a".google.cloud.gkehub.v1.Membership">\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1/{name=projects/*/locations/*/memberships/*}\x12\x95\x01\n\nGetFeature\x12).google.cloud.gkehub.v1.GetFeatureRequest\x1a\x1f.google.cloud.gkehub.v1.Feature";\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/features/*}\x12\xe8\x01\n\x10CreateMembership\x12/.google.cloud.gkehub.v1.CreateMembershipRequest\x1a\x1d.google.longrunning.Operation"\x83\x01\xcaA\x1f\n\nMembership\x12\x11OperationMetadata\xdaA\x1dparent,resource,membership_id\x82\xd3\xe4\x93\x02;"//v1/{parent=projects/*/locations/*}/memberships:\x08resource\x12\xd8\x01\n\rCreateFeature\x12,.google.cloud.gkehub.v1.CreateFeatureRequest\x1a\x1d.google.longrunning.Operation"z\xcaA\x1c\n\x07Feature\x12\x11OperationMetadata\xdaA\x1aparent,resource,feature_id\x82\xd3\xe4\x93\x028",/v1/{parent=projects/*/locations/*}/features:\x08resource\x12\xcf\x01\n\x10DeleteMembership\x12/.google.cloud.gkehub.v1.DeleteMembershipRequest\x1a\x1d.google.longrunning.Operation"k\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1/{name=projects/*/locations/*/memberships/*}\x12\xc6\x01\n\rDeleteFeature\x12,.google.cloud.gkehub.v1.DeleteFeatureRequest\x1a\x1d.google.longrunning.Operation"h\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02.*,/v1/{name=projects/*/locations/*/features/*}\x12\xe3\x01\n\x10UpdateMembership\x12/.google.cloud.gkehub.v1.UpdateMembershipRequest\x1a\x1d.google.longrunning.Operation"\x7f\xcaA\x1f\n\nMembership\x12\x11OperationMetadata\xdaA\x19name,resource,update_mask\x82\xd3\xe4\x93\x02;2//v1/{name=projects/*/locations/*/memberships/*}:\x08resource\x12\xd7\x01\n\rUpdateFeature\x12,.google.cloud.gkehub.v1.UpdateFeatureRequest\x1a\x1d.google.longrunning.Operation"y\xcaA\x1c\n\x07Feature\x12\x11OperationMetadata\xdaA\x19name,resource,update_mask\x82\xd3\xe4\x93\x0282,/v1/{name=projects/*/locations/*/features/*}:\x08resource\x12\xdb\x01\n\x17GenerateConnectManifest\x126.google.cloud.gkehub.v1.GenerateConnectManifestRequest\x1a7.google.cloud.gkehub.v1.GenerateConnectManifestResponse"O\x82\xd3\xe4\x93\x02I\x12G/v1/{name=projects/*/locations/*/memberships/*}:generateConnectManifest\x1aI\xcaA\x15gkehub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xae\x01\n\x1acom.google.cloud.gkehub.v1B\x0cServiceProtoP\x01Z2cloud.google.com/go/gkehub/apiv1/gkehubpb;gkehubpb\xaa\x02\x16Google.Cloud.GkeHub.V1\xca\x02\x16Google\\Cloud\\GkeHub\\V1\xea\x02\x19Google::Cloud::GkeHub::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkehub.v1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.gkehub.v1B\x0cServiceProtoP\x01Z2cloud.google.com/go/gkehub/apiv1/gkehubpb;gkehubpb\xaa\x02\x16Google.Cloud.GkeHub.V1\xca\x02\x16Google\\Cloud\\GkeHub\\V1\xea\x02\x19Google::Cloud::GkeHub::V1'
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 gkehub.googleapis.com/Membership'
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTMEMBERSHIPSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETMEMBERSHIPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMEMBERSHIPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n gkehub.googleapis.com/Membership'
    _globals['_CREATEMEMBERSHIPREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEMEMBERSHIPREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 gkehub.googleapis.com/Membership'
    _globals['_CREATEMEMBERSHIPREQUEST'].fields_by_name['membership_id']._loaded_options = None
    _globals['_CREATEMEMBERSHIPREQUEST'].fields_by_name['membership_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEMEMBERSHIPREQUEST'].fields_by_name['resource']._loaded_options = None
    _globals['_CREATEMEMBERSHIPREQUEST'].fields_by_name['resource']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEMEMBERSHIPREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEMEMBERSHIPREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEMEMBERSHIPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEMEMBERSHIPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n gkehub.googleapis.com/Membership'
    _globals['_DELETEMEMBERSHIPREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEMEMBERSHIPREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEMEMBERSHIPREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETEMEMBERSHIPREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEMEMBERSHIPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATEMEMBERSHIPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n gkehub.googleapis.com/Membership'
    _globals['_UPDATEMEMBERSHIPREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEMEMBERSHIPREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEMEMBERSHIPREQUEST'].fields_by_name['resource']._loaded_options = None
    _globals['_UPDATEMEMBERSHIPREQUEST'].fields_by_name['resource']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEMEMBERSHIPREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEMEMBERSHIPREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECONNECTMANIFESTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GENERATECONNECTMANIFESTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n gkehub.googleapis.com/Membership'
    _globals['_GENERATECONNECTMANIFESTREQUEST'].fields_by_name['namespace']._loaded_options = None
    _globals['_GENERATECONNECTMANIFESTREQUEST'].fields_by_name['namespace']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECONNECTMANIFESTREQUEST'].fields_by_name['proxy']._loaded_options = None
    _globals['_GENERATECONNECTMANIFESTREQUEST'].fields_by_name['proxy']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECONNECTMANIFESTREQUEST'].fields_by_name['version']._loaded_options = None
    _globals['_GENERATECONNECTMANIFESTREQUEST'].fields_by_name['version']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECONNECTMANIFESTREQUEST'].fields_by_name['is_upgrade']._loaded_options = None
    _globals['_GENERATECONNECTMANIFESTREQUEST'].fields_by_name['is_upgrade']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECONNECTMANIFESTREQUEST'].fields_by_name['registry']._loaded_options = None
    _globals['_GENERATECONNECTMANIFESTREQUEST'].fields_by_name['registry']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECONNECTMANIFESTREQUEST'].fields_by_name['image_pull_secret_content']._loaded_options = None
    _globals['_GENERATECONNECTMANIFESTREQUEST'].fields_by_name['image_pull_secret_content']._serialized_options = b'\xe0A\x01'
    _globals['_LISTFEATURESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFEATURESREQUEST'].fields_by_name['parent']._serialized_options = b'\xfaA\x1f\x12\x1dgkehub.googleapis.com/Feature'
    _globals['_GETFEATUREREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFEATUREREQUEST'].fields_by_name['name']._serialized_options = b'\xfaA\x1f\n\x1dgkehub.googleapis.com/Feature'
    _globals['_CREATEFEATUREREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEFEATUREREQUEST'].fields_by_name['parent']._serialized_options = b'\xfaA\x1f\x12\x1dgkehub.googleapis.com/Feature'
    _globals['_DELETEFEATUREREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEFEATUREREQUEST'].fields_by_name['name']._serialized_options = b'\xfaA\x1f\n\x1dgkehub.googleapis.com/Feature'
    _globals['_DELETEFEATUREREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEFEATUREREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEFEATUREREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATEFEATUREREQUEST'].fields_by_name['name']._serialized_options = b'\xfaA\x1f\n\x1dgkehub.googleapis.com/Feature'
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
    _globals['_GKEHUB'].methods_by_name['ListMemberships']._loaded_options = None
    _globals['_GKEHUB'].methods_by_name['ListMemberships']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=projects/*/locations/*}/memberships'
    _globals['_GKEHUB'].methods_by_name['ListFeatures']._loaded_options = None
    _globals['_GKEHUB'].methods_by_name['ListFeatures']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/features'
    _globals['_GKEHUB'].methods_by_name['GetMembership']._loaded_options = None
    _globals['_GKEHUB'].methods_by_name['GetMembership']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1/{name=projects/*/locations/*/memberships/*}'
    _globals['_GKEHUB'].methods_by_name['GetFeature']._loaded_options = None
    _globals['_GKEHUB'].methods_by_name['GetFeature']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/features/*}'
    _globals['_GKEHUB'].methods_by_name['CreateMembership']._loaded_options = None
    _globals['_GKEHUB'].methods_by_name['CreateMembership']._serialized_options = b'\xcaA\x1f\n\nMembership\x12\x11OperationMetadata\xdaA\x1dparent,resource,membership_id\x82\xd3\xe4\x93\x02;"//v1/{parent=projects/*/locations/*}/memberships:\x08resource'
    _globals['_GKEHUB'].methods_by_name['CreateFeature']._loaded_options = None
    _globals['_GKEHUB'].methods_by_name['CreateFeature']._serialized_options = b'\xcaA\x1c\n\x07Feature\x12\x11OperationMetadata\xdaA\x1aparent,resource,feature_id\x82\xd3\xe4\x93\x028",/v1/{parent=projects/*/locations/*}/features:\x08resource'
    _globals['_GKEHUB'].methods_by_name['DeleteMembership']._loaded_options = None
    _globals['_GKEHUB'].methods_by_name['DeleteMembership']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1/{name=projects/*/locations/*/memberships/*}'
    _globals['_GKEHUB'].methods_by_name['DeleteFeature']._loaded_options = None
    _globals['_GKEHUB'].methods_by_name['DeleteFeature']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02.*,/v1/{name=projects/*/locations/*/features/*}'
    _globals['_GKEHUB'].methods_by_name['UpdateMembership']._loaded_options = None
    _globals['_GKEHUB'].methods_by_name['UpdateMembership']._serialized_options = b'\xcaA\x1f\n\nMembership\x12\x11OperationMetadata\xdaA\x19name,resource,update_mask\x82\xd3\xe4\x93\x02;2//v1/{name=projects/*/locations/*/memberships/*}:\x08resource'
    _globals['_GKEHUB'].methods_by_name['UpdateFeature']._loaded_options = None
    _globals['_GKEHUB'].methods_by_name['UpdateFeature']._serialized_options = b'\xcaA\x1c\n\x07Feature\x12\x11OperationMetadata\xdaA\x19name,resource,update_mask\x82\xd3\xe4\x93\x0282,/v1/{name=projects/*/locations/*/features/*}:\x08resource'
    _globals['_GKEHUB'].methods_by_name['GenerateConnectManifest']._loaded_options = None
    _globals['_GKEHUB'].methods_by_name['GenerateConnectManifest']._serialized_options = b'\x82\xd3\xe4\x93\x02I\x12G/v1/{name=projects/*/locations/*/memberships/*}:generateConnectManifest'
    _globals['_LISTMEMBERSHIPSREQUEST']._serialized_start = 363
    _globals['_LISTMEMBERSHIPSREQUEST']._serialized_end = 538
    _globals['_LISTMEMBERSHIPSRESPONSE']._serialized_start = 540
    _globals['_LISTMEMBERSHIPSRESPONSE']._serialized_end = 666
    _globals['_GETMEMBERSHIPREQUEST']._serialized_start = 668
    _globals['_GETMEMBERSHIPREQUEST']._serialized_end = 746
    _globals['_CREATEMEMBERSHIPREQUEST']._serialized_start = 749
    _globals['_CREATEMEMBERSHIPREQUEST']._serialized_end = 944
    _globals['_DELETEMEMBERSHIPREQUEST']._serialized_start = 946
    _globals['_DELETEMEMBERSHIPREQUEST']._serialized_end = 1072
    _globals['_UPDATEMEMBERSHIPREQUEST']._serialized_start = 1075
    _globals['_UPDATEMEMBERSHIPREQUEST']._serialized_end = 1294
    _globals['_GENERATECONNECTMANIFESTREQUEST']._serialized_start = 1297
    _globals['_GENERATECONNECTMANIFESTREQUEST']._serialized_end = 1539
    _globals['_GENERATECONNECTMANIFESTRESPONSE']._serialized_start = 1541
    _globals['_GENERATECONNECTMANIFESTRESPONSE']._serialized_end = 1638
    _globals['_CONNECTAGENTRESOURCE']._serialized_start = 1640
    _globals['_CONNECTAGENTRESOURCE']._serialized_end = 1728
    _globals['_TYPEMETA']._serialized_start = 1730
    _globals['_TYPEMETA']._serialized_end = 1775
    _globals['_LISTFEATURESREQUEST']._serialized_start = 1778
    _globals['_LISTFEATURESREQUEST']._serialized_end = 1924
    _globals['_LISTFEATURESRESPONSE']._serialized_start = 1926
    _globals['_LISTFEATURESRESPONSE']._serialized_end = 2025
    _globals['_GETFEATUREREQUEST']._serialized_start = 2027
    _globals['_GETFEATUREREQUEST']._serialized_end = 2096
    _globals['_CREATEFEATUREREQUEST']._serialized_start = 2099
    _globals['_CREATEFEATUREREQUEST']._serialized_end = 2264
    _globals['_DELETEFEATUREREQUEST']._serialized_start = 2266
    _globals['_DELETEFEATUREREQUEST']._serialized_end = 2378
    _globals['_UPDATEFEATUREREQUEST']._serialized_start = 2381
    _globals['_UPDATEFEATUREREQUEST']._serialized_end = 2573
    _globals['_OPERATIONMETADATA']._serialized_start = 2576
    _globals['_OPERATIONMETADATA']._serialized_end = 2825
    _globals['_GKEHUB']._serialized_start = 2828
    _globals['_GKEHUB']._serialized_end = 5116