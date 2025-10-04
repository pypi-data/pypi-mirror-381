"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2beta/catalog.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2beta import common_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_common__pb2
from .....google.cloud.retail.v2beta import import_config_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_import__config__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/retail/v2beta/catalog.proto\x12\x1agoogle.cloud.retail.v2beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\'google/cloud/retail/v2beta/common.proto\x1a.google/cloud/retail/v2beta/import_config.proto\x1a\x1fgoogle/protobuf/timestamp.proto"^\n\x12ProductLevelConfig\x12\x1e\n\x16ingestion_product_type\x18\x01 \x01(\t\x12(\n merchant_center_product_id_field\x18\x02 \x01(\t"\x8d\x11\n\x10CatalogAttribute\x12\x10\n\x03key\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06in_use\x18\t \x01(\x08B\x03\xe0A\x03\x12M\n\x04type\x18\n \x01(\x0e2:.google.cloud.retail.v2beta.CatalogAttribute.AttributeTypeB\x03\xe0A\x03\x12V\n\x10indexable_option\x18\x05 \x01(\x0e2<.google.cloud.retail.v2beta.CatalogAttribute.IndexableOption\x12e\n\x18dynamic_facetable_option\x18\x06 \x01(\x0e2C.google.cloud.retail.v2beta.CatalogAttribute.DynamicFacetableOption\x12X\n\x11searchable_option\x18\x07 \x01(\x0e2=.google.cloud.retail.v2beta.CatalogAttribute.SearchableOption\x12d\n recommendations_filtering_option\x18\x08 \x01(\x0e2:.google.cloud.retail.v2beta.RecommendationsFilteringOption\x12c\n\x17exact_searchable_option\x18\x0b \x01(\x0e2B.google.cloud.retail.v2beta.CatalogAttribute.ExactSearchableOption\x12Z\n\x12retrievable_option\x18\x0c \x01(\x0e2>.google.cloud.retail.v2beta.CatalogAttribute.RetrievableOption\x12N\n\x0cfacet_config\x18\r \x01(\x0b28.google.cloud.retail.v2beta.CatalogAttribute.FacetConfig\x1a\xfd\x05\n\x0bFacetConfig\x12=\n\x0ffacet_intervals\x18\x01 \x03(\x0b2$.google.cloud.retail.v2beta.Interval\x12i\n\x14ignored_facet_values\x18\x02 \x03(\x0b2K.google.cloud.retail.v2beta.CatalogAttribute.FacetConfig.IgnoredFacetValues\x12f\n\x13merged_facet_values\x18\x03 \x03(\x0b2I.google.cloud.retail.v2beta.CatalogAttribute.FacetConfig.MergedFacetValue\x12Z\n\x0cmerged_facet\x18\x04 \x01(\x0b2D.google.cloud.retail.v2beta.CatalogAttribute.FacetConfig.MergedFacet\x12\\\n\rrerank_config\x18\x05 \x01(\x0b2E.google.cloud.retail.v2beta.CatalogAttribute.FacetConfig.RerankConfig\x1a\x82\x01\n\x12IgnoredFacetValues\x12\x0e\n\x06values\x18\x01 \x03(\t\x12.\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a8\n\x10MergedFacetValue\x12\x0e\n\x06values\x18\x01 \x03(\t\x12\x14\n\x0cmerged_value\x18\x02 \x01(\t\x1a\'\n\x0bMergedFacet\x12\x18\n\x10merged_facet_key\x18\x01 \x01(\t\x1a:\n\x0cRerankConfig\x12\x14\n\x0crerank_facet\x18\x01 \x01(\x08\x12\x14\n\x0cfacet_values\x18\x02 \x03(\t"8\n\rAttributeType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07TEXTUAL\x10\x01\x12\r\n\tNUMERICAL\x10\x02"b\n\x0fIndexableOption\x12 \n\x1cINDEXABLE_OPTION_UNSPECIFIED\x10\x00\x12\x15\n\x11INDEXABLE_ENABLED\x10\x01\x12\x16\n\x12INDEXABLE_DISABLED\x10\x02"\x81\x01\n\x16DynamicFacetableOption\x12(\n$DYNAMIC_FACETABLE_OPTION_UNSPECIFIED\x10\x00\x12\x1d\n\x19DYNAMIC_FACETABLE_ENABLED\x10\x01\x12\x1e\n\x1aDYNAMIC_FACETABLE_DISABLED\x10\x02"f\n\x10SearchableOption\x12!\n\x1dSEARCHABLE_OPTION_UNSPECIFIED\x10\x00\x12\x16\n\x12SEARCHABLE_ENABLED\x10\x01\x12\x17\n\x13SEARCHABLE_DISABLED\x10\x02"}\n\x15ExactSearchableOption\x12\'\n#EXACT_SEARCHABLE_OPTION_UNSPECIFIED\x10\x00\x12\x1c\n\x18EXACT_SEARCHABLE_ENABLED\x10\x01\x12\x1d\n\x19EXACT_SEARCHABLE_DISABLED\x10\x02"j\n\x11RetrievableOption\x12"\n\x1eRETRIEVABLE_OPTION_UNSPECIFIED\x10\x00\x12\x17\n\x13RETRIEVABLE_ENABLED\x10\x01\x12\x18\n\x14RETRIEVABLE_DISABLED\x10\x02"\xc2\x03\n\x10AttributesConfig\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12_\n\x12catalog_attributes\x18\x02 \x03(\x0b2C.google.cloud.retail.v2beta.AttributesConfig.CatalogAttributesEntry\x12U\n\x16attribute_config_level\x18\x03 \x01(\x0e20.google.cloud.retail.v2beta.AttributeConfigLevelB\x03\xe0A\x03\x1af\n\x16CatalogAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12;\n\x05value\x18\x02 \x01(\x0b2,.google.cloud.retail.v2beta.CatalogAttribute:\x028\x01:x\xeaAu\n&retail.googleapis.com/AttributesConfig\x12Kprojects/{project}/locations/{location}/catalogs/{catalog}/attributesConfig"\xa5\x05\n\x10CompletionConfig\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12\x16\n\x0ematching_order\x18\x02 \x01(\t\x12\x17\n\x0fmax_suggestions\x18\x03 \x01(\x05\x12\x19\n\x11min_prefix_length\x18\x04 \x01(\x05\x12\x15\n\rauto_learning\x18\x0b \x01(\x08\x12\\\n\x18suggestions_input_config\x18\x05 \x01(\x0b25.google.cloud.retail.v2beta.CompletionDataInputConfigB\x03\xe0A\x03\x12.\n!last_suggestions_import_operation\x18\x06 \x01(\tB\x03\xe0A\x03\x12Y\n\x15denylist_input_config\x18\x07 \x01(\x0b25.google.cloud.retail.v2beta.CompletionDataInputConfigB\x03\xe0A\x03\x12+\n\x1elast_denylist_import_operation\x18\x08 \x01(\tB\x03\xe0A\x03\x12Z\n\x16allowlist_input_config\x18\t \x01(\x0b25.google.cloud.retail.v2beta.CompletionDataInputConfigB\x03\xe0A\x03\x12,\n\x1flast_allowlist_import_operation\x18\n \x01(\tB\x03\xe0A\x03:x\xeaAu\n&retail.googleapis.com/CompletionConfig\x12Kprojects/{project}/locations/{location}/catalogs/{catalog}/completionConfig"\xd7\x01\n\x12MerchantCenterLink\x12\'\n\x1amerchant_center_account_id\x18\x01 \x01(\x03B\x03\xe0A\x02\x12\x11\n\tbranch_id\x18\x02 \x01(\t\x12\x14\n\x0cdestinations\x18\x03 \x03(\t\x12\x13\n\x0bregion_code\x18\x04 \x01(\t\x12\x15\n\rlanguage_code\x18\x05 \x01(\t\x12C\n\x05feeds\x18\x06 \x03(\x0b24.google.cloud.retail.v2beta.MerchantCenterFeedFilter"N\n\x18MerchantCenterFeedFilter\x12\x17\n\x0fprimary_feed_id\x18\x01 \x01(\x03\x12\x19\n\x11primary_feed_name\x18\x02 \x01(\t"\\\n\x1bMerchantCenterLinkingConfig\x12=\n\x05links\x18\x01 \x03(\x0b2..google.cloud.retail.v2beta.MerchantCenterLink"\xd1\x02\n\x07Catalog\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12\x1c\n\x0cdisplay_name\x18\x02 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12Q\n\x14product_level_config\x18\x04 \x01(\x0b2..google.cloud.retail.v2beta.ProductLevelConfigB\x03\xe0A\x02\x12_\n\x1emerchant_center_linking_config\x18\x06 \x01(\x0b27.google.cloud.retail.v2beta.MerchantCenterLinkingConfig:^\xeaA[\n\x1dretail.googleapis.com/Catalog\x12:projects/{project}/locations/{location}/catalogs/{catalog}B\xcb\x01\n\x1ecom.google.cloud.retail.v2betaB\x0cCatalogProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2beta.catalog_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.retail.v2betaB\x0cCatalogProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2beta'
    _globals['_CATALOGATTRIBUTE'].fields_by_name['key']._loaded_options = None
    _globals['_CATALOGATTRIBUTE'].fields_by_name['key']._serialized_options = b'\xe0A\x02'
    _globals['_CATALOGATTRIBUTE'].fields_by_name['in_use']._loaded_options = None
    _globals['_CATALOGATTRIBUTE'].fields_by_name['in_use']._serialized_options = b'\xe0A\x03'
    _globals['_CATALOGATTRIBUTE'].fields_by_name['type']._loaded_options = None
    _globals['_CATALOGATTRIBUTE'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_ATTRIBUTESCONFIG_CATALOGATTRIBUTESENTRY']._loaded_options = None
    _globals['_ATTRIBUTESCONFIG_CATALOGATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_ATTRIBUTESCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_ATTRIBUTESCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_ATTRIBUTESCONFIG'].fields_by_name['attribute_config_level']._loaded_options = None
    _globals['_ATTRIBUTESCONFIG'].fields_by_name['attribute_config_level']._serialized_options = b'\xe0A\x03'
    _globals['_ATTRIBUTESCONFIG']._loaded_options = None
    _globals['_ATTRIBUTESCONFIG']._serialized_options = b'\xeaAu\n&retail.googleapis.com/AttributesConfig\x12Kprojects/{project}/locations/{location}/catalogs/{catalog}/attributesConfig'
    _globals['_COMPLETIONCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_COMPLETIONCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_COMPLETIONCONFIG'].fields_by_name['suggestions_input_config']._loaded_options = None
    _globals['_COMPLETIONCONFIG'].fields_by_name['suggestions_input_config']._serialized_options = b'\xe0A\x03'
    _globals['_COMPLETIONCONFIG'].fields_by_name['last_suggestions_import_operation']._loaded_options = None
    _globals['_COMPLETIONCONFIG'].fields_by_name['last_suggestions_import_operation']._serialized_options = b'\xe0A\x03'
    _globals['_COMPLETIONCONFIG'].fields_by_name['denylist_input_config']._loaded_options = None
    _globals['_COMPLETIONCONFIG'].fields_by_name['denylist_input_config']._serialized_options = b'\xe0A\x03'
    _globals['_COMPLETIONCONFIG'].fields_by_name['last_denylist_import_operation']._loaded_options = None
    _globals['_COMPLETIONCONFIG'].fields_by_name['last_denylist_import_operation']._serialized_options = b'\xe0A\x03'
    _globals['_COMPLETIONCONFIG'].fields_by_name['allowlist_input_config']._loaded_options = None
    _globals['_COMPLETIONCONFIG'].fields_by_name['allowlist_input_config']._serialized_options = b'\xe0A\x03'
    _globals['_COMPLETIONCONFIG'].fields_by_name['last_allowlist_import_operation']._loaded_options = None
    _globals['_COMPLETIONCONFIG'].fields_by_name['last_allowlist_import_operation']._serialized_options = b'\xe0A\x03'
    _globals['_COMPLETIONCONFIG']._loaded_options = None
    _globals['_COMPLETIONCONFIG']._serialized_options = b'\xeaAu\n&retail.googleapis.com/CompletionConfig\x12Kprojects/{project}/locations/{location}/catalogs/{catalog}/completionConfig'
    _globals['_MERCHANTCENTERLINK'].fields_by_name['merchant_center_account_id']._loaded_options = None
    _globals['_MERCHANTCENTERLINK'].fields_by_name['merchant_center_account_id']._serialized_options = b'\xe0A\x02'
    _globals['_CATALOG'].fields_by_name['name']._loaded_options = None
    _globals['_CATALOG'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_CATALOG'].fields_by_name['display_name']._loaded_options = None
    _globals['_CATALOG'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_CATALOG'].fields_by_name['product_level_config']._loaded_options = None
    _globals['_CATALOG'].fields_by_name['product_level_config']._serialized_options = b'\xe0A\x02'
    _globals['_CATALOG']._loaded_options = None
    _globals['_CATALOG']._serialized_options = b'\xeaA[\n\x1dretail.googleapis.com/Catalog\x12:projects/{project}/locations/{location}/catalogs/{catalog}'
    _globals['_PRODUCTLEVELCONFIG']._serialized_start = 254
    _globals['_PRODUCTLEVELCONFIG']._serialized_end = 348
    _globals['_CATALOGATTRIBUTE']._serialized_start = 351
    _globals['_CATALOGATTRIBUTE']._serialized_end = 2540
    _globals['_CATALOGATTRIBUTE_FACETCONFIG']._serialized_start = 1146
    _globals['_CATALOGATTRIBUTE_FACETCONFIG']._serialized_end = 1911
    _globals['_CATALOGATTRIBUTE_FACETCONFIG_IGNOREDFACETVALUES']._serialized_start = 1622
    _globals['_CATALOGATTRIBUTE_FACETCONFIG_IGNOREDFACETVALUES']._serialized_end = 1752
    _globals['_CATALOGATTRIBUTE_FACETCONFIG_MERGEDFACETVALUE']._serialized_start = 1754
    _globals['_CATALOGATTRIBUTE_FACETCONFIG_MERGEDFACETVALUE']._serialized_end = 1810
    _globals['_CATALOGATTRIBUTE_FACETCONFIG_MERGEDFACET']._serialized_start = 1812
    _globals['_CATALOGATTRIBUTE_FACETCONFIG_MERGEDFACET']._serialized_end = 1851
    _globals['_CATALOGATTRIBUTE_FACETCONFIG_RERANKCONFIG']._serialized_start = 1853
    _globals['_CATALOGATTRIBUTE_FACETCONFIG_RERANKCONFIG']._serialized_end = 1911
    _globals['_CATALOGATTRIBUTE_ATTRIBUTETYPE']._serialized_start = 1913
    _globals['_CATALOGATTRIBUTE_ATTRIBUTETYPE']._serialized_end = 1969
    _globals['_CATALOGATTRIBUTE_INDEXABLEOPTION']._serialized_start = 1971
    _globals['_CATALOGATTRIBUTE_INDEXABLEOPTION']._serialized_end = 2069
    _globals['_CATALOGATTRIBUTE_DYNAMICFACETABLEOPTION']._serialized_start = 2072
    _globals['_CATALOGATTRIBUTE_DYNAMICFACETABLEOPTION']._serialized_end = 2201
    _globals['_CATALOGATTRIBUTE_SEARCHABLEOPTION']._serialized_start = 2203
    _globals['_CATALOGATTRIBUTE_SEARCHABLEOPTION']._serialized_end = 2305
    _globals['_CATALOGATTRIBUTE_EXACTSEARCHABLEOPTION']._serialized_start = 2307
    _globals['_CATALOGATTRIBUTE_EXACTSEARCHABLEOPTION']._serialized_end = 2432
    _globals['_CATALOGATTRIBUTE_RETRIEVABLEOPTION']._serialized_start = 2434
    _globals['_CATALOGATTRIBUTE_RETRIEVABLEOPTION']._serialized_end = 2540
    _globals['_ATTRIBUTESCONFIG']._serialized_start = 2543
    _globals['_ATTRIBUTESCONFIG']._serialized_end = 2993
    _globals['_ATTRIBUTESCONFIG_CATALOGATTRIBUTESENTRY']._serialized_start = 2769
    _globals['_ATTRIBUTESCONFIG_CATALOGATTRIBUTESENTRY']._serialized_end = 2871
    _globals['_COMPLETIONCONFIG']._serialized_start = 2996
    _globals['_COMPLETIONCONFIG']._serialized_end = 3673
    _globals['_MERCHANTCENTERLINK']._serialized_start = 3676
    _globals['_MERCHANTCENTERLINK']._serialized_end = 3891
    _globals['_MERCHANTCENTERFEEDFILTER']._serialized_start = 3893
    _globals['_MERCHANTCENTERFEEDFILTER']._serialized_end = 3971
    _globals['_MERCHANTCENTERLINKINGCONFIG']._serialized_start = 3973
    _globals['_MERCHANTCENTERLINKINGCONFIG']._serialized_end = 4065
    _globals['_CATALOG']._serialized_start = 4068
    _globals['_CATALOG']._serialized_end = 4405