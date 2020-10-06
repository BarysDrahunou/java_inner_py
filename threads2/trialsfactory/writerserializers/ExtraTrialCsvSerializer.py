from trialsfactory.writerserializers.TrialCsvSerializer import TrialCsvSerializer


class ExtraTrialCsvSerializer(TrialCsvSerializer):

    def serialize(self, extra_trial):
        return "{};{}".format(super().serialize(extra_trial), extra_trial.mark3)
