from trials.Trial import Trial
from utils.TrialConstants import CLASS_CONSTANT


class StrongTrial(Trial):

    def __init__(self, account=None, mark1=None, mark2=None):
        super().__init__(account, mark1, mark2)

    def is_passed(self):
        return self.mark1 / 2 + self.mark2 > CLASS_CONSTANT

    @staticmethod
    def copy():
        return StrongTrial()
