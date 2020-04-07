import socket


class Server(object):
    # Buffer Size for receiving a message
    BUFFER_SIZE = 1024

    def __init__(self, ip_address: str, port: int, num_of_connections: int) -> None:
        """
        Constructor
        :param ip_address: ip_address of the server <127.0.0.1>
        :param port: port number of the server <8888>
        :param num_of_connections: number of connections you want to make for the server <3>
        """
        self.ip_address: str = ip_address
        self.port: int = port
        self.num_of_connections: int = num_of_connections
        self.__server_socket: socket = None
        self.__clients: list = list()
        self.__messages: list = list()

    def connect(self) -> None:
        """
        Creates a server socket object
        Bind the ip_address with the port number to the server socket object
        Allow only mentioned number of connections from the instance object
        :return: None
        """
        self.__server_socket: socket = socket.socket()
        self.__server_socket.bind((self.ip_address, self.port))
        self.__server_socket.listen(self.num_of_connections)

    def communicate(self):
        """
        Communication between Server socket and Client socket
        Receive message from the client
        Populate the client to clients list and message to messages list
        :return: None
        """
        client_socket, client_address = self.__server_socket.accept()
        self.__clients.append(client_socket)
        message: str = client_socket.recv(Server.BUFFER_SIZE).decode()
        self.__messages.append("{}: {}".format(client_address[0] + ":" + str(client_address[1]), message))
        print("Connected with {} with message: {}".format(client_address[0] + ":" + str(client_address[1]), message))

    def get_clients(self) -> list:
        """
        Get the list of clients connected to the server
        :return: client_list <list>
        """
        return self.__clients

    def get_messages(self) -> list:
        """
        Get the list of messages from all the clients connected to the server
        :return: message_list <list>
        """
        return self.__messages


if __name__ == '__main__':
    # Run time variables
    arg_ip_address: str = 'localhost'
    arg_port: int = 9999
    arg_num_of_connections: int = 3

    # Server Socket object
    server = Server(ip_address=arg_ip_address, port=arg_port, num_of_connections=arg_num_of_connections)

    # Connect the server
    server.connect()

    while True:
        # Communicate between server and client
        server.communicate()

        # Get Client list
        clients = server.get_clients()

        # Get Message list
        messages = server.get_messages()

        # Check if number of clients or number of messages is equal to number of connections asked for
        if len(clients) == arg_num_of_connections or len(messages) == arg_num_of_connections:
            for client in clients:
                # Send data to all the clients in the list
                client.send(bytes('\n'.join(messages), 'utf-8'))
            break
