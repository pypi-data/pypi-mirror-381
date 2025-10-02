# type: ignore[pb2]
from __future__ import annotations

from typing import TYPE_CHECKING, Tuple

from google.protobuf import json_format, message
from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.wrappers_pb2 import DoubleValue, StringValue

from arize._flight.types import FlightRequestType
from arize._generated.protocol.flight import export_pb2 as flight_exp_pb2
from arize._generated.protocol.flight import ingest_pb2 as flight_ing_pb2
from arize._generated.protocol.rec import public_pb2 as pb2
from arize.exceptions.parameters import InvalidValueType
from arize.types import (
    CATEGORICAL_MODEL_TYPES,
    NUMERIC_MODEL_TYPES,
    CorpusSchema,
    Embedding,
    Environments,
    InstanceSegmentationActualLabel,
    InstanceSegmentationPredictionLabel,
    ModelTypes,
    MultiClassActualLabel,
    MultiClassPredictionLabel,
    ObjectDetectionLabel,
    RankingActualLabel,
    RankingPredictionLabel,
    SemanticSegmentationLabel,
    SimilaritySearchParams,
    convert_element,
    is_list_of,
)

if TYPE_CHECKING:
    from arize.types import (
        EmbeddingColumnNames,
        Schema,
    )


def get_pb_schema(
    schema: Schema,
    model_id: str,
    model_version: str | None,
    model_type: ModelTypes,
    environment: Environments,
    batch_id: str,
):
    s = pb2.Schema()
    s.constants.model_id = model_id

    if model_version is not None:
        s.constants.model_version = model_version

    if environment == Environments.PRODUCTION:
        s.constants.environment = pb2.Schema.Environment.PRODUCTION
    elif environment == Environments.VALIDATION:
        s.constants.environment = pb2.Schema.Environment.VALIDATION
    elif environment == Environments.TRAINING:
        s.constants.environment = pb2.Schema.Environment.TRAINING
    else:
        raise ValueError(f"unexpected environment: {environment}")

    # Map user-friendly external model types -> internal model types when sending to Arize
    if model_type in NUMERIC_MODEL_TYPES:
        s.constants.model_type = pb2.Schema.ModelType.NUMERIC
    elif model_type in CATEGORICAL_MODEL_TYPES:
        s.constants.model_type = pb2.Schema.ModelType.SCORE_CATEGORICAL
    elif model_type == ModelTypes.RANKING:
        s.constants.model_type = pb2.Schema.ModelType.RANKING
    elif model_type == ModelTypes.OBJECT_DETECTION:
        s.constants.model_type = pb2.Schema.ModelType.OBJECT_DETECTION
    elif model_type == ModelTypes.GENERATIVE_LLM:
        s.constants.model_type = pb2.Schema.ModelType.GENERATIVE_LLM
    elif model_type == ModelTypes.MULTI_CLASS:
        s.constants.model_type = pb2.Schema.ModelType.MULTI_CLASS

    if batch_id is not None:
        s.constants.batch_id = batch_id

    if schema.prediction_id_column_name is not None:
        s.arrow_schema.prediction_id_column_name = (
            schema.prediction_id_column_name
        )

    if schema.timestamp_column_name is not None:
        s.arrow_schema.timestamp_column_name = schema.timestamp_column_name

    if schema.prediction_label_column_name is not None:
        s.arrow_schema.prediction_label_column_name = (
            schema.prediction_label_column_name
        )

    if model_type == ModelTypes.OBJECT_DETECTION:
        if schema.object_detection_prediction_column_names is not None:
            s.arrow_schema.prediction_object_detection_label_column_names.bboxes_coordinates_column_name = (
                schema.object_detection_prediction_column_names.bounding_boxes_coordinates_column_name  # noqa: E501
            )
            s.arrow_schema.prediction_object_detection_label_column_names.bboxes_categories_column_name = (
                schema.object_detection_prediction_column_names.categories_column_name  # noqa: E501
            )
            if (
                schema.object_detection_prediction_column_names.scores_column_name
                is not None
            ):
                s.arrow_schema.prediction_object_detection_label_column_names.bboxes_scores_column_name = (
                    schema.object_detection_prediction_column_names.scores_column_name  # noqa: E501
                )

        if schema.semantic_segmentation_prediction_column_names is not None:
            s.arrow_schema.prediction_semantic_segmentation_label_column_names.polygons_coordinates_column_name = (  # noqa: E501
                schema.semantic_segmentation_prediction_column_names.polygon_coordinates_column_name
            )
            s.arrow_schema.prediction_semantic_segmentation_label_column_names.polygons_categories_column_name = (  # noqa: E501
                schema.semantic_segmentation_prediction_column_names.categories_column_name
            )

        if schema.instance_segmentation_prediction_column_names is not None:
            s.arrow_schema.prediction_instance_segmentation_label_column_names.polygons_coordinates_column_name = (  # noqa: E501
                schema.instance_segmentation_prediction_column_names.polygon_coordinates_column_name
            )
            s.arrow_schema.prediction_instance_segmentation_label_column_names.polygons_categories_column_name = (  # noqa: E501
                schema.instance_segmentation_prediction_column_names.categories_column_name
            )
            if (
                schema.instance_segmentation_prediction_column_names.scores_column_name
                is not None
            ):
                s.arrow_schema.prediction_instance_segmentation_label_column_names.polygons_scores_column_name = (  # noqa: E501
                    schema.instance_segmentation_prediction_column_names.scores_column_name
                )
            if (
                schema.instance_segmentation_prediction_column_names.bounding_boxes_coordinates_column_name
                is not None
            ):
                s.arrow_schema.prediction_instance_segmentation_label_column_names.bboxes_coordinates_column_name = (  # noqa: E501
                    schema.instance_segmentation_prediction_column_names.bounding_boxes_coordinates_column_name
                )

    if schema.prediction_score_column_name is not None:
        if model_type in NUMERIC_MODEL_TYPES:
            # allow numeric prediction to be sent in as either prediction_label (legacy) or
            # prediction_score.
            s.arrow_schema.prediction_label_column_name = (
                schema.prediction_score_column_name
            )
        else:
            s.arrow_schema.prediction_score_column_name = (
                schema.prediction_score_column_name
            )

    if schema.feature_column_names is not None:
        s.arrow_schema.feature_column_names.extend(schema.feature_column_names)

    if schema.embedding_feature_column_names is not None:
        for (
            emb_name,
            emb_col_names,
        ) in schema.embedding_feature_column_names.items():
            # emb_name is how it will show in the UI
            s.arrow_schema.embedding_feature_column_names_map[
                emb_name
            ].vector_column_name = emb_col_names.vector_column_name
            if emb_col_names.data_column_name:
                s.arrow_schema.embedding_feature_column_names_map[
                    emb_name
                ].data_column_name = emb_col_names.data_column_name
            if emb_col_names.link_to_data_column_name:
                s.arrow_schema.embedding_feature_column_names_map[
                    emb_name
                ].link_to_data_column_name = (
                    emb_col_names.link_to_data_column_name
                )

    if schema.prompt_column_names is not None:
        if isinstance(schema.prompt_column_names, str):
            s.arrow_schema.embedding_feature_column_names_map[
                "prompt"
            ].data_column_name = schema.prompt_column_names
        elif isinstance(schema.prompt_column_names, EmbeddingColumnNames):
            col_names = schema.prompt_column_names
            s.arrow_schema.embedding_feature_column_names_map[
                "prompt"
            ].vector_column_name = col_names.vector_column_name
            if col_names.data_column_name:
                s.arrow_schema.embedding_feature_column_names_map[
                    "prompt"
                ].data_column_name = col_names.data_column_name
    if schema.response_column_names is not None:
        if isinstance(schema.response_column_names, str):
            s.arrow_schema.embedding_feature_column_names_map[
                "response"
            ].data_column_name = schema.response_column_names
        elif isinstance(schema.response_column_names, EmbeddingColumnNames):
            col_names = schema.response_column_names
            s.arrow_schema.embedding_feature_column_names_map[
                "response"
            ].vector_column_name = col_names.vector_column_name
            if col_names.data_column_name:
                s.arrow_schema.embedding_feature_column_names_map[
                    "response"
                ].data_column_name = col_names.data_column_name

    if schema.tag_column_names is not None:
        s.arrow_schema.tag_column_names.extend(schema.tag_column_names)

    if (
        model_type == ModelTypes.RANKING
        and schema.relevance_labels_column_name is not None
    ):
        s.arrow_schema.actual_label_column_name = (
            schema.relevance_labels_column_name
        )
    elif (
        model_type == ModelTypes.RANKING
        and schema.attributions_column_name is not None
    ):
        s.arrow_schema.actual_label_column_name = (
            schema.attributions_column_name
        )
    elif schema.actual_label_column_name is not None:
        s.arrow_schema.actual_label_column_name = (
            schema.actual_label_column_name
        )

    if (
        model_type == ModelTypes.RANKING
        and schema.relevance_score_column_name is not None
    ):
        s.arrow_schema.actual_score_column_name = (
            schema.relevance_score_column_name
        )
    elif schema.actual_score_column_name is not None:
        if model_type in NUMERIC_MODEL_TYPES:
            # allow numeric prediction to be sent in as either prediction_label (legacy) or
            # prediction_score.
            s.arrow_schema.actual_label_column_name = (
                schema.actual_score_column_name
            )
        else:
            s.arrow_schema.actual_score_column_name = (
                schema.actual_score_column_name
            )

    if schema.shap_values_column_names is not None:
        s.arrow_schema.shap_values_column_names.update(
            schema.shap_values_column_names
        )

    if schema.prediction_group_id_column_name is not None:
        s.arrow_schema.prediction_group_id_column_name = (
            schema.prediction_group_id_column_name
        )

    if schema.rank_column_name is not None:
        s.arrow_schema.rank_column_name = schema.rank_column_name

    if model_type == ModelTypes.OBJECT_DETECTION:
        if schema.object_detection_actual_column_names is not None:
            s.arrow_schema.actual_object_detection_label_column_names.bboxes_coordinates_column_name = (  # noqa: E501
                schema.object_detection_actual_column_names.bounding_boxes_coordinates_column_name
            )
            s.arrow_schema.actual_object_detection_label_column_names.bboxes_categories_column_name = (  # noqa: E501
                schema.object_detection_actual_column_names.categories_column_name
            )
            if (
                schema.object_detection_actual_column_names.scores_column_name
                is not None
            ):
                s.arrow_schema.actual_object_detection_label_column_names.bboxes_scores_column_name = (  # noqa: E501
                    schema.object_detection_actual_column_names.scores_column_name
                )

        if schema.semantic_segmentation_actual_column_names is not None:
            s.arrow_schema.actual_semantic_segmentation_label_column_names.polygons_coordinates_column_name = (  # noqa: E501
                schema.semantic_segmentation_actual_column_names.polygon_coordinates_column_name
            )
            s.arrow_schema.actual_semantic_segmentation_label_column_names.polygons_categories_column_name = (  # noqa: E501
                schema.semantic_segmentation_actual_column_names.categories_column_name
            )

        if schema.instance_segmentation_actual_column_names is not None:
            s.arrow_schema.actual_instance_segmentation_label_column_names.polygons_coordinates_column_name = (  # noqa: E501
                schema.instance_segmentation_actual_column_names.polygon_coordinates_column_name
            )
            s.arrow_schema.actual_instance_segmentation_label_column_names.polygons_categories_column_name = (  # noqa: E501
                schema.instance_segmentation_actual_column_names.categories_column_name
            )
            if (
                schema.instance_segmentation_actual_column_names.bounding_boxes_coordinates_column_name
                is not None
            ):
                s.arrow_schema.actual_instance_segmentation_label_column_names.bboxes_coordinates_column_name = (  # noqa: E501
                    schema.instance_segmentation_actual_column_names.bounding_boxes_coordinates_column_name
                )

    if model_type == ModelTypes.GENERATIVE_LLM:
        if schema.prompt_template_column_names is not None:
            s.arrow_schema.prompt_template_column_names.template_column_name = (
                schema.prompt_template_column_names.template_column_name
            )
            s.arrow_schema.prompt_template_column_names.template_version_column_name = (  # noqa: E501
                schema.prompt_template_column_names.template_version_column_name
            )
        if schema.llm_config_column_names is not None:
            s.arrow_schema.llm_config_column_names.model_column_name = (
                schema.llm_config_column_names.model_column_name
            )
            s.arrow_schema.llm_config_column_names.params_map_column_name = (
                schema.llm_config_column_names.params_column_name
            )
        if schema.retrieved_document_ids_column_name is not None:
            s.arrow_schema.retrieved_document_ids_column_name = (
                schema.retrieved_document_ids_column_name
            )
    if model_type == ModelTypes.MULTI_CLASS:
        if schema.prediction_score_column_name is not None:
            s.arrow_schema.prediction_score_column_name = (
                schema.prediction_score_column_name
            )
        if schema.multi_class_threshold_scores_column_name is not None:
            s.arrow_schema.multi_class_threshold_scores_column_name = (
                schema.multi_class_threshold_scores_column_name
            )
        if schema.actual_score_column_name is not None:
            s.arrow_schema.actual_score_column_name = (
                schema.actual_score_column_name
            )
    return s


