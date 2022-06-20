'''
Linkedin learning: natural-language-processing-with-pytorch

Use a convolutional neural network (CNN) for text classification
'''

#from text_class_net import CNN

import torch
import random

# data set
import torchtext
train, test = torchtext.datasets.AG_NEWS();
# train, test are both datapipes, meaning you do for datum in train: and datum -> tuple (label, text string)

# process with a SpaCy tokenizer
import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English
mytoken = Tokenizer(English().vocab);

for d in train:
    print(d);
    dummys = mytoken(d[-1]);
    for dum in dummys: print(dum);
    assert False;

