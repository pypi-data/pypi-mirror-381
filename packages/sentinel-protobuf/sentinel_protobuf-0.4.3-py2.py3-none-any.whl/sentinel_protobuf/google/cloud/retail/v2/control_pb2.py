"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2/control.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2 import common_pb2 as google_dot_cloud_dot_retail_dot_v2_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$google/cloud/retail/v2/control.proto\x12\x16google.cloud.retail.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/cloud/retail/v2/common.proto"\xa6\x03\n\x07Control\x12,\n\x04rule\x18\x04 \x01(\x0b2\x1c.google.cloud.retail.v2.RuleH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12*\n\x1dassociated_serving_config_ids\x18\x05 \x03(\tB\x03\xe0A\x03\x12D\n\x0esolution_types\x18\x06 \x03(\x0e2$.google.cloud.retail.v2.SolutionTypeB\x06\xe0A\x02\xe0A\x05\x12O\n\x18search_solution_use_case\x18\x07 \x03(\x0e2-.google.cloud.retail.v2.SearchSolutionUseCase:q\xeaAn\n\x1dretail.googleapis.com/Control\x12Mprojects/{project}/locations/{location}/catalogs/{catalog}/controls/{control}B\t\n\x07controlB\xb7\x01\n\x1acom.google.cloud.retail.v2B\x0cControlProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2.control_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.retail.v2B\x0cControlProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2'
    _globals['_CONTROL'].fields_by_name['name']._loaded_options = None
    _globals['_CONTROL'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_CONTROL'].fields_by_name['display_name']._loaded_options = None
    _globals['_CONTROL'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_CONTROL'].fields_by_name['associated_serving_config_ids']._loaded_options = None
    _globals['_CONTROL'].fields_by_name['associated_serving_config_ids']._serialized_options = b'\xe0A\x03'
    _globals['_CONTROL'].fields_by_name['solution_types']._loaded_options = None
    _globals['_CONTROL'].fields_by_name['solution_types']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_CONTROL']._loaded_options = None
    _globals['_CONTROL']._serialized_options = b'\xeaAn\n\x1dretail.googleapis.com/Control\x12Mprojects/{project}/locations/{location}/catalogs/{catalog}/controls/{control}'
    _globals['_CONTROL']._serialized_start = 162
    _globals['_CONTROL']._serialized_end = 584