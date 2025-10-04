from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.universalledger.v1 import common_pb2 as _common_pb2
from google.cloud.universalledger.v1 import status_event_pb2 as _status_event_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ClientTransaction(_message.Message):
    __slots__ = ('app', 'operational', 'chain', 'source', 'signatories', 'sequence_number', 'chained_unit')
    APP_FIELD_NUMBER: _ClassVar[int]
    OPERATIONAL_FIELD_NUMBER: _ClassVar[int]
    CHAIN_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SIGNATORIES_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CHAINED_UNIT_FIELD_NUMBER: _ClassVar[int]
    app: _any_pb2.Any
    operational: _any_pb2.Any
    chain: TransactionChain
    source: _common_pb2.Entity
    signatories: _containers.RepeatedCompositeFieldContainer[_common_pb2.Entity]
    sequence_number: int
    chained_unit: bool

    def __init__(self, app: _Optional[_Union[_any_pb2.Any, _Mapping]]=..., operational: _Optional[_Union[_any_pb2.Any, _Mapping]]=..., chain: _Optional[_Union[TransactionChain, _Mapping]]=..., source: _Optional[_Union[_common_pb2.Entity, _Mapping]]=..., signatories: _Optional[_Iterable[_Union[_common_pb2.Entity, _Mapping]]]=..., sequence_number: _Optional[int]=..., chained_unit: bool=...) -> None:
        ...

class SignedTransaction(_message.Message):
    __slots__ = ('serialized_client_transaction', 'sender_signature', 'other_signatures')
    SERIALIZED_CLIENT_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    SENDER_SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    OTHER_SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    serialized_client_transaction: bytes
    sender_signature: bytes
    other_signatures: _containers.RepeatedScalarFieldContainer[bytes]

    def __init__(self, serialized_client_transaction: _Optional[bytes]=..., sender_signature: _Optional[bytes]=..., other_signatures: _Optional[_Iterable[bytes]]=...) -> None:
        ...

class TransactionChain(_message.Message):
    __slots__ = ('units',)
    UNITS_FIELD_NUMBER: _ClassVar[int]
    units: _containers.RepeatedScalarFieldContainer[bytes]

    def __init__(self, units: _Optional[_Iterable[bytes]]=...) -> None:
        ...

class MerkleTree(_message.Message):
    __slots__ = ('root_hash_hex', 'num_transactions')
    ROOT_HASH_HEX_FIELD_NUMBER: _ClassVar[int]
    NUM_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    root_hash_hex: str
    num_transactions: int

    def __init__(self, root_hash_hex: _Optional[str]=..., num_transactions: _Optional[int]=...) -> None:
        ...

class RoundCertificate(_message.Message):
    __slots__ = ('round_id', 'validator_id', 'round_state_checksum_hex', 'round_delta_checksum_hex', 'merkle_tree', 'validator_signatures', 'is_finalized')
    ROUND_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_ID_FIELD_NUMBER: _ClassVar[int]
    ROUND_STATE_CHECKSUM_HEX_FIELD_NUMBER: _ClassVar[int]
    ROUND_DELTA_CHECKSUM_HEX_FIELD_NUMBER: _ClassVar[int]
    MERKLE_TREE_FIELD_NUMBER: _ClassVar[int]
    VALIDATOR_SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    IS_FINALIZED_FIELD_NUMBER: _ClassVar[int]
    round_id: int
    validator_id: str
    round_state_checksum_hex: str
    round_delta_checksum_hex: str
    merkle_tree: MerkleTree
    validator_signatures: _containers.RepeatedScalarFieldContainer[bytes]
    is_finalized: bool

    def __init__(self, round_id: _Optional[int]=..., validator_id: _Optional[str]=..., round_state_checksum_hex: _Optional[str]=..., round_delta_checksum_hex: _Optional[str]=..., merkle_tree: _Optional[_Union[MerkleTree, _Mapping]]=..., validator_signatures: _Optional[_Iterable[bytes]]=..., is_finalized: bool=...) -> None:
        ...

class TransactionEffect(_message.Message):
    __slots__ = ('key', 'old_val', 'new_val', 'delta_val')
    KEY_FIELD_NUMBER: _ClassVar[int]
    OLD_VAL_FIELD_NUMBER: _ClassVar[int]
    NEW_VAL_FIELD_NUMBER: _ClassVar[int]
    DELTA_VAL_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    old_val: bytes
    new_val: bytes
    delta_val: int

    def __init__(self, key: _Optional[bytes]=..., old_val: _Optional[bytes]=..., new_val: _Optional[bytes]=..., delta_val: _Optional[int]=...) -> None:
        ...

class TransactionStatus(_message.Message):
    __slots__ = ('code', 'message')
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: bytes

    def __init__(self, code: _Optional[int]=..., message: _Optional[bytes]=...) -> None:
        ...

