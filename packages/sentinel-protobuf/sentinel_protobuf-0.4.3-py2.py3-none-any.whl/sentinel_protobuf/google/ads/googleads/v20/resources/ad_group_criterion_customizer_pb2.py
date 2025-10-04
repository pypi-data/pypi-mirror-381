"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/ad_group_criterion_customizer.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.common import customizer_value_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_customizer__value__pb2
from ......google.ads.googleads.v20.enums import customizer_value_status_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_customizer__value__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFgoogle/ads/googleads/v20/resources/ad_group_criterion_customizer.proto\x12"google.ads.googleads.v20.resources\x1a6google/ads/googleads/v20/common/customizer_value.proto\x1a<google/ads/googleads/v20/enums/customizer_value_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x86\x05\n\x1aAdGroupCriterionCustomizer\x12R\n\rresource_name\x18\x01 \x01(\tB;\xe0A\x05\xfaA5\n3googleads.googleapis.com/AdGroupCriterionCustomizer\x12R\n\x12ad_group_criterion\x18\x02 \x01(\tB1\xe0A\x05\xfaA+\n)googleads.googleapis.com/AdGroupCriterionH\x00\x88\x01\x01\x12U\n\x14customizer_attribute\x18\x03 \x01(\tB7\xe0A\x02\xe0A\x05\xfaA.\n,googleads.googleapis.com/CustomizerAttribute\x12d\n\x06status\x18\x04 \x01(\x0e2O.google.ads.googleads.v20.enums.CustomizerValueStatusEnum.CustomizerValueStatusB\x03\xe0A\x03\x12D\n\x05value\x18\x05 \x01(\x0b20.google.ads.googleads.v20.common.CustomizerValueB\x03\xe0A\x02:\xa5\x01\xeaA\xa1\x01\n3googleads.googleapis.com/AdGroupCriterionCustomizer\x12jcustomers/{customer_id}/adGroupCriterionCustomizers/{ad_group_id}~{criterion_id}~{customizer_attribute_id}B\x15\n\x13_ad_group_criterionB\x91\x02\n&com.google.ads.googleads.v20.resourcesB\x1fAdGroupCriterionCustomizerProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.ad_group_criterion_customizer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x1fAdGroupCriterionCustomizerProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_ADGROUPCRITERIONCUSTOMIZER'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADGROUPCRITERIONCUSTOMIZER'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA5\n3googleads.googleapis.com/AdGroupCriterionCustomizer'
    _globals['_ADGROUPCRITERIONCUSTOMIZER'].fields_by_name['ad_group_criterion']._loaded_options = None
    _globals['_ADGROUPCRITERIONCUSTOMIZER'].fields_by_name['ad_group_criterion']._serialized_options = b'\xe0A\x05\xfaA+\n)googleads.googleapis.com/AdGroupCriterion'
    _globals['_ADGROUPCRITERIONCUSTOMIZER'].fields_by_name['customizer_attribute']._loaded_options = None
    _globals['_ADGROUPCRITERIONCUSTOMIZER'].fields_by_name['customizer_attribute']._serialized_options = b'\xe0A\x02\xe0A\x05\xfaA.\n,googleads.googleapis.com/CustomizerAttribute'
    _globals['_ADGROUPCRITERIONCUSTOMIZER'].fields_by_name['status']._loaded_options = None
    _globals['_ADGROUPCRITERIONCUSTOMIZER'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERIONCUSTOMIZER'].fields_by_name['value']._loaded_options = None
    _globals['_ADGROUPCRITERIONCUSTOMIZER'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_ADGROUPCRITERIONCUSTOMIZER']._loaded_options = None
    _globals['_ADGROUPCRITERIONCUSTOMIZER']._serialized_options = b'\xeaA\xa1\x01\n3googleads.googleapis.com/AdGroupCriterionCustomizer\x12jcustomers/{customer_id}/adGroupCriterionCustomizers/{ad_group_id}~{criterion_id}~{customizer_attribute_id}'
    _globals['_ADGROUPCRITERIONCUSTOMIZER']._serialized_start = 289
    _globals['_ADGROUPCRITERIONCUSTOMIZER']._serialized_end = 935