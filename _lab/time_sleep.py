import time
import datetime

def get_ts():
    return int(time.mktime(datetime.datetime.now().timetuple()))
if __name__ == "__main__":

    print "100 times sleep of..."
    before_ts = get_ts()
    for i in range(100):
        time.sleep(1/50)
    after_ts = get_ts()
    print "1/50\t=>\t%s sec" % (after_ts - before_ts)

    before_ts = get_ts()
    for i in range(100):
        time.sleep(1.0/50)
    after_ts = get_ts()
    print "1.0/50\t=>\t%s sec" % (after_ts - before_ts)

    before_ts = get_ts()
    for i in range(100):
        time.sleep(100/5000)
    after_ts = get_ts()
    print "100/5000\t=>\t%s sec" % (after_ts - before_ts)

    before_ts = get_ts()
    for i in range(100):
        time.sleep(1*0.02)
    after_ts = get_ts()
    print "1*00.2\t=>\t%s sec" % (after_ts - before_ts)
