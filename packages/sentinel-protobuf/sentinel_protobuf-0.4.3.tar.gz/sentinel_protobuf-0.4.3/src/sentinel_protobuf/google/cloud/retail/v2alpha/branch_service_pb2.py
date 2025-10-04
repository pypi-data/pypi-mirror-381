"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2alpha/branch_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2alpha import branch_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_branch__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/retail/v2alpha/branch_service.proto\x12\x1bgoogle.cloud.retail.v2alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/retail/v2alpha/branch.proto"\x83\x01\n\x13ListBranchesRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x125\n\x04view\x18\x02 \x01(\x0e2\'.google.cloud.retail.v2alpha.BranchView"M\n\x14ListBranchesResponse\x125\n\x08branches\x18\x01 \x03(\x0b2#.google.cloud.retail.v2alpha.Branch"}\n\x10GetBranchRequest\x122\n\x04name\x18\x01 \x01(\tB$\xe0A\x02\xfaA\x1e\n\x1cretail.googleapis.com/Branch\x125\n\x04view\x18\x02 \x01(\x0e2\'.google.cloud.retail.v2alpha.BranchView2\xce\x03\n\rBranchService\x12\xc2\x01\n\x0cListBranches\x120.google.cloud.retail.v2alpha.ListBranchesRequest\x1a1.google.cloud.retail.v2alpha.ListBranchesResponse"M\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v2alpha/{parent=projects/*/locations/*/catalogs/*}/branches\x12\xac\x01\n\tGetBranch\x12-.google.cloud.retail.v2alpha.GetBranchRequest\x1a#.google.cloud.retail.v2alpha.Branch"K\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v2alpha/{name=projects/*/locations/*/catalogs/*/branches/*}\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd6\x01\n\x1fcom.google.cloud.retail.v2alphaB\x12BranchServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2alpha.branch_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.retail.v2alphaB\x12BranchServiceProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alpha'
    _globals['_LISTBRANCHESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTBRANCHESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_GETBRANCHREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETBRANCHREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1e\n\x1cretail.googleapis.com/Branch'
    _globals['_BRANCHSERVICE']._loaded_options = None
    _globals['_BRANCHSERVICE']._serialized_options = b'\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_BRANCHSERVICE'].methods_by_name['ListBranches']._loaded_options = None
    _globals['_BRANCHSERVICE'].methods_by_name['ListBranches']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v2alpha/{parent=projects/*/locations/*/catalogs/*}/branches'
    _globals['_BRANCHSERVICE'].methods_by_name['GetBranch']._loaded_options = None
    _globals['_BRANCHSERVICE'].methods_by_name['GetBranch']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v2alpha/{name=projects/*/locations/*/catalogs/*/branches/*}'
    _globals['_LISTBRANCHESREQUEST']._serialized_start = 239
    _globals['_LISTBRANCHESREQUEST']._serialized_end = 370
    _globals['_LISTBRANCHESRESPONSE']._serialized_start = 372
    _globals['_LISTBRANCHESRESPONSE']._serialized_end = 449
    _globals['_GETBRANCHREQUEST']._serialized_start = 451
    _globals['_GETBRANCHREQUEST']._serialized_end = 576
    _globals['_BRANCHSERVICE']._serialized_start = 579
    _globals['_BRANCHSERVICE']._serialized_end = 1041