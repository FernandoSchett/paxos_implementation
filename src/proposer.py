import random
import os
import time
from .agent import Agent
from datetime import datetime


class Proposer(Agent):
    def __init__(self, address, acceptors):
        super().__init__(address)
        self.acceptors = acceptors
        self.nodes_number = len(acceptors)
        self.proposal_number = os.getpid()
        self.promises_received = 0  

    def send_prepare_messages(self):
        message = {
            "type": "prepare",
            "proposal_number": self.proposal_number
        }
        print("Sending:", message, datetime.now())
        self.broadcast(message)

    def broadcast(self, message):
        for acceptor in self.acceptors:
            self.send(message, acceptor)

    def start(self):
        "TO DO: Implement the Proposer logic"

        while True:
            prob = self.nodes_number / 100
            if random.randint(0, 100) < prob:
                self.send_prepare_messages()
                while True:
                    message, addr = self.receive()
                    if message["type"] == "promise" and message["proposal_number"] == self.proposal_number:
                        self.promises_received += 1
                        print(f"Received promise from {addr} with proposal {message['proposal_number']}")

                        # Check if the majority has responded
                        if self.promises_received > self.nodes_number // 2:
                            print("Majority reached, proceeding to accept phase.")
                            # Aqui você pode adicionar a lógica para a fase de aceitação (accept phase).
                            self.promises_received = 0
                            break  # Reinicia o ciclo para enviar nova proposta ou continuar o loop
            else:
                time.sleep(5)


