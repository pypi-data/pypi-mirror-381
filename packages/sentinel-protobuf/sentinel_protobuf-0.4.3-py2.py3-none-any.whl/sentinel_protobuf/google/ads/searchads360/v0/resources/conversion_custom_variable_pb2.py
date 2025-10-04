"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/conversion_custom_variable.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.enums import conversion_custom_variable_cardinality_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_conversion__custom__variable__cardinality__pb2
from ......google.ads.searchads360.v0.enums import conversion_custom_variable_family_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_conversion__custom__variable__family__pb2
from ......google.ads.searchads360.v0.enums import conversion_custom_variable_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_conversion__custom__variable__status__pb2
from ......google.ads.searchads360.v0.enums import floodlight_variable_data_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_floodlight__variable__data__type__pb2
from ......google.ads.searchads360.v0.enums import floodlight_variable_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_floodlight__variable__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/ads/searchads360/v0/resources/conversion_custom_variable.proto\x12$google.ads.searchads360.v0.resources\x1aMgoogle/ads/searchads360/v0/enums/conversion_custom_variable_cardinality.proto\x1aHgoogle/ads/searchads360/v0/enums/conversion_custom_variable_family.proto\x1aHgoogle/ads/searchads360/v0/enums/conversion_custom_variable_status.proto\x1aDgoogle/ads/searchads360/v0/enums/floodlight_variable_data_type.proto\x1a?google/ads/searchads360/v0/enums/floodlight_variable_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xb2\n\n\x18ConversionCustomVariable\x12S\n\rresource_name\x18\x01 \x01(\tB<\xe0A\x05\xfaA6\n4searchads360.googleapis.com/ConversionCustomVariable\x12\x0f\n\x02id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x11\n\x04name\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x13\n\x03tag\x18\x04 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12s\n\x06status\x18\x05 \x01(\x0e2c.google.ads.searchads360.v0.enums.ConversionCustomVariableStatusEnum.ConversionCustomVariableStatus\x12D\n\x0eowner_customer\x18\x06 \x01(\tB,\xe0A\x03\xfaA&\n$searchads360.googleapis.com/Customer\x12x\n\x06family\x18\x07 \x01(\x0e2c.google.ads.searchads360.v0.enums.ConversionCustomVariableFamilyEnum.ConversionCustomVariableFamilyB\x03\xe0A\x03\x12\x87\x01\n\x0bcardinality\x18\x08 \x01(\x0e2m.google.ads.searchads360.v0.enums.ConversionCustomVariableCardinalityEnum.ConversionCustomVariableCardinalityB\x03\xe0A\x03\x12\x9e\x01\n*floodlight_conversion_custom_variable_info\x18\t \x01(\x0b2e.google.ads.searchads360.v0.resources.ConversionCustomVariable.FloodlightConversionCustomVariableInfoB\x03\xe0A\x03\x12\x1e\n\x11custom_column_ids\x18\n \x03(\x03B\x03\xe0A\x03\x1a\xf7\x02\n&FloodlightConversionCustomVariableInfo\x12\x7f\n\x18floodlight_variable_type\x18\x01 \x01(\x0e2S.google.ads.searchads360.v0.enums.FloodlightVariableTypeEnum.FloodlightVariableTypeB\x03\xe0A\x03H\x00\x88\x01\x01\x12\x8c\x01\n\x1dfloodlight_variable_data_type\x18\x02 \x01(\x0e2[.google.ads.searchads360.v0.enums.FloodlightVariableDataTypeEnum.FloodlightVariableDataTypeB\x03\xe0A\x03H\x01\x88\x01\x01B\x1b\n\x19_floodlight_variable_typeB \n\x1e_floodlight_variable_data_type:\x8d\x01\xeaA\x89\x01\n4searchads360.googleapis.com/ConversionCustomVariable\x12Qcustomers/{customer_id}/conversionCustomVariables/{conversion_custom_variable_id}B\x9d\x02\n(com.google.ads.searchads360.v0.resourcesB\x1dConversionCustomVariableProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.conversion_custom_variable_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x1dConversionCustomVariableProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_CONVERSIONCUSTOMVARIABLE_FLOODLIGHTCONVERSIONCUSTOMVARIABLEINFO'].fields_by_name['floodlight_variable_type']._loaded_options = None
    _globals['_CONVERSIONCUSTOMVARIABLE_FLOODLIGHTCONVERSIONCUSTOMVARIABLEINFO'].fields_by_name['floodlight_variable_type']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONCUSTOMVARIABLE_FLOODLIGHTCONVERSIONCUSTOMVARIABLEINFO'].fields_by_name['floodlight_variable_data_type']._loaded_options = None
    _globals['_CONVERSIONCUSTOMVARIABLE_FLOODLIGHTCONVERSIONCUSTOMVARIABLEINFO'].fields_by_name['floodlight_variable_data_type']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA6\n4searchads360.googleapis.com/ConversionCustomVariable'
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['id']._loaded_options = None
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['name']._loaded_options = None
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['tag']._loaded_options = None
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['tag']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['owner_customer']._loaded_options = None
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['owner_customer']._serialized_options = b'\xe0A\x03\xfaA&\n$searchads360.googleapis.com/Customer'
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['family']._loaded_options = None
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['family']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['cardinality']._loaded_options = None
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['cardinality']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['floodlight_conversion_custom_variable_info']._loaded_options = None
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['floodlight_conversion_custom_variable_info']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['custom_column_ids']._loaded_options = None
    _globals['_CONVERSIONCUSTOMVARIABLE'].fields_by_name['custom_column_ids']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONCUSTOMVARIABLE']._loaded_options = None
    _globals['_CONVERSIONCUSTOMVARIABLE']._serialized_options = b'\xeaA\x89\x01\n4searchads360.googleapis.com/ConversionCustomVariable\x12Qcustomers/{customer_id}/conversionCustomVariables/{conversion_custom_variable_id}'
    _globals['_CONVERSIONCUSTOMVARIABLE']._serialized_start = 534
    _globals['_CONVERSIONCUSTOMVARIABLE']._serialized_end = 1864
    _globals['_CONVERSIONCUSTOMVARIABLE_FLOODLIGHTCONVERSIONCUSTOMVARIABLEINFO']._serialized_start = 1345
    _globals['_CONVERSIONCUSTOMVARIABLE_FLOODLIGHTCONVERSIONCUSTOMVARIABLEINFO']._serialized_end = 1720