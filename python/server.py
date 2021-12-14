#!/usr/bin/env python

# Basic REST Server for prototyping

import sys, cgi, BaseHTTPServer, mimetypes

# Port to listen on
PORT = 8086

# List of endpoints
class endpoint:
    mimetype = ""
    content = ""
    def __init__(self,mimetype,content):
        self.mimetype = mimetype
        self.content = content
    
endpoints = {}

# The REST handler
class REST(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Access-Control-Allow-Methods","*")
        self.send_header("Access-Control-Allow-Headers","*")
        self.end_headers()

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Access-Control-Allow-Methods","*")
        self.send_header("Access-Control-Allow-Headers","*")
        self.end_headers()

    def do_GET(self):
        self.path = self.path.split("?",1)[0]
        if self.path in endpoints:
            ep = endpoints[self.path]
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin","*")
            self.send_header("Access-Control-Allow-Methods","*")
            self.send_header("Access-Control-Allow-Headers","*")
            self.send_header("Content-Type", ep.mimetype)
            self.end_headers()
            self.wfile.write(ep.content)

        else:
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin","*")
            self.send_header("Access-Control-Allow-Methods","*")
            self.send_header("Access-Control-Allow-Headers","*")
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write("""<html>
<body>
<form method="post" enctype="multipart/form-data" action=""")
            self.wfile.write('"'+self.path+'"')
            self.wfile.write(""">
<input type="file" name="upload"/><input type="submit" value="Submit">
</form>
</body>
</html>""")

    def do_POST(self):
        self.path = self.path.split("?",1)[0]
        try:
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            form = cgi.FieldStorage( fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD':'POST', 'CONTENT_TYPE':self.headers['Content-Type'], })
            content = form['upload'].file.read()
            filename = form['upload'].filename

            mt = mimetypes.guess_type(form["upload"].filename)[0] or "application/octet-stream"
            endpoints[self.path] = endpoint(mt,content)

            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin","*")
            self.send_header("Access-Control-Allow-Methods","*")
            self.send_header("Access-Control-Allow-Headers","*")
            self.send_header("Content-Type",mt)
            self.end_headers()
            self.wfile.write(content)
        except Exception as e:
            print sys.exc_info()
            self.send_response(500)
            self.send_header("Access-Control-Allow-Origin","*")
            self.send_header("Access-Control-Allow-Methods","*")
            self.send_header("Access-Control-Allow-Headers","*")
            self.end_headers()
            self.wfile.write(e)


if __name__ == '__main__':

    endpoints = {   "/": endpoint("text/plain","Hello world!"),
            "/bye.html": endpoint("text/html","<html><body>Bye</body></html>") 
    }

    print repr(endpoints)

    httpd = BaseHTTPServer.HTTPServer(("",PORT), REST)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()