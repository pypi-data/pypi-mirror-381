"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/datamanager/v1/event.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.datamanager.v1 import cart_data_pb2 as google_dot_ads_dot_datamanager_dot_v1_dot_cart__data__pb2
from .....google.ads.datamanager.v1 import consent_pb2 as google_dot_ads_dot_datamanager_dot_v1_dot_consent__pb2
from .....google.ads.datamanager.v1 import device_info_pb2 as google_dot_ads_dot_datamanager_dot_v1_dot_device__info__pb2
from .....google.ads.datamanager.v1 import experimental_field_pb2 as google_dot_ads_dot_datamanager_dot_v1_dot_experimental__field__pb2
from .....google.ads.datamanager.v1 import user_data_pb2 as google_dot_ads_dot_datamanager_dot_v1_dot_user__data__pb2
from .....google.ads.datamanager.v1 import user_properties_pb2 as google_dot_ads_dot_datamanager_dot_v1_dot_user__properties__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/ads/datamanager/v1/event.proto\x12\x19google.ads.datamanager.v1\x1a)google/ads/datamanager/v1/cart_data.proto\x1a\'google/ads/datamanager/v1/consent.proto\x1a+google/ads/datamanager/v1/device_info.proto\x1a2google/ads/datamanager/v1/experimental_field.proto\x1a)google/ads/datamanager/v1/user_data.proto\x1a/google/ads/datamanager/v1/user_properties.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe2\x06\n\x05Event\x12#\n\x16destination_references\x18\x01 \x03(\tB\x03\xe0A\x01\x12\x1b\n\x0etransaction_id\x18\x02 \x01(\tB\x03\xe0A\x02\x128\n\x0fevent_timestamp\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02\x12?\n\x16last_updated_timestamp\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x12;\n\tuser_data\x18\x05 \x01(\x0b2#.google.ads.datamanager.v1.UserDataB\x03\xe0A\x01\x128\n\x07consent\x18\x06 \x01(\x0b2".google.ads.datamanager.v1.ConsentB\x03\xe0A\x01\x12E\n\x0ead_identifiers\x18\x07 \x01(\x0b2(.google.ads.datamanager.v1.AdIdentifiersB\x03\xe0A\x01\x12\x15\n\x08currency\x18\x08 \x01(\tB\x03\xe0A\x01\x12\x1d\n\x10conversion_value\x18\t \x01(\x01B\x03\xe0A\x01\x12A\n\x0cevent_source\x18\n \x01(\x0e2&.google.ads.datamanager.v1.EventSourceB\x03\xe0A\x01\x12E\n\x11event_device_info\x18\x0b \x01(\x0b2%.google.ads.datamanager.v1.DeviceInfoB\x03\xe0A\x01\x12;\n\tcart_data\x18\x0c \x01(\x0b2#.google.ads.datamanager.v1.CartDataB\x03\xe0A\x01\x12H\n\x10custom_variables\x18\r \x03(\x0b2).google.ads.datamanager.v1.CustomVariableB\x03\xe0A\x01\x12N\n\x13experimental_fields\x18\x0e \x03(\x0b2,.google.ads.datamanager.v1.ExperimentalFieldB\x03\xe0A\x01\x12G\n\x0fuser_properties\x18\x0f \x01(\x0b2).google.ads.datamanager.v1.UserPropertiesB\x03\xe0A\x01"\xbc\x01\n\rAdIdentifiers\x12\x1f\n\x12session_attributes\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x12\n\x05gclid\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06gbraid\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06wbraid\x18\x04 \x01(\tB\x03\xe0A\x01\x12L\n\x18landing_page_device_info\x18\x05 \x01(\x0b2%.google.ads.datamanager.v1.DeviceInfoB\x03\xe0A\x01"`\n\x0eCustomVariable\x12\x15\n\x08variable\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x12\n\x05value\x18\x02 \x01(\tB\x03\xe0A\x01\x12#\n\x16destination_references\x18\x03 \x03(\tB\x03\xe0A\x01*a\n\x0bEventSource\x12\x1c\n\x18EVENT_SOURCE_UNSPECIFIED\x10\x00\x12\x07\n\x03WEB\x10\x01\x12\x07\n\x03APP\x10\x02\x12\x0c\n\x08IN_STORE\x10\x03\x12\t\n\x05PHONE\x10\x04\x12\t\n\x05OTHER\x10\x05B\xca\x01\n\x1dcom.google.ads.datamanager.v1B\nEventProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager\xaa\x02\x19Google.Ads.DataManager.V1\xca\x02\x19Google\\Ads\\DataManager\\V1\xea\x02\x1cGoogle::Ads::DataManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.datamanager.v1.event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.ads.datamanager.v1B\nEventProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager\xaa\x02\x19Google.Ads.DataManager.V1\xca\x02\x19Google\\Ads\\DataManager\\V1\xea\x02\x1cGoogle::Ads::DataManager::V1'
    _globals['_EVENT'].fields_by_name['destination_references']._loaded_options = None
    _globals['_EVENT'].fields_by_name['destination_references']._serialized_options = b'\xe0A\x01'
    _globals['_EVENT'].fields_by_name['transaction_id']._loaded_options = None
    _globals['_EVENT'].fields_by_name['transaction_id']._serialized_options = b'\xe0A\x02'
    _globals['_EVENT'].fields_by_name['event_timestamp']._loaded_options = None
    _globals['_EVENT'].fields_by_name['event_timestamp']._serialized_options = b'\xe0A\x02'
    _globals['_EVENT'].fields_by_name['last_updated_timestamp']._loaded_options = None
    _globals['_EVENT'].fields_by_name['last_updated_timestamp']._serialized_options = b'\xe0A\x01'
    _globals['_EVENT'].fields_by_name['user_data']._loaded_options = None
    _globals['_EVENT'].fields_by_name['user_data']._serialized_options = b'\xe0A\x01'
    _globals['_EVENT'].fields_by_name['consent']._loaded_options = None
    _globals['_EVENT'].fields_by_name['consent']._serialized_options = b'\xe0A\x01'
    _globals['_EVENT'].fields_by_name['ad_identifiers']._loaded_options = None
    _globals['_EVENT'].fields_by_name['ad_identifiers']._serialized_options = b'\xe0A\x01'
    _globals['_EVENT'].fields_by_name['currency']._loaded_options = None
    _globals['_EVENT'].fields_by_name['currency']._serialized_options = b'\xe0A\x01'
    _globals['_EVENT'].fields_by_name['conversion_value']._loaded_options = None
    _globals['_EVENT'].fields_by_name['conversion_value']._serialized_options = b'\xe0A\x01'
    _globals['_EVENT'].fields_by_name['event_source']._loaded_options = None
    _globals['_EVENT'].fields_by_name['event_source']._serialized_options = b'\xe0A\x01'
    _globals['_EVENT'].fields_by_name['event_device_info']._loaded_options = None
    _globals['_EVENT'].fields_by_name['event_device_info']._serialized_options = b'\xe0A\x01'
    _globals['_EVENT'].fields_by_name['cart_data']._loaded_options = None
    _globals['_EVENT'].fields_by_name['cart_data']._serialized_options = b'\xe0A\x01'
    _globals['_EVENT'].fields_by_name['custom_variables']._loaded_options = None
    _globals['_EVENT'].fields_by_name['custom_variables']._serialized_options = b'\xe0A\x01'
    _globals['_EVENT'].fields_by_name['experimental_fields']._loaded_options = None
    _globals['_EVENT'].fields_by_name['experimental_fields']._serialized_options = b'\xe0A\x01'
    _globals['_EVENT'].fields_by_name['user_properties']._loaded_options = None
    _globals['_EVENT'].fields_by_name['user_properties']._serialized_options = b'\xe0A\x01'
    _globals['_ADIDENTIFIERS'].fields_by_name['session_attributes']._loaded_options = None
    _globals['_ADIDENTIFIERS'].fields_by_name['session_attributes']._serialized_options = b'\xe0A\x01'
    _globals['_ADIDENTIFIERS'].fields_by_name['gclid']._loaded_options = None
    _globals['_ADIDENTIFIERS'].fields_by_name['gclid']._serialized_options = b'\xe0A\x01'
    _globals['_ADIDENTIFIERS'].fields_by_name['gbraid']._loaded_options = None
    _globals['_ADIDENTIFIERS'].fields_by_name['gbraid']._serialized_options = b'\xe0A\x01'
    _globals['_ADIDENTIFIERS'].fields_by_name['wbraid']._loaded_options = None
    _globals['_ADIDENTIFIERS'].fields_by_name['wbraid']._serialized_options = b'\xe0A\x01'
    _globals['_ADIDENTIFIERS'].fields_by_name['landing_page_device_info']._loaded_options = None
    _globals['_ADIDENTIFIERS'].fields_by_name['landing_page_device_info']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMVARIABLE'].fields_by_name['variable']._loaded_options = None
    _globals['_CUSTOMVARIABLE'].fields_by_name['variable']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMVARIABLE'].fields_by_name['value']._loaded_options = None
    _globals['_CUSTOMVARIABLE'].fields_by_name['value']._serialized_options = b'\xe0A\x01'
    _globals['_CUSTOMVARIABLE'].fields_by_name['destination_references']._loaded_options = None
    _globals['_CUSTOMVARIABLE'].fields_by_name['destination_references']._serialized_options = b'\xe0A\x01'
    _globals['_EVENTSOURCE']._serialized_start = 1565
    _globals['_EVENTSOURCE']._serialized_end = 1662
    _globals['_EVENT']._serialized_start = 408
    _globals['_EVENT']._serialized_end = 1274
    _globals['_ADIDENTIFIERS']._serialized_start = 1277
    _globals['_ADIDENTIFIERS']._serialized_end = 1465
    _globals['_CUSTOMVARIABLE']._serialized_start = 1467
    _globals['_CUSTOMVARIABLE']._serialized_end = 1563