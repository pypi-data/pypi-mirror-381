"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/visionai/v1/annotations.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/visionai/v1/annotations.proto\x12\x18google.cloud.visionai.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x95\r\n*PersonalProtectiveEquipmentDetectionOutput\x120\n\x0ccurrent_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12m\n\x10detected_persons\x18\x02 \x03(\x0b2S.google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.DetectedPerson\x1a(\n\x0cPersonEntity\x12\x18\n\x10person_entity_id\x18\x01 \x01(\x03\x1az\n\tPPEEntity\x12\x14\n\x0cppe_label_id\x18\x01 \x01(\x03\x12\x18\n\x10ppe_label_string\x18\x02 \x01(\t\x12&\n\x1eppe_supercategory_label_string\x18\x03 \x01(\t\x12\x15\n\rppe_entity_id\x18\x04 \x01(\x03\x1aR\n\x15NormalizedBoundingBox\x12\x0c\n\x04xmin\x18\x01 \x01(\x02\x12\x0c\n\x04ymin\x18\x02 \x01(\x02\x12\r\n\x05width\x18\x03 \x01(\x02\x12\x0e\n\x06height\x18\x04 \x01(\x02\x1a\xa6\x02\n\x13PersonIdentifiedBox\x12\x0e\n\x06box_id\x18\x01 \x01(\x03\x12{\n\x17normalized_bounding_box\x18\x02 \x01(\x0b2Z.google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.NormalizedBoundingBox\x12\x18\n\x10confidence_score\x18\x03 \x01(\x02\x12h\n\rperson_entity\x18\x04 \x01(\x0b2Q.google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.PersonEntity\x1a\x9d\x02\n\x10PPEIdentifiedBox\x12\x0e\n\x06box_id\x18\x01 \x01(\x03\x12{\n\x17normalized_bounding_box\x18\x02 \x01(\x0b2Z.google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.NormalizedBoundingBox\x12\x18\n\x10confidence_score\x18\x03 \x01(\x02\x12b\n\nppe_entity\x18\x04 \x01(\x0b2N.google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.PPEEntity\x1a\x82\x05\n\x0eDetectedPerson\x12\x11\n\tperson_id\x18\x01 \x01(\x03\x12\x80\x01\n\x1edetected_person_identified_box\x18\x02 \x01(\x0b2X.google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.PersonIdentifiedBox\x12|\n\x1ddetected_ppe_identified_boxes\x18\x03 \x03(\x0b2U.google.cloud.visionai.v1.PersonalProtectiveEquipmentDetectionOutput.PPEIdentifiedBox\x12 \n\x13face_coverage_score\x18\x04 \x01(\x02H\x00\x88\x01\x01\x12 \n\x13eyes_coverage_score\x18\x05 \x01(\x02H\x01\x88\x01\x01\x12 \n\x13head_coverage_score\x18\x06 \x01(\x02H\x02\x88\x01\x01\x12!\n\x14hands_coverage_score\x18\x07 \x01(\x02H\x03\x88\x01\x01\x12 \n\x13body_coverage_score\x18\x08 \x01(\x02H\x04\x88\x01\x01\x12 \n\x13feet_coverage_score\x18\t \x01(\x02H\x05\x88\x01\x01B\x16\n\x14_face_coverage_scoreB\x16\n\x14_eyes_coverage_scoreB\x16\n\x14_head_coverage_scoreB\x17\n\x15_hands_coverage_scoreB\x16\n\x14_body_coverage_scoreB\x16\n\x14_feet_coverage_score"\xca\x04\n\x1fObjectDetectionPredictionResult\x120\n\x0ccurrent_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12a\n\x10identified_boxes\x18\x02 \x03(\x0b2G.google.cloud.visionai.v1.ObjectDetectionPredictionResult.IdentifiedBox\x1a0\n\x06Entity\x12\x10\n\x08label_id\x18\x01 \x01(\x03\x12\x14\n\x0clabel_string\x18\x02 \x01(\t\x1a\xdf\x02\n\rIdentifiedBox\x12\x0e\n\x06box_id\x18\x01 \x01(\x03\x12~\n\x17normalized_bounding_box\x18\x02 \x01(\x0b2].google.cloud.visionai.v1.ObjectDetectionPredictionResult.IdentifiedBox.NormalizedBoundingBox\x12\x18\n\x10confidence_score\x18\x03 \x01(\x02\x12P\n\x06entity\x18\x04 \x01(\x0b2@.google.cloud.visionai.v1.ObjectDetectionPredictionResult.Entity\x1aR\n\x15NormalizedBoundingBox\x12\x0c\n\x04xmin\x18\x01 \x01(\x02\x12\x0c\n\x04ymin\x18\x02 \x01(\x02\x12\r\n\x05width\x18\x03 \x01(\x02\x12\x0e\n\x06height\x18\x04 \x01(\x02"\x8b\x01\n$ImageObjectDetectionPredictionResult\x12\x0b\n\x03ids\x18\x01 \x03(\x03\x12\x15\n\rdisplay_names\x18\x02 \x03(\t\x12\x13\n\x0bconfidences\x18\x03 \x03(\x02\x12*\n\x06bboxes\x18\x04 \x03(\x0b2\x1a.google.protobuf.ListValue"Y\n\x1eClassificationPredictionResult\x12\x0b\n\x03ids\x18\x01 \x03(\x03\x12\x15\n\rdisplay_names\x18\x02 \x03(\t\x12\x13\n\x0bconfidences\x18\x03 \x03(\x02"S\n!ImageSegmentationPredictionResult\x12\x15\n\rcategory_mask\x18\x01 \x01(\t\x12\x17\n\x0fconfidence_mask\x18\x02 \x01(\t"\xc4\x02\n&VideoActionRecognitionPredictionResult\x126\n\x12segment_start_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x10segment_end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12b\n\x07actions\x18\x03 \x03(\x0b2Q.google.cloud.visionai.v1.VideoActionRecognitionPredictionResult.IdentifiedAction\x1aH\n\x10IdentifiedAction\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x12\n\nconfidence\x18\x03 \x01(\x02"\xf9\x03\n#VideoObjectTrackingPredictionResult\x126\n\x12segment_start_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x10segment_end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12]\n\x07objects\x18\x03 \x03(\x0b2L.google.cloud.visionai.v1.VideoObjectTrackingPredictionResult.DetectedObject\x1aI\n\x0bBoundingBox\x12\r\n\x05x_min\x18\x01 \x01(\x02\x12\r\n\x05x_max\x18\x02 \x01(\x02\x12\r\n\x05y_min\x18\x03 \x01(\x02\x12\r\n\x05y_max\x18\x04 \x01(\x02\x1a\xb9\x01\n\x0eDetectedObject\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12_\n\x0cbounding_box\x18\x03 \x01(\x0b2I.google.cloud.visionai.v1.VideoObjectTrackingPredictionResult.BoundingBox\x12\x12\n\nconfidence\x18\x04 \x01(\x02\x12\x10\n\x08track_id\x18\x05 \x01(\x03"\xd6\x02\n#VideoClassificationPredictionResult\x126\n\x12segment_start_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x10segment_end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12o\n\x0fclassifications\x18\x03 \x03(\x0b2V.google.cloud.visionai.v1.VideoClassificationPredictionResult.IdentifiedClassification\x1aP\n\x18IdentifiedClassification\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x12\n\nconfidence\x18\x03 \x01(\x02"\xeb\x13\n!OccupancyCountingPredictionResult\x120\n\x0ccurrent_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12c\n\x10identified_boxes\x18\x02 \x03(\x0b2I.google.cloud.visionai.v1.OccupancyCountingPredictionResult.IdentifiedBox\x12P\n\x05stats\x18\x03 \x01(\x0b2A.google.cloud.visionai.v1.OccupancyCountingPredictionResult.Stats\x12Y\n\ntrack_info\x18\x04 \x03(\x0b2E.google.cloud.visionai.v1.OccupancyCountingPredictionResult.TrackInfo\x12b\n\x0fdwell_time_info\x18\x05 \x03(\x0b2I.google.cloud.visionai.v1.OccupancyCountingPredictionResult.DwellTimeInfo\x12\x10\n\x03pts\x18\x06 \x01(\x03H\x00\x88\x01\x01\x1a0\n\x06Entity\x12\x10\n\x08label_id\x18\x01 \x01(\x03\x12\x14\n\x0clabel_string\x18\x02 \x01(\t\x1a\xeb\x02\n\rIdentifiedBox\x12\x0e\n\x06box_id\x18\x01 \x01(\x03\x12\x80\x01\n\x17normalized_bounding_box\x18\x02 \x01(\x0b2_.google.cloud.visionai.v1.OccupancyCountingPredictionResult.IdentifiedBox.NormalizedBoundingBox\x12\r\n\x05score\x18\x03 \x01(\x02\x12R\n\x06entity\x18\x04 \x01(\x0b2B.google.cloud.visionai.v1.OccupancyCountingPredictionResult.Entity\x12\x10\n\x08track_id\x18\x05 \x01(\x03\x1aR\n\x15NormalizedBoundingBox\x12\x0c\n\x04xmin\x18\x01 \x01(\x02\x12\x0c\n\x04ymin\x18\x02 \x01(\x02\x12\r\n\x05width\x18\x03 \x01(\x02\x12\x0e\n\x06height\x18\x04 \x01(\x02\x1a\xf5\n\n\x05Stats\x12g\n\x10full_frame_count\x18\x01 \x03(\x0b2M.google.cloud.visionai.v1.OccupancyCountingPredictionResult.Stats.ObjectCount\x12q\n\x14crossing_line_counts\x18\x02 \x03(\x0b2S.google.cloud.visionai.v1.OccupancyCountingPredictionResult.Stats.CrossingLineCount\x12m\n\x12active_zone_counts\x18\x03 \x03(\x0b2Q.google.cloud.visionai.v1.OccupancyCountingPredictionResult.Stats.ActiveZoneCount\x1ap\n\x0bObjectCount\x12R\n\x06entity\x18\x01 \x01(\x0b2B.google.cloud.visionai.v1.OccupancyCountingPredictionResult.Entity\x12\r\n\x05count\x18\x02 \x01(\x05\x1a\xad\x01\n\x16AccumulatedObjectCount\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12c\n\x0cobject_count\x18\x02 \x01(\x0b2M.google.cloud.visionai.v1.OccupancyCountingPredictionResult.Stats.ObjectCount\x1a\xcb\x04\n\x11CrossingLineCount\x12>\n\nannotation\x18\x01 \x01(\x0b2*.google.cloud.visionai.v1.StreamAnnotation\x12p\n\x19positive_direction_counts\x18\x02 \x03(\x0b2M.google.cloud.visionai.v1.OccupancyCountingPredictionResult.Stats.ObjectCount\x12p\n\x19negative_direction_counts\x18\x03 \x03(\x0b2M.google.cloud.visionai.v1.OccupancyCountingPredictionResult.Stats.ObjectCount\x12\x87\x01\n%accumulated_positive_direction_counts\x18\x04 \x03(\x0b2X.google.cloud.visionai.v1.OccupancyCountingPredictionResult.Stats.AccumulatedObjectCount\x12\x87\x01\n%accumulated_negative_direction_counts\x18\x05 \x03(\x0b2X.google.cloud.visionai.v1.OccupancyCountingPredictionResult.Stats.AccumulatedObjectCount\x1a\xb0\x01\n\x0fActiveZoneCount\x12>\n\nannotation\x18\x01 \x01(\x0b2*.google.cloud.visionai.v1.StreamAnnotation\x12]\n\x06counts\x18\x02 \x03(\x0b2M.google.cloud.visionai.v1.OccupancyCountingPredictionResult.Stats.ObjectCount\x1aM\n\tTrackInfo\x12\x10\n\x08track_id\x18\x01 \x01(\t\x12.\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a\x9c\x01\n\rDwellTimeInfo\x12\x10\n\x08track_id\x18\x01 \x01(\t\x12\x0f\n\x07zone_id\x18\x02 \x01(\t\x124\n\x10dwell_start_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x122\n\x0edwell_end_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x06\n\x04_pts"\xaa\x02\n\x10StreamAnnotation\x12B\n\x0bactive_zone\x18\x05 \x01(\x0b2+.google.cloud.visionai.v1.NormalizedPolygonH\x00\x12E\n\rcrossing_line\x18\x06 \x01(\x0b2,.google.cloud.visionai.v1.NormalizedPolylineH\x00\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x15\n\rsource_stream\x18\x03 \x01(\t\x12<\n\x04type\x18\x04 \x01(\x0e2..google.cloud.visionai.v1.StreamAnnotationTypeB\x14\n\x12annotation_payload"[\n\x11StreamAnnotations\x12F\n\x12stream_annotations\x18\x01 \x03(\x0b2*.google.cloud.visionai.v1.StreamAnnotation"\\\n\x11NormalizedPolygon\x12G\n\x13normalized_vertices\x18\x01 \x03(\x0b2*.google.cloud.visionai.v1.NormalizedVertex"]\n\x12NormalizedPolyline\x12G\n\x13normalized_vertices\x18\x01 \x03(\x0b2*.google.cloud.visionai.v1.NormalizedVertex"(\n\x10NormalizedVertex\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02"`\n\x13AppPlatformMetadata\x12\x13\n\x0bapplication\x18\x01 \x01(\t\x12\x13\n\x0binstance_id\x18\x02 \x01(\t\x12\x0c\n\x04node\x18\x03 \x01(\t\x12\x11\n\tprocessor\x18\x04 \x01(\t"\xbe\x02\n\x1fAppPlatformCloudFunctionRequest\x12L\n\x15app_platform_metadata\x18\x01 \x01(\x0b2-.google.cloud.visionai.v1.AppPlatformMetadata\x12f\n\x0bannotations\x18\x02 \x03(\x0b2Q.google.cloud.visionai.v1.AppPlatformCloudFunctionRequest.StructedInputAnnotation\x1ae\n\x17StructedInputAnnotation\x12\x1d\n\x15ingestion_time_micros\x18\x01 \x01(\x03\x12+\n\nannotation\x18\x02 \x01(\x0b2\x17.google.protobuf.Struct"\xb5\x02\n AppPlatformCloudFunctionResponse\x12h\n\x0bannotations\x18\x02 \x03(\x0b2S.google.cloud.visionai.v1.AppPlatformCloudFunctionResponse.StructedOutputAnnotation\x12\x1e\n\x16annotation_passthrough\x18\x03 \x01(\x08\x12>\n\x06events\x18\x04 \x03(\x0b2..google.cloud.visionai.v1.AppPlatformEventBody\x1aG\n\x18StructedOutputAnnotation\x12+\n\nannotation\x18\x01 \x01(\x0b2\x17.google.protobuf.Struct"i\n\x14AppPlatformEventBody\x12\x15\n\revent_message\x18\x01 \x01(\t\x12(\n\x07payload\x18\x02 \x01(\x0b2\x17.google.protobuf.Struct\x12\x10\n\x08event_id\x18\x03 \x01(\t*\x90\x01\n\x14StreamAnnotationType\x12&\n"STREAM_ANNOTATION_TYPE_UNSPECIFIED\x10\x00\x12&\n"STREAM_ANNOTATION_TYPE_ACTIVE_ZONE\x10\x01\x12(\n$STREAM_ANNOTATION_TYPE_CROSSING_LINE\x10\x02B\xc0\x01\n\x1ccom.google.cloud.visionai.v1B\x10AnnotationsProtoP\x01Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\xaa\x02\x18Google.Cloud.VisionAI.V1\xca\x02\x18Google\\Cloud\\VisionAI\\V1\xea\x02\x1bGoogle::Cloud::VisionAI::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.visionai.v1.annotations_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.visionai.v1B\x10AnnotationsProtoP\x01Z8cloud.google.com/go/visionai/apiv1/visionaipb;visionaipb\xaa\x02\x18Google.Cloud.VisionAI.V1\xca\x02\x18Google\\Cloud\\VisionAI\\V1\xea\x02\x1bGoogle::Cloud::VisionAI::V1'
    _globals['_STREAMANNOTATIONTYPE']._serialized_start = 7916
    _globals['_STREAMANNOTATIONTYPE']._serialized_end = 8060
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT']._serialized_start = 136
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT']._serialized_end = 1821
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_PERSONENTITY']._serialized_start = 343
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_PERSONENTITY']._serialized_end = 383
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_PPEENTITY']._serialized_start = 385
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_PPEENTITY']._serialized_end = 507
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_NORMALIZEDBOUNDINGBOX']._serialized_start = 509
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_NORMALIZEDBOUNDINGBOX']._serialized_end = 591
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_PERSONIDENTIFIEDBOX']._serialized_start = 594
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_PERSONIDENTIFIEDBOX']._serialized_end = 888
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_PPEIDENTIFIEDBOX']._serialized_start = 891
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_PPEIDENTIFIEDBOX']._serialized_end = 1176
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_DETECTEDPERSON']._serialized_start = 1179
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_DETECTEDPERSON']._serialized_end = 1821
    _globals['_OBJECTDETECTIONPREDICTIONRESULT']._serialized_start = 1824
    _globals['_OBJECTDETECTIONPREDICTIONRESULT']._serialized_end = 2410
    _globals['_OBJECTDETECTIONPREDICTIONRESULT_ENTITY']._serialized_start = 2008
    _globals['_OBJECTDETECTIONPREDICTIONRESULT_ENTITY']._serialized_end = 2056
    _globals['_OBJECTDETECTIONPREDICTIONRESULT_IDENTIFIEDBOX']._serialized_start = 2059
    _globals['_OBJECTDETECTIONPREDICTIONRESULT_IDENTIFIEDBOX']._serialized_end = 2410
    _globals['_OBJECTDETECTIONPREDICTIONRESULT_IDENTIFIEDBOX_NORMALIZEDBOUNDINGBOX']._serialized_start = 509
    _globals['_OBJECTDETECTIONPREDICTIONRESULT_IDENTIFIEDBOX_NORMALIZEDBOUNDINGBOX']._serialized_end = 591
    _globals['_IMAGEOBJECTDETECTIONPREDICTIONRESULT']._serialized_start = 2413
    _globals['_IMAGEOBJECTDETECTIONPREDICTIONRESULT']._serialized_end = 2552
    _globals['_CLASSIFICATIONPREDICTIONRESULT']._serialized_start = 2554
    _globals['_CLASSIFICATIONPREDICTIONRESULT']._serialized_end = 2643
    _globals['_IMAGESEGMENTATIONPREDICTIONRESULT']._serialized_start = 2645
    _globals['_IMAGESEGMENTATIONPREDICTIONRESULT']._serialized_end = 2728
    _globals['_VIDEOACTIONRECOGNITIONPREDICTIONRESULT']._serialized_start = 2731
    _globals['_VIDEOACTIONRECOGNITIONPREDICTIONRESULT']._serialized_end = 3055
    _globals['_VIDEOACTIONRECOGNITIONPREDICTIONRESULT_IDENTIFIEDACTION']._serialized_start = 2983
    _globals['_VIDEOACTIONRECOGNITIONPREDICTIONRESULT_IDENTIFIEDACTION']._serialized_end = 3055
    _globals['_VIDEOOBJECTTRACKINGPREDICTIONRESULT']._serialized_start = 3058
    _globals['_VIDEOOBJECTTRACKINGPREDICTIONRESULT']._serialized_end = 3563
    _globals['_VIDEOOBJECTTRACKINGPREDICTIONRESULT_BOUNDINGBOX']._serialized_start = 3302
    _globals['_VIDEOOBJECTTRACKINGPREDICTIONRESULT_BOUNDINGBOX']._serialized_end = 3375
    _globals['_VIDEOOBJECTTRACKINGPREDICTIONRESULT_DETECTEDOBJECT']._serialized_start = 3378
    _globals['_VIDEOOBJECTTRACKINGPREDICTIONRESULT_DETECTEDOBJECT']._serialized_end = 3563
    _globals['_VIDEOCLASSIFICATIONPREDICTIONRESULT']._serialized_start = 3566
    _globals['_VIDEOCLASSIFICATIONPREDICTIONRESULT']._serialized_end = 3908
    _globals['_VIDEOCLASSIFICATIONPREDICTIONRESULT_IDENTIFIEDCLASSIFICATION']._serialized_start = 3828
    _globals['_VIDEOCLASSIFICATIONPREDICTIONRESULT_IDENTIFIEDCLASSIFICATION']._serialized_end = 3908
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT']._serialized_start = 3911
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT']._serialized_end = 6450
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_ENTITY']._serialized_start = 2008
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_ENTITY']._serialized_end = 2056
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_IDENTIFIEDBOX']._serialized_start = 4441
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_IDENTIFIEDBOX']._serialized_end = 4804
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_IDENTIFIEDBOX_NORMALIZEDBOUNDINGBOX']._serialized_start = 509
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_IDENTIFIEDBOX_NORMALIZEDBOUNDINGBOX']._serialized_end = 591
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_STATS']._serialized_start = 4807
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_STATS']._serialized_end = 6204
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_STATS_OBJECTCOUNT']._serialized_start = 5147
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_STATS_OBJECTCOUNT']._serialized_end = 5259
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_STATS_ACCUMULATEDOBJECTCOUNT']._serialized_start = 5262
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_STATS_ACCUMULATEDOBJECTCOUNT']._serialized_end = 5435
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_STATS_CROSSINGLINECOUNT']._serialized_start = 5438
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_STATS_CROSSINGLINECOUNT']._serialized_end = 6025
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_STATS_ACTIVEZONECOUNT']._serialized_start = 6028
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_STATS_ACTIVEZONECOUNT']._serialized_end = 6204
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_TRACKINFO']._serialized_start = 6206
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_TRACKINFO']._serialized_end = 6283
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_DWELLTIMEINFO']._serialized_start = 6286
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_DWELLTIMEINFO']._serialized_end = 6442
    _globals['_STREAMANNOTATION']._serialized_start = 6453
    _globals['_STREAMANNOTATION']._serialized_end = 6751
    _globals['_STREAMANNOTATIONS']._serialized_start = 6753
    _globals['_STREAMANNOTATIONS']._serialized_end = 6844
    _globals['_NORMALIZEDPOLYGON']._serialized_start = 6846
    _globals['_NORMALIZEDPOLYGON']._serialized_end = 6938
    _globals['_NORMALIZEDPOLYLINE']._serialized_start = 6940
    _globals['_NORMALIZEDPOLYLINE']._serialized_end = 7033
    _globals['_NORMALIZEDVERTEX']._serialized_start = 7035
    _globals['_NORMALIZEDVERTEX']._serialized_end = 7075
    _globals['_APPPLATFORMMETADATA']._serialized_start = 7077
    _globals['_APPPLATFORMMETADATA']._serialized_end = 7173
    _globals['_APPPLATFORMCLOUDFUNCTIONREQUEST']._serialized_start = 7176
    _globals['_APPPLATFORMCLOUDFUNCTIONREQUEST']._serialized_end = 7494
    _globals['_APPPLATFORMCLOUDFUNCTIONREQUEST_STRUCTEDINPUTANNOTATION']._serialized_start = 7393
    _globals['_APPPLATFORMCLOUDFUNCTIONREQUEST_STRUCTEDINPUTANNOTATION']._serialized_end = 7494
    _globals['_APPPLATFORMCLOUDFUNCTIONRESPONSE']._serialized_start = 7497
    _globals['_APPPLATFORMCLOUDFUNCTIONRESPONSE']._serialized_end = 7806
    _globals['_APPPLATFORMCLOUDFUNCTIONRESPONSE_STRUCTEDOUTPUTANNOTATION']._serialized_start = 7735
    _globals['_APPPLATFORMCLOUDFUNCTIONRESPONSE_STRUCTEDOUTPUTANNOTATION']._serialized_end = 7806
    _globals['_APPPLATFORMEVENTBODY']._serialized_start = 7808
    _globals['_APPPLATFORMEVENTBODY']._serialized_end = 7913