from trialsfactory import TrialsFactory
from utils.ConnectionUtils import DATABASE_PARAM, TABLE_PARAM, \
    SQL_FOR_SELECTION, get_connection, COUNTER_START, \
    TRIAL_PARAM, COUNTER_STEP, CLASS_PARAM, ACCOUNT_PARAM, \
    MARK1_PARAM, MARK2_PARAM, MARK3_PARAM, SQL_PARAMS_NUMBER, is_table_exist
from utils.ExceptionHandling import get_logger_, \
    NOT_ENOUGH_PARAMETERS_SQL, TABLE_DOES_NOT_EXIST
from utils.ReaderWriterConstants import DOT, READER_CONSTANT, \
    CONFIG_CONSTANT
from utils.TrialConstants import FINAL_TRIAL


class SqlTrialReader:
    logger = get_logger_()

    def __init__(self, *args):
        reader = args[READER_CONSTANT]
        configuration_file_name = args[CONFIG_CONSTANT]
        params = reader.split(DOT)
        if len(params) < SQL_PARAMS_NUMBER:
            raise ValueError(NOT_ENOUGH_PARAMETERS_SQL + reader)
        database_name = params[DATABASE_PARAM]
        table_name = params[TABLE_PARAM]
        if is_table_exist(configuration_file_name, database_name, table_name):
            self.SQL = SQL_FOR_SELECTION.format(table_name)
            self.counter = COUNTER_START
            self.connection = get_connection(configuration_file_name, database_name)
            self.cursor = self.connection.cursor(prepared=True)
        else:
            raise ValueError(TABLE_DOES_NOT_EXIST.format(database_name, table_name))

    def __enter__(self):
        return self

    def next_trial(self):
        self.cursor.execute(self.SQL, str(self.counter))
        trial = self.cursor.fetchall()
        if len(trial) > TRIAL_PARAM:
            self.counter += COUNTER_STEP
            return TrialsFactory.get_trial(trial[TRIAL_PARAM][CLASS_PARAM],
                                           trial[TRIAL_PARAM][ACCOUNT_PARAM],
                                           trial[TRIAL_PARAM][MARK1_PARAM],
                                           trial[TRIAL_PARAM][MARK2_PARAM],
                                           trial[TRIAL_PARAM][MARK3_PARAM])
        else:
            return FINAL_TRIAL

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
