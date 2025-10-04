"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/datamanager/v1/user_properties.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/ads/datamanager/v1/user_properties.proto\x12\x19google.ads.datamanager.v1\x1a\x1fgoogle/api/field_behavior.proto"\xa9\x01\n\x0eUserProperties\x12C\n\rcustomer_type\x18\x01 \x01(\x0e2\'.google.ads.datamanager.v1.CustomerTypeB\x03\xe0A\x01\x12R\n\x15customer_value_bucket\x18\x02 \x01(\x0e2..google.ads.datamanager.v1.CustomerValueBucketB\x03\xe0A\x01*T\n\x0cCustomerType\x12\x1d\n\x19CUSTOMER_TYPE_UNSPECIFIED\x10\x00\x12\x07\n\x03NEW\x10\x01\x12\r\n\tRETURNING\x10\x02\x12\r\n\tREENGAGED\x10\x03*[\n\x13CustomerValueBucket\x12%\n!CUSTOMER_VALUE_BUCKET_UNSPECIFIED\x10\x00\x12\x07\n\x03LOW\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x12\x08\n\x04HIGH\x10\x03B\xd3\x01\n\x1dcom.google.ads.datamanager.v1B\x13UserPropertiesProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager\xaa\x02\x19Google.Ads.DataManager.V1\xca\x02\x19Google\\Ads\\DataManager\\V1\xea\x02\x1cGoogle::Ads::DataManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.datamanager.v1.user_properties_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.ads.datamanager.v1B\x13UserPropertiesProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager\xaa\x02\x19Google.Ads.DataManager.V1\xca\x02\x19Google\\Ads\\DataManager\\V1\xea\x02\x1cGoogle::Ads::DataManager::V1'
    _globals['_USERPROPERTIES'].fields_by_name['customer_type']._loaded_options = None
    _globals['_USERPROPERTIES'].fields_by_name['customer_type']._serialized_options = b'\xe0A\x01'
    _globals['_USERPROPERTIES'].fields_by_name['customer_value_bucket']._loaded_options = None
    _globals['_USERPROPERTIES'].fields_by_name['customer_value_bucket']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMERTYPE']._serialized_start = 283
    _globals['_CUSTOMERTYPE']._serialized_end = 367
    _globals['_CUSTOMERVALUEBUCKET']._serialized_start = 369
    _globals['_CUSTOMERVALUEBUCKET']._serialized_end = 460
    _globals['_USERPROPERTIES']._serialized_start = 112
    _globals['_USERPROPERTIES']._serialized_end = 281