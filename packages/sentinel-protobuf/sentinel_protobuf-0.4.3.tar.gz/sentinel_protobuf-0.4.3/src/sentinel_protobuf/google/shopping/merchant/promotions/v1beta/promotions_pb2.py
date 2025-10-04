"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/promotions/v1beta/promotions.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.shopping.merchant.promotions.v1beta import promotions_common_pb2 as google_dot_shopping_dot_merchant_dot_promotions_dot_v1beta_dot_promotions__common__pb2
from ......google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/shopping/merchant/promotions/v1beta/promotions.proto\x12*google.shopping.merchant.promotions.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1aBgoogle/shopping/merchant/promotions/v1beta/promotions_common.proto\x1a google/shopping/type/types.proto"\x85\x05\n\tPromotion\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cpromotion_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1d\n\x10content_language\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x0etarget_country\x18\x04 \x01(\tB\x03\xe0A\x02\x12^\n\x12redemption_channel\x18\x05 \x03(\x0e2=.google.shopping.merchant.promotions.v1beta.RedemptionChannelB\x03\xe0A\x02\x12\x18\n\x0bdata_source\x18\x06 \x01(\tB\x03\xe0A\x03\x12O\n\nattributes\x18\x07 \x01(\x0b26.google.shopping.merchant.promotions.v1beta.AttributesB\x03\xe0A\x01\x12E\n\x11custom_attributes\x18\x08 \x03(\x0b2%.google.shopping.type.CustomAttributeB\x03\xe0A\x01\x12Z\n\x10promotion_status\x18\t \x01(\x0b2;.google.shopping.merchant.promotions.v1beta.PromotionStatusB\x03\xe0A\x03\x12 \n\x0eversion_number\x18\n \x01(\x03B\x03\xe0A\x01H\x00\x88\x01\x01:k\xeaAh\n$merchantapi.googleapis.com/Promotion\x12)accounts/{account}/promotions/{promotion}*\npromotions2\tpromotionB\x11\n\x0f_version_number"\x96\x01\n\x16InsertPromotionRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12M\n\tpromotion\x18\x02 \x01(\x0b25.google.shopping.merchant.promotions.v1beta.PromotionB\x03\xe0A\x02\x12\x18\n\x0bdata_source\x18\x03 \x01(\tB\x03\xe0A\x02"Q\n\x13GetPromotionRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$merchantapi.googleapis.com/Promotion"]\n\x15ListPromotionsRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x03\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x03"|\n\x16ListPromotionsResponse\x12I\n\npromotions\x18\x01 \x03(\x0b25.google.shopping.merchant.promotions.v1beta.Promotion\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xd9\x05\n\x11PromotionsService\x12\xd1\x01\n\x0fInsertPromotion\x12B.google.shopping.merchant.promotions.v1beta.InsertPromotionRequest\x1a5.google.shopping.merchant.promotions.v1beta.Promotion"C\x82\xd3\xe4\x93\x02="8/promotions/v1beta/{parent=accounts/*}/promotions:insert:\x01*\x12\xc8\x01\n\x0cGetPromotion\x12?.google.shopping.merchant.promotions.v1beta.GetPromotionRequest\x1a5.google.shopping.merchant.promotions.v1beta.Promotion"@\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/promotions/v1beta/{name=accounts/*/promotions/*}\x12\xdb\x01\n\x0eListPromotions\x12A.google.shopping.merchant.promotions.v1beta.ListPromotionsRequest\x1aB.google.shopping.merchant.promotions.v1beta.ListPromotionsResponse"B\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/promotions/v1beta/{parent=accounts/*}/promotions\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xd4\x01\n.com.google.shopping.merchant.promotions.v1betaB\x0fPromotionsProtoP\x01ZTcloud.google.com/go/shopping/merchant/promotions/apiv1beta/promotionspb;promotionspb\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.promotions.v1beta.promotions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n.com.google.shopping.merchant.promotions.v1betaB\x0fPromotionsProtoP\x01ZTcloud.google.com/go/shopping/merchant/promotions/apiv1beta/promotionspb;promotionspb\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}'
    _globals['_PROMOTION'].fields_by_name['name']._loaded_options = None
    _globals['_PROMOTION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_PROMOTION'].fields_by_name['promotion_id']._loaded_options = None
    _globals['_PROMOTION'].fields_by_name['promotion_id']._serialized_options = b'\xe0A\x02'
    _globals['_PROMOTION'].fields_by_name['content_language']._loaded_options = None
    _globals['_PROMOTION'].fields_by_name['content_language']._serialized_options = b'\xe0A\x02'
    _globals['_PROMOTION'].fields_by_name['target_country']._loaded_options = None
    _globals['_PROMOTION'].fields_by_name['target_country']._serialized_options = b'\xe0A\x02'
    _globals['_PROMOTION'].fields_by_name['redemption_channel']._loaded_options = None
    _globals['_PROMOTION'].fields_by_name['redemption_channel']._serialized_options = b'\xe0A\x02'
    _globals['_PROMOTION'].fields_by_name['data_source']._loaded_options = None
    _globals['_PROMOTION'].fields_by_name['data_source']._serialized_options = b'\xe0A\x03'
    _globals['_PROMOTION'].fields_by_name['attributes']._loaded_options = None
    _globals['_PROMOTION'].fields_by_name['attributes']._serialized_options = b'\xe0A\x01'
    _globals['_PROMOTION'].fields_by_name['custom_attributes']._loaded_options = None
    _globals['_PROMOTION'].fields_by_name['custom_attributes']._serialized_options = b'\xe0A\x01'
    _globals['_PROMOTION'].fields_by_name['promotion_status']._loaded_options = None
    _globals['_PROMOTION'].fields_by_name['promotion_status']._serialized_options = b'\xe0A\x03'
    _globals['_PROMOTION'].fields_by_name['version_number']._loaded_options = None
    _globals['_PROMOTION'].fields_by_name['version_number']._serialized_options = b'\xe0A\x01'
    _globals['_PROMOTION']._loaded_options = None
    _globals['_PROMOTION']._serialized_options = b'\xeaAh\n$merchantapi.googleapis.com/Promotion\x12)accounts/{account}/promotions/{promotion}*\npromotions2\tpromotion'
    _globals['_INSERTPROMOTIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_INSERTPROMOTIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_INSERTPROMOTIONREQUEST'].fields_by_name['promotion']._loaded_options = None
    _globals['_INSERTPROMOTIONREQUEST'].fields_by_name['promotion']._serialized_options = b'\xe0A\x02'
    _globals['_INSERTPROMOTIONREQUEST'].fields_by_name['data_source']._loaded_options = None
    _globals['_INSERTPROMOTIONREQUEST'].fields_by_name['data_source']._serialized_options = b'\xe0A\x02'
    _globals['_GETPROMOTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPROMOTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$merchantapi.googleapis.com/Promotion'
    _globals['_LISTPROMOTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPROMOTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_LISTPROMOTIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPROMOTIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x03'
    _globals['_LISTPROMOTIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPROMOTIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x03'
    _globals['_PROMOTIONSSERVICE']._loaded_options = None
    _globals['_PROMOTIONSSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_PROMOTIONSSERVICE'].methods_by_name['InsertPromotion']._loaded_options = None
    _globals['_PROMOTIONSSERVICE'].methods_by_name['InsertPromotion']._serialized_options = b'\x82\xd3\xe4\x93\x02="8/promotions/v1beta/{parent=accounts/*}/promotions:insert:\x01*'
    _globals['_PROMOTIONSSERVICE'].methods_by_name['GetPromotion']._loaded_options = None
    _globals['_PROMOTIONSSERVICE'].methods_by_name['GetPromotion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/promotions/v1beta/{name=accounts/*/promotions/*}'
    _globals['_PROMOTIONSSERVICE'].methods_by_name['ListPromotions']._loaded_options = None
    _globals['_PROMOTIONSSERVICE'].methods_by_name['ListPromotions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/promotions/v1beta/{parent=accounts/*}/promotions'
    _globals['_PROMOTION']._serialized_start = 325
    _globals['_PROMOTION']._serialized_end = 970
    _globals['_INSERTPROMOTIONREQUEST']._serialized_start = 973
    _globals['_INSERTPROMOTIONREQUEST']._serialized_end = 1123
    _globals['_GETPROMOTIONREQUEST']._serialized_start = 1125
    _globals['_GETPROMOTIONREQUEST']._serialized_end = 1206
    _globals['_LISTPROMOTIONSREQUEST']._serialized_start = 1208
    _globals['_LISTPROMOTIONSREQUEST']._serialized_end = 1301
    _globals['_LISTPROMOTIONSRESPONSE']._serialized_start = 1303
    _globals['_LISTPROMOTIONSRESPONSE']._serialized_end = 1427
    _globals['_PROMOTIONSSERVICE']._serialized_start = 1430
    _globals['_PROMOTIONSSERVICE']._serialized_end = 2159