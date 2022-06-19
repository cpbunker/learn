'''
Linkedin learning: training neural networks in python

Test user defined neural network objects by building logic gates
'''
from objects import *
import numpy as np
import itertools

# implement and gate
print("\nAndGate:");
AndGate = Perceptron(2);
AndGate.set_weights([100,100,-150]);
for inpt in itertools.product([0,1],[0,1]):
    output = AndGate.fire(inpt);
    print(inpt," -> ","{0:.4f}".format(output));

# implement or gate
print("\nOrGate:");
OrGate = Perceptron(2);
OrGate.set_weights([100,100,-50]);
for inpt in itertools.product([0,1],[0,1]):
    output = OrGate.fire(inpt);
    print(inpt," -> ","{0:.4f}".format(output));

# implement xor gate
# we will need two layer of perceptrons for this
# input layer is still two bits
# first layer (hidden layer) is a nand and an or with same input
# output layer is an and
print("\nXorGate");
XorGate = MultiLayerPerceptron([2,2,1]);
XorWeights = [[-100,-100,150],[100,100,-50],[100,100,-150]]; # nand, or, and
XorGate.set_weights(XorWeights);
for inpt in itertools.product([0,1],[0,1]):
    output = XorGate.fire(inpt);
    print(inpt," -> ","{0:.4f}".format(output));
