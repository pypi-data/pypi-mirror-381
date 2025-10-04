"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1beta/user_event.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1beta import common_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_common__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/discoveryengine/v1beta/user_event.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/discoveryengine/v1beta/common.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa7\t\n\tUserEvent\x12\x17\n\nevent_type\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x0euser_pseudo_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12:\n\x06engine\x18\x13 \x01(\tB*\xfaA\'\n%discoveryengine.googleapis.com/Engine\x12A\n\ndata_store\x18\x14 \x01(\tB-\xfaA*\n(discoveryengine.googleapis.com/DataStore\x12.\n\nevent_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12@\n\tuser_info\x18\x04 \x01(\x0b2-.google.cloud.discoveryengine.v1beta.UserInfo\x12\x1b\n\x13direct_user_request\x18\x05 \x01(\x08\x12\x12\n\nsession_id\x18\x06 \x01(\t\x12@\n\tpage_info\x18\x07 \x01(\x0b2-.google.cloud.discoveryengine.v1beta.PageInfo\x12\x19\n\x11attribution_token\x18\x08 \x01(\t\x12\x0e\n\x06filter\x18\t \x01(\t\x12D\n\tdocuments\x18\n \x03(\x0b21.google.cloud.discoveryengine.v1beta.DocumentInfo\x12=\n\x05panel\x18\x0b \x01(\x0b2..google.cloud.discoveryengine.v1beta.PanelInfo\x12D\n\x0bsearch_info\x18\x0c \x01(\x0b2/.google.cloud.discoveryengine.v1beta.SearchInfo\x12L\n\x0fcompletion_info\x18\r \x01(\x0b23.google.cloud.discoveryengine.v1beta.CompletionInfo\x12N\n\x10transaction_info\x18\x0e \x01(\x0b24.google.cloud.discoveryengine.v1beta.TransactionInfo\x12\x0f\n\x07tag_ids\x18\x0f \x03(\t\x12\x15\n\rpromotion_ids\x18\x10 \x03(\t\x12R\n\nattributes\x18\x11 \x03(\x0b2>.google.cloud.discoveryengine.v1beta.UserEvent.AttributesEntry\x12B\n\nmedia_info\x18\x12 \x01(\x0b2..google.cloud.discoveryengine.v1beta.MediaInfo\x12C\n\x06panels\x18\x16 \x03(\x0b2..google.cloud.discoveryengine.v1beta.PanelInfoB\x03\xe0A\x01\x1ag\n\x0fAttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12C\n\x05value\x18\x02 \x01(\x0b24.google.cloud.discoveryengine.v1beta.CustomAttribute:\x028\x01"Y\n\x08PageInfo\x12\x13\n\x0bpageview_id\x18\x01 \x01(\t\x12\x15\n\rpage_category\x18\x02 \x01(\t\x12\x0b\n\x03uri\x18\x03 \x01(\t\x12\x14\n\x0creferrer_uri\x18\x04 \x01(\t"T\n\nSearchInfo\x12\x14\n\x0csearch_query\x18\x01 \x01(\t\x12\x10\n\x08order_by\x18\x02 \x01(\t\x12\x13\n\x06offset\x18\x03 \x01(\x05H\x00\x88\x01\x01B\t\n\x07_offset"H\n\x0eCompletionInfo\x12\x1b\n\x13selected_suggestion\x18\x01 \x01(\t\x12\x19\n\x11selected_position\x18\x02 \x01(\x05"\xc9\x01\n\x0fTransactionInfo\x12\x17\n\x05value\x18\x01 \x01(\x02B\x03\xe0A\x02H\x00\x88\x01\x01\x12\x15\n\x08currency\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x16\n\x0etransaction_id\x18\x03 \x01(\t\x12\x10\n\x03tax\x18\x04 \x01(\x02H\x01\x88\x01\x01\x12\x11\n\x04cost\x18\x05 \x01(\x02H\x02\x88\x01\x01\x12\x1b\n\x0ediscount_value\x18\x06 \x01(\x02H\x03\x88\x01\x01B\x08\n\x06_valueB\x06\n\x04_taxB\x07\n\x05_costB\x11\n\x0f_discount_value"\xd0\x01\n\x0cDocumentInfo\x12\x0c\n\x02id\x18\x01 \x01(\tH\x00\x12<\n\x04name\x18\x02 \x01(\tB,\xfaA)\n\'discoveryengine.googleapis.com/DocumentH\x00\x12\r\n\x03uri\x18\x06 \x01(\tH\x00\x12\x15\n\x08quantity\x18\x03 \x01(\x05H\x01\x88\x01\x01\x12\x15\n\rpromotion_ids\x18\x04 \x03(\t\x12\x13\n\x06joined\x18\x05 \x01(\x08B\x03\xe0A\x03B\x15\n\x13document_descriptorB\x0b\n\t_quantity"\xdf\x01\n\tPanelInfo\x12\x15\n\x08panel_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12\x1b\n\x0epanel_position\x18\x04 \x01(\x05H\x00\x88\x01\x01\x12\x19\n\x0ctotal_panels\x18\x05 \x01(\x05H\x01\x88\x01\x01\x12I\n\tdocuments\x18\x06 \x03(\x0b21.google.cloud.discoveryengine.v1beta.DocumentInfoB\x03\xe0A\x01B\x11\n\x0f_panel_positionB\x0f\n\r_total_panels"\x8d\x01\n\tMediaInfo\x12:\n\x17media_progress_duration\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12&\n\x19media_progress_percentage\x18\x02 \x01(\x02H\x00\x88\x01\x01B\x1c\n\x1a_media_progress_percentageB\x95\x02\n\'com.google.cloud.discoveryengine.v1betaB\x0eUserEventProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.user_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x0eUserEventProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
    _globals['_USEREVENT_ATTRIBUTESENTRY']._loaded_options = None
    _globals['_USEREVENT_ATTRIBUTESENTRY']._serialized_options = b'8\x01'
    _globals['_USEREVENT'].fields_by_name['event_type']._loaded_options = None
    _globals['_USEREVENT'].fields_by_name['event_type']._serialized_options = b'\xe0A\x02'
    _globals['_USEREVENT'].fields_by_name['user_pseudo_id']._loaded_options = None
    _globals['_USEREVENT'].fields_by_name['user_pseudo_id']._serialized_options = b'\xe0A\x02'
    _globals['_USEREVENT'].fields_by_name['engine']._loaded_options = None
    _globals['_USEREVENT'].fields_by_name['engine']._serialized_options = b"\xfaA'\n%discoveryengine.googleapis.com/Engine"
    _globals['_USEREVENT'].fields_by_name['data_store']._loaded_options = None
    _globals['_USEREVENT'].fields_by_name['data_store']._serialized_options = b'\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_USEREVENT'].fields_by_name['panels']._loaded_options = None
    _globals['_USEREVENT'].fields_by_name['panels']._serialized_options = b'\xe0A\x01'
    _globals['_TRANSACTIONINFO'].fields_by_name['value']._loaded_options = None
    _globals['_TRANSACTIONINFO'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_TRANSACTIONINFO'].fields_by_name['currency']._loaded_options = None
    _globals['_TRANSACTIONINFO'].fields_by_name['currency']._serialized_options = b'\xe0A\x02'
    _globals['_DOCUMENTINFO'].fields_by_name['name']._loaded_options = None
    _globals['_DOCUMENTINFO'].fields_by_name['name']._serialized_options = b"\xfaA)\n'discoveryengine.googleapis.com/Document"
    _globals['_DOCUMENTINFO'].fields_by_name['joined']._loaded_options = None
    _globals['_DOCUMENTINFO'].fields_by_name['joined']._serialized_options = b'\xe0A\x03'
    _globals['_PANELINFO'].fields_by_name['panel_id']._loaded_options = None
    _globals['_PANELINFO'].fields_by_name['panel_id']._serialized_options = b'\xe0A\x02'
    _globals['_PANELINFO'].fields_by_name['documents']._loaded_options = None
    _globals['_PANELINFO'].fields_by_name['documents']._serialized_options = b'\xe0A\x01'
    _globals['_USEREVENT']._serialized_start = 269
    _globals['_USEREVENT']._serialized_end = 1460
    _globals['_USEREVENT_ATTRIBUTESENTRY']._serialized_start = 1357
    _globals['_USEREVENT_ATTRIBUTESENTRY']._serialized_end = 1460
    _globals['_PAGEINFO']._serialized_start = 1462
    _globals['_PAGEINFO']._serialized_end = 1551
    _globals['_SEARCHINFO']._serialized_start = 1553
    _globals['_SEARCHINFO']._serialized_end = 1637
    _globals['_COMPLETIONINFO']._serialized_start = 1639
    _globals['_COMPLETIONINFO']._serialized_end = 1711
    _globals['_TRANSACTIONINFO']._serialized_start = 1714
    _globals['_TRANSACTIONINFO']._serialized_end = 1915
    _globals['_DOCUMENTINFO']._serialized_start = 1918
    _globals['_DOCUMENTINFO']._serialized_end = 2126
    _globals['_PANELINFO']._serialized_start = 2129
    _globals['_PANELINFO']._serialized_end = 2352
    _globals['_MEDIAINFO']._serialized_start = 2355
    _globals['_MEDIAINFO']._serialized_end = 2496