def get_pb_schema_corpus(
    schema: CorpusSchema,
    model_id: str,
) -> pb2.Schema:
    s = pb2.Schema()
    s.constants.model_id = model_id
    s.constants.environment = pb2.Schema.Environment.CORPUS
    s.constants.model_type = pb2.Schema.ModelType.GENERATIVE_LLM
    if schema.document_id_column_name is not None:
        s.arrow_schema.document_column_names.id_column_name = (
            schema.document_id_column_name
        )
    if schema.document_version_column_name is not None:
        s.arrow_schema.document_column_names.version_column_name = (
            schema.document_version_column_name
        )
    if schema.document_text_embedding_column_names is not None:
        s.arrow_schema.document_column_names.text_column_name.vector_column_name = schema.document_text_embedding_column_names.vector_column_name  # noqa: E501
        s.arrow_schema.document_column_names.text_column_name.data_column_name = schema.document_text_embedding_column_names.data_column_name  # noqa: E501
        if (
            schema.document_text_embedding_column_names.link_to_data_column_name
            is not None
        ):
            s.arrow_schema.document_column_names.text_column_name.link_to_data_column_name = schema.document_text_embedding_column_names.link_to_data_column_name  # noqa: E501
    return s


def get_pb_schema_tracing(
    project_name: str,
) -> pb2.Schema:
    s = pb2.Schema()
    s.constants.model_id = project_name
    s.constants.environment = pb2.Schema.Environment.TRACING
    s.constants.model_type = pb2.Schema.ModelType.GENERATIVE_LLM
    s.arize_spans.SetInParent()
    return s


