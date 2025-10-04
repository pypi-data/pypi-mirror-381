"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/notifications/v1beta/notificationsapi.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDgoogle/shopping/merchant/notifications/v1beta/notificationsapi.proto\x12-google.shopping.merchant.notifications.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a google/shopping/type/types.proto"o\n"GetNotificationSubscriptionRequest\x12I\n\x04name\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\n3merchantapi.googleapis.com/NotificationSubscription"\xe5\x01\n%CreateNotificationSubscriptionRequest\x12K\n\x06parent\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\x123merchantapi.googleapis.com/NotificationSubscription\x12o\n\x19notification_subscription\x18\x02 \x01(\x0b2G.google.shopping.merchant.notifications.v1beta.NotificationSubscriptionB\x03\xe0A\x02"\xc9\x01\n%UpdateNotificationSubscriptionRequest\x12o\n\x19notification_subscription\x18\x01 \x01(\x0b2G.google.shopping.merchant.notifications.v1beta.NotificationSubscriptionB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"r\n%DeleteNotificationSubscriptionRequest\x12I\n\x04name\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\n3merchantapi.googleapis.com/NotificationSubscription"\x9a\x01\n$ListNotificationSubscriptionsRequest\x12K\n\x06parent\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\x123merchantapi.googleapis.com/NotificationSubscription\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\xad\x01\n%ListNotificationSubscriptionsResponse\x12k\n\x1anotification_subscriptions\x18\x01 \x03(\x0b2G.google.shopping.merchant.notifications.v1beta.NotificationSubscription\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xea\x03\n\x18NotificationSubscription\x12\x1e\n\x14all_managed_accounts\x18\x03 \x01(\x08H\x00\x12\x18\n\x0etarget_account\x18\x04 \x01(\tH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12w\n\x10registered_event\x18\x02 \x01(\x0e2].google.shopping.merchant.notifications.v1beta.NotificationSubscription.NotificationEventType\x12\x15\n\rcall_back_uri\x18\x05 \x01(\t"[\n\x15NotificationEventType\x12\'\n#NOTIFICATION_EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15PRODUCT_STATUS_CHANGE\x10\x01:\x82\x01\xeaA\x7f\n3merchantapi.googleapis.com/NotificationSubscription\x12Haccounts/{account}/notificationsubscriptions/{notification_subscription}B\x0f\n\rinterested_in"\xf8\x01\n\rProductChange\x12\x16\n\told_value\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tnew_value\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x0bregion_code\x18\x03 \x01(\tH\x02\x88\x01\x01\x12[\n\x11reporting_context\x18\x04 \x01(\x0e2;.google.shopping.type.ReportingContext.ReportingContextEnumH\x03\x88\x01\x01B\x0c\n\n_old_valueB\x0c\n\n_new_valueB\x0e\n\x0c_region_codeB\x14\n\x12_reporting_context"\xd6\x03\n\x1aProductStatusChangeMessage\x12\x14\n\x07account\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1d\n\x10managing_account\x18\x02 \x01(\tH\x01\x88\x01\x01\x12S\n\rresource_type\x18\x03 \x01(\x0e27.google.shopping.merchant.notifications.v1beta.ResourceH\x02\x88\x01\x01\x12P\n\tattribute\x18\x04 \x01(\x0e28.google.shopping.merchant.notifications.v1beta.AttributeH\x03\x88\x01\x01\x12M\n\x07changes\x18\x05 \x03(\x0b2<.google.shopping.merchant.notifications.v1beta.ProductChange\x12\x18\n\x0bresource_id\x18\x06 \x01(\tH\x04\x88\x01\x01\x12\x15\n\x08resource\x18\x07 \x01(\tH\x05\x88\x01\x01B\n\n\x08_accountB\x13\n\x11_managing_accountB\x10\n\x0e_resource_typeB\x0c\n\n_attributeB\x0e\n\x0c_resource_idB\x0b\n\t_resource*1\n\x08Resource\x12\x18\n\x14RESOURCE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PRODUCT\x10\x01*2\n\tAttribute\x12\x19\n\x15ATTRIBUTE_UNSPECIFIED\x10\x00\x12\n\n\x06STATUS\x10\x012\xb5\x0c\n\x17NotificationsApiService\x12\x8d\x02\n\x1bGetNotificationSubscription\x12Q.google.shopping.merchant.notifications.v1beta.GetNotificationSubscriptionRequest\x1aG.google.shopping.merchant.notifications.v1beta.NotificationSubscription"R\xdaA\x04name\x82\xd3\xe4\x93\x02E\x12C/notifications/v1beta/{name=accounts/*/notificationsubscriptions/*}\x12\xcb\x02\n\x1eCreateNotificationSubscription\x12T.google.shopping.merchant.notifications.v1beta.CreateNotificationSubscriptionRequest\x1aG.google.shopping.merchant.notifications.v1beta.NotificationSubscription"\x89\x01\xdaA parent,notification_subscription\x82\xd3\xe4\x93\x02`"C/notifications/v1beta/{parent=accounts/*}/notificationsubscriptions:\x19notification_subscription\x12\xea\x02\n\x1eUpdateNotificationSubscription\x12T.google.shopping.merchant.notifications.v1beta.UpdateNotificationSubscriptionRequest\x1aG.google.shopping.merchant.notifications.v1beta.NotificationSubscription"\xa8\x01\xdaA%notification_subscription,update_mask\x82\xd3\xe4\x93\x02z2]/notifications/v1beta/{notification_subscription.name=accounts/*/notificationsubscriptions/*}:\x19notification_subscription\x12\xe2\x01\n\x1eDeleteNotificationSubscription\x12T.google.shopping.merchant.notifications.v1beta.DeleteNotificationSubscriptionRequest\x1a\x16.google.protobuf.Empty"R\xdaA\x04name\x82\xd3\xe4\x93\x02E*C/notifications/v1beta/{name=accounts/*/notificationsubscriptions/*}\x12\xa0\x02\n\x1dListNotificationSubscriptions\x12S.google.shopping.merchant.notifications.v1beta.ListNotificationSubscriptionsRequest\x1aT.google.shopping.merchant.notifications.v1beta.ListNotificationSubscriptionsResponse"T\xdaA\x06parent\x82\xd3\xe4\x93\x02E\x12C/notifications/v1beta/{parent=accounts/*}/notificationsubscriptions\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xe6\x01\n1com.google.shopping.merchant.notifications.v1betaB\x15NotificationsApiProtoP\x01Z]cloud.google.com/go/shopping/merchant/notifications/apiv1beta/notificationspb;notificationspb\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.notifications.v1beta.notificationsapi_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n1com.google.shopping.merchant.notifications.v1betaB\x15NotificationsApiProtoP\x01Z]cloud.google.com/go/shopping/merchant/notifications/apiv1beta/notificationspb;notificationspb\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}'
    _globals['_GETNOTIFICATIONSUBSCRIPTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETNOTIFICATIONSUBSCRIPTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA5\n3merchantapi.googleapis.com/NotificationSubscription'
    _globals['_CREATENOTIFICATIONSUBSCRIPTIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATENOTIFICATIONSUBSCRIPTIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA5\x123merchantapi.googleapis.com/NotificationSubscription'
    _globals['_CREATENOTIFICATIONSUBSCRIPTIONREQUEST'].fields_by_name['notification_subscription']._loaded_options = None
    _globals['_CREATENOTIFICATIONSUBSCRIPTIONREQUEST'].fields_by_name['notification_subscription']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATENOTIFICATIONSUBSCRIPTIONREQUEST'].fields_by_name['notification_subscription']._loaded_options = None
    _globals['_UPDATENOTIFICATIONSUBSCRIPTIONREQUEST'].fields_by_name['notification_subscription']._serialized_options = b'\xe0A\x02'
    _globals['_DELETENOTIFICATIONSUBSCRIPTIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETENOTIFICATIONSUBSCRIPTIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA5\n3merchantapi.googleapis.com/NotificationSubscription'
    _globals['_LISTNOTIFICATIONSUBSCRIPTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTNOTIFICATIONSUBSCRIPTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA5\x123merchantapi.googleapis.com/NotificationSubscription'
    _globals['_NOTIFICATIONSUBSCRIPTION'].fields_by_name['name']._loaded_options = None
    _globals['_NOTIFICATIONSUBSCRIPTION'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_NOTIFICATIONSUBSCRIPTION']._loaded_options = None
    _globals['_NOTIFICATIONSUBSCRIPTION']._serialized_options = b'\xeaA\x7f\n3merchantapi.googleapis.com/NotificationSubscription\x12Haccounts/{account}/notificationsubscriptions/{notification_subscription}'
    _globals['_NOTIFICATIONSAPISERVICE']._loaded_options = None
    _globals['_NOTIFICATIONSAPISERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['GetNotificationSubscription']._loaded_options = None
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['GetNotificationSubscription']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02E\x12C/notifications/v1beta/{name=accounts/*/notificationsubscriptions/*}'
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['CreateNotificationSubscription']._loaded_options = None
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['CreateNotificationSubscription']._serialized_options = b'\xdaA parent,notification_subscription\x82\xd3\xe4\x93\x02`"C/notifications/v1beta/{parent=accounts/*}/notificationsubscriptions:\x19notification_subscription'
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['UpdateNotificationSubscription']._loaded_options = None
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['UpdateNotificationSubscription']._serialized_options = b'\xdaA%notification_subscription,update_mask\x82\xd3\xe4\x93\x02z2]/notifications/v1beta/{notification_subscription.name=accounts/*/notificationsubscriptions/*}:\x19notification_subscription'
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['DeleteNotificationSubscription']._loaded_options = None
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['DeleteNotificationSubscription']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02E*C/notifications/v1beta/{name=accounts/*/notificationsubscriptions/*}'
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['ListNotificationSubscriptions']._loaded_options = None
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['ListNotificationSubscriptions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02E\x12C/notifications/v1beta/{parent=accounts/*}/notificationsubscriptions'
    _globals['_RESOURCE']._serialized_start = 2546
    _globals['_RESOURCE']._serialized_end = 2595
    _globals['_ATTRIBUTE']._serialized_start = 2597
    _globals['_ATTRIBUTE']._serialized_end = 2647
    _globals['_GETNOTIFICATIONSUBSCRIPTIONREQUEST']._serialized_start = 331
    _globals['_GETNOTIFICATIONSUBSCRIPTIONREQUEST']._serialized_end = 442
    _globals['_CREATENOTIFICATIONSUBSCRIPTIONREQUEST']._serialized_start = 445
    _globals['_CREATENOTIFICATIONSUBSCRIPTIONREQUEST']._serialized_end = 674
    _globals['_UPDATENOTIFICATIONSUBSCRIPTIONREQUEST']._serialized_start = 677
    _globals['_UPDATENOTIFICATIONSUBSCRIPTIONREQUEST']._serialized_end = 878
    _globals['_DELETENOTIFICATIONSUBSCRIPTIONREQUEST']._serialized_start = 880
    _globals['_DELETENOTIFICATIONSUBSCRIPTIONREQUEST']._serialized_end = 994
    _globals['_LISTNOTIFICATIONSUBSCRIPTIONSREQUEST']._serialized_start = 997
    _globals['_LISTNOTIFICATIONSUBSCRIPTIONSREQUEST']._serialized_end = 1151
    _globals['_LISTNOTIFICATIONSUBSCRIPTIONSRESPONSE']._serialized_start = 1154
    _globals['_LISTNOTIFICATIONSUBSCRIPTIONSRESPONSE']._serialized_end = 1327
    _globals['_NOTIFICATIONSUBSCRIPTION']._serialized_start = 1330
    _globals['_NOTIFICATIONSUBSCRIPTION']._serialized_end = 1820
    _globals['_NOTIFICATIONSUBSCRIPTION_NOTIFICATIONEVENTTYPE']._serialized_start = 1579
    _globals['_NOTIFICATIONSUBSCRIPTION_NOTIFICATIONEVENTTYPE']._serialized_end = 1670
    _globals['_PRODUCTCHANGE']._serialized_start = 1823
    _globals['_PRODUCTCHANGE']._serialized_end = 2071
    _globals['_PRODUCTSTATUSCHANGEMESSAGE']._serialized_start = 2074
    _globals['_PRODUCTSTATUSCHANGEMESSAGE']._serialized_end = 2544
    _globals['_NOTIFICATIONSAPISERVICE']._serialized_start = 2650
    _globals['_NOTIFICATIONSAPISERVICE']._serialized_end = 4239