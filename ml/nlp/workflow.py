'''
NLP with Python for Machine Learning Essential Training
'''

# sms spam data from nlp toolkit
# turn into a panda dataframe
# columns are sms text and spam label
import pandas as pd
#pd.set_option('display.max_colwidth',100);
data = pd.read_csv('SMSSPamCollection.tsv', sep = '\t', header = None);
data.columns = ['label', 'text'];
print(data.head());

# we have correct data format but text is still raw
# preprocessing workflow:
# 1) tokenize: take from long strings to tokens (words/subwords) the model should look at
# 2) clean: remove stop words, punctuation, etc
# 3) vectorize: convert tokens to numeric

# machine learning workflow:
# divide into train, validate, and test sets
# train multiple models
# validate to find best one
# run best model on test set

