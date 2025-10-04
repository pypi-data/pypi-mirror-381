"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/ad_parameter.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/ads/googleads/v19/resources/ad_parameter.proto\x12"google.ads.googleads.v19.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa4\x03\n\x0bAdParameter\x12C\n\rresource_name\x18\x01 \x01(\tB,\xe0A\x05\xfaA&\n$googleads.googleapis.com/AdParameter\x12R\n\x12ad_group_criterion\x18\x05 \x01(\tB1\xe0A\x05\xfaA+\n)googleads.googleapis.com/AdGroupCriterionH\x00\x88\x01\x01\x12!\n\x0fparameter_index\x18\x06 \x01(\x03B\x03\xe0A\x05H\x01\x88\x01\x01\x12\x1b\n\x0einsertion_text\x18\x07 \x01(\tH\x02\x88\x01\x01:~\xeaA{\n$googleads.googleapis.com/AdParameter\x12Scustomers/{customer_id}/adParameters/{ad_group_id}~{criterion_id}~{parameter_index}B\x15\n\x13_ad_group_criterionB\x12\n\x10_parameter_indexB\x11\n\x0f_insertion_textB\x82\x02\n&com.google.ads.googleads.v19.resourcesB\x10AdParameterProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.ad_parameter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x10AdParameterProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_ADPARAMETER'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADPARAMETER'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA&\n$googleads.googleapis.com/AdParameter'
    _globals['_ADPARAMETER'].fields_by_name['ad_group_criterion']._loaded_options = None
    _globals['_ADPARAMETER'].fields_by_name['ad_group_criterion']._serialized_options = b'\xe0A\x05\xfaA+\n)googleads.googleapis.com/AdGroupCriterion'
    _globals['_ADPARAMETER'].fields_by_name['parameter_index']._loaded_options = None
    _globals['_ADPARAMETER'].fields_by_name['parameter_index']._serialized_options = b'\xe0A\x05'
    _globals['_ADPARAMETER']._loaded_options = None
    _globals['_ADPARAMETER']._serialized_options = b'\xeaA{\n$googleads.googleapis.com/AdParameter\x12Scustomers/{customer_id}/adParameters/{ad_group_id}~{criterion_id}~{parameter_index}'
    _globals['_ADPARAMETER']._serialized_start = 154
    _globals['_ADPARAMETER']._serialized_end = 574