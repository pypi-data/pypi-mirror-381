"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/networkservices/v1/common.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/networkservices/v1/common.proto\x12\x1fgoogle.cloud.networkservices.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x80\x02\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x03")\n\x13TrafficPortSelector\x12\x12\n\x05ports\x18\x01 \x03(\tB\x03\xe0A\x01"\xcc\x04\n\x0fEndpointMatcher\x12g\n\x16metadata_label_matcher\x18\x01 \x01(\x0b2E.google.cloud.networkservices.v1.EndpointMatcher.MetadataLabelMatcherH\x00\x1a\xbf\x03\n\x14MetadataLabelMatcher\x12\x87\x01\n\x1dmetadata_label_match_criteria\x18\x01 \x01(\x0e2`.google.cloud.networkservices.v1.EndpointMatcher.MetadataLabelMatcher.MetadataLabelMatchCriteria\x12m\n\x0fmetadata_labels\x18\x02 \x03(\x0b2T.google.cloud.networkservices.v1.EndpointMatcher.MetadataLabelMatcher.MetadataLabels\x1aC\n\x0eMetadataLabels\x12\x17\n\nlabel_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0blabel_value\x18\x02 \x01(\tB\x03\xe0A\x02"i\n\x1aMetadataLabelMatchCriteria\x12-\n)METADATA_LABEL_MATCH_CRITERIA_UNSPECIFIED\x10\x00\x12\r\n\tMATCH_ANY\x10\x01\x12\r\n\tMATCH_ALL\x10\x02B\x0e\n\x0cmatcher_type*J\n\x0cEnvoyHeaders\x12\x1d\n\x19ENVOY_HEADERS_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\x11\n\rDEBUG_HEADERS\x10\x02B\xec\x01\n#com.google.cloud.networkservices.v1B\x0bCommonProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networkservices.v1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.networkservices.v1B\x0bCommonProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_TRAFFICPORTSELECTOR'].fields_by_name['ports']._loaded_options = None
    _globals['_TRAFFICPORTSELECTOR'].fields_by_name['ports']._serialized_options = b'\xe0A\x01'
    _globals['_ENDPOINTMATCHER_METADATALABELMATCHER_METADATALABELS'].fields_by_name['label_name']._loaded_options = None
    _globals['_ENDPOINTMATCHER_METADATALABELMATCHER_METADATALABELS'].fields_by_name['label_name']._serialized_options = b'\xe0A\x02'
    _globals['_ENDPOINTMATCHER_METADATALABELMATCHER_METADATALABELS'].fields_by_name['label_value']._loaded_options = None
    _globals['_ENDPOINTMATCHER_METADATALABELMATCHER_METADATALABELS'].fields_by_name['label_value']._serialized_options = b'\xe0A\x02'
    _globals['_ENVOYHEADERS']._serialized_start = 1040
    _globals['_ENVOYHEADERS']._serialized_end = 1114
    _globals['_OPERATIONMETADATA']._serialized_start = 148
    _globals['_OPERATIONMETADATA']._serialized_end = 404
    _globals['_TRAFFICPORTSELECTOR']._serialized_start = 406
    _globals['_TRAFFICPORTSELECTOR']._serialized_end = 447
    _globals['_ENDPOINTMATCHER']._serialized_start = 450
    _globals['_ENDPOINTMATCHER']._serialized_end = 1038
    _globals['_ENDPOINTMATCHER_METADATALABELMATCHER']._serialized_start = 575
    _globals['_ENDPOINTMATCHER_METADATALABELMATCHER']._serialized_end = 1022
    _globals['_ENDPOINTMATCHER_METADATALABELMATCHER_METADATALABELS']._serialized_start = 848
    _globals['_ENDPOINTMATCHER_METADATALABELMATCHER_METADATALABELS']._serialized_end = 915
    _globals['_ENDPOINTMATCHER_METADATALABELMATCHER_METADATALABELMATCHCRITERIA']._serialized_start = 917
    _globals['_ENDPOINTMATCHER_METADATALABELMATCHER_METADATALABELMATCHCRITERIA']._serialized_end = 1022