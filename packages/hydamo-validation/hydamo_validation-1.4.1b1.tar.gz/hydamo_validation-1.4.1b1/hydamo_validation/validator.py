"""Function to be picked up by the api."""

from typing import List, Callable, Literal, Union
from pathlib import Path
import pandas as pd
from functools import partial
import json
import shutil
import logging
from jsonschema import validate, ValidationError
from json import JSONDecodeError
from hydamo_validation import logical_validation
from hydamo_validation.utils import Timer
from hydamo_validation.summaries import LayersSummary, ResultSummary
from hydamo_validation.datasets import DataSets
from hydamo_validation.datamodel import HyDAMO
from hydamo_validation.syntax_validation import (
    datamodel_layers,
    missing_layers,
    fields_syntax,
)
import traceback

OUTPUT_TYPES = ["geopackage", "geojson", "csv"]
LOG_LEVELS = Literal["INFO", "DEBUG"]
INCLUDE_COLUMNS = ["nen3610id", "code", "categorieoppwaterlichaam"]
SCHEMAS_PATH = Path(__file__).parent.joinpath(r"./schemas")
HYDAMO_SCHEMAS_PATH = SCHEMAS_PATH.joinpath("hydamo")
RULES_SCHEMAS_PATH = SCHEMAS_PATH.joinpath("rules")


def _read_schema(version, schemas_path):
    schema_json = schemas_path.joinpath(rf"rules/rules_{version}.json").resolve()
    with open(schema_json) as src:
        schema = json.load(src)
    return schema


def _init_logger(log_level):
    """Init logger for validator."""
    logger = logging.getLogger(__name__)
    logger.setLevel(getattr(logging, log_level))
    return logger


def _add_log_file(logger, log_file):
    """Add log-file to existing logger"""
    fh = logging.FileHandler(log_file)
    fh.setFormatter(
        logging.Formatter("%(asctime)s %(name)s %(levelname)s - %(message)s")
    )
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    return logger


def _close_log_file(logger):
    """Remove log-file from existing logger"""
    for h in logger.handlers:
        h.close()
        logger.removeHandler(h)


def _log_to_results(log_file, result_summary):
    result_summary.log = log_file.read_text().split("\n")


def read_validation_rules(
    validation_rules_json: Path,
    result_summary: Union[ResultSummary, None] = None,
) -> dict:
    """_summary_

    Parameters
    ----------
    validation_rules_json : Path
        Path to ValidationRules.json()
    result_summary : Union[ResultSummary, None]
        ResultSummary to write exceptions to if specified. Default is None.

    Returns
    -------
    dict
        Validated validationrules

    Raises
    ------
    Exceptions
        - the file with validationrules is not a valid JSON (see exception)
        - schema version cannot be read from validation rules (see exception)
        - validation rules invalid according to json-schema (see exception)
    """
    try:
        validation_rules_sets = json.loads(validation_rules_json.read_text())
    except JSONDecodeError as e:
        if result_summary is not None:
            result_summary.error = [
                "the file with validationrules is not a valid JSON (see exception)"
            ]
        raise e
    try:
        rules_version = validation_rules_sets["schema"]
        schema = _read_schema(rules_version, SCHEMAS_PATH)
    except FileNotFoundError as e:
        if result_summary is not None:
            result_summary.error = [
                "schema version cannot be read from validation rules (see exception)"
            ]
        raise e
    try:
        validate(validation_rules_sets, schema)
    except ValidationError as e:
        if result_summary is not None:
            result_summary.error = [
                "validation rules invalid according to json-schema (see exception)"
            ]
        raise e

    return validation_rules_sets


