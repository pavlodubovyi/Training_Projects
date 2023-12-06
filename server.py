from http.server import HTTPServer, BaseHTTPRequestHandler

html = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Test html</title>
</head>
<body>
<h1>Hello, Pavlo</h1>
<div class="test">Test</div>
</body>
</html>
"""


class MyHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        self.wfile.write(html.encode())


def run(server=HTTPServer, handler=MyHTTPHandler):
    address = ('', 5001)  # '' = localhost
    http_server = server(address, handler)  # http server created
    try:  # http server launched
        print("Starting http server")
        http_server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down http server")
        http_server.server_close()


if __name__ == '__main__':
    run()
