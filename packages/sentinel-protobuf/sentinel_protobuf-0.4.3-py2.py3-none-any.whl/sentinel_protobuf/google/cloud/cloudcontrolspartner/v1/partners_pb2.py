"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/cloudcontrolspartner/v1/partners.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/cloudcontrolspartner/v1/partners.proto\x12$google.cloud.cloudcontrolspartner.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbd\x03\n\x07Partner\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x127\n\x04skus\x18\x03 \x03(\x0b2).google.cloud.cloudcontrolspartner.v1.Sku\x12H\n\rekm_solutions\x18\x04 \x03(\x0b21.google.cloud.cloudcontrolspartner.v1.EkmMetadata\x12\x1e\n\x16operated_cloud_regions\x18\x05 \x03(\t\x12\x1a\n\x12partner_project_id\x18\x07 \x01(\t\x124\n\x0bcreate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:t\xeaAq\n+cloudcontrolspartner.googleapis.com/Partner\x129organizations/{organization}/locations/{location}/partner2\x07partner"V\n\x11GetPartnerRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudcontrolspartner.googleapis.com/Partner"\'\n\x03Sku\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t"\xe0\x01\n\x0bEkmMetadata\x12S\n\x0cekm_solution\x18\x01 \x01(\x0e2=.google.cloud.cloudcontrolspartner.v1.EkmMetadata.EkmSolution\x12\x18\n\x10ekm_endpoint_uri\x18\x02 \x01(\t"b\n\x0bEkmSolution\x12\x1c\n\x18EKM_SOLUTION_UNSPECIFIED\x10\x00\x12\x0c\n\x08FORTANIX\x10\x01\x12\x0b\n\x07FUTUREX\x10\x02\x12\n\n\x06THALES\x10\x03\x12\x0e\n\x06VIRTRU\x10\x04\x1a\x02\x08\x01B\x91\x02\n(com.google.cloud.cloudcontrolspartner.v1B\rPartnersProtoP\x01Z\\cloud.google.com/go/cloudcontrolspartner/apiv1/cloudcontrolspartnerpb;cloudcontrolspartnerpb\xaa\x02$Google.Cloud.CloudControlsPartner.V1\xca\x02$Google\\Cloud\\CloudControlsPartner\\V1\xea\x02\'Google::Cloud::CloudControlsPartner::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.cloudcontrolspartner.v1.partners_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.cloudcontrolspartner.v1B\rPartnersProtoP\x01Z\\cloud.google.com/go/cloudcontrolspartner/apiv1/cloudcontrolspartnerpb;cloudcontrolspartnerpb\xaa\x02$Google.Cloud.CloudControlsPartner.V1\xca\x02$Google\\Cloud\\CloudControlsPartner\\V1\xea\x02'Google::Cloud::CloudControlsPartner::V1"
    _globals['_PARTNER'].fields_by_name['name']._loaded_options = None
    _globals['_PARTNER'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_PARTNER'].fields_by_name['create_time']._loaded_options = None
    _globals['_PARTNER'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_PARTNER'].fields_by_name['update_time']._loaded_options = None
    _globals['_PARTNER'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_PARTNER']._loaded_options = None
    _globals['_PARTNER']._serialized_options = b'\xeaAq\n+cloudcontrolspartner.googleapis.com/Partner\x129organizations/{organization}/locations/{location}/partner2\x07partner'
    _globals['_GETPARTNERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPARTNERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudcontrolspartner.googleapis.com/Partner'
    _globals['_EKMMETADATA_EKMSOLUTION'].values_by_name['VIRTRU']._loaded_options = None
    _globals['_EKMMETADATA_EKMSOLUTION'].values_by_name['VIRTRU']._serialized_options = b'\x08\x01'
    _globals['_PARTNER']._serialized_start = 187
    _globals['_PARTNER']._serialized_end = 632
    _globals['_GETPARTNERREQUEST']._serialized_start = 634
    _globals['_GETPARTNERREQUEST']._serialized_end = 720
    _globals['_SKU']._serialized_start = 722
    _globals['_SKU']._serialized_end = 761
    _globals['_EKMMETADATA']._serialized_start = 764
    _globals['_EKMMETADATA']._serialized_end = 988
    _globals['_EKMMETADATA_EKMSOLUTION']._serialized_start = 890
    _globals['_EKMMETADATA_EKMSOLUTION']._serialized_end = 988