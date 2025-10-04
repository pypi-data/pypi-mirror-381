"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/issueresolution/v1/aggregateproductstatuses.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nJgoogle/shopping/merchant/issueresolution/v1/aggregateproductstatuses.proto\x12+google.shopping.merchant.issueresolution.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/shopping/type/types.proto"\xb6\x01\n#ListAggregateProductStatusesRequest\x12I\n\x06parent\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\x121merchantapi.googleapis.com/AggregateProductStatus\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"\xa8\x01\n$ListAggregateProductStatusesResponse\x12g\n\x1aaggregate_product_statuses\x18\x01 \x03(\x0b2C.google.shopping.merchant.issueresolution.v1.AggregateProductStatus\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x94\t\n\x16AggregateProductStatus\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12V\n\x11reporting_context\x18\x03 \x01(\x0e2;.google.shopping.type.ReportingContext.ReportingContextEnum\x12\x0f\n\x07country\x18\x04 \x01(\t\x12X\n\x05stats\x18\x05 \x01(\x0b2I.google.shopping.merchant.issueresolution.v1.AggregateProductStatus.Stats\x12m\n\x11item_level_issues\x18\x06 \x03(\x0b2R.google.shopping.merchant.issueresolution.v1.AggregateProductStatus.ItemLevelIssue\x1ag\n\x05Stats\x12\x14\n\x0cactive_count\x18\x01 \x01(\x03\x12\x15\n\rpending_count\x18\x02 \x01(\x03\x12\x19\n\x11disapproved_count\x18\x03 \x01(\x03\x12\x16\n\x0eexpiring_count\x18\x04 \x01(\x03\x1a\x97\x04\n\x0eItemLevelIssue\x12\x0c\n\x04code\x18\x01 \x01(\t\x12m\n\x08severity\x18\x02 \x01(\x0e2[.google.shopping.merchant.issueresolution.v1.AggregateProductStatus.ItemLevelIssue.Severity\x12q\n\nresolution\x18\x03 \x01(\x0e2].google.shopping.merchant.issueresolution.v1.AggregateProductStatus.ItemLevelIssue.Resolution\x12\x11\n\tattribute\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x06 \x01(\t\x12\x0e\n\x06detail\x18\x07 \x01(\t\x12\x19\n\x11documentation_uri\x18\x08 \x01(\t\x12\x15\n\rproduct_count\x18\t \x01(\x03"T\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x10\n\x0cNOT_IMPACTED\x10\x01\x12\x0b\n\x07DEMOTED\x10\x02\x12\x0f\n\x0bDISAPPROVED\x10\x03"U\n\nResolution\x12\x1a\n\x16RESOLUTION_UNSPECIFIED\x10\x00\x12\x13\n\x0fMERCHANT_ACTION\x10\x01\x12\x16\n\x12PENDING_PROCESSING\x10\x02:\xb1\x01\xeaA\xad\x01\n1merchantapi.googleapis.com/AggregateProductStatus\x12Faccounts/{account}/aggregateProductStatuses/{aggregate_product_status}*\x18aggregateProductStatuses2\x16aggregateProductStatus2\x83\x03\n\x1fAggregateProductStatusesService\x12\x96\x02\n\x1cListAggregateProductStatuses\x12P.google.shopping.merchant.issueresolution.v1.ListAggregateProductStatusesRequest\x1aQ.google.shopping.merchant.issueresolution.v1.ListAggregateProductStatusesResponse"Q\xdaA\x06parent\x82\xd3\xe4\x93\x02B\x12@/issueresolution/v1/{parent=accounts/*}/aggregateProductStatuses\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xc1\x02\n/com.google.shopping.merchant.issueresolution.v1B\x1dAggregateProductStatusesProtoP\x01Z_cloud.google.com/go/shopping/merchant/issueresolution/apiv1/issueresolutionpb;issueresolutionpb\xaa\x02+Google.Shopping.Merchant.IssueResolution.V1\xca\x02+Google\\Shopping\\Merchant\\IssueResolution\\V1\xea\x02/Google::Shopping::Merchant::IssueResolution::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.issueresolution.v1.aggregateproductstatuses_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.shopping.merchant.issueresolution.v1B\x1dAggregateProductStatusesProtoP\x01Z_cloud.google.com/go/shopping/merchant/issueresolution/apiv1/issueresolutionpb;issueresolutionpb\xaa\x02+Google.Shopping.Merchant.IssueResolution.V1\xca\x02+Google\\Shopping\\Merchant\\IssueResolution\\V1\xea\x02/Google::Shopping::Merchant::IssueResolution::V1'
    _globals['_LISTAGGREGATEPRODUCTSTATUSESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTAGGREGATEPRODUCTSTATUSESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA3\x121merchantapi.googleapis.com/AggregateProductStatus'
    _globals['_LISTAGGREGATEPRODUCTSTATUSESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTAGGREGATEPRODUCTSTATUSESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTAGGREGATEPRODUCTSTATUSESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTAGGREGATEPRODUCTSTATUSESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTAGGREGATEPRODUCTSTATUSESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTAGGREGATEPRODUCTSTATUSESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_AGGREGATEPRODUCTSTATUS'].fields_by_name['name']._loaded_options = None
    _globals['_AGGREGATEPRODUCTSTATUS'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_AGGREGATEPRODUCTSTATUS']._loaded_options = None
    _globals['_AGGREGATEPRODUCTSTATUS']._serialized_options = b'\xeaA\xad\x01\n1merchantapi.googleapis.com/AggregateProductStatus\x12Faccounts/{account}/aggregateProductStatuses/{aggregate_product_status}*\x18aggregateProductStatuses2\x16aggregateProductStatus'
    _globals['_AGGREGATEPRODUCTSTATUSESSERVICE']._loaded_options = None
    _globals['_AGGREGATEPRODUCTSTATUSESSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_AGGREGATEPRODUCTSTATUSESSERVICE'].methods_by_name['ListAggregateProductStatuses']._loaded_options = None
    _globals['_AGGREGATEPRODUCTSTATUSESSERVICE'].methods_by_name['ListAggregateProductStatuses']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02B\x12@/issueresolution/v1/{parent=accounts/*}/aggregateProductStatuses'
    _globals['_LISTAGGREGATEPRODUCTSTATUSESREQUEST']._serialized_start = 273
    _globals['_LISTAGGREGATEPRODUCTSTATUSESREQUEST']._serialized_end = 455
    _globals['_LISTAGGREGATEPRODUCTSTATUSESRESPONSE']._serialized_start = 458
    _globals['_LISTAGGREGATEPRODUCTSTATUSESRESPONSE']._serialized_end = 626
    _globals['_AGGREGATEPRODUCTSTATUS']._serialized_start = 629
    _globals['_AGGREGATEPRODUCTSTATUS']._serialized_end = 1801
    _globals['_AGGREGATEPRODUCTSTATUS_STATS']._serialized_start = 980
    _globals['_AGGREGATEPRODUCTSTATUS_STATS']._serialized_end = 1083
    _globals['_AGGREGATEPRODUCTSTATUS_ITEMLEVELISSUE']._serialized_start = 1086
    _globals['_AGGREGATEPRODUCTSTATUS_ITEMLEVELISSUE']._serialized_end = 1621
    _globals['_AGGREGATEPRODUCTSTATUS_ITEMLEVELISSUE_SEVERITY']._serialized_start = 1450
    _globals['_AGGREGATEPRODUCTSTATUS_ITEMLEVELISSUE_SEVERITY']._serialized_end = 1534
    _globals['_AGGREGATEPRODUCTSTATUS_ITEMLEVELISSUE_RESOLUTION']._serialized_start = 1536
    _globals['_AGGREGATEPRODUCTSTATUS_ITEMLEVELISSUE_RESOLUTION']._serialized_end = 1621
    _globals['_AGGREGATEPRODUCTSTATUSESSERVICE']._serialized_start = 1804
    _globals['_AGGREGATEPRODUCTSTATUSESSERVICE']._serialized_end = 2191