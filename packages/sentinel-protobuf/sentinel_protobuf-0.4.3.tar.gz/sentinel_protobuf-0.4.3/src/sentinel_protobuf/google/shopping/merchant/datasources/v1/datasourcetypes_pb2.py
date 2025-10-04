"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/datasources/v1/datasourcetypes.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/shopping/merchant/datasources/v1/datasourcetypes.proto\x12\'google.shopping.merchant.datasources.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a google/shopping/type/types.proto"\x9d\x06\n\x18PrimaryProductDataSource\x12\x1c\n\x0clegacy_local\x18\x0b \x01(\x08B\x06\xe0A\x01\xe0A\x05\x12\x1f\n\nfeed_label\x18\x04 \x01(\tB\x06\xe0A\x01\xe0A\x05H\x00\x88\x01\x01\x12%\n\x10content_language\x18\x05 \x01(\tB\x06\xe0A\x01\xe0A\x05H\x01\x88\x01\x01\x12\x16\n\tcountries\x18\x06 \x03(\tB\x03\xe0A\x01\x12h\n\x0cdefault_rule\x18\x07 \x01(\x0b2M.google.shopping.merchant.datasources.v1.PrimaryProductDataSource.DefaultRuleB\x03\xe0A\x01\x12"\n\x15contains_custom_rules\x18\t \x01(\x08B\x03\xe0A\x03\x12h\n\x0cdestinations\x18\n \x03(\x0b2M.google.shopping.merchant.datasources.v1.PrimaryProductDataSource.DestinationB\x03\xe0A\x01\x1ap\n\x0bDefaultRule\x12a\n\x16take_from_data_sources\x18\x01 \x03(\x0b2<.google.shopping.merchant.datasources.v1.DataSourceReferenceB\x03\xe0A\x02\x1a\xf4\x01\n\x0bDestination\x12F\n\x0bdestination\x18\x01 \x01(\x0e21.google.shopping.type.Destination.DestinationEnum\x12b\n\x05state\x18\x02 \x01(\x0e2S.google.shopping.merchant.datasources.v1.PrimaryProductDataSource.Destination.State"9\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\x0c\n\x08DISABLED\x10\x02B\r\n\x0b_feed_labelB\x13\n\x11_content_language"\xf8\x01\n\x1dSupplementalProductDataSource\x12\x1f\n\nfeed_label\x18\x04 \x01(\tB\x06\xe0A\x01\xe0A\x05H\x00\x88\x01\x01\x12%\n\x10content_language\x18\x05 \x01(\tB\x06\xe0A\x01\xe0A\x05H\x01\x88\x01\x01\x12k\n referencing_primary_data_sources\x18\x07 \x03(\x0b2<.google.shopping.merchant.datasources.v1.DataSourceReferenceB\x03\xe0A\x03B\r\n\x0b_feed_labelB\x13\n\x11_content_language"X\n\x18LocalInventoryDataSource\x12\x1a\n\nfeed_label\x18\x04 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12 \n\x10content_language\x18\x05 \x01(\tB\x06\xe0A\x02\xe0A\x05"[\n\x1bRegionalInventoryDataSource\x12\x1a\n\nfeed_label\x18\x04 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12 \n\x10content_language\x18\x05 \x01(\tB\x06\xe0A\x02\xe0A\x05"W\n\x13PromotionDataSource\x12\x1e\n\x0etarget_country\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12 \n\x10content_language\x18\x02 \x01(\tB\x06\xe0A\x02\xe0A\x05"\x19\n\x17ProductReviewDataSource"\x1a\n\x18MerchantReviewDataSource"\x8e\x01\n\x13DataSourceReference\x12\x0e\n\x04self\x18\x01 \x01(\x08H\x00\x12\'\n\x18primary_data_source_name\x18\x03 \x01(\tB\x03\xe0A\x01H\x00\x12,\n\x1dsupplemental_data_source_name\x18\x02 \x01(\tB\x03\xe0A\x01H\x00B\x10\n\x0edata_source_idB\x9c\x02\n+com.google.shopping.merchant.datasources.v1B\x14DatasourcetypesProtoP\x01ZScloud.google.com/go/shopping/merchant/datasources/apiv1/datasourcespb;datasourcespb\xaa\x02\'Google.Shopping.Merchant.DataSources.V1\xca\x02\'Google\\Shopping\\Merchant\\DataSources\\V1\xea\x02+Google::Shopping::Merchant::DataSources::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.datasources.v1.datasourcetypes_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.shopping.merchant.datasources.v1B\x14DatasourcetypesProtoP\x01ZScloud.google.com/go/shopping/merchant/datasources/apiv1/datasourcespb;datasourcespb\xaa\x02'Google.Shopping.Merchant.DataSources.V1\xca\x02'Google\\Shopping\\Merchant\\DataSources\\V1\xea\x02+Google::Shopping::Merchant::DataSources::V1"
    _globals['_PRIMARYPRODUCTDATASOURCE_DEFAULTRULE'].fields_by_name['take_from_data_sources']._loaded_options = None
    _globals['_PRIMARYPRODUCTDATASOURCE_DEFAULTRULE'].fields_by_name['take_from_data_sources']._serialized_options = b'\xe0A\x02'
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['legacy_local']._loaded_options = None
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['legacy_local']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['feed_label']._loaded_options = None
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['feed_label']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['content_language']._loaded_options = None
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['content_language']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['countries']._loaded_options = None
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['countries']._serialized_options = b'\xe0A\x01'
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['default_rule']._loaded_options = None
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['default_rule']._serialized_options = b'\xe0A\x01'
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['contains_custom_rules']._loaded_options = None
    _globals['_PRIMARYPRODUCTDATASOURCE'].fields_by_name['contains_custom_rules']._serialized_options = b'\xe0A\x03'
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
    _globals['_PRIMARYPRODUCTDATASOURCE']._serialized_start = 174
    _globals['_PRIMARYPRODUCTDATASOURCE']._serialized_end = 971
    _globals['_PRIMARYPRODUCTDATASOURCE_DEFAULTRULE']._serialized_start = 576
    _globals['_PRIMARYPRODUCTDATASOURCE_DEFAULTRULE']._serialized_end = 688
    _globals['_PRIMARYPRODUCTDATASOURCE_DESTINATION']._serialized_start = 691
    _globals['_PRIMARYPRODUCTDATASOURCE_DESTINATION']._serialized_end = 935
    _globals['_PRIMARYPRODUCTDATASOURCE_DESTINATION_STATE']._serialized_start = 878
    _globals['_PRIMARYPRODUCTDATASOURCE_DESTINATION_STATE']._serialized_end = 935
    _globals['_SUPPLEMENTALPRODUCTDATASOURCE']._serialized_start = 974
    _globals['_SUPPLEMENTALPRODUCTDATASOURCE']._serialized_end = 1222
    _globals['_LOCALINVENTORYDATASOURCE']._serialized_start = 1224
    _globals['_LOCALINVENTORYDATASOURCE']._serialized_end = 1312
    _globals['_REGIONALINVENTORYDATASOURCE']._serialized_start = 1314
    _globals['_REGIONALINVENTORYDATASOURCE']._serialized_end = 1405
    _globals['_PROMOTIONDATASOURCE']._serialized_start = 1407
    _globals['_PROMOTIONDATASOURCE']._serialized_end = 1494
    _globals['_PRODUCTREVIEWDATASOURCE']._serialized_start = 1496
    _globals['_PRODUCTREVIEWDATASOURCE']._serialized_end = 1521
    _globals['_MERCHANTREVIEWDATASOURCE']._serialized_start = 1523
    _globals['_MERCHANTREVIEWDATASOURCE']._serialized_end = 1549
    _globals['_DATASOURCEREFERENCE']._serialized_start = 1552
    _globals['_DATASOURCEREFERENCE']._serialized_end = 1694