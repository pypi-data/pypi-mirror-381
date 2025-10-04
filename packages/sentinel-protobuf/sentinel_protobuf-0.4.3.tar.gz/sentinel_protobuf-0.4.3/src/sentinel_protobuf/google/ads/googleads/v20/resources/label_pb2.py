"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/label.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.common import text_label_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_text__label__pb2
from ......google.ads.googleads.v20.enums import label_status_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_label__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/ads/googleads/v20/resources/label.proto\x12"google.ads.googleads.v20.resources\x1a0google/ads/googleads/v20/common/text_label.proto\x1a1google/ads/googleads/v20/enums/label_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xe1\x02\n\x05Label\x12=\n\rresource_name\x18\x01 \x01(\tB&\xe0A\x05\xfaA \n\x1egoogleads.googleapis.com/Label\x12\x14\n\x02id\x18\x06 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x11\n\x04name\x18\x07 \x01(\tH\x01\x88\x01\x01\x12P\n\x06status\x18\x04 \x01(\x0e2;.google.ads.googleads.v20.enums.LabelStatusEnum.LabelStatusB\x03\xe0A\x03\x12>\n\ntext_label\x18\x05 \x01(\x0b2*.google.ads.googleads.v20.common.TextLabel:N\xeaAK\n\x1egoogleads.googleapis.com/Label\x12)customers/{customer_id}/labels/{label_id}B\x05\n\x03_idB\x07\n\x05_nameB\xfc\x01\n&com.google.ads.googleads.v20.resourcesB\nLabelProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.label_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\nLabelProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_LABEL'].fields_by_name['resource_name']._loaded_options = None
    _globals['_LABEL'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA \n\x1egoogleads.googleapis.com/Label'
    _globals['_LABEL'].fields_by_name['id']._loaded_options = None
    _globals['_LABEL'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_LABEL'].fields_by_name['status']._loaded_options = None
    _globals['_LABEL'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_LABEL']._loaded_options = None
    _globals['_LABEL']._serialized_options = b'\xeaAK\n\x1egoogleads.googleapis.com/Label\x12)customers/{customer_id}/labels/{label_id}'
    _globals['_LABEL']._serialized_start = 248
    _globals['_LABEL']._serialized_end = 601