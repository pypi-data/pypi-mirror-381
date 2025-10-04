"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2alpha/branch.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2alpha import product_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_product__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/retail/v2alpha/branch.proto\x12\x1bgoogle.cloud.retail.v2alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/retail/v2alpha/product.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf9\x07\n\x06Branch\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x17\n\nis_default\x18\x03 \x01(\x08B\x03\xe0A\x03\x12A\n\x18last_product_import_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12[\n\x13product_count_stats\x18\x07 \x03(\x0b29.google.cloud.retail.v2alpha.Branch.ProductCountStatisticB\x03\xe0A\x03\x12O\n\x0fquality_metrics\x18\x06 \x03(\x0b21.google.cloud.retail.v2alpha.Branch.QualityMetricB\x03\xe0A\x03\x1a\xde\x02\n\x15ProductCountStatistic\x12Z\n\x05scope\x18\x01 \x01(\x0e2K.google.cloud.retail.v2alpha.Branch.ProductCountStatistic.ProductCountScope\x12U\n\x06counts\x18\x02 \x03(\x0b2E.google.cloud.retail.v2alpha.Branch.ProductCountStatistic.CountsEntry\x1a-\n\x0bCountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x028\x01"c\n\x11ProductCountScope\x12#\n\x1fPRODUCT_COUNT_SCOPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cALL_PRODUCTS\x10\x01\x12\x17\n\x13LAST_24_HOUR_UPDATE\x10\x02\x1a\xe4\x01\n\rQualityMetric\x12\x17\n\x0frequirement_key\x18\x01 \x01(\t\x12\x1f\n\x17qualified_product_count\x18\x02 \x01(\x05\x12!\n\x19unqualified_product_count\x18\x03 \x01(\x05\x12+\n#suggested_quality_percent_threshold\x18\x04 \x01(\x01\x12I\n\x1bunqualified_sample_products\x18\x05 \x03(\x0b2$.google.cloud.retail.v2alpha.Product:o\xeaAl\n\x1cretail.googleapis.com/Branch\x12Lprojects/{project}/locations/{location}/catalogs/{catalog}/branches/{branch}*V\n\nBranchView\x12\x1b\n\x17BRANCH_VIEW_UNSPECIFIED\x10\x00\x12\x15\n\x11BRANCH_VIEW_BASIC\x10\x01\x12\x14\n\x10BRANCH_VIEW_FULL\x10\x02B\xcf\x01\n\x1fcom.google.cloud.retail.v2alphaB\x0bBranchProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2alpha.branch_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.retail.v2alphaB\x0bBranchProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alpha'
    _globals['_BRANCH_PRODUCTCOUNTSTATISTIC_COUNTSENTRY']._loaded_options = None
    _globals['_BRANCH_PRODUCTCOUNTSTATISTIC_COUNTSENTRY']._serialized_options = b'8\x01'
    _globals['_BRANCH'].fields_by_name['name']._loaded_options = None
    _globals['_BRANCH'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_BRANCH'].fields_by_name['display_name']._loaded_options = None
    _globals['_BRANCH'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_BRANCH'].fields_by_name['is_default']._loaded_options = None
    _globals['_BRANCH'].fields_by_name['is_default']._serialized_options = b'\xe0A\x03'
    _globals['_BRANCH'].fields_by_name['last_product_import_time']._loaded_options = None
    _globals['_BRANCH'].fields_by_name['last_product_import_time']._serialized_options = b'\xe0A\x03'
    _globals['_BRANCH'].fields_by_name['product_count_stats']._loaded_options = None
    _globals['_BRANCH'].fields_by_name['product_count_stats']._serialized_options = b'\xe0A\x03'
    _globals['_BRANCH'].fields_by_name['quality_metrics']._loaded_options = None
    _globals['_BRANCH'].fields_by_name['quality_metrics']._serialized_options = b'\xe0A\x03'
    _globals['_BRANCH']._loaded_options = None
    _globals['_BRANCH']._serialized_options = b'\xeaAl\n\x1cretail.googleapis.com/Branch\x12Lprojects/{project}/locations/{location}/catalogs/{catalog}/branches/{branch}'
    _globals['_BRANCHVIEW']._serialized_start = 1229
    _globals['_BRANCHVIEW']._serialized_end = 1315
    _globals['_BRANCH']._serialized_start = 210
    _globals['_BRANCH']._serialized_end = 1227
    _globals['_BRANCH_PRODUCTCOUNTSTATISTIC']._serialized_start = 533
    _globals['_BRANCH_PRODUCTCOUNTSTATISTIC']._serialized_end = 883
    _globals['_BRANCH_PRODUCTCOUNTSTATISTIC_COUNTSENTRY']._serialized_start = 737
    _globals['_BRANCH_PRODUCTCOUNTSTATISTIC_COUNTSENTRY']._serialized_end = 782
    _globals['_BRANCH_PRODUCTCOUNTSTATISTIC_PRODUCTCOUNTSCOPE']._serialized_start = 784
    _globals['_BRANCH_PRODUCTCOUNTSTATISTIC_PRODUCTCOUNTSCOPE']._serialized_end = 883
    _globals['_BRANCH_QUALITYMETRIC']._serialized_start = 886
    _globals['_BRANCH_QUALITYMETRIC']._serialized_end = 1114