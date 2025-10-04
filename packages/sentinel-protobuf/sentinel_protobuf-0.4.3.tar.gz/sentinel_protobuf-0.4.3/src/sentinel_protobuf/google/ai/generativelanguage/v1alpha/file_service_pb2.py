"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ai/generativelanguage/v1alpha/file_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ai.generativelanguage.v1alpha import file_pb2 as google_dot_ai_dot_generativelanguage_dot_v1alpha_dot_file__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/ai/generativelanguage/v1alpha/file_service.proto\x12$google.ai.generativelanguage.v1alpha\x1a/google/ai/generativelanguage/v1alpha/file.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto"R\n\x11CreateFileRequest\x12=\n\x04file\x18\x01 \x01(\x0b2*.google.ai.generativelanguage.v1alpha.FileB\x03\xe0A\x01"N\n\x12CreateFileResponse\x128\n\x04file\x18\x01 \x01(\x0b2*.google.ai.generativelanguage.v1alpha.File"C\n\x10ListFilesRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"g\n\x11ListFilesResponse\x129\n\x05files\x18\x01 \x03(\x0b2*.google.ai.generativelanguage.v1alpha.File\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"N\n\x0eGetFileRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&generativelanguage.googleapis.com/File"Q\n\x11DeleteFileRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&generativelanguage.googleapis.com/File2\x85\x05\n\x0bFileService\x12\x9a\x01\n\nCreateFile\x127.google.ai.generativelanguage.v1alpha.CreateFileRequest\x1a8.google.ai.generativelanguage.v1alpha.CreateFileResponse"\x19\x82\xd3\xe4\x93\x02\x13"\x0e/v1alpha/files:\x01*\x12\x94\x01\n\tListFiles\x126.google.ai.generativelanguage.v1alpha.ListFilesRequest\x1a7.google.ai.generativelanguage.v1alpha.ListFilesResponse"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/v1alpha/files\x12\x93\x01\n\x07GetFile\x124.google.ai.generativelanguage.v1alpha.GetFileRequest\x1a*.google.ai.generativelanguage.v1alpha.File"&\xdaA\x04name\x82\xd3\xe4\x93\x02\x19\x12\x17/v1alpha/{name=files/*}\x12\x85\x01\n\nDeleteFile\x127.google.ai.generativelanguage.v1alpha.DeleteFileRequest\x1a\x16.google.protobuf.Empty"&\xdaA\x04name\x82\xd3\xe4\x93\x02\x19*\x17/v1alpha/{name=files/*}\x1a$\xcaA!generativelanguage.googleapis.comB\x9e\x01\n(com.google.ai.generativelanguage.v1alphaB\x10FileServiceProtoP\x01Z^cloud.google.com/go/ai/generativelanguage/apiv1alpha/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1alpha.file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ai.generativelanguage.v1alphaB\x10FileServiceProtoP\x01Z^cloud.google.com/go/ai/generativelanguage/apiv1alpha/generativelanguagepb;generativelanguagepb'
    _globals['_CREATEFILEREQUEST'].fields_by_name['file']._loaded_options = None
    _globals['_CREATEFILEREQUEST'].fields_by_name['file']._serialized_options = b'\xe0A\x01'
    _globals['_LISTFILESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTFILESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTFILESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTFILESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETFILEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFILEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&generativelanguage.googleapis.com/File'
    _globals['_DELETEFILEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEFILEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&generativelanguage.googleapis.com/File'
    _globals['_FILESERVICE']._loaded_options = None
    _globals['_FILESERVICE']._serialized_options = b'\xcaA!generativelanguage.googleapis.com'
    _globals['_FILESERVICE'].methods_by_name['CreateFile']._loaded_options = None
    _globals['_FILESERVICE'].methods_by_name['CreateFile']._serialized_options = b'\x82\xd3\xe4\x93\x02\x13"\x0e/v1alpha/files:\x01*'
    _globals['_FILESERVICE'].methods_by_name['ListFiles']._loaded_options = None
    _globals['_FILESERVICE'].methods_by_name['ListFiles']._serialized_options = b'\x82\xd3\xe4\x93\x02\x10\x12\x0e/v1alpha/files'
    _globals['_FILESERVICE'].methods_by_name['GetFile']._loaded_options = None
    _globals['_FILESERVICE'].methods_by_name['GetFile']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x19\x12\x17/v1alpha/{name=files/*}'
    _globals['_FILESERVICE'].methods_by_name['DeleteFile']._loaded_options = None
    _globals['_FILESERVICE'].methods_by_name['DeleteFile']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x19*\x17/v1alpha/{name=files/*}'
    _globals['_CREATEFILEREQUEST']._serialized_start = 290
    _globals['_CREATEFILEREQUEST']._serialized_end = 372
    _globals['_CREATEFILERESPONSE']._serialized_start = 374
    _globals['_CREATEFILERESPONSE']._serialized_end = 452
    _globals['_LISTFILESREQUEST']._serialized_start = 454
    _globals['_LISTFILESREQUEST']._serialized_end = 521
    _globals['_LISTFILESRESPONSE']._serialized_start = 523
    _globals['_LISTFILESRESPONSE']._serialized_end = 626
    _globals['_GETFILEREQUEST']._serialized_start = 628
    _globals['_GETFILEREQUEST']._serialized_end = 706
    _globals['_DELETEFILEREQUEST']._serialized_start = 708
    _globals['_DELETEFILEREQUEST']._serialized_end = 789
    _globals['_FILESERVICE']._serialized_start = 792
    _globals['_FILESERVICE']._serialized_end = 1437