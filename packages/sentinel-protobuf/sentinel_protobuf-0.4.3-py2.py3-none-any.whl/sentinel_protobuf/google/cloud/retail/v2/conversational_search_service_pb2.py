"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2/conversational_search_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2 import common_pb2 as google_dot_cloud_dot_retail_dot_v2_dot_common__pb2
from .....google.cloud.retail.v2 import safety_pb2 as google_dot_cloud_dot_retail_dot_v2_dot_safety__pb2
from .....google.cloud.retail.v2 import search_service_pb2 as google_dot_cloud_dot_retail_dot_v2_dot_search__service__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/retail/v2/conversational_search_service.proto\x12\x16google.cloud.retail.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/cloud/retail/v2/common.proto\x1a#google/cloud/retail/v2/safety.proto\x1a+google/cloud/retail/v2/search_service.proto"\xef\x0b\n\x1bConversationalSearchRequest\x12\x16\n\tplacement\x18\x01 \x01(\tB\x03\xe0A\x02\x124\n\x06branch\x18\x02 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cretail.googleapis.com/Branch\x12\x12\n\x05query\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1c\n\x0fpage_categories\x18\x04 \x03(\tB\x03\xe0A\x01\x12\x1c\n\x0fconversation_id\x18\x05 \x01(\tB\x03\xe0A\x01\x12\\\n\rsearch_params\x18\x06 \x01(\x0b2@.google.cloud.retail.v2.ConversationalSearchRequest.SearchParamsB\x03\xe0A\x01\x12\x17\n\nvisitor_id\x18\t \x01(\tB\x03\xe0A\x02\x128\n\tuser_info\x18\x07 \x01(\x0b2 .google.cloud.retail.v2.UserInfoB\x03\xe0A\x01\x12{\n\x1dconversational_filtering_spec\x18\x08 \x01(\x0b2O.google.cloud.retail.v2.ConversationalSearchRequest.ConversationalFilteringSpecB\x03\xe0A\x01\x12]\n\x0buser_labels\x18\x0c \x03(\x0b2C.google.cloud.retail.v2.ConversationalSearchRequest.UserLabelsEntryB\x03\xe0A\x01\x12C\n\x0fsafety_settings\x18\x0e \x03(\x0b2%.google.cloud.retail.v2.SafetySettingB\x03\xe0A\x01\x1a\xa2\x01\n\x0cSearchParams\x12\x13\n\x06filter\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x1d\n\x10canonical_filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x14\n\x07sort_by\x18\x03 \x01(\tB\x03\xe0A\x01\x12H\n\nboost_spec\x18\x04 \x01(\x0b2/.google.cloud.retail.v2.SearchRequest.BoostSpecB\x03\xe0A\x01\x1a\x81\x02\n\nUserAnswer\x12\x15\n\x0btext_answer\x18\x01 \x01(\tH\x00\x12m\n\x0fselected_answer\x18\x02 \x01(\x0b2M.google.cloud.retail.v2.ConversationalSearchRequest.UserAnswer.SelectedAnswerB\x03\xe0A\x01H\x00\x1ae\n\x0eSelectedAnswer\x12S\n\x17product_attribute_value\x18\x01 \x01(\x0b2-.google.cloud.retail.v2.ProductAttributeValueB\x03\xe0A\x01B\x06\n\x04type\x1a\x83\x03\n\x1bConversationalFilteringSpec\x12.\n\x1fenable_conversational_filtering\x18\x01 \x01(\x08B\x05\x18\x01\xe0A\x01\x12X\n\x0buser_answer\x18\x02 \x01(\x0b2>.google.cloud.retail.v2.ConversationalSearchRequest.UserAnswerB\x03\xe0A\x01\x12\x80\x01\n\x1dconversational_filtering_mode\x18\x04 \x01(\x0e2T.google.cloud.retail.v2.ConversationalSearchRequest.ConversationalFilteringSpec.ModeB\x03\xe0A\x01"W\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x0c\n\x08DISABLED\x10\x01\x12\x0b\n\x07ENABLED\x10\x02\x12\x1e\n\x1aCONVERSATIONAL_FILTER_ONLY\x10\x03\x1a1\n\x0fUserLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xcd\t\n\x1cConversationalSearchResponse\x12\x18\n\x10user_query_types\x18\n \x03(\t\x12$\n\x1cconversational_text_response\x18\x02 \x01(\t\x12`\n\x11followup_question\x18\x03 \x01(\x0b2E.google.cloud.retail.v2.ConversationalSearchResponse.FollowupQuestion\x12\x17\n\x0fconversation_id\x18\x04 \x01(\t\x12Z\n\x0erefined_search\x18\x06 \x03(\x0b2B.google.cloud.retail.v2.ConversationalSearchResponse.RefinedSearch\x12{\n\x1fconversational_filtering_result\x18\x07 \x01(\x0b2R.google.cloud.retail.v2.ConversationalSearchResponse.ConversationalFilteringResult\x12N\n\x05state\x18\t \x01(\x0e2:.google.cloud.retail.v2.ConversationalSearchResponse.StateB\x03\xe0A\x03\x1a\x82\x02\n\x10FollowupQuestion\x12\x19\n\x11followup_question\x18\x01 \x01(\t\x12p\n\x11suggested_answers\x18\x02 \x03(\x0b2U.google.cloud.retail.v2.ConversationalSearchResponse.FollowupQuestion.SuggestedAnswer\x1aa\n\x0fSuggestedAnswer\x12N\n\x17product_attribute_value\x18\x01 \x01(\x0b2-.google.cloud.retail.v2.ProductAttributeValue\x1a\x1e\n\rRefinedSearch\x12\r\n\x05query\x18\x01 \x01(\t\x1a\xe5\x02\n\x1dConversationalFilteringResult\x12`\n\x11followup_question\x18\x01 \x01(\x0b2E.google.cloud.retail.v2.ConversationalSearchResponse.FollowupQuestion\x12~\n\x11additional_filter\x18\x02 \x01(\x0b2c.google.cloud.retail.v2.ConversationalSearchResponse.ConversationalFilteringResult.AdditionalFilter\x1ab\n\x10AdditionalFilter\x12N\n\x17product_attribute_value\x18\x01 \x01(\x0b2-.google.cloud.retail.v2.ProductAttributeValue"<\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tSTREAMING\x10\x01\x12\r\n\tSUCCEEDED\x10\x022\xae\x03\n\x1bConversationalSearchService\x12\xc3\x02\n\x14ConversationalSearch\x123.google.cloud.retail.v2.ConversationalSearchRequest\x1a4.google.cloud.retail.v2.ConversationalSearchResponse"\xbd\x01\x82\xd3\xe4\x93\x02\xb6\x01"S/v2/{placement=projects/*/locations/*/catalogs/*/placements/*}:conversationalSearch:\x01*Z\\"W/v2/{placement=projects/*/locations/*/catalogs/*/servingConfigs/*}:conversationalSearch:\x01*0\x01\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xcb\x01\n\x1acom.google.cloud.retail.v2B ConversationalSearchServiceProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2.conversational_search_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.retail.v2B ConversationalSearchServiceProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2'
    _globals['_CONVERSATIONALSEARCHREQUEST_SEARCHPARAMS'].fields_by_name['filter']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST_SEARCHPARAMS'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONALSEARCHREQUEST_SEARCHPARAMS'].fields_by_name['canonical_filter']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST_SEARCHPARAMS'].fields_by_name['canonical_filter']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONALSEARCHREQUEST_SEARCHPARAMS'].fields_by_name['sort_by']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST_SEARCHPARAMS'].fields_by_name['sort_by']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONALSEARCHREQUEST_SEARCHPARAMS'].fields_by_name['boost_spec']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST_SEARCHPARAMS'].fields_by_name['boost_spec']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONALSEARCHREQUEST_USERANSWER_SELECTEDANSWER'].fields_by_name['product_attribute_value']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST_USERANSWER_SELECTEDANSWER'].fields_by_name['product_attribute_value']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONALSEARCHREQUEST_USERANSWER'].fields_by_name['selected_answer']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST_USERANSWER'].fields_by_name['selected_answer']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONALSEARCHREQUEST_CONVERSATIONALFILTERINGSPEC'].fields_by_name['enable_conversational_filtering']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST_CONVERSATIONALFILTERINGSPEC'].fields_by_name['enable_conversational_filtering']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_CONVERSATIONALSEARCHREQUEST_CONVERSATIONALFILTERINGSPEC'].fields_by_name['user_answer']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST_CONVERSATIONALFILTERINGSPEC'].fields_by_name['user_answer']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONALSEARCHREQUEST_CONVERSATIONALFILTERINGSPEC'].fields_by_name['conversational_filtering_mode']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST_CONVERSATIONALFILTERINGSPEC'].fields_by_name['conversational_filtering_mode']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONALSEARCHREQUEST_USERLABELSENTRY']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST_USERLABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['placement']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['placement']._serialized_options = b'\xe0A\x02'
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['branch']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['branch']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cretail.googleapis.com/Branch'
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['page_categories']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['page_categories']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['conversation_id']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['conversation_id']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['search_params']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['search_params']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['visitor_id']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['visitor_id']._serialized_options = b'\xe0A\x02'
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['user_info']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['user_info']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['conversational_filtering_spec']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['conversational_filtering_spec']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['user_labels']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['user_labels']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['safety_settings']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHREQUEST'].fields_by_name['safety_settings']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONALSEARCHRESPONSE'].fields_by_name['state']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHRESPONSE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSATIONALSEARCHSERVICE']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHSERVICE']._serialized_options = b'\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CONVERSATIONALSEARCHSERVICE'].methods_by_name['ConversationalSearch']._loaded_options = None
    _globals['_CONVERSATIONALSEARCHSERVICE'].methods_by_name['ConversationalSearch']._serialized_options = b'\x82\xd3\xe4\x93\x02\xb6\x01"S/v2/{placement=projects/*/locations/*/catalogs/*/placements/*}:conversationalSearch:\x01*Z\\"W/v2/{placement=projects/*/locations/*/catalogs/*/servingConfigs/*}:conversationalSearch:\x01*'
    _globals['_CONVERSATIONALSEARCHREQUEST']._serialized_start = 321
    _globals['_CONVERSATIONALSEARCHREQUEST']._serialized_end = 1840
    _globals['_CONVERSATIONALSEARCHREQUEST_SEARCHPARAMS']._serialized_start = 977
    _globals['_CONVERSATIONALSEARCHREQUEST_SEARCHPARAMS']._serialized_end = 1139
    _globals['_CONVERSATIONALSEARCHREQUEST_USERANSWER']._serialized_start = 1142
    _globals['_CONVERSATIONALSEARCHREQUEST_USERANSWER']._serialized_end = 1399
    _globals['_CONVERSATIONALSEARCHREQUEST_USERANSWER_SELECTEDANSWER']._serialized_start = 1290
    _globals['_CONVERSATIONALSEARCHREQUEST_USERANSWER_SELECTEDANSWER']._serialized_end = 1391
    _globals['_CONVERSATIONALSEARCHREQUEST_CONVERSATIONALFILTERINGSPEC']._serialized_start = 1402
    _globals['_CONVERSATIONALSEARCHREQUEST_CONVERSATIONALFILTERINGSPEC']._serialized_end = 1789
    _globals['_CONVERSATIONALSEARCHREQUEST_CONVERSATIONALFILTERINGSPEC_MODE']._serialized_start = 1702
    _globals['_CONVERSATIONALSEARCHREQUEST_CONVERSATIONALFILTERINGSPEC_MODE']._serialized_end = 1789
    _globals['_CONVERSATIONALSEARCHREQUEST_USERLABELSENTRY']._serialized_start = 1791
    _globals['_CONVERSATIONALSEARCHREQUEST_USERLABELSENTRY']._serialized_end = 1840
    _globals['_CONVERSATIONALSEARCHRESPONSE']._serialized_start = 1843
    _globals['_CONVERSATIONALSEARCHRESPONSE']._serialized_end = 3072
    _globals['_CONVERSATIONALSEARCHRESPONSE_FOLLOWUPQUESTION']._serialized_start = 2360
    _globals['_CONVERSATIONALSEARCHRESPONSE_FOLLOWUPQUESTION']._serialized_end = 2618
    _globals['_CONVERSATIONALSEARCHRESPONSE_FOLLOWUPQUESTION_SUGGESTEDANSWER']._serialized_start = 2521
    _globals['_CONVERSATIONALSEARCHRESPONSE_FOLLOWUPQUESTION_SUGGESTEDANSWER']._serialized_end = 2618
    _globals['_CONVERSATIONALSEARCHRESPONSE_REFINEDSEARCH']._serialized_start = 2620
    _globals['_CONVERSATIONALSEARCHRESPONSE_REFINEDSEARCH']._serialized_end = 2650
    _globals['_CONVERSATIONALSEARCHRESPONSE_CONVERSATIONALFILTERINGRESULT']._serialized_start = 2653
    _globals['_CONVERSATIONALSEARCHRESPONSE_CONVERSATIONALFILTERINGRESULT']._serialized_end = 3010
    _globals['_CONVERSATIONALSEARCHRESPONSE_CONVERSATIONALFILTERINGRESULT_ADDITIONALFILTER']._serialized_start = 2912
    _globals['_CONVERSATIONALSEARCHRESPONSE_CONVERSATIONALFILTERINGRESULT_ADDITIONALFILTER']._serialized_end = 3010
    _globals['_CONVERSATIONALSEARCHRESPONSE_STATE']._serialized_start = 3012
    _globals['_CONVERSATIONALSEARCHRESPONSE_STATE']._serialized_end = 3072
    _globals['_CONVERSATIONALSEARCHSERVICE']._serialized_start = 3075
    _globals['_CONVERSATIONALSEARCHSERVICE']._serialized_end = 3505