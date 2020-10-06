from utils.TrialConstants import FINAL_TRIAL


class TrialWriter:

    def __init__(self, blocking_queue, consumer):
        self.blocking_queue = blocking_queue
        self.consumer = consumer

    def go(self):
        trial = self.blocking_queue.get()
        while trial != FINAL_TRIAL:
            self.consumer.write_trial(trial)
            trial = self.blocking_queue.get()
        self.consumer.close()
