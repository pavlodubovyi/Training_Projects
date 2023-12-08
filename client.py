import socket


def main():
    host = socket.gethostname()
    port = 5002

    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = input("Input message to server: ")
    while message.lower().strip() != 'exit':
        client_socket.send(message.encode())
        msg_from_server = client_socket.recv(1024).decode()
        print(f"Received message from server: {msg_from_server}")
        message = input("Input message to server: ")

    client_socket.close()


if __name__ == '__main__':
    main()
