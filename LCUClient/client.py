import socket
from .lcu_pb2 import LcuAnnounce, LcuClientMessage, LcuResponseMessage, Success
from google.protobuf.wrappers_pb2 import StringValue

AARDANT_MESSAGE_LENGTH_BYTES = 4
AARDANT_MESSAGE_LENGTH_ENDIAN = "big"


class LCUClient(object):
    def __init__(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip_address = "34.136.227.69"
        self.port = 8000
        self.conn.connect((self.ip_address, self.port))

    def status(self):
        pass

    def register(self, id: str, message: str):
        """
        Register a resource on the network

        :param id: The ID of the resource, str
        :param message: The registration message, str

        :returns: LcuResponseMessage indicating registration success
        """
        id = StringValue(value=id)
        description = StringValue(value=message)
        proto_msg = LcuClientMessage(
            lcu_announce=LcuAnnounce(id=id, description=description)
        )
        msg_bytes = proto_msg.SerializeToString()
        self.send(msg_bytes)
        response = self.recv()
        return LcuResponseMessage.FromString(response)

    def post(self, message: bytes):
        pass

    def get_hash_preimage(hash: str):
        pass

    def recv(self):
        """
        Receives a response using the aardant wire protocol from the connection to the remote LCU.

        :returns: bytes, the received data
        """
        message_length_bytes = self.conn.recv(AARDANT_MESSAGE_LENGTH_BYTES)
        message_length = int.from_bytes(
            message_length_bytes, AARDANT_MESSAGE_LENGTH_ENDIAN
        )

        buf = bytearray(message_length)
        pos = 0
        while pos < message_length:
            n = self.conn.recv_into(memoryview(buf)[pos:])
            if n == 0:
                raise EOFError(bytes(buf[:pos]), message_length)
            pos += n

        return bytes(buf)

    def send(self, message):
        """
        Sends a message using the aardant wire protocol to the remote LCU

        :param message: str A message to send
        """
        message_length = len(message)
        message_length_bytes = message_length.to_bytes(
            AARDANT_MESSAGE_LENGTH_BYTES, AARDANT_MESSAGE_LENGTH_ENDIAN
        )

        self.conn.sendall(message_length_bytes)
        self.conn.sendall(message)
