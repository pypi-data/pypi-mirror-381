"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/conversions/v1/conversionsources.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/shopping/merchant/conversions/v1/conversionsources.proto\x12\'google.shopping.merchant.conversions.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x9a\x06\n\x10ConversionSource\x12b\n\x15google_analytics_link\x18\x03 \x01(\x0b2<.google.shopping.merchant.conversions.v1.GoogleAnalyticsLinkB\x03\xe0A\x05H\x00\x12i\n\x1bmerchant_center_destination\x18\x04 \x01(\x0b2B.google.shopping.merchant.conversions.v1.MerchantCenterDestinationH\x00\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x08\x12S\n\x05state\x18\x05 \x01(\x0e2?.google.shopping.merchant.conversions.v1.ConversionSource.StateB\x03\xe0A\x03\x124\n\x0bexpire_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12]\n\ncontroller\x18\x07 \x01(\x0e2D.google.shopping.merchant.conversions.v1.ConversionSource.ControllerB\x03\xe0A\x03"E\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x0c\n\x08ARCHIVED\x10\x02\x12\x0b\n\x07PENDING\x10\x03"N\n\nController\x12\x1a\n\x16CONTROLLER_UNSPECIFIED\x10\x00\x12\x0c\n\x08MERCHANT\x10\x01\x12\x16\n\x12YOUTUBE_AFFILIATES\x10\x02:\x90\x01\xeaA\x8c\x01\n+merchantapi.googleapis.com/ConversionSource\x128accounts/{account}/conversionSources/{conversion_source}*\x11conversionSources2\x10conversionSourceB\r\n\x0bsource_data"\xe7\x04\n\x13AttributionSettings\x12-\n attribution_lookback_window_days\x18\x01 \x01(\x05B\x03\xe0A\x02\x12m\n\x11attribution_model\x18\x02 \x01(\x0e2M.google.shopping.merchant.conversions.v1.AttributionSettings.AttributionModelB\x03\xe0A\x02\x12l\n\x0fconversion_type\x18\x03 \x03(\x0b2K.google.shopping.merchant.conversions.v1.AttributionSettings.ConversionTypeB\x06\xe0A\x06\xe0A\x05\x1a8\n\x0eConversionType\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x13\n\x06report\x18\x02 \x01(\x08B\x03\xe0A\x03"\x89\x02\n\x10AttributionModel\x12!\n\x1dATTRIBUTION_MODEL_UNSPECIFIED\x10\x00\x12\x1c\n\x18CROSS_CHANNEL_LAST_CLICK\x10\x01\x12\x1c\n\x18ADS_PREFERRED_LAST_CLICK\x10\x02\x12\x1d\n\x19CROSS_CHANNEL_DATA_DRIVEN\x10\x05\x12\x1d\n\x19CROSS_CHANNEL_FIRST_CLICK\x10\x06\x12\x18\n\x14CROSS_CHANNEL_LINEAR\x10\x07\x12 \n\x1cCROSS_CHANNEL_POSITION_BASED\x10\x08\x12\x1c\n\x18CROSS_CHANNEL_TIME_DECAY\x10\t"\xaa\x01\n\x13GoogleAnalyticsLink\x12\x1b\n\x0bproperty_id\x18\x01 \x01(\x03B\x06\xe0A\x02\xe0A\x05\x12_\n\x14attribution_settings\x18\x02 \x01(\x0b2<.google.shopping.merchant.conversions.v1.AttributionSettingsB\x03\xe0A\x03\x12\x15\n\x08property\x18\x03 \x01(\tB\x03\xe0A\x03"\xcd\x01\n\x19MerchantCenterDestination\x12\x18\n\x0bdestination\x18\x01 \x01(\tB\x03\xe0A\x03\x12_\n\x14attribution_settings\x18\x02 \x01(\x0b2<.google.shopping.merchant.conversions.v1.AttributionSettingsB\x03\xe0A\x02\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rcurrency_code\x18\x04 \x01(\tB\x03\xe0A\x02"\xbf\x01\n\x1dCreateConversionSourceRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+merchantapi.googleapis.com/ConversionSource\x12Y\n\x11conversion_source\x18\x02 \x01(\x0b29.google.shopping.merchant.conversions.v1.ConversionSourceB\x03\xe0A\x02"\xb0\x01\n\x1dUpdateConversionSourceRequest\x12Y\n\x11conversion_source\x18\x01 \x01(\x0b29.google.shopping.merchant.conversions.v1.ConversionSourceB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"b\n\x1dDeleteConversionSourceRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+merchantapi.googleapis.com/ConversionSource"d\n\x1fUndeleteConversionSourceRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+merchantapi.googleapis.com/ConversionSource"_\n\x1aGetConversionSourceRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+merchantapi.googleapis.com/ConversionSource"\xaf\x01\n\x1cListConversionSourcesRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+merchantapi.googleapis.com/ConversionSource\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cshow_deleted\x18\x04 \x01(\x08B\x03\xe0A\x01"\x8f\x01\n\x1dListConversionSourcesResponse\x12U\n\x12conversion_sources\x18\x01 \x03(\x0b29.google.shopping.merchant.conversions.v1.ConversionSource\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x8e\x0c\n\x18ConversionSourcesService\x12\x88\x02\n\x16CreateConversionSource\x12F.google.shopping.merchant.conversions.v1.CreateConversionSourceRequest\x1a9.google.shopping.merchant.conversions.v1.ConversionSource"k\xdaA\x18parent,conversion_source\x82\xd3\xe4\x93\x02J"5/conversions/v1/{parent=accounts/*}/conversionSources:\x11conversion_source\x12\xa0\x02\n\x16UpdateConversionSource\x12F.google.shopping.merchant.conversions.v1.UpdateConversionSourceRequest\x1a9.google.shopping.merchant.conversions.v1.ConversionSource"\x82\x01\xdaA\x1dconversion_source,update_mask\x82\xd3\xe4\x93\x02\\2G/conversions/v1/{conversion_source.name=accounts/*/conversionSources/*}:\x11conversion_source\x12\xbe\x01\n\x16DeleteConversionSource\x12F.google.shopping.merchant.conversions.v1.DeleteConversionSourceRequest\x1a\x16.google.protobuf.Empty"D\xdaA\x04name\x82\xd3\xe4\x93\x027*5/conversions/v1/{name=accounts/*/conversionSources/*}\x12\xea\x01\n\x18UndeleteConversionSource\x12H.google.shopping.merchant.conversions.v1.UndeleteConversionSourceRequest\x1a9.google.shopping.merchant.conversions.v1.ConversionSource"I\x82\xd3\xe4\x93\x02C">/conversions/v1/{name=accounts/*/conversionSources/*}:undelete:\x01*\x12\xdb\x01\n\x13GetConversionSource\x12C.google.shopping.merchant.conversions.v1.GetConversionSourceRequest\x1a9.google.shopping.merchant.conversions.v1.ConversionSource"D\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/conversions/v1/{name=accounts/*/conversionSources/*}\x12\xee\x01\n\x15ListConversionSources\x12E.google.shopping.merchant.conversions.v1.ListConversionSourcesRequest\x1aF.google.shopping.merchant.conversions.v1.ListConversionSourcesResponse"F\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/conversions/v1/{parent=accounts/*}/conversionSources\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xd9\x02\n+com.google.shopping.merchant.conversions.v1B\x16ConversionSourcesProtoP\x01ZScloud.google.com/go/shopping/merchant/conversions/apiv1/conversionspb;conversionspb\xaa\x02\'Google.Shopping.Merchant.Conversions.V1\xca\x02\'Google\\Shopping\\Merchant\\Conversions\\V1\xea\x02+Google::Shopping::Merchant::Conversions::V1\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.conversions.v1.conversionsources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n+com.google.shopping.merchant.conversions.v1B\x16ConversionSourcesProtoP\x01ZScloud.google.com/go/shopping/merchant/conversions/apiv1/conversionspb;conversionspb\xaa\x02\'Google.Shopping.Merchant.Conversions.V1\xca\x02\'Google\\Shopping\\Merchant\\Conversions\\V1\xea\x02+Google::Shopping::Merchant::Conversions::V1\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}'
    _globals['_CONVERSIONSOURCE'].fields_by_name['google_analytics_link']._loaded_options = None
    _globals['_CONVERSIONSOURCE'].fields_by_name['google_analytics_link']._serialized_options = b'\xe0A\x05'
    _globals['_CONVERSIONSOURCE'].fields_by_name['name']._loaded_options = None
    _globals['_CONVERSIONSOURCE'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x08'
    _globals['_CONVERSIONSOURCE'].fields_by_name['state']._loaded_options = None
    _globals['_CONVERSIONSOURCE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONSOURCE'].fields_by_name['expire_time']._loaded_options = None
    _globals['_CONVERSIONSOURCE'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONSOURCE'].fields_by_name['controller']._loaded_options = None
    _globals['_CONVERSIONSOURCE'].fields_by_name['controller']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSIONSOURCE']._loaded_options = None
    _globals['_CONVERSIONSOURCE']._serialized_options = b'\xeaA\x8c\x01\n+merchantapi.googleapis.com/ConversionSource\x128accounts/{account}/conversionSources/{conversion_source}*\x11conversionSources2\x10conversionSource'
    _globals['_ATTRIBUTIONSETTINGS_CONVERSIONTYPE'].fields_by_name['name']._loaded_options = None
    _globals['_ATTRIBUTIONSETTINGS_CONVERSIONTYPE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_ATTRIBUTIONSETTINGS_CONVERSIONTYPE'].fields_by_name['report']._loaded_options = None
    _globals['_ATTRIBUTIONSETTINGS_CONVERSIONTYPE'].fields_by_name['report']._serialized_options = b'\xe0A\x03'
    _globals['_ATTRIBUTIONSETTINGS'].fields_by_name['attribution_lookback_window_days']._loaded_options = None
    _globals['_ATTRIBUTIONSETTINGS'].fields_by_name['attribution_lookback_window_days']._serialized_options = b'\xe0A\x02'
    _globals['_ATTRIBUTIONSETTINGS'].fields_by_name['attribution_model']._loaded_options = None
    _globals['_ATTRIBUTIONSETTINGS'].fields_by_name['attribution_model']._serialized_options = b'\xe0A\x02'
    _globals['_ATTRIBUTIONSETTINGS'].fields_by_name['conversion_type']._loaded_options = None
    _globals['_ATTRIBUTIONSETTINGS'].fields_by_name['conversion_type']._serialized_options = b'\xe0A\x06\xe0A\x05'
    _globals['_GOOGLEANALYTICSLINK'].fields_by_name['property_id']._loaded_options = None
    _globals['_GOOGLEANALYTICSLINK'].fields_by_name['property_id']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_GOOGLEANALYTICSLINK'].fields_by_name['attribution_settings']._loaded_options = None
    _globals['_GOOGLEANALYTICSLINK'].fields_by_name['attribution_settings']._serialized_options = b'\xe0A\x03'
    _globals['_GOOGLEANALYTICSLINK'].fields_by_name['property']._loaded_options = None
    _globals['_GOOGLEANALYTICSLINK'].fields_by_name['property']._serialized_options = b'\xe0A\x03'
    _globals['_MERCHANTCENTERDESTINATION'].fields_by_name['destination']._loaded_options = None
    _globals['_MERCHANTCENTERDESTINATION'].fields_by_name['destination']._serialized_options = b'\xe0A\x03'
    _globals['_MERCHANTCENTERDESTINATION'].fields_by_name['attribution_settings']._loaded_options = None
    _globals['_MERCHANTCENTERDESTINATION'].fields_by_name['attribution_settings']._serialized_options = b'\xe0A\x02'
    _globals['_MERCHANTCENTERDESTINATION'].fields_by_name['display_name']._loaded_options = None
    _globals['_MERCHANTCENTERDESTINATION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_MERCHANTCENTERDESTINATION'].fields_by_name['currency_code']._loaded_options = None
    _globals['_MERCHANTCENTERDESTINATION'].fields_by_name['currency_code']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECONVERSIONSOURCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECONVERSIONSOURCEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+merchantapi.googleapis.com/ConversionSource'
    _globals['_CREATECONVERSIONSOURCEREQUEST'].fields_by_name['conversion_source']._loaded_options = None
    _globals['_CREATECONVERSIONSOURCEREQUEST'].fields_by_name['conversion_source']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONVERSIONSOURCEREQUEST'].fields_by_name['conversion_source']._loaded_options = None
    _globals['_UPDATECONVERSIONSOURCEREQUEST'].fields_by_name['conversion_source']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECONVERSIONSOURCEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECONVERSIONSOURCEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_DELETECONVERSIONSOURCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECONVERSIONSOURCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+merchantapi.googleapis.com/ConversionSource'
    _globals['_UNDELETECONVERSIONSOURCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UNDELETECONVERSIONSOURCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+merchantapi.googleapis.com/ConversionSource'
    _globals['_GETCONVERSIONSOURCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONVERSIONSOURCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+merchantapi.googleapis.com/ConversionSource'
    _globals['_LISTCONVERSIONSOURCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONVERSIONSOURCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+merchantapi.googleapis.com/ConversionSource'
    _globals['_LISTCONVERSIONSOURCESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCONVERSIONSOURCESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONVERSIONSOURCESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCONVERSIONSOURCESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONVERSIONSOURCESREQUEST'].fields_by_name['show_deleted']._loaded_options = None
    _globals['_LISTCONVERSIONSOURCESREQUEST'].fields_by_name['show_deleted']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSIONSOURCESSERVICE']._loaded_options = None
    _globals['_CONVERSIONSOURCESSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_CONVERSIONSOURCESSERVICE'].methods_by_name['CreateConversionSource']._loaded_options = None
    _globals['_CONVERSIONSOURCESSERVICE'].methods_by_name['CreateConversionSource']._serialized_options = b'\xdaA\x18parent,conversion_source\x82\xd3\xe4\x93\x02J"5/conversions/v1/{parent=accounts/*}/conversionSources:\x11conversion_source'
    _globals['_CONVERSIONSOURCESSERVICE'].methods_by_name['UpdateConversionSource']._loaded_options = None
    _globals['_CONVERSIONSOURCESSERVICE'].methods_by_name['UpdateConversionSource']._serialized_options = b'\xdaA\x1dconversion_source,update_mask\x82\xd3\xe4\x93\x02\\2G/conversions/v1/{conversion_source.name=accounts/*/conversionSources/*}:\x11conversion_source'
    _globals['_CONVERSIONSOURCESSERVICE'].methods_by_name['DeleteConversionSource']._loaded_options = None
    _globals['_CONVERSIONSOURCESSERVICE'].methods_by_name['DeleteConversionSource']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027*5/conversions/v1/{name=accounts/*/conversionSources/*}'
    _globals['_CONVERSIONSOURCESSERVICE'].methods_by_name['UndeleteConversionSource']._loaded_options = None
    _globals['_CONVERSIONSOURCESSERVICE'].methods_by_name['UndeleteConversionSource']._serialized_options = b'\x82\xd3\xe4\x93\x02C">/conversions/v1/{name=accounts/*/conversionSources/*}:undelete:\x01*'
    _globals['_CONVERSIONSOURCESSERVICE'].methods_by_name['GetConversionSource']._loaded_options = None
    _globals['_CONVERSIONSOURCESSERVICE'].methods_by_name['GetConversionSource']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/conversions/v1/{name=accounts/*/conversionSources/*}'
    _globals['_CONVERSIONSOURCESSERVICE'].methods_by_name['ListConversionSources']._loaded_options = None
    _globals['_CONVERSIONSOURCESSERVICE'].methods_by_name['ListConversionSources']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/conversions/v1/{parent=accounts/*}/conversionSources'
    _globals['_CONVERSIONSOURCE']._serialized_start = 320
    _globals['_CONVERSIONSOURCE']._serialized_end = 1114
    _globals['_CONVERSIONSOURCE_STATE']._serialized_start = 803
    _globals['_CONVERSIONSOURCE_STATE']._serialized_end = 872
    _globals['_CONVERSIONSOURCE_CONTROLLER']._serialized_start = 874
    _globals['_CONVERSIONSOURCE_CONTROLLER']._serialized_end = 952
    _globals['_ATTRIBUTIONSETTINGS']._serialized_start = 1117
    _globals['_ATTRIBUTIONSETTINGS']._serialized_end = 1732
    _globals['_ATTRIBUTIONSETTINGS_CONVERSIONTYPE']._serialized_start = 1408
    _globals['_ATTRIBUTIONSETTINGS_CONVERSIONTYPE']._serialized_end = 1464
    _globals['_ATTRIBUTIONSETTINGS_ATTRIBUTIONMODEL']._serialized_start = 1467
    _globals['_ATTRIBUTIONSETTINGS_ATTRIBUTIONMODEL']._serialized_end = 1732
    _globals['_GOOGLEANALYTICSLINK']._serialized_start = 1735
    _globals['_GOOGLEANALYTICSLINK']._serialized_end = 1905
    _globals['_MERCHANTCENTERDESTINATION']._serialized_start = 1908
    _globals['_MERCHANTCENTERDESTINATION']._serialized_end = 2113
    _globals['_CREATECONVERSIONSOURCEREQUEST']._serialized_start = 2116
    _globals['_CREATECONVERSIONSOURCEREQUEST']._serialized_end = 2307
    _globals['_UPDATECONVERSIONSOURCEREQUEST']._serialized_start = 2310
    _globals['_UPDATECONVERSIONSOURCEREQUEST']._serialized_end = 2486
    _globals['_DELETECONVERSIONSOURCEREQUEST']._serialized_start = 2488
    _globals['_DELETECONVERSIONSOURCEREQUEST']._serialized_end = 2586
    _globals['_UNDELETECONVERSIONSOURCEREQUEST']._serialized_start = 2588
    _globals['_UNDELETECONVERSIONSOURCEREQUEST']._serialized_end = 2688
    _globals['_GETCONVERSIONSOURCEREQUEST']._serialized_start = 2690
    _globals['_GETCONVERSIONSOURCEREQUEST']._serialized_end = 2785
    _globals['_LISTCONVERSIONSOURCESREQUEST']._serialized_start = 2788
    _globals['_LISTCONVERSIONSOURCESREQUEST']._serialized_end = 2963
    _globals['_LISTCONVERSIONSOURCESRESPONSE']._serialized_start = 2966
    _globals['_LISTCONVERSIONSOURCESRESPONSE']._serialized_end = 3109
    _globals['_CONVERSIONSOURCESSERVICE']._serialized_start = 3112
    _globals['_CONVERSIONSOURCESSERVICE']._serialized_end = 4662