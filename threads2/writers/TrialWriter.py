from utils.TrialConstants import FINAL_TRIAL


class TrialWriter:

    def __init__(self, blocking_queue, consumer, readers_amount):
        self.blocking_queue = blocking_queue
        self.consumer = consumer
        self.readers_amount = readers_amount

    def go(self):
        while self.readers_amount > 0:
            trial = self.blocking_queue.get()
            if trial == FINAL_TRIAL:
                self.readers_amount -= 1
            else:
                self.consumer.write_trial(trial)
        self.consumer.close()
