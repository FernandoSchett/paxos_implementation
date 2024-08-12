"""
Author: Fernando Schettini
Date: 12/08/2024
Purpose: Main file to execute the Paxos Agent.
HOW TO USE: python3 main.py -a <agent_type> -os <own_socket_address> -s <acceptor_sockets>
            python main.py -a proposer -os 127.0.0.1:10000 -s 127.0.0.1:10001,127.0.0.1:10002
"""

import argparse
from src.proposer import Proposer
from src.acceptor import Acceptor
from src.learner import Learner

def parse_addresses(addresses_str):
    addresses = []
    if addresses_str:
        for addr in addresses_str.split(','):
            ip, port = addr.split(':')
            addresses.append((ip, int(port)))
    return addresses

def gen_agent(args):
    own_address = parse_addresses(args.own_socket)[0]
    com_addresses = parse_addresses(args.sockets)
    
    if args.agent == "proposer":
        agent = Proposer(own_address, com_addresses)
    elif args.agent == "acceptor":
        agent = Acceptor(own_address, com_addresses)
    elif args.agent == "learner":
        agent = Learner(own_address)
    return agent

def main(args):
    print(args)
    agent = gen_agent(args)
    agent.start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Executes Paxos Agent.")
    
    parser.add_argument(
        "-a",
        '--agent',
        type=str,
        choices=['proposer', 'acceptor', 'learner'],
        help="Agent type: ['proposer', 'acceptor' , 'learner']",
        required=True
    )
    
    parser.add_argument(
        "-os",
        "--own_socket",    
        type=str,
        help="Own socket address in format: ip:port",
        required=True
    )
    
    parser.add_argument(
        "-s",
        "--sockets",    
        type=str,
        help="Other sockets addresses in format: ip:port,ip:port,ip:port...."
    )
    
    args = parser.parse_args()
    main(args)
