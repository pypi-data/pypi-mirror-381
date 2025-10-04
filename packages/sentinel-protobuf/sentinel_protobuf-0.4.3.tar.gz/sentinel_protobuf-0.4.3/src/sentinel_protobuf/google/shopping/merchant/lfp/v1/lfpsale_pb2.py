"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/lfp/v1/lfpsale.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/shopping/merchant/lfp/v1/lfpsale.proto\x12\x1fgoogle.shopping.merchant.lfp.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a google/shopping/type/types.proto"\xe8\x03\n\x07LfpSale\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x08\x12\x1b\n\x0etarget_account\x18\x02 \x01(\x03B\x03\xe0A\x02\x12\x17\n\nstore_code\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08offer_id\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bregion_code\x18\x05 \x01(\tB\x03\xe0A\x02\x12\x1d\n\x10content_language\x18\x06 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04gtin\x18\x07 \x01(\tB\x03\xe0A\x02\x12/\n\x05price\x18\x08 \x01(\x0b2\x1b.google.shopping.type.PriceB\x03\xe0A\x02\x12\x15\n\x08quantity\x18\t \x01(\x03B\x03\xe0A\x02\x122\n\tsale_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02\x12\x1d\n\x03uid\x18\x0b \x01(\tB\x0b\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01H\x00\x88\x01\x01\x12\x1c\n\nfeed_label\x18\x0c \x01(\tB\x03\xe0A\x01H\x01\x88\x01\x01:^\xeaA[\n"merchantapi.googleapis.com/LfpSale\x12"accounts/{account}/lfpSales/{sale}*\x08lfpSales2\x07lfpSaleB\x06\n\x04_uidB\r\n\x0b_feed_label"l\n\x14InsertLfpSaleRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12?\n\x08lfp_sale\x18\x02 \x01(\x0b2(.google.shopping.merchant.lfp.v1.LfpSaleB\x03\xe0A\x022\x8b\x02\n\x0eLfpSaleService\x12\xaf\x01\n\rInsertLfpSale\x125.google.shopping.merchant.lfp.v1.InsertLfpSaleRequest\x1a(.google.shopping.merchant.lfp.v1.LfpSale"=\x82\xd3\xe4\x93\x027"+/lfp/v1/{parent=accounts/*}/lfpSales:insert:\x08lfp_sale\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xdc\x01\n#com.google.shopping.merchant.lfp.v1B\x0cLfpSaleProtoP\x01Z;cloud.google.com/go/shopping/merchant/lfp/apiv1/lfppb;lfppb\xaa\x02\x1fGoogle.Shopping.Merchant.Lfp.V1\xca\x02\x1fGoogle\\Shopping\\Merchant\\Lfp\\V1\xea\x02#Google::Shopping::Merchant::Lfp::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.lfp.v1.lfpsale_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.shopping.merchant.lfp.v1B\x0cLfpSaleProtoP\x01Z;cloud.google.com/go/shopping/merchant/lfp/apiv1/lfppb;lfppb\xaa\x02\x1fGoogle.Shopping.Merchant.Lfp.V1\xca\x02\x1fGoogle\\Shopping\\Merchant\\Lfp\\V1\xea\x02#Google::Shopping::Merchant::Lfp::V1'
    _globals['_LFPSALE'].fields_by_name['name']._loaded_options = None
    _globals['_LFPSALE'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x08'
    _globals['_LFPSALE'].fields_by_name['target_account']._loaded_options = None
    _globals['_LFPSALE'].fields_by_name['target_account']._serialized_options = b'\xe0A\x02'
    _globals['_LFPSALE'].fields_by_name['store_code']._loaded_options = None
    _globals['_LFPSALE'].fields_by_name['store_code']._serialized_options = b'\xe0A\x02'
    _globals['_LFPSALE'].fields_by_name['offer_id']._loaded_options = None
    _globals['_LFPSALE'].fields_by_name['offer_id']._serialized_options = b'\xe0A\x02'
    _globals['_LFPSALE'].fields_by_name['region_code']._loaded_options = None
    _globals['_LFPSALE'].fields_by_name['region_code']._serialized_options = b'\xe0A\x02'
    _globals['_LFPSALE'].fields_by_name['content_language']._loaded_options = None
    _globals['_LFPSALE'].fields_by_name['content_language']._serialized_options = b'\xe0A\x02'
    _globals['_LFPSALE'].fields_by_name['gtin']._loaded_options = None
    _globals['_LFPSALE'].fields_by_name['gtin']._serialized_options = b'\xe0A\x02'
    _globals['_LFPSALE'].fields_by_name['price']._loaded_options = None
    _globals['_LFPSALE'].fields_by_name['price']._serialized_options = b'\xe0A\x02'
    _globals['_LFPSALE'].fields_by_name['quantity']._loaded_options = None
    _globals['_LFPSALE'].fields_by_name['quantity']._serialized_options = b'\xe0A\x02'
    _globals['_LFPSALE'].fields_by_name['sale_time']._loaded_options = None
    _globals['_LFPSALE'].fields_by_name['sale_time']._serialized_options = b'\xe0A\x02'
    _globals['_LFPSALE'].fields_by_name['uid']._loaded_options = None
    _globals['_LFPSALE'].fields_by_name['uid']._serialized_options = b'\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_LFPSALE'].fields_by_name['feed_label']._loaded_options = None
    _globals['_LFPSALE'].fields_by_name['feed_label']._serialized_options = b'\xe0A\x01'
    _globals['_LFPSALE']._loaded_options = None
    _globals['_LFPSALE']._serialized_options = b'\xeaA[\n"merchantapi.googleapis.com/LfpSale\x12"accounts/{account}/lfpSales/{sale}*\x08lfpSales2\x07lfpSale'
    _globals['_INSERTLFPSALEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_INSERTLFPSALEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_INSERTLFPSALEREQUEST'].fields_by_name['lfp_sale']._loaded_options = None
    _globals['_INSERTLFPSALEREQUEST'].fields_by_name['lfp_sale']._serialized_options = b'\xe0A\x02'
    _globals['_LFPSALESERVICE']._loaded_options = None
    _globals['_LFPSALESERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_LFPSALESERVICE'].methods_by_name['InsertLfpSale']._loaded_options = None
    _globals['_LFPSALESERVICE'].methods_by_name['InsertLfpSale']._serialized_options = b'\x82\xd3\xe4\x93\x027"+/lfp/v1/{parent=accounts/*}/lfpSales:insert:\x08lfp_sale'
    _globals['_LFPSALE']._serialized_start = 294
    _globals['_LFPSALE']._serialized_end = 782
    _globals['_INSERTLFPSALEREQUEST']._serialized_start = 784
    _globals['_INSERTLFPSALEREQUEST']._serialized_end = 892
    _globals['_LFPSALESERVICE']._serialized_start = 895
    _globals['_LFPSALESERVICE']._serialized_end = 1162