import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import csv
from scipy.linalg import expm
from qiskit import QuantumCircuit
from qiskit.circuit.library import UnitaryGate
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import random
from qiskit.quantum_info import Operator
import pandas as pd

def quantum_walk_t(A,t,n:int): 
    """
    Creates a quantum circuit for a quantum random walk at a specific time t starting at node n

    """
    # Intialize a quantum circuit
    num_target_qubits = int(np.log2(A.shape[0]))  # Infer target qubits from A
    qc = QuantumCircuit(num_target_qubits)  

    # Convert n to binary
    binary= format(n, f'0{num_target_qubits}b')
    
    # Encode starting node 
    for i, bit in enumerate(reversed(binary)):  # Reverse to match Qiskit's qubit indexing
        if bit == '1':
            qc.x(i)

    # Calculate e^{-iAt}
    i = complex(0, 1)
    U_minus = expm(-i * A * t)  # e^{-iAt}



    qc.unitary(Operator(U_minus), range(num_target_qubits))

    qc.measure_all()

    return qc

def measure_quantum_circuit(qc, simulator: str):
    """
        Runs a simulation of a quantum circuit and returns counts at that point
    """ 
    sim = Aer.get_backend(simulator) 
    result = sim.run(qc).result()
    counts = result.get_counts()
    return counts

def add_max_and_avg(df):
    """
    Adds a row with the maximum value of each column (P-max) and the average of each column (P-avg).
    """
    # Find max values
    p_max = df.drop('Time', axis=1).max()
    
    # Find average values
    p_avg = df.drop('Time', axis=1).mean()

    # Add to DF 
    df.loc[len(df)] = ['P-max'] + p_max.tolist()
    df.loc[len(df)] = ['P-avg'] + p_avg.tolist()
    
    return df


def calculate_possible_nodes(A):
    """
    Calculate the possible nodes based on the number of qubits.
    """
    num_target_qubits = int(np.log2(A.shape[0])) 

    # Generate all possible binary combinations
    possible_nodes = [format(i, f'0{num_target_qubits}b') for i in range(2**num_target_qubits)]
    
    return possible_nodes

def create_results_df(possible_nodes): 
    columns = ['Time'] + possible_nodes
    results_df = pd.DataFrame(columns=columns)
    return results_df

