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
N = random.randint(1, 10000)
P = random.randint(1, 99) / 100
mu1 = random.randint(1, 99) / 100
mu2 = random.randint(1, 99) / 100
plt.plot(generation, wright_fisher(N, P, mu1, mu2), "b",
         label="N =" + str(N) + ", P =" + str(P) + ", mu1 =" + str(mu1) + ", mu2 =" + str(mu2))
N = random.randint(1, 10000)
P = random.randint(1, 99) / 100
mu1 = random.randint(1, 99) / 100
mu2 = random.randint(1, 99) / 100
plt.plot(generation, wright_fisher(N, P, mu1, mu2), "r",
         label="N =" + str(N) + ", P =" + str(P) + ", mu1 =" + str(mu1) + ", mu2 =" + str(mu2))
# plot
plt.legend()
plt.show()
