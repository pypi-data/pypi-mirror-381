"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/services/bidding_strategy_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v21.resources import bidding_strategy_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_bidding__strategy__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/ads/googleads/v21/services/bidding_strategy_service.proto\x12!google.ads.googleads.v21.services\x1a:google/ads/googleads/v21/enums/response_content_type.proto\x1a9google/ads/googleads/v21/resources/bidding_strategy.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\xac\x02\n\x1eMutateBiddingStrategiesRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12T\n\noperations\x18\x02 \x03(\x0b2;.google.ads.googleads.v21.services.BiddingStrategyOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v21.enums.ResponseContentTypeEnum.ResponseContentType"\xa7\x02\n\x18BiddingStrategyOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12E\n\x06create\x18\x01 \x01(\x0b23.google.ads.googleads.v21.resources.BiddingStrategyH\x00\x12E\n\x06update\x18\x02 \x01(\x0b23.google.ads.googleads.v21.resources.BiddingStrategyH\x00\x12?\n\x06remove\x18\x03 \x01(\tB-\xfaA*\n(googleads.googleapis.com/BiddingStrategyH\x00B\x0b\n\toperation"\xa5\x01\n\x1fMutateBiddingStrategiesResponse\x121\n\x15partial_failure_error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12O\n\x07results\x18\x02 \x03(\x0b2>.google.ads.googleads.v21.services.MutateBiddingStrategyResult"\xb2\x01\n\x1bMutateBiddingStrategyResult\x12D\n\rresource_name\x18\x01 \x01(\tB-\xfaA*\n(googleads.googleapis.com/BiddingStrategy\x12M\n\x10bidding_strategy\x18\x02 \x01(\x0b23.google.ads.googleads.v21.resources.BiddingStrategy2\xdf\x02\n\x16BiddingStrategyService\x12\xfd\x01\n\x17MutateBiddingStrategies\x12A.google.ads.googleads.v21.services.MutateBiddingStrategiesRequest\x1aB.google.ads.googleads.v21.services.MutateBiddingStrategiesResponse"[\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02<"7/v21/customers/{customer_id=*}/biddingStrategies:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x87\x02\n%com.google.ads.googleads.v21.servicesB\x1bBiddingStrategyServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.services.bidding_strategy_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v21.servicesB\x1bBiddingStrategyServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Services'
    _globals['_MUTATEBIDDINGSTRATEGIESREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEBIDDINGSTRATEGIESREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEBIDDINGSTRATEGIESREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATEBIDDINGSTRATEGIESREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_BIDDINGSTRATEGYOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_BIDDINGSTRATEGYOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA*\n(googleads.googleapis.com/BiddingStrategy'
    _globals['_MUTATEBIDDINGSTRATEGYRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEBIDDINGSTRATEGYRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA*\n(googleads.googleapis.com/BiddingStrategy'
    _globals['_BIDDINGSTRATEGYSERVICE']._loaded_options = None
    _globals['_BIDDINGSTRATEGYSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_BIDDINGSTRATEGYSERVICE'].methods_by_name['MutateBiddingStrategies']._loaded_options = None
    _globals['_BIDDINGSTRATEGYSERVICE'].methods_by_name['MutateBiddingStrategies']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02<"7/v21/customers/{customer_id=*}/biddingStrategies:mutate:\x01*'
    _globals['_MUTATEBIDDINGSTRATEGIESREQUEST']._serialized_start = 397
    _globals['_MUTATEBIDDINGSTRATEGIESREQUEST']._serialized_end = 697
    _globals['_BIDDINGSTRATEGYOPERATION']._serialized_start = 700
    _globals['_BIDDINGSTRATEGYOPERATION']._serialized_end = 995
    _globals['_MUTATEBIDDINGSTRATEGIESRESPONSE']._serialized_start = 998
    _globals['_MUTATEBIDDINGSTRATEGIESRESPONSE']._serialized_end = 1163
    _globals['_MUTATEBIDDINGSTRATEGYRESULT']._serialized_start = 1166
    _globals['_MUTATEBIDDINGSTRATEGYRESULT']._serialized_end = 1344
    _globals['_BIDDINGSTRATEGYSERVICE']._serialized_start = 1347
    _globals['_BIDDINGSTRATEGYSERVICE']._serialized_end = 1698