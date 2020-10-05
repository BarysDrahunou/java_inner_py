class TrialCsvSerializer:

    def serialize(self, trial):
        return "{};{};{};{}".format(trial.__class__.__name__,
                                    trial.account, trial.mark1,
                                    trial.mark2)
