import os

from utils.ExceptionHandling import EMPTY_WRITER
from utils.ReaderWriterConstants import CSV, JSON, \
    SQL, get_config, EXTENSION_PARAMETER
from writers.CsvTrialWriter import CsvTrialWriter
from writers.JsonTrialWriter import JsonTrialWriter
from writers.SqlTrialWriter import SqlTrialWriter

TRIAL_CONSUMERS_DICT = {CSV: CsvTrialWriter,
                        JSON: JsonTrialWriter,
                        SQL: SqlTrialWriter}


def get_consumer(configuration_file_name, group, writer_name_in_properties):
    config = get_config(configuration_file_name)
    writer = config.get(group, writer_name_in_properties)
    file_extension = os.path.splitext(writer)[EXTENSION_PARAMETER][EXTENSION_PARAMETER:]
    writer_implementation = TRIAL_CONSUMERS_DICT.get(file_extension.upper())
    try:
        return writer_implementation(writer, configuration_file_name)
    except TypeError:
        raise ValueError(EMPTY_WRITER)
