from utils.TrialConstants import FINAL_TRIAL


class TrialReader:

    def __init__(self, buffer, trial_dao):
        self.buffer = buffer
        self.trial_dao = trial_dao

    def run(self):
        trial = self.trial_dao.next_trial()
        while trial != FINAL_TRIAL:
            if trial is not None:
                self.buffer.put_trial(trial)
            trial = self.trial_dao.next_trial()
        self.buffer.put_trial(trial)
