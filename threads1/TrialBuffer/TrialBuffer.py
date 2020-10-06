from threading import Condition


class TrialBuffer:
    cv = Condition()

    def __init__(self):
        self.trial = None
        self.isBufferEmpty = True

    def put_trial(self, trial):
        with TrialBuffer.cv:
            while not self.isBufferEmpty:
                TrialBuffer.cv.wait()
            self.isBufferEmpty = False
            self.trial = trial
            TrialBuffer.cv.notify_all()

    def take_trial(self):
        with TrialBuffer.cv:
            while self.isBufferEmpty:
                TrialBuffer.cv.wait()
            self.isBufferEmpty = True
            TrialBuffer.cv.notify_all()
            return self.trial
