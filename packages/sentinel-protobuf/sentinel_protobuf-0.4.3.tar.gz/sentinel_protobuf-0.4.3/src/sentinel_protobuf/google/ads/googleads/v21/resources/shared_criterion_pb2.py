"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/shared_criterion.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.common import criteria_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_criteria__pb2
from ......google.ads.googleads.v21.enums import criterion_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_criterion__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/ads/googleads/v21/resources/shared_criterion.proto\x12"google.ads.googleads.v21.resources\x1a.google/ads/googleads/v21/common/criteria.proto\x1a3google/ads/googleads/v21/enums/criterion_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xab\x08\n\x0fSharedCriterion\x12G\n\rresource_name\x18\x01 \x01(\tB0\xe0A\x05\xfaA*\n(googleads.googleapis.com/SharedCriterion\x12C\n\nshared_set\x18\n \x01(\tB*\xe0A\x05\xfaA$\n"googleads.googleapis.com/SharedSetH\x01\x88\x01\x01\x12\x1e\n\x0ccriterion_id\x18\x0b \x01(\x03B\x03\xe0A\x03H\x02\x88\x01\x01\x12R\n\x04type\x18\x04 \x01(\x0e2?.google.ads.googleads.v21.enums.CriterionTypeEnum.CriterionTypeB\x03\xe0A\x03\x12D\n\x07keyword\x18\x03 \x01(\x0b2,.google.ads.googleads.v21.common.KeywordInfoB\x03\xe0A\x05H\x00\x12O\n\ryoutube_video\x18\x05 \x01(\x0b21.google.ads.googleads.v21.common.YouTubeVideoInfoB\x03\xe0A\x05H\x00\x12S\n\x0fyoutube_channel\x18\x06 \x01(\x0b23.google.ads.googleads.v21.common.YouTubeChannelInfoB\x03\xe0A\x05H\x00\x12H\n\tplacement\x18\x07 \x01(\x0b2..google.ads.googleads.v21.common.PlacementInfoB\x03\xe0A\x05H\x00\x12Z\n\x13mobile_app_category\x18\x08 \x01(\x0b26.google.ads.googleads.v21.common.MobileAppCategoryInfoB\x03\xe0A\x05H\x00\x12Y\n\x12mobile_application\x18\t \x01(\x0b26.google.ads.googleads.v21.common.MobileApplicationInfoB\x03\xe0A\x05H\x00\x12@\n\x05brand\x18\x0c \x01(\x0b2*.google.ads.googleads.v21.common.BrandInfoB\x03\xe0A\x05H\x00\x12D\n\x07webpage\x18\r \x01(\x0b2,.google.ads.googleads.v21.common.WebpageInfoB\x03\xe0A\x05H\x00:t\xeaAq\n(googleads.googleapis.com/SharedCriterion\x12Ecustomers/{customer_id}/sharedCriteria/{shared_set_id}~{criterion_id}B\x0b\n\tcriterionB\r\n\x0b_shared_setB\x0f\n\r_criterion_idB\x86\x02\n&com.google.ads.googleads.v21.resourcesB\x14SharedCriterionProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.shared_criterion_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\x14SharedCriterionProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_SHAREDCRITERION'].fields_by_name['resource_name']._loaded_options = None
    _globals['_SHAREDCRITERION'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA*\n(googleads.googleapis.com/SharedCriterion'
    _globals['_SHAREDCRITERION'].fields_by_name['shared_set']._loaded_options = None
    _globals['_SHAREDCRITERION'].fields_by_name['shared_set']._serialized_options = b'\xe0A\x05\xfaA$\n"googleads.googleapis.com/SharedSet'
    _globals['_SHAREDCRITERION'].fields_by_name['criterion_id']._loaded_options = None
    _globals['_SHAREDCRITERION'].fields_by_name['criterion_id']._serialized_options = b'\xe0A\x03'
    _globals['_SHAREDCRITERION'].fields_by_name['type']._loaded_options = None
    _globals['_SHAREDCRITERION'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_SHAREDCRITERION'].fields_by_name['keyword']._loaded_options = None
    _globals['_SHAREDCRITERION'].fields_by_name['keyword']._serialized_options = b'\xe0A\x05'
    _globals['_SHAREDCRITERION'].fields_by_name['youtube_video']._loaded_options = None
    _globals['_SHAREDCRITERION'].fields_by_name['youtube_video']._serialized_options = b'\xe0A\x05'
    _globals['_SHAREDCRITERION'].fields_by_name['youtube_channel']._loaded_options = None
    _globals['_SHAREDCRITERION'].fields_by_name['youtube_channel']._serialized_options = b'\xe0A\x05'
    _globals['_SHAREDCRITERION'].fields_by_name['placement']._loaded_options = None
    _globals['_SHAREDCRITERION'].fields_by_name['placement']._serialized_options = b'\xe0A\x05'
    _globals['_SHAREDCRITERION'].fields_by_name['mobile_app_category']._loaded_options = None
    _globals['_SHAREDCRITERION'].fields_by_name['mobile_app_category']._serialized_options = b'\xe0A\x05'
    _globals['_SHAREDCRITERION'].fields_by_name['mobile_application']._loaded_options = None
    _globals['_SHAREDCRITERION'].fields_by_name['mobile_application']._serialized_options = b'\xe0A\x05'
    _globals['_SHAREDCRITERION'].fields_by_name['brand']._loaded_options = None
    _globals['_SHAREDCRITERION'].fields_by_name['brand']._serialized_options = b'\xe0A\x05'
    _globals['_SHAREDCRITERION'].fields_by_name['webpage']._loaded_options = None
    _globals['_SHAREDCRITERION'].fields_by_name['webpage']._serialized_options = b'\xe0A\x05'
    _globals['_SHAREDCRITERION']._loaded_options = None
    _globals['_SHAREDCRITERION']._serialized_options = b'\xeaAq\n(googleads.googleapis.com/SharedCriterion\x12Ecustomers/{customer_id}/sharedCriteria/{shared_set_id}~{criterion_id}'
    _globals['_SHAREDCRITERION']._serialized_start = 259
    _globals['_SHAREDCRITERION']._serialized_end = 1326