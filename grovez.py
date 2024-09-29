from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt  # Import matplotlib to control the plot window

def grovers_algorithm():
    qc = QuantumCircuit(2, 2)
    qc.h([0, 1])
    qc.cz(0, 1)
    qc.h([0, 1])
    qc.measure([0, 1], [0, 1])
    return qc

def simulate_grovers(qc):
    try:
        simulator = AerSimulator()
        compiled_circuit = transpile(qc, simulator)
        result = simulator.run(compiled_circuit, shots=1024).result()
        counts = result.get_counts(qc)
        plot_histogram(counts).show()
        plt.show()  # Add this line to keep the plot window open
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    qc = grovers_algorithm()
    simulate_grovers(qc)
