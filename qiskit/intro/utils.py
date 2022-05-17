'''
https://github.com/cpbunker/learn/qiskit
'''

import qiskit
from qiskit import QuantumCircuit;
from qiskit.providers.aer import AerSimulator


def output(qc: QuantumCircuit) -> None:
    assert(isinstance(qc, QuantumCircuit))

    # display the circuit
    print(qc.draw(output = "text"));

    # simulate the circuit
    if(len(qc.clbits)):
        job = AerSimulator().run(qc); # physically runs the qc
        jobd = job.result(); # results of simulation stored in dictionary
        print("Out >> ",jobd.get_counts()); 