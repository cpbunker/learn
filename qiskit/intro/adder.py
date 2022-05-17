'''
https://github.com/cpbunker/learn/qiskit

https://learn.qiskit.org/course/introduction/the-atoms-of-computation
'''

import utils

import qiskit
from qiskit import QuantumCircuit;

##################################################################################
# circuits for simple tasks

def prep_number(n: int) -> QuantumCircuit:
    '''
    Takes a decimal number and represents it as binary quantum circuit
    '''
    assert(isinstance(n,int));

    # convert to binary string
    n = bin(n)[2:]; # removes the 0b prefix

    # circuit size based on number of bits
    nbits = len(n);
    qc = QuantumCircuit(nbits, nbits);

    # prep state
    # remember qiskit qubits are numbered from last to first
    for biti in range(nbits):
        if(n[biti] == '1'):
            qc.x(nbits - (1+biti));

    return qc;


def half_adder(n1: int, n2: int) -> int:
    '''
    use a quantum circuit to add two single bit binary integers
    '''
    assert(n1 in [0,1] and n2 in [0,1]);

    # first bit of each number is input to halfadder
    input = int(str(n1) + str(n2), 2); # in binary !
    input_circ = prep_number(int(input));

    # half adder circuit
    halfadder = QuantumCircuit(4,2);
    halfadder.cx(0,2);
    halfadder.cx(1,2);
    halfadder.ccx(0,1,3); # toffoli
    halfadder.measure([2,3],[0,1]);

    # compose two circuits together
    qc = QuantumCircuit(len(halfadder.qubits), len(halfadder.clbits)); # zeros like
    qc.compose(input_circ, qubits = list(range(len(input_circ.qubits))), clbits = list(range(len(input_circ.clbits))), inplace = True);
    qc.compose(halfadder, qubits = list(range(len(halfadder.qubits))), clbits = list(range(len(halfadder.clbits))), inplace = True);

    return qc;

##################################################################################
# run code
if(__name__ == '__main__'):
    bits = (1,0);
    myqc = half_adder(*bits);
    print("In >> ", bits);
    utils.output(myqc);