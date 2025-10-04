"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/datasources/v1beta/datasourcetypes.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/shopping/merchant/datasources/v1beta/datasourcetypes.proto\x12+google.shopping.merchant.datasources.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a google/shopping/type/types.proto"\xae\x07\n\x18PrimaryProductDataSource\x12f\n\x07channel\x18\x03 \x01(\x0e2M.google.shopping.merchant.datasources.v1beta.PrimaryProductDataSource.ChannelB\x06\xe0A\x01\xe0A\x05\x12\x1f\n\nfeed_label\x18\x04 \x01(\tB\x06\xe0A\x01\xe0A\x05H\x00\x88\x01\x01\x12%\n\x10content_language\x18\x05 \x01(\tB\x06\xe0A\x01\xe0A\x05H\x01\x88\x01\x01\x12\x16\n\tcountries\x18\x06 \x03(\tB\x03\xe0A\x01\x12l\n\x0cdefault_rule\x18\x07 \x01(\x0b2Q.google.shopping.merchant.datasources.v1beta.PrimaryProductDataSource.DefaultRuleB\x03\xe0A\x01\x12l\n\x0cdestinations\x18\n \x03(\x0b2Q.google.shopping.merchant.datasources.v1beta.PrimaryProductDataSource.DestinationB\x03\xe0A\x01\x1at\n\x0bDefaultRule\x12e\n\x16take_from_data_sources\x18\x01 \x03(\x0b2@.google.shopping.merchant.datasources.v1beta.DataSourceReferenceB\x03\xe0A\x02\x1a\xf8\x01\n\x0bDestination\x12F\n\x0bdestination\x18\x01 \x01(\x0e21.google.shopping.type.Destination.DestinationEnum\x12f\n\x05state\x18\x02 \x01(\x0e2W.google.shopping.merchant.datasources.v1beta.PrimaryProductDataSource.Destination.State"9\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\x0c\n\x08DISABLED\x10\x02"Y\n\x07Channel\x12\x17\n\x13CHANNEL_UNSPECIFIED\x10\x00\x12\x13\n\x0fONLINE_PRODUCTS\x10\x01\x12\x12\n\x0eLOCAL_PRODUCTS\x10\x02\x12\x0c\n\x08PRODUCTS\x10\x03B\r\n\x0b_feed_labelB\x13\n\x11_content_language"\xfc\x01\n\x1dSupplementalProductDataSource\x12\x1f\n\nfeed_label\x18\x04 \x01(\tB\x06\xe0A\x01\xe0A\x05H\x00\x88\x01\x01\x12%\n\x10content_language\x18\x05 \x01(\tB\x06\xe0A\x01\xe0A\x05H\x01\x88\x01\x01\x12o\n referencing_primary_data_sources\x18\x07 \x03(\x0b2@.google.shopping.merchant.datasources.v1beta.DataSourceReferenceB\x03\xe0A\x03B\r\n\x0b_feed_labelB\x13\n\x11_content_language"X\n\x18LocalInventoryDataSource\x12\x1a\n\nfeed_label\x18\x04 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12 \n\x10content_language\x18\x05 \x01(\tB\x06\xe0A\x02\xe0A\x05"[\n\x1bRegionalInventoryDataSource\x12\x1a\n\nfeed_label\x18\x04 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12 \n\x10content_language\x18\x05 \x01(\tB\x06\xe0A\x02\xe0A\x05"W\n\x13PromotionDataSource\x12\x1e\n\x0etarget_country\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12 \n\x10content_language\x18\x02 \x01(\tB\x06\xe0A\x02\xe0A\x05"\x19\n\x17ProductReviewDataSource"\x1a\n\x18MerchantReviewDataSource"\x8e\x01\n\x13DataSourceReference\x12\x0e\n\x04self\x18\x01 \x01(\x08H\x00\x12\'\n\x18primary_data_source_name\x18\x03 \x01(\tB\x03\xe0A\x01H\x00\x12,\n\x1dsupplemental_data_source_name\x18\x02 \x01(\tB\x03\xe0A\x01H\x00B\x10\n\x0edata_source_idB\xb0\x02\n/com.google.shopping.merchant.datasources.v1betaB\x14DatasourcetypesProtoP\x01ZWcloud.google.com/go/shopping/merchant/datasources/apiv1beta/datasourcespb;datasourcespb\xaa\x02+Google.Shopping.Merchant.DataSources.V1Beta\xca\x02+Google\\Shopping\\Merchant\\DataSources\\V1beta\xea\x02/Google::Shopping::Merchant::DataSources::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.datasources.v1beta.datasourcetypes_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.shopping.merchant.datasources.v1betaB\x14DatasourcetypesProtoP\x01ZWcloud.google.com/go/shopping/merchant/datasources/apiv1beta/datasourcespb;datasourcespb\xaa\x02+Google.Shopping.Merchant.DataSources.V1Beta\xca\x02+Google\\Shopping\\Merchant\\DataSources\\V1beta\xea\x02/Google::Shopping::Merchant::DataSources::V1beta'
    _globals['_PRIMARYPRODUCTDATASOURCE_DEFAULTRULE'].fields_by_name['take_from_data_sources']._loaded_options = None
    _globals['_PRIMARYPRODUCTDATASOURCE_DEFAULTRULE'].fields_by_name['take_from_data_sources']._serialized_options = b'\xe0A\x02'
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['channel']._loaded_options = None
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['channel']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['feed_label']._loaded_options = None
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['feed_label']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['content_language']._loaded_options = None
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['content_language']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['countries']._loaded_options = None
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['countries']._serialized_options = b'\xe0A\x01'
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['default_rule']._loaded_options = None
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['default_rule']._serialized_options = b'\xe0A\x01'
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['destinations']._loaded_options = None
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['destinations']._serialized_options = b'\xe0A\x01'
    _globals['_SUPPLEMENTALPRODUCTDATASOURCE'].fields_by_name['feed_label']._loaded_options = None
    _globals['_SUPPLEMENTALPRODUCTDATASOURCE'].fields_by_name['feed_label']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_SUPPLEMENTALPRODUCTDATASOURCE'].fields_by_name['content_language']._loaded_options = None
    _globals['_SUPPLEMENTALPRODUCTDATASOURCE'].fields_by_name['content_language']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_SUPPLEMENTALPRODUCTDATASOURCE'].fields_by_name['referencing_primary_data_sources']._loaded_options = None
    _globals['_SUPPLEMENTALPRODUCTDATASOURCE'].fields_by_name['referencing_primary_data_sources']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALINVENTORYDATASOURCE'].fields_by_name['feed_label']._loaded_options = None
    _globals['_LOCALINVENTORYDATASOURCE'].fields_by_name['feed_label']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_LOCALINVENTORYDATASOURCE'].fields_by_name['content_language']._loaded_options = None
    _globals['_LOCALINVENTORYDATASOURCE'].fields_by_name['content_language']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_REGIONALINVENTORYDATASOURCE'].fields_by_name['feed_label']._loaded_options = None
    _globals['_REGIONALINVENTORYDATASOURCE'].fields_by_name['feed_label']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_REGIONALINVENTORYDATASOURCE'].fields_by_name['content_language']._loaded_options = None
    _globals['_REGIONALINVENTORYDATASOURCE'].fields_by_name['content_language']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_PROMOTIONDATASOURCE'].fields_by_name['target_country']._loaded_options = None
    _globals['_PROMOTIONDATASOURCE'].fields_by_name['target_country']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_PROMOTIONDATASOURCE'].fields_by_name['content_language']._loaded_options = None
    _globals['_PROMOTIONDATASOURCE'].fields_by_name['content_language']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_DATASOURCEREFERENCE'].fields_by_name['primary_data_source_name']._loaded_options = None
    _globals['_DATASOURCEREFERENCE'].fields_by_name['primary_data_source_name']._serialized_options = b'\xe0A\x01'
    _globals['_DATASOURCEREFERENCE'].fields_by_name['supplemental_data_source_name']._loaded_options = None
    _globals['_DATASOURCEREFERENCE'].fields_by_name['supplemental_data_source_name']._serialized_options = b'\xe0A\x01'
    _globals['_PRIMARYPRODUCTDATASOURCE']._serialized_start = 182
    _globals['_PRIMARYPRODUCTDATASOURCE']._serialized_end = 1124
    _globals['_PRIMARYPRODUCTDATASOURCE_DEFAULTRULE']._serialized_start = 630
    _globals['_PRIMARYPRODUCTDATASOURCE_DEFAULTRULE']._serialized_end = 746
    _globals['_PRIMARYPRODUCTDATASOURCE_DESTINATION']._serialized_start = 749
    _globals['_PRIMARYPRODUCTDATASOURCE_DESTINATION']._serialized_end = 997
    _globals['_PRIMARYPRODUCTDATASOURCE_DESTINATION_STATE']._serialized_start = 940
    _globals['_PRIMARYPRODUCTDATASOURCE_DESTINATION_STATE']._serialized_end = 997
    _globals['_PRIMARYPRODUCTDATASOURCE_CHANNEL']._serialized_start = 999
    _globals['_PRIMARYPRODUCTDATASOURCE_CHANNEL']._serialized_end = 1088
    _globals['_SUPPLEMENTALPRODUCTDATASOURCE']._serialized_start = 1127
    _globals['_SUPPLEMENTALPRODUCTDATASOURCE']._serialized_end = 1379
    _globals['_LOCALINVENTORYDATASOURCE']._serialized_start = 1381
    _globals['_LOCALINVENTORYDATASOURCE']._serialized_end = 1469
    _globals['_REGIONALINVENTORYDATASOURCE']._serialized_start = 1471
    _globals['_REGIONALINVENTORYDATASOURCE']._serialized_end = 1562
    _globals['_PROMOTIONDATASOURCE']._serialized_start = 1564
    _globals['_PROMOTIONDATASOURCE']._serialized_end = 1651
    _globals['_PRODUCTREVIEWDATASOURCE']._serialized_start = 1653
    _globals['_PRODUCTREVIEWDATASOURCE']._serialized_end = 1678
    _globals['_MERCHANTREVIEWDATASOURCE']._serialized_start = 1680
    _globals['_MERCHANTREVIEWDATASOURCE']._serialized_end = 1706
    _globals['_DATASOURCEREFERENCE']._serialized_start = 1709
    _globals['_DATASOURCEREFERENCE']._serialized_end = 1851