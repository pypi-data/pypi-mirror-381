"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/bytestream/bytestream.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/bytestream/bytestream.proto\x12\x11google.bytestream"M\n\x0bReadRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x13\n\x0bread_offset\x18\x02 \x01(\x03\x12\x12\n\nread_limit\x18\x03 \x01(\x03"\x1c\n\x0cReadResponse\x12\x0c\n\x04data\x18\n \x01(\x0c"_\n\x0cWriteRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t\x12\x14\n\x0cwrite_offset\x18\x02 \x01(\x03\x12\x14\n\x0cfinish_write\x18\x03 \x01(\x08\x12\x0c\n\x04data\x18\n \x01(\x0c"\'\n\rWriteResponse\x12\x16\n\x0ecommitted_size\x18\x01 \x01(\x03"0\n\x17QueryWriteStatusRequest\x12\x15\n\rresource_name\x18\x01 \x01(\t"D\n\x18QueryWriteStatusResponse\x12\x16\n\x0ecommitted_size\x18\x01 \x01(\x03\x12\x10\n\x08complete\x18\x02 \x01(\x082\x92\x02\n\nByteStream\x12I\n\x04Read\x12\x1e.google.bytestream.ReadRequest\x1a\x1f.google.bytestream.ReadResponse0\x01\x12L\n\x05Write\x12\x1f.google.bytestream.WriteRequest\x1a .google.bytestream.WriteResponse(\x01\x12k\n\x10QueryWriteStatus\x12*.google.bytestream.QueryWriteStatusRequest\x1a+.google.bytestream.QueryWriteStatusResponseBe\n\x15com.google.bytestreamB\x0fByteStreamProtoZ;google.golang.org/genproto/googleapis/bytestream;bytestreamb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.bytestream.bytestream_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x15com.google.bytestreamB\x0fByteStreamProtoZ;google.golang.org/genproto/googleapis/bytestream;bytestream'
    _globals['_READREQUEST']._serialized_start = 57
    _globals['_READREQUEST']._serialized_end = 134
    _globals['_READRESPONSE']._serialized_start = 136
    _globals['_READRESPONSE']._serialized_end = 164
    _globals['_WRITEREQUEST']._serialized_start = 166
    _globals['_WRITEREQUEST']._serialized_end = 261
    _globals['_WRITERESPONSE']._serialized_start = 263
    _globals['_WRITERESPONSE']._serialized_end = 302
    _globals['_QUERYWRITESTATUSREQUEST']._serialized_start = 304
    _globals['_QUERYWRITESTATUSREQUEST']._serialized_end = 352
    _globals['_QUERYWRITESTATUSRESPONSE']._serialized_start = 354
    _globals['_QUERYWRITESTATUSRESPONSE']._serialized_end = 422
    _globals['_BYTESTREAM']._serialized_start = 425
    _globals['_BYTESTREAM']._serialized_end = 699