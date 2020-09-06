import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    expl = np.exp(L)
    return np.divide(expl, expl.sum())

def softmax1(L):
    expl = np.exp(L)
    sum_expl = sum(expl)
    ret = []
    for i in expl:
        ret.append(i * 1.0 / sum_expl)
    
    return ret