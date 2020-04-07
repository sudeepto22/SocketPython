import socket


class Client(object):
    # Buffer Size for receiving a message
    BUFFER_SIZE = 1024

    def __init__(self, ip_address: str, port: int) -> None:
        """
        Constructor
        :param ip_address: ip_address of the server <127.0.0.1>
        :param port: port number of the server <8888>
        """
        self.ip_address: str = ip_address
        self.port: int = port
        self.__client_socket: socket = None

    def connect(self) -> None:
        """
        Creates a client socket object
        Connect to the ip_address with port
        :return: None
        """
        self.__client_socket: socket = socket.socket()
        self.__client_socket.connect((self.ip_address, self.port))

    def send(self, client_message: int) -> None:
        """
        Send data/message to the server
        :param client_message: integer value message
        :return: None
        """
        self.__client_socket.send(bytes(str(client_message), 'utf-8'))

    def receive(self) -> str:
        """
        Receive data/message from the server
        :return: message <str>
        """
        return self.__client_socket.recv(Client.BUFFER_SIZE).decode()


if __name__ == '__main__':
    # Run time variables
    arg_ip_address: str = 'localhost'
    arg_port: int = 9999

    # Client Socket object
    client: Client = Client(ip_address=arg_ip_address, port=arg_port)

    # Connect the client to the server
    client.connect()

    while True:
        try:
            # Integer input from user
            message_send: int = int(input('Enter message (integer) : '))
            break
        except ValueError as value_error:
            # Throw an error when the data/message is a non-integer
            print("Value entered is not an integer")

    # Send message to the server
    client.send(client_message=message_send)

    while True:
        # Receive message from the server
        message_receive: str = client.receive()
        if message_receive:
            print("\nMessages:\n"+message_receive)
            break
