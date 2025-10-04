"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/document.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import common_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_common__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/discoveryengine/v1/document.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/discoveryengine/v1/common.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xad\t\n\x08Document\x12.\n\x0bstruct_data\x18\x04 \x01(\x0b2\x17.google.protobuf.StructH\x00\x12\x13\n\tjson_data\x18\x05 \x01(\tH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x0f\n\x02id\x18\x02 \x01(\tB\x03\xe0A\x05\x12\x11\n\tschema_id\x18\x03 \x01(\t\x12B\n\x07content\x18\n \x01(\x0b21.google.cloud.discoveryengine.v1.Document.Content\x12\x1a\n\x12parent_document_id\x18\x07 \x01(\t\x129\n\x13derived_struct_data\x18\x06 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x03\x12C\n\x08acl_info\x18\x0b \x01(\x0b21.google.cloud.discoveryengine.v1.Document.AclInfo\x123\n\nindex_time\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12P\n\x0cindex_status\x18\x0f \x01(\x0b25.google.cloud.discoveryengine.v1.Document.IndexStatusB\x03\xe0A\x03\x1aK\n\x07Content\x12\x13\n\traw_bytes\x18\x02 \x01(\x0cH\x00\x12\r\n\x03uri\x18\x03 \x01(\tH\x00\x12\x11\n\tmime_type\x18\x01 \x01(\tB\t\n\x07content\x1a\xc6\x01\n\x07AclInfo\x12T\n\x07readers\x18\x01 \x03(\x0b2C.google.cloud.discoveryengine.v1.Document.AclInfo.AccessRestriction\x1ae\n\x11AccessRestriction\x12>\n\nprincipals\x18\x01 \x03(\x0b2*.google.cloud.discoveryengine.v1.Principal\x12\x10\n\x08idp_wide\x18\x02 \x01(\x08\x1a\x86\x01\n\x0bIndexStatus\x12.\n\nindex_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12)\n\rerror_samples\x18\x02 \x03(\x0b2\x12.google.rpc.Status\x12\x1c\n\x0fpending_message\x18\x03 \x01(\tB\x03\xe0A\x05:\x96\x02\xeaA\x92\x02\n\'discoveryengine.googleapis.com/Document\x12fprojects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}/documents/{document}\x12\x7fprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}B\x06\n\x04dataB\x80\x02\n#com.google.cloud.discoveryengine.v1B\rDocumentProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.document_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\rDocumentProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_DOCUMENT_INDEXSTATUS'].fields_by_name['pending_message']._loaded_options = None
    _globals['_DOCUMENT_INDEXSTATUS'].fields_by_name['pending_message']._serialized_options = b'\xe0A\x05'
    _globals['_DOCUMENT'].fields_by_name['name']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_DOCUMENT'].fields_by_name['id']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['id']._serialized_options = b'\xe0A\x05'
    _globals['_DOCUMENT'].fields_by_name['derived_struct_data']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['derived_struct_data']._serialized_options = b'\xe0A\x03'
    _globals['_DOCUMENT'].fields_by_name['index_time']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['index_time']._serialized_options = b'\xe0A\x03'
    _globals['_DOCUMENT'].fields_by_name['index_status']._loaded_options = None
    _globals['_DOCUMENT'].fields_by_name['index_status']._serialized_options = b'\xe0A\x03'
    _globals['_DOCUMENT']._loaded_options = None
    _globals['_DOCUMENT']._serialized_options = b"\xeaA\x92\x02\n'discoveryengine.googleapis.com/Document\x12fprojects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}/documents/{document}\x12\x7fprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}"
    _globals['_DOCUMENT']._serialized_start = 278
    _globals['_DOCUMENT']._serialized_end = 1475
    _globals['_DOCUMENT_CONTENT']._serialized_start = 773
    _globals['_DOCUMENT_CONTENT']._serialized_end = 848
    _globals['_DOCUMENT_ACLINFO']._serialized_start = 851
    _globals['_DOCUMENT_ACLINFO']._serialized_end = 1049
    _globals['_DOCUMENT_ACLINFO_ACCESSRESTRICTION']._serialized_start = 948
    _globals['_DOCUMENT_ACLINFO_ACCESSRESTRICTION']._serialized_end = 1049
    _globals['_DOCUMENT_INDEXSTATUS']._serialized_start = 1052
    _globals['_DOCUMENT_INDEXSTATUS']._serialized_end = 1186