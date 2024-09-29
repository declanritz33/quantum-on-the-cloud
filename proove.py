from qiskit import Aer

# Test if the Aer backend is available
simulator = Aer.get_backend('qasm_simulator')
print("Aer backend is working:", simulator)

