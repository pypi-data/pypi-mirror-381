"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/visionai/v1alpha1/annotations.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/visionai/v1alpha1/annotations.proto\x12\x1egoogle.cloud.visionai.v1alpha1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc2\r\n*PersonalProtectiveEquipmentDetectionOutput\x120\n\x0ccurrent_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12s\n\x10detected_persons\x18\x02 \x03(\x0b2Y.google.cloud.visionai.v1alpha1.PersonalProtectiveEquipmentDetectionOutput.DetectedPerson\x1a(\n\x0cPersonEntity\x12\x18\n\x10person_entity_id\x18\x01 \x01(\x03\x1az\n\tPPEEntity\x12\x14\n\x0cppe_label_id\x18\x01 \x01(\x03\x12\x18\n\x10ppe_label_string\x18\x02 \x01(\t\x12&\n\x1eppe_supercategory_label_string\x18\x03 \x01(\t\x12\x15\n\rppe_entity_id\x18\x04 \x01(\x03\x1aR\n\x15NormalizedBoundingBox\x12\x0c\n\x04xmin\x18\x01 \x01(\x02\x12\x0c\n\x04ymin\x18\x02 \x01(\x02\x12\r\n\x05width\x18\x03 \x01(\x02\x12\x0e\n\x06height\x18\x04 \x01(\x02\x1a\xb3\x02\n\x13PersonIdentifiedBox\x12\x0e\n\x06box_id\x18\x01 \x01(\x03\x12\x81\x01\n\x17normalized_bounding_box\x18\x02 \x01(\x0b2`.google.cloud.visionai.v1alpha1.PersonalProtectiveEquipmentDetectionOutput.NormalizedBoundingBox\x12\x18\n\x10confidence_score\x18\x03 \x01(\x02\x12n\n\rperson_entity\x18\x04 \x01(\x0b2W.google.cloud.visionai.v1alpha1.PersonalProtectiveEquipmentDetectionOutput.PersonEntity\x1a\xaa\x02\n\x10PPEIdentifiedBox\x12\x0e\n\x06box_id\x18\x01 \x01(\x03\x12\x81\x01\n\x17normalized_bounding_box\x18\x02 \x01(\x0b2`.google.cloud.visionai.v1alpha1.PersonalProtectiveEquipmentDetectionOutput.NormalizedBoundingBox\x12\x18\n\x10confidence_score\x18\x03 \x01(\x02\x12h\n\nppe_entity\x18\x04 \x01(\x0b2T.google.cloud.visionai.v1alpha1.PersonalProtectiveEquipmentDetectionOutput.PPEEntity\x1a\x8f\x05\n\x0eDetectedPerson\x12\x11\n\tperson_id\x18\x01 \x01(\x03\x12\x86\x01\n\x1edetected_person_identified_box\x18\x02 \x01(\x0b2^.google.cloud.visionai.v1alpha1.PersonalProtectiveEquipmentDetectionOutput.PersonIdentifiedBox\x12\x82\x01\n\x1ddetected_ppe_identified_boxes\x18\x03 \x03(\x0b2[.google.cloud.visionai.v1alpha1.PersonalProtectiveEquipmentDetectionOutput.PPEIdentifiedBox\x12 \n\x13face_coverage_score\x18\x04 \x01(\x02H\x00\x88\x01\x01\x12 \n\x13eyes_coverage_score\x18\x05 \x01(\x02H\x01\x88\x01\x01\x12 \n\x13head_coverage_score\x18\x06 \x01(\x02H\x02\x88\x01\x01\x12!\n\x14hands_coverage_score\x18\x07 \x01(\x02H\x03\x88\x01\x01\x12 \n\x13body_coverage_score\x18\x08 \x01(\x02H\x04\x88\x01\x01\x12 \n\x13feet_coverage_score\x18\t \x01(\x02H\x05\x88\x01\x01B\x16\n\x14_face_coverage_scoreB\x16\n\x14_eyes_coverage_scoreB\x16\n\x14_head_coverage_scoreB\x17\n\x15_hands_coverage_scoreB\x16\n\x14_body_coverage_scoreB\x16\n\x14_feet_coverage_score"\xdd\x04\n\x1fObjectDetectionPredictionResult\x120\n\x0ccurrent_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12g\n\x10identified_boxes\x18\x02 \x03(\x0b2M.google.cloud.visionai.v1alpha1.ObjectDetectionPredictionResult.IdentifiedBox\x1a0\n\x06Entity\x12\x10\n\x08label_id\x18\x01 \x01(\x03\x12\x14\n\x0clabel_string\x18\x02 \x01(\t\x1a\xec\x02\n\rIdentifiedBox\x12\x0e\n\x06box_id\x18\x01 \x01(\x03\x12\x84\x01\n\x17normalized_bounding_box\x18\x02 \x01(\x0b2c.google.cloud.visionai.v1alpha1.ObjectDetectionPredictionResult.IdentifiedBox.NormalizedBoundingBox\x12\x18\n\x10confidence_score\x18\x03 \x01(\x02\x12V\n\x06entity\x18\x04 \x01(\x0b2F.google.cloud.visionai.v1alpha1.ObjectDetectionPredictionResult.Entity\x1aR\n\x15NormalizedBoundingBox\x12\x0c\n\x04xmin\x18\x01 \x01(\x02\x12\x0c\n\x04ymin\x18\x02 \x01(\x02\x12\r\n\x05width\x18\x03 \x01(\x02\x12\x0e\n\x06height\x18\x04 \x01(\x02"\x8b\x01\n$ImageObjectDetectionPredictionResult\x12\x0b\n\x03ids\x18\x01 \x03(\x03\x12\x15\n\rdisplay_names\x18\x02 \x03(\t\x12\x13\n\x0bconfidences\x18\x03 \x03(\x02\x12*\n\x06bboxes\x18\x04 \x03(\x0b2\x1a.google.protobuf.ListValue"Y\n\x1eClassificationPredictionResult\x12\x0b\n\x03ids\x18\x01 \x03(\x03\x12\x15\n\rdisplay_names\x18\x02 \x03(\t\x12\x13\n\x0bconfidences\x18\x03 \x03(\x02"S\n!ImageSegmentationPredictionResult\x12\x15\n\rcategory_mask\x18\x01 \x01(\t\x12\x17\n\x0fconfidence_mask\x18\x02 \x01(\t"\xca\x02\n&VideoActionRecognitionPredictionResult\x126\n\x12segment_start_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x10segment_end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12h\n\x07actions\x18\x03 \x03(\x0b2W.google.cloud.visionai.v1alpha1.VideoActionRecognitionPredictionResult.IdentifiedAction\x1aH\n\x10IdentifiedAction\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x12\n\nconfidence\x18\x03 \x01(\x02"\x85\x04\n#VideoObjectTrackingPredictionResult\x126\n\x12segment_start_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x10segment_end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12c\n\x07objects\x18\x03 \x03(\x0b2R.google.cloud.visionai.v1alpha1.VideoObjectTrackingPredictionResult.DetectedObject\x1aI\n\x0bBoundingBox\x12\r\n\x05x_min\x18\x01 \x01(\x02\x12\r\n\x05x_max\x18\x02 \x01(\x02\x12\r\n\x05y_min\x18\x03 \x01(\x02\x12\r\n\x05y_max\x18\x04 \x01(\x02\x1a\xbf\x01\n\x0eDetectedObject\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12e\n\x0cbounding_box\x18\x03 \x01(\x0b2O.google.cloud.visionai.v1alpha1.VideoObjectTrackingPredictionResult.BoundingBox\x12\x12\n\nconfidence\x18\x04 \x01(\x02\x12\x10\n\x08track_id\x18\x05 \x01(\x03"\xdc\x02\n#VideoClassificationPredictionResult\x126\n\x12segment_start_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x124\n\x10segment_end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12u\n\x0fclassifications\x18\x03 \x03(\x0b2\\.google.cloud.visionai.v1alpha1.VideoClassificationPredictionResult.IdentifiedClassification\x1aP\n\x18IdentifiedClassification\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x12\n\nconfidence\x18\x03 \x01(\x02"\xbd\x14\n!OccupancyCountingPredictionResult\x120\n\x0ccurrent_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12i\n\x10identified_boxes\x18\x02 \x03(\x0b2O.google.cloud.visionai.v1alpha1.OccupancyCountingPredictionResult.IdentifiedBox\x12V\n\x05stats\x18\x03 \x01(\x0b2G.google.cloud.visionai.v1alpha1.OccupancyCountingPredictionResult.Stats\x12_\n\ntrack_info\x18\x04 \x03(\x0b2K.google.cloud.visionai.v1alpha1.OccupancyCountingPredictionResult.TrackInfo\x12h\n\x0fdwell_time_info\x18\x05 \x03(\x0b2O.google.cloud.visionai.v1alpha1.OccupancyCountingPredictionResult.DwellTimeInfo\x1a0\n\x06Entity\x12\x10\n\x08label_id\x18\x01 \x01(\x03\x12\x14\n\x0clabel_string\x18\x02 \x01(\t\x1a\xf7\x02\n\rIdentifiedBox\x12\x0e\n\x06box_id\x18\x01 \x01(\x03\x12\x86\x01\n\x17normalized_bounding_box\x18\x02 \x01(\x0b2e.google.cloud.visionai.v1alpha1.OccupancyCountingPredictionResult.IdentifiedBox.NormalizedBoundingBox\x12\r\n\x05score\x18\x03 \x01(\x02\x12X\n\x06entity\x18\x04 \x01(\x0b2H.google.cloud.visionai.v1alpha1.OccupancyCountingPredictionResult.Entity\x12\x10\n\x08track_id\x18\x05 \x01(\x03\x1aR\n\x15NormalizedBoundingBox\x12\x0c\n\x04xmin\x18\x01 \x01(\x02\x12\x0c\n\x04ymin\x18\x02 \x01(\x02\x12\r\n\x05width\x18\x03 \x01(\x02\x12\x0e\n\x06height\x18\x04 \x01(\x02\x1a\xbd\x0b\n\x05Stats\x12m\n\x10full_frame_count\x18\x01 \x03(\x0b2S.google.cloud.visionai.v1alpha1.OccupancyCountingPredictionResult.Stats.ObjectCount\x12w\n\x14crossing_line_counts\x18\x02 \x03(\x0b2Y.google.cloud.visionai.v1alpha1.OccupancyCountingPredictionResult.Stats.CrossingLineCount\x12s\n\x12active_zone_counts\x18\x03 \x03(\x0b2W.google.cloud.visionai.v1alpha1.OccupancyCountingPredictionResult.Stats.ActiveZoneCount\x1av\n\x0bObjectCount\x12X\n\x06entity\x18\x01 \x01(\x0b2H.google.cloud.visionai.v1alpha1.OccupancyCountingPredictionResult.Entity\x12\r\n\x05count\x18\x02 \x01(\x05\x1a\xb3\x01\n\x16AccumulatedObjectCount\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12i\n\x0cobject_count\x18\x02 \x01(\x0b2S.google.cloud.visionai.v1alpha1.OccupancyCountingPredictionResult.Stats.ObjectCount\x1a\xe9\x04\n\x11CrossingLineCount\x12D\n\nannotation\x18\x01 \x01(\x0b20.google.cloud.visionai.v1alpha1.StreamAnnotation\x12v\n\x19positive_direction_counts\x18\x02 \x03(\x0b2S.google.cloud.visionai.v1alpha1.OccupancyCountingPredictionResult.Stats.ObjectCount\x12v\n\x19negative_direction_counts\x18\x03 \x03(\x0b2S.google.cloud.visionai.v1alpha1.OccupancyCountingPredictionResult.Stats.ObjectCount\x12\x8d\x01\n%accumulated_positive_direction_counts\x18\x04 \x03(\x0b2^.google.cloud.visionai.v1alpha1.OccupancyCountingPredictionResult.Stats.AccumulatedObjectCount\x12\x8d\x01\n%accumulated_negative_direction_counts\x18\x05 \x03(\x0b2^.google.cloud.visionai.v1alpha1.OccupancyCountingPredictionResult.Stats.AccumulatedObjectCount\x1a\xbc\x01\n\x0fActiveZoneCount\x12D\n\nannotation\x18\x01 \x01(\x0b20.google.cloud.visionai.v1alpha1.StreamAnnotation\x12c\n\x06counts\x18\x02 \x03(\x0b2S.google.cloud.visionai.v1alpha1.OccupancyCountingPredictionResult.Stats.ObjectCount\x1aM\n\tTrackInfo\x12\x10\n\x08track_id\x18\x01 \x01(\t\x12.\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a\x9c\x01\n\rDwellTimeInfo\x12\x10\n\x08track_id\x18\x01 \x01(\t\x12\x0f\n\x07zone_id\x18\x02 \x01(\t\x124\n\x10dwell_start_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x122\n\x0edwell_end_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xbc\x02\n\x10StreamAnnotation\x12H\n\x0bactive_zone\x18\x05 \x01(\x0b21.google.cloud.visionai.v1alpha1.NormalizedPolygonH\x00\x12K\n\rcrossing_line\x18\x06 \x01(\x0b22.google.cloud.visionai.v1alpha1.NormalizedPolylineH\x00\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x15\n\rsource_stream\x18\x03 \x01(\t\x12B\n\x04type\x18\x04 \x01(\x0e24.google.cloud.visionai.v1alpha1.StreamAnnotationTypeB\x14\n\x12annotation_payload"a\n\x11StreamAnnotations\x12L\n\x12stream_annotations\x18\x01 \x03(\x0b20.google.cloud.visionai.v1alpha1.StreamAnnotation"b\n\x11NormalizedPolygon\x12M\n\x13normalized_vertices\x18\x01 \x03(\x0b20.google.cloud.visionai.v1alpha1.NormalizedVertex"c\n\x12NormalizedPolyline\x12M\n\x13normalized_vertices\x18\x01 \x03(\x0b20.google.cloud.visionai.v1alpha1.NormalizedVertex"(\n\x10NormalizedVertex\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02"`\n\x13AppPlatformMetadata\x12\x13\n\x0bapplication\x18\x01 \x01(\t\x12\x13\n\x0binstance_id\x18\x02 \x01(\t\x12\x0c\n\x04node\x18\x03 \x01(\t\x12\x11\n\tprocessor\x18\x04 \x01(\t"\xca\x02\n\x1fAppPlatformCloudFunctionRequest\x12R\n\x15app_platform_metadata\x18\x01 \x01(\x0b23.google.cloud.visionai.v1alpha1.AppPlatformMetadata\x12l\n\x0bannotations\x18\x02 \x03(\x0b2W.google.cloud.visionai.v1alpha1.AppPlatformCloudFunctionRequest.StructedInputAnnotation\x1ae\n\x17StructedInputAnnotation\x12\x1d\n\x15ingestion_time_micros\x18\x01 \x01(\x03\x12+\n\nannotation\x18\x02 \x01(\x0b2\x17.google.protobuf.Struct"\xc1\x02\n AppPlatformCloudFunctionResponse\x12n\n\x0bannotations\x18\x02 \x03(\x0b2Y.google.cloud.visionai.v1alpha1.AppPlatformCloudFunctionResponse.StructedOutputAnnotation\x12\x1e\n\x16annotation_passthrough\x18\x03 \x01(\x08\x12D\n\x06events\x18\x04 \x03(\x0b24.google.cloud.visionai.v1alpha1.AppPlatformEventBody\x1aG\n\x18StructedOutputAnnotation\x12+\n\nannotation\x18\x01 \x01(\x0b2\x17.google.protobuf.Struct"i\n\x14AppPlatformEventBody\x12\x15\n\revent_message\x18\x01 \x01(\t\x12(\n\x07payload\x18\x02 \x01(\x0b2\x17.google.protobuf.Struct\x12\x10\n\x08event_id\x18\x03 \x01(\t*\x90\x01\n\x14StreamAnnotationType\x12&\n"STREAM_ANNOTATION_TYPE_UNSPECIFIED\x10\x00\x12&\n"STREAM_ANNOTATION_TYPE_ACTIVE_ZONE\x10\x01\x12(\n$STREAM_ANNOTATION_TYPE_CROSSING_LINE\x10\x02B\xde\x01\n"com.google.cloud.visionai.v1alpha1B\x10AnnotationsProtoP\x01Z>cloud.google.com/go/visionai/apiv1alpha1/visionaipb;visionaipb\xaa\x02\x1eGoogle.Cloud.VisionAI.V1Alpha1\xca\x02\x1eGoogle\\Cloud\\VisionAI\\V1alpha1\xea\x02!Google::Cloud::VisionAI::V1alpha1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.visionai.v1alpha1.annotations_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.visionai.v1alpha1B\x10AnnotationsProtoP\x01Z>cloud.google.com/go/visionai/apiv1alpha1/visionaipb;visionaipb\xaa\x02\x1eGoogle.Cloud.VisionAI.V1Alpha1\xca\x02\x1eGoogle\\Cloud\\VisionAI\\V1alpha1\xea\x02!Google::Cloud::VisionAI::V1alpha1'
    _globals['_STREAMANNOTATIONTYPE']._serialized_start = 8158
    _globals['_STREAMANNOTATIONTYPE']._serialized_end = 8302
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT']._serialized_start = 148
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT']._serialized_end = 1878
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_PERSONENTITY']._serialized_start = 361
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_PERSONENTITY']._serialized_end = 401
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_PPEENTITY']._serialized_start = 403
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_PPEENTITY']._serialized_end = 525
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_NORMALIZEDBOUNDINGBOX']._serialized_start = 527
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_NORMALIZEDBOUNDINGBOX']._serialized_end = 609
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_PERSONIDENTIFIEDBOX']._serialized_start = 612
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_PERSONIDENTIFIEDBOX']._serialized_end = 919
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_PPEIDENTIFIEDBOX']._serialized_start = 922
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_PPEIDENTIFIEDBOX']._serialized_end = 1220
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_DETECTEDPERSON']._serialized_start = 1223
    _globals['_PERSONALPROTECTIVEEQUIPMENTDETECTIONOUTPUT_DETECTEDPERSON']._serialized_end = 1878
    _globals['_OBJECTDETECTIONPREDICTIONRESULT']._serialized_start = 1881
    _globals['_OBJECTDETECTIONPREDICTIONRESULT']._serialized_end = 2486
    _globals['_OBJECTDETECTIONPREDICTIONRESULT_ENTITY']._serialized_start = 2071
    _globals['_OBJECTDETECTIONPREDICTIONRESULT_ENTITY']._serialized_end = 2119
    _globals['_OBJECTDETECTIONPREDICTIONRESULT_IDENTIFIEDBOX']._serialized_start = 2122
    _globals['_OBJECTDETECTIONPREDICTIONRESULT_IDENTIFIEDBOX']._serialized_end = 2486
    _globals['_OBJECTDETECTIONPREDICTIONRESULT_IDENTIFIEDBOX_NORMALIZEDBOUNDINGBOX']._serialized_start = 527
    _globals['_OBJECTDETECTIONPREDICTIONRESULT_IDENTIFIEDBOX_NORMALIZEDBOUNDINGBOX']._serialized_end = 609
    _globals['_IMAGEOBJECTDETECTIONPREDICTIONRESULT']._serialized_start = 2489
    _globals['_IMAGEOBJECTDETECTIONPREDICTIONRESULT']._serialized_end = 2628
    _globals['_CLASSIFICATIONPREDICTIONRESULT']._serialized_start = 2630
    _globals['_CLASSIFICATIONPREDICTIONRESULT']._serialized_end = 2719
    _globals['_IMAGESEGMENTATIONPREDICTIONRESULT']._serialized_start = 2721
    _globals['_IMAGESEGMENTATIONPREDICTIONRESULT']._serialized_end = 2804
    _globals['_VIDEOACTIONRECOGNITIONPREDICTIONRESULT']._serialized_start = 2807
    _globals['_VIDEOACTIONRECOGNITIONPREDICTIONRESULT']._serialized_end = 3137
    _globals['_VIDEOACTIONRECOGNITIONPREDICTIONRESULT_IDENTIFIEDACTION']._serialized_start = 3065
    _globals['_VIDEOACTIONRECOGNITIONPREDICTIONRESULT_IDENTIFIEDACTION']._serialized_end = 3137
    _globals['_VIDEOOBJECTTRACKINGPREDICTIONRESULT']._serialized_start = 3140
    _globals['_VIDEOOBJECTTRACKINGPREDICTIONRESULT']._serialized_end = 3657
    _globals['_VIDEOOBJECTTRACKINGPREDICTIONRESULT_BOUNDINGBOX']._serialized_start = 3390
    _globals['_VIDEOOBJECTTRACKINGPREDICTIONRESULT_BOUNDINGBOX']._serialized_end = 3463
    _globals['_VIDEOOBJECTTRACKINGPREDICTIONRESULT_DETECTEDOBJECT']._serialized_start = 3466
    _globals['_VIDEOOBJECTTRACKINGPREDICTIONRESULT_DETECTEDOBJECT']._serialized_end = 3657
    _globals['_VIDEOCLASSIFICATIONPREDICTIONRESULT']._serialized_start = 3660
    _globals['_VIDEOCLASSIFICATIONPREDICTIONRESULT']._serialized_end = 4008
    _globals['_VIDEOCLASSIFICATIONPREDICTIONRESULT_IDENTIFIEDCLASSIFICATION']._serialized_start = 3928
    _globals['_VIDEOCLASSIFICATIONPREDICTIONRESULT_IDENTIFIEDCLASSIFICATION']._serialized_end = 4008
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT']._serialized_start = 4011
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT']._serialized_end = 6632
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_ENTITY']._serialized_start = 2071
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_ENTITY']._serialized_end = 2119
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_IDENTIFIEDBOX']._serialized_start = 4547
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_IDENTIFIEDBOX']._serialized_end = 4922
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_IDENTIFIEDBOX_NORMALIZEDBOUNDINGBOX']._serialized_start = 527
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_IDENTIFIEDBOX_NORMALIZEDBOUNDINGBOX']._serialized_end = 609
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_STATS']._serialized_start = 4925
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_STATS']._serialized_end = 6394
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_STATS_OBJECTCOUNT']._serialized_start = 5283
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_STATS_OBJECTCOUNT']._serialized_end = 5401
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_STATS_ACCUMULATEDOBJECTCOUNT']._serialized_start = 5404
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_STATS_ACCUMULATEDOBJECTCOUNT']._serialized_end = 5583
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_STATS_CROSSINGLINECOUNT']._serialized_start = 5586
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_STATS_CROSSINGLINECOUNT']._serialized_end = 6203
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_STATS_ACTIVEZONECOUNT']._serialized_start = 6206
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_STATS_ACTIVEZONECOUNT']._serialized_end = 6394
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_TRACKINFO']._serialized_start = 6396
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_TRACKINFO']._serialized_end = 6473
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_DWELLTIMEINFO']._serialized_start = 6476
    _globals['_OCCUPANCYCOUNTINGPREDICTIONRESULT_DWELLTIMEINFO']._serialized_end = 6632
    _globals['_STREAMANNOTATION']._serialized_start = 6635
    _globals['_STREAMANNOTATION']._serialized_end = 6951
    _globals['_STREAMANNOTATIONS']._serialized_start = 6953
    _globals['_STREAMANNOTATIONS']._serialized_end = 7050
    _globals['_NORMALIZEDPOLYGON']._serialized_start = 7052
    _globals['_NORMALIZEDPOLYGON']._serialized_end = 7150
    _globals['_NORMALIZEDPOLYLINE']._serialized_start = 7152
    _globals['_NORMALIZEDPOLYLINE']._serialized_end = 7251
    _globals['_NORMALIZEDVERTEX']._serialized_start = 7253
    _globals['_NORMALIZEDVERTEX']._serialized_end = 7293
    _globals['_APPPLATFORMMETADATA']._serialized_start = 7295
    _globals['_APPPLATFORMMETADATA']._serialized_end = 7391
    _globals['_APPPLATFORMCLOUDFUNCTIONREQUEST']._serialized_start = 7394
    _globals['_APPPLATFORMCLOUDFUNCTIONREQUEST']._serialized_end = 7724
    _globals['_APPPLATFORMCLOUDFUNCTIONREQUEST_STRUCTEDINPUTANNOTATION']._serialized_start = 7623
    _globals['_APPPLATFORMCLOUDFUNCTIONREQUEST_STRUCTEDINPUTANNOTATION']._serialized_end = 7724
    _globals['_APPPLATFORMCLOUDFUNCTIONRESPONSE']._serialized_start = 7727
    _globals['_APPPLATFORMCLOUDFUNCTIONRESPONSE']._serialized_end = 8048
    _globals['_APPPLATFORMCLOUDFUNCTIONRESPONSE_STRUCTEDOUTPUTANNOTATION']._serialized_start = 7977
    _globals['_APPPLATFORMCLOUDFUNCTIONRESPONSE_STRUCTEDOUTPUTANNOTATION']._serialized_end = 8048
    _globals['_APPPLATFORMEVENTBODY']._serialized_start = 8050
    _globals['_APPPLATFORMEVENTBODY']._serialized_end = 8155