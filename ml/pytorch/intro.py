'''
https://pytorch.org/tutorials/beginner/basics/intro.html

Classify images of apparel in the FashionMNIST data set using a neural network
'''

from intro_net import ImageClassifier # the neural network class we defined in intro_net.py

import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor

import numpy as np
import matplotlib.pyplot as plt

#### top level
verbose = 5;
img_shape = (28,28);
batch_size = 64;
labels_map = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}

# importing the fashion mnist data set
train_data = datasets.FashionMNIST(root="data", train = True, download = True, transform = ToTensor());
test_data = datasets.FashionMNIST(root="data", train = False, download = True, transform = ToTensor());

# DataLoaders process data in minibatches for efficiency
train_loader = DataLoader(train_data, batch_size = batch_size, shuffle = True);
test_loader = DataLoader(test_data, batch_size = batch_size, shuffle = True);

# instantiate model
device = "cpu"
MyModel = ImageClassifier(img_shape[0]*img_shape[1], len(labels_map)).to(device);
print("Model = ",MyModel);

# model hyperparameters
epochs = np.array(range(1));
eta = 1e-3;

# in pytorch, we train model thru an optimizer object
MyOpt = torch.optim.SGD(MyModel.parameters(), lr = eta); # init with net weights and learning rate

def train_loop(loader, model,optimizer):
    for batchi, (inpt, label) in enumerate(loader):

        # compute loss
        outpt = model(inpt);
        loss = model.loss_fn(outpt, label); # loss is a tensor object with a grad_fn def'd so it can backprop

        # backpropagate
        optimizer.zero_grad();
        loss.backward();
        optimizer.step();

        # print some info to terminal
        if(batchi % 100 == 0):
            print("- loss = ","{0:.4f}".format(loss.item()))

def test_loop(loader, model):
    loss_count, correct_count = 0,0;

    with torch.no_grad(): # avoid saving autograd info, since we don't have to here
        for inpt, label in loader:
            outpt = model(inpt);
            loss_count += model.loss_fn(outpt, label).item(); # just want the number since no backprop to do
            correct_count += (outpt.argmax(1) == label).type(torch.float).sum().item(); # again just a number

        # normalize counts
        loss_count /= len(loader);
        correct_count /= len(loader.dataset);
        print("- test avg loss = ", "{0:.4f}".format(loss_count));
        print("- test accuracy = ","{0:.4f}".format(correct_count));

for epochi in epochs:
    print(f"\nEpoch {epochi}\n-------------------------------")
    train_loop(train_loader, MyModel, MyOpt);
    test_loop(test_loader, MyModel);

# saving and loading the model
torch.save(MyModel, 'intro_model.pth');