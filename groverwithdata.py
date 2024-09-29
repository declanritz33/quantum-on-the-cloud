from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt

def initialize_s(qc, qubits):
    """Apply a H-gate to 'qubits' in qc"""
    for q in qubits:
        qc.h(q)
    return qc

def oracle(qc, qubits, target):
    """Oracle that marks the target state (target index)"""
    qc.x(qubits)  # Apply X-gate to all qubits (to set |target>)
    qc.h(qubits[-1])  # Apply H-gate to the last qubit
    qc.mcx(list(qubits[:-1]), qubits[-1])  # Multi-controlled X (Toffoli) to flip the sign
    qc.h(qubits[-1])  # Apply H-gate again
    qc.x(qubits)  # Undo the X-gates
    return qc

def diffusion_operator(qc, qubits):
    """Apply the Grover diffusion operator"""
    qc.h(qubits)
    qc.x(qubits)
    qc.h(qubits[-1])
    qc.mcx(list(qubits[:-1]), qubits[-1])  # Use list() to convert range to list
    qc.h(qubits[-1])
    qc.x(qubits)
    qc.h(qubits)
    return qc

# Setup
n = 3  # Number of qubits (for 8 possible states)
qc = QuantumCircuit(n, n)

# Initialize qubits
initialize_s(qc, range(n))

# Set the target to search for
target_number = 5  # Example target number
target_index = target_number  # Assume numbers 0-7 (for 3 qubits)

# Apply Grover's algorithm
iterations = int(np.floor(np.pi / 4 * np.sqrt(2**n)))
for _ in range(iterations):
    oracle(qc, list(range(n)), target_index)  # Convert to list here as well
    diffusion_operator(qc, list(range(n)))  # Convert to list here as well

# Measure the qubits
qc.measure(range(n), range(n))

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit, shots=1024).result()
counts = result.get_counts(qc)

# Plot the results
plot_histogram(counts)
plt.title("Grover's Algorithm Search Result")
plt.show()
