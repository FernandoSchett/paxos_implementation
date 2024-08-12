#!/bin/bash

#   Author: Fernando Schettini 
#   Description: This script runs Paxos Algorithm with a given number of nodes.
#   How to run: ./run_experiment.sh <num_nodes>

# Kill all running processes
pkill -f main.py
sleep 2

num_nodes=$1
start_port=5000

proposer_add=()
acceptor_add=()
learner_add=()

# Generate addresses for each node
for i in $(seq 0 $(($num_nodes-1)))
do
    proposer_port=$(($start_port + $i))
    acceptor_port=$(($proposer_port + $num_nodes))
    learner_port=$(($acceptor_port + $num_nodes))

    proposer_add+=("127.0.0.1:${proposer_port}")
    acceptor_add+=("127.0.0.1:${acceptor_port}")
    learner_add+=("127.0.0.1:${learner_port}")
done

all_acceptor_addresses=$(IFS=, ; echo "${acceptor_add[*]}")
all_learner_addresses=$(IFS=, ; echo "${all_learner_addresses[*]}")

# Start nodes
for i in $(seq 0 $(($num_nodes-1)))
do
    nohup python3 main.py -a proposer -os ${proposer_add[$i]} -s ${all_acceptor_addresses} > proposer_${proposer_add[$i]}.log 2>&1 &
    nohup python3 main.py -a acceptor -os ${acceptor_add[$i]} -s ${all_learner_addresses} > acceptor_${acceptor_add[$i]}.log 2>&1 &
    nohup python3 main.py -a learner -os ${learner_add[$i]} > learner_${learner_add[$i]}.log 2>&1 &
done

echo "Proposers: ${proposer_add[@]}"
echo "Acceptors: ${acceptor_add[@]}"
echo "Learners: ${learner_add[@]}"
