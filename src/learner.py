from .agent import  Agent
import threading

class Learner(Agent):
    def __init__(self, address):
        super().__init__(address)

    def start(self):
        while True:
            message, addr = self.receive()
            if message["type"] == "accepted":
                print(f"Learned value: {message['value']} from {addr}")

