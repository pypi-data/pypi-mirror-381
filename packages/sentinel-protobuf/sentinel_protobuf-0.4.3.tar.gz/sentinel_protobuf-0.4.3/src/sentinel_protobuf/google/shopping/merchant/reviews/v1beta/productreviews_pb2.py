"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/reviews/v1beta/productreviews.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ......google.shopping.merchant.reviews.v1beta import productreviews_common_pb2 as google_dot_shopping_dot_merchant_dot_reviews_dot_v1beta_dot_productreviews__common__pb2
from ......google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/shopping/merchant/reviews/v1beta/productreviews.proto\x12\'google.shopping.merchant.reviews.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1aCgoogle/shopping/merchant/reviews/v1beta/productreviews_common.proto\x1a google/shopping/type/types.proto"Y\n\x17GetProductReviewRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(merchantapi.googleapis.com/ProductReview"\\\n\x1aDeleteProductReviewRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(merchantapi.googleapis.com/ProductReview"\x8e\x01\n\x19ListProductReviewsRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(merchantapi.googleapis.com/ProductReview\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\xa0\x01\n\x1aInsertProductReviewRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12S\n\x0eproduct_review\x18\x02 \x01(\x0b26.google.shopping.merchant.reviews.v1beta.ProductReviewB\x03\xe0A\x02\x12\x18\n\x0bdata_source\x18\x03 \x01(\tB\x03\xe0A\x02"\x86\x01\n\x1aListProductReviewsResponse\x12O\n\x0fproduct_reviews\x18\x01 \x03(\x0b26.google.shopping.merchant.reviews.v1beta.ProductReview\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xf0\x03\n\rProductReview\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1e\n\x11product_review_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12h\n\x19product_review_attributes\x18\x03 \x01(\x0b2@.google.shopping.merchant.reviews.v1beta.ProductReviewAttributesB\x03\xe0A\x01\x12E\n\x11custom_attributes\x18\x04 \x03(\x0b2%.google.shopping.type.CustomAttributeB\x03\xe0A\x01\x12\x18\n\x0bdata_source\x18\x05 \x01(\tB\x03\xe0A\x03\x12`\n\x15product_review_status\x18\x06 \x01(\x0b2<.google.shopping.merchant.reviews.v1beta.ProductReviewStatusB\x03\xe0A\x03:\x7f\xeaA|\n(merchantapi.googleapis.com/ProductReview\x121accounts/{account}/productReviews/{productreview}*\x0eproductReviews2\rproductReview2\xb7\x07\n\x15ProductReviewsService\x12\xcf\x01\n\x10GetProductReview\x12@.google.shopping.merchant.reviews.v1beta.GetProductReviewRequest\x1a6.google.shopping.merchant.reviews.v1beta.ProductReview"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/reviews/v1beta/{name=accounts/*/productReviews/*}\x12\xe2\x01\n\x12ListProductReviews\x12B.google.shopping.merchant.reviews.v1beta.ListProductReviewsRequest\x1aC.google.shopping.merchant.reviews.v1beta.ListProductReviewsResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/reviews/v1beta/{parent=accounts/*}/productReviews\x12\xe5\x01\n\x13InsertProductReview\x12C.google.shopping.merchant.reviews.v1beta.InsertProductReviewRequest\x1a6.google.shopping.merchant.reviews.v1beta.ProductReview"Q\x82\xd3\xe4\x93\x02K"9/reviews/v1beta/{parent=accounts/*}/productReviews:insert:\x0eproduct_review\x12\xb5\x01\n\x13DeleteProductReview\x12C.google.shopping.merchant.reviews.v1beta.DeleteProductReviewRequest\x1a\x16.google.protobuf.Empty"A\xdaA\x04name\x82\xd3\xe4\x93\x024*2/reviews/v1beta/{name=accounts/*/productReviews/*}\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x93\x02\n+com.google.shopping.merchant.reviews.v1betaB\x13ProductReviewsProtoP\x01ZKcloud.google.com/go/shopping/merchant/reviews/apiv1beta/reviewspb;reviewspb\xaa\x02\'Google.Shopping.Merchant.Reviews.V1Beta\xca\x02\'Google\\Shopping\\Merchant\\Reviews\\V1beta\xea\x02+Google::Shopping::Merchant::Reviews::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.reviews.v1beta.productreviews_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.shopping.merchant.reviews.v1betaB\x13ProductReviewsProtoP\x01ZKcloud.google.com/go/shopping/merchant/reviews/apiv1beta/reviewspb;reviewspb\xaa\x02'Google.Shopping.Merchant.Reviews.V1Beta\xca\x02'Google\\Shopping\\Merchant\\Reviews\\V1beta\xea\x02+Google::Shopping::Merchant::Reviews::V1beta"
    _globals['_GETPRODUCTREVIEWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPRODUCTREVIEWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(merchantapi.googleapis.com/ProductReview'
    _globals['_DELETEPRODUCTREVIEWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPRODUCTREVIEWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(merchantapi.googleapis.com/ProductReview'
    _globals['_LISTPRODUCTREVIEWSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPRODUCTREVIEWSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(merchantapi.googleapis.com/ProductReview'
    _globals['_LISTPRODUCTREVIEWSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPRODUCTREVIEWSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPRODUCTREVIEWSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPRODUCTREVIEWSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_INSERTPRODUCTREVIEWREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_INSERTPRODUCTREVIEWREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_INSERTPRODUCTREVIEWREQUEST'].fields_by_name['product_review']._loaded_options = None
    _globals['_INSERTPRODUCTREVIEWREQUEST'].fields_by_name['product_review']._serialized_options = b'\xe0A\x02'
    _globals['_INSERTPRODUCTREVIEWREQUEST'].fields_by_name['data_source']._loaded_options = None
    _globals['_INSERTPRODUCTREVIEWREQUEST'].fields_by_name['data_source']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCTREVIEW'].fields_by_name['name']._loaded_options = None
    _globals['_PRODUCTREVIEW'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_PRODUCTREVIEW'].fields_by_name['product_review_id']._loaded_options = None
    _globals['_PRODUCTREVIEW'].fields_by_name['product_review_id']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCTREVIEW'].fields_by_name['product_review_attributes']._loaded_options = None
    _globals['_PRODUCTREVIEW'].fields_by_name['product_review_attributes']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTREVIEW'].fields_by_name['custom_attributes']._loaded_options = None
    _globals['_PRODUCTREVIEW'].fields_by_name['custom_attributes']._serialized_options = b'\xe0A\x01'
    _globals['_PRODUCTREVIEW'].fields_by_name['data_source']._loaded_options = None
    _globals['_PRODUCTREVIEW'].fields_by_name['data_source']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTREVIEW'].fields_by_name['product_review_status']._loaded_options = None
    _globals['_PRODUCTREVIEW'].fields_by_name['product_review_status']._serialized_options = b'\xe0A\x03'
    _globals['_PRODUCTREVIEW']._loaded_options = None
    _globals['_PRODUCTREVIEW']._serialized_options = b'\xeaA|\n(merchantapi.googleapis.com/ProductReview\x121accounts/{account}/productReviews/{productreview}*\x0eproductReviews2\rproductReview'
    _globals['_PRODUCTREVIEWSSERVICE']._loaded_options = None
    _globals['_PRODUCTREVIEWSSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_PRODUCTREVIEWSSERVICE'].methods_by_name['GetProductReview']._loaded_options = None
    _globals['_PRODUCTREVIEWSSERVICE'].methods_by_name['GetProductReview']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/reviews/v1beta/{name=accounts/*/productReviews/*}'
    _globals['_PRODUCTREVIEWSSERVICE'].methods_by_name['ListProductReviews']._loaded_options = None
    _globals['_PRODUCTREVIEWSSERVICE'].methods_by_name['ListProductReviews']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/reviews/v1beta/{parent=accounts/*}/productReviews'
    _globals['_PRODUCTREVIEWSSERVICE'].methods_by_name['InsertProductReview']._loaded_options = None
    _globals['_PRODUCTREVIEWSSERVICE'].methods_by_name['InsertProductReview']._serialized_options = b'\x82\xd3\xe4\x93\x02K"9/reviews/v1beta/{parent=accounts/*}/productReviews:insert:\x0eproduct_review'
    _globals['_PRODUCTREVIEWSSERVICE'].methods_by_name['DeleteProductReview']._loaded_options = None
    _globals['_PRODUCTREVIEWSSERVICE'].methods_by_name['DeleteProductReview']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024*2/reviews/v1beta/{name=accounts/*/productReviews/*}'
    _globals['_GETPRODUCTREVIEWREQUEST']._serialized_start = 352
    _globals['_GETPRODUCTREVIEWREQUEST']._serialized_end = 441
    _globals['_DELETEPRODUCTREVIEWREQUEST']._serialized_start = 443
    _globals['_DELETEPRODUCTREVIEWREQUEST']._serialized_end = 535
    _globals['_LISTPRODUCTREVIEWSREQUEST']._serialized_start = 538
    _globals['_LISTPRODUCTREVIEWSREQUEST']._serialized_end = 680
    _globals['_INSERTPRODUCTREVIEWREQUEST']._serialized_start = 683
    _globals['_INSERTPRODUCTREVIEWREQUEST']._serialized_end = 843
    _globals['_LISTPRODUCTREVIEWSRESPONSE']._serialized_start = 846
    _globals['_LISTPRODUCTREVIEWSRESPONSE']._serialized_end = 980
    _globals['_PRODUCTREVIEW']._serialized_start = 983
    _globals['_PRODUCTREVIEW']._serialized_end = 1479
    _globals['_PRODUCTREVIEWSSERVICE']._serialized_start = 1482
    _globals['_PRODUCTREVIEWSSERVICE']._serialized_end = 2433