import socket

MAX_PACKET_SIZE = 1024


def start_client(host=socket.gethostname(), port=5000):
    # Create socket
    client_socket = socket.socket()

    # Connect to host and port
    client_socket.connect((host, port))

    # Enter a message from user
    msg = input("Enter a message: ")

    while msg.lower().strip() not in ("bye", "quit", "exit"):
        # Send message
        client_socket.send(msg.encode())

        # Get response
        resp = client_socket.recv(MAX_PACKET_SIZE).decode()

        print("Got as response: {}".format(resp))
        msg = input("Enter a message: ")
    client_socket.close()


if __name__ == "__main__":
    start_client()
