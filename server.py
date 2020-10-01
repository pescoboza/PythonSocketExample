import socket

MAX_PACKET_SIZE = 1024


def start_server(host=socket.gethostname(), port=5000):
    # Create server socket
    server_socket = socket.socket()
    server_socket.bind((host, port))

    # Set number of simultaneous clients
    print("Awaiting for connection...")
    server_socket.listen(1)

    # Accept new connection
    connection, address = server_socket.accept()

    print("Connection from: {}".format(address))

    while True:
        data = connection.recv(MAX_PACKET_SIZE).decode()
        if not data:
            break
        # Display message from user
        print("Received from user: {}".format(str(data)))

        # Make a response to user
        data = input("Enter response for client: ")
        connection.send(data.encode())

    connection.close()


if __name__ == "__main__":
    start_server()
