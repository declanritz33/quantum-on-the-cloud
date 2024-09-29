from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np

# Function to initialize the qubits in superposition
def initialize_s(qc, qubits):
    for q in qubits:
        qc.h(q)
    return qc

def oracle(qc, qubits, target_pattern):
    """Oracle for matching the target pattern"""
    # Apply X gates to flip qubits based on the target pattern
    for i, bit in enumerate(target_pattern):
        if bit == '0':
            qc.x(qubits[i])
    
    # Multi-controlled X gate (Toffoli)
    qc.mcx(list(qubits[:-1]), qubits[-1])  # Convert range to list
    
    # Flip back the qubits using X gate
    for i, bit in enumerate(target_pattern):
        if bit == '0':
            qc.x(qubits[i])
    return qc


# Diffusion operator
def diffusion_operator(qc, qubits):
    """Apply the Grover diffusion operator"""
    # Apply H and X gates
    qc.h(qubits)
    qc.x(qubits)
    
    # Apply multi-controlled X (Toffoli gate)
    qc.h(qubits[-1])  # H-gate on the last qubit
    qc.mcx(list(qubits[:-1]), qubits[-1])  # Convert range to list for mcx
    qc.h(qubits[-1])  # Apply H-gate again on the last qubit

    # Undo X and H gates
    qc.x(qubits)
    qc.h(qubits)
    return qc


# Number of qubits (for a simple example, adjust as needed)
n = 5  # Change based on the number of bits representing the pattern
qc = QuantumCircuit(n, n)

# Initialize the qubits
initialize_s(qc, range(n))

# Define target pattern, e.g., '00011' (corresponds to some sequence)
target_pattern = '00011'

# Apply Grover's algorithm
iterations = int(np.floor(np.pi / 4 * np.sqrt(2**n)))
for _ in range(iterations):
    oracle(qc, range(n), target_pattern)
    diffusion_operator(qc, range(n))

# Measure the qubits
qc.measure(range(n), range(n))

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit, shots=1024).result()
counts = result.get_counts(qc)

# Plot the results
plot_histogram(counts).show()
plt.show()