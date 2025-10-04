"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/securitycenter/v2/ip_rules.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/securitycenter/v2/ip_rules.proto\x12\x1egoogle.cloud.securitycenter.v2\x1a\x1fgoogle/api/field_behavior.proto"\xe2\x02\n\x07IpRules\x12D\n\tdirection\x18\x01 \x01(\x0e21.google.cloud.securitycenter.v2.IpRules.Direction\x12:\n\x07allowed\x18\x02 \x01(\x0b2\'.google.cloud.securitycenter.v2.AllowedH\x00\x128\n\x06denied\x18\x03 \x01(\x0b2&.google.cloud.securitycenter.v2.DeniedH\x00\x12\x18\n\x10source_ip_ranges\x18\x04 \x03(\t\x12\x1d\n\x15destination_ip_ranges\x18\x05 \x03(\t\x12\x18\n\x10exposed_services\x18\x06 \x03(\t"?\n\tDirection\x12\x19\n\x15DIRECTION_UNSPECIFIED\x10\x00\x12\x0b\n\x07INGRESS\x10\x01\x12\n\n\x06EGRESS\x10\x02B\x07\n\x05rules"\x8d\x01\n\x06IpRule\x12\x10\n\x08protocol\x18\x01 \x01(\t\x12J\n\x0bport_ranges\x18\x02 \x03(\x0b20.google.cloud.securitycenter.v2.IpRule.PortRangeB\x03\xe0A\x01\x1a%\n\tPortRange\x12\x0b\n\x03min\x18\x01 \x01(\x03\x12\x0b\n\x03max\x18\x02 \x01(\x03"H\n\x07Allowed\x12=\n\x08ip_rules\x18\x01 \x03(\x0b2&.google.cloud.securitycenter.v2.IpRuleB\x03\xe0A\x01"G\n\x06Denied\x12=\n\x08ip_rules\x18\x01 \x03(\x0b2&.google.cloud.securitycenter.v2.IpRuleB\x03\xe0A\x01B\xe6\x01\n"com.google.cloud.securitycenter.v2B\x0cIpRulesProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v2.ip_rules_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v2B\x0cIpRulesProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2'
    _globals['_IPRULE'].fields_by_name['port_ranges']._loaded_options = None
    _globals['_IPRULE'].fields_by_name['port_ranges']._serialized_options = b'\xe0A\x01'
    _globals['_ALLOWED'].fields_by_name['ip_rules']._loaded_options = None
    _globals['_ALLOWED'].fields_by_name['ip_rules']._serialized_options = b'\xe0A\x01'
    _globals['_DENIED'].fields_by_name['ip_rules']._loaded_options = None
    _globals['_DENIED'].fields_by_name['ip_rules']._serialized_options = b'\xe0A\x01'
    _globals['_IPRULES']._serialized_start = 115
    _globals['_IPRULES']._serialized_end = 469
    _globals['_IPRULES_DIRECTION']._serialized_start = 397
    _globals['_IPRULES_DIRECTION']._serialized_end = 460
    _globals['_IPRULE']._serialized_start = 472
    _globals['_IPRULE']._serialized_end = 613
    _globals['_IPRULE_PORTRANGE']._serialized_start = 576
    _globals['_IPRULE_PORTRANGE']._serialized_end = 613
    _globals['_ALLOWED']._serialized_start = 615
    _globals['_ALLOWED']._serialized_end = 687
    _globals['_DENIED']._serialized_start = 689
    _globals['_DENIED']._serialized_end = 760