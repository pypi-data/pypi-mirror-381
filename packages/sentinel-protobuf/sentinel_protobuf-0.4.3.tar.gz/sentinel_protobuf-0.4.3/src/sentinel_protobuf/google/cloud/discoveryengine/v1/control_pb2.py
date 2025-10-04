"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/control.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import common_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/discoveryengine/v1/control.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/discoveryengine/v1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xdc\x02\n\tCondition\x12I\n\x0bquery_terms\x18\x02 \x03(\x0b24.google.cloud.discoveryengine.v1.Condition.QueryTerm\x12O\n\x11active_time_range\x18\x03 \x03(\x0b24.google.cloud.discoveryengine.v1.Condition.TimeRange\x12\x18\n\x0bquery_regex\x18\x04 \x01(\tB\x03\xe0A\x01\x1a.\n\tQueryTerm\x12\r\n\x05value\x18\x01 \x01(\t\x12\x12\n\nfull_match\x18\x02 \x01(\x08\x1ai\n\tTimeRange\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xb8\x12\n\x07Control\x12L\n\x0cboost_action\x18\x06 \x01(\x0b24.google.cloud.discoveryengine.v1.Control.BoostActionH\x00\x12N\n\rfilter_action\x18\x07 \x01(\x0b25.google.cloud.discoveryengine.v1.Control.FilterActionH\x00\x12R\n\x0fredirect_action\x18\t \x01(\x0b27.google.cloud.discoveryengine.v1.Control.RedirectActionH\x00\x12R\n\x0fsynonyms_action\x18\n \x01(\x0b27.google.cloud.discoveryengine.v1.Control.SynonymsActionH\x00\x12P\n\x0epromote_action\x18\x0f \x01(\x0b26.google.cloud.discoveryengine.v1.Control.PromoteActionH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12*\n\x1dassociated_serving_config_ids\x18\x03 \x03(\tB\x03\xe0A\x03\x12L\n\rsolution_type\x18\x04 \x01(\x0e2-.google.cloud.discoveryengine.v1.SolutionTypeB\x06\xe0A\x02\xe0A\x05\x12A\n\tuse_cases\x18\x08 \x03(\x0e2..google.cloud.discoveryengine.v1.SearchUseCase\x12>\n\nconditions\x18\x05 \x03(\x0b2*.google.cloud.discoveryengine.v1.Condition\x1a\x9b\x07\n\x0bBoostAction\x12\x1a\n\x0bfixed_boost\x18\x04 \x01(\x02B\x03\xe0A\x01H\x00\x12t\n\x18interpolation_boost_spec\x18\x05 \x01(\x0b2K.google.cloud.discoveryengine.v1.Control.BoostAction.InterpolationBoostSpecB\x03\xe0A\x01H\x00\x12\x11\n\x05boost\x18\x01 \x01(\x02B\x02\x18\x01\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x02\x12D\n\ndata_store\x18\x03 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x1a\xfd\x04\n\x16InterpolationBoostSpec\x12\x17\n\nfield_name\x18\x01 \x01(\tB\x03\xe0A\x01\x12v\n\x0eattribute_type\x18\x02 \x01(\x0e2Y.google.cloud.discoveryengine.v1.Control.BoostAction.InterpolationBoostSpec.AttributeTypeB\x03\xe0A\x01\x12~\n\x12interpolation_type\x18\x03 \x01(\x0e2].google.cloud.discoveryengine.v1.Control.BoostAction.InterpolationBoostSpec.InterpolationTypeB\x03\xe0A\x01\x12u\n\x0econtrol_points\x18\x04 \x03(\x0b2X.google.cloud.discoveryengine.v1.Control.BoostAction.InterpolationBoostSpec.ControlPointB\x03\xe0A\x01\x1aG\n\x0cControlPoint\x12\x1c\n\x0fattribute_value\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cboost_amount\x18\x02 \x01(\x02B\x03\xe0A\x01"M\n\rAttributeType\x12\x1e\n\x1aATTRIBUTE_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tNUMERICAL\x10\x01\x12\r\n\tFRESHNESS\x10\x02"C\n\x11InterpolationType\x12"\n\x1eINTERPOLATION_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06LINEAR\x10\x01B\x0c\n\nboost_spec\x1ai\n\x0cFilterAction\x12\x13\n\x06filter\x18\x01 \x01(\tB\x03\xe0A\x02\x12D\n\ndata_store\x18\x02 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x1a+\n\x0eRedirectAction\x12\x19\n\x0credirect_uri\x18\x01 \x01(\tB\x03\xe0A\x02\x1a"\n\x0eSynonymsAction\x12\x10\n\x08synonyms\x18\x01 \x03(\t\x1a\xaf\x01\n\rPromoteAction\x12D\n\ndata_store\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x12X\n\x15search_link_promotion\x18\x02 \x01(\x0b24.google.cloud.discoveryengine.v1.SearchLinkPromotionB\x03\xe0A\x02:\xd3\x02\xeaA\xcf\x02\n&discoveryengine.googleapis.com/Control\x12Rprojects/{project}/locations/{location}/dataStores/{data_store}/controls/{control}\x12kprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/controls/{control}\x12dprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}/controls/{control}B\x08\n\x06actionB\xff\x01\n#com.google.cloud.discoveryengine.v1B\x0cControlProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.control_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x0cControlProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_CONDITION'].fields_by_name['query_regex']._loaded_options = None
    _globals['_CONDITION'].fields_by_name['query_regex']._serialized_options = b'\xe0A\x01'
    _globals['_CONTROL_BOOSTACTION_INTERPOLATIONBOOSTSPEC_CONTROLPOINT'].fields_by_name['attribute_value']._loaded_options = None
    _globals['_CONTROL_BOOSTACTION_INTERPOLATIONBOOSTSPEC_CONTROLPOINT'].fields_by_name['attribute_value']._serialized_options = b'\xe0A\x01'
    _globals['_CONTROL_BOOSTACTION_INTERPOLATIONBOOSTSPEC_CONTROLPOINT'].fields_by_name['boost_amount']._loaded_options = None
    _globals['_CONTROL_BOOSTACTION_INTERPOLATIONBOOSTSPEC_CONTROLPOINT'].fields_by_name['boost_amount']._serialized_options = b'\xe0A\x01'
    _globals['_CONTROL_BOOSTACTION_INTERPOLATIONBOOSTSPEC'].fields_by_name['field_name']._loaded_options = None
    _globals['_CONTROL_BOOSTACTION_INTERPOLATIONBOOSTSPEC'].fields_by_name['field_name']._serialized_options = b'\xe0A\x01'
    _globals['_CONTROL_BOOSTACTION_INTERPOLATIONBOOSTSPEC'].fields_by_name['attribute_type']._loaded_options = None
    _globals['_CONTROL_BOOSTACTION_INTERPOLATIONBOOSTSPEC'].fields_by_name['attribute_type']._serialized_options = b'\xe0A\x01'
    _globals['_CONTROL_BOOSTACTION_INTERPOLATIONBOOSTSPEC'].fields_by_name['interpolation_type']._loaded_options = None
    _globals['_CONTROL_BOOSTACTION_INTERPOLATIONBOOSTSPEC'].fields_by_name['interpolation_type']._serialized_options = b'\xe0A\x01'
    _globals['_CONTROL_BOOSTACTION_INTERPOLATIONBOOSTSPEC'].fields_by_name['control_points']._loaded_options = None
    _globals['_CONTROL_BOOSTACTION_INTERPOLATIONBOOSTSPEC'].fields_by_name['control_points']._serialized_options = b'\xe0A\x01'
    _globals['_CONTROL_BOOSTACTION'].fields_by_name['fixed_boost']._loaded_options = None
    _globals['_CONTROL_BOOSTACTION'].fields_by_name['fixed_boost']._serialized_options = b'\xe0A\x01'
    _globals['_CONTROL_BOOSTACTION'].fields_by_name['interpolation_boost_spec']._loaded_options = None
    _globals['_CONTROL_BOOSTACTION'].fields_by_name['interpolation_boost_spec']._serialized_options = b'\xe0A\x01'
    _globals['_CONTROL_BOOSTACTION'].fields_by_name['boost']._loaded_options = None
    _globals['_CONTROL_BOOSTACTION'].fields_by_name['boost']._serialized_options = b'\x18\x01'
    _globals['_CONTROL_BOOSTACTION'].fields_by_name['filter']._loaded_options = None
    _globals['_CONTROL_BOOSTACTION'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_CONTROL_BOOSTACTION'].fields_by_name['data_store']._loaded_options = None
    _globals['_CONTROL_BOOSTACTION'].fields_by_name['data_store']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_CONTROL_FILTERACTION'].fields_by_name['filter']._loaded_options = None
    _globals['_CONTROL_FILTERACTION'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_CONTROL_FILTERACTION'].fields_by_name['data_store']._loaded_options = None
    _globals['_CONTROL_FILTERACTION'].fields_by_name['data_store']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_CONTROL_REDIRECTACTION'].fields_by_name['redirect_uri']._loaded_options = None
    _globals['_CONTROL_REDIRECTACTION'].fields_by_name['redirect_uri']._serialized_options = b'\xe0A\x02'
    _globals['_CONTROL_PROMOTEACTION'].fields_by_name['data_store']._loaded_options = None
    _globals['_CONTROL_PROMOTEACTION'].fields_by_name['data_store']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_CONTROL_PROMOTEACTION'].fields_by_name['search_link_promotion']._loaded_options = None
    _globals['_CONTROL_PROMOTEACTION'].fields_by_name['search_link_promotion']._serialized_options = b'\xe0A\x02'
    _globals['_CONTROL'].fields_by_name['name']._loaded_options = None
    _globals['_CONTROL'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_CONTROL'].fields_by_name['display_name']._loaded_options = None
    _globals['_CONTROL'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_CONTROL'].fields_by_name['associated_serving_config_ids']._loaded_options = None
    _globals['_CONTROL'].fields_by_name['associated_serving_config_ids']._serialized_options = b'\xe0A\x03'
    _globals['_CONTROL'].fields_by_name['solution_type']._loaded_options = None
    _globals['_CONTROL'].fields_by_name['solution_type']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_CONTROL']._loaded_options = None
    _globals['_CONTROL']._serialized_options = b'\xeaA\xcf\x02\n&discoveryengine.googleapis.com/Control\x12Rprojects/{project}/locations/{location}/dataStores/{data_store}/controls/{control}\x12kprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/controls/{control}\x12dprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}/controls/{control}'
    _globals['_CONDITION']._serialized_start = 222
    _globals['_CONDITION']._serialized_end = 570
    _globals['_CONDITION_QUERYTERM']._serialized_start = 417
    _globals['_CONDITION_QUERYTERM']._serialized_end = 463
    _globals['_CONDITION_TIMERANGE']._serialized_start = 465
    _globals['_CONDITION_TIMERANGE']._serialized_end = 570
    _globals['_CONTROL']._serialized_start = 573
    _globals['_CONTROL']._serialized_end = 2933
    _globals['_CONTROL_BOOSTACTION']._serialized_start = 1292
    _globals['_CONTROL_BOOSTACTION']._serialized_end = 2215
    _globals['_CONTROL_BOOSTACTION_INTERPOLATIONBOOSTSPEC']._serialized_start = 1564
    _globals['_CONTROL_BOOSTACTION_INTERPOLATIONBOOSTSPEC']._serialized_end = 2201
    _globals['_CONTROL_BOOSTACTION_INTERPOLATIONBOOSTSPEC_CONTROLPOINT']._serialized_start = 1982
    _globals['_CONTROL_BOOSTACTION_INTERPOLATIONBOOSTSPEC_CONTROLPOINT']._serialized_end = 2053
    _globals['_CONTROL_BOOSTACTION_INTERPOLATIONBOOSTSPEC_ATTRIBUTETYPE']._serialized_start = 2055
    _globals['_CONTROL_BOOSTACTION_INTERPOLATIONBOOSTSPEC_ATTRIBUTETYPE']._serialized_end = 2132
    _globals['_CONTROL_BOOSTACTION_INTERPOLATIONBOOSTSPEC_INTERPOLATIONTYPE']._serialized_start = 2134
    _globals['_CONTROL_BOOSTACTION_INTERPOLATIONBOOSTSPEC_INTERPOLATIONTYPE']._serialized_end = 2201
    _globals['_CONTROL_FILTERACTION']._serialized_start = 2217
    _globals['_CONTROL_FILTERACTION']._serialized_end = 2322
    _globals['_CONTROL_REDIRECTACTION']._serialized_start = 2324
    _globals['_CONTROL_REDIRECTACTION']._serialized_end = 2367
    _globals['_CONTROL_SYNONYMSACTION']._serialized_start = 2369
    _globals['_CONTROL_SYNONYMSACTION']._serialized_end = 2403
    _globals['_CONTROL_PROMOTEACTION']._serialized_start = 2406
    _globals['_CONTROL_PROMOTEACTION']._serialized_end = 2581