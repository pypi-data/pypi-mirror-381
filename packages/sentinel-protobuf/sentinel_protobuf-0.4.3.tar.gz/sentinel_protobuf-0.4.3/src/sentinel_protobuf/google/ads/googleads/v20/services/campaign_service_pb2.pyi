from google.ads.googleads.v20.enums import response_content_type_pb2 as _response_content_type_pb2
from google.ads.googleads.v20.resources import campaign_pb2 as _campaign_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MutateCampaignsRequest(_message.Message):
    __slots__ = ('customer_id', 'operations', 'partial_failure', 'validate_only', 'response_content_type')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[CampaignOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: _response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType

    def __init__(self, customer_id: _Optional[str]=..., operations: _Optional[_Iterable[_Union[CampaignOperation, _Mapping]]]=..., partial_failure: bool=..., validate_only: bool=..., response_content_type: _Optional[_Union[_response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType, str]]=...) -> None:
        ...

class CampaignOperation(_message.Message):
    __slots__ = ('update_mask', 'create', 'update', 'remove')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    create: _campaign_pb2.Campaign
    update: _campaign_pb2.Campaign
    remove: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., create: _Optional[_Union[_campaign_pb2.Campaign, _Mapping]]=..., update: _Optional[_Union[_campaign_pb2.Campaign, _Mapping]]=..., remove: _Optional[str]=...) -> None:
        ...

class MutateCampaignsResponse(_message.Message):
    __slots__ = ('partial_failure_error', 'results')
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    partial_failure_error: _status_pb2.Status
    results: _containers.RepeatedCompositeFieldContainer[MutateCampaignResult]

    def __init__(self, partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., results: _Optional[_Iterable[_Union[MutateCampaignResult, _Mapping]]]=...) -> None:
        ...

class MutateCampaignResult(_message.Message):
    __slots__ = ('resource_name', 'campaign')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    campaign: _campaign_pb2.Campaign

    def __init__(self, resource_name: _Optional[str]=..., campaign: _Optional[_Union[_campaign_pb2.Campaign, _Mapping]]=...) -> None:
        ...

class EnablePMaxBrandGuidelinesRequest(_message.Message):
    __slots__ = ('customer_id', 'operations')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[EnableOperation]

    def __init__(self, customer_id: _Optional[str]=..., operations: _Optional[_Iterable[_Union[EnableOperation, _Mapping]]]=...) -> None:
        ...

class EnableOperation(_message.Message):
    __slots__ = ('campaign', 'auto_populate_brand_assets', 'brand_assets', 'final_uri_domain', 'main_color', 'accent_color', 'font_family')
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    AUTO_POPULATE_BRAND_ASSETS_FIELD_NUMBER: _ClassVar[int]
    BRAND_ASSETS_FIELD_NUMBER: _ClassVar[int]
    FINAL_URI_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    MAIN_COLOR_FIELD_NUMBER: _ClassVar[int]
    ACCENT_COLOR_FIELD_NUMBER: _ClassVar[int]
    FONT_FAMILY_FIELD_NUMBER: _ClassVar[int]
    campaign: str
    auto_populate_brand_assets: bool
    brand_assets: BrandCampaignAssets
    final_uri_domain: str
    main_color: str
    accent_color: str
    font_family: str

    def __init__(self, campaign: _Optional[str]=..., auto_populate_brand_assets: bool=..., brand_assets: _Optional[_Union[BrandCampaignAssets, _Mapping]]=..., final_uri_domain: _Optional[str]=..., main_color: _Optional[str]=..., accent_color: _Optional[str]=..., font_family: _Optional[str]=...) -> None:
        ...

class BrandCampaignAssets(_message.Message):
    __slots__ = ('business_name_asset', 'logo_asset', 'landscape_logo_asset')
    BUSINESS_NAME_ASSET_FIELD_NUMBER: _ClassVar[int]
    LOGO_ASSET_FIELD_NUMBER: _ClassVar[int]
    LANDSCAPE_LOGO_ASSET_FIELD_NUMBER: _ClassVar[int]
    business_name_asset: str
    logo_asset: _containers.RepeatedScalarFieldContainer[str]
    landscape_logo_asset: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, business_name_asset: _Optional[str]=..., logo_asset: _Optional[_Iterable[str]]=..., landscape_logo_asset: _Optional[_Iterable[str]]=...) -> None:
        ...

class EnablePMaxBrandGuidelinesResponse(_message.Message):
    __slots__ = ('results',)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[EnablementResult]

    def __init__(self, results: _Optional[_Iterable[_Union[EnablementResult, _Mapping]]]=...) -> None:
        ...

class EnablementResult(_message.Message):
    __slots__ = ('campaign', 'enablement_error')
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    ENABLEMENT_ERROR_FIELD_NUMBER: _ClassVar[int]
    campaign: str
    enablement_error: _status_pb2.Status

    def __init__(self, campaign: _Optional[str]=..., enablement_error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...