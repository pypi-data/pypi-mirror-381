"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/financialservices/v1/bigquery_destination.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/financialservices/v1/bigquery_destination.proto\x12!google.cloud.financialservices.v1\x1a\x1fgoogle/api/field_behavior.proto"\xf2\x01\n\x13BigQueryDestination\x12\x16\n\ttable_uri\x18\x01 \x01(\tB\x03\xe0A\x01\x12g\n\x11write_disposition\x18\x02 \x01(\x0e2G.google.cloud.financialservices.v1.BigQueryDestination.WriteDispositionB\x03\xe0A\x02"Z\n\x10WriteDisposition\x12!\n\x1dWRITE_DISPOSITION_UNSPECIFIED\x10\x00\x12\x0f\n\x0bWRITE_EMPTY\x10\x01\x12\x12\n\x0eWRITE_TRUNCATE\x10\x02B\x87\x02\n%com.google.cloud.financialservices.v1B\x18BigQueryDestinationProtoP\x01ZScloud.google.com/go/financialservices/apiv1/financialservicespb;financialservicespb\xaa\x02!Google.Cloud.FinancialServices.V1\xca\x02!Google\\Cloud\\FinancialServices\\V1\xea\x02$Google::Cloud::FinancialServices::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.financialservices.v1.bigquery_destination_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.financialservices.v1B\x18BigQueryDestinationProtoP\x01ZScloud.google.com/go/financialservices/apiv1/financialservicespb;financialservicespb\xaa\x02!Google.Cloud.FinancialServices.V1\xca\x02!Google\\Cloud\\FinancialServices\\V1\xea\x02$Google::Cloud::FinancialServices::V1'
    _globals['_BIGQUERYDESTINATION'].fields_by_name['table_uri']._loaded_options = None
    _globals['_BIGQUERYDESTINATION'].fields_by_name['table_uri']._serialized_options = b'\xe0A\x01'
    _globals['_BIGQUERYDESTINATION'].fields_by_name['write_disposition']._loaded_options = None
    _globals['_BIGQUERYDESTINATION'].fields_by_name['write_disposition']._serialized_options = b'\xe0A\x02'
    _globals['_BIGQUERYDESTINATION']._serialized_start = 133
    _globals['_BIGQUERYDESTINATION']._serialized_end = 375
    _globals['_BIGQUERYDESTINATION_WRITEDISPOSITION']._serialized_start = 285
    _globals['_BIGQUERYDESTINATION_WRITEDISPOSITION']._serialized_end = 375