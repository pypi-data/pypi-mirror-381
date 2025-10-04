"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/capacityplanner/v1beta/resource.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/capacityplanner/v1beta/resource.proto\x12#google.cloud.capacityplanner.v1beta\x1a\x1fgoogle/api/field_behavior.proto"\xaf\x01\n\x11ResourceContainer\x12I\n\x04type\x18\x01 \x01(\x0e2;.google.cloud.capacityplanner.v1beta.ResourceContainer.Type\x12\x0f\n\x02id\x18\x02 \x01(\tB\x03\xe0A\x02">\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PROJECT\x10\x01\x12\n\n\x06FOLDER\x10\x02\x12\x07\n\x03ORG\x10\x03"\x91\x01\n\rResourceIdKey\x12\x1c\n\rresource_code\x18\x02 \x01(\tB\x03\xe0A\x02H\x00\x12Q\n\x0bresource_id\x18\x01 \x01(\x0b27.google.cloud.capacityplanner.v1beta.ResourceIdentifierB\x03\xe0A\x02B\x0f\n\rdemand_fields"\x96\x01\n\x12ResourceIdentifier\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12S\n\x13resource_attributes\x18\x03 \x03(\x0b26.google.cloud.capacityplanner.v1beta.ResourceAttribute"c\n\x11ResourceAttribute\x12\x0b\n\x03key\x18\x01 \x01(\t\x12A\n\x05value\x18\x02 \x01(\x0b22.google.cloud.capacityplanner.v1beta.ResourceValue"\x83\x01\n\rResourceValue\x127\n\x04unit\x18\x01 \x01(\x0e2).google.cloud.capacityplanner.v1beta.Unit\x129\n\x05value\x18\x02 \x01(\x0b2*.google.cloud.capacityplanner.v1beta.Value"m\n\x05Value\x12\x15\n\x0bint64_value\x18\x01 \x01(\x03H\x00\x12\x16\n\x0cstring_value\x18\x02 \x01(\tH\x00\x12\x16\n\x0cdouble_value\x18\x03 \x01(\x01H\x00\x12\x14\n\nbool_value\x18\x04 \x01(\x08H\x00B\x07\n\x05value*\xec\x01\n\x04Unit\x12\x14\n\x10UNIT_UNSPECIFIED\x10\x00\x12\x0e\n\nUNIT_COUNT\x10\x01\x12\x06\n\x02KB\x10\x02\x12\x06\n\x02GB\x10\x03\x12\x06\n\x02TB\x10\x04\x12\x07\n\x03MIB\x10\x11\x12\x07\n\x03GIB\x10\x05\x12\x07\n\x03TIB\x10\x06\x12\x07\n\x03QPS\x10\x07\x12\x06\n\x02MB\x10\x08\x12\x07\n\x03PIB\x10\t\x12\x0c\n\x04TBPS\x10\n\x1a\x02\x08\x01\x12\r\n\tGBPS_BITS\x10\x0b\x12\x0c\n\x08GIB_BITS\x10\x0c\x12\r\n\tMBPS_BITS\x10\r\x12\x0e\n\nMBPS_BYTES\x10\x0e\x12\r\n\tTBPS_BITS\x10\x0f\x12\x0e\n\nTBPS_BYTES\x10\x10\x12\x08\n\x04KOPS\x10\x12B\x82\x02\n\'com.google.cloud.capacityplanner.v1betaB\rResourceProtoP\x01ZQcloud.google.com/go/capacityplanner/apiv1beta/capacityplannerpb;capacityplannerpb\xaa\x02#Google.Cloud.CapacityPlanner.V1Beta\xca\x02#Google\\Cloud\\CapacityPlanner\\V1beta\xea\x02&Google::Cloud::CapacityPlanner::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.capacityplanner.v1beta.resource_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.capacityplanner.v1betaB\rResourceProtoP\x01ZQcloud.google.com/go/capacityplanner/apiv1beta/capacityplannerpb;capacityplannerpb\xaa\x02#Google.Cloud.CapacityPlanner.V1Beta\xca\x02#Google\\Cloud\\CapacityPlanner\\V1beta\xea\x02&Google::Cloud::CapacityPlanner::V1beta"
    _globals['_UNIT'].values_by_name['TBPS']._loaded_options = None
    _globals['_UNIT'].values_by_name['TBPS']._serialized_options = b'\x08\x01'
    _globals['_RESOURCECONTAINER'].fields_by_name['id']._loaded_options = None
    _globals['_RESOURCECONTAINER'].fields_by_name['id']._serialized_options = b'\xe0A\x02'
    _globals['_RESOURCEIDKEY'].fields_by_name['resource_code']._loaded_options = None
    _globals['_RESOURCEIDKEY'].fields_by_name['resource_code']._serialized_options = b'\xe0A\x02'
    _globals['_RESOURCEIDKEY'].fields_by_name['resource_id']._loaded_options = None
    _globals['_RESOURCEIDKEY'].fields_by_name['resource_id']._serialized_options = b'\xe0A\x02'
    _globals['_UNIT']._serialized_start = 950
    _globals['_UNIT']._serialized_end = 1186
    _globals['_RESOURCECONTAINER']._serialized_start = 125
    _globals['_RESOURCECONTAINER']._serialized_end = 300
    _globals['_RESOURCECONTAINER_TYPE']._serialized_start = 238
    _globals['_RESOURCECONTAINER_TYPE']._serialized_end = 300
    _globals['_RESOURCEIDKEY']._serialized_start = 303
    _globals['_RESOURCEIDKEY']._serialized_end = 448
    _globals['_RESOURCEIDENTIFIER']._serialized_start = 451
    _globals['_RESOURCEIDENTIFIER']._serialized_end = 601
    _globals['_RESOURCEATTRIBUTE']._serialized_start = 603
    _globals['_RESOURCEATTRIBUTE']._serialized_end = 702
    _globals['_RESOURCEVALUE']._serialized_start = 705
    _globals['_RESOURCEVALUE']._serialized_end = 836
    _globals['_VALUE']._serialized_start = 838
    _globals['_VALUE']._serialized_end = 947