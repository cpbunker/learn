'''
Linkedin learning: training neural networks in python

Demonstrate user defined neural network objects by building an
Optical Character Recognition (OCR) network
'''
from net import *
import numpy as np

# construct ocr
# should have 7 inputs for the 7 lightable display segments
# should have 10 outputs for the 10 digits on [0,9]
# ie we classify w/ one hot encoding: each output class is a different dimension in vector space
# aactivation function should be
num_in = 7
num_digits = 10;
eta = 0.5;
OCR = MultiLayerPerceptron([num_in,num_in,num_digits],eta);

# idealized images for digits (abc... encoding)
data = np.array([[1,1,1,1,1,1,0],
                 [0,1,1,0,0,0,0],
                 [1,1,0,1,1,0,1],
                 [1,1,1,1,0,0,1],
                 [0,1,1,0,0,1,1],
                 [1,0,1,1,0,1,1],
                 [1,0,1,1,1,1,1],
                 [1,1,1,0,0,0,0],
                 [1,1,1,1,1,1,1],
                 [1,1,1,1,0,1,1]]);
labels = np.eye(num_digits); # one hot                

# train the net
epochs = np.array(range(100));
MSEvals = np.zeros_like(epochs, dtype = float);
for i in epochs:
    MSE = 0;
    for digiti in range(num_digits):
        MSE += OCR.backpropagate(data[digiti], labels[digiti]);
    MSE = MSE / num_digits; # avg
    MSEvals[i] = MSE;

# visualize the MSE
import matplotlib.pyplot as plt
plt.plot(epochs, MSEvals);
plt.show();
