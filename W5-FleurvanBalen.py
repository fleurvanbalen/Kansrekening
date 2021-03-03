import random
import matplotlib.pyplot as plt
import numpy as np

def geef_me_een_getal():
    r = random.random()
    if r < 0.4:
        return 0
    if r < 0.48:
        return 1
    if r < 0.61:
        return 2
    if r < 0.70:
        return 4
    if r < 0.98:
        return 5
    return 7

def geef_me_een_ander_getal():
    r = random.random()
    pcum = 0
    n = 1
    while True:
        pcum += 2 * (3 ** -n)
        if pcum > r:
            return (3**n) / (n**2)
        n += 1

### Opdracht 1: Voer het kansexperiment 200 keer uit en sla de uitkomsten a op in A
A = []
for i in range(200):
    A.append(geef_me_een_getal())

### Opdracht 2: Maak een histogram van de getallen in A
plt.hist(A, np.arange(-0.5, 8.5, 1.0))
plt.xlabel("Getrokken getal")
# plt.savefig('2-histogram-FleurvanBalen.png')
plt.show()

### Opdracht 3: Reken het gemiddelde van A uit m.b.v de zwakke wet van grote getallen
def Gemiddelde_van(A):
    total = 0
    for i in A:
        total += i
    return total / len(A)

print('E(A)   = ', Gemiddelde_van(A)) # Dit geeft bv. 2.305

### Opdracht 4:
# Stochast A heeft de waardeverzameling W = {0, 1, 2, 4, 5, 7} met resp. de kansen P(W) = {0.4, 0.08, 0.13, 0.09, 0.28, 0.02}
# Voor de verwachtingswaarde E(A) geldt volgens Definitie 4.2: E(A) = 0x0.4 + 1x0.08 + 2x0.13 + 4x0.09 + 5x0.28 + 7x0.02 = 2.24
# E(A) = 0x0.4 + 1x0.08 + 2x0.13 + 4x0.09 + 5x0.28 + 7x0.02 = 2.24

### Opdracht 5
n = [x for x in range(25, 10001, 25)] # Maak een lijst met veelvouden van 25 t/m 10.000, dit zijn de waarden voor hoe vaak het kansexperiment moet worden herhaald
def bereken_gemiddeldes(n_waarden): # Een functie om de gemiddeldes van het kansexperiment te berekenen voor verschillende aantallen trekkingen
    gemiddeldes = []
    for i in range(len(n_waarden)): # De loop wordt voor elke waarde in n herhaald
        B = []
        for k in range(n_waarden[i]): # 
            B.append(geef_me_een_getal())
        gemiddeldes.append(Gemiddelde_van(B))
    return gemiddeldes

### Opdracht 6 en 7: Plot de aantal keren het kansexperiment wordt herhaal tegen het berekende gemiddelde
plt.plot(n, bereken_gemiddeldes(n))
plt.plot(n, bereken_gemiddeldes(n))
plt.plot(n, bereken_gemiddeldes(n))
plt.plot(n, bereken_gemiddeldes(n))
plt.plot(n, bereken_gemiddeldes(n))
plt.xlabel("Aantal getrokken getallen")
plt.ylabel('Gemiddelde')
# plt.savefig('7-plot-FleurvanBalen.png')
plt.show()

### Opdracht 8
# In de plot is te zien dat voor meer getrokken getallen (grotere n) de verwachtingswaarde
# langzaam convergeert naar de in opdracht 4 berekende waarde van 2.24

### Opdracht 9
# Voor  = 3 zou je misschien een kans van 2/3 verwachten, want voor n = 1 geldt:
# P[X=3]= 2/3
# Maar voor n = 3 geldt P[X=3]= 2/27. Dus P[X=3]= 2/3 + 2/27 = 20/27 = 0.74074...
# Dit vinden we ook in deze simulatie:
X = []
for i in range(10000):
    X.append(geef_me_een_ander_getal())

print('P[X=3] = ', X.count(3)/10000) # Geeft bv. 0.7457

plt.hist(X, np.arange(-0.5, 20.5, 1.0))
plt.xlabel("Getrokken getal")
plt.show()

print('E(X)   = ', Gemiddelde_van(X)) # Geeft bv. 3.40259...

# Voor de bereking van de exacte verwachtingswaarde is een pdf bijgevoegd, het antwoord geeft E(X) = (pi^2)/3 = 3.2895...

def bereken_gemiddeldes_2(n_waarden): 
    gemiddeldes = []
    for i in range(len(n_waarden)):
        B = []
        for k in range(n_waarden[i]):
            B.append(geef_me_een_ander_getal())
        gemiddeldes.append(Gemiddelde_van(B))
    return gemiddeldes

plt.plot(n, bereken_gemiddeldes_2(n))
plt.xlabel("Aantal getrokken getallen")
plt.ylabel('Gemiddelde')
plt.show()

# In deze plot zijn soms grote 'spikes' te zien voor sommige kansexperimenten. Dit heeft te maken
# met het feit dat er altijd een kans is (hoe klein ook) op een willekeurig groot getal. Dit
# betekent dat als je het berekenen van het gemiddelde vaak genoeg herhaald, dat je een lijst krijgt
# met een grote uitschieter, en dit heeft heel veel invloed op het gemiddelde, vooral met
# een laag aantal getrokken getallen.
# In dit geval worden ong. 5000 x (10000/25) = 2x10^6 getallen getrokken voor 1 plot. en met
# bijv. n = 13 krijg je: P[X=9433.49]=1.2544...x10^-6
# De kans is dus redelijk dat daar 1 of meerdere van inzitten, en afhankelijk van het aantal
# getrokken getallen verhoogd dit het gemiddelde met 9433.39../(aantal getrokken getallen).