def get_pb_flight_doput_request(
    space_id,
    model_id: str,
    request_type: FlightRequestType,
) -> flight_ing_pb2.DoPutRequest:
    """Return a DoPutRequest for the given request_type."""
    common_args: dict[str, str] = {
        "space_id": space_id,
        "external_model_id": model_id,
    }

    match request_type:
        case FlightRequestType.EVALUATION:
            return flight_ing_pb2.DoPutRequest(
                write_span_evaluation_request=flight_ing_pb2.WriteSpanEvaluationRequest(
                    **common_args
                )
            )
        case FlightRequestType.ANNOTATION:
            return flight_ing_pb2.DoPutRequest(
                write_span_annotation_request=flight_ing_pb2.WriteSpanAnnotationRequest(
                    **common_args
                )
            )
        case FlightRequestType.METADATA:
            return flight_ing_pb2.DoPutRequest(
                write_span_attributes_metadata_request=flight_ing_pb2.WriteSpanAttributesMetadataRequest(
                    **common_args
                )
            )
        case _:
            raise ValueError(f"Unsupported request_type: {request_type}")


def message_to_dict(
    msg: message.Message,
    preserve_names: bool = True,
    use_int_enums: bool = False,
):
    return json_format.MessageToDict(
        msg,
        preserving_proto_field_name=preserve_names,
        use_integers_for_enums=use_int_enums,
    )


