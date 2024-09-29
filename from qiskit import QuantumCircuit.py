from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def create_circuit():
    qc = QuantumCircuit(3, 3)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(0, 2)
    qc.measure([0, 1, 2], [0, 1, 2])
    return qc

def simulate_circuit(qc):
    simulator = Aer.get_backend('aer_simulator')
    compiled_circuit = transpile(qc, simulator)
    result = simulator.run(compiled_circuit).result()
    counts = result.get_counts(qc)
    print("Simulation result:", counts)
    return counts

def visualize_results(counts):
    qc.draw(output='mpl')
    plt.show()

    plot_histogram(counts).show()
    plt.show()

if __name__ == "__main__":
    qc = create_circuit()
    counts = simulate_circuit(qc)
    visualize_results(counts)
