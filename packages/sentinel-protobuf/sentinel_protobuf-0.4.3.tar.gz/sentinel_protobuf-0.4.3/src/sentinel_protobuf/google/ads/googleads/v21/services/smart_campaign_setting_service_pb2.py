"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/services/smart_campaign_setting_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v21.enums import smart_campaign_not_eligible_reason_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_smart__campaign__not__eligible__reason__pb2
from ......google.ads.googleads.v21.enums import smart_campaign_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_smart__campaign__status__pb2
from ......google.ads.googleads.v21.resources import smart_campaign_setting_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_smart__campaign__setting__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFgoogle/ads/googleads/v21/services/smart_campaign_setting_service.proto\x12!google.ads.googleads.v21.services\x1a:google/ads/googleads/v21/enums/response_content_type.proto\x1aGgoogle/ads/googleads/v21/enums/smart_campaign_not_eligible_reason.proto\x1a:google/ads/googleads/v21/enums/smart_campaign_status.proto\x1a?google/ads/googleads/v21/resources/smart_campaign_setting.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"m\n\x1dGetSmartCampaignStatusRequest\x12L\n\rresource_name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-googleads.googleapis.com/SmartCampaignSetting"\xbf\x01\n\x1fSmartCampaignNotEligibleDetails\x12\x83\x01\n\x13not_eligible_reason\x18\x01 \x01(\x0e2a.google.ads.googleads.v21.enums.SmartCampaignNotEligibleReasonEnum.SmartCampaignNotEligibleReasonH\x00\x88\x01\x01B\x16\n\x14_not_eligible_reason"\x92\x01\n\x1cSmartCampaignEligibleDetails\x12&\n\x19last_impression_date_time\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rend_date_time\x18\x02 \x01(\tH\x01\x88\x01\x01B\x1c\n\x1a_last_impression_date_timeB\x10\n\x0e_end_date_time"P\n\x1aSmartCampaignPausedDetails\x12\x1d\n\x10paused_date_time\x18\x01 \x01(\tH\x00\x88\x01\x01B\x13\n\x11_paused_date_time"S\n\x1bSmartCampaignRemovedDetails\x12\x1e\n\x11removed_date_time\x18\x01 \x01(\tH\x00\x88\x01\x01B\x14\n\x12_removed_date_time"I\n\x19SmartCampaignEndedDetails\x12\x1a\n\rend_date_time\x18\x01 \x01(\tH\x00\x88\x01\x01B\x10\n\x0e_end_date_time"\xf9\x04\n\x1eGetSmartCampaignStatusResponse\x12j\n\x15smart_campaign_status\x18\x01 \x01(\x0e2K.google.ads.googleads.v21.enums.SmartCampaignStatusEnum.SmartCampaignStatus\x12b\n\x14not_eligible_details\x18\x02 \x01(\x0b2B.google.ads.googleads.v21.services.SmartCampaignNotEligibleDetailsH\x00\x12[\n\x10eligible_details\x18\x03 \x01(\x0b2?.google.ads.googleads.v21.services.SmartCampaignEligibleDetailsH\x00\x12W\n\x0epaused_details\x18\x04 \x01(\x0b2=.google.ads.googleads.v21.services.SmartCampaignPausedDetailsH\x00\x12Y\n\x0fremoved_details\x18\x05 \x01(\x0b2>.google.ads.googleads.v21.services.SmartCampaignRemovedDetailsH\x00\x12U\n\rended_details\x18\x06 \x01(\x0b2<.google.ads.googleads.v21.services.SmartCampaignEndedDetailsH\x00B\x1f\n\x1dsmart_campaign_status_details"\xb5\x02\n"MutateSmartCampaignSettingsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12Y\n\noperations\x18\x02 \x03(\x0b2@.google.ads.googleads.v21.services.SmartCampaignSettingOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v21.enums.ResponseContentTypeEnum.ResponseContentType"\x9a\x01\n\x1dSmartCampaignSettingOperation\x12H\n\x06update\x18\x01 \x01(\x0b28.google.ads.googleads.v21.resources.SmartCampaignSetting\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xae\x01\n#MutateSmartCampaignSettingsResponse\x121\n\x15partial_failure_error\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x12T\n\x07results\x18\x02 \x03(\x0b2C.google.ads.googleads.v21.services.MutateSmartCampaignSettingResult"\xc7\x01\n MutateSmartCampaignSettingResult\x12I\n\rresource_name\x18\x01 \x01(\tB2\xfaA/\n-googleads.googleapis.com/SmartCampaignSetting\x12X\n\x16smart_campaign_setting\x18\x02 \x01(\x0b28.google.ads.googleads.v21.resources.SmartCampaignSetting2\xfd\x04\n\x1bSmartCampaignSettingService\x12\x86\x02\n\x16GetSmartCampaignStatus\x12@.google.ads.googleads.v21.services.GetSmartCampaignStatusRequest\x1aA.google.ads.googleads.v21.services.GetSmartCampaignStatusResponse"g\xdaA\rresource_name\x82\xd3\xe4\x93\x02Q\x12O/v21/{resource_name=customers/*/smartCampaignSettings/*}:getSmartCampaignStatus\x12\x8d\x02\n\x1bMutateSmartCampaignSettings\x12E.google.ads.googleads.v21.services.MutateSmartCampaignSettingsRequest\x1aF.google.ads.googleads.v21.services.MutateSmartCampaignSettingsResponse"_\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02@";/v21/customers/{customer_id=*}/smartCampaignSettings:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8c\x02\n%com.google.ads.googleads.v21.servicesB SmartCampaignSettingServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.services.smart_campaign_setting_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v21.servicesB SmartCampaignSettingServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Services'
    _globals['_GETSMARTCAMPAIGNSTATUSREQUEST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_GETSMARTCAMPAIGNSTATUSREQUEST'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x02\xfaA/\n-googleads.googleapis.com/SmartCampaignSetting'
    _globals['_MUTATESMARTCAMPAIGNSETTINGSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATESMARTCAMPAIGNSETTINGSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATESMARTCAMPAIGNSETTINGSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATESMARTCAMPAIGNSETTINGSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATESMARTCAMPAIGNSETTINGRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATESMARTCAMPAIGNSETTINGRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA/\n-googleads.googleapis.com/SmartCampaignSetting'
    _globals['_SMARTCAMPAIGNSETTINGSERVICE']._loaded_options = None
    _globals['_SMARTCAMPAIGNSETTINGSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_SMARTCAMPAIGNSETTINGSERVICE'].methods_by_name['GetSmartCampaignStatus']._loaded_options = None
    _globals['_SMARTCAMPAIGNSETTINGSERVICE'].methods_by_name['GetSmartCampaignStatus']._serialized_options = b'\xdaA\rresource_name\x82\xd3\xe4\x93\x02Q\x12O/v21/{resource_name=customers/*/smartCampaignSettings/*}:getSmartCampaignStatus'
    _globals['_SMARTCAMPAIGNSETTINGSERVICE'].methods_by_name['MutateSmartCampaignSettings']._loaded_options = None
    _globals['_SMARTCAMPAIGNSETTINGSERVICE'].methods_by_name['MutateSmartCampaignSettings']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02@";/v21/customers/{customer_id=*}/smartCampaignSettings:mutate:\x01*'
    _globals['_GETSMARTCAMPAIGNSTATUSREQUEST']._serialized_start = 541
    _globals['_GETSMARTCAMPAIGNSTATUSREQUEST']._serialized_end = 650
    _globals['_SMARTCAMPAIGNNOTELIGIBLEDETAILS']._serialized_start = 653
    _globals['_SMARTCAMPAIGNNOTELIGIBLEDETAILS']._serialized_end = 844
    _globals['_SMARTCAMPAIGNELIGIBLEDETAILS']._serialized_start = 847
    _globals['_SMARTCAMPAIGNELIGIBLEDETAILS']._serialized_end = 993
    _globals['_SMARTCAMPAIGNPAUSEDDETAILS']._serialized_start = 995
    _globals['_SMARTCAMPAIGNPAUSEDDETAILS']._serialized_end = 1075
    _globals['_SMARTCAMPAIGNREMOVEDDETAILS']._serialized_start = 1077
    _globals['_SMARTCAMPAIGNREMOVEDDETAILS']._serialized_end = 1160
    _globals['_SMARTCAMPAIGNENDEDDETAILS']._serialized_start = 1162
    _globals['_SMARTCAMPAIGNENDEDDETAILS']._serialized_end = 1235
    _globals['_GETSMARTCAMPAIGNSTATUSRESPONSE']._serialized_start = 1238
    _globals['_GETSMARTCAMPAIGNSTATUSRESPONSE']._serialized_end = 1871
    _globals['_MUTATESMARTCAMPAIGNSETTINGSREQUEST']._serialized_start = 1874
    _globals['_MUTATESMARTCAMPAIGNSETTINGSREQUEST']._serialized_end = 2183
    _globals['_SMARTCAMPAIGNSETTINGOPERATION']._serialized_start = 2186
    _globals['_SMARTCAMPAIGNSETTINGOPERATION']._serialized_end = 2340
    _globals['_MUTATESMARTCAMPAIGNSETTINGSRESPONSE']._serialized_start = 2343
    _globals['_MUTATESMARTCAMPAIGNSETTINGSRESPONSE']._serialized_end = 2517
    _globals['_MUTATESMARTCAMPAIGNSETTINGRESULT']._serialized_start = 2520
    _globals['_MUTATESMARTCAMPAIGNSETTINGRESULT']._serialized_end = 2719
    _globals['_SMARTCAMPAIGNSETTINGSERVICE']._serialized_start = 2722
    _globals['_SMARTCAMPAIGNSETTINGSERVICE']._serialized_end = 3359