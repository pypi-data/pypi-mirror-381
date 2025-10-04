"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/mobile_device_constant.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import mobile_device_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_mobile__device__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/ads/googleads/v20/resources/mobile_device_constant.proto\x12"google.ads.googleads.v20.resources\x1a7google/ads/googleads/v20/enums/mobile_device_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xd4\x03\n\x14MobileDeviceConstant\x12L\n\rresource_name\x18\x01 \x01(\tB5\xe0A\x03\xfaA/\n-googleads.googleapis.com/MobileDeviceConstant\x12\x14\n\x02id\x18\x07 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x16\n\x04name\x18\x08 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12#\n\x11manufacturer_name\x18\t \x01(\tB\x03\xe0A\x03H\x02\x88\x01\x01\x12\'\n\x15operating_system_name\x18\n \x01(\tB\x03\xe0A\x03H\x03\x88\x01\x01\x12X\n\x04type\x18\x06 \x01(\x0e2E.google.ads.googleads.v20.enums.MobileDeviceTypeEnum.MobileDeviceTypeB\x03\xe0A\x03:X\xeaAU\n-googleads.googleapis.com/MobileDeviceConstant\x12$mobileDeviceConstants/{criterion_id}B\x05\n\x03_idB\x07\n\x05_nameB\x14\n\x12_manufacturer_nameB\x18\n\x16_operating_system_nameB\x8b\x02\n&com.google.ads.googleads.v20.resourcesB\x19MobileDeviceConstantProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.mobile_device_constant_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x19MobileDeviceConstantProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_MOBILEDEVICECONSTANT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MOBILEDEVICECONSTANT'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA/\n-googleads.googleapis.com/MobileDeviceConstant'
    _globals['_MOBILEDEVICECONSTANT'].fields_by_name['id']._loaded_options = None
    _globals['_MOBILEDEVICECONSTANT'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_MOBILEDEVICECONSTANT'].fields_by_name['name']._loaded_options = None
    _globals['_MOBILEDEVICECONSTANT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_MOBILEDEVICECONSTANT'].fields_by_name['manufacturer_name']._loaded_options = None
    _globals['_MOBILEDEVICECONSTANT'].fields_by_name['manufacturer_name']._serialized_options = b'\xe0A\x03'
    _globals['_MOBILEDEVICECONSTANT'].fields_by_name['operating_system_name']._loaded_options = None
    _globals['_MOBILEDEVICECONSTANT'].fields_by_name['operating_system_name']._serialized_options = b'\xe0A\x03'
    _globals['_MOBILEDEVICECONSTANT'].fields_by_name['type']._loaded_options = None
    _globals['_MOBILEDEVICECONSTANT'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_MOBILEDEVICECONSTANT']._loaded_options = None
    _globals['_MOBILEDEVICECONSTANT']._serialized_options = b'\xeaAU\n-googleads.googleapis.com/MobileDeviceConstant\x12$mobileDeviceConstants/{criterion_id}'
    _globals['_MOBILEDEVICECONSTANT']._serialized_start = 221
    _globals['_MOBILEDEVICECONSTANT']._serialized_end = 689