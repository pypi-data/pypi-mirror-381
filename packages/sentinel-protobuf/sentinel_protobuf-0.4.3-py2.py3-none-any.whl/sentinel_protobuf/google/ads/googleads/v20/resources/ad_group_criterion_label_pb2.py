"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/ad_group_criterion_label.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/ads/googleads/v20/resources/ad_group_criterion_label.proto\x12"google.ads.googleads.v20.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa6\x03\n\x15AdGroupCriterionLabel\x12M\n\rresource_name\x18\x01 \x01(\tB6\xe0A\x05\xfaA0\n.googleads.googleapis.com/AdGroupCriterionLabel\x12R\n\x12ad_group_criterion\x18\x04 \x01(\tB1\xe0A\x05\xfaA+\n)googleads.googleapis.com/AdGroupCriterionH\x00\x88\x01\x01\x12:\n\x05label\x18\x05 \x01(\tB&\xe0A\x05\xfaA \n\x1egoogleads.googleapis.com/LabelH\x01\x88\x01\x01:\x8c\x01\xeaA\x88\x01\n.googleads.googleapis.com/AdGroupCriterionLabel\x12Vcustomers/{customer_id}/adGroupCriterionLabels/{ad_group_id}~{criterion_id}~{label_id}B\x15\n\x13_ad_group_criterionB\x08\n\x06_labelB\x8c\x02\n&com.google.ads.googleads.v20.resourcesB\x1aAdGroupCriterionLabelProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.ad_group_criterion_label_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x1aAdGroupCriterionLabelProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_ADGROUPCRITERIONLABEL'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADGROUPCRITERIONLABEL'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA0\n.googleads.googleapis.com/AdGroupCriterionLabel'
    _globals['_ADGROUPCRITERIONLABEL'].fields_by_name['ad_group_criterion']._loaded_options = None
    _globals['_ADGROUPCRITERIONLABEL'].fields_by_name['ad_group_criterion']._serialized_options = b'\xe0A\x05\xfaA+\n)googleads.googleapis.com/AdGroupCriterion'
    _globals['_ADGROUPCRITERIONLABEL'].fields_by_name['label']._loaded_options = None
    _globals['_ADGROUPCRITERIONLABEL'].fields_by_name['label']._serialized_options = b'\xe0A\x05\xfaA \n\x1egoogleads.googleapis.com/Label'
    _globals['_ADGROUPCRITERIONLABEL']._loaded_options = None
    _globals['_ADGROUPCRITERIONLABEL']._serialized_options = b'\xeaA\x88\x01\n.googleads.googleapis.com/AdGroupCriterionLabel\x12Vcustomers/{customer_id}/adGroupCriterionLabels/{ad_group_id}~{criterion_id}~{label_id}'
    _globals['_ADGROUPCRITERIONLABEL']._serialized_start = 166
    _globals['_ADGROUPCRITERIONLABEL']._serialized_end = 588