"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/datamanager/v1/terms_of_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/ads/datamanager/v1/terms_of_service.proto\x12\x19google.ads.datamanager.v1\x1a\x1fgoogle/api/field_behavior.proto"v\n\x0eTermsOfService\x12d\n&customer_match_terms_of_service_status\x18\x01 \x01(\x0e2/.google.ads.datamanager.v1.TermsOfServiceStatusB\x03\xe0A\x01*[\n\x14TermsOfServiceStatus\x12\'\n#TERMS_OF_SERVICE_STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08ACCEPTED\x10\x01\x12\x0c\n\x08REJECTED\x10\x02B\xd3\x01\n\x1dcom.google.ads.datamanager.v1B\x13TermsOfServiceProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager\xaa\x02\x19Google.Ads.DataManager.V1\xca\x02\x19Google\\Ads\\DataManager\\V1\xea\x02\x1cGoogle::Ads::DataManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.datamanager.v1.terms_of_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.ads.datamanager.v1B\x13TermsOfServiceProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager\xaa\x02\x19Google.Ads.DataManager.V1\xca\x02\x19Google\\Ads\\DataManager\\V1\xea\x02\x1cGoogle::Ads::DataManager::V1'
    _globals['_TERMSOFSERVICE'].fields_by_name['customer_match_terms_of_service_status']._loaded_options = None
    _globals['_TERMSOFSERVICE'].fields_by_name['customer_match_terms_of_service_status']._serialized_options = b'\xe0A\x01'
    _globals['_TERMSOFSERVICESTATUS']._serialized_start = 232
    _globals['_TERMSOFSERVICESTATUS']._serialized_end = 323
    _globals['_TERMSOFSERVICE']._serialized_start = 112
    _globals['_TERMSOFSERVICE']._serialized_end = 230