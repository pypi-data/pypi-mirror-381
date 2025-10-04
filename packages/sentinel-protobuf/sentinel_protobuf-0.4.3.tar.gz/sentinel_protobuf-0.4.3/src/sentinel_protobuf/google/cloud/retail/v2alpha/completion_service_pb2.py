"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2alpha/completion_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2alpha import common_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_common__pb2
from .....google.cloud.retail.v2alpha import import_config_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_import__config__pb2
from .....google.cloud.retail.v2alpha import search_service_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_search__service__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/retail/v2alpha/completion_service.proto\x12\x1bgoogle.cloud.retail.v2alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/retail/v2alpha/common.proto\x1a/google/cloud/retail/v2alpha/import_config.proto\x1a0google/cloud/retail/v2alpha/search_service.proto\x1a#google/longrunning/operations.proto"\x83\x02\n\x14CompleteQueryRequest\x126\n\x07catalog\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12\x12\n\x05query\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x12\n\nvisitor_id\x18\x07 \x01(\t\x12\x16\n\x0elanguage_codes\x18\x03 \x03(\t\x12\x13\n\x0bdevice_type\x18\x04 \x01(\t\x12\x0f\n\x07dataset\x18\x06 \x01(\t\x12\x17\n\x0fmax_suggestions\x18\x05 \x01(\x05\x12$\n\x1cenable_attribute_suggestions\x18\t \x01(\x08\x12\x0e\n\x06entity\x18\n \x01(\t"\x8b\x07\n\x15CompleteQueryResponse\x12_\n\x12completion_results\x18\x01 \x03(\x0b2C.google.cloud.retail.v2alpha.CompleteQueryResponse.CompletionResult\x12\x19\n\x11attribution_token\x18\x02 \x01(\t\x12h\n\x15recent_search_results\x18\x03 \x03(\x0b2E.google.cloud.retail.v2alpha.CompleteQueryResponse.RecentSearchResultB\x02\x18\x01\x12c\n\x11attribute_results\x18\x04 \x03(\x0b2H.google.cloud.retail.v2alpha.CompleteQueryResponse.AttributeResultsEntry\x1a\xd0\x02\n\x10CompletionResult\x12\x12\n\nsuggestion\x18\x01 \x01(\t\x12g\n\nattributes\x18\x02 \x03(\x0b2S.google.cloud.retail.v2alpha.CompleteQueryResponse.CompletionResult.AttributesEntry\x12A\n\x06facets\x18\x03 \x03(\x0b21.google.cloud.retail.v2alpha.SearchResponse.Facet\x12\x1b\n\x13total_product_count\x18\x04 \x01(\x05\x1a_\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12;\n\x05value\x18\x02 \x01(\x0b2,.google.cloud.retail.v2alpha.CustomAttribute:\x028\x01\x1a/\n\x12RecentSearchResult\x12\x15\n\rrecent_search\x18\x01 \x01(\t:\x02\x18\x01\x1a&\n\x0fAttributeResult\x12\x13\n\x0bsuggestions\x18\x01 \x03(\t\x1a{\n\x15AttributeResultsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12Q\n\x05value\x18\x02 \x01(\x0b2B.google.cloud.retail.v2alpha.CompleteQueryResponse.AttributeResult:\x028\x012\xd5\x04\n\x11CompletionService\x12\xc2\x01\n\rCompleteQuery\x121.google.cloud.retail.v2alpha.CompleteQueryRequest\x1a2.google.cloud.retail.v2alpha.CompleteQueryResponse"J\x82\xd3\xe4\x93\x02D\x12B/v2alpha/{catalog=projects/*/locations/*/catalogs/*}:completeQuery\x12\xaf\x02\n\x14ImportCompletionData\x128.google.cloud.retail.v2alpha.ImportCompletionDataRequest\x1a\x1d.google.longrunning.Operation"\xbd\x01\xcaAf\n8google.cloud.retail.v2alpha.ImportCompletionDataResponse\x12*google.cloud.retail.v2alpha.ImportMetadata\x82\xd3\xe4\x93\x02N"I/v2alpha/{parent=projects/*/locations/*/catalogs/*}/completionData:import:\x01*\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xda\x01\n\x1fcom.google.cloud.retail.v2alphaB\x16CompletionServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2alpha.completion_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.retail.v2alphaB\x16CompletionServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alpha'
    _globals['_COMPLETEQUERYREQUEST'].fields_by_name['catalog']._loaded_options = None
    _globals['_COMPLETEQUERYREQUEST'].fields_by_name['catalog']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_COMPLETEQUERYREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_COMPLETEQUERYREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x02'
    _globals['_COMPLETEQUERYRESPONSE_COMPLETIONRESULT_ATTRIBUTESENTRY']._loaded_options = None
    _globals['_COMPLETEQUERYRESPONSE_COMPLETIONRESULT_ATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_COMPLETEQUERYRESPONSE_RECENTSEARCHRESULT']._loaded_options = None
    _globals['_COMPLETEQUERYRESPONSE_RECENTSEARCHRESULT']._serialized_options = b'\x18\x01'
    _globals['_COMPLETEQUERYRESPONSE_ATTRIBUTERESULTSENTRY']._loaded_options = None
    _globals['_COMPLETEQUERYRESPONSE_ATTRIBUTERESULTSENTRY']._serialized_options = b'8\x01'
    _globals['_COMPLETEQUERYRESPONSE'].fields_by_name['recent_search_results']._loaded_options = None
    _globals['_COMPLETEQUERYRESPONSE'].fields_by_name['recent_search_results']._serialized_options = b'\x18\x01'
    _globals['_COMPLETIONSERVICE']._loaded_options = None
    _globals['_COMPLETIONSERVICE']._serialized_options = b'\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_COMPLETIONSERVICE'].methods_by_name['CompleteQuery']._loaded_options = None
    _globals['_COMPLETIONSERVICE'].methods_by_name['CompleteQuery']._serialized_options = b'\x82\xd3\xe4\x93\x02D\x12B/v2alpha/{catalog=projects/*/locations/*/catalogs/*}:completeQuery'
    _globals['_COMPLETIONSERVICE'].methods_by_name['ImportCompletionData']._loaded_options = None
    _globals['_COMPLETIONSERVICE'].methods_by_name['ImportCompletionData']._serialized_options = b'\xcaAf\n8google.cloud.retail.v2alpha.ImportCompletionDataResponse\x12*google.cloud.retail.v2alpha.ImportMetadata\x82\xd3\xe4\x93\x02N"I/v2alpha/{parent=projects/*/locations/*/catalogs/*}/completionData:import:\x01*'
    _globals['_COMPLETEQUERYREQUEST']._serialized_start = 379
    _globals['_COMPLETEQUERYREQUEST']._serialized_end = 638
    _globals['_COMPLETEQUERYRESPONSE']._serialized_start = 641
    _globals['_COMPLETEQUERYRESPONSE']._serialized_end = 1548
    _globals['_COMPLETEQUERYRESPONSE_COMPLETIONRESULT']._serialized_start = 998
    _globals['_COMPLETEQUERYRESPONSE_COMPLETIONRESULT']._serialized_end = 1334
    _globals['_COMPLETEQUERYRESPONSE_COMPLETIONRESULT_ATTRIBUTESENTRY']._serialized_start = 1239
    _globals['_COMPLETEQUERYRESPONSE_COMPLETIONRESULT_ATTRIBUTESENTRY']._serialized_end = 1334
    _globals['_COMPLETEQUERYRESPONSE_RECENTSEARCHRESULT']._serialized_start = 1336
    _globals['_COMPLETEQUERYRESPONSE_RECENTSEARCHRESULT']._serialized_end = 1383
    _globals['_COMPLETEQUERYRESPONSE_ATTRIBUTERESULT']._serialized_start = 1385
    _globals['_COMPLETEQUERYRESPONSE_ATTRIBUTERESULT']._serialized_end = 1423
    _globals['_COMPLETEQUERYRESPONSE_ATTRIBUTERESULTSENTRY']._serialized_start = 1425
    _globals['_COMPLETEQUERYRESPONSE_ATTRIBUTERESULTSENTRY']._serialized_end = 1548
    _globals['_COMPLETIONSERVICE']._serialized_start = 1551
    _globals['_COMPLETIONSERVICE']._serialized_end = 2148