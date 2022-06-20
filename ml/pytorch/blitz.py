'''
https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html
'''

import torch
import torchvision

# some random data
rand_image = torch.rand((1,3,64,64));
rand_label = torch.rand((1,1000));

# a pretrained net
MyModel = torchvision.models.resnet18(pretrained = True);
print("Model = ",MyModel)
MyParams = MyModel.state_dict();
print(" - some example weights:",MyParams['layer4.1.bn2.bias'][:5]);

MyOpt = torch.optim.SGD(MyModel.parameters(), lr=0.01,momentum=0.0); # what to optimize, hyperparams

for dummyi in range(4):

    # forward pass
    outpt = MyModel(rand_image);
    MyOpt.zero_grad();

    # backwards pass
    loss = (outpt - rand_label).sum(); # loss needs to return a scalar, so we .sum()
    assert(loss.requires_grad);  # this means that autograd will compute grads with respect to everything
    loss.backward();             # in the computational graph which contributed to loss, which, via outpt, includes
                                 # the model params, which thus have their .grad atrributes modified here 
    if(dummyi == 0): print(" - after backwards pass:",MyParams['layer4.1.bn2.bias'][:5]);

    # delta rule is done via an optimizer object
    MyOpt.step(); # now use the .grads computed by backwards pass to update
    print(" - after step "+str(dummyi)+"        :",MyParams['layer4.1.bn2.bias'][:5])