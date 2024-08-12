"""
Author: Fernando Schettini
Date: 09/08/2024
Purpose: Class model for the agent at Paxos Algorithm. Its should act as proposer, acceptor and learner.
HOW TO USE: from .agent import Agent
"""

import socket
import pickle

class Agent:
    def __init__(self, address):
        self.address = address
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(self.address)

    def send(self, message, dest_address):
        self.socket.sendto(pickle.dumps(message), dest_address)

    def receive(self):
        data, addr = self.socket.recvfrom(1024)
        return pickle.loads(data), addr

    def start(self):
        raise NotImplementedError("O método start deve ser implementado nas classes derivadas.")
