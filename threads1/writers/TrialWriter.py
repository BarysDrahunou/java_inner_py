from utils.TrialConstants import FINAL_TRIAL


class TrialWriter:

    def __init__(self, buffer, consumer):
        self.buffer = buffer
        self.consumer = consumer

    def go(self):
        trial = self.buffer.take_trial()
        while trial != FINAL_TRIAL:
            self.consumer.write_trial(trial)
            trial = self.buffer.take_trial()
