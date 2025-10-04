"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/admanager/v1/ad_break_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import ad_break_messages_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_ad__break__messages__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/ads/admanager/v1/ad_break_service.proto\x12\x17google.ads.admanager.v1\x1a/google/ads/admanager/v1/ad_break_messages.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"K\n\x11GetAdBreakRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n admanager.googleapis.com/AdBreak"\xc7\x01\n\x13ListAdBreaksRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(admanager.googleapis.com/LiveStreamEvent\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04skip\x18\x06 \x01(\x05B\x03\xe0A\x01"x\n\x14ListAdBreaksResponse\x123\n\tad_breaks\x18\x01 \x03(\x0b2 .google.ads.admanager.v1.AdBreak\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"\x91\x01\n\x14CreateAdBreakRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(admanager.googleapis.com/LiveStreamEvent\x127\n\x08ad_break\x18\x02 \x01(\x0b2 .google.ads.admanager.v1.AdBreakB\x03\xe0A\x02"\x85\x01\n\x14UpdateAdBreakRequest\x127\n\x08ad_break\x18\x01 \x01(\x0b2 .google.ads.admanager.v1.AdBreakB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"N\n\x14DeleteAdBreakRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n admanager.googleapis.com/AdBreak2\x97\x0b\n\x0eAdBreakService\x12\xa8\x02\n\nGetAdBreak\x12*.google.ads.admanager.v1.GetAdBreakRequest\x1a .google.ads.admanager.v1.AdBreak"\xcb\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xbd\x01\x12=/v1/{name=networks/*/liveStreamEventsByAssetKey/*/adBreaks/*}ZE\x12C/v1/{name=networks/*/liveStreamEventsByCustomAssetKey/*/adBreaks/*}Z5\x123/v1/{name=networks/*/liveStreamEvents/*/adBreaks/*}\x12\xbb\x02\n\x0cListAdBreaks\x12,.google.ads.admanager.v1.ListAdBreaksRequest\x1a-.google.ads.admanager.v1.ListAdBreaksResponse"\xcd\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xbd\x01\x12=/v1/{parent=networks/*/liveStreamEventsByAssetKey/*}/adBreaksZE\x12C/v1/{parent=networks/*/liveStreamEventsByCustomAssetKey/*}/adBreaksZ5\x123/v1/{parent=networks/*/liveStreamEvents/*}/adBreaks\x12\xd7\x02\n\rCreateAdBreak\x12-.google.ads.admanager.v1.CreateAdBreakRequest\x1a .google.ads.admanager.v1.AdBreak"\xf4\x01\xdaA\x0fparent,ad_break\x82\xd3\xe4\x93\x02\xdb\x01"=/v1/{parent=networks/*/liveStreamEventsByAssetKey/*}/adBreaks:\x08ad_breakZO"C/v1/{parent=networks/*/liveStreamEventsByCustomAssetKey/*}/adBreaks:\x08ad_breakZ?"3/v1/{parent=networks/*/liveStreamEvents/*}/adBreaks:\x08ad_break\x12\xd1\x01\n\rUpdateAdBreak\x12-.google.ads.admanager.v1.UpdateAdBreakRequest\x1a .google.ads.admanager.v1.AdBreak"o\xdaA\x14ad_break,update_mask\x82\xd3\xe4\x93\x02R2F/v1/{ad_break.name=networks/*/liveStreamEventsByAssetKey/*/adBreaks/*}:\x08ad_break\x12\xa4\x01\n\rDeleteAdBreak\x12-.google.ads.admanager.v1.DeleteAdBreakRequest\x1a\x16.google.protobuf.Empty"L\xdaA\x04name\x82\xd3\xe4\x93\x02?*=/v1/{name=networks/*/liveStreamEventsByAssetKey/*/adBreaks/*}\x1aG\xcaA\x18admanager.googleapis.com\xd2A)https://www.googleapis.com/auth/admanagerB\xc7\x01\n\x1bcom.google.ads.admanager.v1B\x13AdBreakServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.ad_break_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x13AdBreakServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_GETADBREAKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETADBREAKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n admanager.googleapis.com/AdBreak'
    _globals['_LISTADBREAKSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTADBREAKSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(admanager.googleapis.com/LiveStreamEvent'
    _globals['_LISTADBREAKSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTADBREAKSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTADBREAKSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTADBREAKSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTADBREAKSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTADBREAKSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTADBREAKSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTADBREAKSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTADBREAKSREQUEST'].fields_by_name['skip']._loaded_options = None
    _globals['_LISTADBREAKSREQUEST'].fields_by_name['skip']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEADBREAKREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEADBREAKREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(admanager.googleapis.com/LiveStreamEvent'
    _globals['_CREATEADBREAKREQUEST'].fields_by_name['ad_break']._loaded_options = None
    _globals['_CREATEADBREAKREQUEST'].fields_by_name['ad_break']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEADBREAKREQUEST'].fields_by_name['ad_break']._loaded_options = None
    _globals['_UPDATEADBREAKREQUEST'].fields_by_name['ad_break']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEADBREAKREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEADBREAKREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEADBREAKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEADBREAKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n admanager.googleapis.com/AdBreak'
    _globals['_ADBREAKSERVICE']._loaded_options = None
    _globals['_ADBREAKSERVICE']._serialized_options = b'\xcaA\x18admanager.googleapis.com\xd2A)https://www.googleapis.com/auth/admanager'
    _globals['_ADBREAKSERVICE'].methods_by_name['GetAdBreak']._loaded_options = None
    _globals['_ADBREAKSERVICE'].methods_by_name['GetAdBreak']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xbd\x01\x12=/v1/{name=networks/*/liveStreamEventsByAssetKey/*/adBreaks/*}ZE\x12C/v1/{name=networks/*/liveStreamEventsByCustomAssetKey/*/adBreaks/*}Z5\x123/v1/{name=networks/*/liveStreamEvents/*/adBreaks/*}'
    _globals['_ADBREAKSERVICE'].methods_by_name['ListAdBreaks']._loaded_options = None
    _globals['_ADBREAKSERVICE'].methods_by_name['ListAdBreaks']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xbd\x01\x12=/v1/{parent=networks/*/liveStreamEventsByAssetKey/*}/adBreaksZE\x12C/v1/{parent=networks/*/liveStreamEventsByCustomAssetKey/*}/adBreaksZ5\x123/v1/{parent=networks/*/liveStreamEvents/*}/adBreaks'
    _globals['_ADBREAKSERVICE'].methods_by_name['CreateAdBreak']._loaded_options = None
    _globals['_ADBREAKSERVICE'].methods_by_name['CreateAdBreak']._serialized_options = b'\xdaA\x0fparent,ad_break\x82\xd3\xe4\x93\x02\xdb\x01"=/v1/{parent=networks/*/liveStreamEventsByAssetKey/*}/adBreaks:\x08ad_breakZO"C/v1/{parent=networks/*/liveStreamEventsByCustomAssetKey/*}/adBreaks:\x08ad_breakZ?"3/v1/{parent=networks/*/liveStreamEvents/*}/adBreaks:\x08ad_break'
    _globals['_ADBREAKSERVICE'].methods_by_name['UpdateAdBreak']._loaded_options = None
    _globals['_ADBREAKSERVICE'].methods_by_name['UpdateAdBreak']._serialized_options = b'\xdaA\x14ad_break,update_mask\x82\xd3\xe4\x93\x02R2F/v1/{ad_break.name=networks/*/liveStreamEventsByAssetKey/*/adBreaks/*}:\x08ad_break'
    _globals['_ADBREAKSERVICE'].methods_by_name['DeleteAdBreak']._loaded_options = None
    _globals['_ADBREAKSERVICE'].methods_by_name['DeleteAdBreak']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02?*=/v1/{name=networks/*/liveStreamEventsByAssetKey/*/adBreaks/*}'
    _globals['_GETADBREAKREQUEST']._serialized_start = 302
    _globals['_GETADBREAKREQUEST']._serialized_end = 377
    _globals['_LISTADBREAKSREQUEST']._serialized_start = 380
    _globals['_LISTADBREAKSREQUEST']._serialized_end = 579
    _globals['_LISTADBREAKSRESPONSE']._serialized_start = 581
    _globals['_LISTADBREAKSRESPONSE']._serialized_end = 701
    _globals['_CREATEADBREAKREQUEST']._serialized_start = 704
    _globals['_CREATEADBREAKREQUEST']._serialized_end = 849
    _globals['_UPDATEADBREAKREQUEST']._serialized_start = 852
    _globals['_UPDATEADBREAKREQUEST']._serialized_end = 985
    _globals['_DELETEADBREAKREQUEST']._serialized_start = 987
    _globals['_DELETEADBREAKREQUEST']._serialized_end = 1065
    _globals['_ADBREAKSERVICE']._serialized_start = 1068
    _globals['_ADBREAKSERVICE']._serialized_end = 2499