import time

sec_per_day = 24*60*60 
onset_rate = 0.51/sec_per_day
decline_rate = 0.96/sec_per_day

def ramp_up(delta_max, start_ramp):
    delta = (time.perf_counter()-start_ramp)*onset_rate
    if delta>=delta_max:
        delta = delta_max
    return delta

def ramp_down(delta_max, start_ramp):
    delta = delta_max - (time.perf_counter()-start_ramp)*decline_rate
    if delta<0:
        delta = 0
    return delta