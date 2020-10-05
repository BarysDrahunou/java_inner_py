import json
from json.decoder import JSONDecodeError

from utils.ReaderWriterConstants import READ_MODE, CLASS, ARGS, \
    ACCOUNT, MARK1, MARK2, MARK3, READER_CONSTANT, PATH_TO_FILE
from utils.TrialConstants import INITIAL_VALUE


class JsonTrialReader:

    def __init__(self, *args):
        reader = args[READER_CONSTANT]
        with open(PATH_TO_FILE + reader, mode=READ_MODE) as f:
            try:
                self.json = json.load(f)
                self.counter = len(self.json)
            except JSONDecodeError:
                self.json = None

    def next_trial(self):
        if self.json is not None and self.counter > 0:
            json_object = self.json[len(self.json) - self.counter]
            self.counter -= 1
            class_name = json_object.get(CLASS, None)
            args = json_object.get(ARGS, None)
            if (class_name and args) is None:
                return None
            account = args.get(ACCOUNT, None)
            mark1 = args.get(MARK1, INITIAL_VALUE)
            mark2 = args.get(MARK2, INITIAL_VALUE)
            mark3 = args.get(MARK3, INITIAL_VALUE)
            return [class_name, account, mark1, mark2, mark3]
        else:
            raise StopIteration

    def close(self):
        pass
