import time

def reverse_str(s):
    out = []
    for i in range(len(s) - 1, -1, -1):
        out.append(s[i])
    return "".join(out)

def now_ms():
    return time.ticks_ms()

def elapsed(start, end):
    return time.ticks_diff(end, start) / 1000

