from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def grovers_algorithm():
    # Create a quantum circuit with 2 qubits and 2 classical bits
    qc = QuantumCircuit(2, 2)
    # Apply Hadamard gates to both qubits
    qc.h([0, 1])
    # Apply a controlled-Z gate
    qc.cz(0, 1)
    # Apply Hadamard gates again
    qc.h([0, 1])
    # Measure the qubits
    qc.measure([0, 1], [0, 1])
    return qc

def simulate_grovers(qc):
    try:
        # Initialize the simulator
        simulator = AerSimulator()
        # Transpile the circuit for the simulator
        compiled_circuit = transpile(qc, simulator)
        # Run the simulation
        result = simulator.run(compiled_circuit, shots=1024).result()
        # Get the counts of the results
        counts = result.get_counts(qc)
        # Plot the histogram of the results
        plot_histogram(counts).show()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Create the Grover's algorithm circuit
    qc = grovers_algorithm()
    # Simulate the circuit
    simulate_grovers(qc)
