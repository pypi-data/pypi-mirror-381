"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2/search_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2 import common_pb2 as google_dot_cloud_dot_retail_dot_v2_dot_common__pb2
from .....google.cloud.retail.v2 import product_pb2 as google_dot_cloud_dot_retail_dot_v2_dot_product__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/retail/v2/search_service.proto\x12\x16google.cloud.retail.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/cloud/retail/v2/common.proto\x1a$google/cloud/retail/v2/product.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto"4\n\x15ProductAttributeValue\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t"\\\n\x18ProductAttributeInterval\x12\x0c\n\x04name\x18\x01 \x01(\t\x122\n\x08interval\x18\x02 \x01(\x0b2 .google.cloud.retail.v2.Interval"\xe8\x01\n\x04Tile\x12P\n\x17product_attribute_value\x18\x01 \x01(\x0b2-.google.cloud.retail.v2.ProductAttributeValueH\x00\x12V\n\x1aproduct_attribute_interval\x18\x02 \x01(\x0b20.google.cloud.retail.v2.ProductAttributeIntervalH\x00\x12!\n\x19representative_product_id\x18\x03 \x01(\tB\x13\n\x11product_attribute"\x8d\x1c\n\rSearchRequest\x12\x16\n\tplacement\x18\x01 \x01(\tB\x03\xe0A\x02\x121\n\x06branch\x18\x02 \x01(\tB!\xfaA\x1e\n\x1cretail.googleapis.com/Branch\x12\r\n\x05query\x18\x03 \x01(\t\x12\x17\n\nvisitor_id\x18\x04 \x01(\tB\x03\xe0A\x02\x123\n\tuser_info\x18\x05 \x01(\x0b2 .google.cloud.retail.v2.UserInfo\x12\x11\n\tpage_size\x18\x07 \x01(\x05\x12\x12\n\npage_token\x18\x08 \x01(\t\x12\x0e\n\x06offset\x18\t \x01(\x05\x12\x0e\n\x06filter\x18\n \x01(\t\x12\x18\n\x10canonical_filter\x18\x1c \x01(\t\x12\x10\n\x08order_by\x18\x0b \x01(\t\x12D\n\x0bfacet_specs\x18\x0c \x03(\x0b2/.google.cloud.retail.v2.SearchRequest.FacetSpec\x12V\n\x12dynamic_facet_spec\x18\x15 \x01(\x0b26.google.cloud.retail.v2.SearchRequest.DynamicFacetSpecB\x02\x18\x01\x12C\n\nboost_spec\x18\r \x01(\x0b2/.google.cloud.retail.v2.SearchRequest.BoostSpec\x12V\n\x14query_expansion_spec\x18\x0e \x01(\x0b28.google.cloud.retail.v2.SearchRequest.QueryExpansionSpec\x12\x1b\n\x13variant_rollup_keys\x18\x11 \x03(\t\x12\x17\n\x0fpage_categories\x18\x17 \x03(\t\x12E\n\x0bsearch_mode\x18\x1f \x01(\x0e20.google.cloud.retail.v2.SearchRequest.SearchMode\x12W\n\x14personalization_spec\x18  \x01(\x0b29.google.cloud.retail.v2.SearchRequest.PersonalizationSpec\x12A\n\x06labels\x18" \x03(\x0b21.google.cloud.retail.v2.SearchRequest.LabelsEntry\x12]\n\x15spell_correction_spec\x18# \x01(\x0b29.google.cloud.retail.v2.SearchRequest.SpellCorrectionSpecH\x00\x88\x01\x01\x12\x0e\n\x06entity\x18& \x01(\t\x12g\n\x1aconversational_search_spec\x18( \x01(\x0b2>.google.cloud.retail.v2.SearchRequest.ConversationalSearchSpecB\x03\xe0A\x01\x12[\n\x14tile_navigation_spec\x18) \x01(\x0b28.google.cloud.retail.v2.SearchRequest.TileNavigationSpecB\x03\xe0A\x01\x12\x1a\n\rlanguage_code\x18+ \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bregion_code\x18, \x01(\tB\x03\xe0A\x01\x12\x15\n\x08place_id\x18. \x01(\tB\x03\xe0A\x01\x12W\n\x0fuser_attributes\x18/ \x03(\x0b29.google.cloud.retail.v2.SearchRequest.UserAttributesEntryB\x03\xe0A\x01\x1a\x91\x03\n\tFacetSpec\x12P\n\tfacet_key\x18\x01 \x01(\x0b28.google.cloud.retail.v2.SearchRequest.FacetSpec.FacetKeyB\x03\xe0A\x02\x12\r\n\x05limit\x18\x02 \x01(\x05\x12\x1c\n\x14excluded_filter_keys\x18\x03 \x03(\t\x12\x1f\n\x17enable_dynamic_position\x18\x04 \x01(\x08\x1a\xe3\x01\n\x08FacetKey\x12\x10\n\x03key\x18\x01 \x01(\tB\x03\xe0A\x02\x123\n\tintervals\x18\x02 \x03(\x0b2 .google.cloud.retail.v2.Interval\x12\x19\n\x11restricted_values\x18\x03 \x03(\t\x12\x10\n\x08prefixes\x18\x08 \x03(\t\x12\x10\n\x08contains\x18\t \x03(\t\x12\x18\n\x10case_insensitive\x18\n \x01(\x08\x12\x10\n\x08order_by\x18\x04 \x01(\t\x12\r\n\x05query\x18\x05 \x01(\t\x12\x16\n\x0ereturn_min_max\x18\x0b \x01(\x08\x1a\x96\x01\n\x10DynamicFacetSpec\x12I\n\x04mode\x18\x01 \x01(\x0e2;.google.cloud.retail.v2.SearchRequest.DynamicFacetSpec.Mode"7\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x0c\n\x08DISABLED\x10\x01\x12\x0b\n\x07ENABLED\x10\x02\x1a\xee\x01\n\tBoostSpec\x12a\n\x15condition_boost_specs\x18\x01 \x03(\x0b2B.google.cloud.retail.v2.SearchRequest.BoostSpec.ConditionBoostSpec\x12\'\n\x1askip_boost_spec_validation\x18\x02 \x01(\x08H\x00\x88\x01\x01\x1a6\n\x12ConditionBoostSpec\x12\x11\n\tcondition\x18\x01 \x01(\t\x12\r\n\x05boost\x18\x02 \x01(\x02B\x1d\n\x1b_skip_boost_spec_validation\x1a\xcb\x01\n\x12QueryExpansionSpec\x12U\n\tcondition\x18\x01 \x01(\x0e2B.google.cloud.retail.v2.SearchRequest.QueryExpansionSpec.Condition\x12\x1e\n\x16pin_unexpanded_results\x18\x02 \x01(\x08">\n\tCondition\x12\x19\n\x15CONDITION_UNSPECIFIED\x10\x00\x12\x0c\n\x08DISABLED\x10\x01\x12\x08\n\x04AUTO\x10\x03\x1a\x99\x01\n\x13PersonalizationSpec\x12L\n\x04mode\x18\x01 \x01(\x0e2>.google.cloud.retail.v2.SearchRequest.PersonalizationSpec.Mode"4\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x08\n\x04AUTO\x10\x01\x12\x0c\n\x08DISABLED\x10\x02\x1a\xa0\x01\n\x13SpellCorrectionSpec\x12L\n\x04mode\x18\x01 \x01(\x0e2>.google.cloud.retail.v2.SearchRequest.SpellCorrectionSpec.Mode";\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x13\n\x0fSUGGESTION_ONLY\x10\x01\x12\x08\n\x04AUTO\x10\x02\x1a\x97\x04\n\x18ConversationalSearchSpec\x12\'\n\x1ffollowup_conversation_requested\x18\x01 \x01(\x08\x12\x17\n\x0fconversation_id\x18\x02 \x01(\t\x12^\n\x0buser_answer\x18\x03 \x01(\x0b2I.google.cloud.retail.v2.SearchRequest.ConversationalSearchSpec.UserAnswer\x1a\xd8\x02\n\nUserAnswer\x12\x15\n\x0btext_answer\x18\x01 \x01(\tH\x00\x12s\n\x0fselected_answer\x18\x02 \x01(\x0b2X.google.cloud.retail.v2.SearchRequest.ConversationalSearchSpec.UserAnswer.SelectedAnswerH\x00\x1a\xb5\x01\n\x0eSelectedAnswer\x12S\n\x18product_attribute_values\x18\x01 \x03(\x0b2-.google.cloud.retail.v2.ProductAttributeValueB\x02\x18\x01\x12N\n\x17product_attribute_value\x18\x02 \x01(\x0b2-.google.cloud.retail.v2.ProductAttributeValueB\x06\n\x04type\x1al\n\x12TileNavigationSpec\x12!\n\x19tile_navigation_requested\x18\x01 \x01(\x08\x123\n\rapplied_tiles\x18\x02 \x03(\x0b2\x1c.google.cloud.retail.v2.Tile\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1aY\n\x13UserAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x121\n\x05value\x18\x02 \x01(\x0b2".google.cloud.retail.v2.StringList:\x028\x01"[\n\nSearchMode\x12\x1b\n\x17SEARCH_MODE_UNSPECIFIED\x10\x00\x12\x17\n\x13PRODUCT_SEARCH_ONLY\x10\x01\x12\x17\n\x13FACETED_SEARCH_ONLY\x10\x02B\x18\n\x16_spell_correction_spec"\xa5\x14\n\x0eSearchResponse\x12D\n\x07results\x18\x01 \x03(\x0b23.google.cloud.retail.v2.SearchResponse.SearchResult\x12<\n\x06facets\x18\x02 \x03(\x0b2,.google.cloud.retail.v2.SearchResponse.Facet\x12\x12\n\ntotal_size\x18\x03 \x01(\x05\x12\x17\n\x0fcorrected_query\x18\x04 \x01(\t\x12\x19\n\x11attribution_token\x18\x05 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x06 \x01(\t\x12W\n\x14query_expansion_info\x18\x07 \x01(\x0b29.google.cloud.retail.v2.SearchResponse.QueryExpansionInfo\x12\x14\n\x0credirect_uri\x18\n \x01(\t\x12\x18\n\x10applied_controls\x18\x0c \x03(\t\x12H\n\x14pin_control_metadata\x18\x16 \x01(\x0b2*.google.cloud.retail.v2.PinControlMetadata\x12i\n\x1dinvalid_condition_boost_specs\x18\x0e \x03(\x0b2B.google.cloud.retail.v2.SearchRequest.BoostSpec.ConditionBoostSpec\x12?\n\x0fexperiment_info\x18\x11 \x03(\x0b2&.google.cloud.retail.v2.ExperimentInfo\x12g\n\x1cconversational_search_result\x18\x12 \x01(\x0b2A.google.cloud.retail.v2.SearchResponse.ConversationalSearchResult\x12[\n\x16tile_navigation_result\x18\x13 \x01(\x0b2;.google.cloud.retail.v2.SearchResponse.TileNavigationResult\x1a\xc5\x05\n\x0cSearchResult\x12\n\n\x02id\x18\x01 \x01(\t\x120\n\x07product\x18\x02 \x01(\x0b2\x1f.google.cloud.retail.v2.Product\x12\x1e\n\x16matching_variant_count\x18\x03 \x01(\x05\x12o\n\x17matching_variant_fields\x18\x04 \x03(\x0b2N.google.cloud.retail.v2.SearchResponse.SearchResult.MatchingVariantFieldsEntry\x12k\n\x15variant_rollup_values\x18\x05 \x03(\x0b2L.google.cloud.retail.v2.SearchResponse.SearchResult.VariantRollupValuesEntry\x12\x17\n\x0fpersonal_labels\x18\x07 \x03(\t\x12Z\n\x0cmodel_scores\x18\x08 \x03(\x0b2D.google.cloud.retail.v2.SearchResponse.SearchResult.ModelScoresEntry\x1aX\n\x1aMatchingVariantFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask:\x028\x01\x1aR\n\x18VariantRollupValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x01\x1aV\n\x10ModelScoresEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x121\n\x05value\x18\x02 \x01(\x0b2".google.cloud.retail.v2.DoubleList:\x028\x01\x1a\x8e\x02\n\x05Facet\x12\x0b\n\x03key\x18\x01 \x01(\t\x12G\n\x06values\x18\x02 \x03(\x0b27.google.cloud.retail.v2.SearchResponse.Facet.FacetValue\x12\x15\n\rdynamic_facet\x18\x03 \x01(\x08\x1a\x97\x01\n\nFacetValue\x12\x0f\n\x05value\x18\x01 \x01(\tH\x00\x124\n\x08interval\x18\x02 \x01(\x0b2 .google.cloud.retail.v2.IntervalH\x00\x12\r\n\x05count\x18\x03 \x01(\x03\x12\x11\n\tmin_value\x18\x05 \x01(\x01\x12\x11\n\tmax_value\x18\x06 \x01(\x01B\r\n\x0bfacet_value\x1aI\n\x12QueryExpansionInfo\x12\x16\n\x0eexpanded_query\x18\x01 \x01(\x08\x12\x1b\n\x13pinned_result_count\x18\x02 \x01(\x03\x1a\xff\x04\n\x1aConversationalSearchResult\x12\x17\n\x0fconversation_id\x18\x01 \x01(\t\x12\x15\n\rrefined_query\x18\x02 \x01(\t\x12r\n\x12additional_filters\x18\x03 \x03(\x0b2R.google.cloud.retail.v2.SearchResponse.ConversationalSearchResult.AdditionalFilterB\x02\x18\x01\x12\x19\n\x11followup_question\x18\x04 \x01(\t\x12l\n\x11suggested_answers\x18\x05 \x03(\x0b2Q.google.cloud.retail.v2.SearchResponse.ConversationalSearchResult.SuggestedAnswer\x12m\n\x11additional_filter\x18\x06 \x01(\x0b2R.google.cloud.retail.v2.SearchResponse.ConversationalSearchResult.AdditionalFilter\x1aa\n\x0fSuggestedAnswer\x12N\n\x17product_attribute_value\x18\x01 \x01(\x0b2-.google.cloud.retail.v2.ProductAttributeValue\x1ab\n\x10AdditionalFilter\x12N\n\x17product_attribute_value\x18\x01 \x01(\x0b2-.google.cloud.retail.v2.ProductAttributeValue\x1aC\n\x14TileNavigationResult\x12+\n\x05tiles\x18\x01 \x03(\x0b2\x1c.google.cloud.retail.v2.Tile"\xfb\x02\n\x0eExperimentInfo\x12c\n\x19serving_config_experiment\x18\x02 \x01(\x0b2>.google.cloud.retail.v2.ExperimentInfo.ServingConfigExperimentH\x00\x129\n\nexperiment\x18\x01 \x01(\tB%\xfaA"\n retail.googleapis.com/Experiment\x1a\xb1\x01\n\x17ServingConfigExperiment\x12I\n\x17original_serving_config\x18\x01 \x01(\tB(\xfaA%\n#retail.googleapis.com/ServingConfig\x12K\n\x19experiment_serving_config\x18\x02 \x01(\tB(\xfaA%\n#retail.googleapis.com/ServingConfigB\x15\n\x13experiment_metadata2\xd8\x02\n\rSearchService\x12\xfb\x01\n\x06Search\x12%.google.cloud.retail.v2.SearchRequest\x1a&.google.cloud.retail.v2.SearchResponse"\xa1\x01\x82\xd3\xe4\x93\x02\x9a\x01"E/v2/{placement=projects/*/locations/*/catalogs/*/placements/*}:search:\x01*ZN"I/v2/{placement=projects/*/locations/*/catalogs/*/servingConfigs/*}:search:\x01*\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xb7\x02\n\x1acom.google.cloud.retail.v2B\x12SearchServiceProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2\xeaAw\n retail.googleapis.com/Experiment\x12Sprojects/{project}/locations/{location}/catalogs/{catalog}/experiments/{experiment}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2.search_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.retail.v2B\x12SearchServiceProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2\xeaAw\n retail.googleapis.com/Experiment\x12Sprojects/{project}/locations/{location}/catalogs/{catalog}/experiments/{experiment}'
    _globals['_SEARCHREQUEST_FACETSPEC_FACETKEY'].fields_by_name['key']._loaded_options = None
    _globals['_SEARCHREQUEST_FACETSPEC_FACETKEY'].fields_by_name['key']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHREQUEST_FACETSPEC'].fields_by_name['facet_key']._loaded_options = None
    _globals['_SEARCHREQUEST_FACETSPEC'].fields_by_name['facet_key']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHREQUEST_CONVERSATIONALSEARCHSPEC_USERANSWER_SELECTEDANSWER'].fields_by_name['product_attribute_values']._loaded_options = None
    _globals['_SEARCHREQUEST_CONVERSATIONALSEARCHSPEC_USERANSWER_SELECTEDANSWER'].fields_by_name['product_attribute_values']._serialized_options = b'\x18\x01'
    _globals['_SEARCHREQUEST_LABELSENTRY']._loaded_options = None
    _globals['_SEARCHREQUEST_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_SEARCHREQUEST_USERATTRIBUTESENTRY']._loaded_options = None
    _globals['_SEARCHREQUEST_USERATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_SEARCHREQUEST'].fields_by_name['placement']._loaded_options = None
    _globals['_SEARCHREQUEST'].fields_by_name['placement']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHREQUEST'].fields_by_name['branch']._loaded_options = None
    _globals['_SEARCHREQUEST'].fields_by_name['branch']._serialized_options = b'\xfaA\x1e\n\x1cretail.googleapis.com/Branch'
    _globals['_SEARCHREQUEST'].fields_by_name['visitor_id']._loaded_options = None
    _globals['_SEARCHREQUEST'].fields_by_name['visitor_id']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHREQUEST'].fields_by_name['dynamic_facet_spec']._loaded_options = None
    _globals['_SEARCHREQUEST'].fields_by_name['dynamic_facet_spec']._serialized_options = b'\x18\x01'
    _globals['_SEARCHREQUEST'].fields_by_name['conversational_search_spec']._loaded_options = None
    _globals['_SEARCHREQUEST'].fields_by_name['conversational_search_spec']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHREQUEST'].fields_by_name['tile_navigation_spec']._loaded_options = None
    _globals['_SEARCHREQUEST'].fields_by_name['tile_navigation_spec']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_SEARCHREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHREQUEST'].fields_by_name['region_code']._loaded_options = None
    _globals['_SEARCHREQUEST'].fields_by_name['region_code']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHREQUEST'].fields_by_name['place_id']._loaded_options = None
    _globals['_SEARCHREQUEST'].fields_by_name['place_id']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHREQUEST'].fields_by_name['user_attributes']._loaded_options = None
    _globals['_SEARCHREQUEST'].fields_by_name['user_attributes']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHRESPONSE_SEARCHRESULT_MATCHINGVARIANTFIELDSENTRY']._loaded_options = None
    _globals['_SEARCHRESPONSE_SEARCHRESULT_MATCHINGVARIANTFIELDSENTRY']._serialized_options = b'8\x01'
    _globals['_SEARCHRESPONSE_SEARCHRESULT_VARIANTROLLUPVALUESENTRY']._loaded_options = None
    _globals['_SEARCHRESPONSE_SEARCHRESULT_VARIANTROLLUPVALUESENTRY']._serialized_options = b'8\x01'
    _globals['_SEARCHRESPONSE_SEARCHRESULT_MODELSCORESENTRY']._loaded_options = None
    _globals['_SEARCHRESPONSE_SEARCHRESULT_MODELSCORESENTRY']._serialized_options = b'8\x01'
    _globals['_SEARCHRESPONSE_CONVERSATIONALSEARCHRESULT'].fields_by_name['additional_filters']._loaded_options = None
    _globals['_SEARCHRESPONSE_CONVERSATIONALSEARCHRESULT'].fields_by_name['additional_filters']._serialized_options = b'\x18\x01'
    _globals['_EXPERIMENTINFO_SERVINGCONFIGEXPERIMENT'].fields_by_name['original_serving_config']._loaded_options = None
    _globals['_EXPERIMENTINFO_SERVINGCONFIGEXPERIMENT'].fields_by_name['original_serving_config']._serialized_options = b'\xfaA%\n#retail.googleapis.com/ServingConfig'
    _globals['_EXPERIMENTINFO_SERVINGCONFIGEXPERIMENT'].fields_by_name['experiment_serving_config']._loaded_options = None
    _globals['_EXPERIMENTINFO_SERVINGCONFIGEXPERIMENT'].fields_by_name['experiment_serving_config']._serialized_options = b'\xfaA%\n#retail.googleapis.com/ServingConfig'
    _globals['_EXPERIMENTINFO'].fields_by_name['experiment']._loaded_options = None
    _globals['_EXPERIMENTINFO'].fields_by_name['experiment']._serialized_options = b'\xfaA"\n retail.googleapis.com/Experiment'
    _globals['_SEARCHSERVICE']._loaded_options = None
    _globals['_SEARCHSERVICE']._serialized_options = b'\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SEARCHSERVICE'].methods_by_name['Search']._loaded_options = None
    _globals['_SEARCHSERVICE'].methods_by_name['Search']._serialized_options = b'\x82\xd3\xe4\x93\x02\x9a\x01"E/v2/{placement=projects/*/locations/*/catalogs/*/placements/*}:search:\x01*ZN"I/v2/{placement=projects/*/locations/*/catalogs/*/servingConfigs/*}:search:\x01*'
    _globals['_PRODUCTATTRIBUTEVALUE']._serialized_start = 325
    _globals['_PRODUCTATTRIBUTEVALUE']._serialized_end = 377
    _globals['_PRODUCTATTRIBUTEINTERVAL']._serialized_start = 379
    _globals['_PRODUCTATTRIBUTEINTERVAL']._serialized_end = 471
    _globals['_TILE']._serialized_start = 474
    _globals['_TILE']._serialized_end = 706
    _globals['_SEARCHREQUEST']._serialized_start = 709
    _globals['_SEARCHREQUEST']._serialized_end = 4306
    _globals['_SEARCHREQUEST_FACETSPEC']._serialized_start = 2081
    _globals['_SEARCHREQUEST_FACETSPEC']._serialized_end = 2482
    _globals['_SEARCHREQUEST_FACETSPEC_FACETKEY']._serialized_start = 2255
    _globals['_SEARCHREQUEST_FACETSPEC_FACETKEY']._serialized_end = 2482
    _globals['_SEARCHREQUEST_DYNAMICFACETSPEC']._serialized_start = 2485
    _globals['_SEARCHREQUEST_DYNAMICFACETSPEC']._serialized_end = 2635
    _globals['_SEARCHREQUEST_DYNAMICFACETSPEC_MODE']._serialized_start = 2580
    _globals['_SEARCHREQUEST_DYNAMICFACETSPEC_MODE']._serialized_end = 2635
    _globals['_SEARCHREQUEST_BOOSTSPEC']._serialized_start = 2638
    _globals['_SEARCHREQUEST_BOOSTSPEC']._serialized_end = 2876
    _globals['_SEARCHREQUEST_BOOSTSPEC_CONDITIONBOOSTSPEC']._serialized_start = 2791
    _globals['_SEARCHREQUEST_BOOSTSPEC_CONDITIONBOOSTSPEC']._serialized_end = 2845
    _globals['_SEARCHREQUEST_QUERYEXPANSIONSPEC']._serialized_start = 2879
    _globals['_SEARCHREQUEST_QUERYEXPANSIONSPEC']._serialized_end = 3082
    _globals['_SEARCHREQUEST_QUERYEXPANSIONSPEC_CONDITION']._serialized_start = 3020
    _globals['_SEARCHREQUEST_QUERYEXPANSIONSPEC_CONDITION']._serialized_end = 3082
    _globals['_SEARCHREQUEST_PERSONALIZATIONSPEC']._serialized_start = 3085
    _globals['_SEARCHREQUEST_PERSONALIZATIONSPEC']._serialized_end = 3238
    _globals['_SEARCHREQUEST_PERSONALIZATIONSPEC_MODE']._serialized_start = 3186
    _globals['_SEARCHREQUEST_PERSONALIZATIONSPEC_MODE']._serialized_end = 3238
    _globals['_SEARCHREQUEST_SPELLCORRECTIONSPEC']._serialized_start = 3241
    _globals['_SEARCHREQUEST_SPELLCORRECTIONSPEC']._serialized_end = 3401
    _globals['_SEARCHREQUEST_SPELLCORRECTIONSPEC_MODE']._serialized_start = 3342
    _globals['_SEARCHREQUEST_SPELLCORRECTIONSPEC_MODE']._serialized_end = 3401
    _globals['_SEARCHREQUEST_CONVERSATIONALSEARCHSPEC']._serialized_start = 3404
    _globals['_SEARCHREQUEST_CONVERSATIONALSEARCHSPEC']._serialized_end = 3939
    _globals['_SEARCHREQUEST_CONVERSATIONALSEARCHSPEC_USERANSWER']._serialized_start = 3595
    _globals['_SEARCHREQUEST_CONVERSATIONALSEARCHSPEC_USERANSWER']._serialized_end = 3939
    _globals['_SEARCHREQUEST_CONVERSATIONALSEARCHSPEC_USERANSWER_SELECTEDANSWER']._serialized_start = 3750
    _globals['_SEARCHREQUEST_CONVERSATIONALSEARCHSPEC_USERANSWER_SELECTEDANSWER']._serialized_end = 3931
    _globals['_SEARCHREQUEST_TILENAVIGATIONSPEC']._serialized_start = 3941
    _globals['_SEARCHREQUEST_TILENAVIGATIONSPEC']._serialized_end = 4049
    _globals['_SEARCHREQUEST_LABELSENTRY']._serialized_start = 4051
    _globals['_SEARCHREQUEST_LABELSENTRY']._serialized_end = 4096
    _globals['_SEARCHREQUEST_USERATTRIBUTESENTRY']._serialized_start = 4098
    _globals['_SEARCHREQUEST_USERATTRIBUTESENTRY']._serialized_end = 4187
    _globals['_SEARCHREQUEST_SEARCHMODE']._serialized_start = 4189
    _globals['_SEARCHREQUEST_SEARCHMODE']._serialized_end = 4280
    _globals['_SEARCHRESPONSE']._serialized_start = 4309
    _globals['_SEARCHRESPONSE']._serialized_end = 6906
    _globals['_SEARCHRESPONSE_SEARCHRESULT']._serialized_start = 5138
    _globals['_SEARCHRESPONSE_SEARCHRESULT']._serialized_end = 5847
    _globals['_SEARCHRESPONSE_SEARCHRESULT_MATCHINGVARIANTFIELDSENTRY']._serialized_start = 5587
    _globals['_SEARCHRESPONSE_SEARCHRESULT_MATCHINGVARIANTFIELDSENTRY']._serialized_end = 5675
    _globals['_SEARCHRESPONSE_SEARCHRESULT_VARIANTROLLUPVALUESENTRY']._serialized_start = 5677
    _globals['_SEARCHRESPONSE_SEARCHRESULT_VARIANTROLLUPVALUESENTRY']._serialized_end = 5759
    _globals['_SEARCHRESPONSE_SEARCHRESULT_MODELSCORESENTRY']._serialized_start = 5761
    _globals['_SEARCHRESPONSE_SEARCHRESULT_MODELSCORESENTRY']._serialized_end = 5847
    _globals['_SEARCHRESPONSE_FACET']._serialized_start = 5850
    _globals['_SEARCHRESPONSE_FACET']._serialized_end = 6120
    _globals['_SEARCHRESPONSE_FACET_FACETVALUE']._serialized_start = 5969
    _globals['_SEARCHRESPONSE_FACET_FACETVALUE']._serialized_end = 6120
    _globals['_SEARCHRESPONSE_QUERYEXPANSIONINFO']._serialized_start = 6122
    _globals['_SEARCHRESPONSE_QUERYEXPANSIONINFO']._serialized_end = 6195
    _globals['_SEARCHRESPONSE_CONVERSATIONALSEARCHRESULT']._serialized_start = 6198
    _globals['_SEARCHRESPONSE_CONVERSATIONALSEARCHRESULT']._serialized_end = 6837
    _globals['_SEARCHRESPONSE_CONVERSATIONALSEARCHRESULT_SUGGESTEDANSWER']._serialized_start = 6640
    _globals['_SEARCHRESPONSE_CONVERSATIONALSEARCHRESULT_SUGGESTEDANSWER']._serialized_end = 6737
    _globals['_SEARCHRESPONSE_CONVERSATIONALSEARCHRESULT_ADDITIONALFILTER']._serialized_start = 6739
    _globals['_SEARCHRESPONSE_CONVERSATIONALSEARCHRESULT_ADDITIONALFILTER']._serialized_end = 6837
    _globals['_SEARCHRESPONSE_TILENAVIGATIONRESULT']._serialized_start = 6839
    _globals['_SEARCHRESPONSE_TILENAVIGATIONRESULT']._serialized_end = 6906
    _globals['_EXPERIMENTINFO']._serialized_start = 6909
    _globals['_EXPERIMENTINFO']._serialized_end = 7288
    _globals['_EXPERIMENTINFO_SERVINGCONFIGEXPERIMENT']._serialized_start = 7088
    _globals['_EXPERIMENTINFO_SERVINGCONFIGEXPERIMENT']._serialized_end = 7265
    _globals['_SEARCHSERVICE']._serialized_start = 7291
    _globals['_SEARCHSERVICE']._serialized_end = 7635