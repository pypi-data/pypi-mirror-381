"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/admanager/v1/operating_system_messages.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/ads/admanager/v1/operating_system_messages.proto\x12\x17google.ads.admanager.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xe6\x01\n\x0fOperatingSystem\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1e\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01:\x8e\x01\xeaA\x8a\x01\n(admanager.googleapis.com/OperatingSystem\x12;networks/{network_code}/operatingSystems/{operating_system}*\x10operatingSystems2\x0foperatingSystemB\x0f\n\r_display_nameB\xd0\x01\n\x1bcom.google.ads.admanager.v1B\x1cOperatingSystemMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.operating_system_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x1cOperatingSystemMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_OPERATINGSYSTEM'].fields_by_name['name']._loaded_options = None
    _globals['_OPERATINGSYSTEM'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_OPERATINGSYSTEM'].fields_by_name['display_name']._loaded_options = None
    _globals['_OPERATINGSYSTEM'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATINGSYSTEM']._loaded_options = None
    _globals['_OPERATINGSYSTEM']._serialized_options = b'\xeaA\x8a\x01\n(admanager.googleapis.com/OperatingSystem\x12;networks/{network_code}/operatingSystems/{operating_system}*\x10operatingSystems2\x0foperatingSystem'
    _globals['_OPERATINGSYSTEM']._serialized_start = 145
    _globals['_OPERATINGSYSTEM']._serialized_end = 375