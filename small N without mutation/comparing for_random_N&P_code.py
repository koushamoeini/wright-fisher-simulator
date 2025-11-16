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


N = random.randint(1, 100)
P = random.randint(1, 9) / 10
plt.plot(generation, wright_fisher(N, P, 0, 0), "b", label="N =" + str(N) + ", P =" + str(P))
N = random.randint(1, 100)
P = random.randint(1, 9) / 10
plt.plot(generation, wright_fisher(N, P, 0, 0), "r", label="N =" + str(N) + ", P =" + str(P))

# plot
plt.legend()
plt.show()
