from trialsfactory import TrialsFactory
from utils.ExceptionHandling import get_logger_, TOO_FEW_ARGUMENTS_MESSAGE
from utils.ReaderWriterConstants import PATH_TO_FILE, \
    CSV_PARAMETERS_NUMBER, CSV_SEPARATOR, READER_CONSTANT, READ_MODE
from utils.TrialConstants import INITIAL_VALUE, FINAL_TRIAL


class CsvTrialReader:
    logger = get_logger_()

    def __init__(self, *args):
        reader = args[READER_CONSTANT]
        self.file_reader = open(PATH_TO_FILE + reader, mode=READ_MODE)

    def next_trial(self):
        trial = self.file_reader.readline().strip()
        if trial:
            trial = trial.split(CSV_SEPARATOR)
            if len(trial) < CSV_PARAMETERS_NUMBER:
                CsvTrialReader.logger.error(TOO_FEW_ARGUMENTS_MESSAGE)
                return None
            class_name, account, mark1, mark2 = trial[:CSV_PARAMETERS_NUMBER]
            mark3 = INITIAL_VALUE
            if len(trial) > CSV_PARAMETERS_NUMBER:
                mark3 = trial[CSV_PARAMETERS_NUMBER]
            return TrialsFactory.get_trial(class_name, account, mark1, mark2, mark3)
        else:
            return FINAL_TRIAL

    def close(self):
        self.file_reader.close()
