'''
https://github.com/cpbunker/learn/qiskit
'''

# qiskit
import qiskit
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# visualization
import matplotlib.pyplot as plt
plt.rcParams.update({"text.usetex": True,"font.family": "Times"})
from qiskit.visualization import plot_bloch_multivector

# define the register
nqs = 2; # number of qubits
print("Basis vectors: |00>,|01>, |10>, |11> (|q1, q0>)");

# initialize the |00> state
ket = Statevector.from_int(0,nqs**2); # input is binary digit and dimensionality
print(ket); # recall qiskit basis vectors are labelled from last qubit to first

# take to |01>
qc_x_0 = QuantumCircuit(nqs); qc_x_0.x(0);
ket = ket.evolve(qc_x_0); print("> x(0)");
print(ket);

# controlled X on q1
qc_cx_01 = QuantumCircuit(nqs); qc_cx_01.cx(0,1); #qubit 0 control, 1 target
ket = ket.evolve(qc_cx_01); print("> cx(0,1)");
print(ket);

# hadamard
qc_h_0 = QuantumCircuit(nqs); qc_h_0.h(0);
ket = ket.evolve(qc_h_0); print("> h(0)");
print(ket);

# state vector to bloch sphere
plot_bloch_multivector(ket);
plt.show();
