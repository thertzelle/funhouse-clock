import datetime
import sched, time

starttime = time.time()

s = sched.scheduler(time.time, time.sleep)

def computeSecondsBinary(seconds):
    return list("{0:b}".format(seconds))

def roundWithBase(x, base=5):
    return base * round(x/base)

def computeSTEP(minute, rounded):
    last = (minute - rounded) % 10
    if last == 1:
        return ["S"]
    elif last == 2:
        return ["S", "T"]
    elif last == 3:
        return ["S", "T", "E"]
    elif last == 4:
        return ["S", "T", "E", "P"]
    else:
        return []

def getTime():
    now = datetime.datetime.now()
    roundedMinutes = roundWithBase(now.minute)
    print(now.strftime("%I"), now.minute, now.second, " - ", now.strftime("%I").lstrip('0'), roundedMinutes)
    print(computeSTEP(now.minute, roundedMinutes))
    print(computeSecondsBinary(now.second))

def tick(sc): 
    getTime()
    s.enter(1.0 - ((time.time() - starttime) % 1.0), 1, tick, (sc,))

s.enter(1.0 - ((time.time() - starttime) % 1.0), 1, tick, (s,))
s.run()