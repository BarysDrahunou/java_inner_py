from utils.ConnectionUtils import DATABASE_PARAM, TABLE_PARAM, \
    SQL_FOR_SELECTION, get_connection, COUNTER_START, \
    TRIAL_PARAM, COUNTER_STEP, CLASS_PARAM, ACCOUNT_PARAM, \
    MARK1_PARAM, MARK2_PARAM, MARK3_PARAM
from utils.ReaderWriterConstants import DOT, READER_CONSTANT, CONFIG_CONSTANT


class SqlTrialReader:

    def __init__(self, *args):
        reader = args[READER_CONSTANT]
        configuration_file_name = args[CONFIG_CONSTANT]
        params = reader.split(DOT)
        database_name = params[DATABASE_PARAM]
        table_name = params[TABLE_PARAM]
        self.SQL = SQL_FOR_SELECTION.format(table_name)
        self.counter = COUNTER_START
        self.connection = get_connection(database_name, configuration_file_name)
        self.cursor = self.connection.cursor(prepared=True)

    def next_trial(self):
        self.cursor.execute(self.SQL, str(self.counter))
        trial = self.cursor.fetchall()
        if len(trial) > TRIAL_PARAM:
            self.counter += COUNTER_STEP
            return [trial[TRIAL_PARAM][CLASS_PARAM], trial[TRIAL_PARAM][ACCOUNT_PARAM],
                    trial[TRIAL_PARAM][MARK1_PARAM], trial[TRIAL_PARAM][MARK2_PARAM],
                    trial[TRIAL_PARAM][MARK3_PARAM]]
        else:
            raise StopIteration

    def close(self):
        self.connection.close()
