"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/api/policy.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17google/api/policy.proto\x12\ngoogle.api\x1a google/protobuf/descriptor.proto"S\n\x0bFieldPolicy\x12\x10\n\x08selector\x18\x01 \x01(\t\x12\x1b\n\x13resource_permission\x18\x02 \x01(\t\x12\x15\n\rresource_type\x18\x03 \x01(\t"S\n\x0cMethodPolicy\x12\x10\n\x08selector\x18\t \x01(\t\x121\n\x10request_policies\x18\x02 \x03(\x0b2\x17.google.api.FieldPolicy:O\n\x0cfield_policy\x12\x1d.google.protobuf.FieldOptions\x18\xe8\xce\xc1K \x01(\x0b2\x17.google.api.FieldPolicy:R\n\rmethod_policy\x12\x1e.google.protobuf.MethodOptions\x18\xb5\x97\x99M \x01(\x0b2\x18.google.api.MethodPolicyBm\n\x0ecom.google.apiB\x0bPolicyProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPIb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.policy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x0ecom.google.apiB\x0bPolicyProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPI'
    _globals['_FIELDPOLICY']._serialized_start = 73
    _globals['_FIELDPOLICY']._serialized_end = 156
    _globals['_METHODPOLICY']._serialized_start = 158
    _globals['_METHODPOLICY']._serialized_end = 241