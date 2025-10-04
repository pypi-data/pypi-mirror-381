"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/services/campaign_shared_set_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v19.resources import campaign_shared_set_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_resources_dot_campaign__shared__set__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/ads/googleads/v19/services/campaign_shared_set_service.proto\x12!google.ads.googleads.v19.services\x1a:google/ads/googleads/v19/enums/response_content_type.proto\x1a<google/ads/googleads/v19/resources/campaign_shared_set.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto"\xaf\x02\n\x1fMutateCampaignSharedSetsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12V\n\noperations\x18\x02 \x03(\x0b2=.google.ads.googleads.v19.services.CampaignSharedSetOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v19.enums.ResponseContentTypeEnum.ResponseContentType"\xb5\x01\n\x1aCampaignSharedSetOperation\x12G\n\x06create\x18\x01 \x01(\x0b25.google.ads.googleads.v19.resources.CampaignSharedSetH\x00\x12A\n\x06remove\x18\x03 \x01(\tB/\xfaA,\n*googleads.googleapis.com/CampaignSharedSetH\x00B\x0b\n\toperation"\xa8\x01\n MutateCampaignSharedSetsResponse\x121\n\x15partial_failure_error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12Q\n\x07results\x18\x02 \x03(\x0b2@.google.ads.googleads.v19.services.MutateCampaignSharedSetResult"\xbb\x01\n\x1dMutateCampaignSharedSetResult\x12F\n\rresource_name\x18\x01 \x01(\tB/\xfaA,\n*googleads.googleapis.com/CampaignSharedSet\x12R\n\x13campaign_shared_set\x18\x02 \x01(\x0b25.google.ads.googleads.v19.resources.CampaignSharedSet2\xe5\x02\n\x18CampaignSharedSetService\x12\x81\x02\n\x18MutateCampaignSharedSets\x12B.google.ads.googleads.v19.services.MutateCampaignSharedSetsRequest\x1aC.google.ads.googleads.v19.services.MutateCampaignSharedSetsResponse"\\\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02="8/v19/customers/{customer_id=*}/campaignSharedSets:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x89\x02\n%com.google.ads.googleads.v19.servicesB\x1dCampaignSharedSetServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.services.campaign_shared_set_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v19.servicesB\x1dCampaignSharedSetServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Services'
    _globals['_MUTATECAMPAIGNSHAREDSETSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECAMPAIGNSHAREDSETSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECAMPAIGNSHAREDSETSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATECAMPAIGNSHAREDSETSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_CAMPAIGNSHAREDSETOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_CAMPAIGNSHAREDSETOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA,\n*googleads.googleapis.com/CampaignSharedSet'
    _globals['_MUTATECAMPAIGNSHAREDSETRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECAMPAIGNSHAREDSETRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA,\n*googleads.googleapis.com/CampaignSharedSet'
    _globals['_CAMPAIGNSHAREDSETSERVICE']._loaded_options = None
    _globals['_CAMPAIGNSHAREDSETSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CAMPAIGNSHAREDSETSERVICE'].methods_by_name['MutateCampaignSharedSets']._loaded_options = None
    _globals['_CAMPAIGNSHAREDSETSERVICE'].methods_by_name['MutateCampaignSharedSets']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02="8/v19/customers/{customer_id=*}/campaignSharedSets:mutate:\x01*'
    _globals['_MUTATECAMPAIGNSHAREDSETSREQUEST']._serialized_start = 369
    _globals['_MUTATECAMPAIGNSHAREDSETSREQUEST']._serialized_end = 672
    _globals['_CAMPAIGNSHAREDSETOPERATION']._serialized_start = 675
    _globals['_CAMPAIGNSHAREDSETOPERATION']._serialized_end = 856
    _globals['_MUTATECAMPAIGNSHAREDSETSRESPONSE']._serialized_start = 859
    _globals['_MUTATECAMPAIGNSHAREDSETSRESPONSE']._serialized_end = 1027
    _globals['_MUTATECAMPAIGNSHAREDSETRESULT']._serialized_start = 1030
    _globals['_MUTATECAMPAIGNSHAREDSETRESULT']._serialized_end = 1217
    _globals['_CAMPAIGNSHAREDSETSERVICE']._serialized_start = 1220
    _globals['_CAMPAIGNSHAREDSETSERVICE']._serialized_end = 1577