def get_pb_similarity_search_params(
    similarity_params: SimilaritySearchParams,
) -> flight_exp_pb2.SimilaritySearchParams:
    proto_params = flight_exp_pb2.SimilaritySearchParams()
    proto_params.search_column_name = similarity_params.search_column_name
    proto_params.threshold = similarity_params.threshold
    for ref in similarity_params.references:
        new_ref = proto_params.references.add()
        new_ref.prediction_id = ref.prediction_id
        new_ref.reference_column_name = ref.reference_column_name
        if ref.prediction_timestamp:
            new_ref.prediction_timestamp.FromDatetime(ref.prediction_timestamp)

    return proto_params


def get_pb_dictionary(d):
    if d is None:
        return {}
    # Takes a dictionary and
    # - casts the keys as strings
    # - turns the values of the dictionary to our proto values pb2.Value()
    converted_dict = {}
    for k, v in d.items():
        val = get_pb_value(value=v, name=k)
        if val is not None:
            converted_dict[str(k)] = val
    return converted_dict


def get_pb_value(name: str | int | float, value: pb2.Value) -> pb2.Value:
    if isinstance(value, pb2.Value):
        return value
    if value is not None and is_list_of(value, str):
        return pb2.Value(multi_value=pb2.MultiValue(values=value))
    # The following `convert_element` done in single log validation
    # of features & tags. It is not done in bulk_log
    val = convert_element(value)
    if val is None:
        return None
    elif isinstance(val, (str, bool)):
        return pb2.Value(string=str(val))
    elif isinstance(val, int):
        return pb2.Value(int=val)
    elif isinstance(val, float):
        return pb2.Value(double=val)
    elif isinstance(val, Embedding):
        return pb2.Value(embedding=get_pb_embedding(val))
    else:
        raise TypeError(
            f"dimension '{name}' = {value} is type {type(value)}, but must be "
            "one of: bool, str, float, int, embedding"
        )


