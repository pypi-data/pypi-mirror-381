"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/ad_group.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.common import targeting_setting_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_common_dot_targeting__setting__pb2
from ......google.ads.searchads360.v0.enums import ad_group_ad_rotation_mode_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_ad__group__ad__rotation__mode__pb2
from ......google.ads.searchads360.v0.enums import ad_group_engine_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_ad__group__engine__status__pb2
from ......google.ads.searchads360.v0.enums import ad_group_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_ad__group__status__pb2
from ......google.ads.searchads360.v0.enums import ad_group_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_ad__group__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/ads/searchads360/v0/resources/ad_group.proto\x12$google.ads.searchads360.v0.resources\x1a9google/ads/searchads360/v0/common/targeting_setting.proto\x1a@google/ads/searchads360/v0/enums/ad_group_ad_rotation_mode.proto\x1a=google/ads/searchads360/v0/enums/ad_group_engine_status.proto\x1a6google/ads/searchads360/v0/enums/ad_group_status.proto\x1a4google/ads/searchads360/v0/enums/ad_group_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xac\x08\n\x07AdGroup\x12B\n\rresource_name\x18\x01 \x01(\tB+\xe0A\x05\xfaA%\n#searchads360.googleapis.com/AdGroup\x12\x14\n\x02id\x18" \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x11\n\x04name\x18# \x01(\tH\x01\x88\x01\x01\x12Q\n\x06status\x18\x05 \x01(\x0e2A.google.ads.searchads360.v0.enums.AdGroupStatusEnum.AdGroupStatus\x12P\n\x04type\x18\x0c \x01(\x0e2=.google.ads.searchads360.v0.enums.AdGroupTypeEnum.AdGroupTypeB\x03\xe0A\x05\x12k\n\x10ad_rotation_mode\x18\x16 \x01(\x0e2Q.google.ads.searchads360.v0.enums.AdGroupAdRotationModeEnum.AdGroupAdRotationMode\x12\x1b\n\x0ecpc_bid_micros\x18\' \x01(\x03H\x02\x88\x01\x01\x12\x1a\n\rcreation_time\x18< \x01(\tB\x03\xe0A\x03\x12n\n\rengine_status\x18= \x01(\x0e2M.google.ads.searchads360.v0.enums.AdGroupEngineStatusEnum.AdGroupEngineStatusB\x03\xe0A\x03H\x03\x88\x01\x01\x12N\n\x11targeting_setting\x18\x19 \x01(\x0b23.google.ads.searchads360.v0.common.TargetingSetting\x12@\n\x06labels\x181 \x03(\tB0\xe0A\x03\xfaA*\n(searchads360.googleapis.com/AdGroupLabel\x12S\n\x10effective_labels\x18B \x03(\tB9\xe0A\x03\xfaA3\n1searchads360.googleapis.com/AdGroupEffectiveLabel\x12\x16\n\tengine_id\x182 \x01(\tB\x03\xe0A\x03\x12\x17\n\nstart_date\x183 \x01(\tB\x03\xe0A\x03\x12\x15\n\x08end_date\x184 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rlanguage_code\x185 \x01(\tB\x03\xe0A\x03\x12\x1f\n\x12last_modified_time\x187 \x01(\tB\x03\xe0A\x03:X\xeaAU\n#searchads360.googleapis.com/AdGroup\x12.customers/{customer_id}/adGroups/{ad_group_id}B\x05\n\x03_idB\x07\n\x05_nameB\x11\n\x0f_cpc_bid_microsB\x10\n\x0e_engine_statusB\x8c\x02\n(com.google.ads.searchads360.v0.resourcesB\x0cAdGroupProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.ad_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x0cAdGroupProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_ADGROUP'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA%\n#searchads360.googleapis.com/AdGroup'
    _globals['_ADGROUP'].fields_by_name['id']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUP'].fields_by_name['type']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['type']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUP'].fields_by_name['creation_time']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['creation_time']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUP'].fields_by_name['engine_status']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['engine_status']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUP'].fields_by_name['labels']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['labels']._serialized_options = b'\xe0A\x03\xfaA*\n(searchads360.googleapis.com/AdGroupLabel'
    _globals['_ADGROUP'].fields_by_name['effective_labels']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['effective_labels']._serialized_options = b'\xe0A\x03\xfaA3\n1searchads360.googleapis.com/AdGroupEffectiveLabel'
    _globals['_ADGROUP'].fields_by_name['engine_id']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['engine_id']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUP'].fields_by_name['start_date']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['start_date']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUP'].fields_by_name['end_date']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['end_date']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUP'].fields_by_name['language_code']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['language_code']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUP'].fields_by_name['last_modified_time']._loaded_options = None
    _globals['_ADGROUP'].fields_by_name['last_modified_time']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUP']._loaded_options = None
    _globals['_ADGROUP']._serialized_options = b'\xeaAU\n#searchads360.googleapis.com/AdGroup\x12.customers/{customer_id}/adGroups/{ad_group_id}'
    _globals['_ADGROUP']._serialized_start = 452
    _globals['_ADGROUP']._serialized_end = 1520