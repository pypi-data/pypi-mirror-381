"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/apps/drive/activity/v2/action.proto')
_sym_db = _symbol_database.Default()
from ......google.apps.drive.activity.v2 import actor_pb2 as google_dot_apps_dot_drive_dot_activity_dot_v2_dot_actor__pb2
from ......google.apps.drive.activity.v2 import common_pb2 as google_dot_apps_dot_drive_dot_activity_dot_v2_dot_common__pb2
from ......google.apps.drive.activity.v2 import target_pb2 as google_dot_apps_dot_drive_dot_activity_dot_v2_dot_target__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/apps/drive/activity/v2/action.proto\x12\x1dgoogle.apps.drive.activity.v2\x1a)google/apps/drive/activity/v2/actor.proto\x1a*google/apps/drive/activity/v2/common.proto\x1a*google/apps/drive/activity/v2/target.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xaa\x02\n\x06Action\x12;\n\x06detail\x18\x01 \x01(\x0b2+.google.apps.drive.activity.v2.ActionDetail\x123\n\x05actor\x18\x03 \x01(\x0b2$.google.apps.drive.activity.v2.Actor\x125\n\x06target\x18\x04 \x01(\x0b2%.google.apps.drive.activity.v2.Target\x12/\n\ttimestamp\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x12>\n\ntime_range\x18\x06 \x01(\x0b2(.google.apps.drive.activity.v2.TimeRangeH\x00B\x06\n\x04time"\xae\x06\n\x0cActionDetail\x127\n\x06create\x18\x01 \x01(\x0b2%.google.apps.drive.activity.v2.CreateH\x00\x123\n\x04edit\x18\x02 \x01(\x0b2#.google.apps.drive.activity.v2.EditH\x00\x123\n\x04move\x18\x03 \x01(\x0b2#.google.apps.drive.activity.v2.MoveH\x00\x127\n\x06rename\x18\x04 \x01(\x0b2%.google.apps.drive.activity.v2.RenameH\x00\x127\n\x06delete\x18\x05 \x01(\x0b2%.google.apps.drive.activity.v2.DeleteH\x00\x129\n\x07restore\x18\x06 \x01(\x0b2&.google.apps.drive.activity.v2.RestoreH\x00\x12L\n\x11permission_change\x18\x07 \x01(\x0b2/.google.apps.drive.activity.v2.PermissionChangeH\x00\x129\n\x07comment\x18\x08 \x01(\x0b2&.google.apps.drive.activity.v2.CommentH\x00\x12M\n\ndlp_change\x18\t \x01(\x0b27.google.apps.drive.activity.v2.DataLeakPreventionChangeH\x00\x12H\n\treference\x18\x0c \x01(\x0b23.google.apps.drive.activity.v2.ApplicationReferenceH\x00\x12H\n\x0fsettings_change\x18\r \x01(\x0b2-.google.apps.drive.activity.v2.SettingsChangeH\x00\x12Q\n\x14applied_label_change\x18\x13 \x01(\x0b21.google.apps.drive.activity.v2.AppliedLabelChangeH\x00B\x0f\n\raction_detail"\xaa\x02\n\x06Create\x128\n\x03new\x18\x01 \x01(\x0b2).google.apps.drive.activity.v2.Create.NewH\x00\x12>\n\x06upload\x18\x02 \x01(\x0b2,.google.apps.drive.activity.v2.Create.UploadH\x00\x12:\n\x04copy\x18\x03 \x01(\x0b2*.google.apps.drive.activity.v2.Create.CopyH\x00\x1a\x05\n\x03New\x1a\x08\n\x06Upload\x1aO\n\x04Copy\x12G\n\x0foriginal_object\x18\x01 \x01(\x0b2..google.apps.drive.activity.v2.TargetReferenceB\x08\n\x06origin"\x06\n\x04Edit"\x96\x01\n\x04Move\x12E\n\radded_parents\x18\x01 \x03(\x0b2..google.apps.drive.activity.v2.TargetReference\x12G\n\x0fremoved_parents\x18\x02 \x03(\x0b2..google.apps.drive.activity.v2.TargetReference".\n\x06Rename\x12\x11\n\told_title\x18\x01 \x01(\t\x12\x11\n\tnew_title\x18\x02 \x01(\t"\x81\x01\n\x06Delete\x128\n\x04type\x18\x01 \x01(\x0e2*.google.apps.drive.activity.v2.Delete.Type"=\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05TRASH\x10\x01\x12\x14\n\x10PERMANENT_DELETE\x10\x02"o\n\x07Restore\x129\n\x04type\x18\x01 \x01(\x0e2+.google.apps.drive.activity.v2.Restore.Type")\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07UNTRASH\x10\x01"\xa0\x01\n\x10PermissionChange\x12D\n\x11added_permissions\x18\x01 \x03(\x0b2).google.apps.drive.activity.v2.Permission\x12F\n\x13removed_permissions\x18\x02 \x03(\x0b2).google.apps.drive.activity.v2.Permission"\xe9\x03\n\nPermission\x12<\n\x04role\x18\x01 \x01(\x0e2..google.apps.drive.activity.v2.Permission.Role\x123\n\x04user\x18\x02 \x01(\x0b2#.google.apps.drive.activity.v2.UserH\x00\x125\n\x05group\x18\x03 \x01(\x0b2$.google.apps.drive.activity.v2.GroupH\x00\x127\n\x06domain\x18\x04 \x01(\x0b2%.google.apps.drive.activity.v2.DomainH\x00\x12B\n\x06anyone\x18\x05 \x01(\x0b20.google.apps.drive.activity.v2.Permission.AnyoneH\x00\x12\x17\n\x0fallow_discovery\x18\x06 \x01(\x08\x1a\x08\n\x06Anyone"\x87\x01\n\x04Role\x12\x14\n\x10ROLE_UNSPECIFIED\x10\x00\x12\t\n\x05OWNER\x10\x01\x12\r\n\tORGANIZER\x10\x02\x12\x12\n\x0eFILE_ORGANIZER\x10\x03\x12\n\n\x06EDITOR\x10\x04\x12\r\n\tCOMMENTER\x10\x05\x12\n\n\x06VIEWER\x10\x06\x12\x14\n\x10PUBLISHED_VIEWER\x10\x07B\x07\n\x05scope"\x8d\x08\n\x07Comment\x12;\n\x04post\x18\x01 \x01(\x0b2+.google.apps.drive.activity.v2.Comment.PostH\x00\x12G\n\nassignment\x18\x02 \x01(\x0b21.google.apps.drive.activity.v2.Comment.AssignmentH\x00\x12G\n\nsuggestion\x18\x03 \x01(\x0b21.google.apps.drive.activity.v2.Comment.SuggestionH\x00\x12<\n\x0fmentioned_users\x18\x07 \x03(\x0b2#.google.apps.drive.activity.v2.User\x1a\xc8\x01\n\x04Post\x12D\n\x07subtype\x18\x01 \x01(\x0e23.google.apps.drive.activity.v2.Comment.Post.Subtype"z\n\x07Subtype\x12\x17\n\x13SUBTYPE_UNSPECIFIED\x10\x00\x12\t\n\x05ADDED\x10\x01\x12\x0b\n\x07DELETED\x10\x02\x12\x0f\n\x0bREPLY_ADDED\x10\x03\x12\x11\n\rREPLY_DELETED\x10\x04\x12\x0c\n\x08RESOLVED\x10\x05\x12\x0c\n\x08REOPENED\x10\x06\x1a\xa1\x02\n\nAssignment\x12J\n\x07subtype\x18\x01 \x01(\x0e29.google.apps.drive.activity.v2.Comment.Assignment.Subtype\x12:\n\rassigned_user\x18\x07 \x01(\x0b2#.google.apps.drive.activity.v2.User"\x8a\x01\n\x07Subtype\x12\x17\n\x13SUBTYPE_UNSPECIFIED\x10\x00\x12\t\n\x05ADDED\x10\x01\x12\x0b\n\x07DELETED\x10\x02\x12\x0f\n\x0bREPLY_ADDED\x10\x03\x12\x11\n\rREPLY_DELETED\x10\x04\x12\x0c\n\x08RESOLVED\x10\x05\x12\x0c\n\x08REOPENED\x10\x06\x12\x0e\n\nREASSIGNED\x10\x07\x1a\xfd\x01\n\nSuggestion\x12J\n\x07subtype\x18\x01 \x01(\x0e29.google.apps.drive.activity.v2.Comment.Suggestion.Subtype"\xa2\x01\n\x07Subtype\x12\x17\n\x13SUBTYPE_UNSPECIFIED\x10\x00\x12\t\n\x05ADDED\x10\x01\x12\x0b\n\x07DELETED\x10\x02\x12\x0f\n\x0bREPLY_ADDED\x10\x03\x12\x11\n\rREPLY_DELETED\x10\x04\x12\x0c\n\x08ACCEPTED\x10\x07\x12\x0c\n\x08REJECTED\x10\x08\x12\x12\n\x0eACCEPT_DELETED\x10\t\x12\x12\n\x0eREJECT_DELETED\x10\nB\x06\n\x04type"\x9e\x01\n\x18DataLeakPreventionChange\x12J\n\x04type\x18\x01 \x01(\x0e2<.google.apps.drive.activity.v2.DataLeakPreventionChange.Type"6\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07FLAGGED\x10\x01\x12\x0b\n\x07CLEARED\x10\x02"\x9d\x01\n\x14ApplicationReference\x12F\n\x04type\x18\x01 \x01(\x0e28.google.apps.drive.activity.v2.ApplicationReference.Type"=\n\x04Type\x12\x1e\n\x1aUNSPECIFIED_REFERENCE_TYPE\x10\x00\x12\x08\n\x04LINK\x10\x01\x12\x0b\n\x07DISCUSS\x10\x02"\xc0\x04\n\x0eSettingsChange\x12\\\n\x13restriction_changes\x18\x01 \x03(\x0b2?.google.apps.drive.activity.v2.SettingsChange.RestrictionChange\x1a\xcf\x03\n\x11RestrictionChange\x12X\n\x07feature\x18\x01 \x01(\x0e2G.google.apps.drive.activity.v2.SettingsChange.RestrictionChange.Feature\x12d\n\x0fnew_restriction\x18\x02 \x01(\x0e2K.google.apps.drive.activity.v2.SettingsChange.RestrictionChange.Restriction"\xa5\x01\n\x07Feature\x12\x17\n\x13FEATURE_UNSPECIFIED\x10\x00\x12\x1a\n\x16SHARING_OUTSIDE_DOMAIN\x10\x01\x12\x12\n\x0eDIRECT_SHARING\x10\x02\x12\x14\n\x10ITEM_DUPLICATION\x10\x03\x12\x15\n\x11DRIVE_FILE_STREAM\x10\x04\x12$\n FILE_ORGANIZER_CAN_SHARE_FOLDERS\x10\x05"R\n\x0bRestriction\x12\x1b\n\x17RESTRICTION_UNSPECIFIED\x10\x00\x12\x10\n\x0cUNRESTRICTED\x10\x01\x12\x14\n\x10FULLY_RESTRICTED\x10\x02"\x8a\x15\n\x12AppliedLabelChange\x12[\n\x07changes\x18\x01 \x03(\x0b2J.google.apps.drive.activity.v2.AppliedLabelChange.AppliedLabelChangeDetail\x1a\x96\x14\n\x18AppliedLabelChangeDetail\x12\r\n\x05label\x18\x01 \x01(\t\x12^\n\x05types\x18\x02 \x03(\x0e2O.google.apps.drive.activity.v2.AppliedLabelChange.AppliedLabelChangeDetail.Type\x12\r\n\x05title\x18\x03 \x01(\t\x12r\n\rfield_changes\x18\x04 \x03(\x0b2[.google.apps.drive.activity.v2.AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange\x1a\x83\x11\n\x10FieldValueChange\x12\x15\n\x08field_id\x18\x01 \x01(\tH\x00\x88\x01\x01\x12~\n\told_value\x18\x02 \x01(\x0b2f.google.apps.drive.activity.v2.AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValueH\x01\x88\x01\x01\x12~\n\tnew_value\x18\x03 \x01(\x0b2f.google.apps.drive.activity.v2.AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValueH\x02\x88\x01\x01\x12\x19\n\x0cdisplay_name\x18\x04 \x01(\tH\x03\x88\x01\x01\x1a\x82\x0e\n\nFieldValue\x12{\n\x04text\x18\x01 \x01(\x0b2k.google.apps.drive.activity.v2.AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.TextH\x00\x12\x84\x01\n\ttext_list\x18\x03 \x01(\x0b2o.google.apps.drive.activity.v2.AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.TextListH\x00\x12\x85\x01\n\tselection\x18\x04 \x01(\x0b2p.google.apps.drive.activity.v2.AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.SelectionH\x00\x12\x8e\x01\n\x0eselection_list\x18\x05 \x01(\x0b2t.google.apps.drive.activity.v2.AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.SelectionListH\x00\x12\x81\x01\n\x07integer\x18\x06 \x01(\x0b2n.google.apps.drive.activity.v2.AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.IntegerH\x00\x12\x81\x01\n\x04user\x18\x07 \x01(\x0b2q.google.apps.drive.activity.v2.AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.SingleUserH\x00\x12\x84\x01\n\tuser_list\x18\x08 \x01(\x0b2o.google.apps.drive.activity.v2.AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.UserListH\x00\x12{\n\x04date\x18\t \x01(\x0b2k.google.apps.drive.activity.v2.AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.DateH\x00\x1a$\n\x04Text\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_value\x1a\x87\x01\n\x08TextList\x12{\n\x06values\x18\x01 \x03(\x0b2k.google.apps.drive.activity.v2.AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.Text\x1aU\n\tSelection\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tH\x01\x88\x01\x01B\x08\n\x06_valueB\x0f\n\r_display_name\x1a\x92\x01\n\rSelectionList\x12\x80\x01\n\x06values\x18\x01 \x03(\x0b2p.google.apps.drive.activity.v2.AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.Selection\x1a\'\n\x07Integer\x12\x12\n\x05value\x18\x01 \x01(\x03H\x00\x88\x01\x01B\x08\n\x06_value\x1a*\n\nSingleUser\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_value\x1a\x8e\x01\n\x08UserList\x12\x81\x01\n\x06values\x18\x01 \x03(\x0b2q.google.apps.drive.activity.v2.AppliedLabelChange.AppliedLabelChangeDetail.FieldValueChange.FieldValue.SingleUser\x1a@\n\x04Date\x12.\n\x05value\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x88\x01\x01B\x08\n\x06_valueB\x07\n\x05valueB\x0b\n\t_field_idB\x0c\n\n_old_valueB\x0c\n\n_new_valueB\x0f\n\r_display_name"\x81\x01\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bLABEL_ADDED\x10\x01\x12\x11\n\rLABEL_REMOVED\x10\x02\x12\x1d\n\x19LABEL_FIELD_VALUE_CHANGED\x10\x03\x12 \n\x1cLABEL_APPLIED_BY_ITEM_CREATE\x10\x04B\xc0\x01\n!com.google.apps.drive.activity.v2B\x0bActionProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/activity/v2;activity\xa2\x02\x04GADA\xaa\x02\x1dGoogle.Apps.Drive.Activity.V2\xca\x02\x1dGoogle\\Apps\\Drive\\Activity\\V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.drive.activity.v2.action_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.apps.drive.activity.v2B\x0bActionProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/activity/v2;activity\xa2\x02\x04GADA\xaa\x02\x1dGoogle.Apps.Drive.Activity.V2\xca\x02\x1dGoogle\\Apps\\Drive\\Activity\\V2'
    _globals['_ACTION']._serialized_start = 242
    _globals['_ACTION']._serialized_end = 540
    _globals['_ACTIONDETAIL']._serialized_start = 543
    _globals['_ACTIONDETAIL']._serialized_end = 1357
    _globals['_CREATE']._serialized_start = 1360
    _globals['_CREATE']._serialized_end = 1658
    _globals['_CREATE_NEW']._serialized_start = 1552
    _globals['_CREATE_NEW']._serialized_end = 1557
    _globals['_CREATE_UPLOAD']._serialized_start = 1559
    _globals['_CREATE_UPLOAD']._serialized_end = 1567
    _globals['_CREATE_COPY']._serialized_start = 1569
    _globals['_CREATE_COPY']._serialized_end = 1648
    _globals['_EDIT']._serialized_start = 1660
    _globals['_EDIT']._serialized_end = 1666
    _globals['_MOVE']._serialized_start = 1669
    _globals['_MOVE']._serialized_end = 1819
    _globals['_RENAME']._serialized_start = 1821
    _globals['_RENAME']._serialized_end = 1867
    _globals['_DELETE']._serialized_start = 1870
    _globals['_DELETE']._serialized_end = 1999
    _globals['_DELETE_TYPE']._serialized_start = 1938
    _globals['_DELETE_TYPE']._serialized_end = 1999
    _globals['_RESTORE']._serialized_start = 2001
    _globals['_RESTORE']._serialized_end = 2112
    _globals['_RESTORE_TYPE']._serialized_start = 2071
    _globals['_RESTORE_TYPE']._serialized_end = 2112
    _globals['_PERMISSIONCHANGE']._serialized_start = 2115
    _globals['_PERMISSIONCHANGE']._serialized_end = 2275
    _globals['_PERMISSION']._serialized_start = 2278
    _globals['_PERMISSION']._serialized_end = 2767
    _globals['_PERMISSION_ANYONE']._serialized_start = 2612
    _globals['_PERMISSION_ANYONE']._serialized_end = 2620
    _globals['_PERMISSION_ROLE']._serialized_start = 2623
    _globals['_PERMISSION_ROLE']._serialized_end = 2758
    _globals['_COMMENT']._serialized_start = 2770
    _globals['_COMMENT']._serialized_end = 3807
    _globals['_COMMENT_POST']._serialized_start = 3051
    _globals['_COMMENT_POST']._serialized_end = 3251
    _globals['_COMMENT_POST_SUBTYPE']._serialized_start = 3129
    _globals['_COMMENT_POST_SUBTYPE']._serialized_end = 3251
    _globals['_COMMENT_ASSIGNMENT']._serialized_start = 3254
    _globals['_COMMENT_ASSIGNMENT']._serialized_end = 3543
    _globals['_COMMENT_ASSIGNMENT_SUBTYPE']._serialized_start = 3405
    _globals['_COMMENT_ASSIGNMENT_SUBTYPE']._serialized_end = 3543
    _globals['_COMMENT_SUGGESTION']._serialized_start = 3546
    _globals['_COMMENT_SUGGESTION']._serialized_end = 3799
    _globals['_COMMENT_SUGGESTION_SUBTYPE']._serialized_start = 3637
    _globals['_COMMENT_SUGGESTION_SUBTYPE']._serialized_end = 3799
    _globals['_DATALEAKPREVENTIONCHANGE']._serialized_start = 3810
    _globals['_DATALEAKPREVENTIONCHANGE']._serialized_end = 3968
    _globals['_DATALEAKPREVENTIONCHANGE_TYPE']._serialized_start = 3914
    _globals['_DATALEAKPREVENTIONCHANGE_TYPE']._serialized_end = 3968
    _globals['_APPLICATIONREFERENCE']._serialized_start = 3971
    _globals['_APPLICATIONREFERENCE']._serialized_end = 4128
    _globals['_APPLICATIONREFERENCE_TYPE']._serialized_start = 4067
    _globals['_APPLICATIONREFERENCE_TYPE']._serialized_end = 4128
    _globals['_SETTINGSCHANGE']._serialized_start = 4131
    _globals['_SETTINGSCHANGE']._serialized_end = 4707
    _globals['_SETTINGSCHANGE_RESTRICTIONCHANGE']._serialized_start = 4244
    _globals['_SETTINGSCHANGE_RESTRICTIONCHANGE']._serialized_end = 4707
    _globals['_SETTINGSCHANGE_RESTRICTIONCHANGE_FEATURE']._serialized_start = 4458
    _globals['_SETTINGSCHANGE_RESTRICTIONCHANGE_FEATURE']._serialized_end = 4623
    _globals['_SETTINGSCHANGE_RESTRICTIONCHANGE_RESTRICTION']._serialized_start = 4625
    _globals['_SETTINGSCHANGE_RESTRICTIONCHANGE_RESTRICTION']._serialized_end = 4707
    _globals['_APPLIEDLABELCHANGE']._serialized_start = 4710
    _globals['_APPLIEDLABELCHANGE']._serialized_end = 7408
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL']._serialized_start = 4826
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL']._serialized_end = 7408
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_FIELDVALUECHANGE']._serialized_start = 5097
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_FIELDVALUECHANGE']._serialized_end = 7276
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_FIELDVALUECHANGE_FIELDVALUE']._serialized_start = 5424
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_FIELDVALUECHANGE_FIELDVALUE']._serialized_end = 7218
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_FIELDVALUECHANGE_FIELDVALUE_TEXT']._serialized_start = 6503
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_FIELDVALUECHANGE_FIELDVALUE_TEXT']._serialized_end = 6539
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_FIELDVALUECHANGE_FIELDVALUE_TEXTLIST']._serialized_start = 6542
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_FIELDVALUECHANGE_FIELDVALUE_TEXTLIST']._serialized_end = 6677
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_FIELDVALUECHANGE_FIELDVALUE_SELECTION']._serialized_start = 6679
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_FIELDVALUECHANGE_FIELDVALUE_SELECTION']._serialized_end = 6764
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_FIELDVALUECHANGE_FIELDVALUE_SELECTIONLIST']._serialized_start = 6767
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_FIELDVALUECHANGE_FIELDVALUE_SELECTIONLIST']._serialized_end = 6913
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_FIELDVALUECHANGE_FIELDVALUE_INTEGER']._serialized_start = 6915
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_FIELDVALUECHANGE_FIELDVALUE_INTEGER']._serialized_end = 6954
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_FIELDVALUECHANGE_FIELDVALUE_SINGLEUSER']._serialized_start = 6956
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_FIELDVALUECHANGE_FIELDVALUE_SINGLEUSER']._serialized_end = 6998
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_FIELDVALUECHANGE_FIELDVALUE_USERLIST']._serialized_start = 7001
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_FIELDVALUECHANGE_FIELDVALUE_USERLIST']._serialized_end = 7143
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_FIELDVALUECHANGE_FIELDVALUE_DATE']._serialized_start = 7145
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_FIELDVALUECHANGE_FIELDVALUE_DATE']._serialized_end = 7209
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_TYPE']._serialized_start = 7279
    _globals['_APPLIEDLABELCHANGE_APPLIEDLABELCHANGEDETAIL_TYPE']._serialized_end = 7408