"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/cloudsecuritycompliance/v1/config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.cloudsecuritycompliance.v1 import common_pb2 as google_dot_cloud_dot_cloudsecuritycompliance_dot_v1_dot_common__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/cloudsecuritycompliance/v1/config.proto\x12\'google.cloud.cloudsecuritycompliance.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a4google/cloud/cloudsecuritycompliance/v1/common.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x92\x01\n\x15ListFrameworksRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\x120cloudsecuritycompliance.googleapis.com/Framework\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"y\n\x16ListFrameworksResponse\x12F\n\nframeworks\x18\x01 \x03(\x0b22.google.cloud.cloudsecuritycompliance.v1.Framework\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"}\n\x13GetFrameworkRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0cloudsecuritycompliance.googleapis.com/Framework\x12\x1e\n\x11major_revision_id\x18\x02 \x01(\x03B\x03\xe0A\x01"\xc9\x01\n\x16CreateFrameworkRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\x120cloudsecuritycompliance.googleapis.com/Framework\x12\x19\n\x0cframework_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12J\n\tframework\x18\x03 \x01(\x0b22.google.cloud.cloudsecuritycompliance.v1.FrameworkB\x03\xe0A\x02"\xba\x01\n\x16UpdateFrameworkRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12J\n\tframework\x18\x02 \x01(\x0b22.google.cloud.cloudsecuritycompliance.v1.FrameworkB\x03\xe0A\x02\x12\x1e\n\x11major_revision_id\x18\x03 \x01(\x03B\x03\xe0A\x01"`\n\x16DeleteFrameworkRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0cloudsecuritycompliance.googleapis.com/Framework"\x98\x01\n\x18ListCloudControlsRequest\x12K\n\x06parent\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\x123cloudsecuritycompliance.googleapis.com/CloudControl\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x83\x01\n\x19ListCloudControlsResponse\x12M\n\x0ecloud_controls\x18\x01 \x03(\x0b25.google.cloud.cloudsecuritycompliance.v1.CloudControl\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"c\n\x16GetCloudControlRequest\x12I\n\x04name\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\n3cloudsecuritycompliance.googleapis.com/CloudControl"\xda\x01\n\x19CreateCloudControlRequest\x12K\n\x06parent\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\x123cloudsecuritycompliance.googleapis.com/CloudControl\x12\x1d\n\x10cloud_control_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12Q\n\rcloud_control\x18\x03 \x01(\x0b25.google.cloud.cloudsecuritycompliance.v1.CloudControlB\x03\xe0A\x02"\xa4\x01\n\x19UpdateCloudControlRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12Q\n\rcloud_control\x18\x02 \x01(\x0b25.google.cloud.cloudsecuritycompliance.v1.CloudControlB\x03\xe0A\x02"f\n\x19DeleteCloudControlRequest\x12I\n\x04name\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\n3cloudsecuritycompliance.googleapis.com/CloudControl2\xa1\x12\n\x06Config\x12\xd7\x01\n\x0eListFrameworks\x12>.google.cloud.cloudsecuritycompliance.v1.ListFrameworksRequest\x1a?.google.cloud.cloudsecuritycompliance.v1.ListFrameworksResponse"D\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1/{parent=organizations/*/locations/*}/frameworks\x12\xc4\x01\n\x0cGetFramework\x12<.google.cloud.cloudsecuritycompliance.v1.GetFrameworkRequest\x1a2.google.cloud.cloudsecuritycompliance.v1.Framework"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1/{name=organizations/*/locations/*/frameworks/*}\x12\xee\x01\n\x0fCreateFramework\x12?.google.cloud.cloudsecuritycompliance.v1.CreateFrameworkRequest\x1a2.google.cloud.cloudsecuritycompliance.v1.Framework"f\xdaA\x1dparent,framework,framework_id\x82\xd3\xe4\x93\x02@"3/v1/{parent=organizations/*/locations/*}/frameworks:\tframework\x12\xf0\x01\n\x0fUpdateFramework\x12?.google.cloud.cloudsecuritycompliance.v1.UpdateFrameworkRequest\x1a2.google.cloud.cloudsecuritycompliance.v1.Framework"h\xdaA\x15framework,update_mask\x82\xd3\xe4\x93\x02J2=/v1/{framework.name=organizations/*/locations/*/frameworks/*}:\tframework\x12\xae\x01\n\x0fDeleteFramework\x12?.google.cloud.cloudsecuritycompliance.v1.DeleteFrameworkRequest\x1a\x16.google.protobuf.Empty"B\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1/{name=organizations/*/locations/*/frameworks/*}\x12\xe3\x01\n\x11ListCloudControls\x12A.google.cloud.cloudsecuritycompliance.v1.ListCloudControlsRequest\x1aB.google.cloud.cloudsecuritycompliance.v1.ListCloudControlsResponse"G\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1/{parent=organizations/*/locations/*}/cloudControls\x12\xd0\x01\n\x0fGetCloudControl\x12?.google.cloud.cloudsecuritycompliance.v1.GetCloudControlRequest\x1a5.google.cloud.cloudsecuritycompliance.v1.CloudControl"E\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1/{name=organizations/*/locations/*/cloudControls/*}\x12\x86\x02\n\x12CreateCloudControl\x12B.google.cloud.cloudsecuritycompliance.v1.CreateCloudControlRequest\x1a5.google.cloud.cloudsecuritycompliance.v1.CloudControl"u\xdaA%parent,cloud_control,cloud_control_id\x82\xd3\xe4\x93\x02G"6/v1/{parent=organizations/*/locations/*}/cloudControls:\rcloud_control\x12\x88\x02\n\x12UpdateCloudControl\x12B.google.cloud.cloudsecuritycompliance.v1.UpdateCloudControlRequest\x1a5.google.cloud.cloudsecuritycompliance.v1.CloudControl"w\xdaA\x19cloud_control,update_mask\x82\xd3\xe4\x93\x02U2D/v1/{cloud_control.name=organizations/*/locations/*/cloudControls/*}:\rcloud_control\x12\xb7\x01\n\x12DeleteCloudControl\x12B.google.cloud.cloudsecuritycompliance.v1.DeleteCloudControlRequest\x1a\x16.google.protobuf.Empty"E\xdaA\x04name\x82\xd3\xe4\x93\x028*6/v1/{name=organizations/*/locations/*/cloudControls/*}\x1aZ\xcaA&cloudsecuritycompliance.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa4\x02\n+com.google.cloud.cloudsecuritycompliance.v1B\x0bConfigProtoP\x01Zecloud.google.com/go/cloudsecuritycompliance/apiv1/cloudsecuritycompliancepb;cloudsecuritycompliancepb\xaa\x02\'Google.Cloud.CloudSecurityCompliance.V1\xca\x02\'Google\\Cloud\\CloudSecurityCompliance\\V1\xea\x02*Google::Cloud::CloudSecurityCompliance::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.cloudsecuritycompliance.v1.config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.cloud.cloudsecuritycompliance.v1B\x0bConfigProtoP\x01Zecloud.google.com/go/cloudsecuritycompliance/apiv1/cloudsecuritycompliancepb;cloudsecuritycompliancepb\xaa\x02'Google.Cloud.CloudSecurityCompliance.V1\xca\x02'Google\\Cloud\\CloudSecurityCompliance\\V1\xea\x02*Google::Cloud::CloudSecurityCompliance::V1"
    _globals['_LISTFRAMEWORKSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFRAMEWORKSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\x120cloudsecuritycompliance.googleapis.com/Framework'
    _globals['_LISTFRAMEWORKSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTFRAMEWORKSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTFRAMEWORKSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTFRAMEWORKSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETFRAMEWORKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFRAMEWORKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0cloudsecuritycompliance.googleapis.com/Framework'
    _globals['_GETFRAMEWORKREQUEST'].fields_by_name['major_revision_id']._loaded_options = None
    _globals['_GETFRAMEWORKREQUEST'].fields_by_name['major_revision_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEFRAMEWORKREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEFRAMEWORKREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\x120cloudsecuritycompliance.googleapis.com/Framework'
    _globals['_CREATEFRAMEWORKREQUEST'].fields_by_name['framework_id']._loaded_options = None
    _globals['_CREATEFRAMEWORKREQUEST'].fields_by_name['framework_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEFRAMEWORKREQUEST'].fields_by_name['framework']._loaded_options = None
    _globals['_CREATEFRAMEWORKREQUEST'].fields_by_name['framework']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEFRAMEWORKREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEFRAMEWORKREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEFRAMEWORKREQUEST'].fields_by_name['framework']._loaded_options = None
    _globals['_UPDATEFRAMEWORKREQUEST'].fields_by_name['framework']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEFRAMEWORKREQUEST'].fields_by_name['major_revision_id']._loaded_options = None
    _globals['_UPDATEFRAMEWORKREQUEST'].fields_by_name['major_revision_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEFRAMEWORKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEFRAMEWORKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0cloudsecuritycompliance.googleapis.com/Framework'
    _globals['_LISTCLOUDCONTROLSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCLOUDCONTROLSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA5\x123cloudsecuritycompliance.googleapis.com/CloudControl'
    _globals['_LISTCLOUDCONTROLSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCLOUDCONTROLSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCLOUDCONTROLSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCLOUDCONTROLSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETCLOUDCONTROLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCLOUDCONTROLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA5\n3cloudsecuritycompliance.googleapis.com/CloudControl'
    _globals['_CREATECLOUDCONTROLREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECLOUDCONTROLREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA5\x123cloudsecuritycompliance.googleapis.com/CloudControl'
    _globals['_CREATECLOUDCONTROLREQUEST'].fields_by_name['cloud_control_id']._loaded_options = None
    _globals['_CREATECLOUDCONTROLREQUEST'].fields_by_name['cloud_control_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECLOUDCONTROLREQUEST'].fields_by_name['cloud_control']._loaded_options = None
    _globals['_CREATECLOUDCONTROLREQUEST'].fields_by_name['cloud_control']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECLOUDCONTROLREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECLOUDCONTROLREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATECLOUDCONTROLREQUEST'].fields_by_name['cloud_control']._loaded_options = None
    _globals['_UPDATECLOUDCONTROLREQUEST'].fields_by_name['cloud_control']._serialized_options = b'\xe0A\x02'
    _globals['_DELETECLOUDCONTROLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECLOUDCONTROLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA5\n3cloudsecuritycompliance.googleapis.com/CloudControl'
    _globals['_CONFIG']._loaded_options = None
    _globals['_CONFIG']._serialized_options = b'\xcaA&cloudsecuritycompliance.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CONFIG'].methods_by_name['ListFrameworks']._loaded_options = None
    _globals['_CONFIG'].methods_by_name['ListFrameworks']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1/{parent=organizations/*/locations/*}/frameworks'
    _globals['_CONFIG'].methods_by_name['GetFramework']._loaded_options = None
    _globals['_CONFIG'].methods_by_name['GetFramework']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1/{name=organizations/*/locations/*/frameworks/*}'
    _globals['_CONFIG'].methods_by_name['CreateFramework']._loaded_options = None
    _globals['_CONFIG'].methods_by_name['CreateFramework']._serialized_options = b'\xdaA\x1dparent,framework,framework_id\x82\xd3\xe4\x93\x02@"3/v1/{parent=organizations/*/locations/*}/frameworks:\tframework'
    _globals['_CONFIG'].methods_by_name['UpdateFramework']._loaded_options = None
    _globals['_CONFIG'].methods_by_name['UpdateFramework']._serialized_options = b'\xdaA\x15framework,update_mask\x82\xd3\xe4\x93\x02J2=/v1/{framework.name=organizations/*/locations/*/frameworks/*}:\tframework'
    _globals['_CONFIG'].methods_by_name['DeleteFramework']._loaded_options = None
    _globals['_CONFIG'].methods_by_name['DeleteFramework']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1/{name=organizations/*/locations/*/frameworks/*}'
    _globals['_CONFIG'].methods_by_name['ListCloudControls']._loaded_options = None
    _globals['_CONFIG'].methods_by_name['ListCloudControls']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1/{parent=organizations/*/locations/*}/cloudControls'
    _globals['_CONFIG'].methods_by_name['GetCloudControl']._loaded_options = None
    _globals['_CONFIG'].methods_by_name['GetCloudControl']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1/{name=organizations/*/locations/*/cloudControls/*}'
    _globals['_CONFIG'].methods_by_name['CreateCloudControl']._loaded_options = None
    _globals['_CONFIG'].methods_by_name['CreateCloudControl']._serialized_options = b'\xdaA%parent,cloud_control,cloud_control_id\x82\xd3\xe4\x93\x02G"6/v1/{parent=organizations/*/locations/*}/cloudControls:\rcloud_control'
    _globals['_CONFIG'].methods_by_name['UpdateCloudControl']._loaded_options = None
    _globals['_CONFIG'].methods_by_name['UpdateCloudControl']._serialized_options = b'\xdaA\x19cloud_control,update_mask\x82\xd3\xe4\x93\x02U2D/v1/{cloud_control.name=organizations/*/locations/*/cloudControls/*}:\rcloud_control'
    _globals['_CONFIG'].methods_by_name['DeleteCloudControl']._loaded_options = None
    _globals['_CONFIG'].methods_by_name['DeleteCloudControl']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028*6/v1/{name=organizations/*/locations/*/cloudControls/*}'
    _globals['_LISTFRAMEWORKSREQUEST']._serialized_start = 330
    _globals['_LISTFRAMEWORKSREQUEST']._serialized_end = 476
    _globals['_LISTFRAMEWORKSRESPONSE']._serialized_start = 478
    _globals['_LISTFRAMEWORKSRESPONSE']._serialized_end = 599
    _globals['_GETFRAMEWORKREQUEST']._serialized_start = 601
    _globals['_GETFRAMEWORKREQUEST']._serialized_end = 726
    _globals['_CREATEFRAMEWORKREQUEST']._serialized_start = 729
    _globals['_CREATEFRAMEWORKREQUEST']._serialized_end = 930
    _globals['_UPDATEFRAMEWORKREQUEST']._serialized_start = 933
    _globals['_UPDATEFRAMEWORKREQUEST']._serialized_end = 1119
    _globals['_DELETEFRAMEWORKREQUEST']._serialized_start = 1121
    _globals['_DELETEFRAMEWORKREQUEST']._serialized_end = 1217
    _globals['_LISTCLOUDCONTROLSREQUEST']._serialized_start = 1220
    _globals['_LISTCLOUDCONTROLSREQUEST']._serialized_end = 1372
    _globals['_LISTCLOUDCONTROLSRESPONSE']._serialized_start = 1375
    _globals['_LISTCLOUDCONTROLSRESPONSE']._serialized_end = 1506
    _globals['_GETCLOUDCONTROLREQUEST']._serialized_start = 1508
    _globals['_GETCLOUDCONTROLREQUEST']._serialized_end = 1607
    _globals['_CREATECLOUDCONTROLREQUEST']._serialized_start = 1610
    _globals['_CREATECLOUDCONTROLREQUEST']._serialized_end = 1828
    _globals['_UPDATECLOUDCONTROLREQUEST']._serialized_start = 1831
    _globals['_UPDATECLOUDCONTROLREQUEST']._serialized_end = 1995
    _globals['_DELETECLOUDCONTROLREQUEST']._serialized_start = 1997
    _globals['_DELETECLOUDCONTROLREQUEST']._serialized_end = 2099
    _globals['_CONFIG']._serialized_start = 2102
    _globals['_CONFIG']._serialized_end = 4439