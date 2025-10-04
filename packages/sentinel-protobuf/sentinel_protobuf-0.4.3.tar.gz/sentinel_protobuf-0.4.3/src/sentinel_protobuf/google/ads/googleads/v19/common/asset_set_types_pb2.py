"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/common/asset_set_types.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import chain_relationship_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_chain__relationship__type__pb2
from ......google.ads.googleads.v19.enums import location_ownership_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_location__ownership__type__pb2
from ......google.ads.googleads.v19.enums import location_string_filter_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_location__string__filter__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/ads/googleads/v19/common/asset_set_types.proto\x12\x1fgoogle.ads.googleads.v19.common\x1a<google/ads/googleads/v19/enums/chain_relationship_type.proto\x1a<google/ads/googleads/v19/enums/location_ownership_type.proto\x1a@google/ads/googleads/v19/enums/location_string_filter_type.proto\x1a\x1fgoogle/api/field_behavior.proto"\x8f\x03\n\x0bLocationSet\x12x\n\x17location_ownership_type\x18\x03 \x01(\x0e2O.google.ads.googleads.v19.enums.LocationOwnershipTypeEnum.LocationOwnershipTypeB\x06\xe0A\x02\xe0A\x05\x12d\n\x1dbusiness_profile_location_set\x18\x01 \x01(\x0b2;.google.ads.googleads.v19.common.BusinessProfileLocationSetH\x00\x12G\n\x12chain_location_set\x18\x02 \x01(\x0b2).google.ads.googleads.v19.common.ChainSetH\x00\x12M\n\x11maps_location_set\x18\x05 \x01(\x0b20.google.ads.googleads.v19.common.MapsLocationSetH\x00B\x08\n\x06source"\xd8\x01\n\x1aBusinessProfileLocationSet\x12(\n\x18http_authorization_token\x18\x01 \x01(\tB\x06\xe0A\x05\xe0A\x02\x12\x1d\n\remail_address\x18\x02 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12\x1c\n\x14business_name_filter\x18\x03 \x01(\t\x12\x15\n\rlabel_filters\x18\x04 \x03(\t\x12\x1a\n\x12listing_id_filters\x18\x05 \x03(\x03\x12 \n\x13business_account_id\x18\x06 \x01(\tB\x03\xe0A\x05"\xc1\x01\n\x08ChainSet\x12r\n\x11relationship_type\x18\x01 \x01(\x0e2O.google.ads.googleads.v19.enums.ChainRelationshipTypeEnum.ChainRelationshipTypeB\x06\xe0A\x02\xe0A\x05\x12A\n\x06chains\x18\x02 \x03(\x0b2,.google.ads.googleads.v19.common.ChainFilterB\x03\xe0A\x02"A\n\x0bChainFilter\x12\x15\n\x08chain_id\x18\x01 \x01(\x03B\x03\xe0A\x02\x12\x1b\n\x13location_attributes\x18\x02 \x03(\t"a\n\x0fMapsLocationSet\x12N\n\x0emaps_locations\x18\x01 \x03(\x0b21.google.ads.googleads.v19.common.MapsLocationInfoB\x03\xe0A\x02"$\n\x10MapsLocationInfo\x12\x10\n\x08place_id\x18\x01 \x01(\t"\xa3\x01\n\x1cBusinessProfileLocationGroup\x12\x82\x01\n.dynamic_business_profile_location_group_filter\x18\x01 \x01(\x0b2J.google.ads.googleads.v19.common.DynamicBusinessProfileLocationGroupFilter"\xde\x01\n)DynamicBusinessProfileLocationGroupFilter\x12\x15\n\rlabel_filters\x18\x01 \x03(\t\x12e\n\x14business_name_filter\x18\x02 \x01(\x0b2B.google.ads.googleads.v19.common.BusinessProfileBusinessNameFilterH\x00\x88\x01\x01\x12\x1a\n\x12listing_id_filters\x18\x03 \x03(\x03B\x17\n\x15_business_name_filter"\xa6\x01\n!BusinessProfileBusinessNameFilter\x12\x15\n\rbusiness_name\x18\x01 \x01(\t\x12j\n\x0bfilter_type\x18\x02 \x01(\x0e2U.google.ads.googleads.v19.enums.LocationStringFilterTypeEnum.LocationStringFilterType"p\n\x12ChainLocationGroup\x12Z\n$dynamic_chain_location_group_filters\x18\x01 \x03(\x0b2,.google.ads.googleads.v19.common.ChainFilterB\xf2\x01\n#com.google.ads.googleads.v19.commonB\x12AssetSetTypesProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v19/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V19.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V19\\Common\xea\x02#Google::Ads::GoogleAds::V19::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.common.asset_set_types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v19.commonB\x12AssetSetTypesProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v19/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V19.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V19\\Common\xea\x02#Google::Ads::GoogleAds::V19::Common'
    _globals['_LOCATIONSET'].fields_by_name['location_ownership_type']._loaded_options = None
    _globals['_LOCATIONSET'].fields_by_name['location_ownership_type']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_BUSINESSPROFILELOCATIONSET'].fields_by_name['http_authorization_token']._loaded_options = None
    _globals['_BUSINESSPROFILELOCATIONSET'].fields_by_name['http_authorization_token']._serialized_options = b'\xe0A\x05\xe0A\x02'
    _globals['_BUSINESSPROFILELOCATIONSET'].fields_by_name['email_address']._loaded_options = None
    _globals['_BUSINESSPROFILELOCATIONSET'].fields_by_name['email_address']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_BUSINESSPROFILELOCATIONSET'].fields_by_name['business_account_id']._loaded_options = None
    _globals['_BUSINESSPROFILELOCATIONSET'].fields_by_name['business_account_id']._serialized_options = b'\xe0A\x05'
    _globals['_CHAINSET'].fields_by_name['relationship_type']._loaded_options = None
    _globals['_CHAINSET'].fields_by_name['relationship_type']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_CHAINSET'].fields_by_name['chains']._loaded_options = None
    _globals['_CHAINSET'].fields_by_name['chains']._serialized_options = b'\xe0A\x02'
    _globals['_CHAINFILTER'].fields_by_name['chain_id']._loaded_options = None
    _globals['_CHAINFILTER'].fields_by_name['chain_id']._serialized_options = b'\xe0A\x02'
    _globals['_MAPSLOCATIONSET'].fields_by_name['maps_locations']._loaded_options = None
    _globals['_MAPSLOCATIONSET'].fields_by_name['maps_locations']._serialized_options = b'\xe0A\x02'
    _globals['_LOCATIONSET']._serialized_start = 314
    _globals['_LOCATIONSET']._serialized_end = 713
    _globals['_BUSINESSPROFILELOCATIONSET']._serialized_start = 716
    _globals['_BUSINESSPROFILELOCATIONSET']._serialized_end = 932
    _globals['_CHAINSET']._serialized_start = 935
    _globals['_CHAINSET']._serialized_end = 1128
    _globals['_CHAINFILTER']._serialized_start = 1130
    _globals['_CHAINFILTER']._serialized_end = 1195
    _globals['_MAPSLOCATIONSET']._serialized_start = 1197
    _globals['_MAPSLOCATIONSET']._serialized_end = 1294
    _globals['_MAPSLOCATIONINFO']._serialized_start = 1296
    _globals['_MAPSLOCATIONINFO']._serialized_end = 1332
    _globals['_BUSINESSPROFILELOCATIONGROUP']._serialized_start = 1335
    _globals['_BUSINESSPROFILELOCATIONGROUP']._serialized_end = 1498
    _globals['_DYNAMICBUSINESSPROFILELOCATIONGROUPFILTER']._serialized_start = 1501
    _globals['_DYNAMICBUSINESSPROFILELOCATIONGROUPFILTER']._serialized_end = 1723
    _globals['_BUSINESSPROFILEBUSINESSNAMEFILTER']._serialized_start = 1726
    _globals['_BUSINESSPROFILEBUSINESSNAMEFILTER']._serialized_end = 1892
    _globals['_CHAINLOCATIONGROUP']._serialized_start = 1894
    _globals['_CHAINLOCATIONGROUP']._serialized_end = 2006