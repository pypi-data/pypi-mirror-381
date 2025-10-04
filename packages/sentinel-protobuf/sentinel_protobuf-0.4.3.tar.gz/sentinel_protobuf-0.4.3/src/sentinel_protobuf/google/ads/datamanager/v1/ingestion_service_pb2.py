"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/datamanager/v1/ingestion_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.datamanager.v1 import audience_pb2 as google_dot_ads_dot_datamanager_dot_v1_dot_audience__pb2
from .....google.ads.datamanager.v1 import consent_pb2 as google_dot_ads_dot_datamanager_dot_v1_dot_consent__pb2
from .....google.ads.datamanager.v1 import destination_pb2 as google_dot_ads_dot_datamanager_dot_v1_dot_destination__pb2
from .....google.ads.datamanager.v1 import encryption_info_pb2 as google_dot_ads_dot_datamanager_dot_v1_dot_encryption__info__pb2
from .....google.ads.datamanager.v1 import event_pb2 as google_dot_ads_dot_datamanager_dot_v1_dot_event__pb2
from .....google.ads.datamanager.v1 import terms_of_service_pb2 as google_dot_ads_dot_datamanager_dot_v1_dot_terms__of__service__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/ads/datamanager/v1/ingestion_service.proto\x12\x19google.ads.datamanager.v1\x1a(google/ads/datamanager/v1/audience.proto\x1a\'google/ads/datamanager/v1/consent.proto\x1a+google/ads/datamanager/v1/destination.proto\x1a/google/ads/datamanager/v1/encryption_info.proto\x1a%google/ads/datamanager/v1/event.proto\x1a0google/ads/datamanager/v1/terms_of_service.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto"\xd0\x03\n\x1cIngestAudienceMembersRequest\x12A\n\x0cdestinations\x18\x01 \x03(\x0b2&.google.ads.datamanager.v1.DestinationB\x03\xe0A\x02\x12H\n\x10audience_members\x18\x02 \x03(\x0b2).google.ads.datamanager.v1.AudienceMemberB\x03\xe0A\x02\x128\n\x07consent\x18\x03 \x01(\x0b2".google.ads.datamanager.v1.ConsentB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x04 \x01(\x08B\x03\xe0A\x01\x12:\n\x08encoding\x18\x05 \x01(\x0e2#.google.ads.datamanager.v1.EncodingB\x03\xe0A\x01\x12G\n\x0fencryption_info\x18\x06 \x01(\x0b2).google.ads.datamanager.v1.EncryptionInfoB\x03\xe0A\x01\x12H\n\x10terms_of_service\x18\x07 \x01(\x0b2).google.ads.datamanager.v1.TermsOfServiceB\x03\xe0A\x01"3\n\x1dIngestAudienceMembersResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t"\xcc\x02\n\x1cRemoveAudienceMembersRequest\x12A\n\x0cdestinations\x18\x01 \x03(\x0b2&.google.ads.datamanager.v1.DestinationB\x03\xe0A\x02\x12H\n\x10audience_members\x18\x02 \x03(\x0b2).google.ads.datamanager.v1.AudienceMemberB\x03\xe0A\x02\x12\x1a\n\rvalidate_only\x18\x03 \x01(\x08B\x03\xe0A\x01\x12:\n\x08encoding\x18\x04 \x01(\x0e2#.google.ads.datamanager.v1.EncodingB\x03\xe0A\x01\x12G\n\x0fencryption_info\x18\x05 \x01(\x0b2).google.ads.datamanager.v1.EncryptionInfoB\x03\xe0A\x01"3\n\x1dRemoveAudienceMembersResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t"\xea\x02\n\x13IngestEventsRequest\x12A\n\x0cdestinations\x18\x01 \x03(\x0b2&.google.ads.datamanager.v1.DestinationB\x03\xe0A\x02\x125\n\x06events\x18\x02 \x03(\x0b2 .google.ads.datamanager.v1.EventB\x03\xe0A\x02\x128\n\x07consent\x18\x03 \x01(\x0b2".google.ads.datamanager.v1.ConsentB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x04 \x01(\x08B\x03\xe0A\x01\x12:\n\x08encoding\x18\x05 \x01(\x0e2#.google.ads.datamanager.v1.EncodingB\x03\xe0A\x01\x12G\n\x0fencryption_info\x18\x06 \x01(\x0b2).google.ads.datamanager.v1.EncryptionInfoB\x03\xe0A\x01"*\n\x14IngestEventsResponse\x12\x12\n\nrequest_id\x18\x01 \x01(\t*9\n\x08Encoding\x12\x18\n\x14ENCODING_UNSPECIFIED\x10\x00\x12\x07\n\x03HEX\x10\x01\x12\n\n\x06BASE64\x10\x022\xd7\x04\n\x10IngestionService\x12\xb1\x01\n\x15IngestAudienceMembers\x127.google.ads.datamanager.v1.IngestAudienceMembersRequest\x1a8.google.ads.datamanager.v1.IngestAudienceMembersResponse"%\x82\xd3\xe4\x93\x02\x1f"\x1a/v1/audienceMembers:ingest:\x01*\x12\xb1\x01\n\x15RemoveAudienceMembers\x127.google.ads.datamanager.v1.RemoveAudienceMembersRequest\x1a8.google.ads.datamanager.v1.RemoveAudienceMembersResponse"%\x82\xd3\xe4\x93\x02\x1f"\x1a/v1/audienceMembers:remove:\x01*\x12\x8d\x01\n\x0cIngestEvents\x12..google.ads.datamanager.v1.IngestEventsRequest\x1a/.google.ads.datamanager.v1.IngestEventsResponse"\x1c\x82\xd3\xe4\x93\x02\x16"\x11/v1/events:ingest:\x01*\x1aK\xcaA\x1adatamanager.googleapis.com\xd2A+https://www.googleapis.com/auth/datamanagerB\xd5\x01\n\x1dcom.google.ads.datamanager.v1B\x15IngestionServiceProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager\xaa\x02\x19Google.Ads.DataManager.V1\xca\x02\x19Google\\Ads\\DataManager\\V1\xea\x02\x1cGoogle::Ads::DataManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.datamanager.v1.ingestion_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.ads.datamanager.v1B\x15IngestionServiceProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/datamanager/v1;datamanager\xaa\x02\x19Google.Ads.DataManager.V1\xca\x02\x19Google\\Ads\\DataManager\\V1\xea\x02\x1cGoogle::Ads::DataManager::V1'
    _globals['_INGESTAUDIENCEMEMBERSREQUEST'].fields_by_name['destinations']._loaded_options = None
    _globals['_INGESTAUDIENCEMEMBERSREQUEST'].fields_by_name['destinations']._serialized_options = b'\xe0A\x02'
    _globals['_INGESTAUDIENCEMEMBERSREQUEST'].fields_by_name['audience_members']._loaded_options = None
    _globals['_INGESTAUDIENCEMEMBERSREQUEST'].fields_by_name['audience_members']._serialized_options = b'\xe0A\x02'
    _globals['_INGESTAUDIENCEMEMBERSREQUEST'].fields_by_name['consent']._loaded_options = None
    _globals['_INGESTAUDIENCEMEMBERSREQUEST'].fields_by_name['consent']._serialized_options = b'\xe0A\x01'
    _globals['_INGESTAUDIENCEMEMBERSREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_INGESTAUDIENCEMEMBERSREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_INGESTAUDIENCEMEMBERSREQUEST'].fields_by_name['encoding']._loaded_options = None
    _globals['_INGESTAUDIENCEMEMBERSREQUEST'].fields_by_name['encoding']._serialized_options = b'\xe0A\x01'
    _globals['_INGESTAUDIENCEMEMBERSREQUEST'].fields_by_name['encryption_info']._loaded_options = None
    _globals['_INGESTAUDIENCEMEMBERSREQUEST'].fields_by_name['encryption_info']._serialized_options = b'\xe0A\x01'
    _globals['_INGESTAUDIENCEMEMBERSREQUEST'].fields_by_name['terms_of_service']._loaded_options = None
    _globals['_INGESTAUDIENCEMEMBERSREQUEST'].fields_by_name['terms_of_service']._serialized_options = b'\xe0A\x01'
    _globals['_REMOVEAUDIENCEMEMBERSREQUEST'].fields_by_name['destinations']._loaded_options = None
    _globals['_REMOVEAUDIENCEMEMBERSREQUEST'].fields_by_name['destinations']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVEAUDIENCEMEMBERSREQUEST'].fields_by_name['audience_members']._loaded_options = None
    _globals['_REMOVEAUDIENCEMEMBERSREQUEST'].fields_by_name['audience_members']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVEAUDIENCEMEMBERSREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_REMOVEAUDIENCEMEMBERSREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_REMOVEAUDIENCEMEMBERSREQUEST'].fields_by_name['encoding']._loaded_options = None
    _globals['_REMOVEAUDIENCEMEMBERSREQUEST'].fields_by_name['encoding']._serialized_options = b'\xe0A\x01'
    _globals['_REMOVEAUDIENCEMEMBERSREQUEST'].fields_by_name['encryption_info']._loaded_options = None
    _globals['_REMOVEAUDIENCEMEMBERSREQUEST'].fields_by_name['encryption_info']._serialized_options = b'\xe0A\x01'
    _globals['_INGESTEVENTSREQUEST'].fields_by_name['destinations']._loaded_options = None
    _globals['_INGESTEVENTSREQUEST'].fields_by_name['destinations']._serialized_options = b'\xe0A\x02'
    _globals['_INGESTEVENTSREQUEST'].fields_by_name['events']._loaded_options = None
    _globals['_INGESTEVENTSREQUEST'].fields_by_name['events']._serialized_options = b'\xe0A\x02'
    _globals['_INGESTEVENTSREQUEST'].fields_by_name['consent']._loaded_options = None
    _globals['_INGESTEVENTSREQUEST'].fields_by_name['consent']._serialized_options = b'\xe0A\x01'
    _globals['_INGESTEVENTSREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_INGESTEVENTSREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_INGESTEVENTSREQUEST'].fields_by_name['encoding']._loaded_options = None
    _globals['_INGESTEVENTSREQUEST'].fields_by_name['encoding']._serialized_options = b'\xe0A\x01'
    _globals['_INGESTEVENTSREQUEST'].fields_by_name['encryption_info']._loaded_options = None
    _globals['_INGESTEVENTSREQUEST'].fields_by_name['encryption_info']._serialized_options = b'\xe0A\x01'
    _globals['_INGESTIONSERVICE']._loaded_options = None
    _globals['_INGESTIONSERVICE']._serialized_options = b'\xcaA\x1adatamanager.googleapis.com\xd2A+https://www.googleapis.com/auth/datamanager'
    _globals['_INGESTIONSERVICE'].methods_by_name['IngestAudienceMembers']._loaded_options = None
    _globals['_INGESTIONSERVICE'].methods_by_name['IngestAudienceMembers']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f"\x1a/v1/audienceMembers:ingest:\x01*'
    _globals['_INGESTIONSERVICE'].methods_by_name['RemoveAudienceMembers']._loaded_options = None
    _globals['_INGESTIONSERVICE'].methods_by_name['RemoveAudienceMembers']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1f"\x1a/v1/audienceMembers:remove:\x01*'
    _globals['_INGESTIONSERVICE'].methods_by_name['IngestEvents']._loaded_options = None
    _globals['_INGESTIONSERVICE'].methods_by_name['IngestEvents']._serialized_options = b'\x82\xd3\xe4\x93\x02\x16"\x11/v1/events:ingest:\x01*'
    _globals['_ENCODING']._serialized_start = 1751
    _globals['_ENCODING']._serialized_end = 1808
    _globals['_INGESTAUDIENCEMEMBERSREQUEST']._serialized_start = 435
    _globals['_INGESTAUDIENCEMEMBERSREQUEST']._serialized_end = 899
    _globals['_INGESTAUDIENCEMEMBERSRESPONSE']._serialized_start = 901
    _globals['_INGESTAUDIENCEMEMBERSRESPONSE']._serialized_end = 952
    _globals['_REMOVEAUDIENCEMEMBERSREQUEST']._serialized_start = 955
    _globals['_REMOVEAUDIENCEMEMBERSREQUEST']._serialized_end = 1287
    _globals['_REMOVEAUDIENCEMEMBERSRESPONSE']._serialized_start = 1289
    _globals['_REMOVEAUDIENCEMEMBERSRESPONSE']._serialized_end = 1340
    _globals['_INGESTEVENTSREQUEST']._serialized_start = 1343
    _globals['_INGESTEVENTSREQUEST']._serialized_end = 1705
    _globals['_INGESTEVENTSRESPONSE']._serialized_start = 1707
    _globals['_INGESTEVENTSRESPONSE']._serialized_end = 1749
    _globals['_INGESTIONSERVICE']._serialized_start = 1811
    _globals['_INGESTIONSERVICE']._serialized_end = 2410