def get_pb_label(
    prediction_or_actual: str,
    value: str
    | bool
    | int
    | float
    | Tuple[str, float]
    | ObjectDetectionLabel
    | SemanticSegmentationLabel
    | InstanceSegmentationPredictionLabel
    | InstanceSegmentationActualLabel
    | RankingPredictionLabel
    | RankingActualLabel
    | MultiClassPredictionLabel
    | MultiClassActualLabel,
    model_type: ModelTypes,
) -> pb2.PredictionLabel | pb2.ActualLabel:
    value = convert_element(value)
    if model_type in NUMERIC_MODEL_TYPES:
        return _get_numeric_pb_label(prediction_or_actual, value)
    elif (
        model_type in CATEGORICAL_MODEL_TYPES
        or model_type == ModelTypes.GENERATIVE_LLM
    ):
        return _get_score_categorical_pb_label(prediction_or_actual, value)
    elif model_type == ModelTypes.OBJECT_DETECTION:
        return _get_cv_pb_label(prediction_or_actual, value)
    elif model_type == ModelTypes.RANKING:
        return _get_ranking_pb_label(value)
    elif model_type == ModelTypes.MULTI_CLASS:
        return _get_multi_class_pb_label(value)
    raise ValueError(
        f"model_type must be one of: {[mt.prediction_or_actual for mt in ModelTypes]} "
        f"Got "
        f"{model_type} instead."
    )


def get_pb_timestamp(time_overwrite):
    if time_overwrite is None:
        return None
    time = convert_element(time_overwrite)
    if not isinstance(time_overwrite, int):
        raise TypeError(
            f"time_overwrite {time_overwrite} is type {type(time_overwrite)}, "
            "but expects int (Unix epoch time in seconds)."
        )
    ts = Timestamp()
    ts.FromSeconds(time)
    return ts


def get_pb_embedding(val: Embedding) -> pb2.Embedding:
    if Embedding._is_valid_iterable(val.data):
        return pb2.Embedding(
            vector=val.vector,
            raw_data=pb2.Embedding.RawData(
                tokenArray=pb2.Embedding.TokenArray(tokens=val.data)
            ),
            link_to_data=StringValue(value=val.link_to_data),
        )
    elif isinstance(val.data, str):
        return pb2.Embedding(
            vector=val.vector,
            raw_data=pb2.Embedding.RawData(
                tokenArray=pb2.Embedding.TokenArray(tokens=[val.data])
                # Convert to list of 1 string
            ),
            link_to_data=StringValue(value=val.link_to_data),
        )
    elif val.data is None:
        return pb2.Embedding(
            vector=val.vector,
            link_to_data=StringValue(value=val.link_to_data),
        )

    return None


