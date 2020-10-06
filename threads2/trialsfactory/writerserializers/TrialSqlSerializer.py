class TrialSqlSerializer:

    def serialize(self, trial):
        return *TrialSqlSerializer._get_common_values(trial), 0

    @staticmethod
    def _get_common_values(trial):
        return trial.__class__.__name__, trial.account, trial.mark1, trial.mark2
