"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/support/v2beta/escalation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/support/v2beta/escalation.proto\x12\x1bgoogle.cloud.support.v2beta\x1a\x1fgoogle/api/field_behavior.proto"\xd2\x01\n\nEscalation\x12C\n\x06reason\x18\x04 \x01(\x0e2..google.cloud.support.v2beta.Escalation.ReasonB\x03\xe0A\x02\x12\x1a\n\rjustification\x18\x05 \x01(\tB\x03\xe0A\x02"c\n\x06Reason\x12\x16\n\x12REASON_UNSPECIFIED\x10\x00\x12\x13\n\x0fRESOLUTION_TIME\x10\x01\x12\x17\n\x13TECHNICAL_EXPERTISE\x10\x02\x12\x13\n\x0fBUSINESS_IMPACT\x10\x03B\xcc\x01\n\x1fcom.google.cloud.support.v2betaB\x0fEscalationProtoP\x01Z9cloud.google.com/go/support/apiv2beta/supportpb;supportpb\xaa\x02\x1bGoogle.Cloud.Support.V2Beta\xca\x02\x1bGoogle\\Cloud\\Support\\V2beta\xea\x02\x1eGoogle::Cloud::Support::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.support.v2beta.escalation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.support.v2betaB\x0fEscalationProtoP\x01Z9cloud.google.com/go/support/apiv2beta/supportpb;supportpb\xaa\x02\x1bGoogle.Cloud.Support.V2Beta\xca\x02\x1bGoogle\\Cloud\\Support\\V2beta\xea\x02\x1eGoogle::Cloud::Support::V2beta'
    _globals['_ESCALATION'].fields_by_name['reason']._loaded_options = None
    _globals['_ESCALATION'].fields_by_name['reason']._serialized_options = b'\xe0A\x02'
    _globals['_ESCALATION'].fields_by_name['justification']._loaded_options = None
    _globals['_ESCALATION'].fields_by_name['justification']._serialized_options = b'\xe0A\x02'
    _globals['_ESCALATION']._serialized_start = 111
    _globals['_ESCALATION']._serialized_end = 321
    _globals['_ESCALATION_REASON']._serialized_start = 222
    _globals['_ESCALATION_REASON']._serialized_end = 321