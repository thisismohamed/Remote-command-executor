import socket

PORT = 8080
BUFFER_SIZE = 1024

def main():
    # create a tcp socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Set a server address
    server_socket.bind(("127.0.0.1", PORT))
    server_socket.listen(3)

    print("Server listening on port {}...".format(PORT))

    client_socket, client_address = server_socket.accept()

    print("Client Connected...")

    while True:
        command = input("Enter command: ")
        client_socket.send(command.encode())
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
