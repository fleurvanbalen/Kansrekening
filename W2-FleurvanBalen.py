import random as rd
import matplotlib.pyplot as plt
import numpy as np

### Opdracht 1
# Trek willekeurige getallen
getallen1 = []
for _ in range(1000):
    worp1 = rd.randrange(1, 7, 1)
    worp2 = rd.randrange(1, 7, 1)
    getallen1.append(worp1 + worp2)

# Definieer de rander van de balken in het histogram
randen1 = np.linspace(1.5, 12.5, 12) # waarden van X = { de integers van 2 t/m 12 }

# Maak het histogram en laat het zien
plt.hist(getallen1, randen1)
plt.title('Opdracht 1')
plt.xlabel('X(\u03c9)')
plt.ylabel('Frequentie')
plt.show()

### Opdracht 2
# Trek willekeurige getallen
getallen2 = []
for _ in range(10000):
    # Parameters van het vaasmodel zonder terugleggen
    N = 40 # aantal objecten
    n = 5 # succes objecten
    r = 15 # aantal keer trekken
    X = 0 # aantal successen
    for i in range(r):
        greep = rd.randrange(1, N+1, 1)
        N -= 1
        if greep <= n:
            X += 1
            n -= 1
    getallen2.append(X)

# Definieer de rander van de balken in het histogram
randen2 = np.linspace(-0.5, 5.5, 7) # waarden van X = { 0, ..., 5 }

# Maak het histogram en laat het zien
plt.hist(getallen2, randen2)
plt.title('Opdracht 2')
plt.xlabel('X(\u03c9)')
plt.ylabel('Frequentie')
plt.show()

### Opdracht 3
# Trek willekeurige getallen
getallen3 = []
for _ in range(100000):
    X = 0 # aantal worpen
    succesworp = False
    while not succesworp:
        worp = rd.randrange(1, 7, 1)
        if worp == 6:
            succesworp = True
        X += 1
    getallen3.append(X)

# Definieer de rander van de balken in het histogram
randen3 = np.linspace(0.5, 60.5, 61) # waarden van X = { 1, 2, 3, ... }, ik heb ervoor gekozen de histogram t/m 60 te laten zien

# Maak het histogram en laat het zien
plt.hist(getallen3, randen3)
plt.title('Opdracht 3')
plt.xlabel('X(\u03c9)')
plt.ylabel('Frequentie')
plt.show()

### Opdracht 4
# Maak het histogram en laat het zien
plt.hist(getallen3, randen3)
plt.title('Opdracht 4')
plt.xlabel('X(\u03c9)')
plt.ylabel('Frequentie')
plt.yscale('log')
plt.show()