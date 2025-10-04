"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/securitycenter/v2/file.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/securitycenter/v2/file.proto\x12\x1egoogle.cloud.securitycenter.v2"\x83\x04\n\x04File\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\x03\x12\x0e\n\x06sha256\x18\x03 \x01(\t\x12\x13\n\x0bhashed_size\x18\x04 \x01(\x03\x12\x18\n\x10partially_hashed\x18\x05 \x01(\x08\x12\x10\n\x08contents\x18\x06 \x01(\t\x12@\n\tdisk_path\x18\x07 \x01(\x0b2-.google.cloud.securitycenter.v2.File.DiskPath\x12F\n\noperations\x18\x08 \x03(\x0b22.google.cloud.securitycenter.v2.File.FileOperation\x1a9\n\x08DiskPath\x12\x16\n\x0epartition_uuid\x18\x01 \x01(\t\x12\x15\n\rrelative_path\x18\x02 \x01(\t\x1a\xc8\x01\n\rFileOperation\x12N\n\x04type\x18\x01 \x01(\x0e2@.google.cloud.securitycenter.v2.File.FileOperation.OperationType"g\n\rOperationType\x12\x1e\n\x1aOPERATION_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04OPEN\x10\x01\x12\x08\n\x04READ\x10\x02\x12\n\n\x06RENAME\x10\x03\x12\t\n\x05WRITE\x10\x04\x12\x0b\n\x07EXECUTE\x10\x05B\xe3\x01\n"com.google.cloud.securitycenter.v2B\tFileProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v2.file_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v2B\tFileProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2'
    _globals['_FILE']._serialized_start = 78
    _globals['_FILE']._serialized_end = 593
    _globals['_FILE_DISKPATH']._serialized_start = 333
    _globals['_FILE_DISKPATH']._serialized_end = 390
    _globals['_FILE_FILEOPERATION']._serialized_start = 393
    _globals['_FILE_FILEOPERATION']._serialized_end = 593
    _globals['_FILE_FILEOPERATION_OPERATIONTYPE']._serialized_start = 490
    _globals['_FILE_FILEOPERATION_OPERATIONTYPE']._serialized_end = 593