class TransactionEffects(_message.Message):
    __slots__ = ('status', 'effects')
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EFFECTS_FIELD_NUMBER: _ClassVar[int]
    status: TransactionStatus
    effects: _containers.RepeatedCompositeFieldContainer[TransactionEffect]

    def __init__(self, status: _Optional[_Union[TransactionStatus, _Mapping]]=..., effects: _Optional[_Iterable[_Union[TransactionEffect, _Mapping]]]=...) -> None:
        ...

class TransactionEvent(_message.Message):
    __slots__ = ('type', 'attributes')

    class EventAttribute(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    type: str
    attributes: _containers.RepeatedCompositeFieldContainer[TransactionEvent.EventAttribute]

    def __init__(self, type: _Optional[str]=..., attributes: _Optional[_Iterable[_Union[TransactionEvent.EventAttribute, _Mapping]]]=...) -> None:
        ...

class TransactionCertificate(_message.Message):
    __slots__ = ('transaction_digest_hex', 'round_id', 'transaction_effects', 'events', 'transaction_effects_state_checksum_hex', 'certification_results_digest_hex')
    TRANSACTION_DIGEST_HEX_FIELD_NUMBER: _ClassVar[int]
    ROUND_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_EFFECTS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_EFFECTS_STATE_CHECKSUM_HEX_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATION_RESULTS_DIGEST_HEX_FIELD_NUMBER: _ClassVar[int]
    transaction_digest_hex: str
    round_id: int
    transaction_effects: TransactionEffects
    events: _containers.RepeatedCompositeFieldContainer[TransactionEvent]
    transaction_effects_state_checksum_hex: str
    certification_results_digest_hex: str

    def __init__(self, transaction_digest_hex: _Optional[str]=..., round_id: _Optional[int]=..., transaction_effects: _Optional[_Union[TransactionEffects, _Mapping]]=..., events: _Optional[_Iterable[_Union[TransactionEvent, _Mapping]]]=..., transaction_effects_state_checksum_hex: _Optional[str]=..., certification_results_digest_hex: _Optional[str]=...) -> None:
        ...

class ProofOfInclusion(_message.Message):
    __slots__ = ('transaction_certificate', 'round_certificate', 'path_to_round_root')

    class MerkleTreeNode(_message.Message):
        __slots__ = ('left_child_hash_hex', 'right_child_hash_hex')
        LEFT_CHILD_HASH_HEX_FIELD_NUMBER: _ClassVar[int]
        RIGHT_CHILD_HASH_HEX_FIELD_NUMBER: _ClassVar[int]
        left_child_hash_hex: str
        right_child_hash_hex: str

        def __init__(self, left_child_hash_hex: _Optional[str]=..., right_child_hash_hex: _Optional[str]=...) -> None:
            ...
    TRANSACTION_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    ROUND_CERTIFICATE_FIELD_NUMBER: _ClassVar[int]
    PATH_TO_ROUND_ROOT_FIELD_NUMBER: _ClassVar[int]
    transaction_certificate: TransactionCertificate
    round_certificate: RoundCertificate
    path_to_round_root: _containers.RepeatedCompositeFieldContainer[ProofOfInclusion.MerkleTreeNode]

    def __init__(self, transaction_certificate: _Optional[_Union[TransactionCertificate, _Mapping]]=..., round_certificate: _Optional[_Union[RoundCertificate, _Mapping]]=..., path_to_round_root: _Optional[_Iterable[_Union[ProofOfInclusion.MerkleTreeNode, _Mapping]]]=...) -> None:
        ...

class TransactionAttempt(_message.Message):
    __slots__ = ('status', 'proof_of_inclusion', 'status_events')

    class TransactionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRANSACTION_STATUS_UNSPECIFIED: _ClassVar[TransactionAttempt.TransactionStatus]
        PENDING: _ClassVar[TransactionAttempt.TransactionStatus]
        FINALIZED: _ClassVar[TransactionAttempt.TransactionStatus]
    TRANSACTION_STATUS_UNSPECIFIED: TransactionAttempt.TransactionStatus
    PENDING: TransactionAttempt.TransactionStatus
    FINALIZED: TransactionAttempt.TransactionStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PROOF_OF_INCLUSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_EVENTS_FIELD_NUMBER: _ClassVar[int]
    status: TransactionAttempt.TransactionStatus
    proof_of_inclusion: ProofOfInclusion
    status_events: _containers.RepeatedCompositeFieldContainer[_status_event_pb2.StatusEvent]

    def __init__(self, status: _Optional[_Union[TransactionAttempt.TransactionStatus, str]]=..., proof_of_inclusion: _Optional[_Union[ProofOfInclusion, _Mapping]]=..., status_events: _Optional[_Iterable[_Union[_status_event_pb2.StatusEvent, _Mapping]]]=...) -> None:
        ...