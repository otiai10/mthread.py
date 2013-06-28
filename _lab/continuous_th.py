import threading
import time

def work():
  """thread worker function"""
  for i in range(5):
    print "This is %s => seq %s" % (threading.currentThread().getName(), i)
    time.sleep(0.1)
  return

if __name__ == "__main__":

  threads = []
  for i in range(10):
    t = threading.Thread(target=work)
    threads.append(t)
    t.start()

  # thread health check and clean up
  while 1:
    all_dead = True
    for t in threads:
      if t.is_alive():
        all_dead = False
      else:
        print "%s is dead" % t.getName()
        threads.remove(t)
    if all_dead:
      print "<< All Dead >>"
      break
 
  print "***** END OF MAIN *****" 
  print threads # expected to be [], but "sometimes" it contains dead thread!!
