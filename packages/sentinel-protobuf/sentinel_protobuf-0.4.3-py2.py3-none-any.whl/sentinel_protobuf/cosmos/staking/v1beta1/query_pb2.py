"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'cosmos/staking/v1beta1/query.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....cosmos.staking.v1beta1 import staking_pb2 as cosmos_dot_staking_dot_v1beta1_dot_staking__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.query.v1 import query_pb2 as cosmos_dot_query_dot_v1_dot_query__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"cosmos/staking/v1beta1/query.proto\x12\x16cosmos.staking.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a$cosmos/staking/v1beta1/staking.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1bcosmos/query/v1/query.proto\x1a\x11amino/amino.proto"d\n\x16QueryValidatorsRequest\x12\x0e\n\x06status\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x98\x01\n\x17QueryValidatorsResponse\x12@\n\nvalidators\x18\x01 \x03(\x0b2!.cosmos.staking.v1beta1.ValidatorB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"I\n\x15QueryValidatorRequest\x120\n\x0evalidator_addr\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString"Y\n\x16QueryValidatorResponse\x12?\n\tvalidator\x18\x01 \x01(\x0b2!.cosmos.staking.v1beta1.ValidatorB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01"\x90\x01\n QueryValidatorDelegationsRequest\x120\n\x0evalidator_addr\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xcc\x01\n!QueryValidatorDelegationsResponse\x12j\n\x14delegation_responses\x18\x01 \x03(\x0b2*.cosmos.staking.v1beta1.DelegationResponseB \xc8\xde\x1f\x00\xaa\xdf\x1f\x13DelegationResponses\xa8\xe7\xb0*\x01\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x99\x01\n)QueryValidatorUnbondingDelegationsRequest\x120\n\x0evalidator_addr\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\xbe\x01\n*QueryValidatorUnbondingDelegationsResponse\x12S\n\x13unbonding_responses\x18\x01 \x03(\x0b2+.cosmos.staking.v1beta1.UnbondingDelegationB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x86\x01\n\x16QueryDelegationRequest\x120\n\x0edelegator_addr\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x120\n\x0evalidator_addr\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"b\n\x17QueryDelegationResponse\x12G\n\x13delegation_response\x18\x01 \x01(\x0b2*.cosmos.staking.v1beta1.DelegationResponse"\x8f\x01\n\x1fQueryUnbondingDelegationRequest\x120\n\x0edelegator_addr\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x120\n\x0evalidator_addr\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"j\n QueryUnbondingDelegationResponse\x12F\n\x06unbond\x18\x01 \x01(\x0b2+.cosmos.staking.v1beta1.UnbondingDelegationB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01"\x9a\x01\n QueryDelegatorDelegationsRequest\x120\n\x0edelegator_addr\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xb5\x01\n!QueryDelegatorDelegationsResponse\x12S\n\x14delegation_responses\x18\x01 \x03(\x0b2*.cosmos.staking.v1beta1.DelegationResponseB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\xa3\x01\n)QueryDelegatorUnbondingDelegationsRequest\x120\n\x0edelegator_addr\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xbe\x01\n*QueryDelegatorUnbondingDelegationsResponse\x12S\n\x13unbonding_responses\x18\x01 \x03(\x0b2+.cosmos.staking.v1beta1.UnbondingDelegationB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\xff\x01\n\x19QueryRedelegationsRequest\x120\n\x0edelegator_addr\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x124\n\x12src_validator_addr\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x124\n\x12dst_validator_addr\x18\x03 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\npagination\x18\x04 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xb2\x01\n\x1aQueryRedelegationsResponse\x12W\n\x16redelegation_responses\x18\x01 \x03(\x0b2,.cosmos.staking.v1beta1.RedelegationResponseB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x99\x01\n\x1fQueryDelegatorValidatorsRequest\x120\n\x0edelegator_addr\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\xa1\x01\n QueryDelegatorValidatorsResponse\x12@\n\nvalidators\x18\x01 \x03(\x0b2!.cosmos.staking.v1beta1.ValidatorB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\x8e\x01\n\x1eQueryDelegatorValidatorRequest\x120\n\x0edelegator_addr\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x120\n\x0evalidator_addr\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"b\n\x1fQueryDelegatorValidatorResponse\x12?\n\tvalidator\x18\x01 \x01(\x0b2!.cosmos.staking.v1beta1.ValidatorB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01",\n\x1aQueryHistoricalInfoRequest\x12\x0e\n\x06height\x18\x01 \x01(\x03"S\n\x1bQueryHistoricalInfoResponse\x124\n\x04hist\x18\x01 \x01(\x0b2&.cosmos.staking.v1beta1.HistoricalInfo"\x12\n\x10QueryPoolRequest"J\n\x11QueryPoolResponse\x125\n\x04pool\x18\x01 \x01(\x0b2\x1c.cosmos.staking.v1beta1.PoolB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01"\x14\n\x12QueryParamsRequest"P\n\x13QueryParamsResponse\x129\n\x06params\x18\x01 \x01(\x0b2\x1e.cosmos.staking.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x012\xb0\x16\n\x05Query\x12\x9e\x01\n\nValidators\x12..cosmos.staking.v1beta1.QueryValidatorsRequest\x1a/.cosmos.staking.v1beta1.QueryValidatorsResponse"/\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02$\x12"/cosmos/staking/v1beta1/validators\x12\xac\x01\n\tValidator\x12-.cosmos.staking.v1beta1.QueryValidatorRequest\x1a..cosmos.staking.v1beta1.QueryValidatorResponse"@\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x025\x123/cosmos/staking/v1beta1/validators/{validator_addr}\x12\xd9\x01\n\x14ValidatorDelegations\x128.cosmos.staking.v1beta1.QueryValidatorDelegationsRequest\x1a9.cosmos.staking.v1beta1.QueryValidatorDelegationsResponse"L\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02A\x12?/cosmos/staking/v1beta1/validators/{validator_addr}/delegations\x12\xfe\x01\n\x1dValidatorUnbondingDelegations\x12A.cosmos.staking.v1beta1.QueryValidatorUnbondingDelegationsRequest\x1aB.cosmos.staking.v1beta1.QueryValidatorUnbondingDelegationsResponse"V\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02K\x12I/cosmos/staking/v1beta1/validators/{validator_addr}/unbonding_delegations\x12\xcc\x01\n\nDelegation\x12..cosmos.staking.v1beta1.QueryDelegationRequest\x1a/.cosmos.staking.v1beta1.QueryDelegationResponse"]\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02R\x12P/cosmos/staking/v1beta1/validators/{validator_addr}/delegations/{delegator_addr}\x12\xfc\x01\n\x13UnbondingDelegation\x127.cosmos.staking.v1beta1.QueryUnbondingDelegationRequest\x1a8.cosmos.staking.v1beta1.QueryUnbondingDelegationResponse"r\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02g\x12e/cosmos/staking/v1beta1/validators/{validator_addr}/delegations/{delegator_addr}/unbonding_delegation\x12\xce\x01\n\x14DelegatorDelegations\x128.cosmos.staking.v1beta1.QueryDelegatorDelegationsRequest\x1a9.cosmos.staking.v1beta1.QueryDelegatorDelegationsResponse"A\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x026\x124/cosmos/staking/v1beta1/delegations/{delegator_addr}\x12\xfe\x01\n\x1dDelegatorUnbondingDelegations\x12A.cosmos.staking.v1beta1.QueryDelegatorUnbondingDelegationsRequest\x1aB.cosmos.staking.v1beta1.QueryDelegatorUnbondingDelegationsResponse"V\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02K\x12I/cosmos/staking/v1beta1/delegators/{delegator_addr}/unbonding_delegations\x12\xc6\x01\n\rRedelegations\x121.cosmos.staking.v1beta1.QueryRedelegationsRequest\x1a2.cosmos.staking.v1beta1.QueryRedelegationsResponse"N\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02C\x12A/cosmos/staking/v1beta1/delegators/{delegator_addr}/redelegations\x12\xd5\x01\n\x13DelegatorValidators\x127.cosmos.staking.v1beta1.QueryDelegatorValidatorsRequest\x1a8.cosmos.staking.v1beta1.QueryDelegatorValidatorsResponse"K\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02@\x12>/cosmos/staking/v1beta1/delegators/{delegator_addr}/validators\x12\xe3\x01\n\x12DelegatorValidator\x126.cosmos.staking.v1beta1.QueryDelegatorValidatorRequest\x1a7.cosmos.staking.v1beta1.QueryDelegatorValidatorResponse"\\\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02Q\x12O/cosmos/staking/v1beta1/delegators/{delegator_addr}/validators/{validator_addr}\x12\xb8\x01\n\x0eHistoricalInfo\x122.cosmos.staking.v1beta1.QueryHistoricalInfoRequest\x1a3.cosmos.staking.v1beta1.QueryHistoricalInfoResponse"=\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x022\x120/cosmos/staking/v1beta1/historical_info/{height}\x12\x86\x01\n\x04Pool\x12(.cosmos.staking.v1beta1.QueryPoolRequest\x1a).cosmos.staking.v1beta1.QueryPoolResponse")\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\x1e\x12\x1c/cosmos/staking/v1beta1/pool\x12\x8e\x01\n\x06Params\x12*.cosmos.staking.v1beta1.QueryParamsRequest\x1a+.cosmos.staking.v1beta1.QueryParamsResponse"+\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02 \x12\x1e/cosmos/staking/v1beta1/paramsB.Z,github.com/cosmos/cosmos-sdk/x/staking/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.staking.v1beta1.query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/staking/types'
    _globals['_QUERYVALIDATORSRESPONSE'].fields_by_name['validators']._loaded_options = None
    _globals['_QUERYVALIDATORSRESPONSE'].fields_by_name['validators']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_QUERYVALIDATORREQUEST'].fields_by_name['validator_addr']._loaded_options = None
    _globals['_QUERYVALIDATORREQUEST'].fields_by_name['validator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_QUERYVALIDATORRESPONSE'].fields_by_name['validator']._loaded_options = None
    _globals['_QUERYVALIDATORRESPONSE'].fields_by_name['validator']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_QUERYVALIDATORDELEGATIONSREQUEST'].fields_by_name['validator_addr']._loaded_options = None
    _globals['_QUERYVALIDATORDELEGATIONSREQUEST'].fields_by_name['validator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_QUERYVALIDATORDELEGATIONSRESPONSE'].fields_by_name['delegation_responses']._loaded_options = None
    _globals['_QUERYVALIDATORDELEGATIONSRESPONSE'].fields_by_name['delegation_responses']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f\x13DelegationResponses\xa8\xe7\xb0*\x01'
    _globals['_QUERYVALIDATORUNBONDINGDELEGATIONSREQUEST'].fields_by_name['validator_addr']._loaded_options = None
    _globals['_QUERYVALIDATORUNBONDINGDELEGATIONSREQUEST'].fields_by_name['validator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_QUERYVALIDATORUNBONDINGDELEGATIONSRESPONSE'].fields_by_name['unbonding_responses']._loaded_options = None
    _globals['_QUERYVALIDATORUNBONDINGDELEGATIONSRESPONSE'].fields_by_name['unbonding_responses']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_QUERYDELEGATIONREQUEST'].fields_by_name['delegator_addr']._loaded_options = None
    _globals['_QUERYDELEGATIONREQUEST'].fields_by_name['delegator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_QUERYDELEGATIONREQUEST'].fields_by_name['validator_addr']._loaded_options = None
    _globals['_QUERYDELEGATIONREQUEST'].fields_by_name['validator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_QUERYDELEGATIONREQUEST']._loaded_options = None
    _globals['_QUERYDELEGATIONREQUEST']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_QUERYUNBONDINGDELEGATIONREQUEST'].fields_by_name['delegator_addr']._loaded_options = None
    _globals['_QUERYUNBONDINGDELEGATIONREQUEST'].fields_by_name['delegator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_QUERYUNBONDINGDELEGATIONREQUEST'].fields_by_name['validator_addr']._loaded_options = None
    _globals['_QUERYUNBONDINGDELEGATIONREQUEST'].fields_by_name['validator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_QUERYUNBONDINGDELEGATIONREQUEST']._loaded_options = None
    _globals['_QUERYUNBONDINGDELEGATIONREQUEST']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_QUERYUNBONDINGDELEGATIONRESPONSE'].fields_by_name['unbond']._loaded_options = None
    _globals['_QUERYUNBONDINGDELEGATIONRESPONSE'].fields_by_name['unbond']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_QUERYDELEGATORDELEGATIONSREQUEST'].fields_by_name['delegator_addr']._loaded_options = None
    _globals['_QUERYDELEGATORDELEGATIONSREQUEST'].fields_by_name['delegator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_QUERYDELEGATORDELEGATIONSREQUEST']._loaded_options = None
    _globals['_QUERYDELEGATORDELEGATIONSREQUEST']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_QUERYDELEGATORDELEGATIONSRESPONSE'].fields_by_name['delegation_responses']._loaded_options = None
    _globals['_QUERYDELEGATORDELEGATIONSRESPONSE'].fields_by_name['delegation_responses']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_QUERYDELEGATORUNBONDINGDELEGATIONSREQUEST'].fields_by_name['delegator_addr']._loaded_options = None
    _globals['_QUERYDELEGATORUNBONDINGDELEGATIONSREQUEST'].fields_by_name['delegator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_QUERYDELEGATORUNBONDINGDELEGATIONSREQUEST']._loaded_options = None
    _globals['_QUERYDELEGATORUNBONDINGDELEGATIONSREQUEST']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_QUERYDELEGATORUNBONDINGDELEGATIONSRESPONSE'].fields_by_name['unbonding_responses']._loaded_options = None
    _globals['_QUERYDELEGATORUNBONDINGDELEGATIONSRESPONSE'].fields_by_name['unbonding_responses']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_QUERYREDELEGATIONSREQUEST'].fields_by_name['delegator_addr']._loaded_options = None
    _globals['_QUERYREDELEGATIONSREQUEST'].fields_by_name['delegator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_QUERYREDELEGATIONSREQUEST'].fields_by_name['src_validator_addr']._loaded_options = None
    _globals['_QUERYREDELEGATIONSREQUEST'].fields_by_name['src_validator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_QUERYREDELEGATIONSREQUEST'].fields_by_name['dst_validator_addr']._loaded_options = None
    _globals['_QUERYREDELEGATIONSREQUEST'].fields_by_name['dst_validator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_QUERYREDELEGATIONSREQUEST']._loaded_options = None
    _globals['_QUERYREDELEGATIONSREQUEST']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_QUERYREDELEGATIONSRESPONSE'].fields_by_name['redelegation_responses']._loaded_options = None
    _globals['_QUERYREDELEGATIONSRESPONSE'].fields_by_name['redelegation_responses']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_QUERYDELEGATORVALIDATORSREQUEST'].fields_by_name['delegator_addr']._loaded_options = None
    _globals['_QUERYDELEGATORVALIDATORSREQUEST'].fields_by_name['delegator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_QUERYDELEGATORVALIDATORSREQUEST']._loaded_options = None
    _globals['_QUERYDELEGATORVALIDATORSREQUEST']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_QUERYDELEGATORVALIDATORSRESPONSE'].fields_by_name['validators']._loaded_options = None
    _globals['_QUERYDELEGATORVALIDATORSRESPONSE'].fields_by_name['validators']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_QUERYDELEGATORVALIDATORREQUEST'].fields_by_name['delegator_addr']._loaded_options = None
    _globals['_QUERYDELEGATORVALIDATORREQUEST'].fields_by_name['delegator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_QUERYDELEGATORVALIDATORREQUEST'].fields_by_name['validator_addr']._loaded_options = None
    _globals['_QUERYDELEGATORVALIDATORREQUEST'].fields_by_name['validator_addr']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_QUERYDELEGATORVALIDATORREQUEST']._loaded_options = None
    _globals['_QUERYDELEGATORVALIDATORREQUEST']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_QUERYDELEGATORVALIDATORRESPONSE'].fields_by_name['validator']._loaded_options = None
    _globals['_QUERYDELEGATORVALIDATORRESPONSE'].fields_by_name['validator']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_QUERYPOOLRESPONSE'].fields_by_name['pool']._loaded_options = None
    _globals['_QUERYPOOLRESPONSE'].fields_by_name['pool']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._loaded_options = None
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_QUERY'].methods_by_name['Validators']._loaded_options = None
    _globals['_QUERY'].methods_by_name['Validators']._serialized_options = b'\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02$\x12"/cosmos/staking/v1beta1/validators'
    _globals['_QUERY'].methods_by_name['Validator']._loaded_options = None
    _globals['_QUERY'].methods_by_name['Validator']._serialized_options = b'\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x025\x123/cosmos/staking/v1beta1/validators/{validator_addr}'
    _globals['_QUERY'].methods_by_name['ValidatorDelegations']._loaded_options = None
    _globals['_QUERY'].methods_by_name['ValidatorDelegations']._serialized_options = b'\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02A\x12?/cosmos/staking/v1beta1/validators/{validator_addr}/delegations'
    _globals['_QUERY'].methods_by_name['ValidatorUnbondingDelegations']._loaded_options = None
    _globals['_QUERY'].methods_by_name['ValidatorUnbondingDelegations']._serialized_options = b'\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02K\x12I/cosmos/staking/v1beta1/validators/{validator_addr}/unbonding_delegations'
    _globals['_QUERY'].methods_by_name['Delegation']._loaded_options = None
    _globals['_QUERY'].methods_by_name['Delegation']._serialized_options = b'\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02R\x12P/cosmos/staking/v1beta1/validators/{validator_addr}/delegations/{delegator_addr}'
    _globals['_QUERY'].methods_by_name['UnbondingDelegation']._loaded_options = None
    _globals['_QUERY'].methods_by_name['UnbondingDelegation']._serialized_options = b'\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02g\x12e/cosmos/staking/v1beta1/validators/{validator_addr}/delegations/{delegator_addr}/unbonding_delegation'
    _globals['_QUERY'].methods_by_name['DelegatorDelegations']._loaded_options = None
    _globals['_QUERY'].methods_by_name['DelegatorDelegations']._serialized_options = b'\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x026\x124/cosmos/staking/v1beta1/delegations/{delegator_addr}'
    _globals['_QUERY'].methods_by_name['DelegatorUnbondingDelegations']._loaded_options = None
    _globals['_QUERY'].methods_by_name['DelegatorUnbondingDelegations']._serialized_options = b'\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02K\x12I/cosmos/staking/v1beta1/delegators/{delegator_addr}/unbonding_delegations'
    _globals['_QUERY'].methods_by_name['Redelegations']._loaded_options = None
    _globals['_QUERY'].methods_by_name['Redelegations']._serialized_options = b'\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02C\x12A/cosmos/staking/v1beta1/delegators/{delegator_addr}/redelegations'
    _globals['_QUERY'].methods_by_name['DelegatorValidators']._loaded_options = None
    _globals['_QUERY'].methods_by_name['DelegatorValidators']._serialized_options = b'\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02@\x12>/cosmos/staking/v1beta1/delegators/{delegator_addr}/validators'
    _globals['_QUERY'].methods_by_name['DelegatorValidator']._loaded_options = None
    _globals['_QUERY'].methods_by_name['DelegatorValidator']._serialized_options = b'\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02Q\x12O/cosmos/staking/v1beta1/delegators/{delegator_addr}/validators/{validator_addr}'
    _globals['_QUERY'].methods_by_name['HistoricalInfo']._loaded_options = None
    _globals['_QUERY'].methods_by_name['HistoricalInfo']._serialized_options = b'\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x022\x120/cosmos/staking/v1beta1/historical_info/{height}'
    _globals['_QUERY'].methods_by_name['Pool']._loaded_options = None
    _globals['_QUERY'].methods_by_name['Pool']._serialized_options = b'\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02\x1e\x12\x1c/cosmos/staking/v1beta1/pool'
    _globals['_QUERY'].methods_by_name['Params']._loaded_options = None
    _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\x88\xe7\xb0*\x01\x82\xd3\xe4\x93\x02 \x12\x1e/cosmos/staking/v1beta1/params'
    _globals['_QUERYVALIDATORSREQUEST']._serialized_start = 271
    _globals['_QUERYVALIDATORSREQUEST']._serialized_end = 371
    _globals['_QUERYVALIDATORSRESPONSE']._serialized_start = 374
    _globals['_QUERYVALIDATORSRESPONSE']._serialized_end = 526
    _globals['_QUERYVALIDATORREQUEST']._serialized_start = 528
    _globals['_QUERYVALIDATORREQUEST']._serialized_end = 601
    _globals['_QUERYVALIDATORRESPONSE']._serialized_start = 603
    _globals['_QUERYVALIDATORRESPONSE']._serialized_end = 692
    _globals['_QUERYVALIDATORDELEGATIONSREQUEST']._serialized_start = 695
    _globals['_QUERYVALIDATORDELEGATIONSREQUEST']._serialized_end = 839
    _globals['_QUERYVALIDATORDELEGATIONSRESPONSE']._serialized_start = 842
    _globals['_QUERYVALIDATORDELEGATIONSRESPONSE']._serialized_end = 1046
    _globals['_QUERYVALIDATORUNBONDINGDELEGATIONSREQUEST']._serialized_start = 1049
    _globals['_QUERYVALIDATORUNBONDINGDELEGATIONSREQUEST']._serialized_end = 1202
    _globals['_QUERYVALIDATORUNBONDINGDELEGATIONSRESPONSE']._serialized_start = 1205
    _globals['_QUERYVALIDATORUNBONDINGDELEGATIONSRESPONSE']._serialized_end = 1395
    _globals['_QUERYDELEGATIONREQUEST']._serialized_start = 1398
    _globals['_QUERYDELEGATIONREQUEST']._serialized_end = 1532
    _globals['_QUERYDELEGATIONRESPONSE']._serialized_start = 1534
    _globals['_QUERYDELEGATIONRESPONSE']._serialized_end = 1632
    _globals['_QUERYUNBONDINGDELEGATIONREQUEST']._serialized_start = 1635
    _globals['_QUERYUNBONDINGDELEGATIONREQUEST']._serialized_end = 1778
    _globals['_QUERYUNBONDINGDELEGATIONRESPONSE']._serialized_start = 1780
    _globals['_QUERYUNBONDINGDELEGATIONRESPONSE']._serialized_end = 1886
    _globals['_QUERYDELEGATORDELEGATIONSREQUEST']._serialized_start = 1889
    _globals['_QUERYDELEGATORDELEGATIONSREQUEST']._serialized_end = 2043
    _globals['_QUERYDELEGATORDELEGATIONSRESPONSE']._serialized_start = 2046
    _globals['_QUERYDELEGATORDELEGATIONSRESPONSE']._serialized_end = 2227
    _globals['_QUERYDELEGATORUNBONDINGDELEGATIONSREQUEST']._serialized_start = 2230
    _globals['_QUERYDELEGATORUNBONDINGDELEGATIONSREQUEST']._serialized_end = 2393
    _globals['_QUERYDELEGATORUNBONDINGDELEGATIONSRESPONSE']._serialized_start = 2396
    _globals['_QUERYDELEGATORUNBONDINGDELEGATIONSRESPONSE']._serialized_end = 2586
    _globals['_QUERYREDELEGATIONSREQUEST']._serialized_start = 2589
    _globals['_QUERYREDELEGATIONSREQUEST']._serialized_end = 2844
    _globals['_QUERYREDELEGATIONSRESPONSE']._serialized_start = 2847
    _globals['_QUERYREDELEGATIONSRESPONSE']._serialized_end = 3025
    _globals['_QUERYDELEGATORVALIDATORSREQUEST']._serialized_start = 3028
    _globals['_QUERYDELEGATORVALIDATORSREQUEST']._serialized_end = 3181
    _globals['_QUERYDELEGATORVALIDATORSRESPONSE']._serialized_start = 3184
    _globals['_QUERYDELEGATORVALIDATORSRESPONSE']._serialized_end = 3345
    _globals['_QUERYDELEGATORVALIDATORREQUEST']._serialized_start = 3348
    _globals['_QUERYDELEGATORVALIDATORREQUEST']._serialized_end = 3490
    _globals['_QUERYDELEGATORVALIDATORRESPONSE']._serialized_start = 3492
    _globals['_QUERYDELEGATORVALIDATORRESPONSE']._serialized_end = 3590
    _globals['_QUERYHISTORICALINFOREQUEST']._serialized_start = 3592
    _globals['_QUERYHISTORICALINFOREQUEST']._serialized_end = 3636
    _globals['_QUERYHISTORICALINFORESPONSE']._serialized_start = 3638
    _globals['_QUERYHISTORICALINFORESPONSE']._serialized_end = 3721
    _globals['_QUERYPOOLREQUEST']._serialized_start = 3723
    _globals['_QUERYPOOLREQUEST']._serialized_end = 3741
    _globals['_QUERYPOOLRESPONSE']._serialized_start = 3743
    _globals['_QUERYPOOLRESPONSE']._serialized_end = 3817
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 3819
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 3839
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 3841
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 3921
    _globals['_QUERY']._serialized_start = 3924
    _globals['_QUERY']._serialized_end = 6788