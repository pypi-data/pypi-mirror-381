"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/services/conversion_adjustment_upload_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.common import offline_user_data_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_offline__user__data__pb2
from ......google.ads.googleads.v20.enums import conversion_adjustment_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_conversion__adjustment__type__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nLgoogle/ads/googleads/v20/services/conversion_adjustment_upload_service.proto\x12!google.ads.googleads.v20.services\x1a7google/ads/googleads/v20/common/offline_user_data.proto\x1a?google/ads/googleads/v20/enums/conversion_adjustment_type.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x17google/rpc/status.proto"\xf6\x01\n"UploadConversionAdjustmentsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\\\n\x16conversion_adjustments\x18\x02 \x03(\x0b27.google.ads.googleads.v20.services.ConversionAdjustmentB\x03\xe0A\x02\x12\x1c\n\x0fpartial_failure\x18\x03 \x01(\x08B\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12\x18\n\x06job_id\x18\x05 \x01(\x05B\x03\xe0A\x01H\x00\x88\x01\x01B\t\n\x07_job_id"\xb8\x01\n#UploadConversionAdjustmentsResponse\x121\n\x15partial_failure_error\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x12N\n\x07results\x18\x02 \x03(\x0b2=.google.ads.googleads.v20.services.ConversionAdjustmentResult\x12\x0e\n\x06job_id\x18\x03 \x01(\x03"\xb3\x04\n\x14ConversionAdjustment\x12R\n\x14gclid_date_time_pair\x18\x0c \x01(\x0b24.google.ads.googleads.v20.services.GclidDateTimePair\x12\x15\n\x08order_id\x18\r \x01(\tH\x00\x88\x01\x01\x12\x1e\n\x11conversion_action\x18\x08 \x01(\tH\x01\x88\x01\x01\x12!\n\x14adjustment_date_time\x18\t \x01(\tH\x02\x88\x01\x01\x12n\n\x0fadjustment_type\x18\x05 \x01(\x0e2U.google.ads.googleads.v20.enums.ConversionAdjustmentTypeEnum.ConversionAdjustmentType\x12N\n\x11restatement_value\x18\x06 \x01(\x0b23.google.ads.googleads.v20.services.RestatementValue\x12I\n\x10user_identifiers\x18\n \x03(\x0b2/.google.ads.googleads.v20.common.UserIdentifier\x12\x17\n\nuser_agent\x18\x0b \x01(\tH\x03\x88\x01\x01B\x0b\n\t_order_idB\x14\n\x12_conversion_actionB\x17\n\x15_adjustment_date_timeB\r\n\x0b_user_agent"p\n\x10RestatementValue\x12\x1b\n\x0eadjusted_value\x18\x03 \x01(\x01H\x00\x88\x01\x01\x12\x1a\n\rcurrency_code\x18\x04 \x01(\tH\x01\x88\x01\x01B\x11\n\x0f_adjusted_valueB\x10\n\x0e_currency_code"m\n\x11GclidDateTimePair\x12\x12\n\x05gclid\x18\x03 \x01(\tH\x00\x88\x01\x01\x12!\n\x14conversion_date_time\x18\x04 \x01(\tH\x01\x88\x01\x01B\x08\n\x06_gclidB\x17\n\x15_conversion_date_time"\xe4\x02\n\x1aConversionAdjustmentResult\x12R\n\x14gclid_date_time_pair\x18\t \x01(\x0b24.google.ads.googleads.v20.services.GclidDateTimePair\x12\x10\n\x08order_id\x18\n \x01(\t\x12\x1e\n\x11conversion_action\x18\x07 \x01(\tH\x00\x88\x01\x01\x12!\n\x14adjustment_date_time\x18\x08 \x01(\tH\x01\x88\x01\x01\x12n\n\x0fadjustment_type\x18\x05 \x01(\x0e2U.google.ads.googleads.v20.enums.ConversionAdjustmentTypeEnum.ConversionAdjustmentTypeB\x14\n\x12_conversion_actionB\x17\n\x15_adjustment_date_time2\x95\x03\n!ConversionAdjustmentUploadService\x12\xa8\x02\n\x1bUploadConversionAdjustments\x12E.google.ads.googleads.v20.services.UploadConversionAdjustmentsRequest\x1aF.google.ads.googleads.v20.services.UploadConversionAdjustmentsResponse"z\xdaA2customer_id,conversion_adjustments,partial_failure\x82\xd3\xe4\x93\x02?":/v20/customers/{customer_id=*}:uploadConversionAdjustments:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x92\x02\n%com.google.ads.googleads.v20.servicesB&ConversionAdjustmentUploadServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.services.conversion_adjustment_upload_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v20.servicesB&ConversionAdjustmentUploadServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Services'
    _globals['_UPLOADCONVERSIONADJUSTMENTSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_UPLOADCONVERSIONADJUSTMENTSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPLOADCONVERSIONADJUSTMENTSREQUEST'].fields_by_name['conversion_adjustments']._loaded_options = None
    _globals['_UPLOADCONVERSIONADJUSTMENTSREQUEST'].fields_by_name['conversion_adjustments']._serialized_options = b'\xe0A\x02'
    _globals['_UPLOADCONVERSIONADJUSTMENTSREQUEST'].fields_by_name['partial_failure']._loaded_options = None
    _globals['_UPLOADCONVERSIONADJUSTMENTSREQUEST'].fields_by_name['partial_failure']._serialized_options = b'\xe0A\x02'
    _globals['_UPLOADCONVERSIONADJUSTMENTSREQUEST'].fields_by_name['job_id']._loaded_options = None
    _globals['_UPLOADCONVERSIONADJUSTMENTSREQUEST'].fields_by_name['job_id']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSIONADJUSTMENTUPLOADSERVICE']._loaded_options = None
    _globals['_CONVERSIONADJUSTMENTUPLOADSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CONVERSIONADJUSTMENTUPLOADSERVICE'].methods_by_name['UploadConversionAdjustments']._loaded_options = None
    _globals['_CONVERSIONADJUSTMENTUPLOADSERVICE'].methods_by_name['UploadConversionAdjustments']._serialized_options = b'\xdaA2customer_id,conversion_adjustments,partial_failure\x82\xd3\xe4\x93\x02?":/v20/customers/{customer_id=*}:uploadConversionAdjustments:\x01*'
    _globals['_UPLOADCONVERSIONADJUSTMENTSREQUEST']._serialized_start = 351
    _globals['_UPLOADCONVERSIONADJUSTMENTSREQUEST']._serialized_end = 597
    _globals['_UPLOADCONVERSIONADJUSTMENTSRESPONSE']._serialized_start = 600
    _globals['_UPLOADCONVERSIONADJUSTMENTSRESPONSE']._serialized_end = 784
    _globals['_CONVERSIONADJUSTMENT']._serialized_start = 787
    _globals['_CONVERSIONADJUSTMENT']._serialized_end = 1350
    _globals['_RESTATEMENTVALUE']._serialized_start = 1352
    _globals['_RESTATEMENTVALUE']._serialized_end = 1464
    _globals['_GCLIDDATETIMEPAIR']._serialized_start = 1466
    _globals['_GCLIDDATETIMEPAIR']._serialized_end = 1575
    _globals['_CONVERSIONADJUSTMENTRESULT']._serialized_start = 1578
    _globals['_CONVERSIONADJUSTMENTRESULT']._serialized_end = 1934
    _globals['_CONVERSIONADJUSTMENTUPLOADSERVICE']._serialized_start = 1937
    _globals['_CONVERSIONADJUSTMENTUPLOADSERVICE']._serialized_end = 2342