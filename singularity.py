print(">>> singularity.py foi executado <<<")

import time
import socket
import json
import threading
from gravity_core import BlackHole


class Singularity:
    def __init__(self, mass):
        self.black_hole = BlackHole(mass)
        self.storage = []
        self.lock = threading.Lock()
        self.start_time = time.time()  # ⏱️ tempo inicial da singularidade

    def start(self, host="127.0.0.1", port=9000):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(10)

        print("🌌 Singularidade ativa (modo concorrente)...")

        while True:
            conn, addr = server.accept()
            thread = threading.Thread(
                target=self.handle_node,
                args=(conn, addr)
            )
            thread.start()

    def handle_node(self, conn, addr):
        print(f"📡 Conexão aceita de {addr}")

        try:
            data = b""
            while True:
                chunk = conn.recv(1024)
                if not chunk:
                    break
                data += chunk

            payload = json.loads(data.decode())

            # ================================
            # ⏳ DILATAÇÃO TEMPORAL RELATIVÍSTICA
            # ================================

            rs = self.black_hole.schwarzschild_radius()

            # r como múltiplo do raio de Schwarzschild
            r_factor = payload.get("r_factor", 3)
            r = rs * r_factor

            factor = self.black_hole.time_dilation_factor(r)

            base_time = 1.0
            delay = base_time / factor if factor > 0 else 5.0
            delay = min(delay, 5.0)

            print(
                f"⏳ Nó {payload['id']} | "
                f"r={r_factor:.2f} rs | "
                f"fator={factor:.4f} | "
                f"delay={delay:.2f}s"
            )

            time.sleep(delay)

            with self.lock:
                self.absorb(payload)

        except Exception as e:
            print("❌ Erro ao absorver nó:", e)

        finally:
            conn.close()

    def absorb(self, payload):
        elapsed = time.time() - self.start_time
        print(f"🕳️ t={elapsed:.2f}s | Nó {payload['id']} absorvido.")
        self.storage.append(payload)


if __name__ == "__main__":
    s = Singularity(mass=1000)
    s.start()