import json
from trialsfactory.writerserializers.TrialJsonSerializer \
    import TrialJsonSerializer
from utils.ReaderWriterConstants import ARGS, MARK3


class ExtraTrialJsonSerializer(TrialJsonSerializer):

    @staticmethod
    def serialize(trial):
        return json.dumps(ExtraTrialJsonSerializer._get_trial(trial))

    @staticmethod
    def get_trial(trial):
        trial_json = super()._get_trial(trial)
        trial_json[ARGS][MARK3] = trial.mark3
        return trial_json
