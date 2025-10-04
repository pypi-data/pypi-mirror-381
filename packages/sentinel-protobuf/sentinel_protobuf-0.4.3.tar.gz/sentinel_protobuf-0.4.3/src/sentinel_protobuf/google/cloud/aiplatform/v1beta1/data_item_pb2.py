"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/data_item.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/aiplatform/v1beta1/data_item.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf8\x03\n\x08DataItem\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12J\n\x06labels\x18\x03 \x03(\x0b25.google.cloud.aiplatform.v1beta1.DataItem.LabelsEntryB\x03\xe0A\x01\x12,\n\x07payload\x18\x04 \x01(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x02\x12\x11\n\x04etag\x18\x07 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rsatisfies_pzs\x18\n \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x0b \x01(\x08B\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:y\xeaAv\n"aiplatform.googleapis.com/DataItem\x12Pprojects/{project}/locations/{location}/datasets/{dataset}/dataItems/{data_item}B\xe4\x01\n#com.google.cloud.aiplatform.v1beta1B\rDataItemProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.data_item_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\rDataItemProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_DATAITEM_LABELSENTRY']._loaded_options = None
    _globals['_DATAITEM_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_DATAITEM'].fields_by_name['name']._loaded_options = None
    _globals['_DATAITEM'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_DATAITEM'].fields_by_name['create_time']._loaded_options = None
    _globals['_DATAITEM'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATAITEM'].fields_by_name['update_time']._loaded_options = None
    _globals['_DATAITEM'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATAITEM'].fields_by_name['labels']._loaded_options = None
    _globals['_DATAITEM'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_DATAITEM'].fields_by_name['payload']._loaded_options = None
    _globals['_DATAITEM'].fields_by_name['payload']._serialized_options = b'\xe0A\x02'
    _globals['_DATAITEM'].fields_by_name['etag']._loaded_options = None
    _globals['_DATAITEM'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_DATAITEM'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_DATAITEM'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_DATAITEM'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_DATAITEM'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_DATAITEM']._loaded_options = None
    _globals['_DATAITEM']._serialized_options = b'\xeaAv\n"aiplatform.googleapis.com/DataItem\x12Pprojects/{project}/locations/{location}/datasets/{dataset}/dataItems/{data_item}'
    _globals['_DATAITEM']._serialized_start = 208
    _globals['_DATAITEM']._serialized_end = 712
    _globals['_DATAITEM_LABELSENTRY']._serialized_start = 544
    _globals['_DATAITEM_LABELSENTRY']._serialized_end = 589