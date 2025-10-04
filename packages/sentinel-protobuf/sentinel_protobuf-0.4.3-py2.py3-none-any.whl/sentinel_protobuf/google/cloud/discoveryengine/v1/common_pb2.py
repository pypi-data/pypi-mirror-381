"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/common.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/discoveryengine/v1/common.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"x\n\x08Interval\x12\x11\n\x07minimum\x18\x01 \x01(\x01H\x00\x12\x1b\n\x11exclusive_minimum\x18\x02 \x01(\x01H\x00\x12\x11\n\x07maximum\x18\x03 \x01(\x01H\x01\x12\x1b\n\x11exclusive_maximum\x18\x04 \x01(\x01H\x01B\x05\n\x03minB\x05\n\x03max"0\n\x0fCustomAttribute\x12\x0c\n\x04text\x18\x01 \x03(\t\x12\x0f\n\x07numbers\x18\x02 \x03(\x01"G\n\x08UserInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x12\n\nuser_agent\x18\x02 \x01(\t\x12\x16\n\ttime_zone\x18\x03 \x01(\tB\x03\xe0A\x01"\x1c\n\nDoubleList\x12\x0e\n\x06values\x18\x01 \x03(\x01"]\n\tPrincipal\x12\x11\n\x07user_id\x18\x01 \x01(\tH\x00\x12\x12\n\x08group_id\x18\x02 \x01(\tH\x00\x12\x1c\n\x12external_entity_id\x18\x03 \x01(\tH\x00B\x0b\n\tprincipal"n\n\x14HealthcareFhirConfig\x12"\n\x1aenable_configurable_schema\x18\x01 \x01(\x08\x122\n*enable_static_indexing_for_batch_ingestion\x18\x02 \x01(\x08"\xc6\x01\n\x13SearchLinkPromotion\x12\x12\n\x05title\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x10\n\x03uri\x18\x02 \x01(\tB\x03\xe0A\x01\x12A\n\x08document\x18\x06 \x01(\tB/\xe0A\x01\xfaA)\n\'discoveryengine.googleapis.com/Document\x12\x16\n\timage_uri\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x14\n\x07enabled\x18\x05 \x01(\x08B\x03\xe0A\x01*b\n\x10IndustryVertical\x12!\n\x1dINDUSTRY_VERTICAL_UNSPECIFIED\x10\x00\x12\x0b\n\x07GENERIC\x10\x01\x12\t\n\x05MEDIA\x10\x02\x12\x13\n\x0fHEALTHCARE_FHIR\x10\x07*\xa4\x01\n\x0cSolutionType\x12\x1d\n\x19SOLUTION_TYPE_UNSPECIFIED\x10\x00\x12 \n\x1cSOLUTION_TYPE_RECOMMENDATION\x10\x01\x12\x18\n\x14SOLUTION_TYPE_SEARCH\x10\x02\x12\x16\n\x12SOLUTION_TYPE_CHAT\x10\x03\x12!\n\x1dSOLUTION_TYPE_GENERATIVE_CHAT\x10\x04*h\n\rSearchUseCase\x12\x1f\n\x1bSEARCH_USE_CASE_UNSPECIFIED\x10\x00\x12\x1a\n\x16SEARCH_USE_CASE_SEARCH\x10\x01\x12\x1a\n\x16SEARCH_USE_CASE_BROWSE\x10\x02*_\n\nSearchTier\x12\x1b\n\x17SEARCH_TIER_UNSPECIFIED\x10\x00\x12\x18\n\x14SEARCH_TIER_STANDARD\x10\x01\x12\x1a\n\x16SEARCH_TIER_ENTERPRISE\x10\x02*C\n\x0bSearchAddOn\x12\x1d\n\x19SEARCH_ADD_ON_UNSPECIFIED\x10\x00\x12\x15\n\x11SEARCH_ADD_ON_LLM\x10\x01B\xda\r\n#com.google.cloud.discoveryengine.v1B\x0bCommonProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1\xeaA\xe6\x01\n%discoveryengine.googleapis.com/Branch\x12Qprojects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}\x12jprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}\xeaAm\n)discoveryengine.googleapis.com/Collection\x12@projects/{project}/locations/{location}/collections/{collection}\xeaAR\n\'discoveryengine.googleapis.com/Location\x12\'projects/{project}/locations/{location}\xeaA}\n.discoveryengine.googleapis.com/GroundingConfig\x12Kprojects/{project}/locations/{location}/groundingConfigs/{grounding_config}\xeaAw\n,discoveryengine.googleapis.com/RankingConfig\x12Gprojects/{project}/locations/{location}/rankingConfigs/{ranking_config}\xeaAw\n,discoveryengine.googleapis.com/LicenseConfig\x12Gprojects/{project}/locations/{location}/licenseConfigs/{license_config}\xeaAk\n(discoveryengine.googleapis.com/UserStore\x12?projects/{project}/locations/{location}/userStores/{user_store}\xeaAy\n#healthcare.googleapis.com/FhirStore\x12Rprojects/{project}/locations/{location}/datasets/{dataset}/fhirStores/{fhir_store}\xeaA\xa4\x01\n&healthcare.googleapis.com/FhirResource\x12zprojects/{project}/locations/{location}/datasets/{dataset}/fhirStores/{fhir_store}/fhir/{resource_type}/{fhir_resource_id}\xeaAy\n"cloudkms.googleapis.com/CryptoKeys\x12Sprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}\xeaA\xa7\x01\n)cloudkms.googleapis.com/CryptoKeyVersions\x12zprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x0bCommonProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1\xeaA\xe6\x01\n%discoveryengine.googleapis.com/Branch\x12Qprojects/{project}/locations/{location}/dataStores/{data_store}/branches/{branch}\x12jprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}\xeaAm\n)discoveryengine.googleapis.com/Collection\x12@projects/{project}/locations/{location}/collections/{collection}\xeaAR\n\'discoveryengine.googleapis.com/Location\x12\'projects/{project}/locations/{location}\xeaA}\n.discoveryengine.googleapis.com/GroundingConfig\x12Kprojects/{project}/locations/{location}/groundingConfigs/{grounding_config}\xeaAw\n,discoveryengine.googleapis.com/RankingConfig\x12Gprojects/{project}/locations/{location}/rankingConfigs/{ranking_config}\xeaAw\n,discoveryengine.googleapis.com/LicenseConfig\x12Gprojects/{project}/locations/{location}/licenseConfigs/{license_config}\xeaAk\n(discoveryengine.googleapis.com/UserStore\x12?projects/{project}/locations/{location}/userStores/{user_store}\xeaAy\n#healthcare.googleapis.com/FhirStore\x12Rprojects/{project}/locations/{location}/datasets/{dataset}/fhirStores/{fhir_store}\xeaA\xa4\x01\n&healthcare.googleapis.com/FhirResource\x12zprojects/{project}/locations/{location}/datasets/{dataset}/fhirStores/{fhir_store}/fhir/{resource_type}/{fhir_resource_id}\xeaAy\n"cloudkms.googleapis.com/CryptoKeys\x12Sprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}\xeaA\xa7\x01\n)cloudkms.googleapis.com/CryptoKeyVersions\x12zprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}'
    _globals['_USERINFO'].fields_by_name['time_zone']._loaded_options = None
    _globals['_USERINFO'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHLINKPROMOTION'].fields_by_name['title']._loaded_options = None
    _globals['_SEARCHLINKPROMOTION'].fields_by_name['title']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHLINKPROMOTION'].fields_by_name['uri']._loaded_options = None
    _globals['_SEARCHLINKPROMOTION'].fields_by_name['uri']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHLINKPROMOTION'].fields_by_name['document']._loaded_options = None
    _globals['_SEARCHLINKPROMOTION'].fields_by_name['document']._serialized_options = b"\xe0A\x01\xfaA)\n'discoveryengine.googleapis.com/Document"
    _globals['_SEARCHLINKPROMOTION'].fields_by_name['image_uri']._loaded_options = None
    _globals['_SEARCHLINKPROMOTION'].fields_by_name['image_uri']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHLINKPROMOTION'].fields_by_name['description']._loaded_options = None
    _globals['_SEARCHLINKPROMOTION'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHLINKPROMOTION'].fields_by_name['enabled']._loaded_options = None
    _globals['_SEARCHLINKPROMOTION'].fields_by_name['enabled']._serialized_options = b'\xe0A\x01'
    _globals['_INDUSTRYVERTICAL']._serialized_start = 824
    _globals['_INDUSTRYVERTICAL']._serialized_end = 922
    _globals['_SOLUTIONTYPE']._serialized_start = 925
    _globals['_SOLUTIONTYPE']._serialized_end = 1089
    _globals['_SEARCHUSECASE']._serialized_start = 1091
    _globals['_SEARCHUSECASE']._serialized_end = 1195
    _globals['_SEARCHTIER']._serialized_start = 1197
    _globals['_SEARCHTIER']._serialized_end = 1292
    _globals['_SEARCHADDON']._serialized_start = 1294
    _globals['_SEARCHADDON']._serialized_end = 1361
    _globals['_INTERVAL']._serialized_start = 141
    _globals['_INTERVAL']._serialized_end = 261
    _globals['_CUSTOMATTRIBUTE']._serialized_start = 263
    _globals['_CUSTOMATTRIBUTE']._serialized_end = 311
    _globals['_USERINFO']._serialized_start = 313
    _globals['_USERINFO']._serialized_end = 384
    _globals['_DOUBLELIST']._serialized_start = 386
    _globals['_DOUBLELIST']._serialized_end = 414
    _globals['_PRINCIPAL']._serialized_start = 416
    _globals['_PRINCIPAL']._serialized_end = 509
    _globals['_HEALTHCAREFHIRCONFIG']._serialized_start = 511
    _globals['_HEALTHCAREFHIRCONFIG']._serialized_end = 621
    _globals['_SEARCHLINKPROMOTION']._serialized_start = 624
    _globals['_SEARCHLINKPROMOTION']._serialized_end = 822