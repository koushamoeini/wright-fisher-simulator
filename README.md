# Wright-Fisher Simulator

A Python implementation of the Wright-Fisher model for simulating genetic drift and allele frequency changes in populations over multiple generations. This simulator explores how population size, initial allele frequencies, and mutation rates affect the evolution of genetic diversity.

## 📋 Overview

The Wright-Fisher model is a fundamental concept in population genetics that describes how allele frequencies change from one generation to the next due to random sampling (genetic drift) and mutation. This project provides various simulations to visualize and compare different scenarios.

## ✨ Features

- **Core Wright-Fisher Implementation**: Discrete-time stochastic model for allele frequency evolution
- **Flexible Parameters**: Customize population size (N), initial allele frequency (p), and mutation rates (μ₁, μ₂)
- **Mutation Support**: Simulate both neutral evolution and evolution with bidirectional mutation
- **Visualization**: Generate clear plots showing allele frequency trajectories over generations
- **Comparative Analysis**: Compare different parameter combinations side-by-side
- **Multiple Scenarios**:
  - Small vs. large population effects
  - With and without mutation
  - Different mutation rate combinations
  - Random parameter exploration

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- NumPy
- Matplotlib

### Installation

1. Clone the repository:
```bash
git clone https://github.com/koushamoeini/wright-fisher-simulator.git
cd wright-fisher-simulator
```

2. Install required packages:
```bash
pip install numpy matplotlib
```

Or using conda:
```bash
conda install numpy matplotlib
```

## 💻 Usage

### Basic Usage

Run the main simulator:
```bash
python final-code.py
```

This will generate a plot comparing:
- Large population (N=10,000) vs. small population (N=100) without mutation
- Effects of mutation with different parameter combinations

### Wright-Fisher Function

```python
import numpy as np

def wright_fisher(N, prob, mu1, mu2):
    """
    Simulate the Wright-Fisher model.
    
    Parameters:
    -----------
    N : int
        Population size (number of diploid individuals)
    prob : float
        Initial allele frequency (0 to 1)
    mu1 : float
        Mutation rate from allele A to allele a
    mu2 : float
        Mutation rate from allele a to allele A
    
    Returns:
    --------
    list : Allele frequencies over generations
    """
    ProbOf_a_Genes = []
    for i in range(numOfGenes + 1):
        ProbOf_a_Genes.append(prob)
        prob = (1 - mu1) * prob + mu2 * (1 - prob)
        prob = np.random.binomial(2 * N, prob) / (2 * N)
    return ProbOf_a_Genes
```

### Example Simulations

**Without Mutation (Genetic Drift Only):**
```bash
cd "small N without mutation"
python normal_plotting_code.py
```

**With Mutation:**
```bash
cd "with mutation"
python normal_plotting_code.py
```

**Comparing Different Parameters:**
```bash
cd "big N without mutation"
python "comparing for_random N&P-code.py"
```

## 📊 Experimental Scenarios

### 1. **Small Population (N < 1000) without Mutation**
- Demonstrates strong genetic drift
- Rapid fixation or loss of alleles
- High stochasticity between runs

### 2. **Large Population (N ≥ 10,000) without Mutation**
- Slower drift dynamics
- More stable allele frequencies
- Demonstrates effect of effective population size

### 3. **With Mutation**
- Balancing between drift and mutation
- Equilibrium allele frequencies
- Effect of mutation rate on genetic diversity

### 4. **Comparative Studies**
- Side-by-side comparison of parameter effects
- Random parameter exploration
- Population size vs. mutation rate trade-offs

## 🔬 Theoretical Background

The Wright-Fisher model assumes:
- Non-overlapping generations
- Random mating
- Constant population size
- No selection (neutral evolution)
- Optional mutation

The allele frequency in generation t+1 is sampled from a binomial distribution:
$$X_{t+1} \sim \text{Binomial}(2N, p_t')$$

Where $p_t'$ is the frequency after mutation:
$$p_t' = (1-\mu_1)p_t + \mu_2(1-p_t)$$

## 📁 Project Structure

```
wright-fisher-simulator/
├── final-code.py                          # Main simulation script
├── small N without mutation/              # Small population experiments
│   ├── normal_plotting_code.py
│   ├── comparing for_random_N&P_code.py
│   └── comparing_N=100,P=0,7&&N=20,P=0.3_code.py
├── big N without mutation/                # Large population experiments
│   ├── normal_plotting_code.py
│   ├── comparing for_random N&P-code.py
│   └── comparing N=10000,P=0.4&&N=2000,P=0.5.py
├── with mutation/                         # Mutation experiments
│   ├── normal_plotting_code.py
│   ├── comparing for_random_N&P&MUs_code.py
│   └── comparing_N=200,P=0.7,Mu1=0.1,Mu2=0.18&&N=100,P=0.7,Mu1=0.1,Mu2=0.4.py
├── comparing mutated & non-mutated/       # Comparative analysis
│   └── comparing-code.py
├── long generation/                       # Extended generation simulations
├── final result.jpg                       # Example output visualization
├── result of (mini)research.jpg          # Research findings visualization
├── LICENSE                                # MIT License
└── README.md                              # This file
```

## 🎯 Key Parameters

| Parameter | Symbol | Description | Typical Range |
|-----------|--------|-------------|---------------|
| Population Size | N | Number of diploid individuals | 20 - 10,000+ |
| Initial Frequency | p | Starting allele frequency | 0.0 - 1.0 |
| Mutation Rate (A→a) | μ₁ | Forward mutation rate | 0.0 - 0.5 |
| Mutation Rate (a→A) | μ₂ | Backward mutation rate | 0.0 - 0.5 |
| Generations | t | Number of time steps | 100 - 1000+ |

## 📈 Example Results

The simulations demonstrate key population genetics principles:
- **Genetic Drift**: Random fluctuations stronger in small populations
- **Fixation**: Alleles eventually fix (p=1) or are lost (p=0) without mutation
- **Mutation-Drift Balance**: Stable polymorphism with sufficient mutation
- **Effective Population Size**: Larger N → slower allele frequency changes

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language
- **NumPy**: Numerical computing and random number generation
- **Matplotlib**: Data visualization and plotting

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Kousha Moeini**
- Email: koushamoeini@gmail.com
- GitHub: [@koushamoeini](https://github.com/koushamoeini)

---

## 📚 References

- Wright, S. (1931). Evolution in Mendelian Populations. *Genetics*, 16(2), 97-159.
- Fisher, R. A. (1930). *The Genetical Theory of Natural Selection*. Oxford University Press.
- Ewens, W. J. (2004). *Mathematical Population Genetics*. Springer.


