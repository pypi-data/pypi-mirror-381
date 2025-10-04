"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/datasources/v1beta/datasources.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.shopping.merchant.datasources.v1beta import datasourcetypes_pb2 as google_dot_shopping_dot_merchant_dot_datasources_dot_v1beta_dot_datasourcetypes__pb2
from ......google.shopping.merchant.datasources.v1beta import fileinputs_pb2 as google_dot_shopping_dot_merchant_dot_datasources_dot_v1beta_dot_fileinputs__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/shopping/merchant/datasources/v1beta/datasources.proto\x12+google.shopping.merchant.datasources.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1aAgoogle/shopping/merchant/datasources/v1beta/datasourcetypes.proto\x1a<google/shopping/merchant/datasources/v1beta/fileinputs.proto"\xc3\t\n\nDataSource\x12l\n\x1bprimary_product_data_source\x18\x04 \x01(\x0b2E.google.shopping.merchant.datasources.v1beta.PrimaryProductDataSourceH\x00\x12v\n supplemental_product_data_source\x18\x05 \x01(\x0b2J.google.shopping.merchant.datasources.v1beta.SupplementalProductDataSourceH\x00\x12l\n\x1blocal_inventory_data_source\x18\x06 \x01(\x0b2E.google.shopping.merchant.datasources.v1beta.LocalInventoryDataSourceH\x00\x12r\n\x1eregional_inventory_data_source\x18\x07 \x01(\x0b2H.google.shopping.merchant.datasources.v1beta.RegionalInventoryDataSourceH\x00\x12a\n\x15promotion_data_source\x18\x08 \x01(\x0b2@.google.shopping.merchant.datasources.v1beta.PromotionDataSourceH\x00\x12j\n\x1aproduct_review_data_source\x18\t \x01(\x0b2D.google.shopping.merchant.datasources.v1beta.ProductReviewDataSourceH\x00\x12l\n\x1bmerchant_review_data_source\x18\x0c \x01(\x0b2E.google.shopping.merchant.datasources.v1beta.MerchantReviewDataSourceH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1b\n\x0edata_source_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x02\x12Q\n\x05input\x18\n \x01(\x0e2=.google.shopping.merchant.datasources.v1beta.DataSource.InputB\x03\xe0A\x03\x12O\n\nfile_input\x18\x0b \x01(\x0b26.google.shopping.merchant.datasources.v1beta.FileInputB\x03\xe0A\x01"G\n\x05Input\x12\x15\n\x11INPUT_UNSPECIFIED\x10\x00\x12\x07\n\x03API\x10\x01\x12\x08\n\x04FILE\x10\x02\x12\x06\n\x02UI\x10\x03\x12\x0c\n\x08AUTOFEED\x10\x04:p\xeaAm\n%merchantapi.googleapis.com/DataSource\x12+accounts/{account}/dataSources/{datasource}*\x0bdataSources2\ndataSourceB\x06\n\x04Type"S\n\x14GetDataSourceRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%merchantapi.googleapis.com/DataSource"\x88\x01\n\x16ListDataSourcesRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%merchantapi.googleapis.com/DataSource\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x81\x01\n\x17ListDataSourcesResponse\x12M\n\x0cdata_sources\x18\x01 \x03(\x0b27.google.shopping.merchant.datasources.v1beta.DataSource\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xab\x01\n\x17CreateDataSourceRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%merchantapi.googleapis.com/DataSource\x12Q\n\x0bdata_source\x18\x02 \x01(\x0b27.google.shopping.merchant.datasources.v1beta.DataSourceB\x03\xe0A\x02"\xa2\x01\n\x17UpdateDataSourceRequest\x12Q\n\x0bdata_source\x18\x01 \x01(\x0b27.google.shopping.merchant.datasources.v1beta.DataSourceB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"U\n\x16FetchDataSourceRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%merchantapi.googleapis.com/DataSource"V\n\x17DeleteDataSourceRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%merchantapi.googleapis.com/DataSource2\xf9\n\n\x12DataSourcesService\x12\xcf\x01\n\rGetDataSource\x12A.google.shopping.merchant.datasources.v1beta.GetDataSourceRequest\x1a7.google.shopping.merchant.datasources.v1beta.DataSource"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/datasources/v1beta/{name=accounts/*/dataSources/*}\x12\xe2\x01\n\x0fListDataSources\x12C.google.shopping.merchant.datasources.v1beta.ListDataSourcesRequest\x1aD.google.shopping.merchant.datasources.v1beta.ListDataSourcesResponse"D\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/datasources/v1beta/{parent=accounts/*}/dataSources\x12\xf0\x01\n\x10CreateDataSource\x12D.google.shopping.merchant.datasources.v1beta.CreateDataSourceRequest\x1a7.google.shopping.merchant.datasources.v1beta.DataSource"]\xdaA\x12parent,data_source\x82\xd3\xe4\x93\x02B"3/datasources/v1beta/{parent=accounts/*}/dataSources:\x0bdata_source\x12\x81\x02\n\x10UpdateDataSource\x12D.google.shopping.merchant.datasources.v1beta.UpdateDataSourceRequest\x1a7.google.shopping.merchant.datasources.v1beta.DataSource"n\xdaA\x17data_source,update_mask\x82\xd3\xe4\x93\x02N2?/datasources/v1beta/{data_source.name=accounts/*/dataSources/*}:\x0bdata_source\x12\xb4\x01\n\x10DeleteDataSource\x12D.google.shopping.merchant.datasources.v1beta.DeleteDataSourceRequest\x1a\x16.google.protobuf.Empty"B\xdaA\x04name\x82\xd3\xe4\x93\x025*3/datasources/v1beta/{name=accounts/*/dataSources/*}\x12\xb4\x01\n\x0fFetchDataSource\x12C.google.shopping.merchant.datasources.v1beta.FetchDataSourceRequest\x1a\x16.google.protobuf.Empty"D\x82\xd3\xe4\x93\x02>"9/datasources/v1beta/{name=accounts/*/dataSources/*}:fetch:\x01*\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xbe\x03\n/com.google.shopping.merchant.datasources.v1betaB\x10DataSourcesProtoP\x01ZWcloud.google.com/go/shopping/merchant/datasources/apiv1beta/datasourcespb;datasourcespb\xaa\x02+Google.Shopping.Merchant.DataSources.V1Beta\xca\x02+Google\\Shopping\\Merchant\\DataSources\\V1beta\xea\x02/Google::Shopping::Merchant::DataSources::V1beta\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}\xeaAT\n%merchantapi.googleapis.com/Datasource\x12+accounts/{account}/dataSources/{datasource}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.datasources.v1beta.datasources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.shopping.merchant.datasources.v1betaB\x10DataSourcesProtoP\x01ZWcloud.google.com/go/shopping/merchant/datasources/apiv1beta/datasourcespb;datasourcespb\xaa\x02+Google.Shopping.Merchant.DataSources.V1Beta\xca\x02+Google\\Shopping\\Merchant\\DataSources\\V1beta\xea\x02/Google::Shopping::Merchant::DataSources::V1beta\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}\xeaAT\n%merchantapi.googleapis.com/Datasource\x12+accounts/{account}/dataSources/{datasource}'
    _globals['_DATASOURCE'].fields_by_name['name']._loaded_options = None
    _globals['_DATASOURCE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_DATASOURCE'].fields_by_name['data_source_id']._loaded_options = None
    _globals['_DATASOURCE'].fields_by_name['data_source_id']._serialized_options = b'\xe0A\x03'
    _globals['_DATASOURCE'].fields_by_name['display_name']._loaded_options = None
    _globals['_DATASOURCE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_DATASOURCE'].fields_by_name['input']._loaded_options = None
    _globals['_DATASOURCE'].fields_by_name['input']._serialized_options = b'\xe0A\x03'
    _globals['_DATASOURCE'].fields_by_name['file_input']._loaded_options = None
    _globals['_DATASOURCE'].fields_by_name['file_input']._serialized_options = b'\xe0A\x01'
    _globals['_DATASOURCE']._loaded_options = None
    _globals['_DATASOURCE']._serialized_options = b'\xeaAm\n%merchantapi.googleapis.com/DataSource\x12+accounts/{account}/dataSources/{datasource}*\x0bdataSources2\ndataSource'
    _globals['_GETDATASOURCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATASOURCEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%merchantapi.googleapis.com/DataSource"
    _globals['_LISTDATASOURCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATASOURCESREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%merchantapi.googleapis.com/DataSource"
    _globals['_LISTDATASOURCESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTDATASOURCESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATASOURCESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTDATASOURCESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEDATASOURCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDATASOURCEREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%merchantapi.googleapis.com/DataSource"
    _globals['_CREATEDATASOURCEREQUEST'].fields_by_name['data_source']._loaded_options = None
    _globals['_CREATEDATASOURCEREQUEST'].fields_by_name['data_source']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDATASOURCEREQUEST'].fields_by_name['data_source']._loaded_options = None
    _globals['_UPDATEDATASOURCEREQUEST'].fields_by_name['data_source']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDATASOURCEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEDATASOURCEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_FETCHDATASOURCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_FETCHDATASOURCEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%merchantapi.googleapis.com/DataSource"
    _globals['_DELETEDATASOURCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDATASOURCEREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%merchantapi.googleapis.com/DataSource"
    _globals['_DATASOURCESSERVICE']._loaded_options = None
    _globals['_DATASOURCESSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_DATASOURCESSERVICE'].methods_by_name['GetDataSource']._loaded_options = None
    _globals['_DATASOURCESSERVICE'].methods_by_name['GetDataSource']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/datasources/v1beta/{name=accounts/*/dataSources/*}'
    _globals['_DATASOURCESSERVICE'].methods_by_name['ListDataSources']._loaded_options = None
    _globals['_DATASOURCESSERVICE'].methods_by_name['ListDataSources']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/datasources/v1beta/{parent=accounts/*}/dataSources'
    _globals['_DATASOURCESSERVICE'].methods_by_name['CreateDataSource']._loaded_options = None
    _globals['_DATASOURCESSERVICE'].methods_by_name['CreateDataSource']._serialized_options = b'\xdaA\x12parent,data_source\x82\xd3\xe4\x93\x02B"3/datasources/v1beta/{parent=accounts/*}/dataSources:\x0bdata_source'
    _globals['_DATASOURCESSERVICE'].methods_by_name['UpdateDataSource']._loaded_options = None
    _globals['_DATASOURCESSERVICE'].methods_by_name['UpdateDataSource']._serialized_options = b'\xdaA\x17data_source,update_mask\x82\xd3\xe4\x93\x02N2?/datasources/v1beta/{data_source.name=accounts/*/dataSources/*}:\x0bdata_source'
    _globals['_DATASOURCESSERVICE'].methods_by_name['DeleteDataSource']._loaded_options = None
    _globals['_DATASOURCESSERVICE'].methods_by_name['DeleteDataSource']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025*3/datasources/v1beta/{name=accounts/*/dataSources/*}'
    _globals['_DATASOURCESSERVICE'].methods_by_name['FetchDataSource']._loaded_options = None
    _globals['_DATASOURCESSERVICE'].methods_by_name['FetchDataSource']._serialized_options = b'\x82\xd3\xe4\x93\x02>"9/datasources/v1beta/{name=accounts/*/dataSources/*}:fetch:\x01*'
    _globals['_DATASOURCE']._serialized_start = 418
    _globals['_DATASOURCE']._serialized_end = 1637
    _globals['_DATASOURCE_INPUT']._serialized_start = 1444
    _globals['_DATASOURCE_INPUT']._serialized_end = 1515
    _globals['_GETDATASOURCEREQUEST']._serialized_start = 1639
    _globals['_GETDATASOURCEREQUEST']._serialized_end = 1722
    _globals['_LISTDATASOURCESREQUEST']._serialized_start = 1725
    _globals['_LISTDATASOURCESREQUEST']._serialized_end = 1861
    _globals['_LISTDATASOURCESRESPONSE']._serialized_start = 1864
    _globals['_LISTDATASOURCESRESPONSE']._serialized_end = 1993
    _globals['_CREATEDATASOURCEREQUEST']._serialized_start = 1996
    _globals['_CREATEDATASOURCEREQUEST']._serialized_end = 2167
    _globals['_UPDATEDATASOURCEREQUEST']._serialized_start = 2170
    _globals['_UPDATEDATASOURCEREQUEST']._serialized_end = 2332
    _globals['_FETCHDATASOURCEREQUEST']._serialized_start = 2334
    _globals['_FETCHDATASOURCEREQUEST']._serialized_end = 2419
    _globals['_DELETEDATASOURCEREQUEST']._serialized_start = 2421
    _globals['_DELETEDATASOURCEREQUEST']._serialized_end = 2507
    _globals['_DATASOURCESSERVICE']._serialized_start = 2510
    _globals['_DATASOURCESSERVICE']._serialized_end = 3911