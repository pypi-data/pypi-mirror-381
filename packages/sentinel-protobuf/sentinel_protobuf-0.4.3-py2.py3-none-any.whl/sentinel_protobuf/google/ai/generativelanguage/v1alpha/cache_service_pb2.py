"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ai/generativelanguage/v1alpha/cache_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ai.generativelanguage.v1alpha import cached_content_pb2 as google_dot_ai_dot_generativelanguage_dot_v1alpha_dot_cached__content__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ai/generativelanguage/v1alpha/cache_service.proto\x12$google.ai.generativelanguage.v1alpha\x1a9google/ai/generativelanguage/v1alpha/cached_content.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"L\n\x19ListCachedContentsRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x02 \x01(\tB\x03\xe0A\x01"\x83\x01\n\x1aListCachedContentsResponse\x12L\n\x0fcached_contents\x18\x01 \x03(\x0b23.google.ai.generativelanguage.v1alpha.CachedContent\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"n\n\x1aCreateCachedContentRequest\x12P\n\x0ecached_content\x18\x01 \x01(\x0b23.google.ai.generativelanguage.v1alpha.CachedContentB\x03\xe0A\x02"`\n\x17GetCachedContentRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/generativelanguage.googleapis.com/CachedContent"\x9f\x01\n\x1aUpdateCachedContentRequest\x12P\n\x0ecached_content\x18\x01 \x01(\x0b23.google.ai.generativelanguage.v1alpha.CachedContentB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"c\n\x1aDeleteCachedContentRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/generativelanguage.googleapis.com/CachedContent2\x95\x08\n\x0cCacheService\x12\xbb\x01\n\x12ListCachedContents\x12?.google.ai.generativelanguage.v1alpha.ListCachedContentsRequest\x1a@.google.ai.generativelanguage.v1alpha.ListCachedContentsResponse""\xdaA\x00\x82\xd3\xe4\x93\x02\x19\x12\x17/v1alpha/cachedContents\x12\xce\x01\n\x13CreateCachedContent\x12@.google.ai.generativelanguage.v1alpha.CreateCachedContentRequest\x1a3.google.ai.generativelanguage.v1alpha.CachedContent"@\xdaA\x0ecached_content\x82\xd3\xe4\x93\x02)"\x17/v1alpha/cachedContents:\x0ecached_content\x12\xb7\x01\n\x10GetCachedContent\x12=.google.ai.generativelanguage.v1alpha.GetCachedContentRequest\x1a3.google.ai.generativelanguage.v1alpha.CachedContent"/\xdaA\x04name\x82\xd3\xe4\x93\x02"\x12 /v1alpha/{name=cachedContents/*}\x12\xf2\x01\n\x13UpdateCachedContent\x12@.google.ai.generativelanguage.v1alpha.UpdateCachedContentRequest\x1a3.google.ai.generativelanguage.v1alpha.CachedContent"d\xdaA\x1acached_content,update_mask\x82\xd3\xe4\x93\x02A2//v1alpha/{cached_content.name=cachedContents/*}:\x0ecached_content\x12\xa0\x01\n\x13DeleteCachedContent\x12@.google.ai.generativelanguage.v1alpha.DeleteCachedContentRequest\x1a\x16.google.protobuf.Empty"/\xdaA\x04name\x82\xd3\xe4\x93\x02"* /v1alpha/{name=cachedContents/*}\x1a$\xcaA!generativelanguage.googleapis.comB\x9f\x01\n(com.google.ai.generativelanguage.v1alphaB\x11CacheServiceProtoP\x01Z^cloud.google.com/go/ai/generativelanguage/apiv1alpha/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1alpha.cache_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ai.generativelanguage.v1alphaB\x11CacheServiceProtoP\x01Z^cloud.google.com/go/ai/generativelanguage/apiv1alpha/generativelanguagepb;generativelanguagepb'
    _globals['_LISTCACHEDCONTENTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCACHEDCONTENTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCACHEDCONTENTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCACHEDCONTENTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_CREATECACHEDCONTENTREQUEST'].fields_by_name['cached_content']._loaded_options = None
    _globals['_CREATECACHEDCONTENTREQUEST'].fields_by_name['cached_content']._serialized_options = b'\xe0A\x02'
    _globals['_GETCACHEDCONTENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCACHEDCONTENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/generativelanguage.googleapis.com/CachedContent'
    _globals['_UPDATECACHEDCONTENTREQUEST'].fields_by_name['cached_content']._loaded_options = None
    _globals['_UPDATECACHEDCONTENTREQUEST'].fields_by_name['cached_content']._serialized_options = b'\xe0A\x02'
    _globals['_DELETECACHEDCONTENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECACHEDCONTENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/generativelanguage.googleapis.com/CachedContent'
    _globals['_CACHESERVICE']._loaded_options = None
    _globals['_CACHESERVICE']._serialized_options = b'\xcaA!generativelanguage.googleapis.com'
    _globals['_CACHESERVICE'].methods_by_name['ListCachedContents']._loaded_options = None
    _globals['_CACHESERVICE'].methods_by_name['ListCachedContents']._serialized_options = b'\xdaA\x00\x82\xd3\xe4\x93\x02\x19\x12\x17/v1alpha/cachedContents'
    _globals['_CACHESERVICE'].methods_by_name['CreateCachedContent']._loaded_options = None
    _globals['_CACHESERVICE'].methods_by_name['CreateCachedContent']._serialized_options = b'\xdaA\x0ecached_content\x82\xd3\xe4\x93\x02)"\x17/v1alpha/cachedContents:\x0ecached_content'
    _globals['_CACHESERVICE'].methods_by_name['GetCachedContent']._loaded_options = None
    _globals['_CACHESERVICE'].methods_by_name['GetCachedContent']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02"\x12 /v1alpha/{name=cachedContents/*}'
    _globals['_CACHESERVICE'].methods_by_name['UpdateCachedContent']._loaded_options = None
    _globals['_CACHESERVICE'].methods_by_name['UpdateCachedContent']._serialized_options = b'\xdaA\x1acached_content,update_mask\x82\xd3\xe4\x93\x02A2//v1alpha/{cached_content.name=cachedContents/*}:\x0ecached_content'
    _globals['_CACHESERVICE'].methods_by_name['DeleteCachedContent']._loaded_options = None
    _globals['_CACHESERVICE'].methods_by_name['DeleteCachedContent']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02"* /v1alpha/{name=cachedContents/*}'
    _globals['_LISTCACHEDCONTENTSREQUEST']._serialized_start = 335
    _globals['_LISTCACHEDCONTENTSREQUEST']._serialized_end = 411
    _globals['_LISTCACHEDCONTENTSRESPONSE']._serialized_start = 414
    _globals['_LISTCACHEDCONTENTSRESPONSE']._serialized_end = 545
    _globals['_CREATECACHEDCONTENTREQUEST']._serialized_start = 547
    _globals['_CREATECACHEDCONTENTREQUEST']._serialized_end = 657
    _globals['_GETCACHEDCONTENTREQUEST']._serialized_start = 659
    _globals['_GETCACHEDCONTENTREQUEST']._serialized_end = 755
    _globals['_UPDATECACHEDCONTENTREQUEST']._serialized_start = 758
    _globals['_UPDATECACHEDCONTENTREQUEST']._serialized_end = 917
    _globals['_DELETECACHEDCONTENTREQUEST']._serialized_start = 919
    _globals['_DELETECACHEDCONTENTREQUEST']._serialized_end = 1018
    _globals['_CACHESERVICE']._serialized_start = 1021
    _globals['_CACHESERVICE']._serialized_end = 2066