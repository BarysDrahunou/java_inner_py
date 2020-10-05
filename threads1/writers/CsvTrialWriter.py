from utils.ReaderWriterConstants import PATH_TO_FILE, \
    WRITE_MODE, END_LINE, READER_CONSTANT
from utils.TrialConstants \
    import TRIAL, LIGHT_TRIAL, STRONG_TRIAL, EXTRA_TRIAL, camel_to_snake
from trialsfactory.writerserializers.ExtraTrialCsvSerializer \
    import ExtraTrialCsvSerializer
from trialsfactory.writerserializers.TrialCsvSerializer \
    import TrialCsvSerializer

TRIAL_CSV_SERIALIZERS_DICT = {TRIAL: TrialCsvSerializer(),
                              LIGHT_TRIAL: TrialCsvSerializer(),
                              STRONG_TRIAL: TrialCsvSerializer(),
                              EXTRA_TRIAL: ExtraTrialCsvSerializer()}


class CsvTrialWriter:

    def __init__(self, *args):
        writer = args[READER_CONSTANT]
        self.writer = open(PATH_TO_FILE + writer, mode=WRITE_MODE)

    def write_trial(self, trial):
        self.writer.write(TRIAL_CSV_SERIALIZERS_DICT
                          .get(camel_to_snake(trial.__class__.__name__))
                          .serialize(trial) + END_LINE)

    def close(self):
        self.writer.close()
