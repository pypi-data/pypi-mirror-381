"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/common/asset_types.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.common import criteria_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_criteria__pb2
from ......google.ads.googleads.v19.common import feed_common_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_feed__common__pb2
from ......google.ads.googleads.v19.enums import business_message_call_to_action_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_business__message__call__to__action__type__pb2
from ......google.ads.googleads.v19.enums import business_message_provider_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_business__message__provider__pb2
from ......google.ads.googleads.v19.enums import call_conversion_reporting_state_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_call__conversion__reporting__state__pb2
from ......google.ads.googleads.v19.enums import call_to_action_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_call__to__action__type__pb2
from ......google.ads.googleads.v19.enums import lead_form_call_to_action_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_lead__form__call__to__action__type__pb2
from ......google.ads.googleads.v19.enums import lead_form_desired_intent_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_lead__form__desired__intent__pb2
from ......google.ads.googleads.v19.enums import lead_form_field_user_input_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_lead__form__field__user__input__type__pb2
from ......google.ads.googleads.v19.enums import lead_form_post_submit_call_to_action_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_lead__form__post__submit__call__to__action__type__pb2
from ......google.ads.googleads.v19.enums import location_ownership_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_location__ownership__type__pb2
from ......google.ads.googleads.v19.enums import mime_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_mime__type__pb2
from ......google.ads.googleads.v19.enums import mobile_app_vendor_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_mobile__app__vendor__pb2
from ......google.ads.googleads.v19.enums import price_extension_price_qualifier_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_price__extension__price__qualifier__pb2
from ......google.ads.googleads.v19.enums import price_extension_price_unit_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_price__extension__price__unit__pb2
from ......google.ads.googleads.v19.enums import price_extension_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_price__extension__type__pb2
from ......google.ads.googleads.v19.enums import promotion_extension_discount_modifier_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_promotion__extension__discount__modifier__pb2
from ......google.ads.googleads.v19.enums import promotion_extension_occasion_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_promotion__extension__occasion__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/ads/googleads/v19/common/asset_types.proto\x12\x1fgoogle.ads.googleads.v19.common\x1a.google/ads/googleads/v19/common/criteria.proto\x1a1google/ads/googleads/v19/common/feed_common.proto\x1aIgoogle/ads/googleads/v19/enums/business_message_call_to_action_type.proto\x1a>google/ads/googleads/v19/enums/business_message_provider.proto\x1aDgoogle/ads/googleads/v19/enums/call_conversion_reporting_state.proto\x1a8google/ads/googleads/v19/enums/call_to_action_type.proto\x1aBgoogle/ads/googleads/v19/enums/lead_form_call_to_action_type.proto\x1a=google/ads/googleads/v19/enums/lead_form_desired_intent.proto\x1aDgoogle/ads/googleads/v19/enums/lead_form_field_user_input_type.proto\x1aNgoogle/ads/googleads/v19/enums/lead_form_post_submit_call_to_action_type.proto\x1a<google/ads/googleads/v19/enums/location_ownership_type.proto\x1a.google/ads/googleads/v19/enums/mime_type.proto\x1a6google/ads/googleads/v19/enums/mobile_app_vendor.proto\x1aDgoogle/ads/googleads/v19/enums/price_extension_price_qualifier.proto\x1a?google/ads/googleads/v19/enums/price_extension_price_unit.proto\x1a9google/ads/googleads/v19/enums/price_extension_type.proto\x1aJgoogle/ads/googleads/v19/enums/promotion_extension_discount_modifier.proto\x1aAgoogle/ads/googleads/v19/enums/promotion_extension_occasion.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"d\n\x11YoutubeVideoAsset\x12\x1d\n\x10youtube_video_id\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x13youtube_video_title\x18\x03 \x01(\tB\x13\n\x11_youtube_video_id".\n\x10MediaBundleAsset\x12\x11\n\x04data\x18\x02 \x01(\x0cH\x00\x88\x01\x01B\x07\n\x05_data"\xdc\x01\n\nImageAsset\x12\x11\n\x04data\x18\x05 \x01(\x0cH\x00\x88\x01\x01\x12\x16\n\tfile_size\x18\x06 \x01(\x03H\x01\x88\x01\x01\x12H\n\tmime_type\x18\x03 \x01(\x0e25.google.ads.googleads.v19.enums.MimeTypeEnum.MimeType\x12B\n\tfull_size\x18\x04 \x01(\x0b2/.google.ads.googleads.v19.common.ImageDimensionB\x07\n\x05_dataB\x0c\n\n_file_size"\x84\x01\n\x0eImageDimension\x12\x1a\n\rheight_pixels\x18\x04 \x01(\x03H\x00\x88\x01\x01\x12\x19\n\x0cwidth_pixels\x18\x05 \x01(\x03H\x01\x88\x01\x01\x12\x10\n\x03url\x18\x06 \x01(\tH\x02\x88\x01\x01B\x10\n\x0e_height_pixelsB\x0f\n\r_width_pixelsB\x06\n\x04_url"\'\n\tTextAsset\x12\x11\n\x04text\x18\x02 \x01(\tH\x00\x88\x01\x01B\x07\n\x05_text"\x82\x08\n\rLeadFormAsset\x12\x1a\n\rbusiness_name\x18\n \x01(\tB\x03\xe0A\x02\x12w\n\x13call_to_action_type\x18\x11 \x01(\x0e2U.google.ads.googleads.v19.enums.LeadFormCallToActionTypeEnum.LeadFormCallToActionTypeB\x03\xe0A\x02\x12\'\n\x1acall_to_action_description\x18\x12 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08headline\x18\x0c \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\r \x01(\tB\x03\xe0A\x02\x12\x1f\n\x12privacy_policy_url\x18\x0e \x01(\tB\x03\xe0A\x02\x12!\n\x14post_submit_headline\x18\x0f \x01(\tH\x00\x88\x01\x01\x12$\n\x17post_submit_description\x18\x10 \x01(\tH\x01\x88\x01\x01\x12>\n\x06fields\x18\x08 \x03(\x0b2..google.ads.googleads.v19.common.LeadFormField\x12\\\n\x16custom_question_fields\x18\x17 \x03(\x0b2<.google.ads.googleads.v19.common.LeadFormCustomQuestionField\x12Q\n\x10delivery_methods\x18\t \x03(\x0b27.google.ads.googleads.v19.common.LeadFormDeliveryMethod\x12\x92\x01\n\x1fpost_submit_call_to_action_type\x18\x13 \x01(\x0e2i.google.ads.googleads.v19.enums.LeadFormPostSubmitCallToActionTypeEnum.LeadFormPostSubmitCallToActionType\x12#\n\x16background_image_asset\x18\x14 \x01(\tH\x02\x88\x01\x01\x12g\n\x0edesired_intent\x18\x15 \x01(\x0e2O.google.ads.googleads.v19.enums.LeadFormDesiredIntentEnum.LeadFormDesiredIntent\x12\x1e\n\x11custom_disclosure\x18\x16 \x01(\tH\x03\x88\x01\x01B\x17\n\x15_post_submit_headlineB\x1a\n\x18_post_submit_descriptionB\x19\n\x17_background_image_assetB\x14\n\x12_custom_disclosure"\x87\x02\n\rLeadFormField\x12m\n\ninput_type\x18\x01 \x01(\x0e2Y.google.ads.googleads.v19.enums.LeadFormFieldUserInputTypeEnum.LeadFormFieldUserInputType\x12]\n\x15single_choice_answers\x18\x02 \x01(\x0b2<.google.ads.googleads.v19.common.LeadFormSingleChoiceAnswersH\x00\x12\x1d\n\x13has_location_answer\x18\x03 \x01(\x08H\x00B\t\n\x07answers"\xc4\x01\n\x1bLeadFormCustomQuestionField\x12\x1c\n\x14custom_question_text\x18\x01 \x01(\t\x12]\n\x15single_choice_answers\x18\x02 \x01(\x0b2<.google.ads.googleads.v19.common.LeadFormSingleChoiceAnswersH\x00\x12\x1d\n\x13has_location_answer\x18\x03 \x01(\x08H\x00B\t\n\x07answers".\n\x1bLeadFormSingleChoiceAnswers\x12\x0f\n\x07answers\x18\x01 \x03(\t"q\n\x16LeadFormDeliveryMethod\x12C\n\x07webhook\x18\x01 \x01(\x0b20.google.ads.googleads.v19.common.WebhookDeliveryH\x00B\x12\n\x10delivery_details"\xbf\x01\n\x0fWebhookDelivery\x12#\n\x16advertiser_webhook_url\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rgoogle_secret\x18\x05 \x01(\tH\x01\x88\x01\x01\x12#\n\x16payload_schema_version\x18\x06 \x01(\x03H\x02\x88\x01\x01B\x19\n\x17_advertiser_webhook_urlB\x10\n\x0e_google_secretB\x19\n\x17_payload_schema_version"\x13\n\x11BookOnGoogleAsset"\xcb\x05\n\x0ePromotionAsset\x12\x1d\n\x10promotion_target\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x84\x01\n\x11discount_modifier\x18\x02 \x01(\x0e2i.google.ads.googleads.v19.enums.PromotionExtensionDiscountModifierEnum.PromotionExtensionDiscountModifier\x12\x1d\n\x15redemption_start_date\x18\x07 \x01(\t\x12\x1b\n\x13redemption_end_date\x18\x08 \x01(\t\x12k\n\x08occasion\x18\t \x01(\x0e2Y.google.ads.googleads.v19.enums.PromotionExtensionOccasionEnum.PromotionExtensionOccasion\x12\x15\n\rlanguage_code\x18\n \x01(\t\x12\x12\n\nstart_date\x18\x0b \x01(\t\x12\x10\n\x08end_date\x18\x0c \x01(\t\x12L\n\x13ad_schedule_targets\x18\r \x03(\x0b2/.google.ads.googleads.v19.common.AdScheduleInfo\x12\x15\n\x0bpercent_off\x18\x03 \x01(\x03H\x00\x12B\n\x10money_amount_off\x18\x04 \x01(\x0b2&.google.ads.googleads.v19.common.MoneyH\x00\x12\x18\n\x0epromotion_code\x18\x05 \x01(\tH\x01\x12D\n\x12orders_over_amount\x18\x06 \x01(\x0b2&.google.ads.googleads.v19.common.MoneyH\x01B\x0f\n\rdiscount_typeB\x13\n\x11promotion_trigger"\x9d\x01\n\x0cCalloutAsset\x12\x19\n\x0ccallout_text\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\nstart_date\x18\x02 \x01(\t\x12\x10\n\x08end_date\x18\x03 \x01(\t\x12L\n\x13ad_schedule_targets\x18\x04 \x03(\x0b2/.google.ads.googleads.v19.common.AdScheduleInfo"B\n\x16StructuredSnippetAsset\x12\x13\n\x06header\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06values\x18\x02 \x03(\tB\x03\xe0A\x02"\xc7\x01\n\rSitelinkAsset\x12\x16\n\tlink_text\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x0cdescription1\x18\x02 \x01(\t\x12\x14\n\x0cdescription2\x18\x03 \x01(\t\x12\x12\n\nstart_date\x18\x04 \x01(\t\x12\x10\n\x08end_date\x18\x05 \x01(\t\x12L\n\x13ad_schedule_targets\x18\x06 \x03(\x0b2/.google.ads.googleads.v19.common.AdScheduleInfo"6\n\rPageFeedAsset\x12\x15\n\x08page_url\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x0e\n\x06labels\x18\x02 \x03(\t"\xe8\x02\n\x15DynamicEducationAsset\x12\x17\n\nprogram_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0blocation_id\x18\x02 \x01(\t\x12\x19\n\x0cprogram_name\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x0f\n\x07subject\x18\x04 \x01(\t\x12\x1b\n\x13program_description\x18\x05 \x01(\t\x12\x13\n\x0bschool_name\x18\x06 \x01(\t\x12\x0f\n\x07address\x18\x07 \x01(\t\x12\x1b\n\x13contextual_keywords\x18\x08 \x03(\t\x12\x18\n\x10android_app_link\x18\t \x01(\t\x12\x1b\n\x13similar_program_ids\x18\n \x03(\t\x12\x14\n\x0cios_app_link\x18\x0b \x01(\t\x12\x18\n\x10ios_app_store_id\x18\x0c \x01(\x03\x12\x1b\n\x13thumbnail_image_url\x18\r \x01(\t\x12\x11\n\timage_url\x18\x0e \x01(\t"\xc0\x01\n\x0eMobileAppAsset\x12\x13\n\x06app_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12[\n\tapp_store\x18\x02 \x01(\x0e2C.google.ads.googleads.v19.enums.MobileAppVendorEnum.MobileAppVendorB\x03\xe0A\x02\x12\x16\n\tlink_text\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x12\n\nstart_date\x18\x04 \x01(\t\x12\x10\n\x08end_date\x18\x05 \x01(\t"B\n\x11HotelCalloutAsset\x12\x11\n\x04text\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rlanguage_code\x18\x02 \x01(\tB\x03\xe0A\x02"\xe8\x02\n\tCallAsset\x12\x19\n\x0ccountry_code\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0cphone_number\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x86\x01\n\x1fcall_conversion_reporting_state\x18\x03 \x01(\x0e2].google.ads.googleads.v19.enums.CallConversionReportingStateEnum.CallConversionReportingState\x12N\n\x16call_conversion_action\x18\x04 \x01(\tB.\xfaA+\n)googleads.googleapis.com/ConversionAction\x12L\n\x13ad_schedule_targets\x18\x05 \x03(\x0b2/.google.ads.googleads.v19.common.AdScheduleInfo"\xc7\x02\n\nPriceAsset\x12\\\n\x04type\x18\x01 \x01(\x0e2I.google.ads.googleads.v19.enums.PriceExtensionTypeEnum.PriceExtensionTypeB\x03\xe0A\x02\x12v\n\x0fprice_qualifier\x18\x02 \x01(\x0e2].google.ads.googleads.v19.enums.PriceExtensionPriceQualifierEnum.PriceExtensionPriceQualifier\x12\x1a\n\rlanguage_code\x18\x03 \x01(\tB\x03\xe0A\x02\x12G\n\x0fprice_offerings\x18\x04 \x03(\x0b2..google.ads.googleads.v19.common.PriceOffering"\x8f\x02\n\rPriceOffering\x12\x13\n\x06header\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x02\x12:\n\x05price\x18\x03 \x01(\x0b2&.google.ads.googleads.v19.common.MoneyB\x03\xe0A\x02\x12a\n\x04unit\x18\x04 \x01(\x0e2S.google.ads.googleads.v19.enums.PriceExtensionPriceUnitEnum.PriceExtensionPriceUnit\x12\x16\n\tfinal_url\x18\x05 \x01(\tB\x03\xe0A\x02\x12\x18\n\x10final_mobile_url\x18\x06 \x01(\t"r\n\x11CallToActionAsset\x12]\n\x0ecall_to_action\x18\x01 \x01(\x0e2E.google.ads.googleads.v19.enums.CallToActionTypeEnum.CallToActionType"\xf1\x02\n\x16DynamicRealEstateAsset\x12\x17\n\nlisting_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0clisting_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x11\n\tcity_name\x18\x03 \x01(\t\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x12\x0f\n\x07address\x18\x05 \x01(\t\x12\r\n\x05price\x18\x06 \x01(\t\x12\x11\n\timage_url\x18\x07 \x01(\t\x12\x15\n\rproperty_type\x18\x08 \x01(\t\x12\x14\n\x0clisting_type\x18\t \x01(\t\x12\x1b\n\x13contextual_keywords\x18\n \x03(\t\x12\x17\n\x0fformatted_price\x18\x0b \x01(\t\x12\x18\n\x10android_app_link\x18\x0c \x01(\t\x12\x14\n\x0cios_app_link\x18\r \x01(\t\x12\x18\n\x10ios_app_store_id\x18\x0e \x01(\x03\x12\x1b\n\x13similar_listing_ids\x18\x0f \x03(\t"\x92\x03\n\x12DynamicCustomAsset\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x0b\n\x03id2\x18\x02 \x01(\t\x12\x17\n\nitem_title\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x15\n\ritem_subtitle\x18\x04 \x01(\t\x12\x18\n\x10item_description\x18\x05 \x01(\t\x12\x14\n\x0citem_address\x18\x06 \x01(\t\x12\x15\n\ritem_category\x18\x07 \x01(\t\x12\r\n\x05price\x18\x08 \x01(\t\x12\x12\n\nsale_price\x18\t \x01(\t\x12\x17\n\x0fformatted_price\x18\n \x01(\t\x12\x1c\n\x14formatted_sale_price\x18\x0b \x01(\t\x12\x11\n\timage_url\x18\x0c \x01(\t\x12\x1b\n\x13contextual_keywords\x18\r \x03(\t\x12\x18\n\x10android_app_link\x18\x0e \x01(\t\x12\x14\n\x0cios_app_link\x18\x10 \x01(\t\x12\x18\n\x10ios_app_store_id\x18\x11 \x01(\x03\x12\x13\n\x0bsimilar_ids\x18\x0f \x03(\t"\xad\x03\n\x1cDynamicHotelsAndRentalsAsset\x12\x18\n\x0bproperty_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rproperty_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x11\n\timage_url\x18\x03 \x01(\t\x12\x18\n\x10destination_name\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t\x12\r\n\x05price\x18\x06 \x01(\t\x12\x12\n\nsale_price\x18\x07 \x01(\t\x12\x13\n\x0bstar_rating\x18\x08 \x01(\x03\x12\x10\n\x08category\x18\t \x01(\t\x12\x1b\n\x13contextual_keywords\x18\n \x03(\t\x12\x0f\n\x07address\x18\x0b \x01(\t\x12\x18\n\x10android_app_link\x18\x0c \x01(\t\x12\x14\n\x0cios_app_link\x18\r \x01(\t\x12\x18\n\x10ios_app_store_id\x18\x0e \x01(\x03\x12\x17\n\x0fformatted_price\x18\x0f \x01(\t\x12\x1c\n\x14formatted_sale_price\x18\x10 \x01(\t\x12\x1c\n\x14similar_property_ids\x18\x11 \x03(\t"\x93\x03\n\x13DynamicFlightsAsset\x12\x1b\n\x0edestination_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\torigin_id\x18\x02 \x01(\t\x12\x1f\n\x12flight_description\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x11\n\timage_url\x18\x04 \x01(\t\x12\x18\n\x10destination_name\x18\x05 \x01(\t\x12\x13\n\x0borigin_name\x18\x06 \x01(\t\x12\x14\n\x0cflight_price\x18\x07 \x01(\t\x12\x19\n\x11flight_sale_price\x18\x08 \x01(\t\x12\x17\n\x0fformatted_price\x18\t \x01(\t\x12\x1c\n\x14formatted_sale_price\x18\n \x01(\t\x12\x18\n\x10android_app_link\x18\x0b \x01(\t\x12\x14\n\x0cios_app_link\x18\x0c \x01(\t\x12\x18\n\x10ios_app_store_id\x18\r \x01(\x03\x12\x1f\n\x17similar_destination_ids\x18\x0e \x03(\t\x12\x16\n\x0ecustom_mapping\x18\x0f \x01(\t"\xbd\x01\n\x1aDemandGenCarouselCardAsset\x12\x1d\n\x15marketing_image_asset\x18\x01 \x01(\t\x12$\n\x1csquare_marketing_image_asset\x18\x02 \x01(\t\x12&\n\x1eportrait_marketing_image_asset\x18\x03 \x01(\t\x12\x15\n\x08headline\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x13call_to_action_text\x18\x05 \x01(\t"\xab\x03\n\x12DynamicTravelAsset\x12\x1b\n\x0edestination_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\torigin_id\x18\x02 \x01(\t\x12\x12\n\x05title\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x18\n\x10destination_name\x18\x04 \x01(\t\x12\x1b\n\x13destination_address\x18\x05 \x01(\t\x12\x13\n\x0borigin_name\x18\x06 \x01(\t\x12\r\n\x05price\x18\x07 \x01(\t\x12\x12\n\nsale_price\x18\x08 \x01(\t\x12\x17\n\x0fformatted_price\x18\t \x01(\t\x12\x1c\n\x14formatted_sale_price\x18\n \x01(\t\x12\x10\n\x08category\x18\x0b \x01(\t\x12\x1b\n\x13contextual_keywords\x18\x0c \x03(\t\x12\x1f\n\x17similar_destination_ids\x18\r \x03(\t\x12\x11\n\timage_url\x18\x0e \x01(\t\x12\x18\n\x10android_app_link\x18\x0f \x01(\t\x12\x14\n\x0cios_app_link\x18\x10 \x01(\t\x12\x18\n\x10ios_app_store_id\x18\x11 \x01(\x03"\xf9\x02\n\x11DynamicLocalAsset\x12\x14\n\x07deal_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tdeal_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x10\n\x08subtitle\x18\x03 \x01(\t\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x12\r\n\x05price\x18\x05 \x01(\t\x12\x12\n\nsale_price\x18\x06 \x01(\t\x12\x11\n\timage_url\x18\x07 \x01(\t\x12\x0f\n\x07address\x18\x08 \x01(\t\x12\x10\n\x08category\x18\t \x01(\t\x12\x1b\n\x13contextual_keywords\x18\n \x03(\t\x12\x17\n\x0fformatted_price\x18\x0b \x01(\t\x12\x1c\n\x14formatted_sale_price\x18\x0c \x01(\t\x12\x18\n\x10android_app_link\x18\r \x01(\t\x12\x18\n\x10similar_deal_ids\x18\x0e \x03(\t\x12\x14\n\x0cios_app_link\x18\x0f \x01(\t\x12\x18\n\x10ios_app_store_id\x18\x10 \x01(\x03"\xc9\x02\n\x10DynamicJobsAsset\x12\x13\n\x06job_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0blocation_id\x18\x02 \x01(\t\x12\x16\n\tjob_title\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x14\n\x0cjob_subtitle\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t\x12\x11\n\timage_url\x18\x06 \x01(\t\x12\x14\n\x0cjob_category\x18\x07 \x01(\t\x12\x1b\n\x13contextual_keywords\x18\x08 \x03(\t\x12\x0f\n\x07address\x18\t \x01(\t\x12\x0e\n\x06salary\x18\n \x01(\t\x12\x18\n\x10android_app_link\x18\x0b \x01(\t\x12\x17\n\x0fsimilar_job_ids\x18\x0c \x03(\t\x12\x14\n\x0cios_app_link\x18\r \x01(\t\x12\x18\n\x10ios_app_store_id\x18\x0e \x01(\x03"\xf1\x01\n\rLocationAsset\x12\x10\n\x08place_id\x18\x01 \x01(\t\x12\\\n\x1abusiness_profile_locations\x18\x02 \x03(\x0b28.google.ads.googleads.v19.common.BusinessProfileLocation\x12p\n\x17location_ownership_type\x18\x03 \x01(\x0e2O.google.ads.googleads.v19.enums.LocationOwnershipTypeEnum.LocationOwnershipType"Q\n\x17BusinessProfileLocation\x12\x0e\n\x06labels\x18\x01 \x03(\t\x12\x12\n\nstore_code\x18\x02 \x01(\t\x12\x12\n\nlisting_id\x18\x03 \x01(\x03"Q\n\x12HotelPropertyAsset\x12\x10\n\x08place_id\x18\x01 \x01(\t\x12\x15\n\rhotel_address\x18\x02 \x01(\t\x12\x12\n\nhotel_name\x18\x03 \x01(\t"\x8a\x03\n\x14BusinessMessageAsset\x12r\n\x10message_provider\x18\x01 \x01(\x0e2S.google.ads.googleads.v19.enums.BusinessMessageProviderEnum.BusinessMessageProviderB\x03\xe0A\x02\x12\x1c\n\x0fstarter_message\x18\x02 \x01(\tB\x03\xe0A\x02\x12]\n\x0ecall_to_action\x18\x03 \x01(\x0b2@.google.ads.googleads.v19.common.BusinessMessageCallToActionInfoH\x01\x88\x01\x01\x12U\n\rwhatsapp_info\x18\x05 \x01(\x0b2<.google.ads.googleads.v19.common.WhatsappBusinessMessageInfoH\x00B\x17\n\x15message_provider_dataB\x11\n\x0f_call_to_action"S\n\x1bWhatsappBusinessMessageInfo\x12\x19\n\x0ccountry_code\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0cphone_number\x18\x02 \x01(\tB\x03\xe0A\x02"\xd7\x01\n\x1fBusinessMessageCallToActionInfo\x12\x8a\x01\n\x18call_to_action_selection\x18\x01 \x01(\x0e2c.google.ads.googleads.v19.enums.BusinessMessageCallToActionTypeEnum.BusinessMessageCallToActionTypeB\x03\xe0A\x02\x12\'\n\x1acall_to_action_description\x18\x02 \x01(\tB\x03\xe0A\x02"-\n\x10AppDeepLinkAsset\x12\x19\n\x11app_deep_link_uri\x18\x01 \x01(\tB\xef\x01\n#com.google.ads.googleads.v19.commonB\x0fAssetTypesProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v19/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V19.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V19\\Common\xea\x02#Google::Ads::GoogleAds::V19::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.common.asset_types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v19.commonB\x0fAssetTypesProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v19/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V19.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V19\\Common\xea\x02#Google::Ads::GoogleAds::V19::Common'
    _globals['_LEADFORMASSET'].fields_by_name['business_name']._loaded_options = None
    _globals['_LEADFORMASSET'].fields_by_name['business_name']._serialized_options = b'\xe0A\x02'
    _globals['_LEADFORMASSET'].fields_by_name['call_to_action_type']._loaded_options = None
    _globals['_LEADFORMASSET'].fields_by_name['call_to_action_type']._serialized_options = b'\xe0A\x02'
    _globals['_LEADFORMASSET'].fields_by_name['call_to_action_description']._loaded_options = None
    _globals['_LEADFORMASSET'].fields_by_name['call_to_action_description']._serialized_options = b'\xe0A\x02'
    _globals['_LEADFORMASSET'].fields_by_name['headline']._loaded_options = None
    _globals['_LEADFORMASSET'].fields_by_name['headline']._serialized_options = b'\xe0A\x02'
    _globals['_LEADFORMASSET'].fields_by_name['description']._loaded_options = None
    _globals['_LEADFORMASSET'].fields_by_name['description']._serialized_options = b'\xe0A\x02'
    _globals['_LEADFORMASSET'].fields_by_name['privacy_policy_url']._loaded_options = None
    _globals['_LEADFORMASSET'].fields_by_name['privacy_policy_url']._serialized_options = b'\xe0A\x02'
    _globals['_PROMOTIONASSET'].fields_by_name['promotion_target']._loaded_options = None
    _globals['_PROMOTIONASSET'].fields_by_name['promotion_target']._serialized_options = b'\xe0A\x02'
    _globals['_CALLOUTASSET'].fields_by_name['callout_text']._loaded_options = None
    _globals['_CALLOUTASSET'].fields_by_name['callout_text']._serialized_options = b'\xe0A\x02'
    _globals['_STRUCTUREDSNIPPETASSET'].fields_by_name['header']._loaded_options = None
    _globals['_STRUCTUREDSNIPPETASSET'].fields_by_name['header']._serialized_options = b'\xe0A\x02'
    _globals['_STRUCTUREDSNIPPETASSET'].fields_by_name['values']._loaded_options = None
    _globals['_STRUCTUREDSNIPPETASSET'].fields_by_name['values']._serialized_options = b'\xe0A\x02'
    _globals['_SITELINKASSET'].fields_by_name['link_text']._loaded_options = None
    _globals['_SITELINKASSET'].fields_by_name['link_text']._serialized_options = b'\xe0A\x02'
    _globals['_PAGEFEEDASSET'].fields_by_name['page_url']._loaded_options = None
    _globals['_PAGEFEEDASSET'].fields_by_name['page_url']._serialized_options = b'\xe0A\x02'
    _globals['_DYNAMICEDUCATIONASSET'].fields_by_name['program_id']._loaded_options = None
    _globals['_DYNAMICEDUCATIONASSET'].fields_by_name['program_id']._serialized_options = b'\xe0A\x02'
    _globals['_DYNAMICEDUCATIONASSET'].fields_by_name['program_name']._loaded_options = None
    _globals['_DYNAMICEDUCATIONASSET'].fields_by_name['program_name']._serialized_options = b'\xe0A\x02'
    _globals['_MOBILEAPPASSET'].fields_by_name['app_id']._loaded_options = None
    _globals['_MOBILEAPPASSET'].fields_by_name['app_id']._serialized_options = b'\xe0A\x02'
    _globals['_MOBILEAPPASSET'].fields_by_name['app_store']._loaded_options = None
    _globals['_MOBILEAPPASSET'].fields_by_name['app_store']._serialized_options = b'\xe0A\x02'
    _globals['_MOBILEAPPASSET'].fields_by_name['link_text']._loaded_options = None
    _globals['_MOBILEAPPASSET'].fields_by_name['link_text']._serialized_options = b'\xe0A\x02'
    _globals['_HOTELCALLOUTASSET'].fields_by_name['text']._loaded_options = None
    _globals['_HOTELCALLOUTASSET'].fields_by_name['text']._serialized_options = b'\xe0A\x02'
    _globals['_HOTELCALLOUTASSET'].fields_by_name['language_code']._loaded_options = None
    _globals['_HOTELCALLOUTASSET'].fields_by_name['language_code']._serialized_options = b'\xe0A\x02'
    _globals['_CALLASSET'].fields_by_name['country_code']._loaded_options = None
    _globals['_CALLASSET'].fields_by_name['country_code']._serialized_options = b'\xe0A\x02'
    _globals['_CALLASSET'].fields_by_name['phone_number']._loaded_options = None
    _globals['_CALLASSET'].fields_by_name['phone_number']._serialized_options = b'\xe0A\x02'
    _globals['_CALLASSET'].fields_by_name['call_conversion_action']._loaded_options = None
    _globals['_CALLASSET'].fields_by_name['call_conversion_action']._serialized_options = b'\xfaA+\n)googleads.googleapis.com/ConversionAction'
    _globals['_PRICEASSET'].fields_by_name['type']._loaded_options = None
    _globals['_PRICEASSET'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_PRICEASSET'].fields_by_name['language_code']._loaded_options = None
    _globals['_PRICEASSET'].fields_by_name['language_code']._serialized_options = b'\xe0A\x02'
    _globals['_PRICEOFFERING'].fields_by_name['header']._loaded_options = None
    _globals['_PRICEOFFERING'].fields_by_name['header']._serialized_options = b'\xe0A\x02'
    _globals['_PRICEOFFERING'].fields_by_name['description']._loaded_options = None
    _globals['_PRICEOFFERING'].fields_by_name['description']._serialized_options = b'\xe0A\x02'
    _globals['_PRICEOFFERING'].fields_by_name['price']._loaded_options = None
    _globals['_PRICEOFFERING'].fields_by_name['price']._serialized_options = b'\xe0A\x02'
    _globals['_PRICEOFFERING'].fields_by_name['final_url']._loaded_options = None
    _globals['_PRICEOFFERING'].fields_by_name['final_url']._serialized_options = b'\xe0A\x02'
    _globals['_DYNAMICREALESTATEASSET'].fields_by_name['listing_id']._loaded_options = None
    _globals['_DYNAMICREALESTATEASSET'].fields_by_name['listing_id']._serialized_options = b'\xe0A\x02'
    _globals['_DYNAMICREALESTATEASSET'].fields_by_name['listing_name']._loaded_options = None
    _globals['_DYNAMICREALESTATEASSET'].fields_by_name['listing_name']._serialized_options = b'\xe0A\x02'
    _globals['_DYNAMICCUSTOMASSET'].fields_by_name['id']._loaded_options = None
    _globals['_DYNAMICCUSTOMASSET'].fields_by_name['id']._serialized_options = b'\xe0A\x02'
    _globals['_DYNAMICCUSTOMASSET'].fields_by_name['item_title']._loaded_options = None
    _globals['_DYNAMICCUSTOMASSET'].fields_by_name['item_title']._serialized_options = b'\xe0A\x02'
    _globals['_DYNAMICHOTELSANDRENTALSASSET'].fields_by_name['property_id']._loaded_options = None
    _globals['_DYNAMICHOTELSANDRENTALSASSET'].fields_by_name['property_id']._serialized_options = b'\xe0A\x02'
    _globals['_DYNAMICHOTELSANDRENTALSASSET'].fields_by_name['property_name']._loaded_options = None
    _globals['_DYNAMICHOTELSANDRENTALSASSET'].fields_by_name['property_name']._serialized_options = b'\xe0A\x02'
    _globals['_DYNAMICFLIGHTSASSET'].fields_by_name['destination_id']._loaded_options = None
    _globals['_DYNAMICFLIGHTSASSET'].fields_by_name['destination_id']._serialized_options = b'\xe0A\x02'
    _globals['_DYNAMICFLIGHTSASSET'].fields_by_name['flight_description']._loaded_options = None
    _globals['_DYNAMICFLIGHTSASSET'].fields_by_name['flight_description']._serialized_options = b'\xe0A\x02'
    _globals['_DEMANDGENCAROUSELCARDASSET'].fields_by_name['headline']._loaded_options = None
    _globals['_DEMANDGENCAROUSELCARDASSET'].fields_by_name['headline']._serialized_options = b'\xe0A\x02'
    _globals['_DYNAMICTRAVELASSET'].fields_by_name['destination_id']._loaded_options = None
    _globals['_DYNAMICTRAVELASSET'].fields_by_name['destination_id']._serialized_options = b'\xe0A\x02'
    _globals['_DYNAMICTRAVELASSET'].fields_by_name['title']._loaded_options = None
    _globals['_DYNAMICTRAVELASSET'].fields_by_name['title']._serialized_options = b'\xe0A\x02'
    _globals['_DYNAMICLOCALASSET'].fields_by_name['deal_id']._loaded_options = None
    _globals['_DYNAMICLOCALASSET'].fields_by_name['deal_id']._serialized_options = b'\xe0A\x02'
    _globals['_DYNAMICLOCALASSET'].fields_by_name['deal_name']._loaded_options = None
    _globals['_DYNAMICLOCALASSET'].fields_by_name['deal_name']._serialized_options = b'\xe0A\x02'
    _globals['_DYNAMICJOBSASSET'].fields_by_name['job_id']._loaded_options = None
    _globals['_DYNAMICJOBSASSET'].fields_by_name['job_id']._serialized_options = b'\xe0A\x02'
    _globals['_DYNAMICJOBSASSET'].fields_by_name['job_title']._loaded_options = None
    _globals['_DYNAMICJOBSASSET'].fields_by_name['job_title']._serialized_options = b'\xe0A\x02'
    _globals['_BUSINESSMESSAGEASSET'].fields_by_name['message_provider']._loaded_options = None
    _globals['_BUSINESSMESSAGEASSET'].fields_by_name['message_provider']._serialized_options = b'\xe0A\x02'
    _globals['_BUSINESSMESSAGEASSET'].fields_by_name['starter_message']._loaded_options = None
    _globals['_BUSINESSMESSAGEASSET'].fields_by_name['starter_message']._serialized_options = b'\xe0A\x02'
    _globals['_WHATSAPPBUSINESSMESSAGEINFO'].fields_by_name['country_code']._loaded_options = None
    _globals['_WHATSAPPBUSINESSMESSAGEINFO'].fields_by_name['country_code']._serialized_options = b'\xe0A\x02'
    _globals['_WHATSAPPBUSINESSMESSAGEINFO'].fields_by_name['phone_number']._loaded_options = None
    _globals['_WHATSAPPBUSINESSMESSAGEINFO'].fields_by_name['phone_number']._serialized_options = b'\xe0A\x02'
    _globals['_BUSINESSMESSAGECALLTOACTIONINFO'].fields_by_name['call_to_action_selection']._loaded_options = None
    _globals['_BUSINESSMESSAGECALLTOACTIONINFO'].fields_by_name['call_to_action_selection']._serialized_options = b'\xe0A\x02'
    _globals['_BUSINESSMESSAGECALLTOACTIONINFO'].fields_by_name['call_to_action_description']._loaded_options = None
    _globals['_BUSINESSMESSAGECALLTOACTIONINFO'].fields_by_name['call_to_action_description']._serialized_options = b'\xe0A\x02'
    _globals['_YOUTUBEVIDEOASSET']._serialized_start = 1296
    _globals['_YOUTUBEVIDEOASSET']._serialized_end = 1396
    _globals['_MEDIABUNDLEASSET']._serialized_start = 1398
    _globals['_MEDIABUNDLEASSET']._serialized_end = 1444
    _globals['_IMAGEASSET']._serialized_start = 1447
    _globals['_IMAGEASSET']._serialized_end = 1667
    _globals['_IMAGEDIMENSION']._serialized_start = 1670
    _globals['_IMAGEDIMENSION']._serialized_end = 1802
    _globals['_TEXTASSET']._serialized_start = 1804
    _globals['_TEXTASSET']._serialized_end = 1843
    _globals['_LEADFORMASSET']._serialized_start = 1846
    _globals['_LEADFORMASSET']._serialized_end = 2872
    _globals['_LEADFORMFIELD']._serialized_start = 2875
    _globals['_LEADFORMFIELD']._serialized_end = 3138
    _globals['_LEADFORMCUSTOMQUESTIONFIELD']._serialized_start = 3141
    _globals['_LEADFORMCUSTOMQUESTIONFIELD']._serialized_end = 3337
    _globals['_LEADFORMSINGLECHOICEANSWERS']._serialized_start = 3339
    _globals['_LEADFORMSINGLECHOICEANSWERS']._serialized_end = 3385
    _globals['_LEADFORMDELIVERYMETHOD']._serialized_start = 3387
    _globals['_LEADFORMDELIVERYMETHOD']._serialized_end = 3500
    _globals['_WEBHOOKDELIVERY']._serialized_start = 3503
    _globals['_WEBHOOKDELIVERY']._serialized_end = 3694
    _globals['_BOOKONGOOGLEASSET']._serialized_start = 3696
    _globals['_BOOKONGOOGLEASSET']._serialized_end = 3715
    _globals['_PROMOTIONASSET']._serialized_start = 3718
    _globals['_PROMOTIONASSET']._serialized_end = 4433
    _globals['_CALLOUTASSET']._serialized_start = 4436
    _globals['_CALLOUTASSET']._serialized_end = 4593
    _globals['_STRUCTUREDSNIPPETASSET']._serialized_start = 4595
    _globals['_STRUCTUREDSNIPPETASSET']._serialized_end = 4661
    _globals['_SITELINKASSET']._serialized_start = 4664
    _globals['_SITELINKASSET']._serialized_end = 4863
    _globals['_PAGEFEEDASSET']._serialized_start = 4865
    _globals['_PAGEFEEDASSET']._serialized_end = 4919
    _globals['_DYNAMICEDUCATIONASSET']._serialized_start = 4922
    _globals['_DYNAMICEDUCATIONASSET']._serialized_end = 5282
    _globals['_MOBILEAPPASSET']._serialized_start = 5285
    _globals['_MOBILEAPPASSET']._serialized_end = 5477
    _globals['_HOTELCALLOUTASSET']._serialized_start = 5479
    _globals['_HOTELCALLOUTASSET']._serialized_end = 5545
    _globals['_CALLASSET']._serialized_start = 5548
    _globals['_CALLASSET']._serialized_end = 5908
    _globals['_PRICEASSET']._serialized_start = 5911
    _globals['_PRICEASSET']._serialized_end = 6238
    _globals['_PRICEOFFERING']._serialized_start = 6241
    _globals['_PRICEOFFERING']._serialized_end = 6512
    _globals['_CALLTOACTIONASSET']._serialized_start = 6514
    _globals['_CALLTOACTIONASSET']._serialized_end = 6628
    _globals['_DYNAMICREALESTATEASSET']._serialized_start = 6631
    _globals['_DYNAMICREALESTATEASSET']._serialized_end = 7000
    _globals['_DYNAMICCUSTOMASSET']._serialized_start = 7003
    _globals['_DYNAMICCUSTOMASSET']._serialized_end = 7405
    _globals['_DYNAMICHOTELSANDRENTALSASSET']._serialized_start = 7408
    _globals['_DYNAMICHOTELSANDRENTALSASSET']._serialized_end = 7837
    _globals['_DYNAMICFLIGHTSASSET']._serialized_start = 7840
    _globals['_DYNAMICFLIGHTSASSET']._serialized_end = 8243
    _globals['_DEMANDGENCAROUSELCARDASSET']._serialized_start = 8246
    _globals['_DEMANDGENCAROUSELCARDASSET']._serialized_end = 8435
    _globals['_DYNAMICTRAVELASSET']._serialized_start = 8438
    _globals['_DYNAMICTRAVELASSET']._serialized_end = 8865
    _globals['_DYNAMICLOCALASSET']._serialized_start = 8868
    _globals['_DYNAMICLOCALASSET']._serialized_end = 9245
    _globals['_DYNAMICJOBSASSET']._serialized_start = 9248
    _globals['_DYNAMICJOBSASSET']._serialized_end = 9577
    _globals['_LOCATIONASSET']._serialized_start = 9580
    _globals['_LOCATIONASSET']._serialized_end = 9821
    _globals['_BUSINESSPROFILELOCATION']._serialized_start = 9823
    _globals['_BUSINESSPROFILELOCATION']._serialized_end = 9904
    _globals['_HOTELPROPERTYASSET']._serialized_start = 9906
    _globals['_HOTELPROPERTYASSET']._serialized_end = 9987
    _globals['_BUSINESSMESSAGEASSET']._serialized_start = 9990
    _globals['_BUSINESSMESSAGEASSET']._serialized_end = 10384
    _globals['_WHATSAPPBUSINESSMESSAGEINFO']._serialized_start = 10386
    _globals['_WHATSAPPBUSINESSMESSAGEINFO']._serialized_end = 10469
    _globals['_BUSINESSMESSAGECALLTOACTIONINFO']._serialized_start = 10472
    _globals['_BUSINESSMESSAGECALLTOACTIONINFO']._serialized_end = 10687
    _globals['_APPDEEPLINKASSET']._serialized_start = 10689
    _globals['_APPDEEPLINKASSET']._serialized_end = 10734