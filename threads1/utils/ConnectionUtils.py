import mysql.connector
from mysql.connector import ProgrammingError

from utils.ReaderWriterConstants import get_config

COUNTER_START = 0
COUNTER_STEP = 1
TRIAL_PARAM = 0
CLASS_PARAM = 0
ACCOUNT_PARAM = 1
MARK1_PARAM = 2
MARK2_PARAM = 3
MARK3_PARAM = 4
SQL_PARAMS_NUMBER = 3
DATABASE_PARAM = 0
TABLE_PARAM = 1
SQL_GROUP = "SQL data"
USER = "username"
PASSWORD = "password"
HOST = "host"
SQL_FOR_CHECK_IS_TABLE_EXISTS = "SHOW TABLES LIKE '{}'"
SQL_FOR_DATABASE_CREATION = "CREATE DATABASE {}"
SQL_FOR_TABLE_CREATION = "CREATE TABLE {}.{} (ID int(15)  " \
                         "NOT NULL AUTO_INCREMENT ,CLASS VARCHAR(45)" \
                         " NOT NULL,ACCOUNT VARCHAR(45) NOT NULL," \
                         "MARK1 int(45) NOT NULL,MARK2 int(45) NOT NULL," \
                         "MARK3 int(45) NOT NULL,PRIMARY KEY (ID))"
SQL_FOR_TRIAL_INSERTION = "INSERT INTO {}.{} " \
                          "(CLASS, ACCOUNT, MARK1, MARK2, MARK3) " \
                          "VALUES (%s,%s,%s,%s,%s)"
SQL_FOR_SELECTION = "SELECT CLASS, ACCOUNT, MARK1, MARK2, MARK3 FROM {} LIMIT 1 OFFSET %s"


def is_database_exist(configuration_file_name, database_name):
    try:
        get_connection(configuration_file_name, database_name)
        return True
    except ProgrammingError:
        return False


def is_table_exist(configuration_file_name, database_name, table_name):
    try:
        connection = get_connection(configuration_file_name, database_name)
        statement = SQL_FOR_CHECK_IS_TABLE_EXISTS.format(table_name)
        cursor = connection.cursor()
        cursor.execute(statement)
        result = cursor.fetchone()
        return result is not None
    except ProgrammingError:
        return False


def get_connection(configuration_file_name, database_name=None):
    config = get_config(configuration_file_name)
    user = config.get(SQL_GROUP, USER)
    password = config.get(SQL_GROUP, PASSWORD)
    host = config.get(SQL_GROUP, HOST)
    if database_name is not None:
        return mysql.connector.connect(user=user, password=password,
                                       host=host,
                                       database=database_name)
    else:
        return mysql.connector.connect(user=user, password=password,
                                       host=host)
