"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2/import_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2 import product_pb2 as google_dot_cloud_dot_retail_dot_v2_dot_product__pb2
from .....google.cloud.retail.v2 import user_event_pb2 as google_dot_cloud_dot_retail_dot_v2_dot_user__event__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from .....google.type import date_pb2 as google_dot_type_dot_date__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/retail/v2/import_config.proto\x12\x16google.cloud.retail.v2\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a$google/cloud/retail/v2/product.proto\x1a\'google/cloud/retail/v2/user_event.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x16google/type/date.proto"9\n\tGcsSource\x12\x17\n\ninput_uris\x18\x01 \x03(\tB\x03\xe0A\x02\x12\x13\n\x0bdata_schema\x18\x02 \x01(\t"\xbc\x01\n\x0eBigQuerySource\x12+\n\x0epartition_date\x18\x06 \x01(\x0b2\x11.google.type.DateH\x00\x12\x12\n\nproject_id\x18\x05 \x01(\t\x12\x17\n\ndataset_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x17\n\x0fgcs_staging_dir\x18\x03 \x01(\t\x12\x13\n\x0bdata_schema\x18\x04 \x01(\tB\x0b\n\tpartition"M\n\x13ProductInlineSource\x126\n\x08products\x18\x01 \x03(\x0b2\x1f.google.cloud.retail.v2.ProductB\x03\xe0A\x02"T\n\x15UserEventInlineSource\x12;\n\x0buser_events\x18\x01 \x03(\x0b2!.google.cloud.retail.v2.UserEventB\x03\xe0A\x02"9\n\x12ImportErrorsConfig\x12\x14\n\ngcs_prefix\x18\x01 \x01(\tH\x00B\r\n\x0bdestination"\xf8\x03\n\x15ImportProductsRequest\x124\n\x06parent\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cretail.googleapis.com/Branch\x12\x16\n\nrequest_id\x18\x06 \x01(\tB\x02\x18\x01\x12E\n\x0cinput_config\x18\x02 \x01(\x0b2*.google.cloud.retail.v2.ProductInputConfigB\x03\xe0A\x02\x12A\n\rerrors_config\x18\x03 \x01(\x0b2*.google.cloud.retail.v2.ImportErrorsConfig\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12]\n\x13reconciliation_mode\x18\x05 \x01(\x0e2@.google.cloud.retail.v2.ImportProductsRequest.ReconciliationMode\x12!\n\x19notification_pubsub_topic\x18\x07 \x01(\t"T\n\x12ReconciliationMode\x12#\n\x1fRECONCILIATION_MODE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bINCREMENTAL\x10\x01\x12\x08\n\x04FULL\x10\x02"\xdc\x01\n\x17ImportUserEventsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12G\n\x0cinput_config\x18\x02 \x01(\x0b2,.google.cloud.retail.v2.UserEventInputConfigB\x03\xe0A\x02\x12A\n\rerrors_config\x18\x03 \x01(\x0b2*.google.cloud.retail.v2.ImportErrorsConfig"\xc5\x01\n\x1bImportCompletionDataRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12L\n\x0cinput_config\x18\x02 \x01(\x0b21.google.cloud.retail.v2.CompletionDataInputConfigB\x03\xe0A\x02\x12!\n\x19notification_pubsub_topic\x18\x03 \x01(\t"\xe9\x01\n\x12ProductInputConfig\x12L\n\x15product_inline_source\x18\x01 \x01(\x0b2+.google.cloud.retail.v2.ProductInlineSourceH\x00\x127\n\ngcs_source\x18\x02 \x01(\x0b2!.google.cloud.retail.v2.GcsSourceH\x00\x12B\n\x10big_query_source\x18\x03 \x01(\x0b2&.google.cloud.retail.v2.BigQuerySourceH\x00B\x08\n\x06source"\xff\x01\n\x14UserEventInputConfig\x12V\n\x18user_event_inline_source\x18\x01 \x01(\x0b2-.google.cloud.retail.v2.UserEventInlineSourceB\x03\xe0A\x02H\x00\x12<\n\ngcs_source\x18\x02 \x01(\x0b2!.google.cloud.retail.v2.GcsSourceB\x03\xe0A\x02H\x00\x12G\n\x10big_query_source\x18\x03 \x01(\x0b2&.google.cloud.retail.v2.BigQuerySourceB\x03\xe0A\x02H\x00B\x08\n\x06source"n\n\x19CompletionDataInputConfig\x12G\n\x10big_query_source\x18\x01 \x01(\x0b2&.google.cloud.retail.v2.BigQuerySourceB\x03\xe0A\x02H\x00B\x08\n\x06source"\xdb\x01\n\x0eImportMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rsuccess_count\x18\x03 \x01(\x03\x12\x15\n\rfailure_count\x18\x04 \x01(\x03\x12\x16\n\nrequest_id\x18\x05 \x01(\tB\x02\x18\x01\x12!\n\x19notification_pubsub_topic\x18\x06 \x01(\t"\x86\x01\n\x16ImportProductsResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12A\n\rerrors_config\x18\x02 \x01(\x0b2*.google.cloud.retail.v2.ImportErrorsConfig"\xd0\x01\n\x18ImportUserEventsResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12A\n\rerrors_config\x18\x02 \x01(\x0b2*.google.cloud.retail.v2.ImportErrorsConfig\x12F\n\x0eimport_summary\x18\x03 \x01(\x0b2..google.cloud.retail.v2.UserEventImportSummary"T\n\x16UserEventImportSummary\x12\x1b\n\x13joined_events_count\x18\x01 \x01(\x03\x12\x1d\n\x15unjoined_events_count\x18\x02 \x01(\x03"I\n\x1cImportCompletionDataResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.StatusB\xbc\x01\n\x1acom.google.cloud.retail.v2B\x11ImportConfigProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2.import_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.retail.v2B\x11ImportConfigProtoP\x01Z2cloud.google.com/go/retail/apiv2/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x16Google.Cloud.Retail.V2\xca\x02\x16Google\\Cloud\\Retail\\V2\xea\x02\x19Google::Cloud::Retail::V2'
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
    _globals['_GCSSOURCE']._serialized_start = 325
    _globals['_GCSSOURCE']._serialized_end = 382
    _globals['_BIGQUERYSOURCE']._serialized_start = 385
    _globals['_BIGQUERYSOURCE']._serialized_end = 573
    _globals['_PRODUCTINLINESOURCE']._serialized_start = 575
    _globals['_PRODUCTINLINESOURCE']._serialized_end = 652
    _globals['_USEREVENTINLINESOURCE']._serialized_start = 654
    _globals['_USEREVENTINLINESOURCE']._serialized_end = 738
    _globals['_IMPORTERRORSCONFIG']._serialized_start = 740
    _globals['_IMPORTERRORSCONFIG']._serialized_end = 797
    _globals['_IMPORTPRODUCTSREQUEST']._serialized_start = 800
    _globals['_IMPORTPRODUCTSREQUEST']._serialized_end = 1304
    _globals['_IMPORTPRODUCTSREQUEST_RECONCILIATIONMODE']._serialized_start = 1220
    _globals['_IMPORTPRODUCTSREQUEST_RECONCILIATIONMODE']._serialized_end = 1304
    _globals['_IMPORTUSEREVENTSREQUEST']._serialized_start = 1307
    _globals['_IMPORTUSEREVENTSREQUEST']._serialized_end = 1527
    _globals['_IMPORTCOMPLETIONDATAREQUEST']._serialized_start = 1530
    _globals['_IMPORTCOMPLETIONDATAREQUEST']._serialized_end = 1727
    _globals['_PRODUCTINPUTCONFIG']._serialized_start = 1730
    _globals['_PRODUCTINPUTCONFIG']._serialized_end = 1963
    _globals['_USEREVENTINPUTCONFIG']._serialized_start = 1966
    _globals['_USEREVENTINPUTCONFIG']._serialized_end = 2221
    _globals['_COMPLETIONDATAINPUTCONFIG']._serialized_start = 2223
    _globals['_COMPLETIONDATAINPUTCONFIG']._serialized_end = 2333
    _globals['_IMPORTMETADATA']._serialized_start = 2336
    _globals['_IMPORTMETADATA']._serialized_end = 2555
    _globals['_IMPORTPRODUCTSRESPONSE']._serialized_start = 2558
    _globals['_IMPORTPRODUCTSRESPONSE']._serialized_end = 2692
    _globals['_IMPORTUSEREVENTSRESPONSE']._serialized_start = 2695
    _globals['_IMPORTUSEREVENTSRESPONSE']._serialized_end = 2903
    _globals['_USEREVENTIMPORTSUMMARY']._serialized_start = 2905
    _globals['_USEREVENTIMPORTSUMMARY']._serialized_end = 2989
    _globals['_IMPORTCOMPLETIONDATARESPONSE']._serialized_start = 2991
    _globals['_IMPORTCOMPLETIONDATARESPONSE']._serialized_end = 3064