import random as rd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Opdracht 1: Een functie voor m aantal getallen Z_n
# voor een stochast X_k ~ Un(0,1) geldt: verwachting mu = 0,5 en variantie sigma^2 = 1/12, dus sigma = sqrt(1/12)
mu = 0.5
sigma_2 = 1.0/12.0

def simuleer(n, m): # n is het aantal stochasten en m het aantal getallen
    Z_n = []
    for i in range(m):
        S_n = 0
        for j in range(n):
            S_n += rd.random() # Optellen van n X_k stochasten met elk een verdeling volgens Un(0,1)
        Z_n.append((S_n-n*mu)/(np.sqrt(sigma_2*n))) # Berekenen van Z_n
    return Z_n

# Opdracht 2: Simuleer normaalverdeling
Z_2 = simuleer(2, 100000)
Z_10 = simuleer(10, 100000)

# Opdracht 3: Tekenen van het histogram met Z_2 en Z_10
randen = np.linspace(-3.5, 3.5, 30)
plt.hist([Z_2, Z_10], randen, label=['$n=2$', '$n=10$'])
plt.legend()
plt.title('Simulatie normaalverdeling met $n$ aantal stochasten $X_k$ ~ $Un(0,1)$')
plt.xlabel('$Z_n$')
plt.ylabel('Frequentie')
plt.show()

# Opdracht 4
stat2, p2 = stats.kstest(Z_2, 'norm')
stat10, p10 = stats.kstest(Z_10, 'norm')
print('KS-statistiek voor n=2 : ', stat2)
print('KS-statistiek voor n=10 : ', stat10)

# Opdracht 5
n = [x for x in range(1, 26)]
ks_stats = []

for i in n:
    statn, pn = stats.kstest(simuleer(i, 100000), 'norm')
    ks_stats.append(statn)

# Opdracht 6
plt.scatter(n, ks_stats)
plt.title('KS-statistieken tegen n aantal stochasten $X_k$ ~ $Un(0,1)$')
plt.xlabel('$n$')
plt.ylabel('KS-statistiek')
plt.show()

# Opdracht 7