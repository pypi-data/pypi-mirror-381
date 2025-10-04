"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/asset/v1p5beta1/assets.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.orgpolicy.v1 import orgpolicy_pb2 as google_dot_cloud_dot_orgpolicy_dot_v1_dot_orgpolicy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from .....google.identity.accesscontextmanager.v1 import access_level_pb2 as google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__level__pb2
from .....google.identity.accesscontextmanager.v1 import access_policy_pb2 as google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__policy__pb2
from .....google.identity.accesscontextmanager.v1 import service_perimeter_pb2 as google_dot_identity_dot_accesscontextmanager_dot_v1_dot_service__perimeter__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/asset/v1p5beta1/assets.proto\x12\x1cgoogle.cloud.asset.v1p5beta1\x1a\x19google/api/resource.proto\x1a)google/cloud/orgpolicy/v1/orgpolicy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a:google/identity/accesscontextmanager/v1/access_level.proto\x1a;google/identity/accesscontextmanager/v1/access_policy.proto\x1a?google/identity/accesscontextmanager/v1/service_perimeter.proto\x1a\x1cgoogle/protobuf/struct.proto"\x90\x04\n\x05Asset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nasset_type\x18\x02 \x01(\t\x128\n\x08resource\x18\x03 \x01(\x0b2&.google.cloud.asset.v1p5beta1.Resource\x12)\n\niam_policy\x18\x04 \x01(\x0b2\x15.google.iam.v1.Policy\x125\n\norg_policy\x18\x06 \x03(\x0b2!.google.cloud.orgpolicy.v1.Policy\x12N\n\raccess_policy\x18\x07 \x01(\x0b25.google.identity.accesscontextmanager.v1.AccessPolicyH\x00\x12L\n\x0caccess_level\x18\x08 \x01(\x0b24.google.identity.accesscontextmanager.v1.AccessLevelH\x00\x12V\n\x11service_perimeter\x18\t \x01(\x0b29.google.identity.accesscontextmanager.v1.ServicePerimeterH\x00\x12\x11\n\tancestors\x18\n \x03(\t:\'\xeaA$\n\x1fcloudasset.googleapis.com/Asset\x12\x01*B\x17\n\x15access_context_policy"\xa0\x01\n\x08Resource\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x1e\n\x16discovery_document_uri\x18\x02 \x01(\t\x12\x16\n\x0ediscovery_name\x18\x03 \x01(\t\x12\x14\n\x0cresource_url\x18\x04 \x01(\t\x12\x0e\n\x06parent\x18\x05 \x01(\t\x12%\n\x04data\x18\x06 \x01(\x0b2\x17.google.protobuf.StructB\xa6\x01\n com.google.cloud.asset.v1p5beta1B\nAssetProtoP\x01Z6cloud.google.com/go/asset/apiv1p5beta1/assetpb;assetpb\xaa\x02\x1cGoogle.Cloud.Asset.V1p5Beta1\xca\x02\x1cGoogle\\Cloud\\Asset\\V1p5beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.asset.v1p5beta1.assets_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.asset.v1p5beta1B\nAssetProtoP\x01Z6cloud.google.com/go/asset/apiv1p5beta1/assetpb;assetpb\xaa\x02\x1cGoogle.Cloud.Asset.V1p5Beta1\xca\x02\x1cGoogle\\Cloud\\Asset\\V1p5beta1'
    _globals['_ASSET']._loaded_options = None
    _globals['_ASSET']._serialized_options = b'\xeaA$\n\x1fcloudasset.googleapis.com/Asset\x12\x01*'
    _globals['_ASSET']._serialized_start = 390
    _globals['_ASSET']._serialized_end = 918
    _globals['_RESOURCE']._serialized_start = 921
    _globals['_RESOURCE']._serialized_end = 1081