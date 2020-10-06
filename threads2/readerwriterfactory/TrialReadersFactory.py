import os

from utils.ExceptionHandling import EMPTY_READER, get_logger_
from utils.ReaderWriterConstants import get_config, \
    CSV, JSON, SQL, EXTENSION_PARAMETER, CSV_SEPARATOR
from readers.CsvTrialReader import CsvTrialReader
from readers.JsonTrialReader import JsonTrialReader
from readers.SqlTrialReader import SqlTrialReader


class TrialReadersFactory:
    TRIAL_DAO_PATTERNS_DICT = {CSV: CsvTrialReader,
                               JSON: JsonTrialReader,
                               SQL: SqlTrialReader}
    logger = get_logger_()

    def __init__(self):
        self.trial_dao_list = list()

    def get_trial_dao(self, configuration_file_name, group, readers_name_in_properties):
        config = get_config(configuration_file_name)
        reader = config.get(group, readers_name_in_properties)
        readers = reader.split(CSV_SEPARATOR)
        for reader in readers:
            try:
                file_extension = os.path.splitext(reader)[EXTENSION_PARAMETER][EXTENSION_PARAMETER:]
                reader_implementation = TrialReadersFactory \
                    .TRIAL_DAO_PATTERNS_DICT.get(file_extension.upper())
                self.trial_dao_list.append(reader_implementation(reader, configuration_file_name))
            except TypeError:
                TrialReadersFactory.logger.error(EMPTY_READER)
            except (FileNotFoundError, ValueError) as e:
                TrialReadersFactory.logger.error(e)
        return self.trial_dao_list
