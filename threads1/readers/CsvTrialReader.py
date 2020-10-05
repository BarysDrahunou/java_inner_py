from utils.ReaderWriterConstants import PATH_TO_FILE, \
    CSV_PARAMETERS_NUMBER, CSV_SEPARATOR, READER_CONSTANT, READ_MODE
from utils.TrialConstants import INITIAL_VALUE


class CsvTrialReader:

    def __init__(self, *args):
        reader = args[READER_CONSTANT]
        self.file_reader = open(PATH_TO_FILE + reader, mode=READ_MODE)
        self.PARAMETERS_NUMBER = CSV_PARAMETERS_NUMBER

    def next_trial(self):
        trial = self.file_reader.readline().strip()
        if trial:
            trial = trial.split(CSV_SEPARATOR)
            class_name, account, mark1, mark2 = trial[:CSV_PARAMETERS_NUMBER]
            mark3 = INITIAL_VALUE
            if len(trial) > self.PARAMETERS_NUMBER:
                mark3 = trial[CSV_PARAMETERS_NUMBER]
            return [class_name, account, mark1, mark2, mark3]
        else:
            raise StopIteration

    def close(self):
        self.file_reader.close()
