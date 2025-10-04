"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/ad_group_ad.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.enums import ad_group_ad_engine_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_ad__group__ad__engine__status__pb2
from ......google.ads.searchads360.v0.enums import ad_group_ad_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_ad__group__ad__status__pb2
from ......google.ads.searchads360.v0.resources import ad_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_resources_dot_ad__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/ads/searchads360/v0/resources/ad_group_ad.proto\x12$google.ads.searchads360.v0.resources\x1a@google/ads/searchads360/v0/enums/ad_group_ad_engine_status.proto\x1a9google/ads/searchads360/v0/enums/ad_group_ad_status.proto\x1a-google/ads/searchads360/v0/resources/ad.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa8\x05\n\tAdGroupAd\x12D\n\rresource_name\x18\x01 \x01(\tB-\xe0A\x05\xfaA\'\n%searchads360.googleapis.com/AdGroupAd\x12U\n\x06status\x18\x03 \x01(\x0e2E.google.ads.searchads360.v0.enums.AdGroupAdStatusEnum.AdGroupAdStatus\x129\n\x02ad\x18\x05 \x01(\x0b2(.google.ads.searchads360.v0.resources.AdB\x03\xe0A\x05\x12\x1a\n\rcreation_time\x18\x0e \x01(\tB\x03\xe0A\x03\x12B\n\x06labels\x18\n \x03(\tB2\xe0A\x03\xfaA,\n*searchads360.googleapis.com/AdGroupAdLabel\x12U\n\x10effective_labels\x18\x13 \x03(\tB;\xe0A\x03\xfaA5\n3searchads360.googleapis.com/AdGroupAdEffectiveLabel\x12\x16\n\tengine_id\x18\x0b \x01(\tB\x03\xe0A\x03\x12m\n\rengine_status\x18\x0f \x01(\x0e2Q.google.ads.searchads360.v0.enums.AdGroupAdEngineStatusEnum.AdGroupAdEngineStatusB\x03\xe0A\x03\x12\x1f\n\x12last_modified_time\x18\x0c \x01(\tB\x03\xe0A\x03:d\xeaAa\n%searchads360.googleapis.com/AdGroupAd\x128customers/{customer_id}/adGroupAds/{ad_group_id}~{ad_id}B\x8e\x02\n(com.google.ads.searchads360.v0.resourcesB\x0eAdGroupAdProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.ad_group_ad_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x0eAdGroupAdProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_ADGROUPAD'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADGROUPAD'].fields_by_name['resource_name']._serialized_options = b"\xe0A\x05\xfaA'\n%searchads360.googleapis.com/AdGroupAd"
    _globals['_ADGROUPAD'].fields_by_name['ad']._loaded_options = None
    _globals['_ADGROUPAD'].fields_by_name['ad']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPAD'].fields_by_name['creation_time']._loaded_options = None
    _globals['_ADGROUPAD'].fields_by_name['creation_time']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPAD'].fields_by_name['labels']._loaded_options = None
    _globals['_ADGROUPAD'].fields_by_name['labels']._serialized_options = b'\xe0A\x03\xfaA,\n*searchads360.googleapis.com/AdGroupAdLabel'
    _globals['_ADGROUPAD'].fields_by_name['effective_labels']._loaded_options = None
    _globals['_ADGROUPAD'].fields_by_name['effective_labels']._serialized_options = b'\xe0A\x03\xfaA5\n3searchads360.googleapis.com/AdGroupAdEffectiveLabel'
    _globals['_ADGROUPAD'].fields_by_name['engine_id']._loaded_options = None
    _globals['_ADGROUPAD'].fields_by_name['engine_id']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPAD'].fields_by_name['engine_status']._loaded_options = None
    _globals['_ADGROUPAD'].fields_by_name['engine_status']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPAD'].fields_by_name['last_modified_time']._loaded_options = None
    _globals['_ADGROUPAD'].fields_by_name['last_modified_time']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPAD']._loaded_options = None
    _globals['_ADGROUPAD']._serialized_options = b'\xeaAa\n%searchads360.googleapis.com/AdGroupAd\x128customers/{customer_id}/adGroupAds/{ad_group_id}~{ad_id}'
    _globals['_ADGROUPAD']._serialized_start = 329
    _globals['_ADGROUPAD']._serialized_end = 1009