import random

import numpy as np
from matplotlib import pyplot as plt

numOfGenes = 100
generation = range(0, numOfGenes + 1)


def wright_fisher(N, prob, mu1, mu2):
    # without mutation-->mu1=mu2=0
    ProbOf_a_Genes = []
    for i in range(0, numOfGenes + 1):
        ProbOf_a_Genes.append(prob)
        prob = (1 - mu1) * prob + mu2 * (1 - prob)
        prob = np.random.binomial(2 * N, prob) / (2 * N)
    return ProbOf_a_Genes


for i in range(1, 5):
    N = 100  # your input
    P = 0.3  # your input
    plt.subplot(2, 2, i)
    plt.plot(generation, wright_fisher(N, P, 0, 0))

# plot
plt.show()
