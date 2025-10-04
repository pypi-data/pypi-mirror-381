"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/admanager/v1/targeting.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import request_platform_enum_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_request__platform__enum__pb2
from .....google.ads.admanager.v1 import targeted_video_bumper_type_enum_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_targeted__video__bumper__type__enum__pb2
from .....google.ads.admanager.v1 import video_position_enum_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_video__position__enum__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/ads/admanager/v1/targeting.proto\x12\x17google.ads.admanager.v1\x1a3google/ads/admanager/v1/request_platform_enum.proto\x1a=google/ads/admanager/v1/targeted_video_bumper_type_enum.proto\x1a1google/ads/admanager/v1/video_position_enum.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x91\x05\n\tTargeting\x12A\n\rgeo_targeting\x18\x02 \x01(\x0b2%.google.ads.admanager.v1.GeoTargetingB\x03\xe0A\x01\x12O\n\x14technology_targeting\x18\x03 \x01(\x0b2,.google.ads.admanager.v1.TechnologyTargetingB\x03\xe0A\x01\x12M\n\x13inventory_targeting\x18\x05 \x01(\x0b2+.google.ads.admanager.v1.InventoryTargetingB\x03\xe0A\x01\x12Z\n\x1arequest_platform_targeting\x18\x06 \x01(\x0b21.google.ads.admanager.v1.RequestPlatformTargetingB\x03\xe0A\x01\x12G\n\x10custom_targeting\x18\x07 \x01(\x0b2(.google.ads.admanager.v1.CustomTargetingB\x03\xe0A\x01\x12P\n\x15user_domain_targeting\x18\n \x01(\x0b2,.google.ads.admanager.v1.UserDomainTargetingB\x03\xe0A\x01\x12V\n\x18video_position_targeting\x18\x0c \x01(\x0b2/.google.ads.admanager.v1.VideoPositionTargetingB\x03\xe0A\x01\x12R\n\x16data_segment_targeting\x18\r \x01(\x0b2-.google.ads.admanager.v1.DataSegmentTargetingB\x03\xe0A\x01"\x94\x01\n\x0cGeoTargeting\x12A\n\rtargeted_geos\x18\x03 \x03(\tB*\xe0A\x01\xfaA$\n"admanager.googleapis.com/GeoTarget\x12A\n\rexcluded_geos\x18\x04 \x03(\tB*\xe0A\x01\xfaA$\n"admanager.googleapis.com/GeoTarget"\x9a\x02\n\x13TechnologyTargeting\x12M\n\x13bandwidth_targeting\x18\x03 \x01(\x0b2+.google.ads.admanager.v1.BandwidthTargetingB\x03\xe0A\x01\x12X\n\x19device_category_targeting\x18\x01 \x01(\x0b20.google.ads.admanager.v1.DeviceCategoryTargetingB\x03\xe0A\x01\x12Z\n\x1aoperating_system_targeting\x18\x02 \x01(\x0b21.google.ads.admanager.v1.OperatingSystemTargetingB\x03\xe0A\x01"\xbc\x01\n\x12BandwidthTargeting\x12R\n\x19targeted_bandwidth_groups\x18\x03 \x03(\tB/\xe0A\x01\xfaA)\n\'admanager.googleapis.com/BandwidthGroup\x12R\n\x19excluded_bandwidth_groups\x18\x04 \x03(\tB/\xe0A\x01\xfaA)\n\'admanager.googleapis.com/BandwidthGroup"\xb5\x01\n\x17DeviceCategoryTargeting\x12L\n\x13targeted_categories\x18\x03 \x03(\tB/\xe0A\x01\xfaA)\n\'admanager.googleapis.com/DeviceCategory\x12L\n\x13excluded_categories\x18\x04 \x03(\tB/\xe0A\x01\xfaA)\n\'admanager.googleapis.com/DeviceCategory"\x90\x03\n\x18OperatingSystemTargeting\x12T\n\x1atargeted_operating_systems\x18\x05 \x03(\tB0\xe0A\x01\xfaA*\n(admanager.googleapis.com/OperatingSystem\x12T\n\x1aexcluded_operating_systems\x18\x06 \x03(\tB0\xe0A\x01\xfaA*\n(admanager.googleapis.com/OperatingSystem\x12c\n"targeted_operating_system_versions\x18\x07 \x03(\tB7\xe0A\x01\xfaA1\n/admanager.googleapis.com/OperatingSystemVersion\x12c\n"excluded_operating_system_versions\x18\x08 \x03(\tB7\xe0A\x01\xfaA1\n/admanager.googleapis.com/OperatingSystemVersion"\xf1\x01\n\x12InventoryTargeting\x12H\n\x11targeted_ad_units\x18\x01 \x03(\x0b2(.google.ads.admanager.v1.AdUnitTargetingB\x03\xe0A\x01\x12H\n\x11excluded_ad_units\x18\x02 \x03(\x0b2(.google.ads.admanager.v1.AdUnitTargetingB\x03\xe0A\x01\x12G\n\x13targeted_placements\x18\x05 \x03(\tB*\xe0A\x01\xfaA$\n"admanager.googleapis.com/Placement"\x96\x01\n\x0fAdUnitTargeting\x12 \n\x13include_descendants\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12=\n\x07ad_unit\x18\x03 \x01(\tB\'\xe0A\x01\xfaA!\n\x1fadmanager.googleapis.com/AdUnitH\x01\x88\x01\x01B\x16\n\x14_include_descendantsB\n\n\x08_ad_unit"x\n\x18RequestPlatformTargeting\x12\\\n\x11request_platforms\x18\x01 \x03(\x0e2<.google.ads.admanager.v1.RequestPlatformEnum.RequestPlatformB\x03\xe0A\x01"h\n\x0fCustomTargeting\x12U\n\x18custom_targeting_clauses\x18\x01 \x03(\x0b2..google.ads.admanager.v1.CustomTargetingClauseB\x03\xe0A\x01"p\n\x15CustomTargetingClause\x12W\n\x19custom_targeting_literals\x18\x01 \x03(\x0b2/.google.ads.admanager.v1.CustomTargetingLiteralB\x03\xe0A\x01"\x85\x02\n\x16CustomTargetingLiteral\x12\x15\n\x08negative\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12V\n\x14custom_targeting_key\x18\x04 \x01(\tB3\xe0A\x01\xfaA-\n+admanager.googleapis.com/CustomTargetingKeyH\x01\x88\x01\x01\x12V\n\x17custom_targeting_values\x18\x05 \x03(\tB5\xe0A\x01\xfaA/\n-admanager.googleapis.com/CustomTargetingValueB\x0b\n\t_negativeB\x17\n\x15_custom_targeting_key"]\n\x13UserDomainTargeting\x12"\n\x15targeted_user_domains\x18\x01 \x03(\tB\x03\xe0A\x01\x12"\n\x15excluded_user_domains\x18\x02 \x03(\tB\x03\xe0A\x01"^\n\x16VideoPositionTargeting\x12D\n\x0fvideo_positions\x18\x01 \x03(\x0b2&.google.ads.admanager.v1.VideoPositionB\x03\xe0A\x01"\xa0\x03\n\rVideoPosition\x12\x1f\n\rmidroll_index\x18\x01 \x01(\x03B\x03\xe0A\x01H\x00\x88\x01\x01\x12\'\n\x15reverse_midroll_index\x18\x02 \x01(\x03B\x03\xe0A\x01H\x01\x88\x01\x01\x12\x1e\n\x0cpod_position\x18\x03 \x01(\x03B\x03\xe0A\x01H\x02\x88\x01\x01\x12Y\n\rposition_type\x18\x05 \x01(\x0e28.google.ads.admanager.v1.VideoPositionEnum.VideoPositionB\x03\xe0A\x01H\x03\x88\x01\x01\x12k\n\x0bbumper_type\x18\x06 \x01(\x0e2L.google.ads.admanager.v1.TargetedVideoBumperTypeEnum.TargetedVideoBumperTypeB\x03\xe0A\x01H\x04\x88\x01\x01B\x10\n\x0e_midroll_indexB\x18\n\x16_reverse_midroll_indexB\x0f\n\r_pod_positionB\x10\n\x0e_position_typeB\x0e\n\x0c_bumper_type"?\n\x14DataSegmentTargeting\x12\'\n\x1ahas_data_segment_targeting\x18\x02 \x01(\x08B\x03\xe0A\x03B\xc2\x01\n\x1bcom.google.ads.admanager.v1B\x0eTargetingProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.targeting_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x0eTargetingProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_TARGETING'].fields_by_name['geo_targeting']._loaded_options = None
    _globals['_TARGETING'].fields_by_name['geo_targeting']._serialized_options = b'\xe0A\x01'
    _globals['_TARGETING'].fields_by_name['technology_targeting']._loaded_options = None
    _globals['_TARGETING'].fields_by_name['technology_targeting']._serialized_options = b'\xe0A\x01'
    _globals['_TARGETING'].fields_by_name['inventory_targeting']._loaded_options = None
    _globals['_TARGETING'].fields_by_name['inventory_targeting']._serialized_options = b'\xe0A\x01'
    _globals['_TARGETING'].fields_by_name['request_platform_targeting']._loaded_options = None
    _globals['_TARGETING'].fields_by_name['request_platform_targeting']._serialized_options = b'\xe0A\x01'
    _globals['_TARGETING'].fields_by_name['custom_targeting']._loaded_options = None
    _globals['_TARGETING'].fields_by_name['custom_targeting']._serialized_options = b'\xe0A\x01'
    _globals['_TARGETING'].fields_by_name['user_domain_targeting']._loaded_options = None
    _globals['_TARGETING'].fields_by_name['user_domain_targeting']._serialized_options = b'\xe0A\x01'
    _globals['_TARGETING'].fields_by_name['video_position_targeting']._loaded_options = None
    _globals['_TARGETING'].fields_by_name['video_position_targeting']._serialized_options = b'\xe0A\x01'
    _globals['_TARGETING'].fields_by_name['data_segment_targeting']._loaded_options = None
    _globals['_TARGETING'].fields_by_name['data_segment_targeting']._serialized_options = b'\xe0A\x01'
    _globals['_GEOTARGETING'].fields_by_name['targeted_geos']._loaded_options = None
    _globals['_GEOTARGETING'].fields_by_name['targeted_geos']._serialized_options = b'\xe0A\x01\xfaA$\n"admanager.googleapis.com/GeoTarget'
    _globals['_GEOTARGETING'].fields_by_name['excluded_geos']._loaded_options = None
    _globals['_GEOTARGETING'].fields_by_name['excluded_geos']._serialized_options = b'\xe0A\x01\xfaA$\n"admanager.googleapis.com/GeoTarget'
    _globals['_TECHNOLOGYTARGETING'].fields_by_name['bandwidth_targeting']._loaded_options = None
    _globals['_TECHNOLOGYTARGETING'].fields_by_name['bandwidth_targeting']._serialized_options = b'\xe0A\x01'
    _globals['_TECHNOLOGYTARGETING'].fields_by_name['device_category_targeting']._loaded_options = None
    _globals['_TECHNOLOGYTARGETING'].fields_by_name['device_category_targeting']._serialized_options = b'\xe0A\x01'
    _globals['_TECHNOLOGYTARGETING'].fields_by_name['operating_system_targeting']._loaded_options = None
    _globals['_TECHNOLOGYTARGETING'].fields_by_name['operating_system_targeting']._serialized_options = b'\xe0A\x01'
    _globals['_BANDWIDTHTARGETING'].fields_by_name['targeted_bandwidth_groups']._loaded_options = None
    _globals['_BANDWIDTHTARGETING'].fields_by_name['targeted_bandwidth_groups']._serialized_options = b"\xe0A\x01\xfaA)\n'admanager.googleapis.com/BandwidthGroup"
    _globals['_BANDWIDTHTARGETING'].fields_by_name['excluded_bandwidth_groups']._loaded_options = None
    _globals['_BANDWIDTHTARGETING'].fields_by_name['excluded_bandwidth_groups']._serialized_options = b"\xe0A\x01\xfaA)\n'admanager.googleapis.com/BandwidthGroup"
    _globals['_DEVICECATEGORYTARGETING'].fields_by_name['targeted_categories']._loaded_options = None
    _globals['_DEVICECATEGORYTARGETING'].fields_by_name['targeted_categories']._serialized_options = b"\xe0A\x01\xfaA)\n'admanager.googleapis.com/DeviceCategory"
    _globals['_DEVICECATEGORYTARGETING'].fields_by_name['excluded_categories']._loaded_options = None
    _globals['_DEVICECATEGORYTARGETING'].fields_by_name['excluded_categories']._serialized_options = b"\xe0A\x01\xfaA)\n'admanager.googleapis.com/DeviceCategory"
    _globals['_OPERATINGSYSTEMTARGETING'].fields_by_name['targeted_operating_systems']._loaded_options = None
    _globals['_OPERATINGSYSTEMTARGETING'].fields_by_name['targeted_operating_systems']._serialized_options = b'\xe0A\x01\xfaA*\n(admanager.googleapis.com/OperatingSystem'
    _globals['_OPERATINGSYSTEMTARGETING'].fields_by_name['excluded_operating_systems']._loaded_options = None
    _globals['_OPERATINGSYSTEMTARGETING'].fields_by_name['excluded_operating_systems']._serialized_options = b'\xe0A\x01\xfaA*\n(admanager.googleapis.com/OperatingSystem'
    _globals['_OPERATINGSYSTEMTARGETING'].fields_by_name['targeted_operating_system_versions']._loaded_options = None
    _globals['_OPERATINGSYSTEMTARGETING'].fields_by_name['targeted_operating_system_versions']._serialized_options = b'\xe0A\x01\xfaA1\n/admanager.googleapis.com/OperatingSystemVersion'
    _globals['_OPERATINGSYSTEMTARGETING'].fields_by_name['excluded_operating_system_versions']._loaded_options = None
    _globals['_OPERATINGSYSTEMTARGETING'].fields_by_name['excluded_operating_system_versions']._serialized_options = b'\xe0A\x01\xfaA1\n/admanager.googleapis.com/OperatingSystemVersion'
    _globals['_INVENTORYTARGETING'].fields_by_name['targeted_ad_units']._loaded_options = None
    _globals['_INVENTORYTARGETING'].fields_by_name['targeted_ad_units']._serialized_options = b'\xe0A\x01'
    _globals['_INVENTORYTARGETING'].fields_by_name['excluded_ad_units']._loaded_options = None
    _globals['_INVENTORYTARGETING'].fields_by_name['excluded_ad_units']._serialized_options = b'\xe0A\x01'
    _globals['_INVENTORYTARGETING'].fields_by_name['targeted_placements']._loaded_options = None
    _globals['_INVENTORYTARGETING'].fields_by_name['targeted_placements']._serialized_options = b'\xe0A\x01\xfaA$\n"admanager.googleapis.com/Placement'
    _globals['_ADUNITTARGETING'].fields_by_name['ad_unit']._loaded_options = None
    _globals['_ADUNITTARGETING'].fields_by_name['ad_unit']._serialized_options = b'\xe0A\x01\xfaA!\n\x1fadmanager.googleapis.com/AdUnit'
    _globals['_REQUESTPLATFORMTARGETING'].fields_by_name['request_platforms']._loaded_options = None
    _globals['_REQUESTPLATFORMTARGETING'].fields_by_name['request_platforms']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMTARGETING'].fields_by_name['custom_targeting_clauses']._loaded_options = None
    _globals['_CUSTOMTARGETING'].fields_by_name['custom_targeting_clauses']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMTARGETINGCLAUSE'].fields_by_name['custom_targeting_literals']._loaded_options = None
    _globals['_CUSTOMTARGETINGCLAUSE'].fields_by_name['custom_targeting_literals']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMTARGETINGLITERAL'].fields_by_name['custom_targeting_key']._loaded_options = None
    _globals['_CUSTOMTARGETINGLITERAL'].fields_by_name['custom_targeting_key']._serialized_options = b'\xe0A\x01\xfaA-\n+admanager.googleapis.com/CustomTargetingKey'
    _globals['_CUSTOMTARGETINGLITERAL'].fields_by_name['custom_targeting_values']._loaded_options = None
    _globals['_CUSTOMTARGETINGLITERAL'].fields_by_name['custom_targeting_values']._serialized_options = b'\xe0A\x01\xfaA/\n-admanager.googleapis.com/CustomTargetingValue'
    _globals['_USERDOMAINTARGETING'].fields_by_name['targeted_user_domains']._loaded_options = None
    _globals['_USERDOMAINTARGETING'].fields_by_name['targeted_user_domains']._serialized_options = b'\xe0A\x01'
    _globals['_USERDOMAINTARGETING'].fields_by_name['excluded_user_domains']._loaded_options = None
    _globals['_USERDOMAINTARGETING'].fields_by_name['excluded_user_domains']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOPOSITIONTARGETING'].fields_by_name['video_positions']._loaded_options = None
    _globals['_VIDEOPOSITIONTARGETING'].fields_by_name['video_positions']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOPOSITION'].fields_by_name['midroll_index']._loaded_options = None
    _globals['_VIDEOPOSITION'].fields_by_name['midroll_index']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOPOSITION'].fields_by_name['reverse_midroll_index']._loaded_options = None
    _globals['_VIDEOPOSITION'].fields_by_name['reverse_midroll_index']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOPOSITION'].fields_by_name['pod_position']._loaded_options = None
    _globals['_VIDEOPOSITION'].fields_by_name['pod_position']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOPOSITION'].fields_by_name['position_type']._loaded_options = None
    _globals['_VIDEOPOSITION'].fields_by_name['position_type']._serialized_options = b'\xe0A\x01'
    _globals['_VIDEOPOSITION'].fields_by_name['bumper_type']._loaded_options = None
    _globals['_VIDEOPOSITION'].fields_by_name['bumper_type']._serialized_options = b'\xe0A\x01'
    _globals['_DATASEGMENTTARGETING'].fields_by_name['has_data_segment_targeting']._loaded_options = None
    _globals['_DATASEGMENTTARGETING'].fields_by_name['has_data_segment_targeting']._serialized_options = b'\xe0A\x03'
    _globals['_TARGETING']._serialized_start = 296
    _globals['_TARGETING']._serialized_end = 953
    _globals['_GEOTARGETING']._serialized_start = 956
    _globals['_GEOTARGETING']._serialized_end = 1104
    _globals['_TECHNOLOGYTARGETING']._serialized_start = 1107
    _globals['_TECHNOLOGYTARGETING']._serialized_end = 1389
    _globals['_BANDWIDTHTARGETING']._serialized_start = 1392
    _globals['_BANDWIDTHTARGETING']._serialized_end = 1580
    _globals['_DEVICECATEGORYTARGETING']._serialized_start = 1583
    _globals['_DEVICECATEGORYTARGETING']._serialized_end = 1764
    _globals['_OPERATINGSYSTEMTARGETING']._serialized_start = 1767
    _globals['_OPERATINGSYSTEMTARGETING']._serialized_end = 2167
    _globals['_INVENTORYTARGETING']._serialized_start = 2170
    _globals['_INVENTORYTARGETING']._serialized_end = 2411
    _globals['_ADUNITTARGETING']._serialized_start = 2414
    _globals['_ADUNITTARGETING']._serialized_end = 2564
    _globals['_REQUESTPLATFORMTARGETING']._serialized_start = 2566
    _globals['_REQUESTPLATFORMTARGETING']._serialized_end = 2686
    _globals['_CUSTOMTARGETING']._serialized_start = 2688
    _globals['_CUSTOMTARGETING']._serialized_end = 2792
    _globals['_CUSTOMTARGETINGCLAUSE']._serialized_start = 2794
    _globals['_CUSTOMTARGETINGCLAUSE']._serialized_end = 2906
    _globals['_CUSTOMTARGETINGLITERAL']._serialized_start = 2909
    _globals['_CUSTOMTARGETINGLITERAL']._serialized_end = 3170
    _globals['_USERDOMAINTARGETING']._serialized_start = 3172
    _globals['_USERDOMAINTARGETING']._serialized_end = 3265
    _globals['_VIDEOPOSITIONTARGETING']._serialized_start = 3267
    _globals['_VIDEOPOSITIONTARGETING']._serialized_end = 3361
    _globals['_VIDEOPOSITION']._serialized_start = 3364
    _globals['_VIDEOPOSITION']._serialized_end = 3780
    _globals['_DATASEGMENTTARGETING']._serialized_start = 3782
    _globals['_DATASEGMENTTARGETING']._serialized_end = 3845