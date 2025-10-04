from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class WasmPluginView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WASM_PLUGIN_VIEW_UNSPECIFIED: _ClassVar[WasmPluginView]
    WASM_PLUGIN_VIEW_BASIC: _ClassVar[WasmPluginView]
    WASM_PLUGIN_VIEW_FULL: _ClassVar[WasmPluginView]
WASM_PLUGIN_VIEW_UNSPECIFIED: WasmPluginView
WASM_PLUGIN_VIEW_BASIC: WasmPluginView
WASM_PLUGIN_VIEW_FULL: WasmPluginView

class WasmPlugin(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'description', 'labels', 'main_version_id', 'log_config', 'versions', 'used_by')

    class VersionDetails(_message.Message):
        __slots__ = ('plugin_config_data', 'plugin_config_uri', 'create_time', 'update_time', 'description', 'labels', 'image_uri', 'image_digest', 'plugin_config_digest')

        class LabelsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        PLUGIN_CONFIG_DATA_FIELD_NUMBER: _ClassVar[int]
        PLUGIN_CONFIG_URI_FIELD_NUMBER: _ClassVar[int]
        CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
        UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
        IMAGE_DIGEST_FIELD_NUMBER: _ClassVar[int]
        PLUGIN_CONFIG_DIGEST_FIELD_NUMBER: _ClassVar[int]
        plugin_config_data: bytes
        plugin_config_uri: str
        create_time: _timestamp_pb2.Timestamp
        update_time: _timestamp_pb2.Timestamp
        description: str
        labels: _containers.ScalarMap[str, str]
        image_uri: str
        image_digest: str
        plugin_config_digest: str

        def __init__(self, plugin_config_data: _Optional[bytes]=..., plugin_config_uri: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., image_uri: _Optional[str]=..., image_digest: _Optional[str]=..., plugin_config_digest: _Optional[str]=...) -> None:
            ...

    class LogConfig(_message.Message):
        __slots__ = ('enable', 'sample_rate', 'min_log_level')

        class LogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            LOG_LEVEL_UNSPECIFIED: _ClassVar[WasmPlugin.LogConfig.LogLevel]
            TRACE: _ClassVar[WasmPlugin.LogConfig.LogLevel]
            DEBUG: _ClassVar[WasmPlugin.LogConfig.LogLevel]
            INFO: _ClassVar[WasmPlugin.LogConfig.LogLevel]
            WARN: _ClassVar[WasmPlugin.LogConfig.LogLevel]
            ERROR: _ClassVar[WasmPlugin.LogConfig.LogLevel]
            CRITICAL: _ClassVar[WasmPlugin.LogConfig.LogLevel]
        LOG_LEVEL_UNSPECIFIED: WasmPlugin.LogConfig.LogLevel
        TRACE: WasmPlugin.LogConfig.LogLevel
        DEBUG: WasmPlugin.LogConfig.LogLevel
        INFO: WasmPlugin.LogConfig.LogLevel
        WARN: WasmPlugin.LogConfig.LogLevel
        ERROR: WasmPlugin.LogConfig.LogLevel
        CRITICAL: WasmPlugin.LogConfig.LogLevel
        ENABLE_FIELD_NUMBER: _ClassVar[int]
        SAMPLE_RATE_FIELD_NUMBER: _ClassVar[int]
        MIN_LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
        enable: bool
        sample_rate: float
        min_log_level: WasmPlugin.LogConfig.LogLevel

        def __init__(self, enable: bool=..., sample_rate: _Optional[float]=..., min_log_level: _Optional[_Union[WasmPlugin.LogConfig.LogLevel, str]]=...) -> None:
            ...

    class UsedBy(_message.Message):
        __slots__ = ('name',)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str

        def __init__(self, name: _Optional[str]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class VersionsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: WasmPlugin.VersionDetails

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[WasmPlugin.VersionDetails, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    MAIN_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    LOG_CONFIG_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    USED_BY_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    labels: _containers.ScalarMap[str, str]
    main_version_id: str
    log_config: WasmPlugin.LogConfig
    versions: _containers.MessageMap[str, WasmPlugin.VersionDetails]
    used_by: _containers.RepeatedCompositeFieldContainer[WasmPlugin.UsedBy]

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., main_version_id: _Optional[str]=..., log_config: _Optional[_Union[WasmPlugin.LogConfig, _Mapping]]=..., versions: _Optional[_Mapping[str, WasmPlugin.VersionDetails]]=..., used_by: _Optional[_Iterable[_Union[WasmPlugin.UsedBy, _Mapping]]]=...) -> None:
        ...

class WasmPluginVersion(_message.Message):
    __slots__ = ('plugin_config_data', 'plugin_config_uri', 'name', 'create_time', 'update_time', 'description', 'labels', 'image_uri', 'image_digest', 'plugin_config_digest')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PLUGIN_CONFIG_DATA_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_CONFIG_URI_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    IMAGE_DIGEST_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_CONFIG_DIGEST_FIELD_NUMBER: _ClassVar[int]
    plugin_config_data: bytes
    plugin_config_uri: str
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    description: str
    labels: _containers.ScalarMap[str, str]
    image_uri: str
    image_digest: str
    plugin_config_digest: str

    def __init__(self, plugin_config_data: _Optional[bytes]=..., plugin_config_uri: _Optional[str]=..., name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., description: _Optional[str]=..., labels: _Optional[_Mapping[str, str]]=..., image_uri: _Optional[str]=..., image_digest: _Optional[str]=..., plugin_config_digest: _Optional[str]=...) -> None:
        ...

class ListWasmPluginsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListWasmPluginsResponse(_message.Message):
    __slots__ = ('wasm_plugins', 'next_page_token', 'unreachable')
    WASM_PLUGINS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    wasm_plugins: _containers.RepeatedCompositeFieldContainer[WasmPlugin]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, wasm_plugins: _Optional[_Iterable[_Union[WasmPlugin, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetWasmPluginRequest(_message.Message):
    __slots__ = ('name', 'view')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    name: str
    view: WasmPluginView

    def __init__(self, name: _Optional[str]=..., view: _Optional[_Union[WasmPluginView, str]]=...) -> None:
        ...

class CreateWasmPluginRequest(_message.Message):
    __slots__ = ('parent', 'wasm_plugin_id', 'wasm_plugin')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WASM_PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    WASM_PLUGIN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    wasm_plugin_id: str
    wasm_plugin: WasmPlugin

    def __init__(self, parent: _Optional[str]=..., wasm_plugin_id: _Optional[str]=..., wasm_plugin: _Optional[_Union[WasmPlugin, _Mapping]]=...) -> None:
        ...

class UpdateWasmPluginRequest(_message.Message):
    __slots__ = ('update_mask', 'wasm_plugin')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    WASM_PLUGIN_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    wasm_plugin: WasmPlugin

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., wasm_plugin: _Optional[_Union[WasmPlugin, _Mapping]]=...) -> None:
        ...

class DeleteWasmPluginRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListWasmPluginVersionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListWasmPluginVersionsResponse(_message.Message):
    __slots__ = ('wasm_plugin_versions', 'next_page_token', 'unreachable')
    WASM_PLUGIN_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    wasm_plugin_versions: _containers.RepeatedCompositeFieldContainer[WasmPluginVersion]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, wasm_plugin_versions: _Optional[_Iterable[_Union[WasmPluginVersion, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetWasmPluginVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateWasmPluginVersionRequest(_message.Message):
    __slots__ = ('parent', 'wasm_plugin_version_id', 'wasm_plugin_version')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WASM_PLUGIN_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    WASM_PLUGIN_VERSION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    wasm_plugin_version_id: str
    wasm_plugin_version: WasmPluginVersion

    def __init__(self, parent: _Optional[str]=..., wasm_plugin_version_id: _Optional[str]=..., wasm_plugin_version: _Optional[_Union[WasmPluginVersion, _Mapping]]=...) -> None:
        ...

class DeleteWasmPluginVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...