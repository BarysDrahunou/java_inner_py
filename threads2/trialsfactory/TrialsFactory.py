from utils.ExceptionHandling import get_logger_, INCORRECT_CLASS_NAME
from utils.TrialConstants import camel_to_snake, TRIAL, LIGHT_TRIAL, STRONG_TRIAL, EXTRA_TRIAL
from trialsfactory.readervalidators.TrialValidator import TrialValidator
from trialsfactory.readervalidators.ExtraTrialValidator import ExtraTrialValidator
from trials import Trial, StrongTrial, LightTrial, ExtraTrial

trials_dict = {TRIAL: TrialValidator(Trial.Trial()),
               LIGHT_TRIAL: TrialValidator(LightTrial.LightTrial()),
               STRONG_TRIAL: TrialValidator(StrongTrial.StrongTrial()),
               EXTRA_TRIAL: ExtraTrialValidator(ExtraTrial.ExtraTrial()),
               }
logger = get_logger_()


def get_trial(class_name, account, mark1, mark2, mark3):
    try:
        return trials_dict.get(camel_to_snake(class_name)) \
            .get_valid_trial(account, mark1, mark2, mark3)
    except ValueError as e:
        logger.error(*e.args)
        return None
    except AttributeError:
        logger.error(INCORRECT_CLASS_NAME + class_name)
        return None
    except TypeError as e:
        logger.error(e)
        return None
