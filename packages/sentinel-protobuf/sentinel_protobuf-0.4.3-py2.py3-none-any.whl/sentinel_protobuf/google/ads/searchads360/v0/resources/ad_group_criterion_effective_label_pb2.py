"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/ad_group_criterion_effective_label.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nMgoogle/ads/searchads360/v0/resources/ad_group_criterion_effective_label.proto\x12$google.ads.searchads360.v0.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xd2\x04\n\x1eAdGroupCriterionEffectiveLabel\x12Y\n\rresource_name\x18\x01 \x01(\tBB\xe0A\x05\xfaA<\n:searchads360.googleapis.com/AdGroupCriterionEffectiveLabel\x12U\n\x12ad_group_criterion\x18\x02 \x01(\tB4\xe0A\x05\xfaA.\n,searchads360.googleapis.com/AdGroupCriterionH\x00\x88\x01\x01\x12=\n\x05label\x18\x03 \x01(\tB)\xe0A\x05\xfaA#\n!searchads360.googleapis.com/LabelH\x01\x88\x01\x01\x12#\n\x11owner_customer_id\x18\x04 \x01(\x03B\x03\xe0A\x03H\x02\x88\x01\x01:\xe2\x01\xeaA\xde\x01\n:searchads360.googleapis.com/AdGroupCriterionEffectiveLabel\x12_customers/{customer_id}/adGroupCriterionEffectiveLabels/{ad_group_id}~{criterion_id}~{label_id}*\x1fadGroupCriterionEffectiveLabels2\x1eadGroupCriterionEffectiveLabelB\x15\n\x13_ad_group_criterionB\x08\n\x06_labelB\x14\n\x12_owner_customer_idB\xa3\x02\n(com.google.ads.searchads360.v0.resourcesB#AdGroupCriterionEffectiveLabelProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.ad_group_criterion_effective_label_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB#AdGroupCriterionEffectiveLabelProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_ADGROUPCRITERIONEFFECTIVELABEL'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADGROUPCRITERIONEFFECTIVELABEL'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA<\n:searchads360.googleapis.com/AdGroupCriterionEffectiveLabel'
    _globals['_ADGROUPCRITERIONEFFECTIVELABEL'].fields_by_name['ad_group_criterion']._loaded_options = None
    _globals['_ADGROUPCRITERIONEFFECTIVELABEL'].fields_by_name['ad_group_criterion']._serialized_options = b'\xe0A\x05\xfaA.\n,searchads360.googleapis.com/AdGroupCriterion'
    _globals['_ADGROUPCRITERIONEFFECTIVELABEL'].fields_by_name['label']._loaded_options = None
    _globals['_ADGROUPCRITERIONEFFECTIVELABEL'].fields_by_name['label']._serialized_options = b'\xe0A\x05\xfaA#\n!searchads360.googleapis.com/Label'
    _globals['_ADGROUPCRITERIONEFFECTIVELABEL'].fields_by_name['owner_customer_id']._loaded_options = None
    _globals['_ADGROUPCRITERIONEFFECTIVELABEL'].fields_by_name['owner_customer_id']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERIONEFFECTIVELABEL']._loaded_options = None
    _globals['_ADGROUPCRITERIONEFFECTIVELABEL']._serialized_options = b'\xeaA\xde\x01\n:searchads360.googleapis.com/AdGroupCriterionEffectiveLabel\x12_customers/{customer_id}/adGroupCriterionEffectiveLabels/{ad_group_id}~{criterion_id}~{label_id}*\x1fadGroupCriterionEffectiveLabels2\x1eadGroupCriterionEffectiveLabel'
    _globals['_ADGROUPCRITERIONEFFECTIVELABEL']._serialized_start = 180
    _globals['_ADGROUPCRITERIONEFFECTIVELABEL']._serialized_end = 774