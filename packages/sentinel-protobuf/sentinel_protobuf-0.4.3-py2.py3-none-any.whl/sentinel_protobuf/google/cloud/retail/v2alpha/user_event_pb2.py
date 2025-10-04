"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2alpha/user_event.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.retail.v2alpha import common_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_common__pb2
from .....google.cloud.retail.v2alpha import product_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_product__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/retail/v2alpha/user_event.proto\x12\x1bgoogle.cloud.retail.v2alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a(google/cloud/retail/v2alpha/common.proto\x1a)google/cloud/retail/v2alpha/product.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xb5\x06\n\tUserEvent\x12\x17\n\nevent_type\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\nvisitor_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x12\n\nsession_id\x18\x15 \x01(\t\x12.\n\nevent_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x16\n\x0eexperiment_ids\x18\x04 \x03(\t\x12\x19\n\x11attribution_token\x18\x05 \x01(\t\x12C\n\x0fproduct_details\x18\x06 \x03(\x0b2*.google.cloud.retail.v2alpha.ProductDetail\x12H\n\x11completion_detail\x18\x16 \x01(\x0b2-.google.cloud.retail.v2alpha.CompletionDetail\x12J\n\nattributes\x18\x07 \x03(\x0b26.google.cloud.retail.v2alpha.UserEvent.AttributesEntry\x12\x0f\n\x07cart_id\x18\x08 \x01(\t\x12N\n\x14purchase_transaction\x18\t \x01(\x0b20.google.cloud.retail.v2alpha.PurchaseTransaction\x12\x14\n\x0csearch_query\x18\n \x01(\t\x12\x0e\n\x06filter\x18\x10 \x01(\t\x12\x10\n\x08order_by\x18\x11 \x01(\t\x12\x0e\n\x06offset\x18\x12 \x01(\x05\x12\x17\n\x0fpage_categories\x18\x0b \x03(\t\x128\n\tuser_info\x18\x0c \x01(\x0b2%.google.cloud.retail.v2alpha.UserInfo\x12\x0b\n\x03uri\x18\r \x01(\t\x12\x14\n\x0creferrer_uri\x18\x0e \x01(\t\x12\x14\n\x0cpage_view_id\x18\x0f \x01(\t\x12\x0e\n\x06entity\x18\x17 \x01(\t\x1a_\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12;\n\x05value\x18\x02 \x01(\x0b2,.google.cloud.retail.v2alpha.CustomAttribute:\x028\x01"z\n\rProductDetail\x12:\n\x07product\x18\x01 \x01(\x0b2$.google.cloud.retail.v2alpha.ProductB\x03\xe0A\x02\x12-\n\x08quantity\x18\x02 \x01(\x0b2\x1b.google.protobuf.Int32Value"p\n\x10CompletionDetail\x12$\n\x1ccompletion_attribution_token\x18\x01 \x01(\t\x12\x1b\n\x13selected_suggestion\x18\x02 \x01(\t\x12\x19\n\x11selected_position\x18\x03 \x01(\x05"n\n\x13PurchaseTransaction\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x07revenue\x18\x02 \x01(\x02B\x03\xe0A\x02\x12\x0b\n\x03tax\x18\x03 \x01(\x02\x12\x0c\n\x04cost\x18\x04 \x01(\x02\x12\x1a\n\rcurrency_code\x18\x05 \x01(\tB\x03\xe0A\x02B\xd2\x01\n\x1fcom.google.cloud.retail.v2alphaB\x0eUserEventProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2alpha.user_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.retail.v2alphaB\x0eUserEventProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alpha'
    _globals['_USEREVENT_ATTRIBUTESENTRY']._loaded_options = None
    _globals['_USEREVENT_ATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_USEREVENT'].fields_by_name['event_type']._loaded_options = None
    _globals['_USEREVENT'].fields_by_name['event_type']._serialized_options = b'\xe0A\x02'
    _globals['_USEREVENT'].fields_by_name['visitor_id']._loaded_options = None
    _globals['_USEREVENT'].fields_by_name['visitor_id']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCTDETAIL'].fields_by_name['product']._loaded_options = None
    _globals['_PRODUCTDETAIL'].fields_by_name['product']._serialized_options = b'\xe0A\x02'
    _globals['_PURCHASETRANSACTION'].fields_by_name['revenue']._loaded_options = None
    _globals['_PURCHASETRANSACTION'].fields_by_name['revenue']._serialized_options = b'\xe0A\x02'
    _globals['_PURCHASETRANSACTION'].fields_by_name['currency_code']._loaded_options = None
    _globals['_PURCHASETRANSACTION'].fields_by_name['currency_code']._serialized_options = b'\xe0A\x02'
    _globals['_USEREVENT']._serialized_start = 261
    _globals['_USEREVENT']._serialized_end = 1082
    _globals['_USEREVENT_ATTRIBUTESENTRY']._serialized_start = 987
    _globals['_USEREVENT_ATTRIBUTESENTRY']._serialized_end = 1082
    _globals['_PRODUCTDETAIL']._serialized_start = 1084
    _globals['_PRODUCTDETAIL']._serialized_end = 1206
    _globals['_COMPLETIONDETAIL']._serialized_start = 1208
    _globals['_COMPLETIONDETAIL']._serialized_end = 1320
    _globals['_PURCHASETRANSACTION']._serialized_start = 1322
    _globals['_PURCHASETRANSACTION']._serialized_end = 1432