import random as rd
import matplotlib.pyplot as plt
import numpy as np
# Opdracht 2
# De verdelingsfunctie is gedefinieerd voor alle x (Reële getallen) dus het domein van F(x) zijn alle reële getallen
# Voor de inverse geldt: F^-1(y) = -ln(1-y)/a voor y in [0,1]

# Opdracht 3
def inverse1(y, a):
    return -(np.log(1-y))/a

# Opdracht 4
uitvoerInverse1 = []
for i in range(10000):
    uitvoerInverse1.append(inverse1(rd.random(), 2))

# Opdracht 5
def pdf1(x, a):
    return a*np.e**(-a*x)

# Opdracht 6
interval = np.linspace(0,5,101)

# Opdracht 7
uitvoerPdf1 = []
for i in interval:
    uitvoerPdf1.append(pdf1(i, 2))

# Opdracht 8
plt.hist(uitvoerInverse1, 100, density=1)
plt.plot(interval, uitvoerPdf1)
plt.ylabel("Frequentie")
plt.show()

# Opdracht 9
# F(x) = -1/2cos(x) + 1/2 voor 0 < x < pi, F(x) = 0 voor x < 0 en F(x) = 1 voor x > pi
# Gedefinieerd voor alle x dus het domein van F(x) zijn alle reële getallen
# Voor de inverse geldt: F^-1(y) = arccos(-2y+1) voor y in [0,1]

def inverse2(y):
    return np.arccos(-2*y+1)

def pdf2(x):
    if 0 < x < np.pi:
        return 1/2*np.sin(x)
    return 0

uitvoerInverse2 = []
for i in range(10000):
    uitvoerInverse2.append(inverse2(rd.random()))

uitvoerPdf2 = []
for i in interval:
    uitvoerPdf2.append(pdf2(i))

plt.hist(uitvoerInverse2, 100, density=1)
plt.plot(interval, uitvoerPdf2)
plt.ylabel("Frequentie")
plt.show()

# Opdracht 10
uitvoer10 = []
g = 0
for i in range(1000000):
    uitvoer10.append(inverse2(rd.random())+inverse2(rd.random())+inverse2(rd.random()))
    if uitvoer10[i] <= 5:
        g += 1

print(g/len(uitvoer10))
# Geeft P[X+Y+Z<=5] = 0.59...

# plt.hist(uitvoer10, 100, density=1)
# plt.ylabel("Frequentie")
# plt.show()


