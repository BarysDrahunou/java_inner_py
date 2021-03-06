from utils.ExceptionHandling import WRITER_ALREADY_EXISTS
from utils.ReaderWriterConstants import \
    PATH_TO_FILE, WRITE_MODE, END_ARRAY, \
    BEGIN_ARRAY, COMMA, END_LINE, READER_CONSTANT
from utils.TrialConstants import TRIAL, \
    LIGHT_TRIAL, STRONG_TRIAL, EXTRA_TRIAL, camel_to_snake
from trialsfactory.writerserializers.ExtraTrialJsonSerializer \
    import ExtraTrialJsonSerializer
from trialsfactory.writerserializers.TrialJsonSerializer \
    import TrialJsonSerializer
import os


class JsonTrialWriter:
    __TRIAL_JSON_SERIALIZERS_DICT = {TRIAL: TrialJsonSerializer(),
                                     LIGHT_TRIAL: TrialJsonSerializer(),
                                     STRONG_TRIAL: TrialJsonSerializer(),
                                     EXTRA_TRIAL: ExtraTrialJsonSerializer()}

    def __init__(self, *args):
        writer = args[READER_CONSTANT]
        if os.path.isfile(PATH_TO_FILE + writer):
            raise ValueError(WRITER_ALREADY_EXISTS + writer)
        self.writer = open(PATH_TO_FILE + writer, mode=WRITE_MODE)
        self.writer.write(BEGIN_ARRAY)
        self.first = True

    def __enter__(self):
        return self

    def write_trial(self, trial):
        json_trial = JsonTrialWriter.__TRIAL_JSON_SERIALIZERS_DICT \
            .get(camel_to_snake(trial.__class__.__name__)) \
            .serialize(trial)
        if self.first:
            self.writer.write(json_trial)
            self.first = False
        else:
            self.writer.write(
                COMMA + END_LINE + json_trial)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.writer.write(END_ARRAY)
        self.writer.close()
