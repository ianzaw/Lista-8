import numpy as np
import matplotlib.pyplot as plt

r0 = 100  # kapitał początkowy
lam = 0.5  # intensywność procesu Poissona
k = 10          # parametr w rozkładzie wykładniczym
proloss = -1  # współczynnik zysku/straty
czas_max = 250  # maksymalny czas

def p(t):
    return proloss * np.e**(-t)

time = 0            # początkowy czas jest równy 0
kapital = r0        # początkowy kapitał jest równy r0
capitals = [kapital] # lista kapitałów
times = [time]      # lista czasów


while time < czas_max:
    # krok czasu do następnego zdarzenia procesu Poissona
    skok = np.random.exponential(1 / lam)
    time += skok

    # aktualizujemy kapitał (zysk albo strata)
    kapital += proloss * skok

    # skok w procesie Poissona
    if np.random.rand() < lam * skok:
        damage = np.random.exponential(1/k)
        kapital -= damage

    # zapisujemy wyniki
    times.append(time)
    capitals.append(kapital)

    # jeśli kapitał spadnie poniżej 0,
    # kończymy symulację
    if kapital < 0:
        break

# tworzymy wykres
plt.figure(figsize=(12, 6))
plt.plot(times, capitals, label='Kapitał firmy')
plt.xlabel('Czas')
plt.ylabel('Kapitał')
plt.title('Kapitał firmy ubezpieczeniowej')
plt.legend(loc = 'upper left')
plt.grid()
plt.show()