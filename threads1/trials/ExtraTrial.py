from trials.Trial import Trial
from utils.TrialConstants import CLASS_CONSTANT_FOR_EXTRA_TRIAL


class ExtraTrial(Trial):

    def __init__(self, account=None, mark1=None, mark2=None, mark3=None):
        super().__init__(account, mark1, mark2)
        self.mark3 = mark3

    def is_passed(self):
        return super().is_passed() and self.mark3 > CLASS_CONSTANT_FOR_EXTRA_TRIAL

    @staticmethod
    def copy():
        return ExtraTrial()

    def set_mark3(self, mark3):
        self.mark3 = mark3

    def get_mark3(self):
        return self.mark3

    def __eq__(self, other):
        if isinstance(other, ExtraTrial):
            return \
                self.account == other.account \
                and self.mark1 == other.mark1 \
                and self.mark2 == other.mark2 \
                and self.mark3 == other.mark3
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.account, self.mark1, self.mark2, self.mark3))

    def __str__(self):
        return "{}; {}; trial is passed - {}" \
            .format(super().fields_to_string(),
                    self.mark3, self.is_passed())
