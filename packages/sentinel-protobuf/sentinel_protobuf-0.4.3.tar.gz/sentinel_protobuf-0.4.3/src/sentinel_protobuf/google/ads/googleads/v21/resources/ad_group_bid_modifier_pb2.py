"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/ad_group_bid_modifier.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.common import criteria_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_criteria__pb2
from ......google.ads.googleads.v21.enums import bid_modifier_source_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_bid__modifier__source__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/ads/googleads/v21/resources/ad_group_bid_modifier.proto\x12"google.ads.googleads.v21.resources\x1a.google/ads/googleads/v21/common/criteria.proto\x1a8google/ads/googleads/v21/enums/bid_modifier_source.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x8b\t\n\x12AdGroupBidModifier\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0A\x05\xfaA-\n+googleads.googleapis.com/AdGroupBidModifier\x12?\n\x08ad_group\x18\r \x01(\tB(\xe0A\x05\xfaA"\n googleads.googleapis.com/AdGroupH\x01\x88\x01\x01\x12\x1e\n\x0ccriterion_id\x18\x0e \x01(\x03B\x03\xe0A\x03H\x02\x88\x01\x01\x12\x19\n\x0cbid_modifier\x18\x0f \x01(\x01H\x03\x88\x01\x01\x12D\n\rbase_ad_group\x18\x10 \x01(\tB(\xe0A\x03\xfaA"\n googleads.googleapis.com/AdGroupH\x04\x88\x01\x01\x12i\n\x13bid_modifier_source\x18\n \x01(\x0e2G.google.ads.googleads.v21.enums.BidModifierSourceEnum.BidModifierSourceB\x03\xe0A\x03\x12e\n\x19hotel_date_selection_type\x18\x05 \x01(\x0b2;.google.ads.googleads.v21.common.HotelDateSelectionTypeInfoB\x03\xe0A\x05H\x00\x12k\n\x1chotel_advance_booking_window\x18\x06 \x01(\x0b2>.google.ads.googleads.v21.common.HotelAdvanceBookingWindowInfoB\x03\xe0A\x05H\x00\x12[\n\x14hotel_length_of_stay\x18\x07 \x01(\x0b26.google.ads.googleads.v21.common.HotelLengthOfStayInfoB\x03\xe0A\x05H\x00\x12W\n\x12hotel_check_in_day\x18\x08 \x01(\x0b24.google.ads.googleads.v21.common.HotelCheckInDayInfoB\x03\xe0A\x05H\x00\x12B\n\x06device\x18\x0b \x01(\x0b2+.google.ads.googleads.v21.common.DeviceInfoB\x03\xe0A\x05H\x00\x12d\n\x19hotel_check_in_date_range\x18\x11 \x01(\x0b2:.google.ads.googleads.v21.common.HotelCheckInDateRangeInfoB\x03\xe0A\x05H\x00:z\xeaAw\n+googleads.googleapis.com/AdGroupBidModifier\x12Hcustomers/{customer_id}/adGroupBidModifiers/{ad_group_id}~{criterion_id}B\x0b\n\tcriterionB\x0b\n\t_ad_groupB\x0f\n\r_criterion_idB\x0f\n\r_bid_modifierB\x10\n\x0e_base_ad_groupB\x89\x02\n&com.google.ads.googleads.v21.resourcesB\x17AdGroupBidModifierProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.ad_group_bid_modifier_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\x17AdGroupBidModifierProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA-\n+googleads.googleapis.com/AdGroupBidModifier'
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['ad_group']._loaded_options = None
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['ad_group']._serialized_options = b'\xe0A\x05\xfaA"\n googleads.googleapis.com/AdGroup'
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['criterion_id']._loaded_options = None
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['criterion_id']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['base_ad_group']._loaded_options = None
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['base_ad_group']._serialized_options = b'\xe0A\x03\xfaA"\n googleads.googleapis.com/AdGroup'
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['bid_modifier_source']._loaded_options = None
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['bid_modifier_source']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['hotel_date_selection_type']._loaded_options = None
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['hotel_date_selection_type']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['hotel_advance_booking_window']._loaded_options = None
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['hotel_advance_booking_window']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['hotel_length_of_stay']._loaded_options = None
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['hotel_length_of_stay']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['hotel_check_in_day']._loaded_options = None
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['hotel_check_in_day']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['device']._loaded_options = None
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['device']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['hotel_check_in_date_range']._loaded_options = None
    _globals['_ADGROUPBIDMODIFIER'].fields_by_name['hotel_check_in_date_range']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPBIDMODIFIER']._loaded_options = None
    _globals['_ADGROUPBIDMODIFIER']._serialized_options = b'\xeaAw\n+googleads.googleapis.com/AdGroupBidModifier\x12Hcustomers/{customer_id}/adGroupBidModifiers/{ad_group_id}~{criterion_id}'
    _globals['_ADGROUPBIDMODIFIER']._serialized_start = 269
    _globals['_ADGROUPBIDMODIFIER']._serialized_end = 1432