"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/datamanager/v1/cart_data.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/ads/datamanager/v1/cart_data.proto\x12\x19google.ads.datamanager.v1\x1a\x1fgoogle/api/field_behavior.proto"\xc8\x01\n\x08CartData\x12\x18\n\x0bmerchant_id\x18\x01 \x01(\tB\x03\xe0A\x01\x12 \n\x13merchant_feed_label\x18\x02 \x01(\tB\x03\xe0A\x01\x12(\n\x1bmerchant_feed_language_code\x18\x03 \x01(\tB\x03\xe0A\x01\x12!\n\x14transaction_discount\x18\x04 \x01(\x01B\x03\xe0A\x01\x123\n\x05items\x18\x05 \x03(\x0b2\x1f.google.ads.datamanager.v1.ItemB\x03\xe0A\x01"X\n\x04Item\x12 \n\x13merchant_product_id\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08quantity\x18\x02 \x01(\x03B\x03\xe0A\x01\x12\x17\n\nunit_price\x18\x03 \x01(\x01B\x03\xe0A\x01B\xcd\x01\n\x1dcom.google.ads.datamanager.v1B\rCartDataProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager\xaa\x02\x19Google.Ads.DataManager.V1\xca\x02\x19Google\\Ads\\DataManager\\V1\xea\x02\x1cGoogle::Ads::DataManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.datamanager.v1.cart_data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.ads.datamanager.v1B\rCartDataProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager\xaa\x02\x19Google.Ads.DataManager.V1\xca\x02\x19Google\\Ads\\DataManager\\V1\xea\x02\x1cGoogle::Ads::DataManager::V1'
    _globals['_CARTDATA'].fields_by_name['merchant_id']._loaded_options = None
    _globals['_CARTDATA'].fields_by_name['merchant_id']._serialized_options = b'\xe0A\x01'
    _globals['_CARTDATA'].fields_by_name['merchant_feed_label']._loaded_options = None
    _globals['_CARTDATA'].fields_by_name['merchant_feed_label']._serialized_options = b'\xe0A\x01'
    _globals['_CARTDATA'].fields_by_name['merchant_feed_language_code']._loaded_options = None
    _globals['_CARTDATA'].fields_by_name['merchant_feed_language_code']._serialized_options = b'\xe0A\x01'
    _globals['_CARTDATA'].fields_by_name['transaction_discount']._loaded_options = None
    _globals['_CARTDATA'].fields_by_name['transaction_discount']._serialized_options = b'\xe0A\x01'
    _globals['_CARTDATA'].fields_by_name['items']._loaded_options = None
    _globals['_CARTDATA'].fields_by_name['items']._serialized_options = b'\xe0A\x01'
    _globals['_ITEM'].fields_by_name['merchant_product_id']._loaded_options = None
    _globals['_ITEM'].fields_by_name['merchant_product_id']._serialized_options = b'\xe0A\x01'
    _globals['_ITEM'].fields_by_name['quantity']._loaded_options = None
    _globals['_ITEM'].fields_by_name['quantity']._serialized_options = b'\xe0A\x01'
    _globals['_ITEM'].fields_by_name['unit_price']._loaded_options = None
    _globals['_ITEM'].fields_by_name['unit_price']._serialized_options = b'\xe0A\x01'
    _globals['_CARTDATA']._serialized_start = 106
    _globals['_CARTDATA']._serialized_end = 306
    _globals['_ITEM']._serialized_start = 308
    _globals['_ITEM']._serialized_end = 396