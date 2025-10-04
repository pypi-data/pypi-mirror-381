"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/type/types.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n google/shopping/type/types.proto\x12\x14google.shopping.type"\xb1\x01\n\x06Weight\x12\x1a\n\ramount_micros\x18\x01 \x01(\x03H\x00\x88\x01\x01\x125\n\x04unit\x18\x02 \x01(\x0e2\'.google.shopping.type.Weight.WeightUnit"B\n\nWeightUnit\x12\x1b\n\x17WEIGHT_UNIT_UNSPECIFIED\x10\x00\x12\t\n\x05POUND\x10\x01\x12\x0c\n\x08KILOGRAM\x10\x02B\x10\n\x0e_amount_micros"c\n\x05Price\x12\x1a\n\ramount_micros\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x1a\n\rcurrency_code\x18\x02 \x01(\tH\x01\x88\x01\x01B\x10\n\x0e_amount_microsB\x10\n\x0e_currency_code"\x88\x01\n\x0fCustomAttribute\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x12\n\x05value\x18\x02 \x01(\tH\x01\x88\x01\x01\x12;\n\x0cgroup_values\x18\x03 \x03(\x0b2%.google.shopping.type.CustomAttributeB\x07\n\x05_nameB\x08\n\x06_value"\xc1\x01\n\x0bDestination"\xb1\x01\n\x0fDestinationEnum\x12 \n\x1cDESTINATION_ENUM_UNSPECIFIED\x10\x00\x12\x10\n\x0cSHOPPING_ADS\x10\x01\x12\x0f\n\x0bDISPLAY_ADS\x10\x02\x12\x17\n\x13LOCAL_INVENTORY_ADS\x10\x03\x12\x11\n\rFREE_LISTINGS\x10\x04\x12\x17\n\x13FREE_LOCAL_LISTINGS\x10\x05\x12\x14\n\x10YOUTUBE_SHOPPING\x10\x06"\x96\x03\n\x10ReportingContext"\x81\x03\n\x14ReportingContextEnum\x12&\n"REPORTING_CONTEXT_ENUM_UNSPECIFIED\x10\x00\x12\x10\n\x0cSHOPPING_ADS\x10\x01\x12\x15\n\rDISCOVERY_ADS\x10\x02\x1a\x02\x08\x01\x12\x12\n\x0eDEMAND_GEN_ADS\x10\r\x12#\n\x1fDEMAND_GEN_ADS_DISCOVER_SURFACE\x10\x0e\x12\r\n\tVIDEO_ADS\x10\x03\x12\x0f\n\x0bDISPLAY_ADS\x10\x04\x12\x17\n\x13LOCAL_INVENTORY_ADS\x10\x05\x12\x19\n\x15VEHICLE_INVENTORY_ADS\x10\x06\x12\x11\n\rFREE_LISTINGS\x10\x07\x12\x17\n\x13FREE_LOCAL_LISTINGS\x10\x08\x12\x1f\n\x1bFREE_LOCAL_VEHICLE_LISTINGS\x10\t\x12\x14\n\x10YOUTUBE_SHOPPING\x10\n\x12\x10\n\x0cCLOUD_RETAIL\x10\x0b\x12\x16\n\x12LOCAL_CLOUD_RETAIL\x10\x0c"M\n\x07Channel"B\n\x0bChannelEnum\x12\x1c\n\x18CHANNEL_ENUM_UNSPECIFIED\x10\x00\x12\n\n\x06ONLINE\x10\x01\x12\t\n\x05LOCAL\x10\x02Bp\n\x18com.google.shopping.typeB\nTypesProtoP\x01Z/cloud.google.com/go/shopping/type/typepb;typepb\xaa\x02\x14Google.Shopping.Typeb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.type.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.shopping.typeB\nTypesProtoP\x01Z/cloud.google.com/go/shopping/type/typepb;typepb\xaa\x02\x14Google.Shopping.Type'
    _globals['_REPORTINGCONTEXT_REPORTINGCONTEXTENUM'].values_by_name['DISCOVERY_ADS']._loaded_options = None
    _globals['_REPORTINGCONTEXT_REPORTINGCONTEXTENUM'].values_by_name['DISCOVERY_ADS']._serialized_options = b'\x08\x01'
    _globals['_WEIGHT']._serialized_start = 59
    _globals['_WEIGHT']._serialized_end = 236
    _globals['_WEIGHT_WEIGHTUNIT']._serialized_start = 152
    _globals['_WEIGHT_WEIGHTUNIT']._serialized_end = 218
    _globals['_PRICE']._serialized_start = 238
    _globals['_PRICE']._serialized_end = 337
    _globals['_CUSTOMATTRIBUTE']._serialized_start = 340
    _globals['_CUSTOMATTRIBUTE']._serialized_end = 476
    _globals['_DESTINATION']._serialized_start = 479
    _globals['_DESTINATION']._serialized_end = 672
    _globals['_DESTINATION_DESTINATIONENUM']._serialized_start = 495
    _globals['_DESTINATION_DESTINATIONENUM']._serialized_end = 672
    _globals['_REPORTINGCONTEXT']._serialized_start = 675
    _globals['_REPORTINGCONTEXT']._serialized_end = 1081
    _globals['_REPORTINGCONTEXT_REPORTINGCONTEXTENUM']._serialized_start = 696
    _globals['_REPORTINGCONTEXT_REPORTINGCONTEXTENUM']._serialized_end = 1081
    _globals['_CHANNEL']._serialized_start = 1083
    _globals['_CHANNEL']._serialized_end = 1160
    _globals['_CHANNEL_CHANNELENUM']._serialized_start = 1094
    _globals['_CHANNEL_CHANNELENUM']._serialized_end = 1160