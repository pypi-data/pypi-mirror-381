"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/admanager/v1/operating_system_version_messages.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/ads/admanager/v1/operating_system_version_messages.proto\x12\x17google.ads.admanager.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xf9\x02\n\x16OperatingSystemVersion\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1f\n\rmajor_version\x18\x02 \x01(\x05B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1f\n\rminor_version\x18\x03 \x01(\x05B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x1f\n\rmicro_version\x18\x04 \x01(\x05B\x03\xe0A\x03H\x02\x88\x01\x01:\xb2\x01\xeaA\xae\x01\n/admanager.googleapis.com/OperatingSystemVersion\x12Jnetworks/{network_code}/operatingSystemVersions/{operating_system_version}*\x17operatingSystemVersions2\x16operatingSystemVersionB\x10\n\x0e_major_versionB\x10\n\x0e_minor_versionB\x10\n\x0e_micro_versionB\xd7\x01\n\x1bcom.google.ads.admanager.v1B#OperatingSystemVersionMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.operating_system_version_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B#OperatingSystemVersionMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_OPERATINGSYSTEMVERSION'].fields_by_name['name']._loaded_options = None
    _globals['_OPERATINGSYSTEMVERSION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_OPERATINGSYSTEMVERSION'].fields_by_name['major_version']._loaded_options = None
    _globals['_OPERATINGSYSTEMVERSION'].fields_by_name['major_version']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATINGSYSTEMVERSION'].fields_by_name['minor_version']._loaded_options = None
    _globals['_OPERATINGSYSTEMVERSION'].fields_by_name['minor_version']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATINGSYSTEMVERSION'].fields_by_name['micro_version']._loaded_options = None
    _globals['_OPERATINGSYSTEMVERSION'].fields_by_name['micro_version']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATINGSYSTEMVERSION']._loaded_options = None
    _globals['_OPERATINGSYSTEMVERSION']._serialized_options = b'\xeaA\xae\x01\n/admanager.googleapis.com/OperatingSystemVersion\x12Jnetworks/{network_code}/operatingSystemVersions/{operating_system_version}*\x17operatingSystemVersions2\x16operatingSystemVersion'
    _globals['_OPERATINGSYSTEMVERSION']._serialized_start = 153
    _globals['_OPERATINGSYSTEMVERSION']._serialized_end = 530