"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/ad_group_effective_label.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/ads/searchads360/v0/resources/ad_group_effective_label.proto\x12$google.ads.searchads360.v0.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xf0\x03\n\x15AdGroupEffectiveLabel\x12P\n\rresource_name\x18\x01 \x01(\tB9\xe0A\x05\xfaA3\n1searchads360.googleapis.com/AdGroupEffectiveLabel\x12B\n\x08ad_group\x18\x02 \x01(\tB+\xe0A\x05\xfaA%\n#searchads360.googleapis.com/AdGroupH\x00\x88\x01\x01\x12=\n\x05label\x18\x03 \x01(\tB)\xe0A\x05\xfaA#\n!searchads360.googleapis.com/LabelH\x01\x88\x01\x01\x12#\n\x11owner_customer_id\x18\x04 \x01(\x03B\x03\xe0A\x03H\x02\x88\x01\x01:\xaf\x01\xeaA\xab\x01\n1searchads360.googleapis.com/AdGroupEffectiveLabel\x12Gcustomers/{customer_id}/adGroupEffectiveLabels/{ad_group_id}~{label_id}*\x16adGroupEffectiveLabels2\x15adGroupEffectiveLabelB\x0b\n\t_ad_groupB\x08\n\x06_labelB\x14\n\x12_owner_customer_idB\x9a\x02\n(com.google.ads.searchads360.v0.resourcesB\x1aAdGroupEffectiveLabelProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.ad_group_effective_label_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x1aAdGroupEffectiveLabelProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_ADGROUPEFFECTIVELABEL'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADGROUPEFFECTIVELABEL'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA3\n1searchads360.googleapis.com/AdGroupEffectiveLabel'
    _globals['_ADGROUPEFFECTIVELABEL'].fields_by_name['ad_group']._loaded_options = None
    _globals['_ADGROUPEFFECTIVELABEL'].fields_by_name['ad_group']._serialized_options = b'\xe0A\x05\xfaA%\n#searchads360.googleapis.com/AdGroup'
    _globals['_ADGROUPEFFECTIVELABEL'].fields_by_name['label']._loaded_options = None
    _globals['_ADGROUPEFFECTIVELABEL'].fields_by_name['label']._serialized_options = b'\xe0A\x05\xfaA#\n!searchads360.googleapis.com/Label'
    _globals['_ADGROUPEFFECTIVELABEL'].fields_by_name['owner_customer_id']._loaded_options = None
    _globals['_ADGROUPEFFECTIVELABEL'].fields_by_name['owner_customer_id']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPEFFECTIVELABEL']._loaded_options = None
    _globals['_ADGROUPEFFECTIVELABEL']._serialized_options = b'\xeaA\xab\x01\n1searchads360.googleapis.com/AdGroupEffectiveLabel\x12Gcustomers/{customer_id}/adGroupEffectiveLabels/{ad_group_id}~{label_id}*\x16adGroupEffectiveLabels2\x15adGroupEffectiveLabel'
    _globals['_ADGROUPEFFECTIVELABEL']._serialized_start = 170
    _globals['_ADGROUPEFFECTIVELABEL']._serialized_end = 666