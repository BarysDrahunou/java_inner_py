from utils.TrialConstants import FINAL_TRIAL


class TrialReader:

    def __init__(self, blocking_queue, trial_dao):
        self.blocking_queue = blocking_queue
        self.trial_dao = trial_dao

    def run(self):
        trial = self.trial_dao.next_trial()
        while trial != FINAL_TRIAL:
            if trial is not None:
                self.blocking_queue.put(trial)
            trial = self.trial_dao.next_trial()
        self.blocking_queue.put(FINAL_TRIAL)
        self.trial_dao.close()
