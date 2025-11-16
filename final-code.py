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


# wright fisher without mutation
plt.plot(generation, wright_fisher(10000, 0.7, 0, 0), "r", label="N=10000,p=0.7,mu1=0,mu2=0")
plt.plot(generation, wright_fisher(100, 0.7, 0, 0), "b", label="N=100,p=0.7,mu1=0,mu2=0")
for k in range(0, 5):
    plt.plot(generation, wright_fisher(10000, 0.7, 0, 0), "r")
    plt.plot(generation, wright_fisher(100, 0.7, 0, 0), "b")

# wright fisher with mutation
plt.plot(generation, wright_fisher(100, 0.3, 0.7, 0.3), color='orange', label="N=100,p=0.3,mu1=0.7,mu2=0.3")
plt.plot(generation, wright_fisher(10000, 0.3, 0.05, 0.1), "g", label="N=10000,p=0.3,mu1=0.05,mu2=0.1")
for k in range(0, 5):
    plt.plot(generation, wright_fisher(100, 0.3, 0.7, 0.3), color='orange')
    plt.plot(generation, wright_fisher(10000, 0.3, 0.05, 0.1), "g")
# plot
plt.title("wright_fisher model")
plt.xlabel("generation")
plt.ylabel("allele-frequency")
plt.legend()
plt.show()
