"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/support/v2beta/feed_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.support.v2beta import feed_item_pb2 as google_dot_cloud_dot_support_dot_v2beta_dot_feed__item__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/support/v2beta/feed_service.proto\x12\x1bgoogle.cloud.support.v2beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a+google/cloud/support/v2beta/feed_item.proto"\x93\x01\n\x0fShowFeedRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case\x12\x15\n\x08order_by\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01"f\n\x10ShowFeedResponse\x129\n\nfeed_items\x18\x01 \x03(\x0b2%.google.cloud.support.v2beta.FeedItem\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xbc\x02\n\x0bFeedService\x12\xdb\x01\n\x08ShowFeed\x12,.google.cloud.support.v2beta.ShowFeedRequest\x1a-.google.cloud.support.v2beta.ShowFeedResponse"r\xdaA\x06parent\x82\xd3\xe4\x93\x02c\x12,/v2beta/{parent=projects/*/cases/*}:showFeedZ3\x121/v2beta/{parent=organizations/*/cases/*}:showFeed\x1aO\xcaA\x1bcloudsupport.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xcd\x01\n\x1fcom.google.cloud.support.v2betaB\x10FeedServiceProtoP\x01Z9cloud.google.com/go/support/apiv2beta/supportpb;supportpb\xaa\x02\x1bGoogle.Cloud.Support.V2Beta\xca\x02\x1bGoogle\\Cloud\\Support\\V2beta\xea\x02\x1eGoogle::Cloud::Support::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.support.v2beta.feed_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.support.v2betaB\x10FeedServiceProtoP\x01Z9cloud.google.com/go/support/apiv2beta/supportpb;supportpb\xaa\x02\x1bGoogle.Cloud.Support.V2Beta\xca\x02\x1bGoogle\\Cloud\\Support\\V2beta\xea\x02\x1eGoogle::Cloud::Support::V2beta'
    _globals['_SHOWFEEDREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_SHOWFEEDREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case'
    _globals['_SHOWFEEDREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_SHOWFEEDREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_SHOWFEEDREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_SHOWFEEDREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_SHOWFEEDREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_SHOWFEEDREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_FEEDSERVICE']._loaded_options = None
    _globals['_FEEDSERVICE']._serialized_options = b'\xcaA\x1bcloudsupport.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_FEEDSERVICE'].methods_by_name['ShowFeed']._loaded_options = None
    _globals['_FEEDSERVICE'].methods_by_name['ShowFeed']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02c\x12,/v2beta/{parent=projects/*/cases/*}:showFeedZ3\x121/v2beta/{parent=organizations/*/cases/*}:showFeed'
    _globals['_SHOWFEEDREQUEST']._serialized_start = 240
    _globals['_SHOWFEEDREQUEST']._serialized_end = 387
    _globals['_SHOWFEEDRESPONSE']._serialized_start = 389
    _globals['_SHOWFEEDRESPONSE']._serialized_end = 491
    _globals['_FEEDSERVICE']._serialized_start = 494
    _globals['_FEEDSERVICE']._serialized_end = 810