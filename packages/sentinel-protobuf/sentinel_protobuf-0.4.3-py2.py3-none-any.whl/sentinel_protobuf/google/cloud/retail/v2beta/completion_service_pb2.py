"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2beta/completion_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2beta import common_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_common__pb2
from .....google.cloud.retail.v2beta import import_config_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_import__config__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/retail/v2beta/completion_service.proto\x12\x1agoogle.cloud.retail.v2beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\'google/cloud/retail/v2beta/common.proto\x1a.google/cloud/retail/v2beta/import_config.proto\x1a#google/longrunning/operations.proto"\x83\x02\n\x14CompleteQueryRequest\x126\n\x07catalog\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12\x12\n\x05query\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x12\n\nvisitor_id\x18\x07 \x01(\t\x12\x16\n\x0elanguage_codes\x18\x03 \x03(\t\x12\x13\n\x0bdevice_type\x18\x04 \x01(\t\x12\x0f\n\x07dataset\x18\x06 \x01(\t\x12\x17\n\x0fmax_suggestions\x18\x05 \x01(\x05\x12$\n\x1cenable_attribute_suggestions\x18\t \x01(\x08\x12\x0e\n\x06entity\x18\n \x01(\t"\xa5\x06\n\x15CompleteQueryResponse\x12^\n\x12completion_results\x18\x01 \x03(\x0b2B.google.cloud.retail.v2beta.CompleteQueryResponse.CompletionResult\x12\x19\n\x11attribution_token\x18\x02 \x01(\t\x12g\n\x15recent_search_results\x18\x03 \x03(\x0b2D.google.cloud.retail.v2beta.CompleteQueryResponse.RecentSearchResultB\x02\x18\x01\x12b\n\x11attribute_results\x18\x04 \x03(\x0b2G.google.cloud.retail.v2beta.CompleteQueryResponse.AttributeResultsEntry\x1a\xee\x01\n\x10CompletionResult\x12\x12\n\nsuggestion\x18\x01 \x01(\t\x12f\n\nattributes\x18\x02 \x03(\x0b2R.google.cloud.retail.v2beta.CompleteQueryResponse.CompletionResult.AttributesEntry\x1a^\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12:\n\x05value\x18\x02 \x01(\x0b2+.google.cloud.retail.v2beta.CustomAttribute:\x028\x01\x1a/\n\x12RecentSearchResult\x12\x15\n\rrecent_search\x18\x01 \x01(\t:\x02\x18\x01\x1a&\n\x0fAttributeResult\x12\x13\n\x0bsuggestions\x18\x01 \x03(\t\x1az\n\x15AttributeResultsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12P\n\x05value\x18\x02 \x01(\x0b2A.google.cloud.retail.v2beta.CompleteQueryResponse.AttributeResult:\x028\x012\xce\x04\n\x11CompletionService\x12\xbf\x01\n\rCompleteQuery\x120.google.cloud.retail.v2beta.CompleteQueryRequest\x1a1.google.cloud.retail.v2beta.CompleteQueryResponse"I\x82\xd3\xe4\x93\x02C\x12A/v2beta/{catalog=projects/*/locations/*/catalogs/*}:completeQuery\x12\xab\x02\n\x14ImportCompletionData\x127.google.cloud.retail.v2beta.ImportCompletionDataRequest\x1a\x1d.google.longrunning.Operation"\xba\x01\xcaAd\n7google.cloud.retail.v2beta.ImportCompletionDataResponse\x12)google.cloud.retail.v2beta.ImportMetadata\x82\xd3\xe4\x93\x02M"H/v2beta/{parent=projects/*/locations/*/catalogs/*}/completionData:import:\x01*\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd5\x01\n\x1ecom.google.cloud.retail.v2betaB\x16CompletionServiceProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2beta.completion_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.retail.v2betaB\x16CompletionServiceProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2beta'
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
    _globals['_COMPLETIONSERVICE'].methods_by_name['CompleteQuery']._serialized_options = b'\x82\xd3\xe4\x93\x02C\x12A/v2beta/{catalog=projects/*/locations/*/catalogs/*}:completeQuery'
    _globals['_COMPLETIONSERVICE'].methods_by_name['ImportCompletionData']._loaded_options = None
    _globals['_COMPLETIONSERVICE'].methods_by_name['ImportCompletionData']._serialized_options = b'\xcaAd\n7google.cloud.retail.v2beta.ImportCompletionDataResponse\x12)google.cloud.retail.v2beta.ImportMetadata\x82\xd3\xe4\x93\x02M"H/v2beta/{parent=projects/*/locations/*/catalogs/*}/completionData:import:\x01*'
    _globals['_COMPLETEQUERYREQUEST']._serialized_start = 325
    _globals['_COMPLETEQUERYREQUEST']._serialized_end = 584
    _globals['_COMPLETEQUERYRESPONSE']._serialized_start = 587
    _globals['_COMPLETEQUERYRESPONSE']._serialized_end = 1392
    _globals['_COMPLETEQUERYRESPONSE_COMPLETIONRESULT']._serialized_start = 941
    _globals['_COMPLETEQUERYRESPONSE_COMPLETIONRESULT']._serialized_end = 1179
    _globals['_COMPLETEQUERYRESPONSE_COMPLETIONRESULT_ATTRIBUTESENTRY']._serialized_start = 1085
    _globals['_COMPLETEQUERYRESPONSE_COMPLETIONRESULT_ATTRIBUTESENTRY']._serialized_end = 1179
    _globals['_COMPLETEQUERYRESPONSE_RECENTSEARCHRESULT']._serialized_start = 1181
    _globals['_COMPLETEQUERYRESPONSE_RECENTSEARCHRESULT']._serialized_end = 1228
    _globals['_COMPLETEQUERYRESPONSE_ATTRIBUTERESULT']._serialized_start = 1230
    _globals['_COMPLETEQUERYRESPONSE_ATTRIBUTERESULT']._serialized_end = 1268
    _globals['_COMPLETEQUERYRESPONSE_ATTRIBUTERESULTSENTRY']._serialized_start = 1270
    _globals['_COMPLETEQUERYRESPONSE_ATTRIBUTERESULTSENTRY']._serialized_end = 1392
    _globals['_COMPLETIONSERVICE']._serialized_start = 1395
    _globals['_COMPLETIONSERVICE']._serialized_end = 1985