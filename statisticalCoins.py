# lets make a code to aproach the statistical distribution of the launch of 1000 coins.
# # We will use a binomial distribution to model the number of heads in 1000 coin flips.
# we will launch 1000 coins and count the number of heads and tails.
import numpy as np  
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.special import factorial



def simulate_coin_flips(n_flips=1000, n_trials=10000):
    """Simulate flipping n_flips coins for n_trials times."""
    results = np.random.binomial(n_flips, 0.5, n_trials)
    return results

def bimodal_distribution():
    n_flips = 1000
    p = 0.5
    k = np.arange(0, n_flips + 1)  # Valores enteros posibles de caras

    # Usamos la fórmula del coeficiente binomial con factoriales:
    # P(k) = C(n, k) * p^k * (1-p)^(n-k)
    # C(n, k) = n! / (k! * (n-k)!)
    coef = factorial(n_flips) / (factorial(k) * factorial(n_flips - k))
    f = coef * (p ** k) * ((1 - p) ** (n_flips - k))

    plt.figure(figsize=(10, 6))
    plt.plot(k, f, label='Binomial Distribution (manual)', color='green')
    plt.title('Binomial Distribution (n=1000, p=0.5) - Manual Calculation')
    plt.xlabel('Number of Heads')
    plt.ylabel('Probability')
    plt.xlim(0, n_flips)
    plt.ylim(0, 0.25)
    plt.grid()
    plt.legend()
    plt.show()


def plot_coin_flip_distribution(results, n_flips=1000):
    """Plot the distribution of heads in coin flips."""
    plt.figure(figsize=(10, 6))
    plt.hist(results, bins=np.arange(0, n_flips + 1) - 0.5, density=True, alpha=0.7, color='blue', edgecolor='black')
    
    # Plot the theoretical binomial distribution
    x = np.arange(0, n_flips + 1)
    pmf = binom.pmf(x, n_flips, 0.5)
    plt.plot(x, pmf, 'r-', lw=2, label='Theoretical PMF', color='orange')
    
    plt.title(f'Distribution of Heads in {n_flips} Coin Flips (Over {len(results)} Trials)')
    plt.xlabel('Number of Heads')
    plt.ylabel('Probability')
    plt.xticks(np.arange(0, n_flips + 1, 50))
    plt.grid()
    plt.legend()
    plt.show()

def main():
    n_flips = 1000  # Number of coins flipped each trial
    n_trials = 10000  # Number of trials to simulate
    
    # Simulate coin flips
    results = simulate_coin_flips(n_flips, n_trials)
    
    # Plot the distribution of results
    plot_coin_flip_distribution(results, n_flips)
    print(f"Simulated {n_trials} trials of flipping {n_flips} coins each.")
    print(f"Mean number of heads: {np.mean(results)}")
    print(f"Standard deviation of heads: {np.std(results)}")
    print(f"Expected mean: {n_flips * 0.5}, Expected std: {np.sqrt(n_flips * 0.5 * 0.5)}")
    print(f"95% Confidence Interval: [{np.mean(results) - 1.96 * np.std(results) / np.sqrt(n_trials)}, {np.mean(results) + 1.96 * np.std(results) / np.sqrt(n_trials)}]")
    print(f"99% Confidence Interval: [{np.mean(results) - 2.576 * np.std(results) / np.sqrt(n_trials)}, {np.mean(results) + 2.576 * np.std(results) / np.sqrt(n_trials)}]")


bimodal_distribution()


# main()
# This code simulates flipping 1000 coins for 10000 trials and plots the distribution of heads. 
# It also calculates the mean, standard deviation, and confidence intervals for the number of heads observed. 
# The theoretical binomial distribution is overlaid on the histogram for comparison.
# The expected mean and standard deviation are also printed for reference.# The results should show a normal distribution centered around 500 heads, with the spread determined by the standard deviation.
# The confidence intervals give an idea of the variability in the results.  