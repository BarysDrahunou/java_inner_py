from utils.TrialConstants import camel_to_snake, TRIAL, LIGHT_TRIAL, STRONG_TRIAL, EXTRA_TRIAL
from trialsfactory.readervalidators.TrialValidator import TrialValidator
from trialsfactory.readervalidators.ExtraTrialValidator import ExtraTrialValidator
from trials import Trial, StrongTrial, LightTrial, ExtraTrial

trials_dict = {TRIAL: TrialValidator(Trial.Trial()),
               LIGHT_TRIAL: TrialValidator(LightTrial.LightTrial()),
               STRONG_TRIAL: TrialValidator(StrongTrial.StrongTrial()),
               EXTRA_TRIAL: ExtraTrialValidator(ExtraTrial.ExtraTrial()),
               }


def get_trial(trial_args):
    try:
        class_name, account, mark1, mark2, mark3 = trial_args
        return trials_dict.get(camel_to_snake(class_name)) \
            .get_valid_trial(account, mark1, mark2, mark3)
    except ValueError:
        return None
    except AttributeError:
        return None
