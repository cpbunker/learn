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


class NeuralNet(object):
    '''
    Neural network parent class that should never be initted
    Just used to define general methods that cen be inherited
    Assumed attributes:
    -layers, 1d array of # neurons in each layer
    -training rate, a float telling the network how aggressively to update
    -network, a list of lists of neurons, organized by layers
    -values, a list of lists of each neuron's firing value
    -errors, a list of list of each neuron's error
    '''

    def __init__(self) -> None:
        raise Exception;

    def fire(self, inpt) -> list:
        '''
        Forward propagate through the neural network
        '''
        if(len(inpt) != self.layers[0]): raise ValueError;

        # input to network
        self.values[0] = inpt;

        # iter thru network
        for i in range(1,len(self.layers)): # iter over layers, skipping input
            for j in range(self.layers[i]): # iter over neurons in layer

                # update value by firing appropriate neuron
                # note that firing input is the entire previous layer of values
                self.values[i][j] = self.network[i][j].fire(self.values[i-1]);

        return self.values[-1]; 

    def backpropagate(self, feature, label) -> float:
        '''
        Update the weights from the output layer backwards to reduce
        the loss function
        Args:
        -feature, 1d array, feature vector
        -label, 1d array, label vector
        '''
        if(not isinstance(feature, np.ndarray)): raise TypeError;
        if(not isinstance(label, np.ndarray)): raise TypeError;
        if(len(feature) != self.layers[0]): raise ValueError;
        if(len(label) != self.layers[-1]): raise ValueError;

        # calculate output
        self.fire(feature); # updates self.values in place

        # mean squared error
        MSE = np.sum(np.power(label - self.values[-1], 2))/len(label);

        # calculate output errors for each neuron
        # has the same structure as self.values: list of layers, list of floats
        # except that it is reversed
        for i in range(len(self.layers)-1, 0, -1): # have to go backwards thru layers
            for j in range(self.layers[i]): # iter over neurons in layer
                #print(" -> ",i,j);
                output = self.values[i][j]; # the output of this neuron
                if(self.is_hidden(i)):
                    next_errors = self.errors[i+1]; # error terms from next layer forwards
                    next_weights = []; # weights that this neuron's output see as input to next layer
                    for next_j in range(self.layers[i+1]): # iter over neurons in next layer
                        # this neuron, the jth in the layer, outputs to the jth weight in the next layer
                        next_weights.append(self.network[i+1][next_j].weights[j]); 
                    error_j = self.values[i][j]*(1-output)*np.dot(next_weights, next_errors);
                    self.errors[i][j] = error_j;
                else: # last layer
                    error_j = output*(1-output)*(label[j] - output);
                    self.errors[i][j] = error_j;

        # update weights using delta rule
        self.update_weights();

        return MSE; # end backpropagate


    #### util functions
                    
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

        return; # end set_weights

    def update_weights(self) -> None:
        for i in range(1,len(self.layers)): # iter over layers, skipping input
            for j in range(self.layers[i]): # iter over neurons in layer
                for k in range(len(self.network[i][j].weights)): # iter over weights
                    x_vec = np.append(self.values[i-1],self.network[i][j].bias); # bias is last input vector
                    self.network[i][j].weights[k] += self.training_rate*self.errors[i][j]*x_vec[k];
        return; # end update_weights

    def print_weights(self) -> None:
        for i in range(1,len(self.layers)): # iter over layers, skipping input
            for j in range(self.layers[i]): # iter over neurons in layer
                print("Layer",i,", neuron",j," weights = ", self.network[i][j].weights);

        return; # end print_weights

    def is_hidden(self,layeri) -> bool: # for readable code
        return (layeri > 0 and layeri < len(self.layers)-1);

class MultiLayerPerceptron(NeuralNet):
    '''
    Neural network formed from multiple Perceptron neurons
    Attributes:
    -layers, 1d array of # neurons in each layer
    -training rate, a float telling the network how aggressively to update
    -network, a list of lists of neurons, organized by layers
    -values, a list of lists of each neuron's firing value
    -errors, a list of list of each neuron's error
     ''' 

    def __init__(self, layers, training_rate) -> None:
        '''
        Args:
        -layers, list of ints, number of nodes/neurons per layer
        '''
        if(not isinstance(layers, list)): raise TypeError;

        # init attributes
        self.layers = np.array(layers);
        self.training_rate = training_rate;

        # set up the network as an array of Perceptron objects
        # such that self.network[i][j] gets the jth neuron in the ith layer
        # and self.values[i][j] is where we store the output of that neuron
        self.network = [];
        self.values = [];
        self.errors = [];
        for i in range(len(self.layers)): # iter over layers
            net_row = [];
            vals_row = [];
            errs_row = [];
            if(i > 0):
                for j in range(self.layers[i]): # iter over neurons in layer
                    net_row.append(Perceptron(self.layers[i-1]));
                    vals_row.append(None);
                    errs_row.append(None);
            self.network.append(net_row);
            self.values.append(vals_row);
            self.errors.append(errs_row);
            del net_row, vals_row, errs_row;


#### test code
if(__name__ == '__main__'):

    # Xor truth table
    X = np.array([[0,0],
                  [0,1],
                  [1,0],
                  [1,1]]);
    y = np.array([[0],[1],[1],[0]]);

    # setup net
    eta = 0.5; # the training rate
    my = MultiLayerPerceptron([2,2,1],eta);
    my.print_weights();

    # train an Xor for 3000 epochs
    num_epochs = 3000;
    MSEvals = np.zeros(num_epochs);
    for i in range(num_epochs):
        MSE = 0;
        for inputi in range(len(y)):
            MSE += my.backpropagate(X[inputi],y[inputi]);
        MSEvals[i] = MSE/4;

    # plot
    import matplotlib.pyplot as plt
    plt.plot(range(num_epochs),MSEvals);
    plt.show(); # looks right!
    
    
    
    




