"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/networkservices/v1/service_binding.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/networkservices/v1/service_binding.proto\x12\x1fgoogle.cloud.networkservices.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x88\x04\n\x0eServiceBinding\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12B\n\x07service\x18\x05 \x01(\tB1\x18\x01\xe0A\x01\xfaA)\n\'servicedirectory.googleapis.com/Service\x12\x19\n\nservice_id\x18\x08 \x01(\tB\x05\x18\x01\xe0A\x03\x12P\n\x06labels\x18\x07 \x03(\x0b2;.google.cloud.networkservices.v1.ServiceBinding.LabelsEntryB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:}\xeaAz\n-networkservices.googleapis.com/ServiceBinding\x12Iprojects/{project}/locations/{location}/serviceBindings/{service_binding}"\x8a\x01\n\x1aListServiceBindingsRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-networkservices.googleapis.com/ServiceBinding\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x96\x01\n\x1bListServiceBindingsResponse\x12I\n\x10service_bindings\x18\x01 \x03(\x0b2/.google.cloud.networkservices.v1.ServiceBinding\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"_\n\x18GetServiceBindingRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-networkservices.googleapis.com/ServiceBinding"\xd4\x01\n\x1bCreateServiceBindingRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-networkservices.googleapis.com/ServiceBinding\x12\x1f\n\x12service_binding_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12M\n\x0fservice_binding\x18\x03 \x01(\x0b2/.google.cloud.networkservices.v1.ServiceBindingB\x03\xe0A\x02"\xa2\x01\n\x1bUpdateServiceBindingRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12M\n\x0fservice_binding\x18\x02 \x01(\x0b2/.google.cloud.networkservices.v1.ServiceBindingB\x03\xe0A\x02"b\n\x1bDeleteServiceBindingRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-networkservices.googleapis.com/ServiceBindingB\xf3\x02\n#com.google.cloud.networkservices.v1B\x13ServiceBindingProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1\xeaA|\n\'servicedirectory.googleapis.com/Service\x12Qprojects/{project}/locations/{location}/namespaces/{namespace}/services/{service}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networkservices.v1.service_binding_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.networkservices.v1B\x13ServiceBindingProtoP\x01ZMcloud.google.com/go/networkservices/apiv1/networkservicespb;networkservicespb\xaa\x02\x1fGoogle.Cloud.NetworkServices.V1\xca\x02\x1fGoogle\\Cloud\\NetworkServices\\V1\xea\x02"Google::Cloud::NetworkServices::V1\xeaA|\n\'servicedirectory.googleapis.com/Service\x12Qprojects/{project}/locations/{location}/namespaces/{namespace}/services/{service}'
    _globals['_SERVICEBINDING_LABELSENTRY']._loaded_options = None
    _globals['_SERVICEBINDING_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_SERVICEBINDING'].fields_by_name['name']._loaded_options = None
    _globals['_SERVICEBINDING'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_SERVICEBINDING'].fields_by_name['description']._loaded_options = None
    _globals['_SERVICEBINDING'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_SERVICEBINDING'].fields_by_name['create_time']._loaded_options = None
    _globals['_SERVICEBINDING'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SERVICEBINDING'].fields_by_name['update_time']._loaded_options = None
    _globals['_SERVICEBINDING'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_SERVICEBINDING'].fields_by_name['service']._loaded_options = None
    _globals['_SERVICEBINDING'].fields_by_name['service']._serialized_options = b"\x18\x01\xe0A\x01\xfaA)\n'servicedirectory.googleapis.com/Service"
    _globals['_SERVICEBINDING'].fields_by_name['service_id']._loaded_options = None
    _globals['_SERVICEBINDING'].fields_by_name['service_id']._serialized_options = b'\x18\x01\xe0A\x03'
    _globals['_SERVICEBINDING'].fields_by_name['labels']._loaded_options = None
    _globals['_SERVICEBINDING'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_SERVICEBINDING']._loaded_options = None
    _globals['_SERVICEBINDING']._serialized_options = b'\xeaAz\n-networkservices.googleapis.com/ServiceBinding\x12Iprojects/{project}/locations/{location}/serviceBindings/{service_binding}'
    _globals['_LISTSERVICEBINDINGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSERVICEBINDINGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-networkservices.googleapis.com/ServiceBinding'
    _globals['_GETSERVICEBINDINGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSERVICEBINDINGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-networkservices.googleapis.com/ServiceBinding'
    _globals['_CREATESERVICEBINDINGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESERVICEBINDINGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-networkservices.googleapis.com/ServiceBinding'
    _globals['_CREATESERVICEBINDINGREQUEST'].fields_by_name['service_binding_id']._loaded_options = None
    _globals['_CREATESERVICEBINDINGREQUEST'].fields_by_name['service_binding_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESERVICEBINDINGREQUEST'].fields_by_name['service_binding']._loaded_options = None
    _globals['_CREATESERVICEBINDINGREQUEST'].fields_by_name['service_binding']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESERVICEBINDINGREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESERVICEBINDINGREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATESERVICEBINDINGREQUEST'].fields_by_name['service_binding']._loaded_options = None
    _globals['_UPDATESERVICEBINDINGREQUEST'].fields_by_name['service_binding']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESERVICEBINDINGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESERVICEBINDINGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-networkservices.googleapis.com/ServiceBinding'
    _globals['_SERVICEBINDING']._serialized_start = 218
    _globals['_SERVICEBINDING']._serialized_end = 738
    _globals['_SERVICEBINDING_LABELSENTRY']._serialized_start = 566
    _globals['_SERVICEBINDING_LABELSENTRY']._serialized_end = 611
    _globals['_LISTSERVICEBINDINGSREQUEST']._serialized_start = 741
    _globals['_LISTSERVICEBINDINGSREQUEST']._serialized_end = 879
    _globals['_LISTSERVICEBINDINGSRESPONSE']._serialized_start = 882
    _globals['_LISTSERVICEBINDINGSRESPONSE']._serialized_end = 1032
    _globals['_GETSERVICEBINDINGREQUEST']._serialized_start = 1034
    _globals['_GETSERVICEBINDINGREQUEST']._serialized_end = 1129
    _globals['_CREATESERVICEBINDINGREQUEST']._serialized_start = 1132
    _globals['_CREATESERVICEBINDINGREQUEST']._serialized_end = 1344
    _globals['_UPDATESERVICEBINDINGREQUEST']._serialized_start = 1347
    _globals['_UPDATESERVICEBINDINGREQUEST']._serialized_end = 1509
    _globals['_DELETESERVICEBINDINGREQUEST']._serialized_start = 1511
    _globals['_DELETESERVICEBINDINGREQUEST']._serialized_end = 1609