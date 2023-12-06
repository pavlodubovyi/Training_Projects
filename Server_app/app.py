from http.server import HTTPServer, BaseHTTPRequestHandler
import pathlib
import urllib.parse  # для маршрутизації

BASE_DIR = pathlib.Path()


class MyHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        route = urllib.parse.urlparse(self.path)
        match route.path:
            case "/":
                self.send_html('index.html')
            case "/contact":
                self.send_html('contact.html')
            case "/blog":
                self.send_html('blog.html')
            case _:
                my_file = BASE_DIR / route.path[1:]
                print(my_file, f"FILE EXISTS: {my_file.exists()}")
                self.send_html('404.html', 404)

    def send_html(self, filename, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as file:  # відправляємо на всі запити тільки 'index.html'
            self.wfile.write(file.read())


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
