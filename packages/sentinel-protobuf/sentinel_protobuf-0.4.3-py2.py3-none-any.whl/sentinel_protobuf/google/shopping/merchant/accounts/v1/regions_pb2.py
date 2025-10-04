"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1/regions.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/shopping/merchant/accounts/v1/regions.proto\x12$google.shopping.merchant.accounts.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1egoogle/protobuf/wrappers.proto"K\n\x10GetRegionRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!merchantapi.googleapis.com/Region"\xac\x01\n\x13CreateRegionRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12\x16\n\tregion_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12A\n\x06region\x18\x03 \x01(\x0b2,.google.shopping.merchant.accounts.v1.RegionB\x03\xe0A\x02"\xa9\x01\n\x19BatchCreateRegionsRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12P\n\x08requests\x18\x02 \x03(\x0b29.google.shopping.merchant.accounts.v1.CreateRegionRequestB\x03\xe0A\x02"[\n\x1aBatchCreateRegionsResponse\x12=\n\x07regions\x18\x01 \x03(\x0b2,.google.shopping.merchant.accounts.v1.Region"\x8e\x01\n\x13UpdateRegionRequest\x12A\n\x06region\x18\x01 \x01(\x0b2,.google.shopping.merchant.accounts.v1.RegionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\xa9\x01\n\x19BatchUpdateRegionsRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12P\n\x08requests\x18\x02 \x03(\x0b29.google.shopping.merchant.accounts.v1.UpdateRegionRequestB\x03\xe0A\x02"[\n\x1aBatchUpdateRegionsResponse\x12=\n\x07regions\x18\x01 \x03(\x0b2,.google.shopping.merchant.accounts.v1.Region"N\n\x13DeleteRegionRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!merchantapi.googleapis.com/Region"\xa9\x01\n\x19BatchDeleteRegionsRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12P\n\x08requests\x18\x02 \x03(\x0b29.google.shopping.merchant.accounts.v1.DeleteRegionRequestB\x03\xe0A\x02"\x81\x01\n\x12ListRegionsRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"m\n\x13ListRegionsResponse\x12=\n\x07regions\x18\x01 \x03(\x0b2,.google.shopping.merchant.accounts.v1.Region\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xe5\x05\n\x06Region\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1e\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x01H\x00\x88\x01\x01\x12Z\n\x10postal_code_area\x18\x03 \x01(\x0b2;.google.shopping.merchant.accounts.v1.Region.PostalCodeAreaB\x03\xe0A\x01\x12W\n\x0egeotarget_area\x18\x04 \x01(\x0b2:.google.shopping.merchant.accounts.v1.Region.GeoTargetAreaB\x03\xe0A\x01\x12D\n\x1bregional_inventory_eligible\x18\x05 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x03\x12:\n\x11shipping_eligible\x18\x06 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x03\x1a\xcb\x01\n\x0ePostalCodeArea\x12\x18\n\x0bregion_code\x18\x01 \x01(\tB\x03\xe0A\x02\x12f\n\x0cpostal_codes\x18\x02 \x03(\x0b2K.google.shopping.merchant.accounts.v1.Region.PostalCodeArea.PostalCodeRangeB\x03\xe0A\x02\x1a7\n\x0fPostalCodeRange\x12\x12\n\x05begin\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x10\n\x03end\x18\x02 \x01(\tB\x03\xe0A\x01\x1a4\n\rGeoTargetArea\x12#\n\x16geotarget_criteria_ids\x18\x01 \x03(\x03B\x03\xe0A\x02:\\\xeaAY\n!merchantapi.googleapis.com/Region\x12#accounts/{account}/regions/{region}*\x07regions2\x06regionB\x0f\n\r_display_name2\xe8\x0c\n\x0eRegionsService\x12\xaa\x01\n\tGetRegion\x126.google.shopping.merchant.accounts.v1.GetRegionRequest\x1a,.google.shopping.merchant.accounts.v1.Region"7\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/accounts/v1/{name=accounts/*/regions/*}\x12\xcb\x01\n\x0cCreateRegion\x129.google.shopping.merchant.accounts.v1.CreateRegionRequest\x1a,.google.shopping.merchant.accounts.v1.Region"R\xdaA\x17parent,region,region_id\x82\xd3\xe4\x93\x022"(/accounts/v1/{parent=accounts/*}/regions:\x06region\x12\xd8\x01\n\x12BatchCreateRegions\x12?.google.shopping.merchant.accounts.v1.BatchCreateRegionsRequest\x1a@.google.shopping.merchant.accounts.v1.BatchCreateRegionsResponse"?\x82\xd3\xe4\x93\x029"4/accounts/v1/{parent=accounts/*}/regions:batchCreate:\x01*\x12\xcd\x01\n\x0cUpdateRegion\x129.google.shopping.merchant.accounts.v1.UpdateRegionRequest\x1a,.google.shopping.merchant.accounts.v1.Region"T\xdaA\x12region,update_mask\x82\xd3\xe4\x93\x0292//accounts/v1/{region.name=accounts/*/regions/*}:\x06region\x12\xd8\x01\n\x12BatchUpdateRegions\x12?.google.shopping.merchant.accounts.v1.BatchUpdateRegionsRequest\x1a@.google.shopping.merchant.accounts.v1.BatchUpdateRegionsResponse"?\x82\xd3\xe4\x93\x029"4/accounts/v1/{parent=accounts/*}/regions:batchUpdate:\x01*\x12\x9a\x01\n\x0cDeleteRegion\x129.google.shopping.merchant.accounts.v1.DeleteRegionRequest\x1a\x16.google.protobuf.Empty"7\xdaA\x04name\x82\xd3\xe4\x93\x02**(/accounts/v1/{name=accounts/*/regions/*}\x12\xae\x01\n\x12BatchDeleteRegions\x12?.google.shopping.merchant.accounts.v1.BatchDeleteRegionsRequest\x1a\x16.google.protobuf.Empty"?\x82\xd3\xe4\x93\x029"4/accounts/v1/{parent=accounts/*}/regions:batchDelete:\x01*\x12\xbd\x01\n\x0bListRegions\x128.google.shopping.merchant.accounts.v1.ListRegionsRequest\x1a9.google.shopping.merchant.accounts.v1.ListRegionsResponse"9\xdaA\x06parent\x82\xd3\xe4\x93\x02*\x12(/accounts/v1/{parent=accounts/*}/regions\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xff\x01\n(com.google.shopping.merchant.accounts.v1B\x0cRegionsProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1.regions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.shopping.merchant.accounts.v1B\x0cRegionsProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1'
    _globals['_GETREGIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETREGIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!merchantapi.googleapis.com/Region'
    _globals['_CREATEREGIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEREGIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_CREATEREGIONREQUEST'].fields_by_name['region_id']._loaded_options = None
    _globals['_CREATEREGIONREQUEST'].fields_by_name['region_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEREGIONREQUEST'].fields_by_name['region']._loaded_options = None
    _globals['_CREATEREGIONREQUEST'].fields_by_name['region']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHCREATEREGIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHCREATEREGIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_BATCHCREATEREGIONSREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHCREATEREGIONSREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEREGIONREQUEST'].fields_by_name['region']._loaded_options = None
    _globals['_UPDATEREGIONREQUEST'].fields_by_name['region']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEREGIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEREGIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHUPDATEREGIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHUPDATEREGIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_BATCHUPDATEREGIONSREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHUPDATEREGIONSREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEREGIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEREGIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!merchantapi.googleapis.com/Region'
    _globals['_BATCHDELETEREGIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHDELETEREGIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_BATCHDELETEREGIONSREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHDELETEREGIONSREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_LISTREGIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTREGIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_LISTREGIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTREGIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTREGIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTREGIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_REGION_POSTALCODEAREA_POSTALCODERANGE'].fields_by_name['begin']._loaded_options = None
    _globals['_REGION_POSTALCODEAREA_POSTALCODERANGE'].fields_by_name['begin']._serialized_options = b'\xe0A\x02'
    _globals['_REGION_POSTALCODEAREA_POSTALCODERANGE'].fields_by_name['end']._loaded_options = None
    _globals['_REGION_POSTALCODEAREA_POSTALCODERANGE'].fields_by_name['end']._serialized_options = b'\xe0A\x01'
    _globals['_REGION_POSTALCODEAREA'].fields_by_name['region_code']._loaded_options = None
    _globals['_REGION_POSTALCODEAREA'].fields_by_name['region_code']._serialized_options = b'\xe0A\x02'
    _globals['_REGION_POSTALCODEAREA'].fields_by_name['postal_codes']._loaded_options = None
    _globals['_REGION_POSTALCODEAREA'].fields_by_name['postal_codes']._serialized_options = b'\xe0A\x02'
    _globals['_REGION_GEOTARGETAREA'].fields_by_name['geotarget_criteria_ids']._loaded_options = None
    _globals['_REGION_GEOTARGETAREA'].fields_by_name['geotarget_criteria_ids']._serialized_options = b'\xe0A\x02'
    _globals['_REGION'].fields_by_name['name']._loaded_options = None
    _globals['_REGION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_REGION'].fields_by_name['display_name']._loaded_options = None
    _globals['_REGION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_REGION'].fields_by_name['postal_code_area']._loaded_options = None
    _globals['_REGION'].fields_by_name['postal_code_area']._serialized_options = b'\xe0A\x01'
    _globals['_REGION'].fields_by_name['geotarget_area']._loaded_options = None
    _globals['_REGION'].fields_by_name['geotarget_area']._serialized_options = b'\xe0A\x01'
    _globals['_REGION'].fields_by_name['regional_inventory_eligible']._loaded_options = None
    _globals['_REGION'].fields_by_name['regional_inventory_eligible']._serialized_options = b'\xe0A\x03'
    _globals['_REGION'].fields_by_name['shipping_eligible']._loaded_options = None
    _globals['_REGION'].fields_by_name['shipping_eligible']._serialized_options = b'\xe0A\x03'
    _globals['_REGION']._loaded_options = None
    _globals['_REGION']._serialized_options = b'\xeaAY\n!merchantapi.googleapis.com/Region\x12#accounts/{account}/regions/{region}*\x07regions2\x06region'
    _globals['_REGIONSSERVICE']._loaded_options = None
    _globals['_REGIONSSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_REGIONSSERVICE'].methods_by_name['GetRegion']._loaded_options = None
    _globals['_REGIONSSERVICE'].methods_by_name['GetRegion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/accounts/v1/{name=accounts/*/regions/*}'
    _globals['_REGIONSSERVICE'].methods_by_name['CreateRegion']._loaded_options = None
    _globals['_REGIONSSERVICE'].methods_by_name['CreateRegion']._serialized_options = b'\xdaA\x17parent,region,region_id\x82\xd3\xe4\x93\x022"(/accounts/v1/{parent=accounts/*}/regions:\x06region'
    _globals['_REGIONSSERVICE'].methods_by_name['BatchCreateRegions']._loaded_options = None
    _globals['_REGIONSSERVICE'].methods_by_name['BatchCreateRegions']._serialized_options = b'\x82\xd3\xe4\x93\x029"4/accounts/v1/{parent=accounts/*}/regions:batchCreate:\x01*'
    _globals['_REGIONSSERVICE'].methods_by_name['UpdateRegion']._loaded_options = None
    _globals['_REGIONSSERVICE'].methods_by_name['UpdateRegion']._serialized_options = b'\xdaA\x12region,update_mask\x82\xd3\xe4\x93\x0292//accounts/v1/{region.name=accounts/*/regions/*}:\x06region'
    _globals['_REGIONSSERVICE'].methods_by_name['BatchUpdateRegions']._loaded_options = None
    _globals['_REGIONSSERVICE'].methods_by_name['BatchUpdateRegions']._serialized_options = b'\x82\xd3\xe4\x93\x029"4/accounts/v1/{parent=accounts/*}/regions:batchUpdate:\x01*'
    _globals['_REGIONSSERVICE'].methods_by_name['DeleteRegion']._loaded_options = None
    _globals['_REGIONSSERVICE'].methods_by_name['DeleteRegion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02**(/accounts/v1/{name=accounts/*/regions/*}'
    _globals['_REGIONSSERVICE'].methods_by_name['BatchDeleteRegions']._loaded_options = None
    _globals['_REGIONSSERVICE'].methods_by_name['BatchDeleteRegions']._serialized_options = b'\x82\xd3\xe4\x93\x029"4/accounts/v1/{parent=accounts/*}/regions:batchDelete:\x01*'
    _globals['_REGIONSSERVICE'].methods_by_name['ListRegions']._loaded_options = None
    _globals['_REGIONSSERVICE'].methods_by_name['ListRegions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02*\x12(/accounts/v1/{parent=accounts/*}/regions'
    _globals['_GETREGIONREQUEST']._serialized_start = 302
    _globals['_GETREGIONREQUEST']._serialized_end = 377
    _globals['_CREATEREGIONREQUEST']._serialized_start = 380
    _globals['_CREATEREGIONREQUEST']._serialized_end = 552
    _globals['_BATCHCREATEREGIONSREQUEST']._serialized_start = 555
    _globals['_BATCHCREATEREGIONSREQUEST']._serialized_end = 724
    _globals['_BATCHCREATEREGIONSRESPONSE']._serialized_start = 726
    _globals['_BATCHCREATEREGIONSRESPONSE']._serialized_end = 817
    _globals['_UPDATEREGIONREQUEST']._serialized_start = 820
    _globals['_UPDATEREGIONREQUEST']._serialized_end = 962
    _globals['_BATCHUPDATEREGIONSREQUEST']._serialized_start = 965
    _globals['_BATCHUPDATEREGIONSREQUEST']._serialized_end = 1134
    _globals['_BATCHUPDATEREGIONSRESPONSE']._serialized_start = 1136
    _globals['_BATCHUPDATEREGIONSRESPONSE']._serialized_end = 1227
    _globals['_DELETEREGIONREQUEST']._serialized_start = 1229
    _globals['_DELETEREGIONREQUEST']._serialized_end = 1307
    _globals['_BATCHDELETEREGIONSREQUEST']._serialized_start = 1310
    _globals['_BATCHDELETEREGIONSREQUEST']._serialized_end = 1479
    _globals['_LISTREGIONSREQUEST']._serialized_start = 1482
    _globals['_LISTREGIONSREQUEST']._serialized_end = 1611
    _globals['_LISTREGIONSRESPONSE']._serialized_start = 1613
    _globals['_LISTREGIONSRESPONSE']._serialized_end = 1722
    _globals['_REGION']._serialized_start = 1725
    _globals['_REGION']._serialized_end = 2466
    _globals['_REGION_POSTALCODEAREA']._serialized_start = 2098
    _globals['_REGION_POSTALCODEAREA']._serialized_end = 2301
    _globals['_REGION_POSTALCODEAREA_POSTALCODERANGE']._serialized_start = 2246
    _globals['_REGION_POSTALCODEAREA_POSTALCODERANGE']._serialized_end = 2301
    _globals['_REGION_GEOTARGETAREA']._serialized_start = 2303
    _globals['_REGION_GEOTARGETAREA']._serialized_end = 2355
    _globals['_REGIONSSERVICE']._serialized_start = 2469
    _globals['_REGIONSSERVICE']._serialized_end = 4109