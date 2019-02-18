# a function to time another function

import time


def time_a_function(func, **kwargs):
    start_time = time.time()
    func(*tuple(value for _, value in kwargs.items()))
    end_time = time.time()
    return round(end_time - start_time, 5)

def stopwatch():
    print("Press ENTER to begin. Afterwards, press ENTER to \"click\" the stopwatch. Press Ctrl_C to quit.")
    input()
    print('Started.')
    start_time = time.time()
    last_time = start_time
    lapNum = 0
    try:
        while True:
            input()
            lap_time = round( time.time() - last_time, 2)
            total_time = round(time.time() - start_time, 2)
            print('Lap #%s: %s (%s)' % (lapNum, total_time, lap_time))
            lapNum += 1
            last_time = time.time()
    except KeyboardInterrupt:
        print("\nDone.")
