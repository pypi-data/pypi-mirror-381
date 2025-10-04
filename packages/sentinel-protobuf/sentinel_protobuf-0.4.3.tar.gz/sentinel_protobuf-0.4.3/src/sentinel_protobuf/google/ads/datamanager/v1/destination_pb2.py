"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/datamanager/v1/destination.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/ads/datamanager/v1/destination.proto\x12\x19google.ads.datamanager.v1\x1a\x1fgoogle/api/field_behavior.proto"\xa4\x02\n\x0bDestination\x12\x16\n\treference\x18\x01 \x01(\tB\x03\xe0A\x01\x12E\n\rlogin_account\x18\x02 \x01(\x0b2).google.ads.datamanager.v1.ProductAccountB\x03\xe0A\x01\x12F\n\x0elinked_account\x18\x03 \x01(\x0b2).google.ads.datamanager.v1.ProductAccountB\x03\xe0A\x01\x12I\n\x11operating_account\x18\x04 \x01(\x0b2).google.ads.datamanager.v1.ProductAccountB\x03\xe0A\x02\x12#\n\x16product_destination_id\x18\x05 \x01(\tB\x03\xe0A\x02"c\n\x0eProductAccount\x128\n\x07product\x18\x01 \x01(\x0e2".google.ads.datamanager.v1.ProductB\x03\xe0A\x02\x12\x17\n\naccount_id\x18\x02 \x01(\tB\x03\xe0A\x02*}\n\x07Product\x12\x17\n\x13PRODUCT_UNSPECIFIED\x10\x00\x12\x0e\n\nGOOGLE_ADS\x10\x01\x12\x19\n\x15DISPLAY_VIDEO_PARTNER\x10\x02\x12\x1c\n\x18DISPLAY_VIDEO_ADVERTISER\x10\x03\x12\x10\n\x0cDATA_PARTNER\x10\x04B\xd0\x01\n\x1dcom.google.ads.datamanager.v1B\x10DestinationProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager\xaa\x02\x19Google.Ads.DataManager.V1\xca\x02\x19Google\\Ads\\DataManager\\V1\xea\x02\x1cGoogle::Ads::DataManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.datamanager.v1.destination_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.ads.datamanager.v1B\x10DestinationProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager\xaa\x02\x19Google.Ads.DataManager.V1\xca\x02\x19Google\\Ads\\DataManager\\V1\xea\x02\x1cGoogle::Ads::DataManager::V1'
    _globals['_DESTINATION'].fields_by_name['reference']._loaded_options = None
    _globals['_DESTINATION'].fields_by_name['reference']._serialized_options = b'\xe0A\x01'
    _globals['_DESTINATION'].fields_by_name['login_account']._loaded_options = None
    _globals['_DESTINATION'].fields_by_name['login_account']._serialized_options = b'\xe0A\x01'
    _globals['_DESTINATION'].fields_by_name['linked_account']._loaded_options = None
    _globals['_DESTINATION'].fields_by_name['linked_account']._serialized_options = b'\xe0A\x01'
    _globals['_DESTINATION'].fields_by_name['operating_account']._loaded_options = None
    _globals['_DESTINATION'].fields_by_name['operating_account']._serialized_options = b'\xe0A\x02'
    _globals['_DESTINATION'].fields_by_name['product_destination_id']._loaded_options = None
    _globals['_DESTINATION'].fields_by_name['product_destination_id']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCTACCOUNT'].fields_by_name['product']._loaded_options = None
    _globals['_PRODUCTACCOUNT'].fields_by_name['product']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCTACCOUNT'].fields_by_name['account_id']._loaded_options = None
    _globals['_PRODUCTACCOUNT'].fields_by_name['account_id']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCT']._serialized_start = 503
    _globals['_PRODUCT']._serialized_end = 628
    _globals['_DESTINATION']._serialized_start = 108
    _globals['_DESTINATION']._serialized_end = 400
    _globals['_PRODUCTACCOUNT']._serialized_start = 402
    _globals['_PRODUCTACCOUNT']._serialized_end = 501