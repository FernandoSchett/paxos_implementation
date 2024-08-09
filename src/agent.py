"""
Author: Fernando Schettini
Date: 09/08/2024
Purpose: Class model for the agent at Paxos Algorithm. Its should act as proposer, acceptor and learner.
HOW TO USE: from src.agent import Agent
"""


import socket
import random
import os

class Agent:
    def __init__(self):
        self.propose_id = os.getpid()
        self.start_server()
        self.nodes_ports = []
    
    def send_message(port, message):
        print("To do ")

    def start_server(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('localhost', 49152))
        self.sock.listen(1)
        self.port = self.sock.getsockname()[1]

    def propose(self, value):
        for node in self.nodes_ports:
            self.send_message(node, value) 
    
    def start(self):
        while True:
            
            if():
                value = random.randint(0, 100)
                self.propose(value)
