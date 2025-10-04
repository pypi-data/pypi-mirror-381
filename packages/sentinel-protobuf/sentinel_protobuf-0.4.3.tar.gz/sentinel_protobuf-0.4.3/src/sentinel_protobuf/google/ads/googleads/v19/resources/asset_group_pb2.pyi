from google.ads.googleads.v19.enums import ad_strength_pb2 as _ad_strength_pb2
from google.ads.googleads.v19.enums import ad_strength_action_item_type_pb2 as _ad_strength_action_item_type_pb2
from google.ads.googleads.v19.enums import asset_coverage_video_aspect_ratio_requirement_pb2 as _asset_coverage_video_aspect_ratio_requirement_pb2
from google.ads.googleads.v19.enums import asset_field_type_pb2 as _asset_field_type_pb2
from google.ads.googleads.v19.enums import asset_group_primary_status_pb2 as _asset_group_primary_status_pb2
from google.ads.googleads.v19.enums import asset_group_primary_status_reason_pb2 as _asset_group_primary_status_reason_pb2
from google.ads.googleads.v19.enums import asset_group_status_pb2 as _asset_group_status_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AssetGroup(_message.Message):
    __slots__ = ('resource_name', 'id', 'campaign', 'name', 'final_urls', 'final_mobile_urls', 'status', 'primary_status', 'primary_status_reasons', 'path1', 'path2', 'ad_strength', 'asset_coverage')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FINAL_URLS_FIELD_NUMBER: _ClassVar[int]
    FINAL_MOBILE_URLS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STATUS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STATUS_REASONS_FIELD_NUMBER: _ClassVar[int]
    PATH1_FIELD_NUMBER: _ClassVar[int]
    PATH2_FIELD_NUMBER: _ClassVar[int]
    AD_STRENGTH_FIELD_NUMBER: _ClassVar[int]
    ASSET_COVERAGE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    id: int
    campaign: str
    name: str
    final_urls: _containers.RepeatedScalarFieldContainer[str]
    final_mobile_urls: _containers.RepeatedScalarFieldContainer[str]
    status: _asset_group_status_pb2.AssetGroupStatusEnum.AssetGroupStatus
    primary_status: _asset_group_primary_status_pb2.AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus
    primary_status_reasons: _containers.RepeatedScalarFieldContainer[_asset_group_primary_status_reason_pb2.AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason]
    path1: str
    path2: str
    ad_strength: _ad_strength_pb2.AdStrengthEnum.AdStrength
    asset_coverage: AssetCoverage

    def __init__(self, resource_name: _Optional[str]=..., id: _Optional[int]=..., campaign: _Optional[str]=..., name: _Optional[str]=..., final_urls: _Optional[_Iterable[str]]=..., final_mobile_urls: _Optional[_Iterable[str]]=..., status: _Optional[_Union[_asset_group_status_pb2.AssetGroupStatusEnum.AssetGroupStatus, str]]=..., primary_status: _Optional[_Union[_asset_group_primary_status_pb2.AssetGroupPrimaryStatusEnum.AssetGroupPrimaryStatus, str]]=..., primary_status_reasons: _Optional[_Iterable[_Union[_asset_group_primary_status_reason_pb2.AssetGroupPrimaryStatusReasonEnum.AssetGroupPrimaryStatusReason, str]]]=..., path1: _Optional[str]=..., path2: _Optional[str]=..., ad_strength: _Optional[_Union[_ad_strength_pb2.AdStrengthEnum.AdStrength, str]]=..., asset_coverage: _Optional[_Union[AssetCoverage, _Mapping]]=...) -> None:
        ...

class AssetCoverage(_message.Message):
    __slots__ = ('ad_strength_action_items',)
    AD_STRENGTH_ACTION_ITEMS_FIELD_NUMBER: _ClassVar[int]
    ad_strength_action_items: _containers.RepeatedCompositeFieldContainer[AdStrengthActionItem]

    def __init__(self, ad_strength_action_items: _Optional[_Iterable[_Union[AdStrengthActionItem, _Mapping]]]=...) -> None:
        ...

class AdStrengthActionItem(_message.Message):
    __slots__ = ('action_item_type', 'add_asset_details')

    class AddAssetDetails(_message.Message):
        __slots__ = ('asset_field_type', 'asset_count', 'video_aspect_ratio_requirement')
        ASSET_FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
        ASSET_COUNT_FIELD_NUMBER: _ClassVar[int]
        VIDEO_ASPECT_RATIO_REQUIREMENT_FIELD_NUMBER: _ClassVar[int]
        asset_field_type: _asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType
        asset_count: int
        video_aspect_ratio_requirement: _asset_coverage_video_aspect_ratio_requirement_pb2.AssetCoverageVideoAspectRatioRequirementEnum.AssetCoverageVideoAspectRatioRequirement

        def __init__(self, asset_field_type: _Optional[_Union[_asset_field_type_pb2.AssetFieldTypeEnum.AssetFieldType, str]]=..., asset_count: _Optional[int]=..., video_aspect_ratio_requirement: _Optional[_Union[_asset_coverage_video_aspect_ratio_requirement_pb2.AssetCoverageVideoAspectRatioRequirementEnum.AssetCoverageVideoAspectRatioRequirement, str]]=...) -> None:
            ...
    ACTION_ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    ADD_ASSET_DETAILS_FIELD_NUMBER: _ClassVar[int]
    action_item_type: _ad_strength_action_item_type_pb2.AdStrengthActionItemTypeEnum.AdStrengthActionItemType
    add_asset_details: AdStrengthActionItem.AddAssetDetails

    def __init__(self, action_item_type: _Optional[_Union[_ad_strength_action_item_type_pb2.AdStrengthActionItemTypeEnum.AdStrengthActionItemType, str]]=..., add_asset_details: _Optional[_Union[AdStrengthActionItem.AddAssetDetails, _Mapping]]=...) -> None:
        ...