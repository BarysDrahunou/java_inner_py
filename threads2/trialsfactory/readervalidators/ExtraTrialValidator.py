from trialsfactory.readervalidators.TrialValidator import TrialValidator


class ExtraTrialValidator(TrialValidator):

    def __init__(self, trial_pattern):
        super().__init__(trial_pattern)

    def get_valid_trial(self, account, mark1, mark2, mark3):
        trial = self.trial.copy()
        super().validate_fields_and_set(account, mark1, mark2, trial)
        trial.set_mark3(super()._validate_integer_field(mark3))
        return trial
