"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/maps/solar/v1/solar_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2
from .....google.type import date_pb2 as google_dot_type_dot_date__pb2
from .....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
from .....google.type import money_pb2 as google_dot_type_dot_money__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/maps/solar/v1/solar_service.proto\x12\x14google.maps.solar.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/httpbody.proto\x1a\x16google/type/date.proto\x1a\x18google/type/latlng.proto\x1a\x17google/type/money.proto"\xf6\x01\n"FindClosestBuildingInsightsRequest\x12*\n\x08location\x18\x01 \x01(\x0b2\x13.google.type.LatLngB\x03\xe0A\x02\x12C\n\x10required_quality\x18\x03 \x01(\x0e2$.google.maps.solar.v1.ImageryQualityB\x03\xe0A\x01\x12#\n\x16exact_quality_required\x18\x04 \x01(\x08B\x03\xe0A\x01\x12:\n\x0bexperiments\x18\x05 \x03(\x0e2 .google.maps.solar.v1.ExperimentB\x03\xe0A\x01"M\n\tLatLngBox\x12\x1f\n\x02sw\x18\x01 \x01(\x0b2\x13.google.type.LatLng\x12\x1f\n\x02ne\x18\x02 \x01(\x0b2\x13.google.type.LatLng"\xb7\x03\n\x10BuildingInsights\x12\x0c\n\x04name\x18\x01 \x01(\t\x12#\n\x06center\x18\x02 \x01(\x0b2\x13.google.type.LatLng\x125\n\x0cbounding_box\x18\t \x01(\x0b2\x1f.google.maps.solar.v1.LatLngBox\x12\'\n\x0cimagery_date\x18\x03 \x01(\x0b2\x11.google.type.Date\x121\n\x16imagery_processed_date\x18\x0b \x01(\x0b2\x11.google.type.Date\x12\x13\n\x0bpostal_code\x18\x04 \x01(\t\x12\x1b\n\x13administrative_area\x18\x05 \x01(\t\x12\x18\n\x10statistical_area\x18\x06 \x01(\t\x12\x13\n\x0bregion_code\x18\x07 \x01(\t\x12=\n\x0fsolar_potential\x18\x08 \x01(\x0b2$.google.maps.solar.v1.SolarPotential\x12=\n\x0fimagery_quality\x18\n \x01(\x0e2$.google.maps.solar.v1.ImageryQuality"\xb2\x05\n\x0eSolarPotential\x12\x1e\n\x16max_array_panels_count\x18\x01 \x01(\x05\x12\x1c\n\x14panel_capacity_watts\x18\t \x01(\x02\x12\x1b\n\x13panel_height_meters\x18\n \x01(\x02\x12\x1a\n\x12panel_width_meters\x18\x0b \x01(\x02\x12\x1c\n\x14panel_lifetime_years\x18\x0c \x01(\x05\x12\x1e\n\x16max_array_area_meters2\x18\x02 \x01(\x02\x12#\n\x1bmax_sunshine_hours_per_year\x18\x03 \x01(\x02\x12\'\n\x1fcarbon_offset_factor_kg_per_mwh\x18\x04 \x01(\x02\x12D\n\x10whole_roof_stats\x18\x05 \x01(\x0b2*.google.maps.solar.v1.SizeAndSunshineStats\x12B\n\x0ebuilding_stats\x18\r \x01(\x0b2*.google.maps.solar.v1.SizeAndSunshineStats\x12Q\n\x12roof_segment_stats\x18\x06 \x03(\x0b25.google.maps.solar.v1.RoofSegmentSizeAndSunshineStats\x126\n\x0csolar_panels\x18\x0e \x03(\x0b2 .google.maps.solar.v1.SolarPanel\x12C\n\x13solar_panel_configs\x18\x07 \x03(\x0b2&.google.maps.solar.v1.SolarPanelConfig\x12C\n\x12financial_analyses\x18\x08 \x03(\x0b2\'.google.maps.solar.v1.FinancialAnalysis"\xe6\x02\n\x1fRoofSegmentSizeAndSunshineStats\x12\x1a\n\rpitch_degrees\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x1c\n\x0fazimuth_degrees\x18\x02 \x01(\x02H\x01\x88\x01\x01\x129\n\x05stats\x18\x03 \x01(\x0b2*.google.maps.solar.v1.SizeAndSunshineStats\x12#\n\x06center\x18\x04 \x01(\x0b2\x13.google.type.LatLng\x125\n\x0cbounding_box\x18\x05 \x01(\x0b2\x1f.google.maps.solar.v1.LatLngBox\x12*\n\x1dplane_height_at_center_meters\x18\x06 \x01(\x02H\x02\x88\x01\x01B\x10\n\x0e_pitch_degreesB\x12\n\x10_azimuth_degreesB \n\x1e_plane_height_at_center_meters"e\n\x14SizeAndSunshineStats\x12\x14\n\x0carea_meters2\x18\x01 \x01(\x02\x12\x1a\n\x12sunshine_quantiles\x18\x02 \x03(\x02\x12\x1b\n\x13ground_area_meters2\x18\x03 \x01(\x02"\xbf\x01\n\nSolarPanel\x12#\n\x06center\x18\x01 \x01(\x0b2\x13.google.type.LatLng\x12@\n\x0borientation\x18\x02 \x01(\x0e2+.google.maps.solar.v1.SolarPanelOrientation\x12\x1c\n\x14yearly_energy_dc_kwh\x18\x03 \x01(\x02\x12\x1a\n\rsegment_index\x18\x04 \x01(\x05H\x00\x88\x01\x01B\x10\n\x0e_segment_index"\x90\x01\n\x10SolarPanelConfig\x12\x14\n\x0cpanels_count\x18\x01 \x01(\x05\x12\x1c\n\x14yearly_energy_dc_kwh\x18\x02 \x01(\x02\x12H\n\x16roof_segment_summaries\x18\x04 \x03(\x0b2(.google.maps.solar.v1.RoofSegmentSummary"\xd6\x01\n\x12RoofSegmentSummary\x12\x1a\n\rpitch_degrees\x18\x02 \x01(\x02H\x00\x88\x01\x01\x12\x1c\n\x0fazimuth_degrees\x18\x03 \x01(\x02H\x01\x88\x01\x01\x12\x14\n\x0cpanels_count\x18\x07 \x01(\x05\x12\x1c\n\x14yearly_energy_dc_kwh\x18\x08 \x01(\x02\x12\x1a\n\rsegment_index\x18\t \x01(\x05H\x02\x88\x01\x01B\x10\n\x0e_pitch_degreesB\x12\n\x10_azimuth_degreesB\x10\n\x0e_segment_index"\xc8\x03\n\x11FinancialAnalysis\x12(\n\x0cmonthly_bill\x18\x03 \x01(\x0b2\x12.google.type.Money\x12\x14\n\x0cdefault_bill\x18\x04 \x01(\x08\x12\x1d\n\x15average_kwh_per_month\x18\x05 \x01(\x02\x12\x1f\n\x12panel_config_index\x18\x06 \x01(\x05H\x00\x88\x01\x01\x12A\n\x11financial_details\x18\x07 \x01(\x0b2&.google.maps.solar.v1.FinancialDetails\x12=\n\x0fleasing_savings\x18\x08 \x01(\x0b2$.google.maps.solar.v1.LeasingSavings\x12H\n\x15cash_purchase_savings\x18\t \x01(\x0b2).google.maps.solar.v1.CashPurchaseSavings\x12P\n\x19financed_purchase_savings\x18\n \x01(\x0b2-.google.maps.solar.v1.FinancedPurchaseSavingsB\x15\n\x13_panel_config_index"\x87\x04\n\x10FinancialDetails\x12\x1f\n\x17initial_ac_kwh_per_year\x18\x01 \x01(\x02\x12;\n\x1fremaining_lifetime_utility_bill\x18\x02 \x01(\x0b2\x12.google.type.Money\x12-\n\x11federal_incentive\x18\x03 \x01(\x0b2\x12.google.type.Money\x12+\n\x0fstate_incentive\x18\x04 \x01(\x0b2\x12.google.type.Money\x12-\n\x11utility_incentive\x18\x05 \x01(\x0b2\x12.google.type.Money\x12/\n\x13lifetime_srec_total\x18\x06 \x01(\x0b2\x12.google.type.Money\x12=\n!cost_of_electricity_without_solar\x18\x07 \x01(\x0b2\x12.google.type.Money\x12\x1c\n\x14net_metering_allowed\x18\x08 \x01(\x08\x12\x1d\n\x10solar_percentage\x18\t \x01(\x02H\x00\x88\x01\x01\x12(\n\x1bpercentage_exported_to_grid\x18\n \x01(\x02H\x01\x88\x01\x01B\x13\n\x11_solar_percentageB\x1e\n\x1c_percentage_exported_to_grid"\xae\x02\n\x0fSavingsOverTime\x12)\n\rsavings_year1\x18\x01 \x01(\x0b2\x12.google.type.Money\x12*\n\x0esavings_year20\x18\x02 \x01(\x0b2\x12.google.type.Money\x12;\n\x1fpresent_value_of_savings_year20\x18\x03 \x01(\x0b2\x12.google.type.Money\x12,\n\x10savings_lifetime\x18\x05 \x01(\x0b2\x12.google.type.Money\x12=\n!present_value_of_savings_lifetime\x18\x06 \x01(\x0b2\x12.google.type.Money\x12\x1a\n\x12financially_viable\x18\x04 \x01(\x08"\xab\x01\n\x0eLeasingSavings\x12\x16\n\x0eleases_allowed\x18\x01 \x01(\x08\x12\x18\n\x10leases_supported\x18\x02 \x01(\x08\x12/\n\x13annual_leasing_cost\x18\x03 \x01(\x0b2\x12.google.type.Money\x126\n\x07savings\x18\x04 \x01(\x0b2%.google.maps.solar.v1.SavingsOverTime"\xff\x01\n\x13CashPurchaseSavings\x12.\n\x12out_of_pocket_cost\x18\x01 \x01(\x0b2\x12.google.type.Money\x12(\n\x0cupfront_cost\x18\x02 \x01(\x0b2\x12.google.type.Money\x12(\n\x0crebate_value\x18\x03 \x01(\x0b2\x12.google.type.Money\x12\x1a\n\rpayback_years\x18\x04 \x01(\x02H\x00\x88\x01\x01\x126\n\x07savings\x18\x05 \x01(\x0b2%.google.maps.solar.v1.SavingsOverTimeB\x10\n\x0e_payback_years"\xc8\x01\n\x17FinancedPurchaseSavings\x12/\n\x13annual_loan_payment\x18\x01 \x01(\x0b2\x12.google.type.Money\x12(\n\x0crebate_value\x18\x02 \x01(\x0b2\x12.google.type.Money\x12\x1a\n\x12loan_interest_rate\x18\x03 \x01(\x02\x126\n\x07savings\x18\x04 \x01(\x0b2%.google.maps.solar.v1.SavingsOverTime"\xdc\x02\n\x14GetDataLayersRequest\x12*\n\x08location\x18\x01 \x01(\x0b2\x13.google.type.LatLngB\x03\xe0A\x02\x12\x1a\n\rradius_meters\x18\x02 \x01(\x02B\x03\xe0A\x02\x126\n\x04view\x18\x03 \x01(\x0e2#.google.maps.solar.v1.DataLayerViewB\x03\xe0A\x01\x12C\n\x10required_quality\x18\x05 \x01(\x0e2$.google.maps.solar.v1.ImageryQualityB\x03\xe0A\x01\x12\x1e\n\x11pixel_size_meters\x18\x06 \x01(\x02B\x03\xe0A\x01\x12#\n\x16exact_quality_required\x18\x07 \x01(\x08B\x03\xe0A\x01\x12:\n\x0bexperiments\x18\x08 \x03(\x0e2 .google.maps.solar.v1.ExperimentB\x03\xe0A\x01"\xa9\x02\n\nDataLayers\x12\'\n\x0cimagery_date\x18\x01 \x01(\x0b2\x11.google.type.Date\x121\n\x16imagery_processed_date\x18\x02 \x01(\x0b2\x11.google.type.Date\x12\x0f\n\x07dsm_url\x18\x03 \x01(\t\x12\x0f\n\x07rgb_url\x18\x04 \x01(\t\x12\x10\n\x08mask_url\x18\x05 \x01(\t\x12\x17\n\x0fannual_flux_url\x18\x06 \x01(\t\x12\x18\n\x10monthly_flux_url\x18\x07 \x01(\t\x12\x19\n\x11hourly_shade_urls\x18\x08 \x03(\t\x12=\n\x0fimagery_quality\x18\t \x01(\x0e2$.google.maps.solar.v1.ImageryQuality"$\n\x11GetGeoTiffRequest\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x02*\xa9\x01\n\rDataLayerView\x12\x1f\n\x1bDATA_LAYER_VIEW_UNSPECIFIED\x10\x00\x12\r\n\tDSM_LAYER\x10\x01\x12\x12\n\x0eIMAGERY_LAYERS\x10\x02\x12"\n\x1eIMAGERY_AND_ANNUAL_FLUX_LAYERS\x10\x03\x12\x1f\n\x1bIMAGERY_AND_ALL_FLUX_LAYERS\x10\x04\x12\x0f\n\x0bFULL_LAYERS\x10\x05*Z\n\x0eImageryQuality\x12\x1f\n\x1bIMAGERY_QUALITY_UNSPECIFIED\x10\x00\x12\x08\n\x04HIGH\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x12\x07\n\x03LOW\x10\x03\x12\x08\n\x04BASE\x10\x04*]\n\x15SolarPanelOrientation\x12\'\n#SOLAR_PANEL_ORIENTATION_UNSPECIFIED\x10\x00\x12\r\n\tLANDSCAPE\x10\x01\x12\x0c\n\x08PORTRAIT\x10\x02*?\n\nExperiment\x12\x1a\n\x16EXPERIMENT_UNSPECIFIED\x10\x00\x12\x15\n\x11EXPANDED_COVERAGE\x10\x012\xde\x03\n\x05Solar\x12\xa9\x01\n\x1bFindClosestBuildingInsights\x128.google.maps.solar.v1.FindClosestBuildingInsightsRequest\x1a&.google.maps.solar.v1.BuildingInsights"(\x82\xd3\xe4\x93\x02"\x12 /v1/buildingInsights:findClosest\x12y\n\rGetDataLayers\x12*.google.maps.solar.v1.GetDataLayersRequest\x1a .google.maps.solar.v1.DataLayers"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/dataLayers:get\x12d\n\nGetGeoTiff\x12\'.google.maps.solar.v1.GetGeoTiffRequest\x1a\x14.google.api.HttpBody"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1/geoTiff:get\x1aH\xcaA\x14solar.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xb7\x01\n\x18com.google.maps.solar.v1B\x11SolarServiceProtoP\x01Z4cloud.google.com/go/maps/solar/apiv1/solarpb;solarpb\xa2\x02\x07GGMPV1A\xaa\x02\x14Google.Maps.Solar.V1\xca\x02\x14Google\\Maps\\Solar\\V1\xea\x02\x17Google::Maps::Solar::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.solar.v1.solar_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.maps.solar.v1B\x11SolarServiceProtoP\x01Z4cloud.google.com/go/maps/solar/apiv1/solarpb;solarpb\xa2\x02\x07GGMPV1A\xaa\x02\x14Google.Maps.Solar.V1\xca\x02\x14Google\\Maps\\Solar\\V1\xea\x02\x17Google::Maps::Solar::V1'
    _globals['_FINDCLOSESTBUILDINGINSIGHTSREQUEST'].fields_by_name['location']._loaded_options = None
    _globals['_FINDCLOSESTBUILDINGINSIGHTSREQUEST'].fields_by_name['location']._serialized_options = b'\xe0A\x02'
    _globals['_FINDCLOSESTBUILDINGINSIGHTSREQUEST'].fields_by_name['required_quality']._loaded_options = None
    _globals['_FINDCLOSESTBUILDINGINSIGHTSREQUEST'].fields_by_name['required_quality']._serialized_options = b'\xe0A\x01'
    _globals['_FINDCLOSESTBUILDINGINSIGHTSREQUEST'].fields_by_name['exact_quality_required']._loaded_options = None
    _globals['_FINDCLOSESTBUILDINGINSIGHTSREQUEST'].fields_by_name['exact_quality_required']._serialized_options = b'\xe0A\x01'
    _globals['_FINDCLOSESTBUILDINGINSIGHTSREQUEST'].fields_by_name['experiments']._loaded_options = None
    _globals['_FINDCLOSESTBUILDINGINSIGHTSREQUEST'].fields_by_name['experiments']._serialized_options = b'\xe0A\x01'
    _globals['_GETDATALAYERSREQUEST'].fields_by_name['location']._loaded_options = None
    _globals['_GETDATALAYERSREQUEST'].fields_by_name['location']._serialized_options = b'\xe0A\x02'
    _globals['_GETDATALAYERSREQUEST'].fields_by_name['radius_meters']._loaded_options = None
    _globals['_GETDATALAYERSREQUEST'].fields_by_name['radius_meters']._serialized_options = b'\xe0A\x02'
    _globals['_GETDATALAYERSREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_GETDATALAYERSREQUEST'].fields_by_name['view']._serialized_options = b'\xe0A\x01'
    _globals['_GETDATALAYERSREQUEST'].fields_by_name['required_quality']._loaded_options = None
    _globals['_GETDATALAYERSREQUEST'].fields_by_name['required_quality']._serialized_options = b'\xe0A\x01'
    _globals['_GETDATALAYERSREQUEST'].fields_by_name['pixel_size_meters']._loaded_options = None
    _globals['_GETDATALAYERSREQUEST'].fields_by_name['pixel_size_meters']._serialized_options = b'\xe0A\x01'
    _globals['_GETDATALAYERSREQUEST'].fields_by_name['exact_quality_required']._loaded_options = None
    _globals['_GETDATALAYERSREQUEST'].fields_by_name['exact_quality_required']._serialized_options = b'\xe0A\x01'
    _globals['_GETDATALAYERSREQUEST'].fields_by_name['experiments']._loaded_options = None
    _globals['_GETDATALAYERSREQUEST'].fields_by_name['experiments']._serialized_options = b'\xe0A\x01'
    _globals['_GETGEOTIFFREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_GETGEOTIFFREQUEST'].fields_by_name['id']._serialized_options = b'\xe0A\x02'
    _globals['_SOLAR']._loaded_options = None
    _globals['_SOLAR']._serialized_options = b'\xcaA\x14solar.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SOLAR'].methods_by_name['FindClosestBuildingInsights']._loaded_options = None
    _globals['_SOLAR'].methods_by_name['FindClosestBuildingInsights']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /v1/buildingInsights:findClosest'
    _globals['_SOLAR'].methods_by_name['GetDataLayers']._loaded_options = None
    _globals['_SOLAR'].methods_by_name['GetDataLayers']._serialized_options = b'\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/dataLayers:get'
    _globals['_SOLAR'].methods_by_name['GetGeoTiff']._loaded_options = None
    _globals['_SOLAR'].methods_by_name['GetGeoTiff']._serialized_options = b'\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1/geoTiff:get'
    _globals['_DATALAYERVIEW']._serialized_start = 5352
    _globals['_DATALAYERVIEW']._serialized_end = 5521
    _globals['_IMAGERYQUALITY']._serialized_start = 5523
    _globals['_IMAGERYQUALITY']._serialized_end = 5613
    _globals['_SOLARPANELORIENTATION']._serialized_start = 5615
    _globals['_SOLARPANELORIENTATION']._serialized_end = 5708
    _globals['_EXPERIMENT']._serialized_start = 5710
    _globals['_EXPERIMENT']._serialized_end = 5773
    _globals['_FINDCLOSESTBUILDINGINSIGHTSREQUEST']._serialized_start = 257
    _globals['_FINDCLOSESTBUILDINGINSIGHTSREQUEST']._serialized_end = 503
    _globals['_LATLNGBOX']._serialized_start = 505
    _globals['_LATLNGBOX']._serialized_end = 582
    _globals['_BUILDINGINSIGHTS']._serialized_start = 585
    _globals['_BUILDINGINSIGHTS']._serialized_end = 1024
    _globals['_SOLARPOTENTIAL']._serialized_start = 1027
    _globals['_SOLARPOTENTIAL']._serialized_end = 1717
    _globals['_ROOFSEGMENTSIZEANDSUNSHINESTATS']._serialized_start = 1720
    _globals['_ROOFSEGMENTSIZEANDSUNSHINESTATS']._serialized_end = 2078
    _globals['_SIZEANDSUNSHINESTATS']._serialized_start = 2080
    _globals['_SIZEANDSUNSHINESTATS']._serialized_end = 2181
    _globals['_SOLARPANEL']._serialized_start = 2184
    _globals['_SOLARPANEL']._serialized_end = 2375
    _globals['_SOLARPANELCONFIG']._serialized_start = 2378
    _globals['_SOLARPANELCONFIG']._serialized_end = 2522
    _globals['_ROOFSEGMENTSUMMARY']._serialized_start = 2525
    _globals['_ROOFSEGMENTSUMMARY']._serialized_end = 2739
    _globals['_FINANCIALANALYSIS']._serialized_start = 2742
    _globals['_FINANCIALANALYSIS']._serialized_end = 3198
    _globals['_FINANCIALDETAILS']._serialized_start = 3201
    _globals['_FINANCIALDETAILS']._serialized_end = 3720
    _globals['_SAVINGSOVERTIME']._serialized_start = 3723
    _globals['_SAVINGSOVERTIME']._serialized_end = 4025
    _globals['_LEASINGSAVINGS']._serialized_start = 4028
    _globals['_LEASINGSAVINGS']._serialized_end = 4199
    _globals['_CASHPURCHASESAVINGS']._serialized_start = 4202
    _globals['_CASHPURCHASESAVINGS']._serialized_end = 4457
    _globals['_FINANCEDPURCHASESAVINGS']._serialized_start = 4460
    _globals['_FINANCEDPURCHASESAVINGS']._serialized_end = 4660
    _globals['_GETDATALAYERSREQUEST']._serialized_start = 4663
    _globals['_GETDATALAYERSREQUEST']._serialized_end = 5011
    _globals['_DATALAYERS']._serialized_start = 5014
    _globals['_DATALAYERS']._serialized_end = 5311
    _globals['_GETGEOTIFFREQUEST']._serialized_start = 5313
    _globals['_GETGEOTIFFREQUEST']._serialized_end = 5349
    _globals['_SOLAR']._serialized_start = 5776
    _globals['_SOLAR']._serialized_end = 6254