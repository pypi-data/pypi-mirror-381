"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/securitycenter/v2/exfiltration.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/securitycenter/v2/exfiltration.proto\x12\x1egoogle.cloud.securitycenter.v2"\xaf\x01\n\x0cExfiltration\x12>\n\x07sources\x18\x01 \x03(\x0b2-.google.cloud.securitycenter.v2.ExfilResource\x12>\n\x07targets\x18\x02 \x03(\x0b2-.google.cloud.securitycenter.v2.ExfilResource\x12\x1f\n\x17total_exfiltrated_bytes\x18\x03 \x01(\x03"1\n\rExfilResource\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncomponents\x18\x02 \x03(\tB\xeb\x01\n"com.google.cloud.securitycenter.v2B\x11ExfiltrationProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v2.exfiltration_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v2B\x11ExfiltrationProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2'
    _globals['_EXFILTRATION']._serialized_start = 86
    _globals['_EXFILTRATION']._serialized_end = 261
    _globals['_EXFILRESOURCE']._serialized_start = 263
    _globals['_EXFILRESOURCE']._serialized_end = 312