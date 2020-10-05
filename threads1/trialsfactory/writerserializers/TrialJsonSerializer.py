import json

from utils.ReaderWriterConstants import CLASS, ARGS, \
    ACCOUNT, MARK1, MARK2


class TrialJsonSerializer:

    @staticmethod
    def serialize(trial):
        return json.dumps(TrialJsonSerializer._get_trial(trial))

    @staticmethod
    def _get_trial(trial):
        return {CLASS: trial.__class__.__name__,
                ARGS: {ACCOUNT: trial.account,
                       MARK1: trial.mark1, MARK2: trial.mark2}}
