import SocketServer
# ...
import socket
import time
import threading

class MyHTTPRequestHandler(SocketServer.StreamRequestHandler):

  def handle(self):
    print self.rfile.readline().strip()

    cur_thread = threading.currentThread()

    f = open("assets/view/index.html",'r')

    # {{{ tmp
    self.wfile.write("HTTP/1.1 200 OK\r\n")
    self.wfile.write("Content-Type: text/html; charset=utf-8\r\n")
    self.wfile.write("\r\n")
    self.wfile.write(f.read())
    f.close()
    # }}}

    for i in range(0,10):
      print cur_thread.getName(), ' seq-> ', i
      time.sleep(1)
    print "--- This is End of %s" % cur_thread.getName()

class ThreadedHTTPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
  pass

if __name__ == "__main__":

  HOST, PORT = "oti10.com", 9090

  server = ThreadedHTTPServer((HOST,PORT), MyHTTPRequestHandler)
  ip, port = server.server_address

  server_thread = threading.Thread(target=server.serve_forever)
  server_thread.setDaemon(True)
  server_thread.start()

  print "Server loop running in thread:", server_thread.getName()
  print "IP: %s" % ip
  print "Port: %s" % port

  # time.sleep(60)
  time.sleep(10)
  print '**** END OF MAIN ***'
