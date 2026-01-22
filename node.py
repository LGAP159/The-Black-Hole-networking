import socket
import json
import threading
import time


class Node:
    def __init__(self, node_id):
        self.node_id = node_id

    def connect(self):
        print(f"🚀 Enviando nó {self.node_id}")

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("127.0.0.1", 9000))

        payload = {
            "id": self.node_id,
            "data": f"estado_no_{self.node_id}",
            "r_factor": self.node_id + 1,
            "local_time": time.time()
        }

        sock.sendall(json.dumps(payload).encode())
        sock.close()


if __name__ == "__main__":
    threads = []

    for i in range(1, 6):
        node = Node(i)
        t = threading.Thread(target=node.connect)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()