def _get_numeric_pb_label(
    prediction_or_actual: str,
    value: int | float,
) -> pb2.PredictionLabel | pb2.ActualLabel:
    if not isinstance(value, (int, float)):
        raise TypeError(
            f"Received {prediction_or_actual}_label = {value}, of type {type(value)}. "
            + f"{[mt.prediction_or_actual for mt in NUMERIC_MODEL_TYPES]} models accept labels of "
            f"type int or float"
        )
    if prediction_or_actual == "prediction":
        return pb2.PredictionLabel(numeric=value)
    elif prediction_or_actual == "actual":
        return pb2.ActualLabel(numeric=value)


def _get_score_categorical_pb_label(
    prediction_or_actual: str,
    value: bool | str | Tuple[str, float],
) -> pb2.PredictionLabel | pb2.ActualLabel:
    sc = pb2.ScoreCategorical()
    if isinstance(value, bool):
        sc.category.category = str(value)
    elif isinstance(value, str):
        sc.category.category = value
    elif isinstance(value, (int, float)):
        sc.score_value.value = value
    elif isinstance(value, tuple):
        # Expect Tuple[str,float]
        if value[1] is None:
            raise TypeError(
                f"Received {prediction_or_actual}_label = {value}, of type "
                f"{type(value)}[{type(value[0])}, None]. "
                f"{[mt.prediction_or_actual for mt in CATEGORICAL_MODEL_TYPES]} models accept "
                "values of type str, bool, or Tuple[str, float]"
            )
        if not isinstance(value[0], (bool, str)) or not isinstance(
            value[1], float
        ):
            raise TypeError(
                f"Received {prediction_or_actual}_label = {value}, of type "
                f"{type(value)}[{type(value[0])}, {type(value[1])}]. "
                f"{[mt.prediction_or_actual for mt in CATEGORICAL_MODEL_TYPES]} models accept "
                "values of type str, bool, or Tuple[str or bool, float]"
            )
        if isinstance(value[0], bool):
            sc.score_category.category = str(value[0])
        else:
            sc.score_category.category = value[0]
        sc.score_category.score = value[1]
    else:
        raise TypeError(
            f"Received {prediction_or_actual}_label = {value}, of type {type(value)}. "
            + f"{[mt.prediction_or_actual for mt in CATEGORICAL_MODEL_TYPES]} models accept values "
            f"of type str, bool, int, float or Tuple[str, float]"
        )
    if prediction_or_actual == "prediction":
        return pb2.PredictionLabel(score_categorical=sc)
    elif prediction_or_actual == "actual":
        return pb2.ActualLabel(score_categorical=sc)


def _get_cv_pb_label(
    prediction_or_actual: str,
    value: ObjectDetectionLabel
    | SemanticSegmentationLabel
    | InstanceSegmentationPredictionLabel
    | InstanceSegmentationActualLabel,
) -> pb2.PredictionLabel | pb2.ActualLabel:
    if isinstance(value, ObjectDetectionLabel):
        return _get_object_detection_pb_label(prediction_or_actual, value)
    elif isinstance(value, SemanticSegmentationLabel):
        return _get_semantic_segmentation_pb_label(prediction_or_actual, value)
    elif isinstance(value, InstanceSegmentationPredictionLabel):
        return _get_instance_segmentation_prediction_pb_label(value)
    elif isinstance(value, InstanceSegmentationActualLabel):
        return _get_instance_segmentation_actual_pb_label(value)
    else:
        raise InvalidValueType(
            "cv label",
            value,
            "ObjectDetectionLabel, SemanticSegmentationLabel, or "
            "InstanceSegmentationPredictionLabel for model type "
            f"{ModelTypes.OBJECT_DETECTION}",
        )


