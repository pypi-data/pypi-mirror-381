"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/services/recommendation_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.common import criteria_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_criteria__pb2
from ......google.ads.googleads.v21.common import extensions_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_extensions__pb2
from ......google.ads.googleads.v21.enums import ad_group_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_ad__group__type__pb2
from ......google.ads.googleads.v21.enums import advertising_channel_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_advertising__channel__type__pb2
from ......google.ads.googleads.v21.enums import bidding_strategy_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_bidding__strategy__type__pb2
from ......google.ads.googleads.v21.enums import conversion_tracking_status_enum_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_conversion__tracking__status__enum__pb2
from ......google.ads.googleads.v21.enums import keyword_match_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_keyword__match__type__pb2
from ......google.ads.googleads.v21.enums import recommendation_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_recommendation__type__pb2
from ......google.ads.googleads.v21.enums import target_impression_share_location_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_target__impression__share__location__pb2
from ......google.ads.googleads.v21.resources import ad_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_ad__pb2
from ......google.ads.googleads.v21.resources import asset_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_asset__pb2
from ......google.ads.googleads.v21.resources import recommendation_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_recommendation__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/ads/googleads/v21/services/recommendation_service.proto\x12!google.ads.googleads.v21.services\x1a.google/ads/googleads/v21/common/criteria.proto\x1a0google/ads/googleads/v21/common/extensions.proto\x1a2google/ads/googleads/v21/enums/ad_group_type.proto\x1a=google/ads/googleads/v21/enums/advertising_channel_type.proto\x1a:google/ads/googleads/v21/enums/bidding_strategy_type.proto\x1aDgoogle/ads/googleads/v21/enums/conversion_tracking_status_enum.proto\x1a7google/ads/googleads/v21/enums/keyword_match_type.proto\x1a8google/ads/googleads/v21/enums/recommendation_type.proto\x1aEgoogle/ads/googleads/v21/enums/target_impression_share_location.proto\x1a+google/ads/googleads/v21/resources/ad.proto\x1a.google/ads/googleads/v21/resources/asset.proto\x1a7google/ads/googleads/v21/resources/recommendation.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto"\xa9\x01\n\x1aApplyRecommendationRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12X\n\noperations\x18\x02 \x03(\x0b2?.google.ads.googleads.v21.services.ApplyRecommendationOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08"\xf3/\n\x1cApplyRecommendationOperation\x12C\n\rresource_name\x18\x01 \x01(\tB,\xfaA)\n\'googleads.googleapis.com/Recommendation\x12s\n\x0fcampaign_budget\x18\x02 \x01(\x0b2X.google.ads.googleads.v21.services.ApplyRecommendationOperation.CampaignBudgetParametersH\x00\x12c\n\x07text_ad\x18\x03 \x01(\x0b2P.google.ads.googleads.v21.services.ApplyRecommendationOperation.TextAdParametersH\x00\x12d\n\x07keyword\x18\x04 \x01(\x0b2Q.google.ads.googleads.v21.services.ApplyRecommendationOperation.KeywordParametersH\x00\x12u\n\x11target_cpa_opt_in\x18\x05 \x01(\x0b2X.google.ads.googleads.v21.services.ApplyRecommendationOperation.TargetCpaOptInParametersH\x00\x12w\n\x12target_roas_opt_in\x18\n \x01(\x0b2Y.google.ads.googleads.v21.services.ApplyRecommendationOperation.TargetRoasOptInParametersH\x00\x12w\n\x11callout_extension\x18\x06 \x01(\x0b2Z.google.ads.googleads.v21.services.ApplyRecommendationOperation.CalloutExtensionParametersH\x00\x12q\n\x0ecall_extension\x18\x07 \x01(\x0b2W.google.ads.googleads.v21.services.ApplyRecommendationOperation.CallExtensionParametersH\x00\x12y\n\x12sitelink_extension\x18\x08 \x01(\x0b2[.google.ads.googleads.v21.services.ApplyRecommendationOperation.SitelinkExtensionParametersH\x00\x12x\n\x12move_unused_budget\x18\t \x01(\x0b2Z.google.ads.googleads.v21.services.ApplyRecommendationOperation.MoveUnusedBudgetParametersH\x00\x12|\n\x14responsive_search_ad\x18\x0b \x01(\x0b2\\.google.ads.googleads.v21.services.ApplyRecommendationOperation.ResponsiveSearchAdParametersH\x00\x12\x81\x01\n\x17use_broad_match_keyword\x18\x0c \x01(\x0b2^.google.ads.googleads.v21.services.ApplyRecommendationOperation.UseBroadMatchKeywordParametersH\x00\x12\x87\x01\n\x1aresponsive_search_ad_asset\x18\r \x01(\x0b2a.google.ads.googleads.v21.services.ApplyRecommendationOperation.ResponsiveSearchAdAssetParametersH\x00\x12\xa1\x01\n(responsive_search_ad_improve_ad_strength\x18\x0e \x01(\x0b2m.google.ads.googleads.v21.services.ApplyRecommendationOperation.ResponsiveSearchAdImproveAdStrengthParametersH\x00\x12\x89\x01\n\x1craise_target_cpa_bid_too_low\x18\x0f \x01(\x0b2a.google.ads.googleads.v21.services.ApplyRecommendationOperation.RaiseTargetCpaBidTooLowParametersH\x00\x12\x89\x01\n\x1bforecasting_set_target_roas\x18\x10 \x01(\x0b2b.google.ads.googleads.v21.services.ApplyRecommendationOperation.ForecastingSetTargetRoasParametersH\x00\x12o\n\rcallout_asset\x18\x11 \x01(\x0b2V.google.ads.googleads.v21.services.ApplyRecommendationOperation.CalloutAssetParametersH\x00\x12i\n\ncall_asset\x18\x12 \x01(\x0b2S.google.ads.googleads.v21.services.ApplyRecommendationOperation.CallAssetParametersH\x00\x12q\n\x0esitelink_asset\x18\x13 \x01(\x0b2W.google.ads.googleads.v21.services.ApplyRecommendationOperation.SitelinkAssetParametersH\x00\x12t\n\x10raise_target_cpa\x18\x14 \x01(\x0b2X.google.ads.googleads.v21.services.ApplyRecommendationOperation.RaiseTargetCpaParametersH\x00\x12v\n\x11lower_target_roas\x18\x15 \x01(\x0b2Y.google.ads.googleads.v21.services.ApplyRecommendationOperation.LowerTargetRoasParametersH\x00\x12\x87\x01\n\x1aforecasting_set_target_cpa\x18\x16 \x01(\x0b2a.google.ads.googleads.v21.services.ApplyRecommendationOperation.ForecastingSetTargetCpaParametersH\x00\x12{\n\x0eset_target_cpa\x18\x17 \x01(\x0b2a.google.ads.googleads.v21.services.ApplyRecommendationOperation.ForecastingSetTargetCpaParametersH\x00\x12}\n\x0fset_target_roas\x18\x18 \x01(\x0b2b.google.ads.googleads.v21.services.ApplyRecommendationOperation.ForecastingSetTargetRoasParametersH\x00\x12r\n\x0flead_form_asset\x18\x19 \x01(\x0b2W.google.ads.googleads.v21.services.ApplyRecommendationOperation.LeadFormAssetParametersH\x00\x1a^\n\x18CampaignBudgetParameters\x12%\n\x18new_budget_amount_micros\x18\x02 \x01(\x03H\x00\x88\x01\x01B\x1b\n\x19_new_budget_amount_micros\x1a\x9c\x01\n"ForecastingSetTargetRoasParameters\x12\x18\n\x0btarget_roas\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12*\n\x1dcampaign_budget_amount_micros\x18\x02 \x01(\x03H\x01\x88\x01\x01B\x0e\n\x0c_target_roasB \n\x1e_campaign_budget_amount_micros\x1aF\n\x10TextAdParameters\x122\n\x02ad\x18\x01 \x01(\x0b2&.google.ads.googleads.v21.resources.Ad\x1a\xc2\x01\n\x11KeywordParameters\x12\x15\n\x08ad_group\x18\x04 \x01(\tH\x00\x88\x01\x01\x12Y\n\nmatch_type\x18\x02 \x01(\x0e2E.google.ads.googleads.v21.enums.KeywordMatchTypeEnum.KeywordMatchType\x12\x1b\n\x0ecpc_bid_micros\x18\x05 \x01(\x03H\x01\x88\x01\x01B\x0b\n\t_ad_groupB\x11\n\x0f_cpc_bid_micros\x1a\xa6\x01\n\x18TargetCpaOptInParameters\x12\x1e\n\x11target_cpa_micros\x18\x03 \x01(\x03H\x00\x88\x01\x01\x12.\n!new_campaign_budget_amount_micros\x18\x04 \x01(\x03H\x01\x88\x01\x01B\x14\n\x12_target_cpa_microsB$\n"_new_campaign_budget_amount_micros\x1a\x9b\x01\n\x19TargetRoasOptInParameters\x12\x18\n\x0btarget_roas\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12.\n!new_campaign_budget_amount_micros\x18\x02 \x01(\x03H\x01\x88\x01\x01B\x0e\n\x0c_target_roasB$\n"_new_campaign_budget_amount_micros\x1aj\n\x1aCalloutExtensionParameters\x12L\n\x12callout_extensions\x18\x01 \x03(\x0b20.google.ads.googleads.v21.common.CalloutFeedItem\x1aa\n\x17CallExtensionParameters\x12F\n\x0fcall_extensions\x18\x01 \x03(\x0b2-.google.ads.googleads.v21.common.CallFeedItem\x1am\n\x1bSitelinkExtensionParameters\x12N\n\x13sitelink_extensions\x18\x01 \x03(\x0b21.google.ads.googleads.v21.common.SitelinkFeedItem\x1a\x98\x01\n\x16CalloutAssetParameters\x12~\n\x19ad_asset_apply_parameters\x18\x01 \x01(\x0b2V.google.ads.googleads.v21.services.ApplyRecommendationOperation.AdAssetApplyParametersB\x03\xe0A\x02\x1a\x95\x01\n\x13CallAssetParameters\x12~\n\x19ad_asset_apply_parameters\x18\x01 \x01(\x0b2V.google.ads.googleads.v21.services.ApplyRecommendationOperation.AdAssetApplyParametersB\x03\xe0A\x02\x1a\x99\x01\n\x17SitelinkAssetParameters\x12~\n\x19ad_asset_apply_parameters\x18\x01 \x01(\x0b2V.google.ads.googleads.v21.services.ApplyRecommendationOperation.AdAssetApplyParametersB\x03\xe0A\x02\x1a>\n\x18RaiseTargetCpaParameters\x12"\n\x15target_cpa_multiplier\x18\x01 \x01(\x01B\x03\xe0A\x02\x1a@\n\x19LowerTargetRoasParameters\x12#\n\x16target_roas_multiplier\x18\x01 \x01(\x01B\x03\xe0A\x02\x1a\xaf\x02\n\x16AdAssetApplyParameters\x12=\n\nnew_assets\x18\x01 \x03(\x0b2).google.ads.googleads.v21.resources.Asset\x12\x17\n\x0fexisting_assets\x18\x02 \x03(\t\x12u\n\x05scope\x18\x03 \x01(\x0e2a.google.ads.googleads.v21.services.ApplyRecommendationOperation.AdAssetApplyParameters.ApplyScopeB\x03\xe0A\x02"F\n\nApplyScope\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07UNKNOWN\x10\x01\x12\x0c\n\x08CUSTOMER\x10\x02\x12\x0c\n\x08CAMPAIGN\x10\x03\x1aZ\n\x1aMoveUnusedBudgetParameters\x12"\n\x15budget_micros_to_move\x18\x02 \x01(\x03H\x00\x88\x01\x01B\x18\n\x16_budget_micros_to_move\x1a_\n!ResponsiveSearchAdAssetParameters\x12:\n\nupdated_ad\x18\x01 \x01(\x0b2&.google.ads.googleads.v21.resources.Ad\x1ak\n-ResponsiveSearchAdImproveAdStrengthParameters\x12:\n\nupdated_ad\x18\x01 \x01(\x0b2&.google.ads.googleads.v21.resources.Ad\x1aW\n\x1cResponsiveSearchAdParameters\x127\n\x02ad\x18\x01 \x01(\x0b2&.google.ads.googleads.v21.resources.AdB\x03\xe0A\x02\x1aC\n!RaiseTargetCpaBidTooLowParameters\x12\x1e\n\x11target_multiplier\x18\x01 \x01(\x01B\x03\xe0A\x02\x1ad\n\x1eUseBroadMatchKeywordParameters\x12%\n\x18new_budget_amount_micros\x18\x01 \x01(\x03H\x00\x88\x01\x01B\x1b\n\x19_new_budget_amount_micros\x1a\xa7\x01\n!ForecastingSetTargetCpaParameters\x12\x1e\n\x11target_cpa_micros\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12*\n\x1dcampaign_budget_amount_micros\x18\x02 \x01(\x03H\x01\x88\x01\x01B\x14\n\x12_target_cpa_microsB \n\x1e_campaign_budget_amount_micros\x1a\xfd\x01\n\x17LeadFormAssetParameters\x12~\n\x19ad_asset_apply_parameters\x18\x01 \x01(\x0b2V.google.ads.googleads.v21.services.ApplyRecommendationOperation.AdAssetApplyParametersB\x03\xe0A\x02\x125\n(set_submit_lead_form_asset_campaign_goal\x18\x02 \x01(\x08H\x00\x88\x01\x01B+\n)_set_submit_lead_form_asset_campaign_goalB\x12\n\x10apply_parameters"\x9f\x01\n\x1bApplyRecommendationResponse\x12M\n\x07results\x18\x01 \x03(\x0b2<.google.ads.googleads.v21.services.ApplyRecommendationResult\x121\n\x15partial_failure_error\x18\x02 \x01(\x0b2\x12.google.rpc.Status"`\n\x19ApplyRecommendationResult\x12C\n\rresource_name\x18\x01 \x01(\tB,\xfaA)\n\'googleads.googleapis.com/Recommendation"\x83\x02\n\x1cDismissRecommendationRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12w\n\noperations\x18\x03 \x03(\x0b2^.google.ads.googleads.v21.services.DismissRecommendationRequest.DismissRecommendationOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x02 \x01(\x08\x1a7\n\x1eDismissRecommendationOperation\x12\x15\n\rresource_name\x18\x01 \x01(\t"\xf7\x01\n\x1dDismissRecommendationResponse\x12m\n\x07results\x18\x01 \x03(\x0b2\\.google.ads.googleads.v21.services.DismissRecommendationResponse.DismissRecommendationResult\x121\n\x15partial_failure_error\x18\x02 \x01(\x0b2\x12.google.rpc.Status\x1a4\n\x1bDismissRecommendationResult\x12\x15\n\rresource_name\x18\x01 \x01(\t"\xd6\x15\n\x1eGenerateRecommendationsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12l\n\x14recommendation_types\x18\x02 \x03(\x0e2I.google.ads.googleads.v21.enums.RecommendationTypeEnum.RecommendationTypeB\x03\xe0A\x02\x12x\n\x18advertising_channel_type\x18\x03 \x01(\x0e2Q.google.ads.googleads.v21.enums.AdvertisingChannelTypeEnum.AdvertisingChannelTypeB\x03\xe0A\x02\x12)\n\x17campaign_sitelink_count\x18\x04 \x01(\x05B\x03\xe0A\x01H\x00\x88\x01\x01\x12\x83\x01\n\x1aconversion_tracking_status\x18\x05 \x01(\x0e2U.google.ads.googleads.v21.enums.ConversionTrackingStatusEnum.ConversionTrackingStatusB\x03\xe0A\x01H\x01\x88\x01\x01\x12m\n\x0cbidding_info\x18\x06 \x01(\x0b2M.google.ads.googleads.v21.services.GenerateRecommendationsRequest.BiddingInfoB\x03\xe0A\x01H\x02\x88\x01\x01\x12i\n\rad_group_info\x18\x07 \x03(\x0b2M.google.ads.googleads.v21.services.GenerateRecommendationsRequest.AdGroupInfoB\x03\xe0A\x01\x12g\n\tseed_info\x18\x08 \x01(\x0b2J.google.ads.googleads.v21.services.GenerateRecommendationsRequest.SeedInfoB\x03\xe0A\x01H\x03\x88\x01\x01\x12k\n\x0bbudget_info\x18\t \x01(\x0b2L.google.ads.googleads.v21.services.GenerateRecommendationsRequest.BudgetInfoB\x03\xe0A\x01H\x04\x88\x01\x01\x12,\n\x1acampaign_image_asset_count\x18\n \x01(\x05B\x03\xe0A\x01H\x05\x88\x01\x01\x12+\n\x19campaign_call_asset_count\x18\x0b \x01(\x05B\x03\xe0A\x01H\x06\x88\x01\x01\x12\x1a\n\rcountry_codes\x18\r \x03(\tB\x03\xe0A\x01\x12\x1b\n\x0elanguage_codes\x18\x0e \x03(\tB\x03\xe0A\x01\x12#\n\x16positive_locations_ids\x18\x0f \x03(\x03B\x03\xe0A\x01\x12#\n\x16negative_locations_ids\x18\x10 \x03(\x03B\x03\xe0A\x01\x12o\n\x10asset_group_info\x18\x11 \x03(\x0b2P.google.ads.googleads.v21.services.GenerateRecommendationsRequest.AssetGroupInfoB\x03\xe0A\x01\x12/\n\x1dtarget_partner_search_network\x18\x12 \x01(\x08B\x03\xe0A\x01H\x07\x88\x01\x01\x12(\n\x16target_content_network\x18\x13 \x01(\x08B\x03\xe0A\x01H\x08\x88\x01\x01\x12,\n\x1amerchant_center_account_id\x18\x14 \x01(\x03B\x03\xe0A\x01H\t\x88\x01\x01\x1a\xf7\x02\n\x0bBiddingInfo\x12o\n\x15bidding_strategy_type\x18\x01 \x01(\x0e2K.google.ads.googleads.v21.enums.BiddingStrategyTypeEnum.BiddingStrategyTypeH\x01\x88\x01\x01\x12\x1b\n\x11target_cpa_micros\x18\x02 \x01(\x03H\x00\x12\x15\n\x0btarget_roas\x18\x03 \x01(\x01H\x00\x12\x88\x01\n\x1ctarget_impression_share_info\x18\x04 \x01(\x0b2[.google.ads.googleads.v21.services.GenerateRecommendationsRequest.TargetImpressionShareInfoB\x03\xe0A\x01H\x00B\x1e\n\x1cbidding_strategy_target_infoB\x18\n\x16_bidding_strategy_type\x1a\xc2\x01\n\x0bAdGroupInfo\x12\\\n\rad_group_type\x18\x01 \x01(\x0e2;.google.ads.googleads.v21.enums.AdGroupTypeEnum.AdGroupTypeB\x03\xe0A\x01H\x00\x88\x01\x01\x12C\n\x08keywords\x18\x02 \x03(\x0b2,.google.ads.googleads.v21.common.KeywordInfoB\x03\xe0A\x01B\x10\n\x0e_ad_group_type\x1aJ\n\x08SeedInfo\x12\x15\n\x08url_seed\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rkeyword_seeds\x18\x03 \x03(\tB\x03\xe0A\x01B\x0b\n\t_url_seed\x1aA\n\nBudgetInfo\x12 \n\x0ecurrent_budget\x18\x01 \x01(\x03B\x03\xe0A\x02H\x00\x88\x01\x01B\x11\n\x0f_current_budget\x1al\n\x0eAssetGroupInfo\x12\x1b\n\tfinal_url\x18\x01 \x01(\tB\x03\xe0A\x02H\x00\x88\x01\x01\x12\x15\n\x08headline\x18\x02 \x03(\tB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x03 \x03(\tB\x03\xe0A\x01B\x0c\n\n_final_url\x1a\xb9\x02\n\x19TargetImpressionShareInfo\x12{\n\x08location\x18\x01 \x01(\x0e2_.google.ads.googleads.v21.enums.TargetImpressionShareLocationEnum.TargetImpressionShareLocationB\x03\xe0A\x02H\x00\x88\x01\x01\x120\n\x1etarget_impression_share_micros\x18\x02 \x01(\x03B\x03\xe0A\x02H\x01\x88\x01\x01\x12%\n\x13max_cpc_bid_ceiling\x18\x03 \x01(\x03B\x03\xe0A\x01H\x02\x88\x01\x01B\x0b\n\t_locationB!\n\x1f_target_impression_share_microsB\x16\n\x14_max_cpc_bid_ceilingB\x1a\n\x18_campaign_sitelink_countB\x1d\n\x1b_conversion_tracking_statusB\x0f\n\r_bidding_infoB\x0c\n\n_seed_infoB\x0e\n\x0c_budget_infoB\x1d\n\x1b_campaign_image_asset_countB\x1c\n\x1a_campaign_call_asset_countB \n\x1e_target_partner_search_networkB\x19\n\x17_target_content_networkB\x1d\n\x1b_merchant_center_account_id"n\n\x1fGenerateRecommendationsResponse\x12K\n\x0frecommendations\x18\x01 \x03(\x0b22.google.ads.googleads.v21.resources.Recommendation2\xeb\x06\n\x15RecommendationService\x12\xee\x01\n\x13ApplyRecommendation\x12=.google.ads.googleads.v21.services.ApplyRecommendationRequest\x1a>.google.ads.googleads.v21.services.ApplyRecommendationResponse"X\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x029"4/v21/customers/{customer_id=*}/recommendations:apply:\x01*\x12\xf6\x01\n\x15DismissRecommendation\x12?.google.ads.googleads.v21.services.DismissRecommendationRequest\x1a@.google.ads.googleads.v21.services.DismissRecommendationResponse"Z\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02;"6/v21/customers/{customer_id=*}/recommendations:dismiss:\x01*\x12\xa0\x02\n\x17GenerateRecommendations\x12A.google.ads.googleads.v21.services.GenerateRecommendationsRequest\x1aB.google.ads.googleads.v21.services.GenerateRecommendationsResponse"~\xdaA9customer_id,recommendation_types,advertising_channel_type\x82\xd3\xe4\x93\x02<"7/v21/customers/{customer_id=*}/recommendations:generate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x86\x02\n%com.google.ads.googleads.v21.servicesB\x1aRecommendationServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.services.recommendation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v21.servicesB\x1aRecommendationServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Services'
    _globals['_APPLYRECOMMENDATIONREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_APPLYRECOMMENDATIONREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_APPLYRECOMMENDATIONREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_APPLYRECOMMENDATIONREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_APPLYRECOMMENDATIONOPERATION_CALLOUTASSETPARAMETERS'].fields_by_name['ad_asset_apply_parameters']._loaded_options = None
    _globals['_APPLYRECOMMENDATIONOPERATION_CALLOUTASSETPARAMETERS'].fields_by_name['ad_asset_apply_parameters']._serialized_options = b'\xe0A\x02'
    _globals['_APPLYRECOMMENDATIONOPERATION_CALLASSETPARAMETERS'].fields_by_name['ad_asset_apply_parameters']._loaded_options = None
    _globals['_APPLYRECOMMENDATIONOPERATION_CALLASSETPARAMETERS'].fields_by_name['ad_asset_apply_parameters']._serialized_options = b'\xe0A\x02'
    _globals['_APPLYRECOMMENDATIONOPERATION_SITELINKASSETPARAMETERS'].fields_by_name['ad_asset_apply_parameters']._loaded_options = None
    _globals['_APPLYRECOMMENDATIONOPERATION_SITELINKASSETPARAMETERS'].fields_by_name['ad_asset_apply_parameters']._serialized_options = b'\xe0A\x02'
    _globals['_APPLYRECOMMENDATIONOPERATION_RAISETARGETCPAPARAMETERS'].fields_by_name['target_cpa_multiplier']._loaded_options = None
    _globals['_APPLYRECOMMENDATIONOPERATION_RAISETARGETCPAPARAMETERS'].fields_by_name['target_cpa_multiplier']._serialized_options = b'\xe0A\x02'
    _globals['_APPLYRECOMMENDATIONOPERATION_LOWERTARGETROASPARAMETERS'].fields_by_name['target_roas_multiplier']._loaded_options = None
    _globals['_APPLYRECOMMENDATIONOPERATION_LOWERTARGETROASPARAMETERS'].fields_by_name['target_roas_multiplier']._serialized_options = b'\xe0A\x02'
    _globals['_APPLYRECOMMENDATIONOPERATION_ADASSETAPPLYPARAMETERS'].fields_by_name['scope']._loaded_options = None
    _globals['_APPLYRECOMMENDATIONOPERATION_ADASSETAPPLYPARAMETERS'].fields_by_name['scope']._serialized_options = b'\xe0A\x02'
    _globals['_APPLYRECOMMENDATIONOPERATION_RESPONSIVESEARCHADPARAMETERS'].fields_by_name['ad']._loaded_options = None
    _globals['_APPLYRECOMMENDATIONOPERATION_RESPONSIVESEARCHADPARAMETERS'].fields_by_name['ad']._serialized_options = b'\xe0A\x02'
    _globals['_APPLYRECOMMENDATIONOPERATION_RAISETARGETCPABIDTOOLOWPARAMETERS'].fields_by_name['target_multiplier']._loaded_options = None
    _globals['_APPLYRECOMMENDATIONOPERATION_RAISETARGETCPABIDTOOLOWPARAMETERS'].fields_by_name['target_multiplier']._serialized_options = b'\xe0A\x02'
    _globals['_APPLYRECOMMENDATIONOPERATION_LEADFORMASSETPARAMETERS'].fields_by_name['ad_asset_apply_parameters']._loaded_options = None
    _globals['_APPLYRECOMMENDATIONOPERATION_LEADFORMASSETPARAMETERS'].fields_by_name['ad_asset_apply_parameters']._serialized_options = b'\xe0A\x02'
    _globals['_APPLYRECOMMENDATIONOPERATION'].fields_by_name['resource_name']._loaded_options = None
    _globals['_APPLYRECOMMENDATIONOPERATION'].fields_by_name['resource_name']._serialized_options = b"\xfaA)\n'googleads.googleapis.com/Recommendation"
    _globals['_APPLYRECOMMENDATIONRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_APPLYRECOMMENDATIONRESULT'].fields_by_name['resource_name']._serialized_options = b"\xfaA)\n'googleads.googleapis.com/Recommendation"
    _globals['_DISMISSRECOMMENDATIONREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_DISMISSRECOMMENDATIONREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_DISMISSRECOMMENDATIONREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_DISMISSRECOMMENDATIONREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATERECOMMENDATIONSREQUEST_BIDDINGINFO'].fields_by_name['target_impression_share_info']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST_BIDDINGINFO'].fields_by_name['target_impression_share_info']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST_ADGROUPINFO'].fields_by_name['ad_group_type']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST_ADGROUPINFO'].fields_by_name['ad_group_type']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST_ADGROUPINFO'].fields_by_name['keywords']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST_ADGROUPINFO'].fields_by_name['keywords']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST_SEEDINFO'].fields_by_name['keyword_seeds']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST_SEEDINFO'].fields_by_name['keyword_seeds']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST_BUDGETINFO'].fields_by_name['current_budget']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST_BUDGETINFO'].fields_by_name['current_budget']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATERECOMMENDATIONSREQUEST_ASSETGROUPINFO'].fields_by_name['final_url']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST_ASSETGROUPINFO'].fields_by_name['final_url']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATERECOMMENDATIONSREQUEST_ASSETGROUPINFO'].fields_by_name['headline']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST_ASSETGROUPINFO'].fields_by_name['headline']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST_ASSETGROUPINFO'].fields_by_name['description']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST_ASSETGROUPINFO'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST_TARGETIMPRESSIONSHAREINFO'].fields_by_name['location']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST_TARGETIMPRESSIONSHAREINFO'].fields_by_name['location']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATERECOMMENDATIONSREQUEST_TARGETIMPRESSIONSHAREINFO'].fields_by_name['target_impression_share_micros']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST_TARGETIMPRESSIONSHAREINFO'].fields_by_name['target_impression_share_micros']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATERECOMMENDATIONSREQUEST_TARGETIMPRESSIONSHAREINFO'].fields_by_name['max_cpc_bid_ceiling']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST_TARGETIMPRESSIONSHAREINFO'].fields_by_name['max_cpc_bid_ceiling']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['recommendation_types']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['recommendation_types']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['advertising_channel_type']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['advertising_channel_type']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['campaign_sitelink_count']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['campaign_sitelink_count']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['conversion_tracking_status']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['conversion_tracking_status']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['bidding_info']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['bidding_info']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['ad_group_info']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['ad_group_info']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['seed_info']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['seed_info']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['budget_info']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['budget_info']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['campaign_image_asset_count']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['campaign_image_asset_count']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['campaign_call_asset_count']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['campaign_call_asset_count']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['country_codes']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['country_codes']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['language_codes']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['language_codes']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['positive_locations_ids']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['positive_locations_ids']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['negative_locations_ids']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['negative_locations_ids']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['asset_group_info']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['asset_group_info']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['target_partner_search_network']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['target_partner_search_network']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['target_content_network']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['target_content_network']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['merchant_center_account_id']._loaded_options = None
    _globals['_GENERATERECOMMENDATIONSREQUEST'].fields_by_name['merchant_center_account_id']._serialized_options = b'\xe0A\x01'
    _globals['_RECOMMENDATIONSERVICE']._loaded_options = None
    _globals['_RECOMMENDATIONSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_RECOMMENDATIONSERVICE'].methods_by_name['ApplyRecommendation']._loaded_options = None
    _globals['_RECOMMENDATIONSERVICE'].methods_by_name['ApplyRecommendation']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x029"4/v21/customers/{customer_id=*}/recommendations:apply:\x01*'
    _globals['_RECOMMENDATIONSERVICE'].methods_by_name['DismissRecommendation']._loaded_options = None
    _globals['_RECOMMENDATIONSERVICE'].methods_by_name['DismissRecommendation']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02;"6/v21/customers/{customer_id=*}/recommendations:dismiss:\x01*'
    _globals['_RECOMMENDATIONSERVICE'].methods_by_name['GenerateRecommendations']._loaded_options = None
    _globals['_RECOMMENDATIONSERVICE'].methods_by_name['GenerateRecommendations']._serialized_options = b'\xdaA9customer_id,recommendation_types,advertising_channel_type\x82\xd3\xe4\x93\x02<"7/v21/customers/{customer_id=*}/recommendations:generate:\x01*'
    _globals['_APPLYRECOMMENDATIONREQUEST']._serialized_start = 921
    _globals['_APPLYRECOMMENDATIONREQUEST']._serialized_end = 1090
    _globals['_APPLYRECOMMENDATIONOPERATION']._serialized_start = 1093
    _globals['_APPLYRECOMMENDATIONOPERATION']._serialized_end = 7224
    _globals['_APPLYRECOMMENDATIONOPERATION_CAMPAIGNBUDGETPARAMETERS']._serialized_start = 4154
    _globals['_APPLYRECOMMENDATIONOPERATION_CAMPAIGNBUDGETPARAMETERS']._serialized_end = 4248
    _globals['_APPLYRECOMMENDATIONOPERATION_FORECASTINGSETTARGETROASPARAMETERS']._serialized_start = 4251
    _globals['_APPLYRECOMMENDATIONOPERATION_FORECASTINGSETTARGETROASPARAMETERS']._serialized_end = 4407
    _globals['_APPLYRECOMMENDATIONOPERATION_TEXTADPARAMETERS']._serialized_start = 4409
    _globals['_APPLYRECOMMENDATIONOPERATION_TEXTADPARAMETERS']._serialized_end = 4479
    _globals['_APPLYRECOMMENDATIONOPERATION_KEYWORDPARAMETERS']._serialized_start = 4482
    _globals['_APPLYRECOMMENDATIONOPERATION_KEYWORDPARAMETERS']._serialized_end = 4676
    _globals['_APPLYRECOMMENDATIONOPERATION_TARGETCPAOPTINPARAMETERS']._serialized_start = 4679
    _globals['_APPLYRECOMMENDATIONOPERATION_TARGETCPAOPTINPARAMETERS']._serialized_end = 4845
    _globals['_APPLYRECOMMENDATIONOPERATION_TARGETROASOPTINPARAMETERS']._serialized_start = 4848
    _globals['_APPLYRECOMMENDATIONOPERATION_TARGETROASOPTINPARAMETERS']._serialized_end = 5003
    _globals['_APPLYRECOMMENDATIONOPERATION_CALLOUTEXTENSIONPARAMETERS']._serialized_start = 5005
    _globals['_APPLYRECOMMENDATIONOPERATION_CALLOUTEXTENSIONPARAMETERS']._serialized_end = 5111
    _globals['_APPLYRECOMMENDATIONOPERATION_CALLEXTENSIONPARAMETERS']._serialized_start = 5113
    _globals['_APPLYRECOMMENDATIONOPERATION_CALLEXTENSIONPARAMETERS']._serialized_end = 5210
    _globals['_APPLYRECOMMENDATIONOPERATION_SITELINKEXTENSIONPARAMETERS']._serialized_start = 5212
    _globals['_APPLYRECOMMENDATIONOPERATION_SITELINKEXTENSIONPARAMETERS']._serialized_end = 5321
    _globals['_APPLYRECOMMENDATIONOPERATION_CALLOUTASSETPARAMETERS']._serialized_start = 5324
    _globals['_APPLYRECOMMENDATIONOPERATION_CALLOUTASSETPARAMETERS']._serialized_end = 5476
    _globals['_APPLYRECOMMENDATIONOPERATION_CALLASSETPARAMETERS']._serialized_start = 5479
    _globals['_APPLYRECOMMENDATIONOPERATION_CALLASSETPARAMETERS']._serialized_end = 5628
    _globals['_APPLYRECOMMENDATIONOPERATION_SITELINKASSETPARAMETERS']._serialized_start = 5631
    _globals['_APPLYRECOMMENDATIONOPERATION_SITELINKASSETPARAMETERS']._serialized_end = 5784
    _globals['_APPLYRECOMMENDATIONOPERATION_RAISETARGETCPAPARAMETERS']._serialized_start = 5786
    _globals['_APPLYRECOMMENDATIONOPERATION_RAISETARGETCPAPARAMETERS']._serialized_end = 5848
    _globals['_APPLYRECOMMENDATIONOPERATION_LOWERTARGETROASPARAMETERS']._serialized_start = 5850
    _globals['_APPLYRECOMMENDATIONOPERATION_LOWERTARGETROASPARAMETERS']._serialized_end = 5914
    _globals['_APPLYRECOMMENDATIONOPERATION_ADASSETAPPLYPARAMETERS']._serialized_start = 5917
    _globals['_APPLYRECOMMENDATIONOPERATION_ADASSETAPPLYPARAMETERS']._serialized_end = 6220
    _globals['_APPLYRECOMMENDATIONOPERATION_ADASSETAPPLYPARAMETERS_APPLYSCOPE']._serialized_start = 6150
    _globals['_APPLYRECOMMENDATIONOPERATION_ADASSETAPPLYPARAMETERS_APPLYSCOPE']._serialized_end = 6220
    _globals['_APPLYRECOMMENDATIONOPERATION_MOVEUNUSEDBUDGETPARAMETERS']._serialized_start = 6222
    _globals['_APPLYRECOMMENDATIONOPERATION_MOVEUNUSEDBUDGETPARAMETERS']._serialized_end = 6312
    _globals['_APPLYRECOMMENDATIONOPERATION_RESPONSIVESEARCHADASSETPARAMETERS']._serialized_start = 6314
    _globals['_APPLYRECOMMENDATIONOPERATION_RESPONSIVESEARCHADASSETPARAMETERS']._serialized_end = 6409
    _globals['_APPLYRECOMMENDATIONOPERATION_RESPONSIVESEARCHADIMPROVEADSTRENGTHPARAMETERS']._serialized_start = 6411
    _globals['_APPLYRECOMMENDATIONOPERATION_RESPONSIVESEARCHADIMPROVEADSTRENGTHPARAMETERS']._serialized_end = 6518
    _globals['_APPLYRECOMMENDATIONOPERATION_RESPONSIVESEARCHADPARAMETERS']._serialized_start = 6520
    _globals['_APPLYRECOMMENDATIONOPERATION_RESPONSIVESEARCHADPARAMETERS']._serialized_end = 6607
    _globals['_APPLYRECOMMENDATIONOPERATION_RAISETARGETCPABIDTOOLOWPARAMETERS']._serialized_start = 6609
    _globals['_APPLYRECOMMENDATIONOPERATION_RAISETARGETCPABIDTOOLOWPARAMETERS']._serialized_end = 6676
    _globals['_APPLYRECOMMENDATIONOPERATION_USEBROADMATCHKEYWORDPARAMETERS']._serialized_start = 6678
    _globals['_APPLYRECOMMENDATIONOPERATION_USEBROADMATCHKEYWORDPARAMETERS']._serialized_end = 6778
    _globals['_APPLYRECOMMENDATIONOPERATION_FORECASTINGSETTARGETCPAPARAMETERS']._serialized_start = 6781
    _globals['_APPLYRECOMMENDATIONOPERATION_FORECASTINGSETTARGETCPAPARAMETERS']._serialized_end = 6948
    _globals['_APPLYRECOMMENDATIONOPERATION_LEADFORMASSETPARAMETERS']._serialized_start = 6951
    _globals['_APPLYRECOMMENDATIONOPERATION_LEADFORMASSETPARAMETERS']._serialized_end = 7204
    _globals['_APPLYRECOMMENDATIONRESPONSE']._serialized_start = 7227
    _globals['_APPLYRECOMMENDATIONRESPONSE']._serialized_end = 7386
    _globals['_APPLYRECOMMENDATIONRESULT']._serialized_start = 7388
    _globals['_APPLYRECOMMENDATIONRESULT']._serialized_end = 7484
    _globals['_DISMISSRECOMMENDATIONREQUEST']._serialized_start = 7487
    _globals['_DISMISSRECOMMENDATIONREQUEST']._serialized_end = 7746
    _globals['_DISMISSRECOMMENDATIONREQUEST_DISMISSRECOMMENDATIONOPERATION']._serialized_start = 7691
    _globals['_DISMISSRECOMMENDATIONREQUEST_DISMISSRECOMMENDATIONOPERATION']._serialized_end = 7746
    _globals['_DISMISSRECOMMENDATIONRESPONSE']._serialized_start = 7749
    _globals['_DISMISSRECOMMENDATIONRESPONSE']._serialized_end = 7996
    _globals['_DISMISSRECOMMENDATIONRESPONSE_DISMISSRECOMMENDATIONRESULT']._serialized_start = 7944
    _globals['_DISMISSRECOMMENDATIONRESPONSE_DISMISSRECOMMENDATIONRESULT']._serialized_end = 7996
    _globals['_GENERATERECOMMENDATIONSREQUEST']._serialized_start = 7999
    _globals['_GENERATERECOMMENDATIONSREQUEST']._serialized_end = 10773
    _globals['_GENERATERECOMMENDATIONSREQUEST_BIDDINGINFO']._serialized_start = 9373
    _globals['_GENERATERECOMMENDATIONSREQUEST_BIDDINGINFO']._serialized_end = 9748
    _globals['_GENERATERECOMMENDATIONSREQUEST_ADGROUPINFO']._serialized_start = 9751
    _globals['_GENERATERECOMMENDATIONSREQUEST_ADGROUPINFO']._serialized_end = 9945
    _globals['_GENERATERECOMMENDATIONSREQUEST_SEEDINFO']._serialized_start = 9947
    _globals['_GENERATERECOMMENDATIONSREQUEST_SEEDINFO']._serialized_end = 10021
    _globals['_GENERATERECOMMENDATIONSREQUEST_BUDGETINFO']._serialized_start = 10023
    _globals['_GENERATERECOMMENDATIONSREQUEST_BUDGETINFO']._serialized_end = 10088
    _globals['_GENERATERECOMMENDATIONSREQUEST_ASSETGROUPINFO']._serialized_start = 10090
    _globals['_GENERATERECOMMENDATIONSREQUEST_ASSETGROUPINFO']._serialized_end = 10198
    _globals['_GENERATERECOMMENDATIONSREQUEST_TARGETIMPRESSIONSHAREINFO']._serialized_start = 10201
    _globals['_GENERATERECOMMENDATIONSREQUEST_TARGETIMPRESSIONSHAREINFO']._serialized_end = 10514
    _globals['_GENERATERECOMMENDATIONSRESPONSE']._serialized_start = 10775
    _globals['_GENERATERECOMMENDATIONSRESPONSE']._serialized_end = 10885
    _globals['_RECOMMENDATIONSERVICE']._serialized_start = 10888
    _globals['_RECOMMENDATIONSERVICE']._serialized_end = 11763