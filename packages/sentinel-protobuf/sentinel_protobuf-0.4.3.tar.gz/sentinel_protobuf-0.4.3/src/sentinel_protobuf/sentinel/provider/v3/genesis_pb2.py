"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/provider/v3/genesis.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.provider.v2 import provider_pb2 as sentinel_dot_provider_dot_v2_dot_provider__pb2
from ....sentinel.provider.v3 import params_pb2 as sentinel_dot_provider_dot_v3_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"sentinel/provider/v3/genesis.proto\x12\x14sentinel.provider.v3\x1a\x14gogoproto/gogo.proto\x1a#sentinel/provider/v2/provider.proto\x1a!sentinel/provider/v3/params.proto"{\n\x0cGenesisState\x127\n\tproviders\x18\x01 \x03(\x0b2\x1e.sentinel.provider.v2.ProviderB\x04\xc8\xde\x1f\x00\x122\n\x06params\x18\x02 \x01(\x0b2\x1c.sentinel.provider.v3.ParamsB\x04\xc8\xde\x1f\x00BJZ@github.com/sentinel-official/sentinelhub/v12/x/provider/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.provider.v3.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z@github.com/sentinel-official/sentinelhub/v12/x/provider/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_GENESISSTATE'].fields_by_name['providers']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['providers']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE'].fields_by_name['params']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE']._serialized_start = 154
    _globals['_GENESISSTATE']._serialized_end = 277