from utils.TrialConstants import FINAL_TRIAL
from trialsfactory import TrialsFactory


class TrialReader:

    def __init__(self, blocking_queue, trial_dao):
        self.blocking_queue = blocking_queue
        self.trial_dao = trial_dao

    def run(self):
        try:
            while True:
                trial_args = self.trial_dao.next_trial()
                if trial_args is not None:
                    trial = TrialsFactory.get_trial(trial_args)
                    if trial is not None:
                        self.blocking_queue.put(trial)
        except StopIteration:
            self.blocking_queue.put(FINAL_TRIAL)
            self.trial_dao.close()
