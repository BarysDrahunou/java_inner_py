from trialsfactory.writerserializers.TrialSqlSerializer\
    import TrialSqlSerializer


class ExtraTrialSqlSerializer(TrialSqlSerializer):

    def serialize(self, extra_trial):
        return *self._get_common_values(extra_trial), extra_trial.mark3
