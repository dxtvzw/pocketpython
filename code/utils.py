import os
import time
import signal
import sys


def strip_text(text, prefix):
    text = text[len(prefix):]
    return text.strip()


def calc_func(func, *args):
    r, w = os.pipe()
    pid = os.fork()
    if pid == 0:
        os.close(r)
        mem = sys.stdout
        sys.stdout = os.fdopen(w, "w")
        result = func(*args)
        if result is not None:
            print(result)
        sys.stdout.close()
        sys.stdout = mem
        sys.exit(0)
    else:
        os.close(w)
        time.sleep(0.1)
        res = os.waitpid(pid, os.WNOHANG)
        if res == (pid, 0):
            r = os.fdopen(r)
            result = r.read()
            r.close()
            if len(result) != 0:
                return result
            else:
                return None
        elif res[0] == 0:
            os.kill(pid, signal.SIGTERM)
        os.close(r)
