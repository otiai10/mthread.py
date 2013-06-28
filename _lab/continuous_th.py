import threading
import time

def work():
  """thread worker function"""
  for i in range(5):
    print "This is %s => seq %s" % (threading.currentThread().getName(), i)
    time.sleep(0.1)
  return

if __name__ == "__main__":

  for i in range(10):
    t = threading.Thread(target=work)
    t.start()

  # thread health check and clean up
  while 1:
    if threading.active_count() is 1:
      print "<< All Sub Threads Dead >>"
      break
 
  print "***** END OF MAIN *****" 
  print threading.enumerate()# this is main
