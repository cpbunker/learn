'''
https://pytorch.org/tutorials/beginner/basics/intro.html

Classify images of apparel in the FashionMNIST data set using a neural network
'''

import os
import torch
from torch import nn

class ImageClassifier(nn.Module):
    '''
    torch.nn.Module is the base class for all user defined neural nets in PyTorch
    '''

    def __init__(self,num_pixels,num_classes,num_hid = 512):
        '''
        Args:
        -num_pixels, int, the number of pixels in the input image
        -num-classes, int, the number of output classes
        -num_hid, the number of neurons in each of the 2 hidden layers
        '''
        if(not isinstance(num_pixels, int)): raise TypeError;
        if(not isinstance(num_classes, int)): raise TypeError;
        if(not isinstance(num_hid, int)): raise TypeError;

        # super calls the parent, a temp torch.nn.Module object
        super(ImageClassifier, self).__init__(); # children of nn.Module must always init the parent first, or get AttributeError                              

        # define the neural network layers
        self.stack = nn.Sequential( 
            nn.Linear(num_pixels,num_hid), # weighted sum over inputs, all pixel inpts -> num_hid hidden layer neurons
            nn.ReLU(), # activation
            nn.Linear(512,512), 
            nn.ReLU(), # activation
            nn.Linear(512,10), # num_hid hidden inputs -> 10 outputs (for 10 classifier categories)
        )

        # for nn.Module models it is more natural to implement methods as attributes
        self.predict = nn.Softmax(dim=1);
        self.loss_fn = nn.CrossEntropyLoss(); 

    def forward(self, inpt):
        '''
        forward defines how the net processes input data
        must define this for all children of nn.module, but should never be called directly
        instead for obj = class(), input data as obj(data) 
        '''

        # have to convert 2d images into 1d inputs
        inpt = nn.Flatten()(inpt);
        
        # run thru the net
        return self.stack(inpt);

    
