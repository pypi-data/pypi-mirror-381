"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/user_license_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import user_license_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_user__license__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/discoveryengine/v1/user_license_service.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a2google/cloud/discoveryengine/v1/user_license.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xa1\x01\n\x17ListUserLicensesRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/UserStore\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"x\n\x18ListUserLicensesResponse\x12C\n\ruser_licenses\x18\x01 \x03(\x0b2,.google.cloud.discoveryengine.v1.UserLicense\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x92\x03\n\x1eBatchUpdateUserLicensesRequest\x12e\n\rinline_source\x18\x02 \x01(\x0b2L.google.cloud.discoveryengine.v1.BatchUpdateUserLicensesRequest.InlineSourceH\x00\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/UserStore\x12,\n\x1fdelete_unassigned_user_licenses\x18\x04 \x01(\x08B\x03\xe0A\x01\x1a\x8e\x01\n\x0cInlineSource\x12H\n\ruser_licenses\x18\x01 \x03(\x0b2,.google.cloud.discoveryengine.v1.UserLicenseB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01B\x08\n\x06source"\xb1\x01\n\x1fBatchUpdateUserLicensesMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rsuccess_count\x18\x03 \x01(\x03\x12\x15\n\rfailure_count\x18\x04 \x01(\x03"\x91\x01\n\x1fBatchUpdateUserLicensesResponse\x12C\n\ruser_licenses\x18\x01 \x03(\x0b2,.google.cloud.discoveryengine.v1.UserLicense\x12)\n\rerror_samples\x18\x02 \x03(\x0b2\x12.google.rpc.Status2\x9a\x05\n\x12UserLicenseService\x12\xd7\x01\n\x10ListUserLicenses\x128.google.cloud.discoveryengine.v1.ListUserLicensesRequest\x1a9.google.cloud.discoveryengine.v1.ListUserLicensesResponse"N\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1/{parent=projects/*/locations/*/userStores/*}/userLicenses\x12\xd5\x02\n\x17BatchUpdateUserLicenses\x12?.google.cloud.discoveryengine.v1.BatchUpdateUserLicensesRequest\x1a\x1d.google.longrunning.Operation"\xd9\x01\xcaA\x82\x01\n?google.cloud.discoveryengine.v1.BatchUpdateUserLicensesResponse\x12?google.cloud.discoveryengine.v1.BatchUpdateUserLicensesMetadata\x82\xd3\xe4\x93\x02M"H/v1/{parent=projects/*/locations/*/userStores/*}:batchUpdateUserLicenses:\x01*\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x8a\x02\n#com.google.cloud.discoveryengine.v1B\x17UserLicenseServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.user_license_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x17UserLicenseServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_LISTUSERLICENSESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTUSERLICENSESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/UserStore'
    _globals['_LISTUSERLICENSESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTUSERLICENSESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTUSERLICENSESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTUSERLICENSESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTUSERLICENSESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTUSERLICENSESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHUPDATEUSERLICENSESREQUEST_INLINESOURCE'].fields_by_name['user_licenses']._loaded_options = None
    _globals['_BATCHUPDATEUSERLICENSESREQUEST_INLINESOURCE'].fields_by_name['user_licenses']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHUPDATEUSERLICENSESREQUEST_INLINESOURCE'].fields_by_name['update_mask']._loaded_options = None
    _globals['_BATCHUPDATEUSERLICENSESREQUEST_INLINESOURCE'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHUPDATEUSERLICENSESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHUPDATEUSERLICENSESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/UserStore'
    _globals['_BATCHUPDATEUSERLICENSESREQUEST'].fields_by_name['delete_unassigned_user_licenses']._loaded_options = None
    _globals['_BATCHUPDATEUSERLICENSESREQUEST'].fields_by_name['delete_unassigned_user_licenses']._serialized_options = b'\xe0A\x01'
    _globals['_USERLICENSESERVICE']._loaded_options = None
    _globals['_USERLICENSESERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_USERLICENSESERVICE'].methods_by_name['ListUserLicenses']._loaded_options = None
    _globals['_USERLICENSESERVICE'].methods_by_name['ListUserLicenses']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1/{parent=projects/*/locations/*/userStores/*}/userLicenses'
    _globals['_USERLICENSESERVICE'].methods_by_name['BatchUpdateUserLicenses']._loaded_options = None
    _globals['_USERLICENSESERVICE'].methods_by_name['BatchUpdateUserLicenses']._serialized_options = b'\xcaA\x82\x01\n?google.cloud.discoveryengine.v1.BatchUpdateUserLicensesResponse\x12?google.cloud.discoveryengine.v1.BatchUpdateUserLicensesMetadata\x82\xd3\xe4\x93\x02M"H/v1/{parent=projects/*/locations/*/userStores/*}:batchUpdateUserLicenses:\x01*'
    _globals['_LISTUSERLICENSESREQUEST']._serialized_start = 392
    _globals['_LISTUSERLICENSESREQUEST']._serialized_end = 553
    _globals['_LISTUSERLICENSESRESPONSE']._serialized_start = 555
    _globals['_LISTUSERLICENSESRESPONSE']._serialized_end = 675
    _globals['_BATCHUPDATEUSERLICENSESREQUEST']._serialized_start = 678
    _globals['_BATCHUPDATEUSERLICENSESREQUEST']._serialized_end = 1080
    _globals['_BATCHUPDATEUSERLICENSESREQUEST_INLINESOURCE']._serialized_start = 928
    _globals['_BATCHUPDATEUSERLICENSESREQUEST_INLINESOURCE']._serialized_end = 1070
    _globals['_BATCHUPDATEUSERLICENSESMETADATA']._serialized_start = 1083
    _globals['_BATCHUPDATEUSERLICENSESMETADATA']._serialized_end = 1260
    _globals['_BATCHUPDATEUSERLICENSESRESPONSE']._serialized_start = 1263
    _globals['_BATCHUPDATEUSERLICENSESRESPONSE']._serialized_end = 1408
    _globals['_USERLICENSESERVICE']._serialized_start = 1411
    _globals['_USERLICENSESERVICE']._serialized_end = 2077