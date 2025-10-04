from websockets.sync.client import ClientConnection, connect
from led_driver_mocks.server.server import Server
from json import dumps


class WebSocket(Server):

    server: ClientConnection
    host = None

    def __init__(self, address, port):
        self.connect_to_server(address, port)

    def connect_to_server(self, address, port):
        host = f'{address}:{port}'
        self.server = connect(host)
        print(f'Connected to WebSocket: {host}')

    def send_led_data(self, data):
        self.server.send(dumps({
            'topic': 'led_upadte',
            'data': data
        }))

