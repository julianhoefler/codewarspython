import time

# Kata: https://www.codewars.com/kata/52685f7382004e774f0001f7

def make_readable(seconds):
    return time.strftime(str(int(seconds / 3600)).zfill(2) + ':%M:%S', time.gmtime(seconds))