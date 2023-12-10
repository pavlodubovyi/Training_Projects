import socket


def main():
    host = socket.gethostname()
    port = 5002

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen()

    connect, address = server_socket.accept()
    print(f"Connection from: {address}")
    while True:
        in_message = connect.recv(100).decode()
        if not in_message:
            break
        print(f"Message received from client: {in_message}")
        out_message = input("Enter message to client: ")
        connect.send(out_message.encode())
    connect.close()
    server_socket.close()


if __name__ == '__main__':
    print("Launching server")
    main()
