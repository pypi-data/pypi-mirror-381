from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.spanner.v1 import type_pb2 as _type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ChangeStreamRecord(_message.Message):
    __slots__ = ('data_change_record', 'heartbeat_record', 'partition_start_record', 'partition_end_record', 'partition_event_record')

    class DataChangeRecord(_message.Message):
        __slots__ = ('commit_timestamp', 'record_sequence', 'server_transaction_id', 'is_last_record_in_transaction_in_partition', 'table', 'column_metadata', 'mods', 'mod_type', 'value_capture_type', 'number_of_records_in_transaction', 'number_of_partitions_in_transaction', 'transaction_tag', 'is_system_transaction')

        class ModType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MOD_TYPE_UNSPECIFIED: _ClassVar[ChangeStreamRecord.DataChangeRecord.ModType]
            INSERT: _ClassVar[ChangeStreamRecord.DataChangeRecord.ModType]
            UPDATE: _ClassVar[ChangeStreamRecord.DataChangeRecord.ModType]
            DELETE: _ClassVar[ChangeStreamRecord.DataChangeRecord.ModType]
        MOD_TYPE_UNSPECIFIED: ChangeStreamRecord.DataChangeRecord.ModType
        INSERT: ChangeStreamRecord.DataChangeRecord.ModType
        UPDATE: ChangeStreamRecord.DataChangeRecord.ModType
        DELETE: ChangeStreamRecord.DataChangeRecord.ModType

        class ValueCaptureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            VALUE_CAPTURE_TYPE_UNSPECIFIED: _ClassVar[ChangeStreamRecord.DataChangeRecord.ValueCaptureType]
            OLD_AND_NEW_VALUES: _ClassVar[ChangeStreamRecord.DataChangeRecord.ValueCaptureType]
            NEW_VALUES: _ClassVar[ChangeStreamRecord.DataChangeRecord.ValueCaptureType]
            NEW_ROW: _ClassVar[ChangeStreamRecord.DataChangeRecord.ValueCaptureType]
            NEW_ROW_AND_OLD_VALUES: _ClassVar[ChangeStreamRecord.DataChangeRecord.ValueCaptureType]
        VALUE_CAPTURE_TYPE_UNSPECIFIED: ChangeStreamRecord.DataChangeRecord.ValueCaptureType
        OLD_AND_NEW_VALUES: ChangeStreamRecord.DataChangeRecord.ValueCaptureType
        NEW_VALUES: ChangeStreamRecord.DataChangeRecord.ValueCaptureType
        NEW_ROW: ChangeStreamRecord.DataChangeRecord.ValueCaptureType
        NEW_ROW_AND_OLD_VALUES: ChangeStreamRecord.DataChangeRecord.ValueCaptureType

        class ColumnMetadata(_message.Message):
            __slots__ = ('name', 'type', 'is_primary_key', 'ordinal_position')
            NAME_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            IS_PRIMARY_KEY_FIELD_NUMBER: _ClassVar[int]
            ORDINAL_POSITION_FIELD_NUMBER: _ClassVar[int]
            name: str
            type: _type_pb2.Type
            is_primary_key: bool
            ordinal_position: int

            def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[_type_pb2.Type, _Mapping]]=..., is_primary_key: bool=..., ordinal_position: _Optional[int]=...) -> None:
                ...

        class ModValue(_message.Message):
            __slots__ = ('column_metadata_index', 'value')
            COLUMN_METADATA_INDEX_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            column_metadata_index: int
            value: _struct_pb2.Value

            def __init__(self, column_metadata_index: _Optional[int]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
                ...

        class Mod(_message.Message):
            __slots__ = ('keys', 'old_values', 'new_values')
            KEYS_FIELD_NUMBER: _ClassVar[int]
            OLD_VALUES_FIELD_NUMBER: _ClassVar[int]
            NEW_VALUES_FIELD_NUMBER: _ClassVar[int]
            keys: _containers.RepeatedCompositeFieldContainer[ChangeStreamRecord.DataChangeRecord.ModValue]
            old_values: _containers.RepeatedCompositeFieldContainer[ChangeStreamRecord.DataChangeRecord.ModValue]
            new_values: _containers.RepeatedCompositeFieldContainer[ChangeStreamRecord.DataChangeRecord.ModValue]

            def __init__(self, keys: _Optional[_Iterable[_Union[ChangeStreamRecord.DataChangeRecord.ModValue, _Mapping]]]=..., old_values: _Optional[_Iterable[_Union[ChangeStreamRecord.DataChangeRecord.ModValue, _Mapping]]]=..., new_values: _Optional[_Iterable[_Union[ChangeStreamRecord.DataChangeRecord.ModValue, _Mapping]]]=...) -> None:
                ...
        COMMIT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        RECORD_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
        SERVER_TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
        IS_LAST_RECORD_IN_TRANSACTION_IN_PARTITION_FIELD_NUMBER: _ClassVar[int]
        TABLE_FIELD_NUMBER: _ClassVar[int]
        COLUMN_METADATA_FIELD_NUMBER: _ClassVar[int]
        MODS_FIELD_NUMBER: _ClassVar[int]
        MOD_TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_CAPTURE_TYPE_FIELD_NUMBER: _ClassVar[int]
        NUMBER_OF_RECORDS_IN_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
        NUMBER_OF_PARTITIONS_IN_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_TAG_FIELD_NUMBER: _ClassVar[int]
        IS_SYSTEM_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
        commit_timestamp: _timestamp_pb2.Timestamp
        record_sequence: str
        server_transaction_id: str
        is_last_record_in_transaction_in_partition: bool
        table: str
        column_metadata: _containers.RepeatedCompositeFieldContainer[ChangeStreamRecord.DataChangeRecord.ColumnMetadata]
        mods: _containers.RepeatedCompositeFieldContainer[ChangeStreamRecord.DataChangeRecord.Mod]
        mod_type: ChangeStreamRecord.DataChangeRecord.ModType
        value_capture_type: ChangeStreamRecord.DataChangeRecord.ValueCaptureType
        number_of_records_in_transaction: int
        number_of_partitions_in_transaction: int
        transaction_tag: str
        is_system_transaction: bool

        def __init__(self, commit_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., record_sequence: _Optional[str]=..., server_transaction_id: _Optional[str]=..., is_last_record_in_transaction_in_partition: bool=..., table: _Optional[str]=..., column_metadata: _Optional[_Iterable[_Union[ChangeStreamRecord.DataChangeRecord.ColumnMetadata, _Mapping]]]=..., mods: _Optional[_Iterable[_Union[ChangeStreamRecord.DataChangeRecord.Mod, _Mapping]]]=..., mod_type: _Optional[_Union[ChangeStreamRecord.DataChangeRecord.ModType, str]]=..., value_capture_type: _Optional[_Union[ChangeStreamRecord.DataChangeRecord.ValueCaptureType, str]]=..., number_of_records_in_transaction: _Optional[int]=..., number_of_partitions_in_transaction: _Optional[int]=..., transaction_tag: _Optional[str]=..., is_system_transaction: bool=...) -> None:
            ...

    class HeartbeatRecord(_message.Message):
        __slots__ = ('timestamp',)
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        timestamp: _timestamp_pb2.Timestamp

        def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class PartitionStartRecord(_message.Message):
        __slots__ = ('start_timestamp', 'record_sequence', 'partition_tokens')
        START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        RECORD_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
        PARTITION_TOKENS_FIELD_NUMBER: _ClassVar[int]
        start_timestamp: _timestamp_pb2.Timestamp
        record_sequence: str
        partition_tokens: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, start_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., record_sequence: _Optional[str]=..., partition_tokens: _Optional[_Iterable[str]]=...) -> None:
            ...

    class PartitionEndRecord(_message.Message):
        __slots__ = ('end_timestamp', 'record_sequence', 'partition_token')
        END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        RECORD_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
        PARTITION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        end_timestamp: _timestamp_pb2.Timestamp
        record_sequence: str
        partition_token: str

        def __init__(self, end_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., record_sequence: _Optional[str]=..., partition_token: _Optional[str]=...) -> None:
            ...

    class PartitionEventRecord(_message.Message):
        __slots__ = ('commit_timestamp', 'record_sequence', 'partition_token', 'move_in_events', 'move_out_events')

        class MoveInEvent(_message.Message):
            __slots__ = ('source_partition_token',)
            SOURCE_PARTITION_TOKEN_FIELD_NUMBER: _ClassVar[int]
            source_partition_token: str

            def __init__(self, source_partition_token: _Optional[str]=...) -> None:
                ...

        class MoveOutEvent(_message.Message):
            __slots__ = ('destination_partition_token',)
            DESTINATION_PARTITION_TOKEN_FIELD_NUMBER: _ClassVar[int]
            destination_partition_token: str

            def __init__(self, destination_partition_token: _Optional[str]=...) -> None:
                ...
        COMMIT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        RECORD_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
        PARTITION_TOKEN_FIELD_NUMBER: _ClassVar[int]
        MOVE_IN_EVENTS_FIELD_NUMBER: _ClassVar[int]
        MOVE_OUT_EVENTS_FIELD_NUMBER: _ClassVar[int]
        commit_timestamp: _timestamp_pb2.Timestamp
        record_sequence: str
        partition_token: str
        move_in_events: _containers.RepeatedCompositeFieldContainer[ChangeStreamRecord.PartitionEventRecord.MoveInEvent]
        move_out_events: _containers.RepeatedCompositeFieldContainer[ChangeStreamRecord.PartitionEventRecord.MoveOutEvent]

        def __init__(self, commit_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., record_sequence: _Optional[str]=..., partition_token: _Optional[str]=..., move_in_events: _Optional[_Iterable[_Union[ChangeStreamRecord.PartitionEventRecord.MoveInEvent, _Mapping]]]=..., move_out_events: _Optional[_Iterable[_Union[ChangeStreamRecord.PartitionEventRecord.MoveOutEvent, _Mapping]]]=...) -> None:
            ...
    DATA_CHANGE_RECORD_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_RECORD_FIELD_NUMBER: _ClassVar[int]
    PARTITION_START_RECORD_FIELD_NUMBER: _ClassVar[int]
    PARTITION_END_RECORD_FIELD_NUMBER: _ClassVar[int]
    PARTITION_EVENT_RECORD_FIELD_NUMBER: _ClassVar[int]
    data_change_record: ChangeStreamRecord.DataChangeRecord
    heartbeat_record: ChangeStreamRecord.HeartbeatRecord
    partition_start_record: ChangeStreamRecord.PartitionStartRecord
    partition_end_record: ChangeStreamRecord.PartitionEndRecord
    partition_event_record: ChangeStreamRecord.PartitionEventRecord

    def __init__(self, data_change_record: _Optional[_Union[ChangeStreamRecord.DataChangeRecord, _Mapping]]=..., heartbeat_record: _Optional[_Union[ChangeStreamRecord.HeartbeatRecord, _Mapping]]=..., partition_start_record: _Optional[_Union[ChangeStreamRecord.PartitionStartRecord, _Mapping]]=..., partition_end_record: _Optional[_Union[ChangeStreamRecord.PartitionEndRecord, _Mapping]]=..., partition_event_record: _Optional[_Union[ChangeStreamRecord.PartitionEventRecord, _Mapping]]=...) -> None:
        ...