import SocketServer,sys,re
from mods import Asset, MyOAuth
from conf import conf

class MyHTTPRequestHandler(SocketServer.StreamRequestHandler):

  def handle(self):
    print self.rfile.readline()
    data = self.rfile.readline().strip()
    print data

    oa_url = MyOAuth.get_url()

    # the socond request's path contains GET parameter both oauth_token and oauth_verifier

    # {{{ tmp
    self.wfile.write("HTTP/1.1 200 OK\r\n")
    self.wfile.write("Content-Type: text/html; charset=utf-8\r\n")
    self.wfile.write("\r\n")
    self.wfile.write(Asset('/view/index.html').apply({'oa_url':oa_url}).get())
    # }}}

def is_int_castable(v):
  try:
    int(v)
    return True
  except ValueError:
    return False

if __name__ == "__main__":

  host = "oti10.com"
  port = 9090

  # change port
  if 1 < len(sys.argv) and is_int_castable(sys.argv[1]):
    port = int(sys.argv[1])

  print host, port

  server = SocketServer.TCPServer((host, port), MyHTTPRequestHandler)
  ip, port = server.server_address
  print "IP: %s" % ip
  print "Port: %s" % port

  server.serve_forever()
