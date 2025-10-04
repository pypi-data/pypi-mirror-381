"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/reviews/v1beta/merchantreviews_common.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDgoogle/shopping/merchant/reviews/v1beta/merchantreviews_common.proto\x12\'google.shopping.merchant.reviews.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a google/shopping/type/types.proto"\xa5\x08\n\x18MerchantReviewAttributes\x12\x1d\n\x0bmerchant_id\x18\x01 \x01(\tB\x03\xe0A\x02H\x00\x88\x01\x01\x12\'\n\x15merchant_display_name\x18\x02 \x01(\tB\x03\xe0A\x01H\x01\x88\x01\x01\x12\x1f\n\rmerchant_link\x18\x03 \x01(\tB\x03\xe0A\x01H\x02\x88\x01\x01\x12&\n\x14merchant_rating_link\x18\x04 \x01(\tB\x03\xe0A\x01H\x03\x88\x01\x01\x12\x1c\n\nmin_rating\x18\x05 \x01(\x03B\x03\xe0A\x01H\x04\x88\x01\x01\x12\x1c\n\nmax_rating\x18\x06 \x01(\x03B\x03\xe0A\x01H\x05\x88\x01\x01\x12\x18\n\x06rating\x18\x07 \x01(\x01B\x03\xe0A\x01H\x06\x88\x01\x01\x12\x17\n\x05title\x18\x08 \x01(\tB\x03\xe0A\x01H\x07\x88\x01\x01\x12\x19\n\x07content\x18\t \x01(\tB\x03\xe0A\x02H\x08\x88\x01\x01\x12\x1d\n\x0breviewer_id\x18\n \x01(\tB\x03\xe0A\x01H\t\x88\x01\x01\x12#\n\x11reviewer_username\x18\x0b \x01(\tB\x03\xe0A\x01H\n\x88\x01\x01\x12\x1e\n\x0cis_anonymous\x18\x0c \x01(\x08B\x03\xe0A\x01H\x0b\x88\x01\x01\x12w\n\x11collection_method\x18\r \x01(\x0e2R.google.shopping.merchant.reviews.v1beta.MerchantReviewAttributes.CollectionMethodB\x03\xe0A\x01H\x0c\x88\x01\x01\x129\n\x0breview_time\x18\x0e \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02H\r\x88\x01\x01\x12!\n\x0freview_language\x18\x0f \x01(\tB\x03\xe0A\x01H\x0e\x88\x01\x01\x12 \n\x0ereview_country\x18\x10 \x01(\tB\x03\xe0A\x01H\x0f\x88\x01\x01"y\n\x10CollectionMethod\x12!\n\x1dCOLLECTION_METHOD_UNSPECIFIED\x10\x00\x12\x18\n\x14MERCHANT_UNSOLICITED\x10\x01\x12\x11\n\rPOINT_OF_SALE\x10\x02\x12\x15\n\x11AFTER_FULFILLMENT\x10\x03B\x0e\n\x0c_merchant_idB\x18\n\x16_merchant_display_nameB\x10\n\x0e_merchant_linkB\x17\n\x15_merchant_rating_linkB\r\n\x0b_min_ratingB\r\n\x0b_max_ratingB\t\n\x07_ratingB\x08\n\x06_titleB\n\n\x08_contentB\x0e\n\x0c_reviewer_idB\x14\n\x12_reviewer_usernameB\x0f\n\r_is_anonymousB\x14\n\x12_collection_methodB\x0e\n\x0c_review_timeB\x12\n\x10_review_languageB\x11\n\x0f_review_country"\xd8\x07\n\x14MerchantReviewStatus\x12\x80\x01\n\x14destination_statuses\x18\x03 \x03(\x0b2].google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewDestinationStatusB\x03\xe0A\x03\x12z\n\x11item_level_issues\x18\x04 \x03(\x0b2Z.google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewItemLevelIssueB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x129\n\x10last_update_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a~\n\x1fMerchantReviewDestinationStatus\x12[\n\x11reporting_context\x18\x01 \x01(\x0e2;.google.shopping.type.ReportingContext.ReportingContextEnumB\x03\xe0A\x03\x1a\xcf\x03\n\x1cMerchantReviewItemLevelIssue\x12\x11\n\x04code\x18\x01 \x01(\tB\x03\xe0A\x03\x12z\n\x08severity\x18\x02 \x01(\x0e2c.google.shopping.merchant.reviews.v1beta.MerchantReviewStatus.MerchantReviewItemLevelIssue.SeverityB\x03\xe0A\x03\x12\x17\n\nresolution\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x16\n\tattribute\x18\x04 \x01(\tB\x03\xe0A\x03\x12[\n\x11reporting_context\x18\x05 \x01(\x0e2;.google.shopping.type.ReportingContext.ReportingContextEnumB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x06 \x01(\tB\x03\xe0A\x03\x12\x13\n\x06detail\x18\x07 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rdocumentation\x18\x08 \x01(\tB\x03\xe0A\x03"G\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x10\n\x0cNOT_IMPACTED\x10\x01\x12\x0f\n\x0bDISAPPROVED\x10\x02B\x9a\x02\n+com.google.shopping.merchant.reviews.v1betaB\x1aMerchantReviewsCommonProtoP\x01ZKcloud.google.com/go/shopping/merchant/reviews/apiv1beta/reviewspb;reviewspb\xaa\x02\'Google.Shopping.Merchant.Reviews.V1Beta\xca\x02\'Google\\Shopping\\Merchant\\Reviews\\V1beta\xea\x02+Google::Shopping::Merchant::Reviews::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.reviews.v1beta.merchantreviews_common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.shopping.merchant.reviews.v1betaB\x1aMerchantReviewsCommonProtoP\x01ZKcloud.google.com/go/shopping/merchant/reviews/apiv1beta/reviewspb;reviewspb\xaa\x02'Google.Shopping.Merchant.Reviews.V1Beta\xca\x02'Google\\Shopping\\Merchant\\Reviews\\V1beta\xea\x02+Google::Shopping::Merchant::Reviews::V1beta"
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['merchant_id']._loaded_options = None
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['merchant_id']._serialized_options = b'\xe0A\x02'
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['merchant_display_name']._loaded_options = None
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['merchant_display_name']._serialized_options = b'\xe0A\x01'
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['merchant_link']._loaded_options = None
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['merchant_link']._serialized_options = b'\xe0A\x01'
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['merchant_rating_link']._loaded_options = None
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['merchant_rating_link']._serialized_options = b'\xe0A\x01'
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['min_rating']._loaded_options = None
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['min_rating']._serialized_options = b'\xe0A\x01'
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['max_rating']._loaded_options = None
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['max_rating']._serialized_options = b'\xe0A\x01'
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['rating']._loaded_options = None
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['rating']._serialized_options = b'\xe0A\x01'
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['title']._loaded_options = None
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['title']._serialized_options = b'\xe0A\x01'
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['content']._loaded_options = None
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['content']._serialized_options = b'\xe0A\x02'
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['reviewer_id']._loaded_options = None
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['reviewer_id']._serialized_options = b'\xe0A\x01'
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['reviewer_username']._loaded_options = None
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['reviewer_username']._serialized_options = b'\xe0A\x01'
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['is_anonymous']._loaded_options = None
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['is_anonymous']._serialized_options = b'\xe0A\x01'
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['collection_method']._loaded_options = None
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['collection_method']._serialized_options = b'\xe0A\x01'
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['review_time']._loaded_options = None
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['review_time']._serialized_options = b'\xe0A\x02'
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['review_language']._loaded_options = None
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['review_language']._serialized_options = b'\xe0A\x01'
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['review_country']._loaded_options = None
    _globals['_MERCHANTREVIEWATTRIBUTES'].fields_by_name['review_country']._serialized_options = b'\xe0A\x01'
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWDESTINATIONSTATUS'].fields_by_name['reporting_context']._loaded_options = None
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWDESTINATIONSTATUS'].fields_by_name['reporting_context']._serialized_options = b'\xe0A\x03'
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWITEMLEVELISSUE'].fields_by_name['code']._loaded_options = None
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWITEMLEVELISSUE'].fields_by_name['code']._serialized_options = b'\xe0A\x03'
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWITEMLEVELISSUE'].fields_by_name['severity']._loaded_options = None
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWITEMLEVELISSUE'].fields_by_name['severity']._serialized_options = b'\xe0A\x03'
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWITEMLEVELISSUE'].fields_by_name['resolution']._loaded_options = None
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWITEMLEVELISSUE'].fields_by_name['resolution']._serialized_options = b'\xe0A\x03'
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWITEMLEVELISSUE'].fields_by_name['attribute']._loaded_options = None
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWITEMLEVELISSUE'].fields_by_name['attribute']._serialized_options = b'\xe0A\x03'
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWITEMLEVELISSUE'].fields_by_name['reporting_context']._loaded_options = None
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWITEMLEVELISSUE'].fields_by_name['reporting_context']._serialized_options = b'\xe0A\x03'
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWITEMLEVELISSUE'].fields_by_name['description']._loaded_options = None
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWITEMLEVELISSUE'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWITEMLEVELISSUE'].fields_by_name['detail']._loaded_options = None
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWITEMLEVELISSUE'].fields_by_name['detail']._serialized_options = b'\xe0A\x03'
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWITEMLEVELISSUE'].fields_by_name['documentation']._loaded_options = None
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWITEMLEVELISSUE'].fields_by_name['documentation']._serialized_options = b'\xe0A\x03'
    _globals['_MERCHANTREVIEWSTATUS'].fields_by_name['destination_statuses']._loaded_options = None
    _globals['_MERCHANTREVIEWSTATUS'].fields_by_name['destination_statuses']._serialized_options = b'\xe0A\x03'
    _globals['_MERCHANTREVIEWSTATUS'].fields_by_name['item_level_issues']._loaded_options = None
    _globals['_MERCHANTREVIEWSTATUS'].fields_by_name['item_level_issues']._serialized_options = b'\xe0A\x03'
    _globals['_MERCHANTREVIEWSTATUS'].fields_by_name['create_time']._loaded_options = None
    _globals['_MERCHANTREVIEWSTATUS'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MERCHANTREVIEWSTATUS'].fields_by_name['last_update_time']._loaded_options = None
    _globals['_MERCHANTREVIEWSTATUS'].fields_by_name['last_update_time']._serialized_options = b'\xe0A\x03'
    _globals['_MERCHANTREVIEWATTRIBUTES']._serialized_start = 214
    _globals['_MERCHANTREVIEWATTRIBUTES']._serialized_end = 1275
    _globals['_MERCHANTREVIEWATTRIBUTES_COLLECTIONMETHOD']._serialized_start = 874
    _globals['_MERCHANTREVIEWATTRIBUTES_COLLECTIONMETHOD']._serialized_end = 995
    _globals['_MERCHANTREVIEWSTATUS']._serialized_start = 1278
    _globals['_MERCHANTREVIEWSTATUS']._serialized_end = 2262
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWDESTINATIONSTATUS']._serialized_start = 1670
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWDESTINATIONSTATUS']._serialized_end = 1796
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWITEMLEVELISSUE']._serialized_start = 1799
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWITEMLEVELISSUE']._serialized_end = 2262
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWITEMLEVELISSUE_SEVERITY']._serialized_start = 2191
    _globals['_MERCHANTREVIEWSTATUS_MERCHANTREVIEWITEMLEVELISSUE_SEVERITY']._serialized_end = 2262