from utils.ExceptionHandling import INVALID_FIELD_MESSAGE, \
    FIELD_IS_NOT_A_NUMBER
from utils.TrialConstants import MIN_ACCEPTABLE_MARK, MAX_ACCEPTABLE_MARK


class TrialValidator:

    def __init__(self, trial_pattern):
        self.trial = trial_pattern

    def get_valid_trial(self, account, mark1, mark2, mark3):
        trial = self.trial.copy()
        TrialValidator.validate_fields_and_set(account, mark1, mark2, trial)
        return trial

    @staticmethod
    def validate_fields_and_set(account, mark1, mark2, trial):
        trial.set_account(TrialValidator._validate_string_field(account))
        trial.set_mark1(TrialValidator._validate_integer_field(mark1))
        trial.set_mark2(TrialValidator._validate_integer_field(mark2))
        return trial

    @staticmethod
    def _validate_string_field(field):
        if field.isalpha():
            return field
        else:
            raise ValueError(INVALID_FIELD_MESSAGE + str(field))

    @staticmethod
    def _validate_integer_field(field):
        value = TrialValidator.__get_integer_value_of_field(field)
        if MIN_ACCEPTABLE_MARK <= value <= MAX_ACCEPTABLE_MARK:
            return value
        else:
            raise ValueError(INVALID_FIELD_MESSAGE + str(field))

    @staticmethod
    def __get_integer_value_of_field(field):
        try:
            return int(field)
        except ValueError:
            raise ValueError(FIELD_IS_NOT_A_NUMBER + str(field))
