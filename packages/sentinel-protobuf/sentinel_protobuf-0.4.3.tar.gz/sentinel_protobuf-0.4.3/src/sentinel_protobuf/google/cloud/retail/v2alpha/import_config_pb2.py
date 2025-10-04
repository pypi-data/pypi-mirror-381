"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2alpha/import_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2alpha import product_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_product__pb2
from .....google.cloud.retail.v2alpha import user_event_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_user__event__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from .....google.type import date_pb2 as google_dot_type_dot_date__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/retail/v2alpha/import_config.proto\x12\x1bgoogle.cloud.retail.v2alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/retail/v2alpha/product.proto\x1a,google/cloud/retail/v2alpha/user_event.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x16google/type/date.proto"9\n\tGcsSource\x12\x17\n\ninput_uris\x18\x01 \x03(\tB\x03\xe0A\x02\x12\x13\n\x0bdata_schema\x18\x02 \x01(\t"\xbc\x01\n\x0eBigQuerySource\x12+\n\x0epartition_date\x18\x06 \x01(\x0b2\x11.google.type.DateH\x00\x12\x12\n\nproject_id\x18\x05 \x01(\t\x12\x17\n\ndataset_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x17\n\x0fgcs_staging_dir\x18\x03 \x01(\t\x12\x13\n\x0bdata_schema\x18\x04 \x01(\tB\x0b\n\tpartition"R\n\x13ProductInlineSource\x12;\n\x08products\x18\x01 \x03(\x0b2$.google.cloud.retail.v2alpha.ProductB\x03\xe0A\x02"Y\n\x15UserEventInlineSource\x12@\n\x0buser_events\x18\x01 \x03(\x0b2&.google.cloud.retail.v2alpha.UserEventB\x03\xe0A\x02"9\n\x12ImportErrorsConfig\x12\x14\n\ngcs_prefix\x18\x01 \x01(\tH\x00B\r\n\x0bdestination"\xaf\x04\n\x15ImportProductsRequest\x124\n\x06parent\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cretail.googleapis.com/Branch\x12\x16\n\nrequest_id\x18\x06 \x01(\tB\x02\x18\x01\x12J\n\x0cinput_config\x18\x02 \x01(\x0b2/.google.cloud.retail.v2alpha.ProductInputConfigB\x03\xe0A\x02\x12F\n\rerrors_config\x18\x03 \x01(\x0b2/.google.cloud.retail.v2alpha.ImportErrorsConfig\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12b\n\x13reconciliation_mode\x18\x05 \x01(\x0e2E.google.cloud.retail.v2alpha.ImportProductsRequest.ReconciliationMode\x12!\n\x19notification_pubsub_topic\x18\x07 \x01(\t\x12&\n\x1eskip_default_branch_protection\x18\x08 \x01(\x08"T\n\x12ReconciliationMode\x12#\n\x1fRECONCILIATION_MODE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bINCREMENTAL\x10\x01\x12\x08\n\x04FULL\x10\x02"\xe6\x01\n\x17ImportUserEventsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12L\n\x0cinput_config\x18\x02 \x01(\x0b21.google.cloud.retail.v2alpha.UserEventInputConfigB\x03\xe0A\x02\x12F\n\rerrors_config\x18\x03 \x01(\x0b2/.google.cloud.retail.v2alpha.ImportErrorsConfig"\xca\x01\n\x1bImportCompletionDataRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12Q\n\x0cinput_config\x18\x02 \x01(\x0b26.google.cloud.retail.v2alpha.CompletionDataInputConfigB\x03\xe0A\x02\x12!\n\x19notification_pubsub_topic\x18\x03 \x01(\t"\xf8\x01\n\x12ProductInputConfig\x12Q\n\x15product_inline_source\x18\x01 \x01(\x0b20.google.cloud.retail.v2alpha.ProductInlineSourceH\x00\x12<\n\ngcs_source\x18\x02 \x01(\x0b2&.google.cloud.retail.v2alpha.GcsSourceH\x00\x12G\n\x10big_query_source\x18\x03 \x01(\x0b2+.google.cloud.retail.v2alpha.BigQuerySourceH\x00B\x08\n\x06source"\x8e\x02\n\x14UserEventInputConfig\x12[\n\x18user_event_inline_source\x18\x01 \x01(\x0b22.google.cloud.retail.v2alpha.UserEventInlineSourceB\x03\xe0A\x02H\x00\x12A\n\ngcs_source\x18\x02 \x01(\x0b2&.google.cloud.retail.v2alpha.GcsSourceB\x03\xe0A\x02H\x00\x12L\n\x10big_query_source\x18\x03 \x01(\x0b2+.google.cloud.retail.v2alpha.BigQuerySourceB\x03\xe0A\x02H\x00B\x08\n\x06source"s\n\x19CompletionDataInputConfig\x12L\n\x10big_query_source\x18\x01 \x01(\x0b2+.google.cloud.retail.v2alpha.BigQuerySourceB\x03\xe0A\x02H\x00B\x08\n\x06source"\xc1\x02\n\x0eImportMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rsuccess_count\x18\x03 \x01(\x03\x12\x15\n\rfailure_count\x18\x04 \x01(\x03\x12\x16\n\nrequest_id\x18\x05 \x01(\tB\x02\x18\x01\x12!\n\x19notification_pubsub_topic\x18\x06 \x01(\t\x12d\n transformed_user_events_metadata\x18\x07 \x01(\x0b2:.google.cloud.retail.v2alpha.TransformedUserEventsMetadata"^\n\x1dTransformedUserEventsMetadata\x12\x1b\n\x13source_events_count\x18\x01 \x01(\x03\x12 \n\x18transformed_events_count\x18\x02 \x01(\x03"\x8b\x01\n\x16ImportProductsResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12F\n\rerrors_config\x18\x02 \x01(\x0b2/.google.cloud.retail.v2alpha.ImportErrorsConfig"\xda\x01\n\x18ImportUserEventsResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12F\n\rerrors_config\x18\x02 \x01(\x0b2/.google.cloud.retail.v2alpha.ImportErrorsConfig\x12K\n\x0eimport_summary\x18\x03 \x01(\x0b23.google.cloud.retail.v2alpha.UserEventImportSummary"T\n\x16UserEventImportSummary\x12\x1b\n\x13joined_events_count\x18\x01 \x01(\x03\x12\x1d\n\x15unjoined_events_count\x18\x02 \x01(\x03"I\n\x1cImportCompletionDataResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.StatusB\xd5\x01\n\x1fcom.google.cloud.retail.v2alphaB\x11ImportConfigProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2alpha.import_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.retail.v2alphaB\x11ImportConfigProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alpha'
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
    _globals['_GCSSOURCE']._serialized_start = 345
    _globals['_GCSSOURCE']._serialized_end = 402
    _globals['_BIGQUERYSOURCE']._serialized_start = 405
    _globals['_BIGQUERYSOURCE']._serialized_end = 593
    _globals['_PRODUCTINLINESOURCE']._serialized_start = 595
    _globals['_PRODUCTINLINESOURCE']._serialized_end = 677
    _globals['_USEREVENTINLINESOURCE']._serialized_start = 679
    _globals['_USEREVENTINLINESOURCE']._serialized_end = 768
    _globals['_IMPORTERRORSCONFIG']._serialized_start = 770
    _globals['_IMPORTERRORSCONFIG']._serialized_end = 827
    _globals['_IMPORTPRODUCTSREQUEST']._serialized_start = 830
    _globals['_IMPORTPRODUCTSREQUEST']._serialized_end = 1389
    _globals['_IMPORTPRODUCTSREQUEST_RECONCILIATIONMODE']._serialized_start = 1305
    _globals['_IMPORTPRODUCTSREQUEST_RECONCILIATIONMODE']._serialized_end = 1389
    _globals['_IMPORTUSEREVENTSREQUEST']._serialized_start = 1392
    _globals['_IMPORTUSEREVENTSREQUEST']._serialized_end = 1622
    _globals['_IMPORTCOMPLETIONDATAREQUEST']._serialized_start = 1625
    _globals['_IMPORTCOMPLETIONDATAREQUEST']._serialized_end = 1827
    _globals['_PRODUCTINPUTCONFIG']._serialized_start = 1830
    _globals['_PRODUCTINPUTCONFIG']._serialized_end = 2078
    _globals['_USEREVENTINPUTCONFIG']._serialized_start = 2081
    _globals['_USEREVENTINPUTCONFIG']._serialized_end = 2351
    _globals['_COMPLETIONDATAINPUTCONFIG']._serialized_start = 2353
    _globals['_COMPLETIONDATAINPUTCONFIG']._serialized_end = 2468
    _globals['_IMPORTMETADATA']._serialized_start = 2471
    _globals['_IMPORTMETADATA']._serialized_end = 2792
    _globals['_TRANSFORMEDUSEREVENTSMETADATA']._serialized_start = 2794
    _globals['_TRANSFORMEDUSEREVENTSMETADATA']._serialized_end = 2888
    _globals['_IMPORTPRODUCTSRESPONSE']._serialized_start = 2891
    _globals['_IMPORTPRODUCTSRESPONSE']._serialized_end = 3030
    _globals['_IMPORTUSEREVENTSRESPONSE']._serialized_start = 3033
    _globals['_IMPORTUSEREVENTSRESPONSE']._serialized_end = 3251
    _globals['_USEREVENTIMPORTSUMMARY']._serialized_start = 3253
    _globals['_USEREVENTIMPORTSUMMARY']._serialized_end = 3337
    _globals['_IMPORTCOMPLETIONDATARESPONSE']._serialized_start = 3339
    _globals['_IMPORTCOMPLETIONDATARESPONSE']._serialized_end = 3412