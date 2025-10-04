"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2beta/import_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2beta import product_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_product__pb2
from .....google.cloud.retail.v2beta import user_event_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_user__event__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from .....google.type import date_pb2 as google_dot_type_dot_date__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/retail/v2beta/import_config.proto\x12\x1agoogle.cloud.retail.v2beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/retail/v2beta/product.proto\x1a+google/cloud/retail/v2beta/user_event.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x16google/type/date.proto"9\n\tGcsSource\x12\x17\n\ninput_uris\x18\x01 \x03(\tB\x03\xe0A\x02\x12\x13\n\x0bdata_schema\x18\x02 \x01(\t"\xbc\x01\n\x0eBigQuerySource\x12+\n\x0epartition_date\x18\x06 \x01(\x0b2\x11.google.type.DateH\x00\x12\x12\n\nproject_id\x18\x05 \x01(\t\x12\x17\n\ndataset_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x17\n\x0fgcs_staging_dir\x18\x03 \x01(\t\x12\x13\n\x0bdata_schema\x18\x04 \x01(\tB\x0b\n\tpartition"Q\n\x13ProductInlineSource\x12:\n\x08products\x18\x01 \x03(\x0b2#.google.cloud.retail.v2beta.ProductB\x03\xe0A\x02"X\n\x15UserEventInlineSource\x12?\n\x0buser_events\x18\x01 \x03(\x0b2%.google.cloud.retail.v2beta.UserEventB\x03\xe0A\x02"9\n\x12ImportErrorsConfig\x12\x14\n\ngcs_prefix\x18\x01 \x01(\tH\x00B\r\n\x0bdestination"\x84\x04\n\x15ImportProductsRequest\x124\n\x06parent\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cretail.googleapis.com/Branch\x12\x16\n\nrequest_id\x18\x06 \x01(\tB\x02\x18\x01\x12I\n\x0cinput_config\x18\x02 \x01(\x0b2..google.cloud.retail.v2beta.ProductInputConfigB\x03\xe0A\x02\x12E\n\rerrors_config\x18\x03 \x01(\x0b2..google.cloud.retail.v2beta.ImportErrorsConfig\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12a\n\x13reconciliation_mode\x18\x05 \x01(\x0e2D.google.cloud.retail.v2beta.ImportProductsRequest.ReconciliationMode\x12!\n\x19notification_pubsub_topic\x18\x07 \x01(\t"T\n\x12ReconciliationMode\x12#\n\x1fRECONCILIATION_MODE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bINCREMENTAL\x10\x01\x12\x08\n\x04FULL\x10\x02"\xe4\x01\n\x17ImportUserEventsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12K\n\x0cinput_config\x18\x02 \x01(\x0b20.google.cloud.retail.v2beta.UserEventInputConfigB\x03\xe0A\x02\x12E\n\rerrors_config\x18\x03 \x01(\x0b2..google.cloud.retail.v2beta.ImportErrorsConfig"\xc9\x01\n\x1bImportCompletionDataRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12P\n\x0cinput_config\x18\x02 \x01(\x0b25.google.cloud.retail.v2beta.CompletionDataInputConfigB\x03\xe0A\x02\x12!\n\x19notification_pubsub_topic\x18\x03 \x01(\t"\xf5\x01\n\x12ProductInputConfig\x12P\n\x15product_inline_source\x18\x01 \x01(\x0b2/.google.cloud.retail.v2beta.ProductInlineSourceH\x00\x12;\n\ngcs_source\x18\x02 \x01(\x0b2%.google.cloud.retail.v2beta.GcsSourceH\x00\x12F\n\x10big_query_source\x18\x03 \x01(\x0b2*.google.cloud.retail.v2beta.BigQuerySourceH\x00B\x08\n\x06source"\x8b\x02\n\x14UserEventInputConfig\x12Z\n\x18user_event_inline_source\x18\x01 \x01(\x0b21.google.cloud.retail.v2beta.UserEventInlineSourceB\x03\xe0A\x02H\x00\x12@\n\ngcs_source\x18\x02 \x01(\x0b2%.google.cloud.retail.v2beta.GcsSourceB\x03\xe0A\x02H\x00\x12K\n\x10big_query_source\x18\x03 \x01(\x0b2*.google.cloud.retail.v2beta.BigQuerySourceB\x03\xe0A\x02H\x00B\x08\n\x06source"r\n\x19CompletionDataInputConfig\x12K\n\x10big_query_source\x18\x01 \x01(\x0b2*.google.cloud.retail.v2beta.BigQuerySourceB\x03\xe0A\x02H\x00B\x08\n\x06source"\xdb\x01\n\x0eImportMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rsuccess_count\x18\x03 \x01(\x03\x12\x15\n\rfailure_count\x18\x04 \x01(\x03\x12\x16\n\nrequest_id\x18\x05 \x01(\tB\x02\x18\x01\x12!\n\x19notification_pubsub_topic\x18\x06 \x01(\t"\x8a\x01\n\x16ImportProductsResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12E\n\rerrors_config\x18\x02 \x01(\x0b2..google.cloud.retail.v2beta.ImportErrorsConfig"\xd8\x01\n\x18ImportUserEventsResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12E\n\rerrors_config\x18\x02 \x01(\x0b2..google.cloud.retail.v2beta.ImportErrorsConfig\x12J\n\x0eimport_summary\x18\x03 \x01(\x0b22.google.cloud.retail.v2beta.UserEventImportSummary"T\n\x16UserEventImportSummary\x12\x1b\n\x13joined_events_count\x18\x01 \x01(\x03\x12\x1d\n\x15unjoined_events_count\x18\x02 \x01(\x03"I\n\x1cImportCompletionDataResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.StatusB\xd0\x01\n\x1ecom.google.cloud.retail.v2betaB\x11ImportConfigProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2beta.import_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.retail.v2betaB\x11ImportConfigProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2beta'
    _globals['_GCSSOURCE'].fields_by_name['input_uris']._loaded_options = None
    _globals['_GCSSOURCE'].fields_by_name['input_uris']._serialized_options = b'\xe0A\x02'
    _globals['_BIGQUERYSOURCE'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_BIGQUERYSOURCE'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_BIGQUERYSOURCE'].fields_by_name['table_id']._loaded_options = None
    _globals['_BIGQUERYSOURCE'].fields_by_name['table_id']._serialized_options = b'\xe0A\x02'
    _globals['_PRODUCTINLINESOURCE'].fields_by_name['products']._loaded_options = None
    _globals['_PRODUCTINLINESOURCE'].fields_by_name['products']._serialized_options = b'\xe0A\x02'
    _globals['_USEREVENTINLINESOURCE'].fields_by_name['user_events']._loaded_options = None
    _globals['_USEREVENTINLINESOURCE'].fields_by_name['user_events']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTPRODUCTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTPRODUCTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cretail.googleapis.com/Branch'
    _globals['_IMPORTPRODUCTSREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_IMPORTPRODUCTSREQUEST'].fields_by_name['request_id']._serialized_options = b'\x18\x01'
    _globals['_IMPORTPRODUCTSREQUEST'].fields_by_name['input_config']._loaded_options = None
    _globals['_IMPORTPRODUCTSREQUEST'].fields_by_name['input_config']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTUSEREVENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTUSEREVENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_IMPORTUSEREVENTSREQUEST'].fields_by_name['input_config']._loaded_options = None
    _globals['_IMPORTUSEREVENTSREQUEST'].fields_by_name['input_config']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTCOMPLETIONDATAREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTCOMPLETIONDATAREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_IMPORTCOMPLETIONDATAREQUEST'].fields_by_name['input_config']._loaded_options = None
    _globals['_IMPORTCOMPLETIONDATAREQUEST'].fields_by_name['input_config']._serialized_options = b'\xe0A\x02'
    _globals['_USEREVENTINPUTCONFIG'].fields_by_name['user_event_inline_source']._loaded_options = None
    _globals['_USEREVENTINPUTCONFIG'].fields_by_name['user_event_inline_source']._serialized_options = b'\xe0A\x02'
    _globals['_USEREVENTINPUTCONFIG'].fields_by_name['gcs_source']._loaded_options = None
    _globals['_USEREVENTINPUTCONFIG'].fields_by_name['gcs_source']._serialized_options = b'\xe0A\x02'
    _globals['_USEREVENTINPUTCONFIG'].fields_by_name['big_query_source']._loaded_options = None
    _globals['_USEREVENTINPUTCONFIG'].fields_by_name['big_query_source']._serialized_options = b'\xe0A\x02'
    _globals['_COMPLETIONDATAINPUTCONFIG'].fields_by_name['big_query_source']._loaded_options = None
    _globals['_COMPLETIONDATAINPUTCONFIG'].fields_by_name['big_query_source']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTMETADATA'].fields_by_name['request_id']._loaded_options = None
    _globals['_IMPORTMETADATA'].fields_by_name['request_id']._serialized_options = b'\x18\x01'
    _globals['_GCSSOURCE']._serialized_start = 341
    _globals['_GCSSOURCE']._serialized_end = 398
    _globals['_BIGQUERYSOURCE']._serialized_start = 401
    _globals['_BIGQUERYSOURCE']._serialized_end = 589
    _globals['_PRODUCTINLINESOURCE']._serialized_start = 591
    _globals['_PRODUCTINLINESOURCE']._serialized_end = 672
    _globals['_USEREVENTINLINESOURCE']._serialized_start = 674
    _globals['_USEREVENTINLINESOURCE']._serialized_end = 762
    _globals['_IMPORTERRORSCONFIG']._serialized_start = 764
    _globals['_IMPORTERRORSCONFIG']._serialized_end = 821
    _globals['_IMPORTPRODUCTSREQUEST']._serialized_start = 824
    _globals['_IMPORTPRODUCTSREQUEST']._serialized_end = 1340
    _globals['_IMPORTPRODUCTSREQUEST_RECONCILIATIONMODE']._serialized_start = 1256
    _globals['_IMPORTPRODUCTSREQUEST_RECONCILIATIONMODE']._serialized_end = 1340
    _globals['_IMPORTUSEREVENTSREQUEST']._serialized_start = 1343
    _globals['_IMPORTUSEREVENTSREQUEST']._serialized_end = 1571
    _globals['_IMPORTCOMPLETIONDATAREQUEST']._serialized_start = 1574
    _globals['_IMPORTCOMPLETIONDATAREQUEST']._serialized_end = 1775
    _globals['_PRODUCTINPUTCONFIG']._serialized_start = 1778
    _globals['_PRODUCTINPUTCONFIG']._serialized_end = 2023
    _globals['_USEREVENTINPUTCONFIG']._serialized_start = 2026
    _globals['_USEREVENTINPUTCONFIG']._serialized_end = 2293
    _globals['_COMPLETIONDATAINPUTCONFIG']._serialized_start = 2295
    _globals['_COMPLETIONDATAINPUTCONFIG']._serialized_end = 2409
    _globals['_IMPORTMETADATA']._serialized_start = 2412
    _globals['_IMPORTMETADATA']._serialized_end = 2631
    _globals['_IMPORTPRODUCTSRESPONSE']._serialized_start = 2634
    _globals['_IMPORTPRODUCTSRESPONSE']._serialized_end = 2772
    _globals['_IMPORTUSEREVENTSRESPONSE']._serialized_start = 2775
    _globals['_IMPORTUSEREVENTSRESPONSE']._serialized_end = 2991
    _globals['_USEREVENTIMPORTSUMMARY']._serialized_start = 2993
    _globals['_USEREVENTIMPORTSUMMARY']._serialized_end = 3077
    _globals['_IMPORTCOMPLETIONDATARESPONSE']._serialized_start = 3079
    _globals['_IMPORTCOMPLETIONDATARESPONSE']._serialized_end = 3152