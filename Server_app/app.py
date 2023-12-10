import json
import logging
import pathlib
import socket
import urllib.parse  # для маршрутизації
import mimetypes
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread

BASE_DIR = pathlib.Path()
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5000  # UDP socket server port. Для внутрішньої комунікації аппки, не для юзерів
BUFFER_SIZE = 1024
APP_PORT = 3000  # для юзерів
OK_RESPONSE = 200
REDIRECT_RESPONSE = 302
ERROR_RESPONSE = 404


def send_data_to_socket(body):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(body, (SERVER_IP, SERVER_PORT)) # відправляю дані на свій сервер
    client_socket.close()


class MyHTTPHandler(BaseHTTPRequestHandler):
    def do_POST(self):  # what client sends (server gets)
        # body - це те, що нам введуть в полях Імʼя і Повідомлення
        body = self.rfile.read(int(self.headers["Content-Length"]))
        # відправляю дані в сокет, який працює на окремому потоці
        send_data_to_socket(body)

        self.send_response(REDIRECT_RESPONSE)  # redirect на index.html після того, як відправились дані у формі
        self.send_header("location", "/")
        self.end_headers()

    def do_GET(self):  # what client gets (server sends)
        route = urllib.parse.urlparse(self.path)
        match route.path:
            case "/":
                self.send_html("index.html")
            case "/contact":
                self.send_html("message.html")
            case _:
                my_file = BASE_DIR / route.path[1:]
                # print(my_file, f"FILE EXISTS: {my_file.exists()}")
                if my_file.exists():
                    self.send_static(my_file)
                else:
                    self.send_html("error.html", ERROR_RESPONSE)

    def send_html(self, filename, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        with open(filename, "rb") as file:
            self.wfile.write(file.read())

    def send_static(self, filename):
        absolute_path = BASE_DIR / filename
        print(f"Absolute Path: {absolute_path}")

        self.send_response(OK_RESPONSE)
        mime_type, _ = mimetypes.guess_type(filename)

        if mime_type:  # if we have assets file
            self.send_header("Content-Type", mime_type)
        else:  # if we don't know what file type
            self.send_header("Content-Type", "text/plain")  # sending plain text
        self.end_headers()
        with open(filename, "rb") as file:  # відправляємо files
            self.wfile.write(file.read())


def run(server=HTTPServer, handler=MyHTTPHandler):
    address = ("", APP_PORT)  # '' = localhost
    http_server = server(address, handler)  # http server created
    try:  # http server launched
        print("Starting http server")
        http_server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down http server")
        http_server.server_close()


def save_data(data):
    new_body = urllib.parse.unquote_plus(data.decode())
    try:
        payload = {}
        for pair in new_body.split("&"):
            key, value = pair.split("=")
            payload[key] = value

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        message_data = {timestamp: {"username": payload.get("username", ""), "message": payload.get("message", "")}}

        with open(BASE_DIR.joinpath("storage/data.json"), "a+", encoding="utf-8") as filo:
            json.dump(message_data, filo, indent=2, ensure_ascii=False)  # ensure_ascii=False - щоб json розумів кирилицю

    except ValueError as err:
        logging.error(f"Failed to parse data {new_body} with error {err}")
    except OSError as err:
        logging.error(f"Failed to write data {new_body} with error {err}")


# створюю сокет-сервер, який приймає дані
def run_socket_server(ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = ip, port
    server_socket.bind(server)
    try:
        while True:
            data, address = server_socket.recvfrom(BUFFER_SIZE)
            save_data(data)
    except KeyboardInterrupt:
        logging.info("Socket server shut down")
    finally:
        server_socket.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")
    thread_server = Thread(target=run)
    thread_server.start()

    thread_socket = Thread(target=run_socket_server, args=(SERVER_IP, SERVER_PORT))
    thread_socket.start()
