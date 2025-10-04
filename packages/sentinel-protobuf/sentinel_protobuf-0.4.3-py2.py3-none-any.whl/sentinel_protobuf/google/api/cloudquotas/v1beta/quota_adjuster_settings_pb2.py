"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/api/cloudquotas/v1beta/quota_adjuster_settings.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/api/cloudquotas/v1beta/quota_adjuster_settings.proto\x12\x1dgoogle.api.cloudquotas.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"i\n\x1fGetQuotaAdjusterSettingsRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0cloudquotas.googleapis.com/QuotaAdjusterSettings"\xd2\x01\n"UpdateQuotaAdjusterSettingsRequest\x12Z\n\x17quota_adjuster_settings\x18\x01 \x01(\x0b24.google.api.cloudquotas.v1beta.QuotaAdjusterSettingsB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12\x1a\n\rvalidate_only\x18\x03 \x01(\x08B\x03\xe0A\x01"\xf6\x04\n\x15QuotaAdjusterSettings\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12X\n\nenablement\x18\x02 \x01(\x0e2?.google.api.cloudquotas.v1beta.QuotaAdjusterSettings.EnablementB\x03\xe0A\x01\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x06 \x01(\tB\x03\xe0A\x01\x12\x16\n\tinherited\x18\x07 \x01(\x08B\x03\xe0A\x01\x12\x1b\n\x0einherited_from\x18\x08 \x01(\tB\x03\xe0A\x03"C\n\nEnablement\x12\x1a\n\x16ENABLEMENT_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x02\x12\x0c\n\x08DISABLED\x10\x03:\xac\x02\xeaA\xa8\x02\n0cloudquotas.googleapis.com/QuotaAdjusterSettings\x12=projects/{project}/locations/{location}/quotaAdjusterSettings\x12Gorganizations/{organization}/locations/{location}/quotaAdjusterSettings\x12;folders/{folder}/locations/{location}/quotaAdjusterSettings*\x15quotaAdjusterSettings2\x15quotaAdjusterSettingsR\x01\x012\xec\x07\n\x1cQuotaAdjusterSettingsManager\x12\x98\x04\n\x1bUpdateQuotaAdjusterSettings\x12A.google.api.cloudquotas.v1beta.UpdateQuotaAdjusterSettingsRequest\x1a4.google.api.cloudquotas.v1beta.QuotaAdjusterSettings"\xff\x02\xdaA#quota_adjuster_settings,update_mask\x82\xd3\xe4\x93\x02\xd2\x022S/v1beta/{quota_adjuster_settings.name=projects/*/locations/*/quotaAdjusterSettings}:\x17quota_adjuster_settingsZm2R/v1beta/{quota_adjuster_settings.name=folders/*/locations/*/quotaAdjusterSettings}:\x17quota_adjuster_settingsZs2X/v1beta/{quota_adjuster_settings.name=organizations/*/locations/*/quotaAdjusterSettings}:\x17quota_adjuster_settings\x12\xe0\x02\n\x18GetQuotaAdjusterSettings\x12>.google.api.cloudquotas.v1beta.GetQuotaAdjusterSettingsRequest\x1a4.google.api.cloudquotas.v1beta.QuotaAdjusterSettings"\xcd\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xbf\x01\x12;/v1beta/{name=projects/*/locations/*/quotaAdjusterSettings}Z<\x12:/v1beta/{name=folders/*/locations/*/quotaAdjusterSettings}ZB\x12@/v1beta/{name=organizations/*/locations/*/quotaAdjusterSettings}\x1aN\xcaA\x1acloudquotas.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf1\x01\n!com.google.api.cloudquotas.v1betaB\x1aQuotaAdjusterSettingsProtoP\x01ZEcloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb;cloudquotaspb\xaa\x02\x1fGoogle.Cloud.CloudQuotas.V1Beta\xca\x02\x1fGoogle\\Cloud\\CloudQuotas\\V1beta\xea\x02"Google::Cloud::CloudQuotas::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.cloudquotas.v1beta.quota_adjuster_settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.api.cloudquotas.v1betaB\x1aQuotaAdjusterSettingsProtoP\x01ZEcloud.google.com/go/cloudquotas/apiv1beta/cloudquotaspb;cloudquotaspb\xaa\x02\x1fGoogle.Cloud.CloudQuotas.V1Beta\xca\x02\x1fGoogle\\Cloud\\CloudQuotas\\V1beta\xea\x02"Google::Cloud::CloudQuotas::V1beta'
    _globals['_GETQUOTAADJUSTERSETTINGSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETQUOTAADJUSTERSETTINGSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0cloudquotas.googleapis.com/QuotaAdjusterSettings'
    _globals['_UPDATEQUOTAADJUSTERSETTINGSREQUEST'].fields_by_name['quota_adjuster_settings']._loaded_options = None
    _globals['_UPDATEQUOTAADJUSTERSETTINGSREQUEST'].fields_by_name['quota_adjuster_settings']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEQUOTAADJUSTERSETTINGSREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEQUOTAADJUSTERSETTINGSREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEQUOTAADJUSTERSETTINGSREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_UPDATEQUOTAADJUSTERSETTINGSREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_QUOTAADJUSTERSETTINGS'].fields_by_name['name']._loaded_options = None
    _globals['_QUOTAADJUSTERSETTINGS'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_QUOTAADJUSTERSETTINGS'].fields_by_name['enablement']._loaded_options = None
    _globals['_QUOTAADJUSTERSETTINGS'].fields_by_name['enablement']._serialized_options = b'\xe0A\x01'
    _globals['_QUOTAADJUSTERSETTINGS'].fields_by_name['update_time']._loaded_options = None
    _globals['_QUOTAADJUSTERSETTINGS'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_QUOTAADJUSTERSETTINGS'].fields_by_name['etag']._loaded_options = None
    _globals['_QUOTAADJUSTERSETTINGS'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_QUOTAADJUSTERSETTINGS'].fields_by_name['inherited']._loaded_options = None
    _globals['_QUOTAADJUSTERSETTINGS'].fields_by_name['inherited']._serialized_options = b'\xe0A\x01'
    _globals['_QUOTAADJUSTERSETTINGS'].fields_by_name['inherited_from']._loaded_options = None
    _globals['_QUOTAADJUSTERSETTINGS'].fields_by_name['inherited_from']._serialized_options = b'\xe0A\x03'
    _globals['_QUOTAADJUSTERSETTINGS']._loaded_options = None
    _globals['_QUOTAADJUSTERSETTINGS']._serialized_options = b'\xeaA\xa8\x02\n0cloudquotas.googleapis.com/QuotaAdjusterSettings\x12=projects/{project}/locations/{location}/quotaAdjusterSettings\x12Gorganizations/{organization}/locations/{location}/quotaAdjusterSettings\x12;folders/{folder}/locations/{location}/quotaAdjusterSettings*\x15quotaAdjusterSettings2\x15quotaAdjusterSettingsR\x01\x01'
    _globals['_QUOTAADJUSTERSETTINGSMANAGER']._loaded_options = None
    _globals['_QUOTAADJUSTERSETTINGSMANAGER']._serialized_options = b'\xcaA\x1acloudquotas.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_QUOTAADJUSTERSETTINGSMANAGER'].methods_by_name['UpdateQuotaAdjusterSettings']._loaded_options = None
    _globals['_QUOTAADJUSTERSETTINGSMANAGER'].methods_by_name['UpdateQuotaAdjusterSettings']._serialized_options = b'\xdaA#quota_adjuster_settings,update_mask\x82\xd3\xe4\x93\x02\xd2\x022S/v1beta/{quota_adjuster_settings.name=projects/*/locations/*/quotaAdjusterSettings}:\x17quota_adjuster_settingsZm2R/v1beta/{quota_adjuster_settings.name=folders/*/locations/*/quotaAdjusterSettings}:\x17quota_adjuster_settingsZs2X/v1beta/{quota_adjuster_settings.name=organizations/*/locations/*/quotaAdjusterSettings}:\x17quota_adjuster_settings'
    _globals['_QUOTAADJUSTERSETTINGSMANAGER'].methods_by_name['GetQuotaAdjusterSettings']._loaded_options = None
    _globals['_QUOTAADJUSTERSETTINGSMANAGER'].methods_by_name['GetQuotaAdjusterSettings']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xbf\x01\x12;/v1beta/{name=projects/*/locations/*/quotaAdjusterSettings}Z<\x12:/v1beta/{name=folders/*/locations/*/quotaAdjusterSettings}ZB\x12@/v1beta/{name=organizations/*/locations/*/quotaAdjusterSettings}'
    _globals['_GETQUOTAADJUSTERSETTINGSREQUEST']._serialized_start = 276
    _globals['_GETQUOTAADJUSTERSETTINGSREQUEST']._serialized_end = 381
    _globals['_UPDATEQUOTAADJUSTERSETTINGSREQUEST']._serialized_start = 384
    _globals['_UPDATEQUOTAADJUSTERSETTINGSREQUEST']._serialized_end = 594
    _globals['_QUOTAADJUSTERSETTINGS']._serialized_start = 597
    _globals['_QUOTAADJUSTERSETTINGS']._serialized_end = 1227
    _globals['_QUOTAADJUSTERSETTINGS_ENABLEMENT']._serialized_start = 857
    _globals['_QUOTAADJUSTERSETTINGS_ENABLEMENT']._serialized_end = 924
    _globals['_QUOTAADJUSTERSETTINGSMANAGER']._serialized_start = 1230
    _globals['_QUOTAADJUSTERSETTINGSMANAGER']._serialized_end = 2234