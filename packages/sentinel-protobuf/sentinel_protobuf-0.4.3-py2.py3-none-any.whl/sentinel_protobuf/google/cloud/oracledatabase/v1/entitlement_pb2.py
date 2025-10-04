"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/oracledatabase/v1/entitlement.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/oracledatabase/v1/entitlement.proto\x12\x1egoogle.cloud.oracledatabase.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x86\x04\n\x0bEntitlement\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12R\n\x15cloud_account_details\x18\x02 \x01(\x0b23.google.cloud.oracledatabase.v1.CloudAccountDetails\x12\x1b\n\x0eentitlement_id\x18\x03 \x01(\tB\x03\xe0A\x03\x12E\n\x05state\x18\x04 \x01(\x0e21.google.cloud.oracledatabase.v1.Entitlement.StateB\x03\xe0A\x03"\x9a\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x16\n\x12ACCOUNT_NOT_LINKED\x10\x01\x12\x16\n\x12ACCOUNT_NOT_ACTIVE\x10\x02\x12\n\n\x06ACTIVE\x10\x03\x12\x15\n\x11ACCOUNT_SUSPENDED\x10\x04\x12\'\n#NOT_APPROVED_IN_PRIVATE_MARKETPLACE\x10\x05:\x8e\x01\xeaA\x8a\x01\n)oracledatabase.googleapis.com/Entitlement\x12Bprojects/{project}/locations/{location}/entitlements/{entitlement}*\x0centitlements2\x0bentitlement"\xe5\x01\n\x13CloudAccountDetails\x12\x1a\n\rcloud_account\x18\x01 \x01(\tB\x03\xe0A\x03\x12&\n\x19cloud_account_home_region\x18\x02 \x01(\tB\x03\xe0A\x03\x12+\n\x19link_existing_account_uri\x18\x03 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12&\n\x14account_creation_uri\x18\x04 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01B\x1c\n\x1a_link_existing_account_uriB\x17\n\x15_account_creation_uriB\xea\x01\n"com.google.cloud.oracledatabase.v1B\x10EntitlementProtoP\x01ZJcloud.google.com/go/oracledatabase/apiv1/oracledatabasepb;oracledatabasepb\xaa\x02\x1eGoogle.Cloud.OracleDatabase.V1\xca\x02\x1eGoogle\\Cloud\\OracleDatabase\\V1\xea\x02!Google::Cloud::OracleDatabase::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.oracledatabase.v1.entitlement_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.oracledatabase.v1B\x10EntitlementProtoP\x01ZJcloud.google.com/go/oracledatabase/apiv1/oracledatabasepb;oracledatabasepb\xaa\x02\x1eGoogle.Cloud.OracleDatabase.V1\xca\x02\x1eGoogle\\Cloud\\OracleDatabase\\V1\xea\x02!Google::Cloud::OracleDatabase::V1'
    _globals['_ENTITLEMENT'].fields_by_name['name']._loaded_options = None
    _globals['_ENTITLEMENT'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ENTITLEMENT'].fields_by_name['entitlement_id']._loaded_options = None
    _globals['_ENTITLEMENT'].fields_by_name['entitlement_id']._serialized_options = b'\xe0A\x03'
    _globals['_ENTITLEMENT'].fields_by_name['state']._loaded_options = None
    _globals['_ENTITLEMENT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_ENTITLEMENT']._loaded_options = None
    _globals['_ENTITLEMENT']._serialized_options = b'\xeaA\x8a\x01\n)oracledatabase.googleapis.com/Entitlement\x12Bprojects/{project}/locations/{location}/entitlements/{entitlement}*\x0centitlements2\x0bentitlement'
    _globals['_CLOUDACCOUNTDETAILS'].fields_by_name['cloud_account']._loaded_options = None
    _globals['_CLOUDACCOUNTDETAILS'].fields_by_name['cloud_account']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDACCOUNTDETAILS'].fields_by_name['cloud_account_home_region']._loaded_options = None
    _globals['_CLOUDACCOUNTDETAILS'].fields_by_name['cloud_account_home_region']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDACCOUNTDETAILS'].fields_by_name['link_existing_account_uri']._loaded_options = None
    _globals['_CLOUDACCOUNTDETAILS'].fields_by_name['link_existing_account_uri']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDACCOUNTDETAILS'].fields_by_name['account_creation_uri']._loaded_options = None
    _globals['_CLOUDACCOUNTDETAILS'].fields_by_name['account_creation_uri']._serialized_options = b'\xe0A\x03'
    _globals['_ENTITLEMENT']._serialized_start = 145
    _globals['_ENTITLEMENT']._serialized_end = 663
    _globals['_ENTITLEMENT_STATE']._serialized_start = 364
    _globals['_ENTITLEMENT_STATE']._serialized_end = 518
    _globals['_CLOUDACCOUNTDETAILS']._serialized_start = 666
    _globals['_CLOUDACCOUNTDETAILS']._serialized_end = 895