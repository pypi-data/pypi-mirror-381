from google.ads.googleads.v21.enums import asset_field_type_pb2 as _asset_field_type_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class RemoveCampaignAutomaticallyCreatedAssetRequest(_message.Message):
    __slots__ = ('customer_id', 'operations', 'partial_failure')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[RemoveCampaignAutomaticallyCreatedAssetOperation]
    partial_failure: bool

    def __init__(self, customer_id: _Optional[str]=..., operations: _Optional[_Iterable[_Union[RemoveCampaignAutomaticallyCreatedAssetOperation, _Mapping]]]=..., partial_failure: bool=...) -> None:
        ...

class RemoveCampaignAutomaticallyCreatedAssetOperation(_message.Message):
    __slots__ = ('campaign', 'asset', 'field_type')
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    ASSET_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    campaign: str
    asset: str
    field_type: _asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType

    def __init__(self, campaign: _Optional[str]=..., asset: _Optional[str]=..., field_type: _Optional[_Union[_asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType, str]]=...) -> None:
        ...

class RemoveCampaignAutomaticallyCreatedAssetResponse(_message.Message):
    __slots__ = ('partial_failure_error',)
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    partial_failure_error: _status_pb2.Status

    def __init__(self, partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...