import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram

def create_circuit():
    qc = QuantumCircuit(3, 3)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(0, 2)
    qc.measure([0, 1, 2], [0, 1, 2])
    return qc

def simulate_circuit(qc, shots=1024):
    simulator = Aer.get_backend('aer_simulator')
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit, shots=shots).result()
    counts = result.get_counts(qc)
    print("Simulation result:", counts)
    return counts

def visualize_results(qc, counts):
    # Plot the quantum circuit
    qc.draw(output='mpl')
    plt.show()

    # Plot the histogram of results
    plot_histogram(counts)
    plt.show()

if __name__ == "__main__":
    qc = create_circuit()
    counts = simulate_circuit(qc, shots=10000)  # Increase the number of shots here
    visualize_results(qc, counts)
