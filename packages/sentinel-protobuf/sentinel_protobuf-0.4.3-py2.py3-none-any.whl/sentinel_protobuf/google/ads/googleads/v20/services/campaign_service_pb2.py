"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/services/campaign_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v20.resources import campaign_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_resources_dot_campaign__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v20/services/campaign_service.proto\x12!google.ads.googleads.v20.services\x1a:google/ads/googleads/v20/enums/response_content_type.proto\x1a1google/ads/googleads/v20/resources/campaign.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\x9d\x02\n\x16MutateCampaignsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12M\n\noperations\x18\x02 \x03(\x0b24.google.ads.googleads.v20.services.CampaignOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v20.enums.ResponseContentTypeEnum.ResponseContentType"\x8b\x02\n\x11CampaignOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12>\n\x06create\x18\x01 \x01(\x0b2,.google.ads.googleads.v20.resources.CampaignH\x00\x12>\n\x06update\x18\x02 \x01(\x0b2,.google.ads.googleads.v20.resources.CampaignH\x00\x128\n\x06remove\x18\x03 \x01(\tB&\xfaA#\n!googleads.googleapis.com/CampaignH\x00B\x0b\n\toperation"\x96\x01\n\x17MutateCampaignsResponse\x121\n\x15partial_failure_error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12H\n\x07results\x18\x02 \x03(\x0b27.google.ads.googleads.v20.services.MutateCampaignResult"\x95\x01\n\x14MutateCampaignResult\x12=\n\rresource_name\x18\x01 \x01(\tB&\xfaA#\n!googleads.googleapis.com/Campaign\x12>\n\x08campaign\x18\x02 \x01(\x0b2,.google.ads.googleads.v20.resources.Campaign"\x89\x01\n EnablePMaxBrandGuidelinesRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12K\n\noperations\x18\x02 \x03(\x0b22.google.ads.googleads.v20.services.EnableOperationB\x03\xe0A\x02"\xb7\x02\n\x0fEnableOperation\x12;\n\x08campaign\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!googleads.googleapis.com/Campaign\x12\'\n\x1aauto_populate_brand_assets\x18\x02 \x01(\x08B\x03\xe0A\x02\x12Q\n\x0cbrand_assets\x18\x03 \x01(\x0b26.google.ads.googleads.v20.services.BrandCampaignAssetsB\x03\xe0A\x01\x12\x1d\n\x10final_uri_domain\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x17\n\nmain_color\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0caccent_color\x18\x06 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bfont_family\x18\x07 \x01(\tB\x03\xe0A\x01"s\n\x13BrandCampaignAssets\x12 \n\x13business_name_asset\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\nlogo_asset\x18\x02 \x03(\tB\x03\xe0A\x02\x12!\n\x14landscape_logo_asset\x18\x03 \x03(\tB\x03\xe0A\x01"i\n!EnablePMaxBrandGuidelinesResponse\x12D\n\x07results\x18\x01 \x03(\x0b23.google.ads.googleads.v20.services.EnablementResult"z\n\x10EnablementResult\x128\n\x08campaign\x18\x01 \x01(\tB&\xfaA#\n!googleads.googleapis.com/Campaign\x12,\n\x10enablement_error\x18\x02 \x01(\x0b2\x12.google.rpc.Status2\xc9\x04\n\x0fCampaignService\x12\xdd\x01\n\x0fMutateCampaigns\x129.google.ads.googleads.v20.services.MutateCampaignsRequest\x1a:.google.ads.googleads.v20.services.MutateCampaignsResponse"S\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x024"//v20/customers/{customer_id=*}/campaigns:mutate:\x01*\x12\x8e\x02\n\x19EnablePMaxBrandGuidelines\x12C.google.ads.googleads.v20.services.EnablePMaxBrandGuidelinesRequest\x1aD.google.ads.googleads.v20.services.EnablePMaxBrandGuidelinesResponse"f\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02G"B/v20/customers/{customer_id=*}/campaigns:enablePMaxBrandGuidelines:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x80\x02\n%com.google.ads.googleads.v20.servicesB\x14CampaignServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.services.campaign_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v20.servicesB\x14CampaignServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Services'
    _globals['_MUTATECAMPAIGNSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECAMPAIGNSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECAMPAIGNSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATECAMPAIGNSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_CAMPAIGNOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_CAMPAIGNOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_MUTATECAMPAIGNRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECAMPAIGNRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_ENABLEPMAXBRANDGUIDELINESREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_ENABLEPMAXBRANDGUIDELINESREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_ENABLEPMAXBRANDGUIDELINESREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_ENABLEPMAXBRANDGUIDELINESREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_ENABLEOPERATION'].fields_by_name['campaign']._loaded_options = None
    _globals['_ENABLEOPERATION'].fields_by_name['campaign']._serialized_options = b'\xe0A\x02\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_ENABLEOPERATION'].fields_by_name['auto_populate_brand_assets']._loaded_options = None
    _globals['_ENABLEOPERATION'].fields_by_name['auto_populate_brand_assets']._serialized_options = b'\xe0A\x02'
    _globals['_ENABLEOPERATION'].fields_by_name['brand_assets']._loaded_options = None
    _globals['_ENABLEOPERATION'].fields_by_name['brand_assets']._serialized_options = b'\xe0A\x01'
    _globals['_ENABLEOPERATION'].fields_by_name['final_uri_domain']._loaded_options = None
    _globals['_ENABLEOPERATION'].fields_by_name['final_uri_domain']._serialized_options = b'\xe0A\x01'
    _globals['_ENABLEOPERATION'].fields_by_name['main_color']._loaded_options = None
    _globals['_ENABLEOPERATION'].fields_by_name['main_color']._serialized_options = b'\xe0A\x01'
    _globals['_ENABLEOPERATION'].fields_by_name['accent_color']._loaded_options = None
    _globals['_ENABLEOPERATION'].fields_by_name['accent_color']._serialized_options = b'\xe0A\x01'
    _globals['_ENABLEOPERATION'].fields_by_name['font_family']._loaded_options = None
    _globals['_ENABLEOPERATION'].fields_by_name['font_family']._serialized_options = b'\xe0A\x01'
    _globals['_BRANDCAMPAIGNASSETS'].fields_by_name['business_name_asset']._loaded_options = None
    _globals['_BRANDCAMPAIGNASSETS'].fields_by_name['business_name_asset']._serialized_options = b'\xe0A\x02'
    _globals['_BRANDCAMPAIGNASSETS'].fields_by_name['logo_asset']._loaded_options = None
    _globals['_BRANDCAMPAIGNASSETS'].fields_by_name['logo_asset']._serialized_options = b'\xe0A\x02'
    _globals['_BRANDCAMPAIGNASSETS'].fields_by_name['landscape_logo_asset']._loaded_options = None
    _globals['_BRANDCAMPAIGNASSETS'].fields_by_name['landscape_logo_asset']._serialized_options = b'\xe0A\x01'
    _globals['_ENABLEMENTRESULT'].fields_by_name['campaign']._loaded_options = None
    _globals['_ENABLEMENTRESULT'].fields_by_name['campaign']._serialized_options = b'\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_CAMPAIGNSERVICE']._loaded_options = None
    _globals['_CAMPAIGNSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CAMPAIGNSERVICE'].methods_by_name['MutateCampaigns']._loaded_options = None
    _globals['_CAMPAIGNSERVICE'].methods_by_name['MutateCampaigns']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x024"//v20/customers/{customer_id=*}/campaigns:mutate:\x01*'
    _globals['_CAMPAIGNSERVICE'].methods_by_name['EnablePMaxBrandGuidelines']._loaded_options = None
    _globals['_CAMPAIGNSERVICE'].methods_by_name['EnablePMaxBrandGuidelines']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02G"B/v20/customers/{customer_id=*}/campaigns:enablePMaxBrandGuidelines:\x01*'
    _globals['_MUTATECAMPAIGNSREQUEST']._serialized_start = 381
    _globals['_MUTATECAMPAIGNSREQUEST']._serialized_end = 666
    _globals['_CAMPAIGNOPERATION']._serialized_start = 669
    _globals['_CAMPAIGNOPERATION']._serialized_end = 936
    _globals['_MUTATECAMPAIGNSRESPONSE']._serialized_start = 939
    _globals['_MUTATECAMPAIGNSRESPONSE']._serialized_end = 1089
    _globals['_MUTATECAMPAIGNRESULT']._serialized_start = 1092
    _globals['_MUTATECAMPAIGNRESULT']._serialized_end = 1241
    _globals['_ENABLEPMAXBRANDGUIDELINESREQUEST']._serialized_start = 1244
    _globals['_ENABLEPMAXBRANDGUIDELINESREQUEST']._serialized_end = 1381
    _globals['_ENABLEOPERATION']._serialized_start = 1384
    _globals['_ENABLEOPERATION']._serialized_end = 1695
    _globals['_BRANDCAMPAIGNASSETS']._serialized_start = 1697
    _globals['_BRANDCAMPAIGNASSETS']._serialized_end = 1812
    _globals['_ENABLEPMAXBRANDGUIDELINESRESPONSE']._serialized_start = 1814
    _globals['_ENABLEPMAXBRANDGUIDELINESRESPONSE']._serialized_end = 1919
    _globals['_ENABLEMENTRESULT']._serialized_start = 1921
    _globals['_ENABLEMENTRESULT']._serialized_end = 2043
    _globals['_CAMPAIGNSERVICE']._serialized_start = 2046
    _globals['_CAMPAIGNSERVICE']._serialized_end = 2631