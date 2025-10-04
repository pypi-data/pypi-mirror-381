"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/geo_target_constant.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import geo_target_constant_status_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_geo__target__constant__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/ads/googleads/v20/resources/geo_target_constant.proto\x12"google.ads.googleads.v20.resources\x1a?google/ads/googleads/v20/enums/geo_target_constant_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xd9\x04\n\x11GeoTargetConstant\x12I\n\rresource_name\x18\x01 \x01(\tB2\xe0A\x03\xfaA,\n*googleads.googleapis.com/GeoTargetConstant\x12\x14\n\x02id\x18\n \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x16\n\x04name\x18\x0b \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12\x1e\n\x0ccountry_code\x18\x0c \x01(\tB\x03\xe0A\x03H\x02\x88\x01\x01\x12\x1d\n\x0btarget_type\x18\r \x01(\tB\x03\xe0A\x03H\x03\x88\x01\x01\x12h\n\x06status\x18\x07 \x01(\x0e2S.google.ads.googleads.v20.enums.GeoTargetConstantStatusEnum.GeoTargetConstantStatusB\x03\xe0A\x03\x12 \n\x0ecanonical_name\x18\x0e \x01(\tB\x03\xe0A\x03H\x04\x88\x01\x01\x12R\n\x11parent_geo_target\x18\t \x01(\tB2\xe0A\x03\xfaA,\n*googleads.googleapis.com/GeoTargetConstantH\x05\x88\x01\x01:R\xeaAO\n*googleads.googleapis.com/GeoTargetConstant\x12!geoTargetConstants/{criterion_id}B\x05\n\x03_idB\x07\n\x05_nameB\x0f\n\r_country_codeB\x0e\n\x0c_target_typeB\x11\n\x0f_canonical_nameB\x14\n\x12_parent_geo_targetB\x88\x02\n&com.google.ads.googleads.v20.resourcesB\x16GeoTargetConstantProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.geo_target_constant_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x16GeoTargetConstantProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_GEOTARGETCONSTANT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_GEOTARGETCONSTANT'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA,\n*googleads.googleapis.com/GeoTargetConstant'
    _globals['_GEOTARGETCONSTANT'].fields_by_name['id']._loaded_options = None
    _globals['_GEOTARGETCONSTANT'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_GEOTARGETCONSTANT'].fields_by_name['name']._loaded_options = None
    _globals['_GEOTARGETCONSTANT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_GEOTARGETCONSTANT'].fields_by_name['country_code']._loaded_options = None
    _globals['_GEOTARGETCONSTANT'].fields_by_name['country_code']._serialized_options = b'\xe0A\x03'
    _globals['_GEOTARGETCONSTANT'].fields_by_name['target_type']._loaded_options = None
    _globals['_GEOTARGETCONSTANT'].fields_by_name['target_type']._serialized_options = b'\xe0A\x03'
    _globals['_GEOTARGETCONSTANT'].fields_by_name['status']._loaded_options = None
    _globals['_GEOTARGETCONSTANT'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_GEOTARGETCONSTANT'].fields_by_name['canonical_name']._loaded_options = None
    _globals['_GEOTARGETCONSTANT'].fields_by_name['canonical_name']._serialized_options = b'\xe0A\x03'
    _globals['_GEOTARGETCONSTANT'].fields_by_name['parent_geo_target']._loaded_options = None
    _globals['_GEOTARGETCONSTANT'].fields_by_name['parent_geo_target']._serialized_options = b'\xe0A\x03\xfaA,\n*googleads.googleapis.com/GeoTargetConstant'
    _globals['_GEOTARGETCONSTANT']._loaded_options = None
    _globals['_GEOTARGETCONSTANT']._serialized_options = b'\xeaAO\n*googleads.googleapis.com/GeoTargetConstant\x12!geoTargetConstants/{criterion_id}'
    _globals['_GEOTARGETCONSTANT']._serialized_start = 226
    _globals['_GEOTARGETCONSTANT']._serialized_end = 827