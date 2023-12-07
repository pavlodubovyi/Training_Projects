import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import pathlib
import urllib.parse  # для маршрутизації
import mimetypes

BASE_DIR = pathlib.Path()


class MyHTTPHandler(BaseHTTPRequestHandler):

    def do_POST(self):  # what client sends (server gets)

        # body - це те, що нам введуть в полях Імʼя і Повідомлення
        body = self.rfile.read(int(self.headers['Content-Length']))
        new_body = urllib.parse.unquote_plus(body.decode())
        payload = {key: value for key, value in [el.split('=') for el in new_body.split('&')]}
        with open(BASE_DIR.joinpath('storage/data.json'), 'a+', encoding='utf-8') as filo:
            json.dump(payload, filo, indent=2, ensure_ascii=False)  # ensure_ascii=False - щоб json розумів кирилицю
        print(payload)

        self.send_response(302)  # redirect to some page
        self.send_header('location', '/')
        self.end_headers()

    def do_GET(self):  # what client gets (server sends)
        route = urllib.parse.urlparse(self.path)
        match route.path:
            case "/":
                self.send_html('index.html')
            case "/contact":
                self.send_html('message.html')
            case _:
                my_file = BASE_DIR / route.path[1:]
                # print(my_file, f"FILE EXISTS: {my_file.exists()}")
                if my_file.exists():
                    self.send_static(my_file)
                else:
                    self.send_html("error.html", 404)

    def send_html(self, filename, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as file:
            self.wfile.write(file.read())

    def send_static(self, filename):
        absolute_path = BASE_DIR / filename
        print(f'Absolute Path: {absolute_path}')

        self.send_response(200)
        mime_type, _ = mimetypes.guess_type(filename)

        if mime_type:  # if we have assets file
            self.send_header('Content-Type', mime_type)
        else:  # if we don't know what file type
            self.send_header('Content-Type', 'text/plain')  # sending plain text
        self.end_headers()
        with open(filename, 'rb') as file:  # відправляємо files
            self.wfile.write(file.read())


def run(server=HTTPServer, handler=MyHTTPHandler):
    address = ('', 3000)  # '' = localhost
    http_server = server(address, handler)  # http server created
    try:  # http server launched
        print("Starting http server")
        http_server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down http server")
        http_server.server_close()


if __name__ == '__main__':
    run()
