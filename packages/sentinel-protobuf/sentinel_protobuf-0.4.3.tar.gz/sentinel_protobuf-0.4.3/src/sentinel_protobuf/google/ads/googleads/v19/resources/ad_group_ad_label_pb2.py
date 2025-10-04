"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/ad_group_ad_label.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/ads/googleads/v19/resources/ad_group_ad_label.proto\x12"google.ads.googleads.v19.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xec\x02\n\x0eAdGroupAdLabel\x12F\n\rresource_name\x18\x01 \x01(\tB/\xe0A\x05\xfaA)\n\'googleads.googleapis.com/AdGroupAdLabel\x12D\n\x0bad_group_ad\x18\x04 \x01(\tB*\xe0A\x05\xfaA$\n"googleads.googleapis.com/AdGroupAdH\x00\x88\x01\x01\x12:\n\x05label\x18\x05 \x01(\tB&\xe0A\x05\xfaA \n\x1egoogleads.googleapis.com/LabelH\x01\x88\x01\x01:v\xeaAs\n\'googleads.googleapis.com/AdGroupAdLabel\x12Hcustomers/{customer_id}/adGroupAdLabels/{ad_group_id}~{ad_id}~{label_id}B\x0e\n\x0c_ad_group_adB\x08\n\x06_labelB\x85\x02\n&com.google.ads.googleads.v19.resourcesB\x13AdGroupAdLabelProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.ad_group_ad_label_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x13AdGroupAdLabelProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_ADGROUPADLABEL'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADGROUPADLABEL'].fields_by_name['resource_name']._serialized_options = b"\xe0A\x05\xfaA)\n'googleads.googleapis.com/AdGroupAdLabel"
    _globals['_ADGROUPADLABEL'].fields_by_name['ad_group_ad']._loaded_options = None
    _globals['_ADGROUPADLABEL'].fields_by_name['ad_group_ad']._serialized_options = b'\xe0A\x05\xfaA$\n"googleads.googleapis.com/AdGroupAd'
    _globals['_ADGROUPADLABEL'].fields_by_name['label']._loaded_options = None
    _globals['_ADGROUPADLABEL'].fields_by_name['label']._serialized_options = b'\xe0A\x05\xfaA \n\x1egoogleads.googleapis.com/Label'
    _globals['_ADGROUPADLABEL']._loaded_options = None
    _globals['_ADGROUPADLABEL']._serialized_options = b"\xeaAs\n'googleads.googleapis.com/AdGroupAdLabel\x12Hcustomers/{customer_id}/adGroupAdLabels/{ad_group_id}~{ad_id}~{label_id}"
    _globals['_ADGROUPADLABEL']._serialized_start = 159
    _globals['_ADGROUPADLABEL']._serialized_end = 523