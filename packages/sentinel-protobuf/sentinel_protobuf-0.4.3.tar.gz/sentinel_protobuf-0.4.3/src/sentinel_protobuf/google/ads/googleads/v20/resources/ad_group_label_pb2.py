"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/ad_group_label.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/ads/googleads/v20/resources/ad_group_label.proto\x12"google.ads.googleads.v20.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xd4\x02\n\x0cAdGroupLabel\x12D\n\rresource_name\x18\x01 \x01(\tB-\xe0A\x05\xfaA\'\n%googleads.googleapis.com/AdGroupLabel\x12?\n\x08ad_group\x18\x04 \x01(\tB(\xe0A\x05\xfaA"\n googleads.googleapis.com/AdGroupH\x00\x88\x01\x01\x12:\n\x05label\x18\x05 \x01(\tB&\xe0A\x05\xfaA \n\x1egoogleads.googleapis.com/LabelH\x01\x88\x01\x01:j\xeaAg\n%googleads.googleapis.com/AdGroupLabel\x12>customers/{customer_id}/adGroupLabels/{ad_group_id}~{label_id}B\x0b\n\t_ad_groupB\x08\n\x06_labelB\x83\x02\n&com.google.ads.googleads.v20.resourcesB\x11AdGroupLabelProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.ad_group_label_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x11AdGroupLabelProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_ADGROUPLABEL'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADGROUPLABEL'].fields_by_name['resource_name']._serialized_options = b"\xe0A\x05\xfaA'\n%googleads.googleapis.com/AdGroupLabel"
    _globals['_ADGROUPLABEL'].fields_by_name['ad_group']._loaded_options = None
    _globals['_ADGROUPLABEL'].fields_by_name['ad_group']._serialized_options = b'\xe0A\x05\xfaA"\n googleads.googleapis.com/AdGroup'
    _globals['_ADGROUPLABEL'].fields_by_name['label']._loaded_options = None
    _globals['_ADGROUPLABEL'].fields_by_name['label']._serialized_options = b'\xe0A\x05\xfaA \n\x1egoogleads.googleapis.com/Label'
    _globals['_ADGROUPLABEL']._loaded_options = None
    _globals['_ADGROUPLABEL']._serialized_options = b'\xeaAg\n%googleads.googleapis.com/AdGroupLabel\x12>customers/{customer_id}/adGroupLabels/{ad_group_id}~{label_id}'
    _globals['_ADGROUPLABEL']._serialized_start = 156
    _globals['_ADGROUPLABEL']._serialized_end = 496