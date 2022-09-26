from utils import *
from constants import *


def bot_eval(message):
        if len(message.text) > max_len_in:
            return "Too long command"
        else:
            result = calc_func(eval, strip_text(message.text, '/eval'))
            if result != None:
                if len(str(result)) <= max_len_out:
                    return result
                else:
                    return "The answer is too long to send you back"
            else:
                return "Invalid input or too slow to evaluate"


def bot_exec(message):
        if len(message.text) > max_len_in:
            return "Too long command"
        else:
            result = calc_func(exec, strip_text(message.text, '/exec'))
            if result != None:
                if len(str(result)) <= max_len_out:
                    return result
                else:
                    return "The answer is too long to send you back"
            else:
                return "Invalid input or too slow to evaluate"