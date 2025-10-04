"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/chat/v1/space_setup.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.chat.v1 import membership_pb2 as google_dot_chat_dot_v1_dot_membership__pb2
from ....google.chat.v1 import space_pb2 as google_dot_chat_dot_v1_dot_space__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n google/chat/v1/space_setup.proto\x12\x0egoogle.chat.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/chat/v1/membership.proto\x1a\x1agoogle/chat/v1/space.proto"\x8d\x01\n\x11SetUpSpaceRequest\x12)\n\x05space\x18\x01 \x01(\x0b2\x15.google.chat.v1.SpaceB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01\x124\n\x0bmemberships\x18\x04 \x03(\x0b2\x1a.google.chat.v1.MembershipB\x03\xe0A\x01B\xa8\x01\n\x12com.google.chat.v1B\x0fSpaceSetupProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.chat.v1.space_setup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x12com.google.chat.v1B\x0fSpaceSetupProtoP\x01Z,cloud.google.com/go/chat/apiv1/chatpb;chatpb\xa2\x02\x0bDYNAPIProto\xaa\x02\x13Google.Apps.Chat.V1\xca\x02\x13Google\\Apps\\Chat\\V1\xea\x02\x16Google::Apps::Chat::V1'
    _globals['_SETUPSPACEREQUEST'].fields_by_name['space']._loaded_options = None
    _globals['_SETUPSPACEREQUEST'].fields_by_name['space']._serialized_options = b'\xe0A\x02'
    _globals['_SETUPSPACEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_SETUPSPACEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_SETUPSPACEREQUEST'].fields_by_name['memberships']._loaded_options = None
    _globals['_SETUPSPACEREQUEST'].fields_by_name['memberships']._serialized_options = b'\xe0A\x01'
    _globals['_SETUPSPACEREQUEST']._serialized_start = 147
    _globals['_SETUPSPACEREQUEST']._serialized_end = 288