import random

import numpy as np
from matplotlib import pyplot as plt

numOfGenes = 100
generation = range(0, numOfGenes + 1)


def wright_fisher(N, prob, mu1, mu2):
    ProbOf_a_Genes = []
    for i in range(0, numOfGenes + 1):
        ProbOf_a_Genes.append(prob)
        prob = (1 - mu1) * prob + mu2 * (1 - prob)
        prob = np.random.binomial(2 * N, prob) / (2 * N)
    return ProbOf_a_Genes


# wright fisher with mutation
plt.plot(generation, wright_fisher(20, 0.3, 0, 0),
         "b", label="non-mutated")  # your input
plt.plot(generation, wright_fisher(20, 0.3, 0.1, 0.18), "r",
         label="mutated")  # your input
# plot
plt.legend()
plt.show()
