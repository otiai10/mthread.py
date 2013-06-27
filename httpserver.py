import SocketServer

class MyHTTPRequestHandler(SocketServer.StreamRequestHandler):

  def handle(self):
    print self.rfile.readline()
    data = self.rfile.readline().strip()
    print data

    f = open("assets/view/index.html", 'r')

    # {{{ tmp
    self.wfile.write("HTTP/1.1 200 OK\r\n")
    self.wfile.write("Content-Type: text/html; charset=utf-8\r\n")
    self.wfile.write("\r\n")
    self.wfile.write(f.read())
    # }}}

    f.close()

if __name__ == "__main__":

  HOST, PORT = "oti10.com", 9090

  server = SocketServer.TCPServer((HOST, PORT), MyHTTPRequestHandler)
  ip, port = server.server_address
  print "IP: %s" % ip
  print "Port: %s" % port

  server.serve_forever()
