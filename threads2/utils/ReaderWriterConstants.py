import configparser

PATH_TO_FILE = "resources/"
PATH_TO_LOGS = "logs/"
WRITE_MODE = "w"
READ_MODE = "r"
END_LINE = "\n"
COMMA = ","
CSV_SEPARATOR = ";"
DOT = "."
BEGIN_ARRAY = "["
END_ARRAY = "]"
CLASS = "class"
ARGS = "args"
ACCOUNT = "account"
MARK1 = "mark1"
MARK2 = "mark2"
MARK3 = "mark3"
CSV = "CSV"
JSON = "JSON"
SQL = "SQL"
EXTENSION_PARAMETER = 1
CSV_PARAMETERS_NUMBER = 4
CONFIG_FILE_NAME = "configuration.ini"
READER_WRITER_GROUP = "Readers and Writers"
READER_IN_CONFIG = "reader"
WRITER_IN_CONFIG = "writer"
QUEUE_SIZE = 1
READER_CONSTANT = 0
CONFIG_CONSTANT = 1
ZERO = 0


def get_config(configuration_file_name):
    config = configparser.ConfigParser()
    config.read(PATH_TO_FILE + configuration_file_name)
    return config
