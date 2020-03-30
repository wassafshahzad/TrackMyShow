import re
from .constants import VALIDATOR_RULES


def link_validator(f):
    def inner(*args): 
        link = args[1]
        for rules in VALIDATOR_RULES:
            if(re.search(rules,link) == None):
                raise Exception("Validation Failed")
        return f(*args)
    return inner

def null_validation(f):
    def inner(*args):
        if(len(args)==1):
            raise Exception("Not Null")
        return f(*args)
    return inner

def episode_validator(f):
    def inner(*args):
        episode_number = args[1]
        if (type(episode_number) is not str or not  episode_number.isnumeric()):
            raise Exception("Invalid")
        return f(*args)
    return inner
