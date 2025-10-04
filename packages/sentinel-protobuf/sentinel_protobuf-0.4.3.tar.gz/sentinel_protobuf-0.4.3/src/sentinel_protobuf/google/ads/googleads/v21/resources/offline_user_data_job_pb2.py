"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/offline_user_data_job.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.common import offline_user_data_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_offline__user__data__pb2
from ......google.ads.googleads.v21.enums import offline_user_data_job_failure_reason_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_offline__user__data__job__failure__reason__pb2
from ......google.ads.googleads.v21.enums import offline_user_data_job_match_rate_range_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_offline__user__data__job__match__rate__range__pb2
from ......google.ads.googleads.v21.enums import offline_user_data_job_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_offline__user__data__job__status__pb2
from ......google.ads.googleads.v21.enums import offline_user_data_job_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_offline__user__data__job__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/ads/googleads/v21/resources/offline_user_data_job.proto\x12"google.ads.googleads.v21.resources\x1a7google/ads/googleads/v21/common/offline_user_data.proto\x1aIgoogle/ads/googleads/v21/enums/offline_user_data_job_failure_reason.proto\x1aKgoogle/ads/googleads/v21/enums/offline_user_data_job_match_rate_range.proto\x1aAgoogle/ads/googleads/v21/enums/offline_user_data_job_status.proto\x1a?google/ads/googleads/v21/enums/offline_user_data_job_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xb7\x07\n\x12OfflineUserDataJob\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0A\x05\xfaA-\n+googleads.googleapis.com/OfflineUserDataJob\x12\x14\n\x02id\x18\t \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x1d\n\x0bexternal_id\x18\n \x01(\x03B\x03\xe0A\x05H\x02\x88\x01\x01\x12d\n\x04type\x18\x04 \x01(\x0e2Q.google.ads.googleads.v21.enums.OfflineUserDataJobTypeEnum.OfflineUserDataJobTypeB\x03\xe0A\x05\x12j\n\x06status\x18\x05 \x01(\x0e2U.google.ads.googleads.v21.enums.OfflineUserDataJobStatusEnum.OfflineUserDataJobStatusB\x03\xe0A\x03\x12\x80\x01\n\x0efailure_reason\x18\x06 \x01(\x0e2c.google.ads.googleads.v21.enums.OfflineUserDataJobFailureReasonEnum.OfflineUserDataJobFailureReasonB\x03\xe0A\x03\x12_\n\x12operation_metadata\x18\x0b \x01(\x0b2>.google.ads.googleads.v21.resources.OfflineUserDataJobMetadataB\x03\xe0A\x03\x12p\n!customer_match_user_list_metadata\x18\x07 \x01(\x0b2>.google.ads.googleads.v21.common.CustomerMatchUserListMetadataB\x03\xe0A\x05H\x00\x12X\n\x14store_sales_metadata\x18\x08 \x01(\x0b23.google.ads.googleads.v21.common.StoreSalesMetadataB\x03\xe0A\x05H\x00:{\xeaAx\n+googleads.googleapis.com/OfflineUserDataJob\x12Icustomers/{customer_id}/offlineUserDataJobs/{offline_user_data_update_id}B\n\n\x08metadataB\x05\n\x03_idB\x0e\n\x0c_external_id"\xa3\x01\n\x1aOfflineUserDataJobMetadata\x12\x84\x01\n\x10match_rate_range\x18\x01 \x01(\x0e2e.google.ads.googleads.v21.enums.OfflineUserDataJobMatchRateRangeEnum.OfflineUserDataJobMatchRateRangeB\x03\xe0A\x03B\x89\x02\n&com.google.ads.googleads.v21.resourcesB\x17OfflineUserDataJobProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.offline_user_data_job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\x17OfflineUserDataJobProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_OFFLINEUSERDATAJOB'].fields_by_name['resource_name']._loaded_options = None
    _globals['_OFFLINEUSERDATAJOB'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA-\n+googleads.googleapis.com/OfflineUserDataJob'
    _globals['_OFFLINEUSERDATAJOB'].fields_by_name['id']._loaded_options = None
    _globals['_OFFLINEUSERDATAJOB'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINEUSERDATAJOB'].fields_by_name['external_id']._loaded_options = None
    _globals['_OFFLINEUSERDATAJOB'].fields_by_name['external_id']._serialized_options = b'\xe0A\x05'
    _globals['_OFFLINEUSERDATAJOB'].fields_by_name['type']._loaded_options = None
    _globals['_OFFLINEUSERDATAJOB'].fields_by_name['type']._serialized_options = b'\xe0A\x05'
    _globals['_OFFLINEUSERDATAJOB'].fields_by_name['status']._loaded_options = None
    _globals['_OFFLINEUSERDATAJOB'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINEUSERDATAJOB'].fields_by_name['failure_reason']._loaded_options = None
    _globals['_OFFLINEUSERDATAJOB'].fields_by_name['failure_reason']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINEUSERDATAJOB'].fields_by_name['operation_metadata']._loaded_options = None
    _globals['_OFFLINEUSERDATAJOB'].fields_by_name['operation_metadata']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINEUSERDATAJOB'].fields_by_name['customer_match_user_list_metadata']._loaded_options = None
    _globals['_OFFLINEUSERDATAJOB'].fields_by_name['customer_match_user_list_metadata']._serialized_options = b'\xe0A\x05'
    _globals['_OFFLINEUSERDATAJOB'].fields_by_name['store_sales_metadata']._loaded_options = None
    _globals['_OFFLINEUSERDATAJOB'].fields_by_name['store_sales_metadata']._serialized_options = b'\xe0A\x05'
    _globals['_OFFLINEUSERDATAJOB']._loaded_options = None
    _globals['_OFFLINEUSERDATAJOB']._serialized_options = b'\xeaAx\n+googleads.googleapis.com/OfflineUserDataJob\x12Icustomers/{customer_id}/offlineUserDataJobs/{offline_user_data_update_id}'
    _globals['_OFFLINEUSERDATAJOBMETADATA'].fields_by_name['match_rate_range']._loaded_options = None
    _globals['_OFFLINEUSERDATAJOBMETADATA'].fields_by_name['match_rate_range']._serialized_options = b'\xe0A\x03'
    _globals['_OFFLINEUSERDATAJOB']._serialized_start = 504
    _globals['_OFFLINEUSERDATAJOB']._serialized_end = 1455
    _globals['_OFFLINEUSERDATAJOBMETADATA']._serialized_start = 1458
    _globals['_OFFLINEUSERDATAJOBMETADATA']._serialized_end = 1621