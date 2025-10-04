"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1beta/regions.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/shopping/merchant/accounts/v1beta/regions.proto\x12(google.shopping.merchant.accounts.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1egoogle/protobuf/wrappers.proto"K\n\x10GetRegionRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!merchantapi.googleapis.com/Region"\xb0\x01\n\x13CreateRegionRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12\x16\n\tregion_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12E\n\x06region\x18\x03 \x01(\x0b20.google.shopping.merchant.accounts.v1beta.RegionB\x03\xe0A\x02"\x92\x01\n\x13UpdateRegionRequest\x12E\n\x06region\x18\x01 \x01(\x0b20.google.shopping.merchant.accounts.v1beta.RegionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"N\n\x13DeleteRegionRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!merchantapi.googleapis.com/Region"\x81\x01\n\x12ListRegionsRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"q\n\x13ListRegionsResponse\x12A\n\x07regions\x18\x01 \x03(\x0b20.google.shopping.merchant.accounts.v1beta.Region\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xf1\x05\n\x06Region\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1e\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x01H\x00\x88\x01\x01\x12^\n\x10postal_code_area\x18\x03 \x01(\x0b2?.google.shopping.merchant.accounts.v1beta.Region.PostalCodeAreaB\x03\xe0A\x01\x12[\n\x0egeotarget_area\x18\x04 \x01(\x0b2>.google.shopping.merchant.accounts.v1beta.Region.GeoTargetAreaB\x03\xe0A\x01\x12D\n\x1bregional_inventory_eligible\x18\x05 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x03\x12:\n\x11shipping_eligible\x18\x06 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x03\x1a\xcf\x01\n\x0ePostalCodeArea\x12\x18\n\x0bregion_code\x18\x01 \x01(\tB\x03\xe0A\x02\x12j\n\x0cpostal_codes\x18\x02 \x03(\x0b2O.google.shopping.merchant.accounts.v1beta.Region.PostalCodeArea.PostalCodeRangeB\x03\xe0A\x02\x1a7\n\x0fPostalCodeRange\x12\x12\n\x05begin\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x10\n\x03end\x18\x02 \x01(\tB\x03\xe0A\x01\x1a4\n\rGeoTargetArea\x12#\n\x16geotarget_criteria_ids\x18\x01 \x03(\x03B\x03\xe0A\x02:\\\xeaAY\n!merchantapi.googleapis.com/Region\x12#accounts/{account}/regions/{region}*\x07regions2\x06regionB\x0f\n\r_display_name2\xb9\x08\n\x0eRegionsService\x12\xb6\x01\n\tGetRegion\x12:.google.shopping.merchant.accounts.v1beta.GetRegionRequest\x1a0.google.shopping.merchant.accounts.v1beta.Region";\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/accounts/v1beta/{name=accounts/*/regions/*}\x12\xd7\x01\n\x0cCreateRegion\x12=.google.shopping.merchant.accounts.v1beta.CreateRegionRequest\x1a0.google.shopping.merchant.accounts.v1beta.Region"V\xdaA\x17parent,region,region_id\x82\xd3\xe4\x93\x026",/accounts/v1beta/{parent=accounts/*}/regions:\x06region\x12\xd9\x01\n\x0cUpdateRegion\x12=.google.shopping.merchant.accounts.v1beta.UpdateRegionRequest\x1a0.google.shopping.merchant.accounts.v1beta.Region"X\xdaA\x12region,update_mask\x82\xd3\xe4\x93\x02=23/accounts/v1beta/{region.name=accounts/*/regions/*}:\x06region\x12\xa2\x01\n\x0cDeleteRegion\x12=.google.shopping.merchant.accounts.v1beta.DeleteRegionRequest\x1a\x16.google.protobuf.Empty";\xdaA\x04name\x82\xd3\xe4\x93\x02.*,/accounts/v1beta/{name=accounts/*/regions/*}\x12\xc9\x01\n\x0bListRegions\x12<.google.shopping.merchant.accounts.v1beta.ListRegionsRequest\x1a=.google.shopping.merchant.accounts.v1beta.ListRegionsResponse"=\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/accounts/v1beta/{parent=accounts/*}/regions\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x8e\x01\n,com.google.shopping.merchant.accounts.v1betaB\x0cRegionsProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1beta.regions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.shopping.merchant.accounts.v1betaB\x0cRegionsProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspb'
    _globals['_GETREGIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETREGIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!merchantapi.googleapis.com/Region'
    _globals['_CREATEREGIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEREGIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_CREATEREGIONREQUEST'].fields_by_name['region_id']._loaded_options = None
    _globals['_CREATEREGIONREQUEST'].fields_by_name['region_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEREGIONREQUEST'].fields_by_name['region']._loaded_options = None
    _globals['_CREATEREGIONREQUEST'].fields_by_name['region']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEREGIONREQUEST'].fields_by_name['region']._loaded_options = None
    _globals['_UPDATEREGIONREQUEST'].fields_by_name['region']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEREGIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEREGIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEREGIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEREGIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!merchantapi.googleapis.com/Region'
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
    _globals['_REGIONSSERVICE'].methods_by_name['GetRegion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/accounts/v1beta/{name=accounts/*/regions/*}'
    _globals['_REGIONSSERVICE'].methods_by_name['CreateRegion']._loaded_options = None
    _globals['_REGIONSSERVICE'].methods_by_name['CreateRegion']._serialized_options = b'\xdaA\x17parent,region,region_id\x82\xd3\xe4\x93\x026",/accounts/v1beta/{parent=accounts/*}/regions:\x06region'
    _globals['_REGIONSSERVICE'].methods_by_name['UpdateRegion']._loaded_options = None
    _globals['_REGIONSSERVICE'].methods_by_name['UpdateRegion']._serialized_options = b'\xdaA\x12region,update_mask\x82\xd3\xe4\x93\x02=23/accounts/v1beta/{region.name=accounts/*/regions/*}:\x06region'
    _globals['_REGIONSSERVICE'].methods_by_name['DeleteRegion']._loaded_options = None
    _globals['_REGIONSSERVICE'].methods_by_name['DeleteRegion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02.*,/accounts/v1beta/{name=accounts/*/regions/*}'
    _globals['_REGIONSSERVICE'].methods_by_name['ListRegions']._loaded_options = None
    _globals['_REGIONSSERVICE'].methods_by_name['ListRegions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/accounts/v1beta/{parent=accounts/*}/regions'
    _globals['_GETREGIONREQUEST']._serialized_start = 310
    _globals['_GETREGIONREQUEST']._serialized_end = 385
    _globals['_CREATEREGIONREQUEST']._serialized_start = 388
    _globals['_CREATEREGIONREQUEST']._serialized_end = 564
    _globals['_UPDATEREGIONREQUEST']._serialized_start = 567
    _globals['_UPDATEREGIONREQUEST']._serialized_end = 713
    _globals['_DELETEREGIONREQUEST']._serialized_start = 715
    _globals['_DELETEREGIONREQUEST']._serialized_end = 793
    _globals['_LISTREGIONSREQUEST']._serialized_start = 796
    _globals['_LISTREGIONSREQUEST']._serialized_end = 925
    _globals['_LISTREGIONSRESPONSE']._serialized_start = 927
    _globals['_LISTREGIONSRESPONSE']._serialized_end = 1040
    _globals['_REGION']._serialized_start = 1043
    _globals['_REGION']._serialized_end = 1796
    _globals['_REGION_POSTALCODEAREA']._serialized_start = 1424
    _globals['_REGION_POSTALCODEAREA']._serialized_end = 1631
    _globals['_REGION_POSTALCODEAREA_POSTALCODERANGE']._serialized_start = 1576
    _globals['_REGION_POSTALCODEAREA_POSTALCODERANGE']._serialized_end = 1631
    _globals['_REGION_GEOTARGETAREA']._serialized_start = 1633
    _globals['_REGION_GEOTARGETAREA']._serialized_end = 1685
    _globals['_REGIONSSERVICE']._serialized_start = 1799
    _globals['_REGIONSSERVICE']._serialized_end = 2880