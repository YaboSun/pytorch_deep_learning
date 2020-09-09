import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    ret = 0.0
    Y = np.float_(Y)
    P = np.float_(P)
    ret = -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))

    return ret