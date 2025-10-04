"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/contentwarehouse/v1/common.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/contentwarehouse/v1/common.proto\x12 google.cloud.contentwarehouse.v1\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"P\n\x0fRequestMetadata\x12=\n\tuser_info\x18\x01 \x01(\x0b2*.google.cloud.contentwarehouse.v1.UserInfo"&\n\x10ResponseMetadata\x12\x12\n\nrequest_id\x18\x01 \x01(\t")\n\x08UserInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tgroup_ids\x18\x02 \x03(\t"\xd7\x01\n\rUpdateOptions\x12A\n\x0bupdate_type\x18\x01 \x01(\x0e2,.google.cloud.contentwarehouse.v1.UpdateType\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12R\n\x14merge_fields_options\x18\x03 \x01(\x0b24.google.cloud.contentwarehouse.v1.MergeFieldsOptions"\x96\x01\n\x12MergeFieldsOptions\x12#\n\x16replace_message_fields\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12$\n\x17replace_repeated_fields\x18\x02 \x01(\x08H\x01\x88\x01\x01B\x19\n\x17_replace_message_fieldsB\x1a\n\x18_replace_repeated_fields*\x9f\x02\n\nUpdateType\x12\x1b\n\x17UPDATE_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13UPDATE_TYPE_REPLACE\x10\x01\x12\x15\n\x11UPDATE_TYPE_MERGE\x10\x02\x12*\n&UPDATE_TYPE_INSERT_PROPERTIES_BY_NAMES\x10\x03\x12+\n\'UPDATE_TYPE_REPLACE_PROPERTIES_BY_NAMES\x10\x04\x12*\n&UPDATE_TYPE_DELETE_PROPERTIES_BY_NAMES\x10\x05\x12?\n;UPDATE_TYPE_MERGE_AND_REPLACE_OR_INSERT_PROPERTIES_BY_NAMES\x10\x06*S\n\x0cDatabaseType\x12\x0e\n\nDB_UNKNOWN\x10\x00\x12\x14\n\x10DB_INFRA_SPANNER\x10\x01\x12\x1d\n\x15DB_CLOUD_SQL_POSTGRES\x10\x02\x1a\x02\x08\x01*\xaa\x01\n\x11AccessControlMode\x12\x14\n\x10ACL_MODE_UNKNOWN\x10\x00\x12\x1d\n\x19ACL_MODE_UNIVERSAL_ACCESS\x10\x01\x120\n,ACL_MODE_DOCUMENT_LEVEL_ACCESS_CONTROL_BYOID\x10\x02\x12.\n*ACL_MODE_DOCUMENT_LEVEL_ACCESS_CONTROL_GCI\x10\x03*\x89\x01\n\x1aDocumentCreatorDefaultRole\x12-\n)DOCUMENT_CREATOR_DEFAULT_ROLE_UNSPECIFIED\x10\x00\x12\x12\n\x0eDOCUMENT_ADMIN\x10\x01\x12\x13\n\x0fDOCUMENT_EDITOR\x10\x02\x12\x13\n\x0fDOCUMENT_VIEWER\x10\x03B\xc9\x02\n$com.google.cloud.contentwarehouse.v1B\x0bCommonProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1\xeaAS\n(contentwarehouse.googleapis.com/Location\x12\'projects/{project}/locations/{location}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.contentwarehouse.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n$com.google.cloud.contentwarehouse.v1B\x0bCommonProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1\xeaAS\n(contentwarehouse.googleapis.com/Location\x12'projects/{project}/locations/{location}"
    _globals['_DATABASETYPE'].values_by_name['DB_CLOUD_SQL_POSTGRES']._loaded_options = None
    _globals['_DATABASETYPE'].values_by_name['DB_CLOUD_SQL_POSTGRES']._serialized_options = b'\x08\x01'
    _globals['_UPDATETYPE']._serialized_start = 681
    _globals['_UPDATETYPE']._serialized_end = 968
    _globals['_DATABASETYPE']._serialized_start = 970
    _globals['_DATABASETYPE']._serialized_end = 1053
    _globals['_ACCESSCONTROLMODE']._serialized_start = 1056
    _globals['_ACCESSCONTROLMODE']._serialized_end = 1226
    _globals['_DOCUMENTCREATORDEFAULTROLE']._serialized_start = 1229
    _globals['_DOCUMENTCREATORDEFAULTROLE']._serialized_end = 1366
    _globals['_REQUESTMETADATA']._serialized_start = 144
    _globals['_REQUESTMETADATA']._serialized_end = 224
    _globals['_RESPONSEMETADATA']._serialized_start = 226
    _globals['_RESPONSEMETADATA']._serialized_end = 264
    _globals['_USERINFO']._serialized_start = 266
    _globals['_USERINFO']._serialized_end = 307
    _globals['_UPDATEOPTIONS']._serialized_start = 310
    _globals['_UPDATEOPTIONS']._serialized_end = 525
    _globals['_MERGEFIELDSOPTIONS']._serialized_start = 528
    _globals['_MERGEFIELDSOPTIONS']._serialized_end = 678