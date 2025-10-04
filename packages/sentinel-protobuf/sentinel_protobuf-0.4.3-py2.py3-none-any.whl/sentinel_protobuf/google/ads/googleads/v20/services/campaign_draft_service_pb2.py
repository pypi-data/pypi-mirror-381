"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/services/campaign_draft_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v20.resources import campaign_draft_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_resources_dot_campaign__draft__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/ads/googleads/v20/services/campaign_draft_service.proto\x12!google.ads.googleads.v20.services\x1a:google/ads/googleads/v20/enums/response_content_type.proto\x1a7google/ads/googleads/v20/resources/campaign_draft.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\xa7\x02\n\x1bMutateCampaignDraftsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12R\n\noperations\x18\x02 \x03(\x0b29.google.ads.googleads.v20.services.CampaignDraftOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v20.enums.ResponseContentTypeEnum.ResponseContentType"|\n\x1bPromoteCampaignDraftRequest\x12F\n\x0ecampaign_draft\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&googleads.googleapis.com/CampaignDraft\x12\x15\n\rvalidate_only\x18\x02 \x01(\x08"\x9f\x02\n\x16CampaignDraftOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12C\n\x06create\x18\x01 \x01(\x0b21.google.ads.googleads.v20.resources.CampaignDraftH\x00\x12C\n\x06update\x18\x02 \x01(\x0b21.google.ads.googleads.v20.resources.CampaignDraftH\x00\x12=\n\x06remove\x18\x03 \x01(\tB+\xfaA(\n&googleads.googleapis.com/CampaignDraftH\x00B\x0b\n\toperation"\xa0\x01\n\x1cMutateCampaignDraftsResponse\x121\n\x15partial_failure_error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12M\n\x07results\x18\x02 \x03(\x0b2<.google.ads.googleads.v20.services.MutateCampaignDraftResult"\xaa\x01\n\x19MutateCampaignDraftResult\x12B\n\rresource_name\x18\x01 \x01(\tB+\xfaA(\n&googleads.googleapis.com/CampaignDraft\x12I\n\x0ecampaign_draft\x18\x02 \x01(\x0b21.google.ads.googleads.v20.resources.CampaignDraft"\x93\x01\n#ListCampaignDraftAsyncErrorsRequest\x12E\n\rresource_name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&googleads.googleapis.com/CampaignDraft\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05"c\n$ListCampaignDraftAsyncErrorsResponse\x12"\n\x06errors\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xe0\x06\n\x14CampaignDraftService\x12\xf1\x01\n\x14MutateCampaignDrafts\x12>.google.ads.googleads.v20.services.MutateCampaignDraftsRequest\x1a?.google.ads.googleads.v20.services.MutateCampaignDraftsResponse"X\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x029"4/v20/customers/{customer_id=*}/campaignDrafts:mutate:\x01*\x12\xff\x01\n\x14PromoteCampaignDraft\x12>.google.ads.googleads.v20.services.PromoteCampaignDraftRequest\x1a\x1d.google.longrunning.Operation"\x87\x01\xcaA.\n\x15google.protobuf.Empty\x12\x15google.protobuf.Empty\xdaA\x0ecampaign_draft\x82\xd3\xe4\x93\x02?":/v20/{campaign_draft=customers/*/campaignDrafts/*}:promote:\x01*\x12\x8a\x02\n\x1cListCampaignDraftAsyncErrors\x12F.google.ads.googleads.v20.services.ListCampaignDraftAsyncErrorsRequest\x1aG.google.ads.googleads.v20.services.ListCampaignDraftAsyncErrorsResponse"Y\xdaA\rresource_name\x82\xd3\xe4\x93\x02C\x12A/v20/{resource_name=customers/*/campaignDrafts/*}:listAsyncErrors\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x85\x02\n%com.google.ads.googleads.v20.servicesB\x19CampaignDraftServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.services.campaign_draft_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v20.servicesB\x19CampaignDraftServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Services'
    _globals['_MUTATECAMPAIGNDRAFTSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECAMPAIGNDRAFTSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECAMPAIGNDRAFTSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATECAMPAIGNDRAFTSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_PROMOTECAMPAIGNDRAFTREQUEST'].fields_by_name['campaign_draft']._loaded_options = None
    _globals['_PROMOTECAMPAIGNDRAFTREQUEST'].fields_by_name['campaign_draft']._serialized_options = b'\xe0A\x02\xfaA(\n&googleads.googleapis.com/CampaignDraft'
    _globals['_CAMPAIGNDRAFTOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_CAMPAIGNDRAFTOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA(\n&googleads.googleapis.com/CampaignDraft'
    _globals['_MUTATECAMPAIGNDRAFTRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECAMPAIGNDRAFTRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA(\n&googleads.googleapis.com/CampaignDraft'
    _globals['_LISTCAMPAIGNDRAFTASYNCERRORSREQUEST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_LISTCAMPAIGNDRAFTASYNCERRORSREQUEST'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x02\xfaA(\n&googleads.googleapis.com/CampaignDraft'
    _globals['_CAMPAIGNDRAFTSERVICE']._loaded_options = None
    _globals['_CAMPAIGNDRAFTSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CAMPAIGNDRAFTSERVICE'].methods_by_name['MutateCampaignDrafts']._loaded_options = None
    _globals['_CAMPAIGNDRAFTSERVICE'].methods_by_name['MutateCampaignDrafts']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x029"4/v20/customers/{customer_id=*}/campaignDrafts:mutate:\x01*'
    _globals['_CAMPAIGNDRAFTSERVICE'].methods_by_name['PromoteCampaignDraft']._loaded_options = None
    _globals['_CAMPAIGNDRAFTSERVICE'].methods_by_name['PromoteCampaignDraft']._serialized_options = b'\xcaA.\n\x15google.protobuf.Empty\x12\x15google.protobuf.Empty\xdaA\x0ecampaign_draft\x82\xd3\xe4\x93\x02?":/v20/{campaign_draft=customers/*/campaignDrafts/*}:promote:\x01*'
    _globals['_CAMPAIGNDRAFTSERVICE'].methods_by_name['ListCampaignDraftAsyncErrors']._loaded_options = None
    _globals['_CAMPAIGNDRAFTSERVICE'].methods_by_name['ListCampaignDraftAsyncErrors']._serialized_options = b'\xdaA\rresource_name\x82\xd3\xe4\x93\x02C\x12A/v20/{resource_name=customers/*/campaignDrafts/*}:listAsyncErrors'
    _globals['_MUTATECAMPAIGNDRAFTSREQUEST']._serialized_start = 459
    _globals['_MUTATECAMPAIGNDRAFTSREQUEST']._serialized_end = 754
    _globals['_PROMOTECAMPAIGNDRAFTREQUEST']._serialized_start = 756
    _globals['_PROMOTECAMPAIGNDRAFTREQUEST']._serialized_end = 880
    _globals['_CAMPAIGNDRAFTOPERATION']._serialized_start = 883
    _globals['_CAMPAIGNDRAFTOPERATION']._serialized_end = 1170
    _globals['_MUTATECAMPAIGNDRAFTSRESPONSE']._serialized_start = 1173
    _globals['_MUTATECAMPAIGNDRAFTSRESPONSE']._serialized_end = 1333
    _globals['_MUTATECAMPAIGNDRAFTRESULT']._serialized_start = 1336
    _globals['_MUTATECAMPAIGNDRAFTRESULT']._serialized_end = 1506
    _globals['_LISTCAMPAIGNDRAFTASYNCERRORSREQUEST']._serialized_start = 1509
    _globals['_LISTCAMPAIGNDRAFTASYNCERRORSREQUEST']._serialized_end = 1656
    _globals['_LISTCAMPAIGNDRAFTASYNCERRORSRESPONSE']._serialized_start = 1658
    _globals['_LISTCAMPAIGNDRAFTASYNCERRORSRESPONSE']._serialized_end = 1757
    _globals['_CAMPAIGNDRAFTSERVICE']._serialized_start = 1760
    _globals['_CAMPAIGNDRAFTSERVICE']._serialized_end = 2624