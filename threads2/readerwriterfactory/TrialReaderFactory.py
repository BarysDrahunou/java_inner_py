import os

from utils.ExceptionHandling import EMPTY_READER
from utils.ReaderWriterConstants import get_config, \
    CSV, JSON, SQL, EXTENSION_PARAMETER
from readers.CsvTrialReader import CsvTrialReader
from readers.JsonTrialReader import JsonTrialReader
from readers.SqlTrialReader import SqlTrialReader

TRIAL_DAO_PATTERNS_DICT = {CSV: CsvTrialReader,
                           JSON: JsonTrialReader,
                           SQL: SqlTrialReader}


def get_trial_dao(configuration_file_name, group, reader_name_in_properties):
    config = get_config(configuration_file_name)
    reader = config.get(group, reader_name_in_properties)
    file_extension = os.path.splitext(reader)[EXTENSION_PARAMETER][EXTENSION_PARAMETER:]
    reader_implementation = TRIAL_DAO_PATTERNS_DICT.get(file_extension.upper())
    try:
        return reader_implementation(reader, configuration_file_name)
    except TypeError:
        raise ValueError(EMPTY_READER)
