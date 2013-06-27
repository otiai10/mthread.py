import threading
import time

def work():
  """thread worker function"""
  for i in range(5):
    print "This is %s => seq %s" % (threading.currentThread().getName(), i)
    time.sleep(1)
  return

if __name__ == "__main__":

  threads = []
  for i in range(10):
    t = threading.Thread(target=work)
    threads.append(t)
    t.start()
 
  print "***** END OF MAIN *****" 
  print len(threads)
