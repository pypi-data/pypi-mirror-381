"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/support/v2beta/email_message.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.support.v2beta import actor_pb2 as google_dot_cloud_dot_support_dot_v2beta_dot_actor__pb2
from .....google.cloud.support.v2beta import content_pb2 as google_dot_cloud_dot_support_dot_v2beta_dot_content__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/support/v2beta/email_message.proto\x12\x1bgoogle.cloud.support.v2beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\'google/cloud/support/v2beta/actor.proto\x1a)google/cloud/support/v2beta/content.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x89\x04\n\x0cEmailMessage\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x126\n\x05actor\x18\x03 \x01(\x0b2".google.cloud.support.v2beta.ActorB\x03\xe0A\x03\x12\x14\n\x07subject\x18\x04 \x01(\tB\x03\xe0A\x03\x12&\n\x19recipient_email_addresses\x18\x05 \x03(\tB\x03\xe0A\x03\x12\x1f\n\x12cc_email_addresses\x18\x06 \x03(\tB\x03\xe0A\x03\x12C\n\x0cbody_content\x18\x08 \x01(\x0b2(.google.cloud.support.v2beta.TextContentB\x03\xe0A\x03:\xd3\x01\xeaA\xcf\x01\n(cloudsupport.googleapis.com/EmailMessage\x12=projects/{project}/cases/{case}/emailMessages/{email_message}\x12Gorganizations/{organization}/cases/{case}/emailMessages/{email_message}*\remailMessages2\x0cemailMessageB\xce\x01\n\x1fcom.google.cloud.support.v2betaB\x11EmailMessageProtoP\x01Z9cloud.google.com/go/support/apiv2beta/supportpb;supportpb\xaa\x02\x1bGoogle.Cloud.Support.V2Beta\xca\x02\x1bGoogle\\Cloud\\Support\\V2beta\xea\x02\x1eGoogle::Cloud::Support::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.support.v2beta.email_message_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.support.v2betaB\x11EmailMessageProtoP\x01Z9cloud.google.com/go/support/apiv2beta/supportpb;supportpb\xaa\x02\x1bGoogle.Cloud.Support.V2Beta\xca\x02\x1bGoogle\\Cloud\\Support\\V2beta\xea\x02\x1eGoogle::Cloud::Support::V2beta'
    _globals['_EMAILMESSAGE'].fields_by_name['name']._loaded_options = None
    _globals['_EMAILMESSAGE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_EMAILMESSAGE'].fields_by_name['create_time']._loaded_options = None
    _globals['_EMAILMESSAGE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_EMAILMESSAGE'].fields_by_name['actor']._loaded_options = None
    _globals['_EMAILMESSAGE'].fields_by_name['actor']._serialized_options = b'\xe0A\x03'
    _globals['_EMAILMESSAGE'].fields_by_name['subject']._loaded_options = None
    _globals['_EMAILMESSAGE'].fields_by_name['subject']._serialized_options = b'\xe0A\x03'
    _globals['_EMAILMESSAGE'].fields_by_name['recipient_email_addresses']._loaded_options = None
    _globals['_EMAILMESSAGE'].fields_by_name['recipient_email_addresses']._serialized_options = b'\xe0A\x03'
    _globals['_EMAILMESSAGE'].fields_by_name['cc_email_addresses']._loaded_options = None
    _globals['_EMAILMESSAGE'].fields_by_name['cc_email_addresses']._serialized_options = b'\xe0A\x03'
    _globals['_EMAILMESSAGE'].fields_by_name['body_content']._loaded_options = None
    _globals['_EMAILMESSAGE'].fields_by_name['body_content']._serialized_options = b'\xe0A\x03'
    _globals['_EMAILMESSAGE']._loaded_options = None
    _globals['_EMAILMESSAGE']._serialized_options = b'\xeaA\xcf\x01\n(cloudsupport.googleapis.com/EmailMessage\x12=projects/{project}/cases/{case}/emailMessages/{email_message}\x12Gorganizations/{organization}/cases/{case}/emailMessages/{email_message}*\remailMessages2\x0cemailMessage'
    _globals['_EMAILMESSAGE']._serialized_start = 258
    _globals['_EMAILMESSAGE']._serialized_end = 779