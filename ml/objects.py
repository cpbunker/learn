'''
Linkedin learning: training neural networks in python

User defined neural network objects
'''

import numpy as np

class Neuron(object):
    '''
    Computational neuron which takes N inputs x_0 ... x_i ... x_N-1
    outputs according to \sum_i w_i x_i where w_i are the weights, ie there is no activation function
    Atributes:
    -weights, 1d array of floats w_0 ... w_N where w_N is the bias weight
    -bias, float, the bias, by convention is one, and we adjust with weights[-1]
    '''

    def __init__(self, weights) -> None:
        if( not isinstance(weights, list)): raise TypeError;

        self.weights = np.array(weights); # like the slope
        self.bias = 1; # like the y intercept

    def activate(self, number) -> float:
        '''
        Activation function, designed to be overwritten by child classes
        '''

        return number;

    def fire(self, input) -> float:
        '''
        Fire neuron based on given input, designed to not be overwritten
        '''
        if( len(input) != len(self.weights) - 1): raise ValueError;

        return self.activate(np.dot(input, self.weights[:-1]) + self.bias*self.weights[-1]);

    def plot_with_labels(self, data, mytitle = "") -> None:

        # create continuous label for each data
        labels = np.zeros(len(data));
        for i in range(len(data)):
            labels[i] = self.fire(data[i]);

        # discretize labels
        labels = labels > 0;

        # plot
        plt.scatter(data[:,0], data[:,1],c=labels);
        plt.title(mytitle);
        plt.show();


class Perceptron(Neuron):
    '''
    computational neuron with a logistic activation function and weights randomized between [-1,1]
    inherits from Neuron class
    '''

    def __init__(self, N) -> None:
        '''
        Initialize with random weights
        Args:
        -N, int, number of inputs. We will need N+1 weights, last is for bias
        '''
        self.weights = 2*np.random.rand(N+1) - 1; # between [-1,1]
        self.bias = 1;

    def activate(self, number) -> float: 
        '''
        logistic activation function
        '''

        return 1/(1+np.exp(-number));

    def set_weights(self, weights) -> None:
        if(not isinstance(weights, list)): raise TypeError;
        if(len(self.weights) != len(weights)): raise ValueError;

        self.weights = np.array(weights);


class MultiLayerPerceptron(object):
    '''
    A neural network formed from multiple Perceptron neurons
    Attributes:
    -layers, 1d array of # neurons in each layer
    ''' 

    def __init__(self, layers) -> None:
        '''
        Args:
        -layers, list of ints, number of nodes/neurons per layer
        '''
        if(not isinstance(layers, list)): raise TypeError;

        # init attributes
        self.layers = np.array(layers);

        # set up the network as an array of Perceptron objects
        # such that self.network[i][j] gets the jth neuron in the ith layer
        # and self.values[i][j] is where we store the output of that neuron
        self.network = [];
        self.values = [];
        for i in range(len(self.layers)): # iter over layers
            net_row = [];
            vals_row = [];
            if(i > 0):
                for j in range(self.layers[i]): # iter over neurons in layer
                    net_row.append(Perceptron(self.layers[i-1]));
                    vals_row.append(None);
            self.network.append(net_row);
            self.values.append(vals_row);
            del net_row, vals_row;

    def fire(self, input) -> float:
        '''
        Forward propagate through the neural network
        '''
        if(len(input) != self.layers[0]): raise ValueError;

        # input to network
        self.values[0] = input;

        # iter thru network
        for i in range(1,len(self.layers)): # iter over layers, skipping input
            for j in range(self.layers[i]): # iter over neurons in layer

                # update value by firing appropriate neuron
                # note that firing input is the entire previous layer of values
                self.values[i][j] = self.network[i][j].fire(self.values[i-1]);

        return self.values[-1][0];

    def set_weights(self, weights) -> None:
        '''
        write weights into each individual neuron
        '''
        if(not isinstance(weights, list)): raise TypeError;
        if(len(weights) != sum(self.layers[1:])): raise ValueError;

        weightsi = 0;
        for i in range(1,len(self.layers)): # iter over layers, skipping input
            for j in range(self.layers[i]): # iter over neurons in layer
                self.network[i][j].set_weights(weights[weightsi]); # set weights to this neuron
                weightsi += 1; # better be in correct order!

    def print_weights(self) -> None:
        for i in range(1,len(self.layers)): # iter over layers, skipping input
            for j in range(self.layers[i]): # iter over neurons in layer
                print("Layer",i,", neuron",j," weights = ", self.network[i][j].weights);




#### test code
if(__name__ == '__main__'):
    pass;
    




