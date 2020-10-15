import logging.config
import os

from utils.ReaderWriterConstants import PATH_TO_LOGS

PATH_TO_CONFIG_FILE = "resources/logging.conf"
FILE_LOGGER = "fileLogger"
INVALID_FIELD_MESSAGE = "Value of this field is invalid: "
TOO_FEW_ARGUMENTS_MESSAGE = "Too few arguments in reader"
INCORRECT_CLASS_NAME = "Incorrect class name: "
FIELD_IS_NOT_A_NUMBER = "This value is not a number: "
CLASS_NAME_IS_EMPTY = "Class name is empty"
ARGS_IS_EMPTY = "Args is empty"
EMPTY_JSON = "Empty json file"
NOT_ENOUGH_PARAMETERS_SQL = "Must be at least 3 parameters: "
TABLE_DOES_NOT_EXIST = "Table doesn't exist: {}.{}"
TABLE_ALREADY_EXIST = "Table already exist: {}.{}"
EMPTY_READER = "Reader is empty or not sql, json or csv format"
EMPTY_WRITER = "Writer is empty or not sql, json or csv format"
SQL_EXCEPTION = "Some problems with database {}.{}"
WRITER_ALREADY_EXISTS = "Writer already exists: "


def get_logger_():
    if not os.path.exists(PATH_TO_LOGS):
        os.makedirs(PATH_TO_LOGS)
    logging.config.fileConfig(fname=PATH_TO_CONFIG_FILE)
    return logging.getLogger(FILE_LOGGER)
