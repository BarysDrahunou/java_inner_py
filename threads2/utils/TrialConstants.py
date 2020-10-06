import re

INITIAL_VALUE = -1
CLASS_CONSTANT = 50
CLASS_CONSTANT_FOR_MARK1 = 10
CLASS_CONSTANT_FOR_MARK2 = 20
CLASS_CONSTANT_FOR_EXTRA_TRIAL = 40
MIN_ACCEPTABLE_MARK = 0
MAX_ACCEPTABLE_MARK = 100
TRIAL = "TRIAL"
LIGHT_TRIAL = "LIGHT_TRIAL"
STRONG_TRIAL = "STRONG_TRIAL"
EXTRA_TRIAL = "EXTRA_TRIAL"
FINAL_TRIAL = "final"


def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).upper()
