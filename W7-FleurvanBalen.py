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
stat2 = stats.kstest(Z_2, 'norm')[0]
stat10= stats.kstest(Z_10, 'norm')[0]
print('KS-statistiek voor n=2 : ', stat2)
print('KS-statistiek voor n=10 : ', stat10)

# Opdracht 5
n = [x for x in range(1, 26)]
ks_stats = []

for i in n:
    statn= stats.kstest(simuleer(i, 100000), 'norm')[0]
    ks_stats.append(statn)

# Opdracht 6
plt.scatter(n, ks_stats)
plt.title('KS-statistieken tegen n aantal stochasten $X_k$ ~ $Un(0,1)$')
plt.xlabel('$n$')
plt.ylabel('KS-statistiek')
plt.show()

# Opdracht 7
# voor een stochast X_k ~ Exp(1) geldt: verwachting mu = 1 en variantie sigma^2 = 1, dus sigma = 1
mu_exp = 1
sigma_2_exp = 1

def inverse_exp(y):
    return -(np.log(1-y))

def simuleer_exp(n, m): # n is het aantal stochasten en m het aantal getallen
    Z_n = []
    for i in range(m):
        S_n = 0
        for j in range(n):
            S_n += inverse_exp(rd.random()) # Optellen van n X_k stochasten met elk een verdeling volgens Exp(1)
        Z_n.append((S_n-n*mu_exp)/(np.sqrt(sigma_2_exp*n))) # Berekenen van Z_n
    return Z_n

# Simuleer normaalverdeling
Z_2_exp = simuleer_exp(2, 100000)
Z_10_exp = simuleer_exp(10, 100000)

# Tekenen van het histogram met Z_2_exp en Z_10_exp
randen = np.linspace(-3.5, 3.5, 30)
plt.hist([Z_2_exp, Z_10_exp], randen, label=['$n=2$', '$n=10$'])
plt.legend()
plt.title('Simulatie normaalverdeling met $n$ aantal stochasten $X_k$ ~ $Exp(1)$')
plt.xlabel('$Z_n$')
plt.ylabel('Frequentie')
plt.show()

n = [x for x in range(1, 26)]
ks_stats_exp = []

for i in n:
    statn = stats.kstest(simuleer_exp(i, 100000), 'norm')[0]
    ks_stats_exp.append(statn)

# Scatterplot
plt.scatter(n, ks_stats_exp)
plt.title('KS-statistieken tegen n aantal stochasten $X_k$ ~ $Exp(1)$')
plt.xlabel('$n$')
plt.ylabel('KS-statistiek')
plt.show()

