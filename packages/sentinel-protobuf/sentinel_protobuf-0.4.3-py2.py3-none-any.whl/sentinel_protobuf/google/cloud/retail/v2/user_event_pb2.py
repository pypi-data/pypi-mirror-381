"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2/user_event.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.retail.v2 import common_pb2 as google_dot_cloud_dot_retail_dot_v2_dot_common__pb2
from .....google.cloud.retail.v2 import product_pb2 as google_dot_cloud_dot_retail_dot_v2_dot_product__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/retail/v2/user_event.proto\x12\x16google.cloud.retail.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a#google/cloud/retail/v2/common.proto\x1a$google/cloud/retail/v2/product.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x97\x06\n\tUserEvent\x12\x17\n\nevent_type\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\nvisitor_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x12\n\nsession_id\x18\x15 \x01(\t\x12.\n\nevent_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x16\n\x0eexperiment_ids\x18\x04 \x03(\t\x12\x19\n\x11attribution_token\x18\x05 \x01(\t\x12>\n\x0fproduct_details\x18\x06 \x03(\x0b2%.google.cloud.retail.v2.ProductDetail\x12C\n\x11completion_detail\x18\x16 \x01(\x0b2(.google.cloud.retail.v2.CompletionDetail\x12E\n\nattributes\x18\x07 \x03(\x0b21.google.cloud.retail.v2.UserEvent.AttributesEntry\x12\x0f\n\x07cart_id\x18\x08 \x01(\t\x12I\n\x14purchase_transaction\x18\t \x01(\x0b2+.google.cloud.retail.v2.PurchaseTransaction\x12\x14\n\x0csearch_query\x18\n \x01(\t\x12\x0e\n\x06filter\x18\x10 \x01(\t\x12\x10\n\x08order_by\x18\x11 \x01(\t\x12\x0e\n\x06offset\x18\x12 \x01(\x05\x12\x17\n\x0fpage_categories\x18\x0b \x03(\t\x123\n\tuser_info\x18\x0c \x01(\x0b2 .google.cloud.retail.v2.UserInfo\x12\x0b\n\x03uri\x18\r \x01(\t\x12\x14\n\x0creferrer_uri\x18\x0e \x01(\t\x12\x14\n\x0cpage_view_id\x18\x0f \x01(\t\x12\x0e\n\x06entity\x18\x17 \x01(\t\x1aZ\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x126\n\x05value\x18\x02 \x01(\x0b2\'.google.cloud.retail.v2.CustomAttribute:\x028\x01"u\n\rProductDetail\x125\n\x07product\x18\x01 \x01(\x0b2\x1f.google.cloud.retail.v2.ProductB\x03\xe0A\x02\x12-\n\x08quantity\x18\x02 \x01(\x0b2\x1b.google.protobuf.Int32Value"p\n\x10CompletionDetail\x12$\n\x1ccompletion_attribution_token\x18\x01 \x01(\t\x12\x1b\n\x13selected_suggestion\x18\x02 \x01(\t\x12\x19\n\x11selected_position\x18\x03 \x01(\x05"n\n\x13PurchaseTransaction\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x07revenue\x18\x02 \x01(\x02B\x03\xe0A\x02\x12\x0b\n\x03tax\x18\x03 \x01(\x02\x12\x0c\n\x04cost\x18\x04 \x01(\x02\x12\x1a\n\rcurrency_code\x18\x05 \x01(\tB\x03\xe0A\x02B\xb9\x01\n\x1acom.google.cloud.retail.v2B\x0eUserEventProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2.user_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.retail.v2B\x0eUserEventProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2'
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
    _globals['_USEREVENT']._serialized_start = 241
    _globals['_USEREVENT']._serialized_end = 1032
    _globals['_USEREVENT_ATTRIBUTESENTRY']._serialized_start = 942
    _globals['_USEREVENT_ATTRIBUTESENTRY']._serialized_end = 1032
    _globals['_PRODUCTDETAIL']._serialized_start = 1034
    _globals['_PRODUCTDETAIL']._serialized_end = 1151
    _globals['_COMPLETIONDETAIL']._serialized_start = 1153
    _globals['_COMPLETIONDETAIL']._serialized_end = 1265
    _globals['_PURCHASETRANSACTION']._serialized_start = 1267
    _globals['_PURCHASETRANSACTION']._serialized_end = 1377