def _get_object_detection_pb_label(
    prediction_or_actual: str,
    value: ObjectDetectionLabel,
) -> pb2.PredictionLabel | pb2.ActualLabel:
    if not isinstance(value, ObjectDetectionLabel):
        raise InvalidValueType(
            "object detection label",
            value,
            f"ObjectDetectionLabel for model type {ModelTypes.OBJECT_DETECTION}",
        )
    od = pb2.ObjectDetection()
    bounding_boxes = []
    for i in range(len(value.bounding_boxes_coordinates)):
        coordinates = value.bounding_boxes_coordinates[i]
        category = value.categories[i]
        if value.scores is None:
            bounding_boxes.append(
                pb2.ObjectDetection.BoundingBox(
                    coordinates=coordinates, category=category
                )
            )
        else:
            score = value.scores[i]
            bounding_boxes.append(
                pb2.ObjectDetection.BoundingBox(
                    coordinates=coordinates,
                    category=category,
                    score=DoubleValue(value=score),
                )
            )

    od.bounding_boxes.extend(bounding_boxes)
    if prediction_or_actual == "prediction":
        return pb2.PredictionLabel(object_detection=od)
    elif prediction_or_actual == "actual":
        return pb2.ActualLabel(object_detection=od)


def _get_semantic_segmentation_pb_label(
    prediction_or_actual: str,
    value: SemanticSegmentationLabel,
) -> pb2.PredictionLabel | pb2.ActualLabel:
    if not isinstance(value, SemanticSegmentationLabel):
        raise InvalidValueType(
            "semantic segmentation label",
            value,
            f"SemanticSegmentationLabel for model type {ModelTypes.OBJECT_DETECTION}",
        )
    polygons = []
    for i in range(len(value.polygon_coordinates)):
        coordinates = value.polygon_coordinates[i]
        category = value.categories[i]
        polygons.append(
            pb2.SemanticSegmentationPolygon(
                coordinates=coordinates, category=category
            )
        )
    if prediction_or_actual == "prediction":
        cv_label = pb2.CVPredictionLabel()
        cv_label.semantic_segmentation_label.polygons.extend(polygons)
        return pb2.PredictionLabel(cv_label=cv_label)
    elif prediction_or_actual == "actual":
        cv_label = pb2.CVActualLabel()
        cv_label.semantic_segmentation_label.polygons.extend(polygons)
        return pb2.ActualLabel(cv_label=cv_label)


def _get_instance_segmentation_prediction_pb_label(
    value: InstanceSegmentationPredictionLabel,
) -> pb2.PredictionLabel | pb2.ActualLabel:
    if not isinstance(value, InstanceSegmentationPredictionLabel):
        raise InvalidValueType(
            "instance segmentation prediction label",
            value,
            f"InstanceSegmentationPredictionLabel for model type {ModelTypes.OBJECT_DETECTION}",
        )
    polygons = []
    for i in range(len(value.polygon_coordinates)):
        coordinates = value.polygon_coordinates[i]
        category = value.categories[i]
        score = (
            DoubleValue(value=value.scores[i])
            if value.scores is not None
            else None
        )
        bounding_box = (
            value.bounding_boxes_coordinates[i]
            if value.bounding_boxes_coordinates is not None
            else None
        )
        polygons.append(
            pb2.PredictionInstanceSegmentationPolygon(
                coordinates=coordinates,
                category=category,
                score=score,
                bbox_coordinates=bounding_box,
            )
        )
    prediction_instance_segmentation_label = (
        pb2.PredictionInstanceSegmentationLabel(
            polygons=polygons,
        )
    )
    cv_label = pb2.CVPredictionLabel(
        prediction_instance_segmentation_label=prediction_instance_segmentation_label,
    )
    return pb2.PredictionLabel(cv_label=cv_label)


