"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2beta/serving_config_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2beta import serving_config_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_serving__config__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/retail/v2beta/serving_config_service.proto\x12\x1agoogle.cloud.retail.v2beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/retail/v2beta/serving_config.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xbb\x01\n\x1aCreateServingConfigRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12F\n\x0eserving_config\x18\x02 \x01(\x0b2).google.cloud.retail.v2beta.ServingConfigB\x03\xe0A\x02\x12\x1e\n\x11serving_config_id\x18\x03 \x01(\tB\x03\xe0A\x02"\x95\x01\n\x1aUpdateServingConfigRequest\x12F\n\x0eserving_config\x18\x01 \x01(\x0b2).google.cloud.retail.v2beta.ServingConfigB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"W\n\x1aDeleteServingConfigRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#retail.googleapis.com/ServingConfig"T\n\x17GetServingConfigRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#retail.googleapis.com/ServingConfig"\x83\x01\n\x19ListServingConfigsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"y\n\x1aListServingConfigsResponse\x12B\n\x0fserving_configs\x18\x01 \x03(\x0b2).google.cloud.retail.v2beta.ServingConfig\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"q\n\x11AddControlRequest\x12C\n\x0eserving_config\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#retail.googleapis.com/ServingConfig\x12\x17\n\ncontrol_id\x18\x02 \x01(\tB\x03\xe0A\x02"t\n\x14RemoveControlRequest\x12C\n\x0eserving_config\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#retail.googleapis.com/ServingConfig\x12\x17\n\ncontrol_id\x18\x02 \x01(\tB\x03\xe0A\x022\x83\r\n\x14ServingConfigService\x12\xfe\x01\n\x13CreateServingConfig\x126.google.cloud.retail.v2beta.CreateServingConfigRequest\x1a).google.cloud.retail.v2beta.ServingConfig"\x83\x01\xdaA\'parent,serving_config,serving_config_id\x82\xd3\xe4\x93\x02S"A/v2beta/{parent=projects/*/locations/*/catalogs/*}/servingConfigs:\x0eserving_config\x12\xb7\x01\n\x13DeleteServingConfig\x126.google.cloud.retail.v2beta.DeleteServingConfigRequest\x1a\x16.google.protobuf.Empty"P\xdaA\x04name\x82\xd3\xe4\x93\x02C*A/v2beta/{name=projects/*/locations/*/catalogs/*/servingConfigs/*}\x12\x80\x02\n\x13UpdateServingConfig\x126.google.cloud.retail.v2beta.UpdateServingConfigRequest\x1a).google.cloud.retail.v2beta.ServingConfig"\x85\x01\xdaA\x1aserving_config,update_mask\x82\xd3\xe4\x93\x02b2P/v2beta/{serving_config.name=projects/*/locations/*/catalogs/*/servingConfigs/*}:\x0eserving_config\x12\xc4\x01\n\x10GetServingConfig\x123.google.cloud.retail.v2beta.GetServingConfigRequest\x1a).google.cloud.retail.v2beta.ServingConfig"P\xdaA\x04name\x82\xd3\xe4\x93\x02C\x12A/v2beta/{name=projects/*/locations/*/catalogs/*/servingConfigs/*}\x12\xd7\x01\n\x12ListServingConfigs\x125.google.cloud.retail.v2beta.ListServingConfigsRequest\x1a6.google.cloud.retail.v2beta.ListServingConfigsResponse"R\xdaA\x06parent\x82\xd3\xe4\x93\x02C\x12A/v2beta/{parent=projects/*/locations/*/catalogs/*}/servingConfigs\x12\xda\x01\n\nAddControl\x12-.google.cloud.retail.v2beta.AddControlRequest\x1a).google.cloud.retail.v2beta.ServingConfig"r\xdaA\x0eserving_config\x82\xd3\xe4\x93\x02["V/v2beta/{serving_config=projects/*/locations/*/catalogs/*/servingConfigs/*}:addControl:\x01*\x12\xe3\x01\n\rRemoveControl\x120.google.cloud.retail.v2beta.RemoveControlRequest\x1a).google.cloud.retail.v2beta.ServingConfig"u\xdaA\x0eserving_config\x82\xd3\xe4\x93\x02^"Y/v2beta/{serving_config=projects/*/locations/*/catalogs/*/servingConfigs/*}:removeControl:\x01*\x1aI\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd8\x01\n\x1ecom.google.cloud.retail.v2betaB\x19ServingConfigServiceProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2beta.serving_config_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.retail.v2betaB\x19ServingConfigServiceProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2beta'
    _globals['_CREATESERVINGCONFIGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESERVINGCONFIGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_CREATESERVINGCONFIGREQUEST'].fields_by_name['serving_config']._loaded_options = None
    _globals['_CREATESERVINGCONFIGREQUEST'].fields_by_name['serving_config']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESERVINGCONFIGREQUEST'].fields_by_name['serving_config_id']._loaded_options = None
    _globals['_CREATESERVINGCONFIGREQUEST'].fields_by_name['serving_config_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESERVINGCONFIGREQUEST'].fields_by_name['serving_config']._loaded_options = None
    _globals['_UPDATESERVINGCONFIGREQUEST'].fields_by_name['serving_config']._serialized_options = b'\xe0A\x02'
    _globals['_DELETESERVINGCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESERVINGCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#retail.googleapis.com/ServingConfig'
    _globals['_GETSERVINGCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSERVINGCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#retail.googleapis.com/ServingConfig'
    _globals['_LISTSERVINGCONFIGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSERVINGCONFIGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dretail.googleapis.com/Catalog'
    _globals['_LISTSERVINGCONFIGSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTSERVINGCONFIGSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSERVINGCONFIGSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTSERVINGCONFIGSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_ADDCONTROLREQUEST'].fields_by_name['serving_config']._loaded_options = None
    _globals['_ADDCONTROLREQUEST'].fields_by_name['serving_config']._serialized_options = b'\xe0A\x02\xfaA%\n#retail.googleapis.com/ServingConfig'
    _globals['_ADDCONTROLREQUEST'].fields_by_name['control_id']._loaded_options = None
    _globals['_ADDCONTROLREQUEST'].fields_by_name['control_id']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVECONTROLREQUEST'].fields_by_name['serving_config']._loaded_options = None
    _globals['_REMOVECONTROLREQUEST'].fields_by_name['serving_config']._serialized_options = b'\xe0A\x02\xfaA%\n#retail.googleapis.com/ServingConfig'
    _globals['_REMOVECONTROLREQUEST'].fields_by_name['control_id']._loaded_options = None
    _globals['_REMOVECONTROLREQUEST'].fields_by_name['control_id']._serialized_options = b'\xe0A\x02'
    _globals['_SERVINGCONFIGSERVICE']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE']._serialized_options = b'\xcaA\x15retail.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['CreateServingConfig']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['CreateServingConfig']._serialized_options = b'\xdaA\'parent,serving_config,serving_config_id\x82\xd3\xe4\x93\x02S"A/v2beta/{parent=projects/*/locations/*/catalogs/*}/servingConfigs:\x0eserving_config'
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['DeleteServingConfig']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['DeleteServingConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02C*A/v2beta/{name=projects/*/locations/*/catalogs/*/servingConfigs/*}'
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['UpdateServingConfig']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['UpdateServingConfig']._serialized_options = b'\xdaA\x1aserving_config,update_mask\x82\xd3\xe4\x93\x02b2P/v2beta/{serving_config.name=projects/*/locations/*/catalogs/*/servingConfigs/*}:\x0eserving_config'
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['GetServingConfig']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['GetServingConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02C\x12A/v2beta/{name=projects/*/locations/*/catalogs/*/servingConfigs/*}'
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['ListServingConfigs']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['ListServingConfigs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02C\x12A/v2beta/{parent=projects/*/locations/*/catalogs/*}/servingConfigs'
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['AddControl']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['AddControl']._serialized_options = b'\xdaA\x0eserving_config\x82\xd3\xe4\x93\x02["V/v2beta/{serving_config=projects/*/locations/*/catalogs/*/servingConfigs/*}:addControl:\x01*'
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['RemoveControl']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['RemoveControl']._serialized_options = b'\xdaA\x0eserving_config\x82\xd3\xe4\x93\x02^"Y/v2beta/{serving_config=projects/*/locations/*/catalogs/*/servingConfigs/*}:removeControl:\x01*'
    _globals['_CREATESERVINGCONFIGREQUEST']._serialized_start = 315
    _globals['_CREATESERVINGCONFIGREQUEST']._serialized_end = 502
    _globals['_UPDATESERVINGCONFIGREQUEST']._serialized_start = 505
    _globals['_UPDATESERVINGCONFIGREQUEST']._serialized_end = 654
    _globals['_DELETESERVINGCONFIGREQUEST']._serialized_start = 656
    _globals['_DELETESERVINGCONFIGREQUEST']._serialized_end = 743
    _globals['_GETSERVINGCONFIGREQUEST']._serialized_start = 745
    _globals['_GETSERVINGCONFIGREQUEST']._serialized_end = 829
    _globals['_LISTSERVINGCONFIGSREQUEST']._serialized_start = 832
    _globals['_LISTSERVINGCONFIGSREQUEST']._serialized_end = 963
    _globals['_LISTSERVINGCONFIGSRESPONSE']._serialized_start = 965
    _globals['_LISTSERVINGCONFIGSRESPONSE']._serialized_end = 1086
    _globals['_ADDCONTROLREQUEST']._serialized_start = 1088
    _globals['_ADDCONTROLREQUEST']._serialized_end = 1201
    _globals['_REMOVECONTROLREQUEST']._serialized_start = 1203
    _globals['_REMOVECONTROLREQUEST']._serialized_end = 1319
    _globals['_SERVINGCONFIGSERVICE']._serialized_start = 1322
    _globals['_SERVINGCONFIGSERVICE']._serialized_end = 2989