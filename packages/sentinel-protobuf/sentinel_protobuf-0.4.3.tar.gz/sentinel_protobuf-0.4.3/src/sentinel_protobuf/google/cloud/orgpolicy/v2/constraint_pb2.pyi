from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Constraint(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'constraint_default', 'list_constraint', 'boolean_constraint', 'supports_dry_run', 'equivalent_constraint', 'supports_simulation')

    class ConstraintDefault(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONSTRAINT_DEFAULT_UNSPECIFIED: _ClassVar[Constraint.ConstraintDefault]
        ALLOW: _ClassVar[Constraint.ConstraintDefault]
        DENY: _ClassVar[Constraint.ConstraintDefault]
    CONSTRAINT_DEFAULT_UNSPECIFIED: Constraint.ConstraintDefault
    ALLOW: Constraint.ConstraintDefault
    DENY: Constraint.ConstraintDefault

    class ListConstraint(_message.Message):
        __slots__ = ('supports_in', 'supports_under')
        SUPPORTS_IN_FIELD_NUMBER: _ClassVar[int]
        SUPPORTS_UNDER_FIELD_NUMBER: _ClassVar[int]
        supports_in: bool
        supports_under: bool

        def __init__(self, supports_in: bool=..., supports_under: bool=...) -> None:
            ...

    class CustomConstraintDefinition(_message.Message):
        __slots__ = ('resource_types', 'method_types', 'condition', 'action_type', 'parameters')

        class MethodType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            METHOD_TYPE_UNSPECIFIED: _ClassVar[Constraint.CustomConstraintDefinition.MethodType]
            CREATE: _ClassVar[Constraint.CustomConstraintDefinition.MethodType]
            UPDATE: _ClassVar[Constraint.CustomConstraintDefinition.MethodType]
            DELETE: _ClassVar[Constraint.CustomConstraintDefinition.MethodType]
            REMOVE_GRANT: _ClassVar[Constraint.CustomConstraintDefinition.MethodType]
            GOVERN_TAGS: _ClassVar[Constraint.CustomConstraintDefinition.MethodType]
        METHOD_TYPE_UNSPECIFIED: Constraint.CustomConstraintDefinition.MethodType
        CREATE: Constraint.CustomConstraintDefinition.MethodType
        UPDATE: Constraint.CustomConstraintDefinition.MethodType
        DELETE: Constraint.CustomConstraintDefinition.MethodType
        REMOVE_GRANT: Constraint.CustomConstraintDefinition.MethodType
        GOVERN_TAGS: Constraint.CustomConstraintDefinition.MethodType

        class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ACTION_TYPE_UNSPECIFIED: _ClassVar[Constraint.CustomConstraintDefinition.ActionType]
            ALLOW: _ClassVar[Constraint.CustomConstraintDefinition.ActionType]
            DENY: _ClassVar[Constraint.CustomConstraintDefinition.ActionType]
        ACTION_TYPE_UNSPECIFIED: Constraint.CustomConstraintDefinition.ActionType
        ALLOW: Constraint.CustomConstraintDefinition.ActionType
        DENY: Constraint.CustomConstraintDefinition.ActionType

        class Parameter(_message.Message):
            __slots__ = ('type', 'default_value', 'valid_values_expr', 'metadata', 'item')

            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                TYPE_UNSPECIFIED: _ClassVar[Constraint.CustomConstraintDefinition.Parameter.Type]
                LIST: _ClassVar[Constraint.CustomConstraintDefinition.Parameter.Type]
                STRING: _ClassVar[Constraint.CustomConstraintDefinition.Parameter.Type]
                BOOLEAN: _ClassVar[Constraint.CustomConstraintDefinition.Parameter.Type]
            TYPE_UNSPECIFIED: Constraint.CustomConstraintDefinition.Parameter.Type
            LIST: Constraint.CustomConstraintDefinition.Parameter.Type
            STRING: Constraint.CustomConstraintDefinition.Parameter.Type
            BOOLEAN: Constraint.CustomConstraintDefinition.Parameter.Type

            class Metadata(_message.Message):
                __slots__ = ('description',)
                DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
                description: str

                def __init__(self, description: _Optional[str]=...) -> None:
                    ...
            TYPE_FIELD_NUMBER: _ClassVar[int]
            DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
            VALID_VALUES_EXPR_FIELD_NUMBER: _ClassVar[int]
            METADATA_FIELD_NUMBER: _ClassVar[int]
            ITEM_FIELD_NUMBER: _ClassVar[int]
            type: Constraint.CustomConstraintDefinition.Parameter.Type
            default_value: _struct_pb2.Value
            valid_values_expr: str
            metadata: Constraint.CustomConstraintDefinition.Parameter.Metadata
            item: Constraint.CustomConstraintDefinition.Parameter.Type

            def __init__(self, type: _Optional[_Union[Constraint.CustomConstraintDefinition.Parameter.Type, str]]=..., default_value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., valid_values_expr: _Optional[str]=..., metadata: _Optional[_Union[Constraint.CustomConstraintDefinition.Parameter.Metadata, _Mapping]]=..., item: _Optional[_Union[Constraint.CustomConstraintDefinition.Parameter.Type, str]]=...) -> None:
                ...

        class ParametersEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: Constraint.CustomConstraintDefinition.Parameter

            def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[Constraint.CustomConstraintDefinition.Parameter, _Mapping]]=...) -> None:
                ...
        RESOURCE_TYPES_FIELD_NUMBER: _ClassVar[int]
        METHOD_TYPES_FIELD_NUMBER: _ClassVar[int]
        CONDITION_FIELD_NUMBER: _ClassVar[int]
        ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
        PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        resource_types: _containers.RepeatedScalarFieldContainer[str]
        method_types: _containers.RepeatedScalarFieldContainer[Constraint.CustomConstraintDefinition.MethodType]
        condition: str
        action_type: Constraint.CustomConstraintDefinition.ActionType
        parameters: _containers.MessageMap[str, Constraint.CustomConstraintDefinition.Parameter]

        def __init__(self, resource_types: _Optional[_Iterable[str]]=..., method_types: _Optional[_Iterable[_Union[Constraint.CustomConstraintDefinition.MethodType, str]]]=..., condition: _Optional[str]=..., action_type: _Optional[_Union[Constraint.CustomConstraintDefinition.ActionType, str]]=..., parameters: _Optional[_Mapping[str, Constraint.CustomConstraintDefinition.Parameter]]=...) -> None:
            ...

    class BooleanConstraint(_message.Message):
        __slots__ = ('custom_constraint_definition',)
        CUSTOM_CONSTRAINT_DEFINITION_FIELD_NUMBER: _ClassVar[int]
        custom_constraint_definition: Constraint.CustomConstraintDefinition

        def __init__(self, custom_constraint_definition: _Optional[_Union[Constraint.CustomConstraintDefinition, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    LIST_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    EQUIVALENT_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    SUPPORTS_SIMULATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    constraint_default: Constraint.ConstraintDefault
    list_constraint: Constraint.ListConstraint
    boolean_constraint: Constraint.BooleanConstraint
    supports_dry_run: bool
    equivalent_constraint: str
    supports_simulation: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., constraint_default: _Optional[_Union[Constraint.ConstraintDefault, str]]=..., list_constraint: _Optional[_Union[Constraint.ListConstraint, _Mapping]]=..., boolean_constraint: _Optional[_Union[Constraint.BooleanConstraint, _Mapping]]=..., supports_dry_run: bool=..., equivalent_constraint: _Optional[str]=..., supports_simulation: bool=...) -> None:
        ...

class CustomConstraint(_message.Message):
    __slots__ = ('name', 'resource_types', 'method_types', 'condition', 'action_type', 'display_name', 'description', 'update_time')

    class MethodType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        METHOD_TYPE_UNSPECIFIED: _ClassVar[CustomConstraint.MethodType]
        CREATE: _ClassVar[CustomConstraint.MethodType]
        UPDATE: _ClassVar[CustomConstraint.MethodType]
        DELETE: _ClassVar[CustomConstraint.MethodType]
        REMOVE_GRANT: _ClassVar[CustomConstraint.MethodType]
        GOVERN_TAGS: _ClassVar[CustomConstraint.MethodType]
    METHOD_TYPE_UNSPECIFIED: CustomConstraint.MethodType
    CREATE: CustomConstraint.MethodType
    UPDATE: CustomConstraint.MethodType
    DELETE: CustomConstraint.MethodType
    REMOVE_GRANT: CustomConstraint.MethodType
    GOVERN_TAGS: CustomConstraint.MethodType

    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_TYPE_UNSPECIFIED: _ClassVar[CustomConstraint.ActionType]
        ALLOW: _ClassVar[CustomConstraint.ActionType]
        DENY: _ClassVar[CustomConstraint.ActionType]
    ACTION_TYPE_UNSPECIFIED: CustomConstraint.ActionType
    ALLOW: CustomConstraint.ActionType
    DENY: CustomConstraint.ActionType
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPES_FIELD_NUMBER: _ClassVar[int]
    METHOD_TYPES_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    resource_types: _containers.RepeatedScalarFieldContainer[str]
    method_types: _containers.RepeatedScalarFieldContainer[CustomConstraint.MethodType]
    condition: str
    action_type: CustomConstraint.ActionType
    display_name: str
    description: str
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., resource_types: _Optional[_Iterable[str]]=..., method_types: _Optional[_Iterable[_Union[CustomConstraint.MethodType, str]]]=..., condition: _Optional[str]=..., action_type: _Optional[_Union[CustomConstraint.ActionType, str]]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...