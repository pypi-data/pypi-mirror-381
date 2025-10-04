"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/promotions/v1beta/promotions_common.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
from ......google.type import interval_pb2 as google_dot_type_dot_interval__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/shopping/merchant/promotions/v1beta/promotions_common.proto\x12*google.shopping.merchant.promotions.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a google/shopping/type/types.proto\x1a\x1agoogle/type/interval.proto"\xd5\x0b\n\nAttributes\x12d\n\x15product_applicability\x18\x01 \x01(\x0e2@.google.shopping.merchant.promotions.v1beta.ProductApplicabilityB\x03\xe0A\x02\x12N\n\noffer_type\x18\x02 \x01(\x0e25.google.shopping.merchant.promotions.v1beta.OfferTypeB\x03\xe0A\x02\x12$\n\x17generic_redemption_code\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x17\n\nlong_title\x18\x04 \x01(\tB\x03\xe0A\x02\x12[\n\x11coupon_value_type\x18\x05 \x01(\x0e2;.google.shopping.merchant.promotions.v1beta.CouponValueTypeB\x03\xe0A\x02\x12V\n\x16promotion_destinations\x18\x06 \x03(\x0e21.google.shopping.type.Destination.DestinationEnumB\x03\xe0A\x02\x12\x1e\n\x11item_id_inclusion\x18\x07 \x03(\tB\x03\xe0A\x01\x12\x1c\n\x0fbrand_inclusion\x18\x08 \x03(\tB\x03\xe0A\x01\x12$\n\x17item_group_id_inclusion\x18\t \x03(\tB\x03\xe0A\x01\x12#\n\x16product_type_inclusion\x18\n \x03(\tB\x03\xe0A\x01\x12\x1e\n\x11item_id_exclusion\x18\x0b \x03(\tB\x03\xe0A\x01\x12\x1c\n\x0fbrand_exclusion\x18\x0c \x03(\tB\x03\xe0A\x01\x12$\n\x17item_group_id_exclusion\x18\r \x03(\tB\x03\xe0A\x01\x12#\n\x16product_type_exclusion\x18\x0e \x03(\tB\x03\xe0A\x01\x12A\n\x17minimum_purchase_amount\x18\x0f \x01(\x0b2\x1b.google.shopping.type.PriceB\x03\xe0A\x01\x12&\n\x19minimum_purchase_quantity\x18\x10 \x01(\x03B\x03\xe0A\x01\x12\x1b\n\x0elimit_quantity\x18\x11 \x01(\x03B\x03\xe0A\x01\x125\n\x0blimit_value\x18\x12 \x01(\x0b2\x1b.google.shopping.type.PriceB\x03\xe0A\x01\x12\x18\n\x0bpercent_off\x18\x13 \x01(\x03B\x03\xe0A\x01\x12:\n\x10money_off_amount\x18\x14 \x01(\x0b2\x1b.google.shopping.type.PriceB\x03\xe0A\x01\x12)\n\x1cget_this_quantity_discounted\x18\x15 \x01(\x03B\x03\xe0A\x01\x129\n\x0ffree_gift_value\x18\x16 \x01(\x0b2\x1b.google.shopping.type.PriceB\x03\xe0A\x01\x12"\n\x15free_gift_description\x18\x17 \x01(\tB\x03\xe0A\x01\x12\x1e\n\x11free_gift_item_id\x18\x18 \x01(\tB\x03\xe0A\x01\x12C\n\x1fpromotion_effective_time_period\x18\x19 \x01(\x0b2\x15.google.type.IntervalB\x03\xe0A\x02\x12A\n\x1dpromotion_display_time_period\x18\x1a \x01(\x0b2\x15.google.type.IntervalB\x03\xe0A\x01\x12`\n\x13store_applicability\x18\x1c \x01(\x0e2>.google.shopping.merchant.promotions.v1beta.StoreApplicabilityB\x03\xe0A\x01\x12"\n\x15store_codes_inclusion\x18\x1d \x03(\tB\x03\xe0A\x01\x12"\n\x15store_codes_exclusion\x18\x1e \x03(\tB\x03\xe0A\x01\x12\x1a\n\rpromotion_url\x18\x1f \x01(\tB\x03\xe0A\x01"\x91\t\n\x0fPromotionStatus\x12p\n\x14destination_statuses\x18\x01 \x03(\x0b2M.google.shopping.merchant.promotions.v1beta.PromotionStatus.DestinationStatusB\x03\xe0A\x03\x12j\n\x11item_level_issues\x18\x02 \x03(\x0b2J.google.shopping.merchant.promotions.v1beta.PromotionStatus.ItemLevelIssueB\x03\xe0A\x03\x126\n\rcreation_date\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x129\n\x10last_update_date\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a\xc8\x02\n\x11DestinationStatus\x12[\n\x11reporting_context\x18\x01 \x01(\x0e2;.google.shopping.type.ReportingContext.ReportingContextEnumB\x03\xe0A\x03\x12h\n\x06status\x18\x02 \x01(\x0e2S.google.shopping.merchant.promotions.v1beta.PromotionStatus.DestinationStatus.StateB\x03\xe0A\x03"l\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tIN_REVIEW\x10\x01\x12\x0c\n\x08REJECTED\x10\x02\x12\x08\n\x04LIVE\x10\x03\x12\x0b\n\x07STOPPED\x10\x04\x12\x0b\n\x07EXPIRED\x10\x05\x12\x0b\n\x07PENDING\x10\x06\x1a\xe1\x03\n\x0eItemLevelIssue\x12\x11\n\x04code\x18\x01 \x01(\tB\x03\xe0A\x03\x12j\n\x08severity\x18\x02 \x01(\x0e2S.google.shopping.merchant.promotions.v1beta.PromotionStatus.ItemLevelIssue.SeverityB\x03\xe0A\x03\x12\x17\n\nresolution\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x16\n\tattribute\x18\x04 \x01(\tB\x03\xe0A\x03\x12[\n\x11reporting_context\x18\x05 \x01(\x0e2;.google.shopping.type.ReportingContext.ReportingContextEnumB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x06 \x01(\tB\x03\xe0A\x03\x12\x13\n\x06detail\x18\x07 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rdocumentation\x18\x08 \x01(\tB\x03\xe0A\x03\x12!\n\x14applicable_countries\x18\t \x03(\tB\x03\xe0A\x03"T\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x10\n\x0cNOT_IMPACTED\x10\x01\x12\x0b\n\x07DEMOTED\x10\x02\x12\x0f\n\x0bDISAPPROVED\x10\x03*f\n\x14ProductApplicability\x12%\n!PRODUCT_APPLICABILITY_UNSPECIFIED\x10\x00\x12\x10\n\x0cALL_PRODUCTS\x10\x01\x12\x15\n\x11SPECIFIC_PRODUCTS\x10\x02*^\n\x12StoreApplicability\x12#\n\x1fSTORE_APPLICABILITY_UNSPECIFIED\x10\x00\x12\x0e\n\nALL_STORES\x10\x01\x12\x13\n\x0fSPECIFIC_STORES\x10\x02*F\n\tOfferType\x12\x1a\n\x16OFFER_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07NO_CODE\x10\x01\x12\x10\n\x0cGENERIC_CODE\x10\x02*Q\n\x11RedemptionChannel\x12"\n\x1eREDEMPTION_CHANNEL_UNSPECIFIED\x10\x00\x12\x0c\n\x08IN_STORE\x10\x01\x12\n\n\x06ONLINE\x10\x02*\xd9\x02\n\x0fCouponValueType\x12!\n\x1dCOUPON_VALUE_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tMONEY_OFF\x10\x01\x12\x0f\n\x0bPERCENT_OFF\x10\x02\x12\x19\n\x15BUY_M_GET_N_MONEY_OFF\x10\x03\x12\x1b\n\x17BUY_M_GET_N_PERCENT_OFF\x10\x04\x12\x17\n\x13BUY_M_GET_MONEY_OFF\x10\x05\x12\x19\n\x15BUY_M_GET_PERCENT_OFF\x10\x06\x12\r\n\tFREE_GIFT\x10\x07\x12\x18\n\x14FREE_GIFT_WITH_VALUE\x10\x08\x12\x1a\n\x16FREE_GIFT_WITH_ITEM_ID\x10\t\x12\x1a\n\x16FREE_SHIPPING_STANDARD\x10\n\x12\x1b\n\x17FREE_SHIPPING_OVERNIGHT\x10\x0b\x12\x19\n\x15FREE_SHIPPING_TWO_DAY\x10\x0cB\x9f\x01\n.com.google.shopping.merchant.promotions.v1betaB\x15PromotionsCommonProtoP\x01ZTcloud.google.com/go/shopping/merchant/promotions/apiv1beta/promotionspb;promotionspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.promotions.v1beta.promotions_common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n.com.google.shopping.merchant.promotions.v1betaB\x15PromotionsCommonProtoP\x01ZTcloud.google.com/go/shopping/merchant/promotions/apiv1beta/promotionspb;promotionspb'
    _globals['_ATTRIBUTES'].fields_by_name['product_applicability']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['product_applicability']._serialized_options = b'\xe0A\x02'
    _globals['_ATTRIBUTES'].fields_by_name['offer_type']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['offer_type']._serialized_options = b'\xe0A\x02'
    _globals['_ATTRIBUTES'].fields_by_name['generic_redemption_code']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['generic_redemption_code']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['long_title']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['long_title']._serialized_options = b'\xe0A\x02'
    _globals['_ATTRIBUTES'].fields_by_name['coupon_value_type']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['coupon_value_type']._serialized_options = b'\xe0A\x02'
    _globals['_ATTRIBUTES'].fields_by_name['promotion_destinations']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['promotion_destinations']._serialized_options = b'\xe0A\x02'
    _globals['_ATTRIBUTES'].fields_by_name['item_id_inclusion']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['item_id_inclusion']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['brand_inclusion']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['brand_inclusion']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['item_group_id_inclusion']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['item_group_id_inclusion']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['product_type_inclusion']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['product_type_inclusion']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['item_id_exclusion']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['item_id_exclusion']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['brand_exclusion']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['brand_exclusion']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['item_group_id_exclusion']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['item_group_id_exclusion']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['product_type_exclusion']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['product_type_exclusion']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['minimum_purchase_amount']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['minimum_purchase_amount']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['minimum_purchase_quantity']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['minimum_purchase_quantity']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['limit_quantity']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['limit_quantity']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['limit_value']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['limit_value']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['percent_off']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['percent_off']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['money_off_amount']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['money_off_amount']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['get_this_quantity_discounted']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['get_this_quantity_discounted']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['free_gift_value']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['free_gift_value']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['free_gift_description']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['free_gift_description']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['free_gift_item_id']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['free_gift_item_id']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['promotion_effective_time_period']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['promotion_effective_time_period']._serialized_options = b'\xe0A\x02'
    _globals['_ATTRIBUTES'].fields_by_name['promotion_display_time_period']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['promotion_display_time_period']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['store_applicability']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['store_applicability']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['store_codes_inclusion']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['store_codes_inclusion']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['store_codes_exclusion']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['store_codes_exclusion']._serialized_options = b'\xe0A\x01'
    _globals['_ATTRIBUTES'].fields_by_name['promotion_url']._loaded_options = None
    _globals['_ATTRIBUTES'].fields_by_name['promotion_url']._serialized_options = b'\xe0A\x01'
    _globals['_PROMOTIONSTATUS_DESTINATIONSTATUS'].fields_by_name['reporting_context']._loaded_options = None
    _globals['_PROMOTIONSTATUS_DESTINATIONSTATUS'].fields_by_name['reporting_context']._serialized_options = b'\xe0A\x03'
    _globals['_PROMOTIONSTATUS_DESTINATIONSTATUS'].fields_by_name['status']._loaded_options = None
    _globals['_PROMOTIONSTATUS_DESTINATIONSTATUS'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE'].fields_by_name['code']._loaded_options = None
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE'].fields_by_name['code']._serialized_options = b'\xe0A\x03'
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE'].fields_by_name['severity']._loaded_options = None
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE'].fields_by_name['severity']._serialized_options = b'\xe0A\x03'
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE'].fields_by_name['resolution']._loaded_options = None
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE'].fields_by_name['resolution']._serialized_options = b'\xe0A\x03'
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE'].fields_by_name['attribute']._loaded_options = None
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE'].fields_by_name['attribute']._serialized_options = b'\xe0A\x03'
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE'].fields_by_name['reporting_context']._loaded_options = None
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE'].fields_by_name['reporting_context']._serialized_options = b'\xe0A\x03'
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE'].fields_by_name['description']._loaded_options = None
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE'].fields_by_name['detail']._loaded_options = None
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE'].fields_by_name['detail']._serialized_options = b'\xe0A\x03'
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE'].fields_by_name['documentation']._loaded_options = None
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE'].fields_by_name['documentation']._serialized_options = b'\xe0A\x03'
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE'].fields_by_name['applicable_countries']._loaded_options = None
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE'].fields_by_name['applicable_countries']._serialized_options = b'\xe0A\x03'
    _globals['_PROMOTIONSTATUS'].fields_by_name['destination_statuses']._loaded_options = None
    _globals['_PROMOTIONSTATUS'].fields_by_name['destination_statuses']._serialized_options = b'\xe0A\x03'
    _globals['_PROMOTIONSTATUS'].fields_by_name['item_level_issues']._loaded_options = None
    _globals['_PROMOTIONSTATUS'].fields_by_name['item_level_issues']._serialized_options = b'\xe0A\x03'
    _globals['_PROMOTIONSTATUS'].fields_by_name['creation_date']._loaded_options = None
    _globals['_PROMOTIONSTATUS'].fields_by_name['creation_date']._serialized_options = b'\xe0A\x03'
    _globals['_PROMOTIONSTATUS'].fields_by_name['last_update_date']._loaded_options = None
    _globals['_PROMOTIONSTATUS'].fields_by_name['last_update_date']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTAPPLICABILITY']._serialized_start = 2910
    _globals['_PRODUCTAPPLICABILITY']._serialized_end = 3012
    _globals['_STOREAPPLICABILITY']._serialized_start = 3014
    _globals['_STOREAPPLICABILITY']._serialized_end = 3108
    _globals['_OFFERTYPE']._serialized_start = 3110
    _globals['_OFFERTYPE']._serialized_end = 3180
    _globals['_REDEMPTIONCHANNEL']._serialized_start = 3182
    _globals['_REDEMPTIONCHANNEL']._serialized_end = 3263
    _globals['_COUPONVALUETYPE']._serialized_start = 3266
    _globals['_COUPONVALUETYPE']._serialized_end = 3611
    _globals['_ATTRIBUTES']._serialized_start = 243
    _globals['_ATTRIBUTES']._serialized_end = 1736
    _globals['_PROMOTIONSTATUS']._serialized_start = 1739
    _globals['_PROMOTIONSTATUS']._serialized_end = 2908
    _globals['_PROMOTIONSTATUS_DESTINATIONSTATUS']._serialized_start = 2096
    _globals['_PROMOTIONSTATUS_DESTINATIONSTATUS']._serialized_end = 2424
    _globals['_PROMOTIONSTATUS_DESTINATIONSTATUS_STATE']._serialized_start = 2316
    _globals['_PROMOTIONSTATUS_DESTINATIONSTATUS_STATE']._serialized_end = 2424
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE']._serialized_start = 2427
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE']._serialized_end = 2908
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE_SEVERITY']._serialized_start = 2824
    _globals['_PROMOTIONSTATUS_ITEMLEVELISSUE_SEVERITY']._serialized_end = 2908