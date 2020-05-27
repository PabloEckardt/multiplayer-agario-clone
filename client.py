import socket
import _pickle as pickle


class Network:
    """
    class to connect, send and recieve information from the server

    need to hardcode the host attirbute to be the server's ip
    """

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.client.settimeout(10.0)

        # Add manually
        self.host = ""

        # use this line if running server locally & if server is at that address
        # self.host = "10.0.0.5"

        self.port = 3000
        self.addr = (self.host, self.port)

    def connect(self, name):
        """
        connects to server and returns the id of the client that connected
        :param name: str
        :return: int reprsenting id
        """
        self.client.connect(self.addr)
        self.client.send(str.encode(name))
        val = self.client.recv(8)
        return int(val.decode())  # can be int because will be an int id

    def disconnect(self):
        """
        disconnects from the server
        :return: None
        """
        self.client.close()

    def send(self, data, pick=False):
        """
        sends information to the server

        :param data: str
        :param pick: boolean if should pickle or not
        :return: str
        """
        try:
            if pick:
                self.client.send(pickle.dumps(data))
            else:
                self.client.send(str.encode(data))
            reply = self.client.recv(2048 * 2)
            try:
                reply = pickle.loads(reply)
            except Exception as e:
                # print(e)
                return [] # what can we return instead, if this exception happened, we failed to retrieve data

            return reply
        except Exception as e:
            # print(e)
            return [] # what can we return instead, if this exception happened, we failed to retrieve data
