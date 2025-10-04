"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/reviews/v1beta/merchantreviews.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ......google.shopping.merchant.reviews.v1beta import merchantreviews_common_pb2 as google_dot_shopping_dot_merchant_dot_reviews_dot_v1beta_dot_merchantreviews__common__pb2
from ......google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/shopping/merchant/reviews/v1beta/merchantreviews.proto\x12\'google.shopping.merchant.reviews.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1aDgoogle/shopping/merchant/reviews/v1beta/merchantreviews_common.proto\x1a google/shopping/type/types.proto"[\n\x18GetMerchantReviewRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/MerchantReview"^\n\x1bDeleteMerchantReviewRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/MerchantReview"\x90\x01\n\x1aListMerchantReviewsRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\x12)merchantapi.googleapis.com/MerchantReview\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\xa3\x01\n\x1bInsertMerchantReviewRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12U\n\x0fmerchant_review\x18\x02 \x01(\x0b27.google.shopping.merchant.reviews.v1beta.MerchantReviewB\x03\xe0A\x02\x12\x18\n\x0bdata_source\x18\x03 \x01(\tB\x03\xe0A\x02"\x89\x01\n\x1bListMerchantReviewsResponse\x12Q\n\x10merchant_reviews\x18\x01 \x03(\x0b27.google.shopping.merchant.reviews.v1beta.MerchantReview\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xf1\x03\n\x0eMerchantReview\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1f\n\x12merchant_review_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12j\n\x1amerchant_review_attributes\x18\x03 \x01(\x0b2A.google.shopping.merchant.reviews.v1beta.MerchantReviewAttributesB\x03\xe0A\x01\x12E\n\x11custom_attributes\x18\x04 \x03(\x0b2%.google.shopping.type.CustomAttributeB\x03\xe0A\x01\x12\x18\n\x0bdata_source\x18\x05 \x01(\tB\x03\xe0A\x03\x12b\n\x16merchant_review_status\x18\x06 \x01(\x0b2=.google.shopping.merchant.reviews.v1beta.MerchantReviewStatusB\x03\xe0A\x03:z\xeaAw\n)merchantapi.googleapis.com/MerchantReview\x12)accounts/{account}/merchantReviews/{name}*\x0fmerchantReviews2\x0emerchantReview2\xc8\x07\n\x16MerchantReviewsService\x12\xd3\x01\n\x11GetMerchantReview\x12A.google.shopping.merchant.reviews.v1beta.GetMerchantReviewRequest\x1a7.google.shopping.merchant.reviews.v1beta.MerchantReview"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/reviews/v1beta/{name=accounts/*/merchantReviews/*}\x12\xe6\x01\n\x13ListMerchantReviews\x12C.google.shopping.merchant.reviews.v1beta.ListMerchantReviewsRequest\x1aD.google.shopping.merchant.reviews.v1beta.ListMerchantReviewsResponse"D\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/reviews/v1beta/{parent=accounts/*}/merchantReviews\x12\xea\x01\n\x14InsertMerchantReview\x12D.google.shopping.merchant.reviews.v1beta.InsertMerchantReviewRequest\x1a7.google.shopping.merchant.reviews.v1beta.MerchantReview"S\x82\xd3\xe4\x93\x02M":/reviews/v1beta/{parent=accounts/*}/merchantReviews:insert:\x0fmerchant_review\x12\xb8\x01\n\x14DeleteMerchantReview\x12D.google.shopping.merchant.reviews.v1beta.DeleteMerchantReviewRequest\x1a\x16.google.protobuf.Empty"B\xdaA\x04name\x82\xd3\xe4\x93\x025*3/reviews/v1beta/{name=accounts/*/merchantReviews/*}\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xcf\x02\n+com.google.shopping.merchant.reviews.v1betaB\x14MerchantReviewsProtoP\x01ZKcloud.google.com/go/shopping/merchant/reviews/apiv1beta/reviewspb;reviewspb\xaa\x02\'Google.Shopping.Merchant.Reviews.V1Beta\xca\x02\'Google\\Shopping\\Merchant\\Reviews\\V1beta\xea\x02+Google::Shopping::Merchant::Reviews::V1beta\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.reviews.v1beta.merchantreviews_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n+com.google.shopping.merchant.reviews.v1betaB\x14MerchantReviewsProtoP\x01ZKcloud.google.com/go/shopping/merchant/reviews/apiv1beta/reviewspb;reviewspb\xaa\x02\'Google.Shopping.Merchant.Reviews.V1Beta\xca\x02\'Google\\Shopping\\Merchant\\Reviews\\V1beta\xea\x02+Google::Shopping::Merchant::Reviews::V1beta\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}'
    _globals['_GETMERCHANTREVIEWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMERCHANTREVIEWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/MerchantReview'
    _globals['_DELETEMERCHANTREVIEWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEMERCHANTREVIEWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)merchantapi.googleapis.com/MerchantReview'
    _globals['_LISTMERCHANTREVIEWSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMERCHANTREVIEWSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\x12)merchantapi.googleapis.com/MerchantReview'
    _globals['_LISTMERCHANTREVIEWSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTMERCHANTREVIEWSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMERCHANTREVIEWSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTMERCHANTREVIEWSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_INSERTMERCHANTREVIEWREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_INSERTMERCHANTREVIEWREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_INSERTMERCHANTREVIEWREQUEST'].fields_by_name['merchant_review']._loaded_options = None
    _globals['_INSERTMERCHANTREVIEWREQUEST'].fields_by_name['merchant_review']._serialized_options = b'\xe0A\x02'
    _globals['_INSERTMERCHANTREVIEWREQUEST'].fields_by_name['data_source']._loaded_options = None
    _globals['_INSERTMERCHANTREVIEWREQUEST'].fields_by_name['data_source']._serialized_options = b'\xe0A\x02'
    _globals['_MERCHANTREVIEW'].fields_by_name['name']._loaded_options = None
    _globals['_MERCHANTREVIEW'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_MERCHANTREVIEW'].fields_by_name['merchant_review_id']._loaded_options = None
    _globals['_MERCHANTREVIEW'].fields_by_name['merchant_review_id']._serialized_options = b'\xe0A\x02'
    _globals['_MERCHANTREVIEW'].fields_by_name['merchant_review_attributes']._loaded_options = None
    _globals['_MERCHANTREVIEW'].fields_by_name['merchant_review_attributes']._serialized_options = b'\xe0A\x01'
    _globals['_MERCHANTREVIEW'].fields_by_name['custom_attributes']._loaded_options = None
    _globals['_MERCHANTREVIEW'].fields_by_name['custom_attributes']._serialized_options = b'\xe0A\x01'
    _globals['_MERCHANTREVIEW'].fields_by_name['data_source']._loaded_options = None
    _globals['_MERCHANTREVIEW'].fields_by_name['data_source']._serialized_options = b'\xe0A\x03'
    _globals['_MERCHANTREVIEW'].fields_by_name['merchant_review_status']._loaded_options = None
    _globals['_MERCHANTREVIEW'].fields_by_name['merchant_review_status']._serialized_options = b'\xe0A\x03'
    _globals['_MERCHANTREVIEW']._loaded_options = None
    _globals['_MERCHANTREVIEW']._serialized_options = b'\xeaAw\n)merchantapi.googleapis.com/MerchantReview\x12)accounts/{account}/merchantReviews/{name}*\x0fmerchantReviews2\x0emerchantReview'
    _globals['_MERCHANTREVIEWSSERVICE']._loaded_options = None
    _globals['_MERCHANTREVIEWSSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_MERCHANTREVIEWSSERVICE'].methods_by_name['GetMerchantReview']._loaded_options = None
    _globals['_MERCHANTREVIEWSSERVICE'].methods_by_name['GetMerchantReview']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/reviews/v1beta/{name=accounts/*/merchantReviews/*}'
    _globals['_MERCHANTREVIEWSSERVICE'].methods_by_name['ListMerchantReviews']._loaded_options = None
    _globals['_MERCHANTREVIEWSSERVICE'].methods_by_name['ListMerchantReviews']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/reviews/v1beta/{parent=accounts/*}/merchantReviews'
    _globals['_MERCHANTREVIEWSSERVICE'].methods_by_name['InsertMerchantReview']._loaded_options = None
    _globals['_MERCHANTREVIEWSSERVICE'].methods_by_name['InsertMerchantReview']._serialized_options = b'\x82\xd3\xe4\x93\x02M":/reviews/v1beta/{parent=accounts/*}/merchantReviews:insert:\x0fmerchant_review'
    _globals['_MERCHANTREVIEWSSERVICE'].methods_by_name['DeleteMerchantReview']._loaded_options = None
    _globals['_MERCHANTREVIEWSSERVICE'].methods_by_name['DeleteMerchantReview']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025*3/reviews/v1beta/{name=accounts/*/merchantReviews/*}'
    _globals['_GETMERCHANTREVIEWREQUEST']._serialized_start = 354
    _globals['_GETMERCHANTREVIEWREQUEST']._serialized_end = 445
    _globals['_DELETEMERCHANTREVIEWREQUEST']._serialized_start = 447
    _globals['_DELETEMERCHANTREVIEWREQUEST']._serialized_end = 541
    _globals['_LISTMERCHANTREVIEWSREQUEST']._serialized_start = 544
    _globals['_LISTMERCHANTREVIEWSREQUEST']._serialized_end = 688
    _globals['_INSERTMERCHANTREVIEWREQUEST']._serialized_start = 691
    _globals['_INSERTMERCHANTREVIEWREQUEST']._serialized_end = 854
    _globals['_LISTMERCHANTREVIEWSRESPONSE']._serialized_start = 857
    _globals['_LISTMERCHANTREVIEWSRESPONSE']._serialized_end = 994
    _globals['_MERCHANTREVIEW']._serialized_start = 997
    _globals['_MERCHANTREVIEW']._serialized_end = 1494
    _globals['_MERCHANTREVIEWSSERVICE']._serialized_start = 1497
    _globals['_MERCHANTREVIEWSSERVICE']._serialized_end = 2465