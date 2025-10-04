"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/notifications/v1/notificationsapi.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/shopping/merchant/notifications/v1/notificationsapi.proto\x12)google.shopping.merchant.notifications.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"o\n"GetNotificationSubscriptionRequest\x12I\n\x04name\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\n3merchantapi.googleapis.com/NotificationSubscription"\xe1\x01\n%CreateNotificationSubscriptionRequest\x12K\n\x06parent\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\x123merchantapi.googleapis.com/NotificationSubscription\x12k\n\x19notification_subscription\x18\x02 \x01(\x0b2C.google.shopping.merchant.notifications.v1.NotificationSubscriptionB\x03\xe0A\x02"\xc5\x01\n%UpdateNotificationSubscriptionRequest\x12k\n\x19notification_subscription\x18\x01 \x01(\x0b2C.google.shopping.merchant.notifications.v1.NotificationSubscriptionB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"r\n%DeleteNotificationSubscriptionRequest\x12I\n\x04name\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\n3merchantapi.googleapis.com/NotificationSubscription"\x9a\x01\n$ListNotificationSubscriptionsRequest\x12K\n\x06parent\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\x123merchantapi.googleapis.com/NotificationSubscription\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\xa9\x01\n%ListNotificationSubscriptionsResponse\x12g\n\x1anotification_subscriptions\x18\x01 \x03(\x0b2C.google.shopping.merchant.notifications.v1.NotificationSubscription\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xe6\x03\n\x18NotificationSubscription\x12\x1e\n\x14all_managed_accounts\x18\x03 \x01(\x08H\x00\x12\x18\n\x0etarget_account\x18\x04 \x01(\tH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12s\n\x10registered_event\x18\x02 \x01(\x0e2Y.google.shopping.merchant.notifications.v1.NotificationSubscription.NotificationEventType\x12\x15\n\rcall_back_uri\x18\x05 \x01(\t"[\n\x15NotificationEventType\x12\'\n#NOTIFICATION_EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15PRODUCT_STATUS_CHANGE\x10\x01:\x82\x01\xeaA\x7f\n3merchantapi.googleapis.com/NotificationSubscription\x12Haccounts/{account}/notificationsubscriptions/{notification_subscription}B\x0f\n\rinterested_in"\x89\x01\n/GetNotificationSubscriptionHealthMetricsRequest\x12V\n\x04name\x18\x01 \x01(\tBH\xe0A\x02\xfaAB\n@merchantapi.googleapis.com/NotificationSubscriptionHealthMetrics"\xcd\x02\n%NotificationSubscriptionHealthMetrics\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x08\x12#\n\x1backnowledged_messages_count\x18\x02 \x01(\x03\x12"\n\x1aundelivered_messages_count\x18\x03 \x01(\x03\x122\n*oldest_unacknowledged_message_waiting_time\x18\x04 \x01(\x03:\x90\x01\xeaA\x8c\x01\n@merchantapi.googleapis.com/NotificationSubscriptionHealthMetrics\x12Haccounts/{account}/notificationsubscriptions/{notification_subscription}2\xb2\x0e\n\x17NotificationsApiService\x12\x81\x02\n\x1bGetNotificationSubscription\x12M.google.shopping.merchant.notifications.v1.GetNotificationSubscriptionRequest\x1aC.google.shopping.merchant.notifications.v1.NotificationSubscription"N\xdaA\x04name\x82\xd3\xe4\x93\x02A\x12?/notifications/v1/{name=accounts/*/notificationsubscriptions/*}\x12\xbf\x02\n\x1eCreateNotificationSubscription\x12P.google.shopping.merchant.notifications.v1.CreateNotificationSubscriptionRequest\x1aC.google.shopping.merchant.notifications.v1.NotificationSubscription"\x85\x01\xdaA parent,notification_subscription\x82\xd3\xe4\x93\x02\\"?/notifications/v1/{parent=accounts/*}/notificationsubscriptions:\x19notification_subscription\x12\xde\x02\n\x1eUpdateNotificationSubscription\x12P.google.shopping.merchant.notifications.v1.UpdateNotificationSubscriptionRequest\x1aC.google.shopping.merchant.notifications.v1.NotificationSubscription"\xa4\x01\xdaA%notification_subscription,update_mask\x82\xd3\xe4\x93\x02v2Y/notifications/v1/{notification_subscription.name=accounts/*/notificationsubscriptions/*}:\x19notification_subscription\x12\xda\x01\n\x1eDeleteNotificationSubscription\x12P.google.shopping.merchant.notifications.v1.DeleteNotificationSubscriptionRequest\x1a\x16.google.protobuf.Empty"N\xdaA\x04name\x82\xd3\xe4\x93\x02A*?/notifications/v1/{name=accounts/*/notificationsubscriptions/*}\x12\x94\x02\n\x1dListNotificationSubscriptions\x12O.google.shopping.merchant.notifications.v1.ListNotificationSubscriptionsRequest\x1aP.google.shopping.merchant.notifications.v1.ListNotificationSubscriptionsResponse"P\xdaA\x06parent\x82\xd3\xe4\x93\x02A\x12?/notifications/v1/{parent=accounts/*}/notificationsubscriptions\x12\xb2\x02\n(GetNotificationSubscriptionHealthMetrics\x12Z.google.shopping.merchant.notifications.v1.GetNotificationSubscriptionHealthMetricsRequest\x1aP.google.shopping.merchant.notifications.v1.NotificationSubscriptionHealthMetrics"X\xdaA\x04name\x82\xd3\xe4\x93\x02K\x12I/notifications/v1/{name=accounts/*/notificationsubscriptions/*}:getHealth\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xe6\x02\n-com.google.shopping.merchant.notifications.v1B\x15NotificationsApiProtoP\x01ZYcloud.google.com/go/shopping/merchant/notifications/apiv1/notificationspb;notificationspb\xaa\x02)Google.Shopping.Merchant.Notifications.V1\xca\x02)Google\\Shopping\\Merchant\\Notifications\\V1\xea\x02-Google::Shopping::Merchant::Notifications::V1\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.notifications.v1.notificationsapi_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n-com.google.shopping.merchant.notifications.v1B\x15NotificationsApiProtoP\x01ZYcloud.google.com/go/shopping/merchant/notifications/apiv1/notificationspb;notificationspb\xaa\x02)Google.Shopping.Merchant.Notifications.V1\xca\x02)Google\\Shopping\\Merchant\\Notifications\\V1\xea\x02-Google::Shopping::Merchant::Notifications::V1\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}'
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
    _globals['_GETNOTIFICATIONSUBSCRIPTIONHEALTHMETRICSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETNOTIFICATIONSUBSCRIPTIONHEALTHMETRICSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaAB\n@merchantapi.googleapis.com/NotificationSubscriptionHealthMetrics'
    _globals['_NOTIFICATIONSUBSCRIPTIONHEALTHMETRICS'].fields_by_name['name']._loaded_options = None
    _globals['_NOTIFICATIONSUBSCRIPTIONHEALTHMETRICS'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x08'
    _globals['_NOTIFICATIONSUBSCRIPTIONHEALTHMETRICS']._loaded_options = None
    _globals['_NOTIFICATIONSUBSCRIPTIONHEALTHMETRICS']._serialized_options = b'\xeaA\x8c\x01\n@merchantapi.googleapis.com/NotificationSubscriptionHealthMetrics\x12Haccounts/{account}/notificationsubscriptions/{notification_subscription}'
    _globals['_NOTIFICATIONSAPISERVICE']._loaded_options = None
    _globals['_NOTIFICATIONSAPISERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['GetNotificationSubscription']._loaded_options = None
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['GetNotificationSubscription']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02A\x12?/notifications/v1/{name=accounts/*/notificationsubscriptions/*}'
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['CreateNotificationSubscription']._loaded_options = None
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['CreateNotificationSubscription']._serialized_options = b'\xdaA parent,notification_subscription\x82\xd3\xe4\x93\x02\\"?/notifications/v1/{parent=accounts/*}/notificationsubscriptions:\x19notification_subscription'
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['UpdateNotificationSubscription']._loaded_options = None
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['UpdateNotificationSubscription']._serialized_options = b'\xdaA%notification_subscription,update_mask\x82\xd3\xe4\x93\x02v2Y/notifications/v1/{notification_subscription.name=accounts/*/notificationsubscriptions/*}:\x19notification_subscription'
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['DeleteNotificationSubscription']._loaded_options = None
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['DeleteNotificationSubscription']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02A*?/notifications/v1/{name=accounts/*/notificationsubscriptions/*}'
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['ListNotificationSubscriptions']._loaded_options = None
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['ListNotificationSubscriptions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02A\x12?/notifications/v1/{parent=accounts/*}/notificationsubscriptions'
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['GetNotificationSubscriptionHealthMetrics']._loaded_options = None
    _globals['_NOTIFICATIONSAPISERVICE'].methods_by_name['GetNotificationSubscriptionHealthMetrics']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02K\x12I/notifications/v1/{name=accounts/*/notificationsubscriptions/*}:getHealth'
    _globals['_GETNOTIFICATIONSUBSCRIPTIONREQUEST']._serialized_start = 289
    _globals['_GETNOTIFICATIONSUBSCRIPTIONREQUEST']._serialized_end = 400
    _globals['_CREATENOTIFICATIONSUBSCRIPTIONREQUEST']._serialized_start = 403
    _globals['_CREATENOTIFICATIONSUBSCRIPTIONREQUEST']._serialized_end = 628
    _globals['_UPDATENOTIFICATIONSUBSCRIPTIONREQUEST']._serialized_start = 631
    _globals['_UPDATENOTIFICATIONSUBSCRIPTIONREQUEST']._serialized_end = 828
    _globals['_DELETENOTIFICATIONSUBSCRIPTIONREQUEST']._serialized_start = 830
    _globals['_DELETENOTIFICATIONSUBSCRIPTIONREQUEST']._serialized_end = 944
    _globals['_LISTNOTIFICATIONSUBSCRIPTIONSREQUEST']._serialized_start = 947
    _globals['_LISTNOTIFICATIONSUBSCRIPTIONSREQUEST']._serialized_end = 1101
    _globals['_LISTNOTIFICATIONSUBSCRIPTIONSRESPONSE']._serialized_start = 1104
    _globals['_LISTNOTIFICATIONSUBSCRIPTIONSRESPONSE']._serialized_end = 1273
    _globals['_NOTIFICATIONSUBSCRIPTION']._serialized_start = 1276
    _globals['_NOTIFICATIONSUBSCRIPTION']._serialized_end = 1762
    _globals['_NOTIFICATIONSUBSCRIPTION_NOTIFICATIONEVENTTYPE']._serialized_start = 1521
    _globals['_NOTIFICATIONSUBSCRIPTION_NOTIFICATIONEVENTTYPE']._serialized_end = 1612
    _globals['_GETNOTIFICATIONSUBSCRIPTIONHEALTHMETRICSREQUEST']._serialized_start = 1765
    _globals['_GETNOTIFICATIONSUBSCRIPTIONHEALTHMETRICSREQUEST']._serialized_end = 1902
    _globals['_NOTIFICATIONSUBSCRIPTIONHEALTHMETRICS']._serialized_start = 1905
    _globals['_NOTIFICATIONSUBSCRIPTIONHEALTHMETRICS']._serialized_end = 2238
    _globals['_NOTIFICATIONSAPISERVICE']._serialized_start = 2241
    _globals['_NOTIFICATIONSAPISERVICE']._serialized_end = 4083