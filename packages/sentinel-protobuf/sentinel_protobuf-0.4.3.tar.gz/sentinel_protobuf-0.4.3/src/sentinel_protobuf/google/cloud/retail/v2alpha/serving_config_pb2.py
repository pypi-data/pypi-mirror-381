"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2alpha/serving_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2alpha import common_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_common__pb2
from .....google.cloud.retail.v2alpha import search_service_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_search__service__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/retail/v2alpha/serving_config.proto\x12\x1bgoogle.cloud.retail.v2alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/retail/v2alpha/common.proto\x1a0google/cloud/retail/v2alpha/search_service.proto"\xaa\x08\n\rServingConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x10\n\x08model_id\x18\x03 \x01(\t\x12\x1d\n\x15price_reranking_level\x18\x04 \x01(\t\x12\x19\n\x11facet_control_ids\x18\x05 \x03(\t\x12W\n\x12dynamic_facet_spec\x18\x06 \x01(\x0b2;.google.cloud.retail.v2alpha.SearchRequest.DynamicFacetSpec\x12\x19\n\x11boost_control_ids\x18\x07 \x03(\t\x12\x1a\n\x12filter_control_ids\x18\t \x03(\t\x12\x1c\n\x14redirect_control_ids\x18\n \x03(\t\x12#\n\x1btwoway_synonyms_control_ids\x18\x12 \x03(\t\x12#\n\x1boneway_synonyms_control_ids\x18\x0c \x03(\t\x12$\n\x1cdo_not_associate_control_ids\x18\r \x03(\t\x12\x1f\n\x17replacement_control_ids\x18\x0e \x03(\t\x12\x1a\n\x12ignore_control_ids\x18\x0f \x03(\t\x12\x17\n\x0fdiversity_level\x18\x08 \x01(\t\x12P\n\x0ediversity_type\x18\x14 \x01(\x0e28.google.cloud.retail.v2alpha.ServingConfig.DiversityType\x12$\n\x1cenable_category_filter_level\x18\x10 \x01(\t\x12\x1c\n\x14ignore_recs_denylist\x18\x18 \x01(\x08\x12\\\n\x14personalization_spec\x18\x15 \x01(\x0b2>.google.cloud.retail.v2alpha.SearchRequest.PersonalizationSpec\x12I\n\x0esolution_types\x18\x13 \x03(\x0e2).google.cloud.retail.v2alpha.SolutionTypeB\x06\xe0A\x02\xe0A\x05"d\n\rDiversityType\x12\x1e\n\x1aDIVERSITY_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14RULE_BASED_DIVERSITY\x10\x02\x12\x19\n\x15DATA_DRIVEN_DIVERSITY\x10\x03:\x85\x01\xeaA\x81\x01\n#retail.googleapis.com/ServingConfig\x12Zprojects/{project}/locations/{location}/catalogs/{catalog}/servingConfigs/{serving_config}B\xd6\x01\n\x1fcom.google.cloud.retail.v2alphaB\x12ServingConfigProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2alpha.serving_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.retail.v2alphaB\x12ServingConfigProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alpha'
    _globals['_SERVINGCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_SERVINGCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_SERVINGCONFIG'].fields_by_name['display_name']._loaded_options = None
    _globals['_SERVINGCONFIG'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_SERVINGCONFIG'].fields_by_name['solution_types']._loaded_options = None
    _globals['_SERVINGCONFIG'].fields_by_name['solution_types']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_SERVINGCONFIG']._loaded_options = None
    _globals['_SERVINGCONFIG']._serialized_options = b'\xeaA\x81\x01\n#retail.googleapis.com/ServingConfig\x12Zprojects/{project}/locations/{location}/catalogs/{catalog}/servingConfigs/{serving_config}'
    _globals['_SERVINGCONFIG']._serialized_start = 234
    _globals['_SERVINGCONFIG']._serialized_end = 1300
    _globals['_SERVINGCONFIG_DIVERSITYTYPE']._serialized_start = 1064
    _globals['_SERVINGCONFIG_DIVERSITYTYPE']._serialized_end = 1164