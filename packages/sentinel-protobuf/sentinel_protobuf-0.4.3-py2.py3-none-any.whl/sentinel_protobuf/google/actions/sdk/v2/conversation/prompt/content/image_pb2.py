"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/actions/sdk/v2/conversation/prompt/content/image.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/actions/sdk/v2/conversation/prompt/content/image.proto\x12"google.actions.sdk.v2.conversation"\x80\x01\n\x05Image\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0b\n\x03alt\x18\x02 \x01(\t\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\r\n\x05width\x18\x04 \x01(\x05">\n\tImageFill\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x08\n\x04GRAY\x10\x01\x12\t\n\x05WHITE\x10\x02\x12\x0b\n\x07CROPPED\x10\x03B\x86\x01\n&com.google.actions.sdk.v2.conversationB\nImageProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversationb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.actions.sdk.v2.conversation.prompt.content.image_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.actions.sdk.v2.conversationB\nImageProtoP\x01ZNgoogle.golang.org/genproto/googleapis/actions/sdk/v2/conversation;conversation'
    _globals['_IMAGE']._serialized_start = 102
    _globals['_IMAGE']._serialized_end = 230
    _globals['_IMAGE_IMAGEFILL']._serialized_start = 168
    _globals['_IMAGE_IMAGEFILL']._serialized_end = 230