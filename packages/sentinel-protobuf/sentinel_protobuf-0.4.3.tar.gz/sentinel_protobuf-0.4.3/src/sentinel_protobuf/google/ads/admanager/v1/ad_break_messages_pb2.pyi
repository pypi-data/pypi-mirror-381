from google.ads.admanager.v1 import early_ad_break_notification_enums_pb2 as _early_ad_break_notification_enums_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AdBreak(_message.Message):
    __slots__ = ('name', 'ad_break_id', 'asset_key', 'custom_asset_key', 'expected_start_time', 'duration', 'break_state', 'break_sequence', 'pod_template_name', 'custom_params', 'scte_35_cue_out')
    NAME_FIELD_NUMBER: _ClassVar[int]
    AD_BREAK_ID_FIELD_NUMBER: _ClassVar[int]
    ASSET_KEY_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_ASSET_KEY_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_START_TIME_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    BREAK_STATE_FIELD_NUMBER: _ClassVar[int]
    BREAK_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    POD_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SCTE_35_CUE_OUT_FIELD_NUMBER: _ClassVar[int]
    name: str
    ad_break_id: str
    asset_key: str
    custom_asset_key: str
    expected_start_time: _timestamp_pb2.Timestamp
    duration: _duration_pb2.Duration
    break_state: _early_ad_break_notification_enums_pb2.AdBreakStateEnum.AdBreakState
    break_sequence: int
    pod_template_name: str
    custom_params: str
    scte_35_cue_out: str

    def __init__(self, name: _Optional[str]=..., ad_break_id: _Optional[str]=..., asset_key: _Optional[str]=..., custom_asset_key: _Optional[str]=..., expected_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., break_state: _Optional[_Union[_early_ad_break_notification_enums_pb2.AdBreakStateEnum.AdBreakState, str]]=..., break_sequence: _Optional[int]=..., pod_template_name: _Optional[str]=..., custom_params: _Optional[str]=..., scte_35_cue_out: _Optional[str]=...) -> None:
        ...