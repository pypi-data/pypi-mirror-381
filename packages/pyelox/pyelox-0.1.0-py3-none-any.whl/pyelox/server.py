import socket
import threading

class PyEloxServer:
    def __init__(self, app_core, host, port):
        self.app = app_core
        self.host = host
        self.port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        self._socket.bind((self.host, self.port))
        self._socket.listen(5)
        print(f"PyElox Is Running in: http://{self.host}:{self.port}")

        try:
            while True:
                client_connection, _ = self._socket.accept()
                client_handler = threading.Thread(
                    target=self.handle_connection,
                    args=(client_connection,)
                )
                client_handler.start()
        except KeyboardInterrupt:
            self._socket.close()
            print("\nPyElox Server Shutdown.")

    def handle_connection(self, client_connection):
        try:
            raw_request = client_connection.recv(4096)
            
            if not raw_request:
                return

            self.app.process_request(raw_request, client_connection)
            
        except Exception:
            pass
        finally:
            client_connection.close()