def _get_instance_segmentation_actual_pb_label(
    value: InstanceSegmentationActualLabel,
) -> pb2.PredictionLabel | pb2.ActualLabel:
    if not isinstance(value, InstanceSegmentationActualLabel):
        raise InvalidValueType(
            "instance segmentation actual label",
            value,
            f"InstanceSegmentationActualLabel for model type {ModelTypes.OBJECT_DETECTION}",
        )
    polygons = []
    for i in range(len(value.polygon_coordinates)):
        coordinates = value.polygon_coordinates[i]
        category = value.categories[i]
        bounding_box = (
            value.bounding_boxes_coordinates[i]
            if value.bounding_boxes_coordinates is not None
            else None
        )
        polygons.append(
            pb2.ActualInstanceSegmentationPolygon(
                coordinates=coordinates,
                category=category,
                bbox_coordinates=bounding_box,
            )
        )
    actual_instance_segmentation_label = pb2.ActualInstanceSegmentationLabel(
        polygons=polygons,
    )
    cv_label = pb2.CVActualLabel(
        actual_instance_segmentation_label=actual_instance_segmentation_label,
    )
    return pb2.ActualLabel(cv_label=cv_label)


def _get_ranking_pb_label(
    value: RankingPredictionLabel | RankingActualLabel,
) -> pb2.PredictionLabel | pb2.ActualLabel:
    if not isinstance(value, (RankingPredictionLabel, RankingActualLabel)):
        raise InvalidValueType(
            "ranking label",
            value,
            f"RankingPredictionLabel or RankingActualLabel for model type {ModelTypes.RANKING}",
        )
    if isinstance(value, RankingPredictionLabel):
        rp = pb2.RankingPrediction()
        # If validation has passed, rank and group_id are guaranteed to be not None
        rp.rank = value.rank
        rp.prediction_group_id = value.group_id
        # score and label are optional
        if value.score is not None:
            rp.prediction_score.value = value.score
        if value.label is not None:
            rp.label = value.label
        return pb2.PredictionLabel(ranking=rp)
    elif isinstance(value, RankingActualLabel):
        ra = pb2.RankingActual()
        # relevance_labels and relevance_score are optional
        if value.relevance_labels is not None:
            ra.category.values.extend(value.relevance_labels)
        if value.relevance_score is not None:
            ra.relevance_score.value = value.relevance_score
        return pb2.ActualLabel(ranking=ra)


def _get_multi_class_pb_label(
    value: MultiClassPredictionLabel | MultiClassActualLabel,
) -> pb2.PredictionLabel | pb2.ActualLabel:
    if not isinstance(
        value, (MultiClassPredictionLabel, MultiClassActualLabel)
    ):
        raise InvalidValueType(
            "multi class label",
            value,
            f"MultiClassPredictionLabel or MultiClassActualLabel for model type {ModelTypes.MULTI_CLASS}",
        )
    if isinstance(value, MultiClassPredictionLabel):
        mc_pred = pb2.MultiClassPrediction()
        # threshold score map is not None in multi-label case
        if value.threshold_scores is not None:
            prediction_threshold_scores = {}
            # Validations checked prediction score map is not None
            for class_name, p_score in value.prediction_scores.items():
                # Validations checked threshold map contains all classes so safe to index w class_name
                multi_label_scores = (
                    pb2.MultiClassPrediction.MultiLabel.MultiLabelScores(
                        prediction_score=DoubleValue(value=p_score),
                        threshold_score=DoubleValue(
                            value=value.threshold_scores[class_name]
                        ),
                    )
                )
                prediction_threshold_scores[class_name] = multi_label_scores
            multi_label = pb2.MultiClassPrediction.MultiLabel(
                prediction_threshold_scores=prediction_threshold_scores
            )
            mc_pred = pb2.MultiClassPrediction(multi_label=multi_label)
        else:
            prediction_scores_double_values = {}
            # Validations checked prediction score map is not None
            for class_name, p_score in value.prediction_scores.items():
                prediction_scores_double_values[class_name] = DoubleValue(
                    value=p_score
                )
            single_label = pb2.MultiClassPrediction.SingleLabel(
                prediction_scores=prediction_scores_double_values,
            )
            mc_pred = pb2.MultiClassPrediction(single_label=single_label)
        p_label = pb2.PredictionLabel(multi_class=mc_pred)
        return p_label
    elif isinstance(value, MultiClassActualLabel):
        # Validations checked actual score map is not None
        actual_labels = []  # list of class names with actual score of 1
        for class_name, score in value.actual_scores.items():
            if float(score) == 1.0:
                actual_labels.append(class_name)
        mc_act = pb2.MultiClassActual(
            actual_labels=actual_labels,
        )
        return pb2.ActualLabel(multi_class=mc_act)
