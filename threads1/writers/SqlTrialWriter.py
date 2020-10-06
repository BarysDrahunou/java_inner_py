from mysql.connector import ProgrammingError
from utils.ConnectionUtils import DATABASE_PARAM, TABLE_PARAM, is_table_exist, \
    is_database_exist, get_connection, \
    SQL_FOR_DATABASE_CREATION, SQL_FOR_TABLE_CREATION, SQL_FOR_TRIAL_INSERTION
from utils.ExceptionHandling import TABLE_ALREADY_EXIST, SQL_EXCEPTION
from utils.ReaderWriterConstants import DOT, READER_CONSTANT, CONFIG_CONSTANT
from utils.TrialConstants import TRIAL, STRONG_TRIAL, EXTRA_TRIAL, LIGHT_TRIAL, camel_to_snake
from trialsfactory.writerserializers.ExtraTrialSqlSerializer \
    import ExtraTrialSqlSerializer
from trialsfactory.writerserializers.TrialSqlSerializer import TrialSqlSerializer


class SqlTrialWriter:
    __TRIAL_SQL_SERIALIZERS_DICT = {TRIAL: TrialSqlSerializer(),
                                    LIGHT_TRIAL: TrialSqlSerializer(),
                                    STRONG_TRIAL: TrialSqlSerializer(),
                                    EXTRA_TRIAL: ExtraTrialSqlSerializer()}

    def __init__(self, *args):
        writer = args[READER_CONSTANT]
        configuration_file_name = args[CONFIG_CONSTANT]
        params = writer.split(DOT)
        database_name = params[DATABASE_PARAM]
        table_name = params[TABLE_PARAM]
        try:
            if not is_table_exist(configuration_file_name, database_name, table_name):
                if not is_database_exist(configuration_file_name, database_name):
                    connection = get_connection(configuration_file_name)
                    cursor = connection.cursor()
                    cursor.execute(SQL_FOR_DATABASE_CREATION.format(database_name))
                else:
                    connection = get_connection(configuration_file_name, database_name)
                    cursor = connection.cursor()
                cursor.execute(SQL_FOR_TABLE_CREATION
                               .format(database_name, table_name))
                self.database_name = database_name
                self.table_name = table_name
                self.cursor = cursor
                self.connection = connection
            else:
                raise ValueError(TABLE_ALREADY_EXIST.format(database_name, table_name))
        except ProgrammingError:
            raise ValueError(SQL_EXCEPTION.format(database_name, table_name))

    def write_trial(self, trial):
        sql = SQL_FOR_TRIAL_INSERTION.format(self.database_name, self.table_name)
        values = SqlTrialWriter.__TRIAL_SQL_SERIALIZERS_DICT \
            .get(camel_to_snake(trial.__class__.__name__)) \
            .serialize(trial)
        self.cursor.execute(sql, values)
        self.connection.commit()

    def close(self):
        self.connection.close()
