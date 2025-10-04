"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/customer_search_term_insight.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/ads/googleads/v19/resources/customer_search_term_insight.proto\x12"google.ads.googleads.v19.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xba\x02\n\x19CustomerSearchTermInsight\x12Q\n\rresource_name\x18\x01 \x01(\tB:\xe0A\x03\xfaA4\n2googleads.googleapis.com/CustomerSearchTermInsight\x12 \n\x0ecategory_label\x18\x02 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12\x14\n\x02id\x18\x03 \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01:x\xeaAu\n2googleads.googleapis.com/CustomerSearchTermInsight\x12?customers/{customer_id}/customerSearchTermInsights/{cluster_id}B\x11\n\x0f_category_labelB\x05\n\x03_idB\x90\x02\n&com.google.ads.googleads.v19.resourcesB\x1eCustomerSearchTermInsightProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.customer_search_term_insight_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x1eCustomerSearchTermInsightProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_CUSTOMERSEARCHTERMINSIGHT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CUSTOMERSEARCHTERMINSIGHT'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA4\n2googleads.googleapis.com/CustomerSearchTermInsight'
    _globals['_CUSTOMERSEARCHTERMINSIGHT'].fields_by_name['category_label']._loaded_options = None
    _globals['_CUSTOMERSEARCHTERMINSIGHT'].fields_by_name['category_label']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERSEARCHTERMINSIGHT'].fields_by_name['id']._loaded_options = None
    _globals['_CUSTOMERSEARCHTERMINSIGHT'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERSEARCHTERMINSIGHT']._loaded_options = None
    _globals['_CUSTOMERSEARCHTERMINSIGHT']._serialized_options = b'\xeaAu\n2googleads.googleapis.com/CustomerSearchTermInsight\x12?customers/{customer_id}/customerSearchTermInsights/{cluster_id}'
    _globals['_CUSTOMERSEARCHTERMINSIGHT']._serialized_start = 170
    _globals['_CUSTOMERSEARCHTERMINSIGHT']._serialized_end = 484