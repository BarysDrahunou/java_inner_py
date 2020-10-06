from trials.Trial import Trial
from utils.TrialConstants import CLASS_CONSTANT_FOR_MARK1, \
    CLASS_CONSTANT_FOR_MARK2


class LightTrial(Trial):

    def __init__(self, account=None, mark1=None, mark2=None):
        super().__init__(account, mark1, mark2)

    def is_passed(self):
        return self.mark1 > CLASS_CONSTANT_FOR_MARK1 \
               and self.mark2 > CLASS_CONSTANT_FOR_MARK2

    @staticmethod
    def copy():
        return LightTrial()