def validator(
    output_types: List[str] = OUTPUT_TYPES,
    log_level: Literal["INFO", "DEBUG"] = "INFO",
    coverages: dict = {},
) -> Callable:
    """

    Parameters
    ----------
    output_types : List[str], optional
        The types of output files that will be written. Options are
        ["geojson", "csv", "geopackage"]. By default all will be written
    log_level : Literal['INFO', 'DEBUG'], optional
        Level for logger. The default is "INFO".
    coverages : dict, optional
       Location of coverages. E.g. {"AHN: path_to_ahn_dir} The default is {}.

    Returns
    -------
    Callable[[str], dict]
        Partial of _validator function

    """

    return partial(
        _validator,
        output_types=output_types,
        log_level=log_level,
        coverages=coverages,
    )


def _validator(
    directory: str,
    output_types: List[str] = OUTPUT_TYPES,
    log_level: Literal["INFO", "DEBUG"] = "INFO",
    coverages: dict = {},
    raise_error: bool = False,
):
    """
    Parameters
    ----------
    directory : str
        Directory with datasets sub-directory and validation_rules.json
    output_types : List[str], optional
        The types of output files that will be written. Options are
        ["geojson", "csv", "geopackage"]. By default all will be written
    log_level : Literal['INFO', 'DEBUG'], optional
        Level for logger. The default is "INFO".
    coverages : dict, optional
       Location of coverages. E.g. {"AHN: path_to_ahn_dir} The default is {}.
    raise_error: bool, optional
        Will raise an error (or not) when Exception is raised. The default is False

    Returns
    -------
    HyDAMO, LayersSummary, ResultSummary
        Will return a tuple with a filled HyDAMO datamodel, layers_summary and result_summary

    """
    timer = Timer()
    try:
        results_path = None
        dir_path = Path(directory)
        logger = _init_logger(
            log_level=log_level,
        )

        logger.info("init validatie")
        date_check = pd.Timestamp.now().isoformat()
        result_summary = ResultSummary(date_check=date_check)
        layers_summary = LayersSummary(date_check=date_check)
        # check if all files are present
        # create a results_path
        permission_error = False
        if dir_path.exists():
            results_path = dir_path.joinpath("results")
            if results_path.exists():
                try:
                    shutil.rmtree(results_path)
                except PermissionError:
                    permission_error = True
            results_path.mkdir(parents=True, exist_ok=True)
        else:
            raise FileNotFoundError(f"{dir_path.absolute().resolve()} does not exist")

        log_file = results_path.joinpath("validator.log")
        logger = _add_log_file(logger, log_file=log_file)
        logger.info("start validatie")
        if permission_error:
            logger.warning(
                f"Kan pad {results_path} niet verwijderen. Dit kan later tot problemen leiden!"
            )
        dataset_path = dir_path.joinpath("datasets")
        validation_rules_json = dir_path.joinpath("validationrules.json")
        missing_paths = []
        for path in [dataset_path, validation_rules_json]:
            if not path.exists():
                missing_paths += [str(path)]
        if missing_paths:
            result_summary.error += [f"missing_paths: {','.join(missing_paths)}"]
            raise FileNotFoundError(f"missing_paths: {','.join(missing_paths)}")
        else:
            validation_rules_sets = read_validation_rules(
                validation_rules_json, result_summary
            )

        # check if output-files are supported
        unsupported_output_types = [
            item for item in output_types if item not in OUTPUT_TYPES
        ]
        if unsupported_output_types:
            error_message = (
                r"unsupported output types: " f"{','.join(unsupported_output_types)}"
            )
            result_summary.error += [error_message]
            raise TypeError(error_message)

        # set coverages
        if coverages:
            for key, item in coverages.items():
                logical_validation.general_functions._set_coverage(key, item)

        # start validation
        # read data-model
        result_summary.status = "define data-model"
        try:
            hydamo_version = validation_rules_sets["hydamo_version"]
            datamodel = HyDAMO(version=hydamo_version, schemas_path=HYDAMO_SCHEMAS_PATH)
        except Exception as e:
            result_summary.error = ["datamodel cannot be defined (see exception)"]
            raise e

        # validate dataset syntax
        result_summary.status = "syntax-validation (layers)"
        datasets = DataSets(dataset_path)

        result_summary.dataset_layers = datasets.layers

        ## validate syntax of datasets on layers-level and append to result
        logger.info("start syntax-validatie van object-lagen")
        valid_layers = datamodel_layers(datamodel.layers, datasets.layers)
        result_summary.missing_layers = missing_layers(
            datamodel.layers, datasets.layers
        )

        ## validate valid_layers on fields-level and add them to data_model
        result_summary.status = "syntax-validation (fields)"
        syntax_result = []

        ## get status_object if any
        status_object = None
        if "status_object" in validation_rules_sets.keys():
            status_object = validation_rules_sets["status_object"]

        for layer in valid_layers:
            logger.info(f"{layer}: inlezen")

            # read layer
            gdf, schema = datasets.read_layer(
                layer, result_summary=result_summary, status_object=status_object
            )
            if gdf.empty:  # pass if gdf is empty. Most likely due to mall-formed or ill-specifiec status_object
                logger.warning(
                    f"{layer}: geen objecten ingelezen. Zorg dat alle waarden in de kolom 'status_object' voorkomen in {status_object}"
                )
                continue

            layer = layer.lower()
            for col in INCLUDE_COLUMNS:
                if col not in gdf.columns:
                    gdf[col] = None
                    schema["properties"][col] = "str"

            logger.info(f"{layer}: syntax-validatie")
            gdf, result_gdf = fields_syntax(
                gdf,
                schema=schema,
                validation_schema=datamodel.validation_schemas[layer],
                keep_columns=INCLUDE_COLUMNS,
            )

            # Add the syntax-validation result to the results_summary
            layers_summary.set_data(result_gdf, layer, schema["geometry"])
            # Add the corrected datasets_layer data to the datamodel.
            if gdf.empty:
                logger.warning(
                    f"{layer}: geen valide objecten na syntax-validatie. Inspecteer 'syntax_oordeel' in de resultaten; deze is false voor alle objecten. De laag zal genegeerd worden in de (topo)logische validatie."
                )
            else:
                datamodel.set_data(gdf, layer, index_col=None)
            syntax_result += [layer]

        # do logical validation: append result to layers_summary
        result_summary.status = "logical validation"
        logger.info("start (topo)logische validatie van object-lagen")
        layers_summary, result_summary = logical_validation.execute(
            datamodel,
            validation_rules_sets,
            layers_summary,
            result_summary,
            logger,
            raise_error,
        )

        # finish validation and export results
        logger.info("exporteren resultaten")
        result_summary.status = "export results"
        result_layers = layers_summary.export(results_path, output_types)
        result_summary.result_layers = result_layers
        result_summary.error_layers = [
            i for i in datasets.layers if i.lower() not in result_layers
        ]
        result_summary.syntax_result = syntax_result
        result_summary.validation_result = [
            i["object"]
            for i in validation_rules_sets["objects"]
            if i["object"] in result_layers
        ]
        result_summary.success = True
        result_summary.status = "finished"
        result_summary.duration = timer.report()
        logger.info(f"klaar in {result_summary.duration:.2f} seconden")

        _log_to_results(log_file, result_summary)
        result_summary.to_json(results_path)

        _close_log_file(logger)

        return datamodel, layers_summary, result_summary

    except Exception as e:
        stacktrace = rf"\n{traceback.format_exc(limit=0, chain=False)}".split("\n")
        if result_summary.error is not None:
            result_summary.error += stacktrace
        else:
            result_summary.error = stacktrace
        if results_path is not None:
            result_layers = layers_summary.export(results_path, output_types)
            _log_to_results(log_file, result_summary)
            result_summary.to_json(results_path)
        if raise_error:
            raise e
        else:
            result_summary.to_dict()

        _close_log_file(logger)

        return None
