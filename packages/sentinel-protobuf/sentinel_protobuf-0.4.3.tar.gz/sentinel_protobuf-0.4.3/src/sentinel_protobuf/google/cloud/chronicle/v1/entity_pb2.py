"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/chronicle/v1/entity.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/chronicle/v1/entity.proto\x12\x19google.cloud.chronicle.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd5\x06\n\tWatchlist\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1f\n\x12multiplying_factor\x18\x05 \x01(\x02B\x03\xe0A\x01\x12h\n\x1bentity_population_mechanism\x18\x06 \x01(\x0b2>.google.cloud.chronicle.v1.Watchlist.EntityPopulationMechanismB\x03\xe0A\x02\x12K\n\x0centity_count\x18\x07 \x01(\x0b20.google.cloud.chronicle.v1.Watchlist.EntityCountB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\\\n\x1awatchlist_user_preferences\x18\n \x01(\x0b23.google.cloud.chronicle.v1.WatchlistUserPreferencesB\x03\xe0A\x01\x1a\x90\x01\n\x19EntityPopulationMechanism\x12\\\n\x06manual\x18\x01 \x01(\x0b2E.google.cloud.chronicle.v1.Watchlist.EntityPopulationMechanism.ManualB\x03\xe0A\x01H\x00\x1a\x08\n\x06ManualB\x0b\n\tmechanism\x1a4\n\x0bEntityCount\x12\x11\n\x04user\x18\x01 \x01(\x05B\x03\xe0A\x03\x12\x12\n\x05asset\x18\x02 \x01(\x05B\x03\xe0A\x03:\x94\x01\xeaA\x90\x01\n"chronicle.googleapis.com/Watchlist\x12Sprojects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}*\nwatchlists2\twatchlist"/\n\x18WatchlistUserPreferences\x12\x13\n\x06pinned\x18\x01 \x01(\x08B\x03\xe0A\x01"O\n\x13GetWatchlistRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"chronicle.googleapis.com/Watchlist"\x99\x01\n\x15ListWatchlistsRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"chronicle.googleapis.com/Watchlist\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"u\n\x16ListWatchlistsResponse\x12=\n\nwatchlists\x18\x01 \x03(\x0b2$.google.cloud.chronicle.v1.WatchlistB\x03\xe0A\x01\x12\x1c\n\x0fnext_page_token\x18\x02 \x01(\tB\x03\xe0A\x01"\xad\x01\n\x16CreateWatchlistRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"chronicle.googleapis.com/Watchlist\x12\x19\n\x0cwatchlist_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12<\n\twatchlist\x18\x03 \x01(\x0b2$.google.cloud.chronicle.v1.WatchlistB\x03\xe0A\x02"\x8c\x01\n\x16UpdateWatchlistRequest\x12<\n\twatchlist\x18\x01 \x01(\x0b2$.google.cloud.chronicle.v1.WatchlistB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"f\n\x16DeleteWatchlistRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"chronicle.googleapis.com/Watchlist\x12\x12\n\x05force\x18\x02 \x01(\x08B\x03\xe0A\x012\xbe\x08\n\rEntityService\x12\xaf\x01\n\x0cGetWatchlist\x12..google.cloud.chronicle.v1.GetWatchlistRequest\x1a$.google.cloud.chronicle.v1.Watchlist"I\xdaA\x04name\x82\xd3\xe4\x93\x02<\x12:/v1/{name=projects/*/locations/*/instances/*/watchlists/*}\x12\xc2\x01\n\x0eListWatchlists\x120.google.cloud.chronicle.v1.ListWatchlistsRequest\x1a1.google.cloud.chronicle.v1.ListWatchlistsResponse"K\xdaA\x06parent\x82\xd3\xe4\x93\x02<\x12:/v1/{parent=projects/*/locations/*/instances/*}/watchlists\x12\xd9\x01\n\x0fCreateWatchlist\x121.google.cloud.chronicle.v1.CreateWatchlistRequest\x1a$.google.cloud.chronicle.v1.Watchlist"m\xdaA\x1dparent,watchlist,watchlist_id\x82\xd3\xe4\x93\x02G":/v1/{parent=projects/*/locations/*/instances/*}/watchlists:\twatchlist\x12\xdb\x01\n\x0fUpdateWatchlist\x121.google.cloud.chronicle.v1.UpdateWatchlistRequest\x1a$.google.cloud.chronicle.v1.Watchlist"o\xdaA\x15watchlist,update_mask\x82\xd3\xe4\x93\x02Q2D/v1/{watchlist.name=projects/*/locations/*/instances/*/watchlists/*}:\twatchlist\x12\xad\x01\n\x0fDeleteWatchlist\x121.google.cloud.chronicle.v1.DeleteWatchlistRequest\x1a\x16.google.protobuf.Empty"O\xdaA\nname,force\x82\xd3\xe4\x93\x02<*:/v1/{name=projects/*/locations/*/instances/*/watchlists/*}\x1aL\xcaA\x18chronicle.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xc2\x01\n\x1dcom.google.cloud.chronicle.v1B\x0bEntityProtoP\x01Z;cloud.google.com/go/chronicle/apiv1/chroniclepb;chroniclepb\xaa\x02\x19Google.Cloud.Chronicle.V1\xca\x02\x19Google\\Cloud\\Chronicle\\V1\xea\x02\x1cGoogle::Cloud::Chronicle::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.chronicle.v1.entity_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.chronicle.v1B\x0bEntityProtoP\x01Z;cloud.google.com/go/chronicle/apiv1/chroniclepb;chroniclepb\xaa\x02\x19Google.Cloud.Chronicle.V1\xca\x02\x19Google\\Cloud\\Chronicle\\V1\xea\x02\x1cGoogle::Cloud::Chronicle::V1'
    _globals['_WATCHLIST_ENTITYPOPULATIONMECHANISM'].fields_by_name['manual']._loaded_options = None
    _globals['_WATCHLIST_ENTITYPOPULATIONMECHANISM'].fields_by_name['manual']._serialized_options = b'\xe0A\x01'
    _globals['_WATCHLIST_ENTITYCOUNT'].fields_by_name['user']._loaded_options = None
    _globals['_WATCHLIST_ENTITYCOUNT'].fields_by_name['user']._serialized_options = b'\xe0A\x03'
    _globals['_WATCHLIST_ENTITYCOUNT'].fields_by_name['asset']._loaded_options = None
    _globals['_WATCHLIST_ENTITYCOUNT'].fields_by_name['asset']._serialized_options = b'\xe0A\x03'
    _globals['_WATCHLIST'].fields_by_name['name']._loaded_options = None
    _globals['_WATCHLIST'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_WATCHLIST'].fields_by_name['display_name']._loaded_options = None
    _globals['_WATCHLIST'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_WATCHLIST'].fields_by_name['description']._loaded_options = None
    _globals['_WATCHLIST'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_WATCHLIST'].fields_by_name['multiplying_factor']._loaded_options = None
    _globals['_WATCHLIST'].fields_by_name['multiplying_factor']._serialized_options = b'\xe0A\x01'
    _globals['_WATCHLIST'].fields_by_name['entity_population_mechanism']._loaded_options = None
    _globals['_WATCHLIST'].fields_by_name['entity_population_mechanism']._serialized_options = b'\xe0A\x02'
    _globals['_WATCHLIST'].fields_by_name['entity_count']._loaded_options = None
    _globals['_WATCHLIST'].fields_by_name['entity_count']._serialized_options = b'\xe0A\x03'
    _globals['_WATCHLIST'].fields_by_name['create_time']._loaded_options = None
    _globals['_WATCHLIST'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_WATCHLIST'].fields_by_name['update_time']._loaded_options = None
    _globals['_WATCHLIST'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_WATCHLIST'].fields_by_name['watchlist_user_preferences']._loaded_options = None
    _globals['_WATCHLIST'].fields_by_name['watchlist_user_preferences']._serialized_options = b'\xe0A\x01'
    _globals['_WATCHLIST']._loaded_options = None
    _globals['_WATCHLIST']._serialized_options = b'\xeaA\x90\x01\n"chronicle.googleapis.com/Watchlist\x12Sprojects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}*\nwatchlists2\twatchlist'
    _globals['_WATCHLISTUSERPREFERENCES'].fields_by_name['pinned']._loaded_options = None
    _globals['_WATCHLISTUSERPREFERENCES'].fields_by_name['pinned']._serialized_options = b'\xe0A\x01'
    _globals['_GETWATCHLISTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETWATCHLISTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"chronicle.googleapis.com/Watchlist'
    _globals['_LISTWATCHLISTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTWATCHLISTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"chronicle.googleapis.com/Watchlist'
    _globals['_LISTWATCHLISTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTWATCHLISTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTWATCHLISTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTWATCHLISTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTWATCHLISTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTWATCHLISTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTWATCHLISTSRESPONSE'].fields_by_name['watchlists']._loaded_options = None
    _globals['_LISTWATCHLISTSRESPONSE'].fields_by_name['watchlists']._serialized_options = b'\xe0A\x01'
    _globals['_LISTWATCHLISTSRESPONSE'].fields_by_name['next_page_token']._loaded_options = None
    _globals['_LISTWATCHLISTSRESPONSE'].fields_by_name['next_page_token']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEWATCHLISTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEWATCHLISTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"chronicle.googleapis.com/Watchlist'
    _globals['_CREATEWATCHLISTREQUEST'].fields_by_name['watchlist_id']._loaded_options = None
    _globals['_CREATEWATCHLISTREQUEST'].fields_by_name['watchlist_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEWATCHLISTREQUEST'].fields_by_name['watchlist']._loaded_options = None
    _globals['_CREATEWATCHLISTREQUEST'].fields_by_name['watchlist']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEWATCHLISTREQUEST'].fields_by_name['watchlist']._loaded_options = None
    _globals['_UPDATEWATCHLISTREQUEST'].fields_by_name['watchlist']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEWATCHLISTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEWATCHLISTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEWATCHLISTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEWATCHLISTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"chronicle.googleapis.com/Watchlist'
    _globals['_DELETEWATCHLISTREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETEWATCHLISTREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x01'
    _globals['_ENTITYSERVICE']._loaded_options = None
    _globals['_ENTITYSERVICE']._serialized_options = b'\xcaA\x18chronicle.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ENTITYSERVICE'].methods_by_name['GetWatchlist']._loaded_options = None
    _globals['_ENTITYSERVICE'].methods_by_name['GetWatchlist']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02<\x12:/v1/{name=projects/*/locations/*/instances/*/watchlists/*}'
    _globals['_ENTITYSERVICE'].methods_by_name['ListWatchlists']._loaded_options = None
    _globals['_ENTITYSERVICE'].methods_by_name['ListWatchlists']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02<\x12:/v1/{parent=projects/*/locations/*/instances/*}/watchlists'
    _globals['_ENTITYSERVICE'].methods_by_name['CreateWatchlist']._loaded_options = None
    _globals['_ENTITYSERVICE'].methods_by_name['CreateWatchlist']._serialized_options = b'\xdaA\x1dparent,watchlist,watchlist_id\x82\xd3\xe4\x93\x02G":/v1/{parent=projects/*/locations/*/instances/*}/watchlists:\twatchlist'
    _globals['_ENTITYSERVICE'].methods_by_name['UpdateWatchlist']._loaded_options = None
    _globals['_ENTITYSERVICE'].methods_by_name['UpdateWatchlist']._serialized_options = b'\xdaA\x15watchlist,update_mask\x82\xd3\xe4\x93\x02Q2D/v1/{watchlist.name=projects/*/locations/*/instances/*/watchlists/*}:\twatchlist'
    _globals['_ENTITYSERVICE'].methods_by_name['DeleteWatchlist']._loaded_options = None
    _globals['_ENTITYSERVICE'].methods_by_name['DeleteWatchlist']._serialized_options = b'\xdaA\nname,force\x82\xd3\xe4\x93\x02<*:/v1/{name=projects/*/locations/*/instances/*/watchlists/*}'
    _globals['_WATCHLIST']._serialized_start = 281
    _globals['_WATCHLIST']._serialized_end = 1134
    _globals['_WATCHLIST_ENTITYPOPULATIONMECHANISM']._serialized_start = 785
    _globals['_WATCHLIST_ENTITYPOPULATIONMECHANISM']._serialized_end = 929
    _globals['_WATCHLIST_ENTITYPOPULATIONMECHANISM_MANUAL']._serialized_start = 908
    _globals['_WATCHLIST_ENTITYPOPULATIONMECHANISM_MANUAL']._serialized_end = 916
    _globals['_WATCHLIST_ENTITYCOUNT']._serialized_start = 931
    _globals['_WATCHLIST_ENTITYCOUNT']._serialized_end = 983
    _globals['_WATCHLISTUSERPREFERENCES']._serialized_start = 1136
    _globals['_WATCHLISTUSERPREFERENCES']._serialized_end = 1183
    _globals['_GETWATCHLISTREQUEST']._serialized_start = 1185
    _globals['_GETWATCHLISTREQUEST']._serialized_end = 1264
    _globals['_LISTWATCHLISTSREQUEST']._serialized_start = 1267
    _globals['_LISTWATCHLISTSREQUEST']._serialized_end = 1420
    _globals['_LISTWATCHLISTSRESPONSE']._serialized_start = 1422
    _globals['_LISTWATCHLISTSRESPONSE']._serialized_end = 1539
    _globals['_CREATEWATCHLISTREQUEST']._serialized_start = 1542
    _globals['_CREATEWATCHLISTREQUEST']._serialized_end = 1715
    _globals['_UPDATEWATCHLISTREQUEST']._serialized_start = 1718
    _globals['_UPDATEWATCHLISTREQUEST']._serialized_end = 1858
    _globals['_DELETEWATCHLISTREQUEST']._serialized_start = 1860
    _globals['_DELETEWATCHLISTREQUEST']._serialized_end = 1962
    _globals['_ENTITYSERVICE']._serialized_start = 1965
    _globals['_ENTITYSERVICE']._serialized_end = 3051