"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/services/offline_user_data_job_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.common import offline_user_data_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_offline__user__data__pb2
from ......google.ads.googleads.v20.resources import offline_user_data_job_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_resources_dot_offline__user__data__job__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/ads/googleads/v20/services/offline_user_data_job_service.proto\x12!google.ads.googleads.v20.services\x1a7google/ads/googleads/v20/common/offline_user_data.proto\x1a>google/ads/googleads/v20/resources/offline_user_data_job.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x17google/rpc/status.proto"\xc5\x01\n\x1fCreateOfflineUserDataJobRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12H\n\x03job\x18\x02 \x01(\x0b26.google.ads.googleads.v20.resources.OfflineUserDataJobB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08\x12\'\n\x1fenable_match_rate_range_preview\x18\x05 \x01(\x08"k\n CreateOfflineUserDataJobResponse\x12G\n\rresource_name\x18\x01 \x01(\tB0\xfaA-\n+googleads.googleapis.com/OfflineUserDataJob"\x81\x01\n\x1cRunOfflineUserDataJobRequest\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+googleads.googleapis.com/OfflineUserDataJob\x12\x15\n\rvalidate_only\x18\x02 \x01(\x08"\xd6\x02\n&AddOfflineUserDataJobOperationsRequest\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+googleads.googleapis.com/OfflineUserDataJob\x12#\n\x16enable_partial_failure\x18\x04 \x01(\x08H\x00\x88\x01\x01\x12\x1c\n\x0fenable_warnings\x18\x06 \x01(\x08H\x01\x88\x01\x01\x12W\n\noperations\x18\x03 \x03(\x0b2>.google.ads.googleads.v20.services.OfflineUserDataJobOperationB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x05 \x01(\x08B\x19\n\x17_enable_partial_failureB\x12\n\x10_enable_warnings"\xba\x01\n\x1bOfflineUserDataJobOperation\x12;\n\x06create\x18\x01 \x01(\x0b2).google.ads.googleads.v20.common.UserDataH\x00\x12;\n\x06remove\x18\x02 \x01(\x0b2).google.ads.googleads.v20.common.UserDataH\x00\x12\x14\n\nremove_all\x18\x03 \x01(\x08H\x00B\x0b\n\toperation"\x81\x01\n\'AddOfflineUserDataJobOperationsResponse\x121\n\x15partial_failure_error\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x12#\n\x07warning\x18\x02 \x01(\x0b2\x12.google.rpc.Status2\xb2\x07\n\x19OfflineUserDataJobService\x12\xfb\x01\n\x18CreateOfflineUserDataJob\x12B.google.ads.googleads.v20.services.CreateOfflineUserDataJobRequest\x1aC.google.ads.googleads.v20.services.CreateOfflineUserDataJobResponse"V\xdaA\x0fcustomer_id,job\x82\xd3\xe4\x93\x02>"9/v20/customers/{customer_id=*}/offlineUserDataJobs:create:\x01*\x12\xa4\x02\n\x1fAddOfflineUserDataJobOperations\x12I.google.ads.googleads.v20.services.AddOfflineUserDataJobOperationsRequest\x1aJ.google.ads.googleads.v20.services.AddOfflineUserDataJobOperationsResponse"j\xdaA\x18resource_name,operations\x82\xd3\xe4\x93\x02I"D/v20/{resource_name=customers/*/offlineUserDataJobs/*}:addOperations:\x01*\x12\xa8\x02\n\x15RunOfflineUserDataJob\x12?.google.ads.googleads.v20.services.RunOfflineUserDataJobRequest\x1a\x1d.google.longrunning.Operation"\xae\x01\xcaAV\n\x15google.protobuf.Empty\x12=google.ads.googleads.v20.resources.OfflineUserDataJobMetadata\xdaA\rresource_name\x82\xd3\xe4\x93\x02?":/v20/{resource_name=customers/*/offlineUserDataJobs/*}:run:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8a\x02\n%com.google.ads.googleads.v20.servicesB\x1eOfflineUserDataJobServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.services.offline_user_data_job_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v20.servicesB\x1eOfflineUserDataJobServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Services'
    _globals['_CREATEOFFLINEUSERDATAJOBREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_CREATEOFFLINEUSERDATAJOBREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEOFFLINEUSERDATAJOBREQUEST'].fields_by_name['job']._loaded_options = None
    _globals['_CREATEOFFLINEUSERDATAJOBREQUEST'].fields_by_name['job']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEOFFLINEUSERDATAJOBRESPONSE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CREATEOFFLINEUSERDATAJOBRESPONSE'].fields_by_name['resource_name']._serialized_options = b'\xfaA-\n+googleads.googleapis.com/OfflineUserDataJob'
    _globals['_RUNOFFLINEUSERDATAJOBREQUEST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_RUNOFFLINEUSERDATAJOBREQUEST'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x02\xfaA-\n+googleads.googleapis.com/OfflineUserDataJob'
    _globals['_ADDOFFLINEUSERDATAJOBOPERATIONSREQUEST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADDOFFLINEUSERDATAJOBOPERATIONSREQUEST'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x02\xfaA-\n+googleads.googleapis.com/OfflineUserDataJob'
    _globals['_ADDOFFLINEUSERDATAJOBOPERATIONSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_ADDOFFLINEUSERDATAJOBOPERATIONSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_OFFLINEUSERDATAJOBSERVICE']._loaded_options = None
    _globals['_OFFLINEUSERDATAJOBSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_OFFLINEUSERDATAJOBSERVICE'].methods_by_name['CreateOfflineUserDataJob']._loaded_options = None
    _globals['_OFFLINEUSERDATAJOBSERVICE'].methods_by_name['CreateOfflineUserDataJob']._serialized_options = b'\xdaA\x0fcustomer_id,job\x82\xd3\xe4\x93\x02>"9/v20/customers/{customer_id=*}/offlineUserDataJobs:create:\x01*'
    _globals['_OFFLINEUSERDATAJOBSERVICE'].methods_by_name['AddOfflineUserDataJobOperations']._loaded_options = None
    _globals['_OFFLINEUSERDATAJOBSERVICE'].methods_by_name['AddOfflineUserDataJobOperations']._serialized_options = b'\xdaA\x18resource_name,operations\x82\xd3\xe4\x93\x02I"D/v20/{resource_name=customers/*/offlineUserDataJobs/*}:addOperations:\x01*'
    _globals['_OFFLINEUSERDATAJOBSERVICE'].methods_by_name['RunOfflineUserDataJob']._loaded_options = None
    _globals['_OFFLINEUSERDATAJOBSERVICE'].methods_by_name['RunOfflineUserDataJob']._serialized_options = b'\xcaAV\n\x15google.protobuf.Empty\x12=google.ads.googleads.v20.resources.OfflineUserDataJobMetadata\xdaA\rresource_name\x82\xd3\xe4\x93\x02?":/v20/{resource_name=customers/*/offlineUserDataJobs/*}:run:\x01*'
    _globals['_CREATEOFFLINEUSERDATAJOBREQUEST']._serialized_start = 436
    _globals['_CREATEOFFLINEUSERDATAJOBREQUEST']._serialized_end = 633
    _globals['_CREATEOFFLINEUSERDATAJOBRESPONSE']._serialized_start = 635
    _globals['_CREATEOFFLINEUSERDATAJOBRESPONSE']._serialized_end = 742
    _globals['_RUNOFFLINEUSERDATAJOBREQUEST']._serialized_start = 745
    _globals['_RUNOFFLINEUSERDATAJOBREQUEST']._serialized_end = 874
    _globals['_ADDOFFLINEUSERDATAJOBOPERATIONSREQUEST']._serialized_start = 877
    _globals['_ADDOFFLINEUSERDATAJOBOPERATIONSREQUEST']._serialized_end = 1219
    _globals['_OFFLINEUSERDATAJOBOPERATION']._serialized_start = 1222
    _globals['_OFFLINEUSERDATAJOBOPERATION']._serialized_end = 1408
    _globals['_ADDOFFLINEUSERDATAJOBOPERATIONSRESPONSE']._serialized_start = 1411
    _globals['_ADDOFFLINEUSERDATAJOBOPERATIONSRESPONSE']._serialized_end = 1540
    _globals['_OFFLINEUSERDATAJOBSERVICE']._serialized_start = 1543
    _globals['_OFFLINEUSERDATAJOBSERVICE']._serialized_end = 2489