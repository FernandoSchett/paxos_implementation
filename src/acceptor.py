import threading
from .agent import Agent

class Acceptor(Agent):
    def __init__(self, address, learners):
        super().__init__(address)
        self.promised_proposal = None
        self.learners = learners

    def handle_prepare(self, message, proposer_address):
        if self.promised_proposal is None or message["proposal_number"] > self.promised_proposal:
            self.promised_proposal = message["proposal_number"]
            response = {
                "type": "promise",
                "proposal_number": self.promised_proposal
            }
            self.send(response, proposer_address)

    def start(self):
        while True:
            message, addr = self.receive()
            if message["type"] == "prepare":
                self.handle_prepare(message, addr)
