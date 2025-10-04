"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/securitycenter/v1p1beta1/finding.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.securitycenter.v1p1beta1 import security_marks_pb2 as google_dot_cloud_dot_securitycenter_dot_v1p1beta1_dot_security__marks__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/securitycenter/v1p1beta1/finding.proto\x12%google.cloud.securitycenter.v1p1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a:google/cloud/securitycenter/v1p1beta1/security_marks.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xdf\x07\n\x07Finding\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06parent\x18\x02 \x01(\t\x12\x15\n\rresource_name\x18\x03 \x01(\t\x12C\n\x05state\x18\x04 \x01(\x0e24.google.cloud.securitycenter.v1p1beta1.Finding.State\x12\x10\n\x08category\x18\x05 \x01(\t\x12\x14\n\x0cexternal_uri\x18\x06 \x01(\t\x12_\n\x11source_properties\x18\x07 \x03(\x0b2D.google.cloud.securitycenter.v1p1beta1.Finding.SourcePropertiesEntry\x12Q\n\x0esecurity_marks\x18\x08 \x01(\x0b24.google.cloud.securitycenter.v1p1beta1.SecurityMarksB\x03\xe0A\x03\x12.\n\nevent_time\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bcreate_time\x18\n \x01(\x0b2\x1a.google.protobuf.Timestamp\x12I\n\x08severity\x18\r \x01(\x0e27.google.cloud.securitycenter.v1p1beta1.Finding.Severity\x12\x16\n\x0ecanonical_name\x18\x0e \x01(\t\x1aO\n\x15SourcePropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x01"8\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x0c\n\x08INACTIVE\x10\x02"Q\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x0c\n\x08CRITICAL\x10\x01\x12\x08\n\x04HIGH\x10\x02\x12\n\n\x06MEDIUM\x10\x03\x12\x07\n\x03LOW\x10\x04:\xdb\x01\xeaA\xd7\x01\n%securitycenter.googleapis.com/Finding\x12@organizations/{organization}/sources/{source}/findings/{finding}\x124folders/{folder}/sources/{source}/findings/{finding}\x126projects/{project}/sources/{source}/findings/{finding}B\xfb\x01\n)com.google.cloud.securitycenter.v1p1beta1P\x01ZQcloud.google.com/go/securitycenter/apiv1p1beta1/securitycenterpb;securitycenterpb\xaa\x02%Google.Cloud.SecurityCenter.V1P1Beta1\xca\x02%Google\\Cloud\\SecurityCenter\\V1p1beta1\xea\x02(Google::Cloud::SecurityCenter::V1p1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1p1beta1.finding_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.securitycenter.v1p1beta1P\x01ZQcloud.google.com/go/securitycenter/apiv1p1beta1/securitycenterpb;securitycenterpb\xaa\x02%Google.Cloud.SecurityCenter.V1P1Beta1\xca\x02%Google\\Cloud\\SecurityCenter\\V1p1beta1\xea\x02(Google::Cloud::SecurityCenter::V1p1beta1'
    _globals['_FINDING_SOURCEPROPERTIESENTRY']._loaded_options = None
    _globals['_FINDING_SOURCEPROPERTIESENTRY']._serialized_options = b'8\x01'
    _globals['_FINDING'].fields_by_name['security_marks']._loaded_options = None
    _globals['_FINDING'].fields_by_name['security_marks']._serialized_options = b'\xe0A\x03'
    _globals['_FINDING']._loaded_options = None
    _globals['_FINDING']._serialized_options = b'\xeaA\xd7\x01\n%securitycenter.googleapis.com/Finding\x12@organizations/{organization}/sources/{source}/findings/{finding}\x124folders/{folder}/sources/{source}/findings/{finding}\x126projects/{project}/sources/{source}/findings/{finding}'
    _globals['_FINDING']._serialized_start = 278
    _globals['_FINDING']._serialized_end = 1269
    _globals['_FINDING_SOURCEPROPERTIESENTRY']._serialized_start = 827
    _globals['_FINDING_SOURCEPROPERTIESENTRY']._serialized_end = 906
    _globals['_FINDING_STATE']._serialized_start = 908
    _globals['_FINDING_STATE']._serialized_end = 964
    _globals['_FINDING_SEVERITY']._serialized_start = 966
    _globals['_FINDING_SEVERITY']._serialized_end = 1047