"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/gen_ai_cache_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import cached_content_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_cached__content__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/aiplatform/v1beta1/gen_ai_cache_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a4google/cloud/aiplatform/v1beta1/cached_content.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xaa\x01\n\x1aCreateCachedContentRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\x12\'aiplatform.googleapis.com/CachedContent\x12K\n\x0ecached_content\x18\x02 \x01(\x0b2..google.cloud.aiplatform.v1beta1.CachedContentB\x03\xe0A\x02"X\n\x17GetCachedContentRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'aiplatform.googleapis.com/CachedContent"\x9f\x01\n\x1aUpdateCachedContentRequest\x12K\n\x0ecached_content\x18\x01 \x01(\x0b2..google.cloud.aiplatform.v1beta1.CachedContentB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"[\n\x1aDeleteCachedContentRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'aiplatform.googleapis.com/CachedContent"\x8d\x01\n\x19ListCachedContentsRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\x12\'aiplatform.googleapis.com/CachedContent\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"~\n\x1aListCachedContentsResponse\x12G\n\x0fcached_contents\x18\x01 \x03(\x0b2..google.cloud.aiplatform.v1beta1.CachedContent\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xa8\t\n\x11GenAiCacheService\x12\xeb\x01\n\x13CreateCachedContent\x12;.google.cloud.aiplatform.v1beta1.CreateCachedContentRequest\x1a..google.cloud.aiplatform.v1beta1.CachedContent"g\xdaA\x15parent,cached_content\x82\xd3\xe4\x93\x02I"7/v1beta1/{parent=projects/*/locations/*}/cachedContents:\x0ecached_content\x12\xc4\x01\n\x10GetCachedContent\x128.google.cloud.aiplatform.v1beta1.GetCachedContentRequest\x1a..google.cloud.aiplatform.v1beta1.CachedContent"F\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v1beta1/{name=projects/*/locations/*/cachedContents/*}\x12\xff\x01\n\x13UpdateCachedContent\x12;.google.cloud.aiplatform.v1beta1.UpdateCachedContentRequest\x1a..google.cloud.aiplatform.v1beta1.CachedContent"{\xdaA\x1acached_content,update_mask\x82\xd3\xe4\x93\x02X2F/v1beta1/{cached_content.name=projects/*/locations/*/cachedContents/*}:\x0ecached_content\x12\xb2\x01\n\x13DeleteCachedContent\x12;.google.cloud.aiplatform.v1beta1.DeleteCachedContentRequest\x1a\x16.google.protobuf.Empty"F\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v1beta1/{name=projects/*/locations/*/cachedContents/*}\x12\xd7\x01\n\x12ListCachedContents\x12:.google.cloud.aiplatform.v1beta1.ListCachedContentsRequest\x1a;.google.cloud.aiplatform.v1beta1.ListCachedContentsResponse"H\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1beta1/{parent=projects/*/locations/*}/cachedContents\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xed\x01\n#com.google.cloud.aiplatform.v1beta1B\x16GenAiCacheServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.gen_ai_cache_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x16GenAiCacheServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CREATECACHEDCONTENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECACHEDCONTENTREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\x12'aiplatform.googleapis.com/CachedContent"
    _globals['_CREATECACHEDCONTENTREQUEST'].fields_by_name['cached_content']._loaded_options = None
    _globals['_CREATECACHEDCONTENTREQUEST'].fields_by_name['cached_content']._serialized_options = b'\xe0A\x02'
    _globals['_GETCACHEDCONTENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCACHEDCONTENTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'aiplatform.googleapis.com/CachedContent"
    _globals['_UPDATECACHEDCONTENTREQUEST'].fields_by_name['cached_content']._loaded_options = None
    _globals['_UPDATECACHEDCONTENTREQUEST'].fields_by_name['cached_content']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECACHEDCONTENTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECACHEDCONTENTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETECACHEDCONTENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECACHEDCONTENTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'aiplatform.googleapis.com/CachedContent"
    _globals['_LISTCACHEDCONTENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCACHEDCONTENTSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\x12'aiplatform.googleapis.com/CachedContent"
    _globals['_LISTCACHEDCONTENTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCACHEDCONTENTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCACHEDCONTENTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCACHEDCONTENTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GENAICACHESERVICE']._loaded_options = None
    _globals['_GENAICACHESERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_GENAICACHESERVICE'].methods_by_name['CreateCachedContent']._loaded_options = None
    _globals['_GENAICACHESERVICE'].methods_by_name['CreateCachedContent']._serialized_options = b'\xdaA\x15parent,cached_content\x82\xd3\xe4\x93\x02I"7/v1beta1/{parent=projects/*/locations/*}/cachedContents:\x0ecached_content'
    _globals['_GENAICACHESERVICE'].methods_by_name['GetCachedContent']._loaded_options = None
    _globals['_GENAICACHESERVICE'].methods_by_name['GetCachedContent']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v1beta1/{name=projects/*/locations/*/cachedContents/*}'
    _globals['_GENAICACHESERVICE'].methods_by_name['UpdateCachedContent']._loaded_options = None
    _globals['_GENAICACHESERVICE'].methods_by_name['UpdateCachedContent']._serialized_options = b'\xdaA\x1acached_content,update_mask\x82\xd3\xe4\x93\x02X2F/v1beta1/{cached_content.name=projects/*/locations/*/cachedContents/*}:\x0ecached_content'
    _globals['_GENAICACHESERVICE'].methods_by_name['DeleteCachedContent']._loaded_options = None
    _globals['_GENAICACHESERVICE'].methods_by_name['DeleteCachedContent']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v1beta1/{name=projects/*/locations/*/cachedContents/*}'
    _globals['_GENAICACHESERVICE'].methods_by_name['ListCachedContents']._loaded_options = None
    _globals['_GENAICACHESERVICE'].methods_by_name['ListCachedContents']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1beta1/{parent=projects/*/locations/*}/cachedContents'
    _globals['_CREATECACHEDCONTENTREQUEST']._serialized_start = 328
    _globals['_CREATECACHEDCONTENTREQUEST']._serialized_end = 498
    _globals['_GETCACHEDCONTENTREQUEST']._serialized_start = 500
    _globals['_GETCACHEDCONTENTREQUEST']._serialized_end = 588
    _globals['_UPDATECACHEDCONTENTREQUEST']._serialized_start = 591
    _globals['_UPDATECACHEDCONTENTREQUEST']._serialized_end = 750
    _globals['_DELETECACHEDCONTENTREQUEST']._serialized_start = 752
    _globals['_DELETECACHEDCONTENTREQUEST']._serialized_end = 843
    _globals['_LISTCACHEDCONTENTSREQUEST']._serialized_start = 846
    _globals['_LISTCACHEDCONTENTSREQUEST']._serialized_end = 987
    _globals['_LISTCACHEDCONTENTSRESPONSE']._serialized_start = 989
    _globals['_LISTCACHEDCONTENTSRESPONSE']._serialized_end = 1115
    _globals['_GENAICACHESERVICE']._serialized_start = 1118
    _globals['_GENAICACHESERVICE']._serialized_end = 2310