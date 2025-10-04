"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/support/v2beta/comment.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.support.v2beta import actor_pb2 as google_dot_cloud_dot_support_dot_v2beta_dot_actor__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/support/v2beta/comment.proto\x12\x1bgoogle.cloud.support.v2beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\'google/cloud/support/v2beta/actor.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xdb\x02\n\x07Comment\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x08\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x128\n\x07creator\x18\x03 \x01(\x0b2".google.cloud.support.v2beta.ActorB\x03\xe0A\x03\x12\x0c\n\x04body\x18\x04 \x01(\t\x12\x1e\n\x0fplain_text_body\x18\x05 \x01(\tB\x05\x18\x01\xe0A\x03:\x9b\x01\xeaA\x97\x01\n#cloudsupport.googleapis.com/Comment\x12<organizations/{organization}/cases/{case}/comments/{comment}\x122projects/{project}/cases/{case}/comments/{comment}B\xc9\x01\n\x1fcom.google.cloud.support.v2betaB\x0cCommentProtoP\x01Z9cloud.google.com/go/support/apiv2beta/supportpb;supportpb\xaa\x02\x1bGoogle.Cloud.Support.V2Beta\xca\x02\x1bGoogle\\Cloud\\Support\\V2beta\xea\x02\x1eGoogle::Cloud::Support::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.support.v2beta.comment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.support.v2betaB\x0cCommentProtoP\x01Z9cloud.google.com/go/support/apiv2beta/supportpb;supportpb\xaa\x02\x1bGoogle.Cloud.Support.V2Beta\xca\x02\x1bGoogle\\Cloud\\Support\\V2beta\xea\x02\x1eGoogle::Cloud::Support::V2beta'
    _globals['_COMMENT'].fields_by_name['name']._loaded_options = None
    _globals['_COMMENT'].fields_by_name['name']._serialized_options = b'\xe0A\x08\xe0A\x03'
    _globals['_COMMENT'].fields_by_name['create_time']._loaded_options = None
    _globals['_COMMENT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_COMMENT'].fields_by_name['creator']._loaded_options = None
    _globals['_COMMENT'].fields_by_name['creator']._serialized_options = b'\xe0A\x03'
    _globals['_COMMENT'].fields_by_name['plain_text_body']._loaded_options = None
    _globals['_COMMENT'].fields_by_name['plain_text_body']._serialized_options = b'\x18\x01\xe0A\x03'
    _globals['_COMMENT']._loaded_options = None
    _globals['_COMMENT']._serialized_options = b'\xeaA\x97\x01\n#cloudsupport.googleapis.com/Comment\x12<organizations/{organization}/cases/{case}/comments/{comment}\x122projects/{project}/cases/{case}/comments/{comment}'
    _globals['_COMMENT']._serialized_start = 209
    _globals['_COMMENT']._serialized_end = 556