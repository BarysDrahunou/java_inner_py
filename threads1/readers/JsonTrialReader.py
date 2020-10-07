import json
from json.decoder import JSONDecodeError

from trialsfactory import TrialsFactory
from utils.ExceptionHandling import get_logger_, CLASS_NAME_IS_EMPTY, \
    ARGS_IS_EMPTY, EMPTY_JSON
from utils.ReaderWriterConstants import READ_MODE, CLASS, ARGS, \
    ACCOUNT, MARK1, MARK2, MARK3, READER_CONSTANT, PATH_TO_FILE, ZERO
from utils.TrialConstants import INITIAL_VALUE, FINAL_TRIAL


class JsonTrialReader:
    logger = get_logger_()

    def __init__(self, *args):
        reader = args[READER_CONSTANT]
        with open(PATH_TO_FILE + reader, mode=READ_MODE) as f:
            try:
                self.json = json.load(f)
                self.counter = len(self.json)
            except JSONDecodeError:
                JsonTrialReader.logger.error(EMPTY_JSON)
                self.counter = ZERO

    def __enter__(self):
        return self

    def next_trial(self):
        if self.counter > ZERO:
            json_object = self.json[len(self.json) - self.counter]
            self.counter -= 1
            class_name = json_object.get(CLASS, None)
            if class_name is None:
                JsonTrialReader.logger.error(CLASS_NAME_IS_EMPTY)
                return None
            args = json_object.get(ARGS, None)
            if args is None:
                JsonTrialReader.logger.error(ARGS_IS_EMPTY)
                return None
            account = args.get(ACCOUNT, None)
            mark1 = args.get(MARK1, INITIAL_VALUE)
            mark2 = args.get(MARK2, INITIAL_VALUE)
            mark3 = args.get(MARK3, INITIAL_VALUE)
            return TrialsFactory.get_trial(class_name, account, mark1, mark2, mark3)
        else:
            return FINAL_TRIAL

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
